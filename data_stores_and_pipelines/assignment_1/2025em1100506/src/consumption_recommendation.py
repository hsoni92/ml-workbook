"""
Consumption Pipeline for Seller Recommendations
This script reads Hudi tables from ETL pipelines and generates recommendations
for sellers about top-selling items they don't currently have in their catalog.
"""

import sys
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import (
    col, sum as spark_sum, count, avg, max as spark_max,
    when, isnull, coalesce, row_number, desc, asc, lit
)
from pyspark.sql.window import Window
from utils import (
    get_spark_session,
    load_yaml_config,
    parse_arguments
)


def read_hudi_table(spark: SparkSession, hudi_path: str, table_name: str) -> DataFrame:
    """
    Read a Hudi table from the specified path.

    Args:
        spark: SparkSession instance
        hudi_path: Path to the Hudi table
        table_name: Name of the table (for logging)

    Returns:
        DataFrame containing the Hudi table data
    """
    print(f"Reading Hudi table: {table_name} from {hudi_path}...")
    df = spark.read.format("org.apache.hudi").load(hudi_path)
    print(f"Successfully read {df.count()} records from {table_name}")
    return df


def aggregate_company_sales(company_sales_df: DataFrame) -> DataFrame:
    """
    Aggregate company sales data to find top 10 selling items per category.

    Args:
        company_sales_df: DataFrame containing company sales data

    Returns:
        DataFrame with top 10 items per category, including:
        - item_id
        - category
        - total_units_sold
        - item_name (if available)
    """
    print("Aggregating company sales data...")

    # Group by item_id and calculate total units_sold
    # Note: company_sales may not have category, so we'll need to get it from other sources
    # For now, aggregate by item_id
    aggregated = company_sales_df.groupBy("item_id") \
        .agg(
            spark_sum("units_sold").alias("total_units_sold"),
            spark_sum("revenue").alias("total_revenue")
        )

    print(f"Aggregated company sales: {aggregated.count()} unique items")
    return aggregated


def get_top_items_per_category(company_sales_df: DataFrame, top_n: int = 10) -> DataFrame:
    """
    Get top N items per category from company sales.

    Since company_sales doesn't have category, we'll need to join with other sources.
    For now, return top items overall.

    Args:
        company_sales_df: DataFrame containing company sales data
        top_n: Number of top items per category (default: 10)

    Returns:
        DataFrame with top N items
    """
    # Aggregate by item_id
    aggregated = company_sales_df.groupBy("item_id") \
        .agg(
            spark_sum("units_sold").alias("total_units_sold"),
            spark_sum("revenue").alias("total_revenue")
        )

    # Get top N items by total_units_sold
    window_spec = Window.orderBy(desc("total_units_sold"))
    top_items = aggregated.withColumn("rank", row_number().over(window_spec)) \
        .filter(col("rank") <= top_n) \
        .drop("rank")

    print(f"Top {top_n} items from company sales: {top_items.count()}")
    return top_items


def aggregate_competitor_sales(competitor_sales_df: DataFrame) -> DataFrame:
    """
    Aggregate competitor sales data to find top-selling items in the market.

    Args:
        competitor_sales_df: DataFrame containing competitor sales data

    Returns:
        DataFrame with aggregated competitor sales including:
        - item_id
        - total_units_sold
        - avg_marketplace_price
        - num_sellers (number of sellers selling this item)
    """
    print("Aggregating competitor sales data...")

    # Group by item_id and calculate aggregates
    aggregated = competitor_sales_df.groupBy("item_id") \
        .agg(
            spark_sum("units_sold").alias("total_units_sold"),
            spark_sum("revenue").alias("total_revenue"),
            avg("marketplace_price").alias("avg_marketplace_price"),
            count("seller_id").alias("num_sellers")
        )

    print(f"Aggregated competitor sales: {aggregated.count()} unique items")
    return aggregated


def identify_missing_items(
    seller_catalog_df: DataFrame,
    company_top_items: DataFrame,
    competitor_top_items: DataFrame
) -> DataFrame:
    """
    Identify items that are missing from each seller's catalog but are top-selling.

    Args:
        seller_catalog_df: DataFrame containing seller catalog data
        company_top_items: DataFrame with top items from company sales
        competitor_top_items: DataFrame with top items from competitor sales

    Returns:
        DataFrame with missing items per seller, including:
        - seller_id
        - item_id
        - source (company or competitor)
    """
    print("Identifying missing items per seller...")

    # Get all unique seller-item pairs from catalog
    seller_items = seller_catalog_df.select("seller_id", "item_id").distinct()

    # Get all sellers
    all_sellers = seller_catalog_df.select("seller_id").distinct()

    # Cross join sellers with top items to find missing items
    # Missing from company top items
    company_missing = all_sellers.crossJoin(
        company_top_items.select("item_id")
    ).join(
        seller_items,
        ["seller_id", "item_id"],
        "left_anti"
    ).withColumn("source", lit("company"))

    # Missing from competitor top items
    competitor_missing = all_sellers.crossJoin(
        competitor_top_items.select("item_id")
    ).join(
        seller_items,
        ["seller_id", "item_id"],
        "left_anti"
    ).withColumn("source", lit("competitor"))

    # Union both sets
    missing_items = company_missing.union(competitor_missing).distinct()

    print(f"Identified {missing_items.count()} missing item-seller pairs")
    return missing_items


def calculate_recommendations(
    missing_items_df: DataFrame,
    seller_catalog_df: DataFrame,
    company_sales_df: DataFrame,
    competitor_sales_df: DataFrame,
    company_top_items: DataFrame,
    competitor_aggregated: DataFrame
) -> DataFrame:
    """
    Calculate recommendation metrics for missing items.

    For each missing item per seller:
    - market_price: Get from competitor_sales or company_sales (prefer competitor)
    - expected_units_sold: total units sold / number of sellers selling this item
    - expected_revenue: expected_units_sold * marketplace_price
    - item_name and category: Get from seller_catalog (any seller's entry for this item)

    Args:
        missing_items_df: DataFrame with missing items per seller
        seller_catalog_df: DataFrame containing seller catalog data (for item metadata)
        company_sales_df: DataFrame containing company sales data
        competitor_sales_df: DataFrame containing competitor sales data
        company_top_items: DataFrame with top items from company sales
        competitor_aggregated: DataFrame with aggregated competitor sales

    Returns:
        DataFrame with recommendations:
        - seller_id
        - item_id
        - item_name
        - category
        - market_price
        - expected_units_sold
        - expected_revenue
    """
    print("Calculating recommendation metrics...")
    print("  - Step 5.1: Getting item metadata (item_name, category)...")

    # Get item metadata from seller_catalog (item_name and category)
    # Since items might be in other sellers' catalogs, we can get metadata from any seller
    item_metadata = seller_catalog_df.select("item_id", "item_name", "category") \
        .distinct() \
        .groupBy("item_id") \
        .agg(
            spark_max("item_name").alias("item_name"),
            spark_max("category").alias("category")
        )
    print(f"    Retrieved metadata for {item_metadata.count()} items")

    print("  - Step 5.2: Calculating market_price (prefer competitor, fallback to company)...")
    # Calculate market_price (prefer competitor, fallback to company)
    # Get price from competitor aggregated data
    competitor_price_df = competitor_aggregated.select(
        "item_id",
        col("avg_marketplace_price").alias("market_price")
    )

    # If no competitor price, try to get from company sales
    # For company sales, we don't have marketplace_price, so we'll calculate from revenue/units
    company_price_df = company_sales_df.groupBy("item_id") \
        .agg(
            spark_sum("revenue").alias("total_revenue"),
            spark_sum("units_sold").alias("total_units")
        ).withColumn(
            "market_price",
            when(col("total_units") > 0,
                 col("total_revenue") / col("total_units")
            ).otherwise(lit(0.0))
        ).select("item_id", "market_price")

    # Combine prices (prefer competitor, fallback to company)
    final_market_price = competitor_price_df.unionByName(
        company_price_df.join(competitor_price_df, "item_id", "left_anti"),
        allowMissingColumns=True
    ).groupBy("item_id") \
        .agg(
            coalesce(
                spark_max("market_price"),
                lit(0.0).cast("double")
            ).alias("market_price")
        )
    print(f"    Calculated market_price for {final_market_price.count()} items")

    print("  - Step 5.3: Calculating expected_units_sold = total_units_sold / num_sellers...")
    # Calculate expected_units_sold = total units sold / number of sellers selling this item
    # Count number of sellers from seller_catalog for each item
    sellers_per_item = seller_catalog_df.groupBy("item_id") \
        .agg(count("seller_id").alias("num_sellers_catalog"))

    # For competitor items: use competitor aggregated data (num_sellers from competitor sales)
    competitor_expected = competitor_aggregated.select(
        "item_id",
        col("total_units_sold"),
        col("num_sellers").alias("num_sellers_comp")
    ).withColumn(
        "expected_units_sold",
        when(col("num_sellers_comp") > 0,
             col("total_units_sold") / col("num_sellers_comp")
        ).otherwise(lit(0.0))
    ).select("item_id", "expected_units_sold")

    # For company items: use company aggregated data with seller count from catalog
    company_expected = company_top_items.join(
        sellers_per_item,
        "item_id",
        "left"
    ).withColumn(
        "num_sellers_est",
        when(col("num_sellers_catalog").isNull() | (col("num_sellers_catalog") == 0),
             lit(1.0)
        ).otherwise(col("num_sellers_catalog"))
    ).select(
        "item_id",
        (col("total_units_sold") / col("num_sellers_est")).alias("expected_units_sold")
    )

    # Combine expected units sold (prefer competitor calculation if available)
    expected_units_df = competitor_expected.unionByName(
        company_expected.join(competitor_expected, "item_id", "left_anti"),
        allowMissingColumns=True
    ).groupBy("item_id") \
        .agg(
            spark_max("expected_units_sold").alias("expected_units_sold")
        )
    print(f"    Calculated expected_units_sold for {expected_units_df.count()} items")

    print("  - Step 5.4: Calculating expected_revenue = expected_units_sold * market_price...")

    # Build final recommendations
    print("  - Step 5.5: Combining all metrics into final recommendations...")
    recommendations = missing_items_df \
        .join(item_metadata, "item_id", "left") \
        .join(final_market_price, "item_id", "left") \
        .join(expected_units_df, "item_id", "left") \
        .withColumn(
            "expected_revenue",
            col("expected_units_sold") * col("market_price")
        ) \
        .select(
            "seller_id",
            "item_id",
            coalesce(col("item_name"), lit("Unknown")).alias("item_name"),
            coalesce(col("category"), lit("Unknown")).alias("category"),
            coalesce(col("market_price"), lit(0.0)).alias("market_price"),
            coalesce(col("expected_units_sold"), lit(0.0)).alias("expected_units_sold"),
            coalesce(col("expected_revenue"), lit(0.0)).alias("expected_revenue")
        )

    print(f"  ✓ Recommendation calculation completed: Generated {recommendations.count()} recommendations")
    return recommendations


def write_recommendations_to_csv(df: DataFrame, output_path: str) -> None:
    """
    Write recommendations DataFrame to CSV with overwrite mode.

    Output columns as per PLAN.md:
    - seller_id, item_id, item_name, category, market_price, expected_units_sold, expected_revenue

    Args:
        df: DataFrame containing recommendations
        output_path: Path to output CSV file
    """
    # Verify columns match PLAN.md requirements
    expected_columns = ["seller_id", "item_id", "item_name", "category", 
                       "market_price", "expected_units_sold", "expected_revenue"]
    actual_columns = df.columns

    print(f"  - Verifying output columns...")
    print(f"    Expected: {expected_columns}")
    print(f"    Actual: {actual_columns}")

    if set(actual_columns) != set(expected_columns):
        print(f"    WARNING: Column mismatch detected!")
    else:
        print(f"    ✓ Columns match requirements")

    print(f"  - Writing {df.count()} recommendations to CSV...")

    # Ensure output directory exists by coalescing to single partition
    df.coalesce(1).write \
        .mode("overwrite") \
        .option("header", "true") \
        .csv(output_path)

    print(f"  ✓ Successfully wrote recommendations to {output_path}")


def main():
    """Main consumption pipeline execution."""
    # Parse command-line arguments
    args = parse_arguments()
    config_path = args.config

    # Initialize Spark session
    spark = get_spark_session("Consumption_Recommendation")

    try:
        # Load configuration
        print(f"Loading configuration from {config_path}...")
        config = load_yaml_config(config_path)
        recommendation_config = config.get("recommendation", {})

        seller_catalog_hudi_path = recommendation_config.get("seller_catalog_hudi")
        company_sales_hudi_path = recommendation_config.get("company_sales_hudi")
        competitor_sales_hudi_path = recommendation_config.get("competitor_sales_hudi")
        output_csv_path = recommendation_config.get("output_csv")

        if not all([seller_catalog_hudi_path, company_sales_hudi_path, 
                   competitor_sales_hudi_path, output_csv_path]):
            raise ValueError("Missing required configuration in recommendation section")

        print(f"Seller catalog Hudi path: {seller_catalog_hudi_path}")
        print(f"Company sales Hudi path: {company_sales_hudi_path}")
        print(f"Competitor sales Hudi path: {competitor_sales_hudi_path}")
        print(f"Output CSV path: {output_csv_path}")

        # Step 1: Read Hudi Tables
        print("\n=== Step 1: Reading Hudi Tables ===")
        seller_catalog_df = read_hudi_table(spark, seller_catalog_hudi_path, "seller_catalog_hudi")
        company_sales_df = read_hudi_table(spark, company_sales_hudi_path, "company_sales_hudi")
        competitor_sales_df = read_hudi_table(spark, competitor_sales_hudi_path, "competitor_sales_hudi")

        # Step 2: Aggregate Company Sales (top 10 per category)
        print("\n=== Step 2: Aggregating Company Sales ===")
        company_top_items = get_top_items_per_category(company_sales_df, top_n=10)

        # Step 3: Aggregate Competitor Sales
        print("\n=== Step 3: Aggregating Competitor Sales ===")
        competitor_aggregated = aggregate_competitor_sales(competitor_sales_df)

        # Get top competitor items (top 10 by total units sold)
        competitor_top_items = competitor_aggregated.orderBy(desc("total_units_sold")).limit(10)

        # Step 4: Identify Missing Items
        print("\n=== Step 4: Identifying Missing Items ===")
        missing_items_df = identify_missing_items(
            seller_catalog_df,
            company_top_items,
            competitor_top_items
        )

        # Step 5: Calculate Recommendations
        print("\n=== Step 5: Calculating Recommendations ===")
        recommendations_df = calculate_recommendations(
            missing_items_df,
            seller_catalog_df,
            company_sales_df,
            competitor_sales_df,
            company_top_items,
            competitor_aggregated
        )

        # Step 4: Output (as per PLAN.md)
        print("\n=== Step 4: Output ===")
        print("  - Columns: seller_id, item_id, item_name, category, market_price, expected_units_sold, expected_revenue")
        print(f"  - Writing to CSV with overwrite mode")
        print(f"  - Output path: {output_csv_path}")
        write_recommendations_to_csv(recommendations_df, output_csv_path)

        print("\n=== Consumption Pipeline completed successfully ===")
        print(f"Total recommendations generated: {recommendations_df.count()}")

    except Exception as e:
        print(f"Error in consumption pipeline: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        raise
    finally:
        spark.stop()


if __name__ == "__main__":
    main()

