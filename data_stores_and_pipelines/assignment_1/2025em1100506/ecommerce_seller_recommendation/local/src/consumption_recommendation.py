
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
    """Read a Hudi table from the specified path."""
    df = spark.read.format("org.apache.hudi").load(hudi_path)
    return df


def aggregate_company_sales(company_sales_df: DataFrame) -> DataFrame:
    """Aggregate company sales data."""
    aggregated = company_sales_df.groupBy("item_id") \
        .agg(
            spark_sum("units_sold").alias("total_units_sold"),
            spark_sum("revenue").alias("total_revenue")
        )
    return aggregated


def get_top_items_per_category(company_sales_df: DataFrame, top_n: int = 10) -> DataFrame:
    """Get top N items from company sales."""
    aggregated = company_sales_df.groupBy("item_id") \
        .agg(
            spark_sum("units_sold").alias("total_units_sold"),
            spark_sum("revenue").alias("total_revenue")
        )

    window_spec = Window.orderBy(desc("total_units_sold"))
    top_items = aggregated.withColumn("rank", row_number().over(window_spec)) \
        .filter(col("rank") <= top_n) \
        .drop("rank")

    return top_items


def aggregate_competitor_sales(competitor_sales_df: DataFrame) -> DataFrame:
    """Aggregate competitor sales data."""
    aggregated = competitor_sales_df.groupBy("item_id") \
        .agg(
            spark_sum("units_sold").alias("total_units_sold"),
            spark_sum("revenue").alias("total_revenue"),
            avg("marketplace_price").alias("avg_marketplace_price"),
            count("seller_id").alias("num_sellers")
        )
    return aggregated


def identify_missing_items(
    seller_catalog_df: DataFrame,
    company_top_items: DataFrame,
    competitor_top_items: DataFrame
) -> DataFrame:
    """Identify items missing from each seller's catalog."""
    seller_items = seller_catalog_df.select("seller_id", "item_id").distinct()
    all_sellers = seller_catalog_df.select("seller_id").distinct()

    company_missing = all_sellers.crossJoin(
        company_top_items.select("item_id")
    ).join(
        seller_items,
        ["seller_id", "item_id"],
        "left_anti"
    ).withColumn("source", lit("company"))

    competitor_missing = all_sellers.crossJoin(
        competitor_top_items.select("item_id")
    ).join(
        seller_items,
        ["seller_id", "item_id"],
        "left_anti"
    ).withColumn("source", lit("competitor"))

    missing_items = company_missing.union(competitor_missing).distinct()
    return missing_items


def calculate_recommendations(
    missing_items_df: DataFrame,
    seller_catalog_df: DataFrame,
    company_sales_df: DataFrame,
    competitor_sales_df: DataFrame,
    company_top_items: DataFrame,
    competitor_aggregated: DataFrame
) -> DataFrame:
    """Calculate recommendation metrics for missing items."""
    item_metadata = seller_catalog_df.select("item_id", "item_name", "category") \
        .distinct() \
        .groupBy("item_id") \
        .agg(
            spark_max("item_name").alias("item_name"),
            spark_max("category").alias("category")
        )

    competitor_price_df = competitor_aggregated.select(
        "item_id",
        col("avg_marketplace_price").alias("market_price")
    )

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

    sellers_per_item = seller_catalog_df.groupBy("item_id") \
        .agg(count("seller_id").alias("num_sellers_catalog"))

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

    expected_units_df = competitor_expected.unionByName(
        company_expected.join(competitor_expected, "item_id", "left_anti"),
        allowMissingColumns=True
    ).groupBy("item_id") \
        .agg(
            spark_max("expected_units_sold").alias("expected_units_sold")
        )

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

    window_spec = Window.partitionBy("seller_id").orderBy(desc("expected_revenue"))
    top_recommendations = recommendations \
        .withColumn("rank", row_number().over(window_spec)) \
        .filter(col("rank") <= 10) \
        .drop("rank")

    return top_recommendations


def write_recommendations_to_csv(df: DataFrame, output_path: str) -> None:
    """Write recommendations DataFrame to CSV."""
    df.coalesce(1).write \
        .mode("overwrite") \
        .option("header", "true") \
        .csv(output_path)


def main():
    """Main consumption pipeline execution."""
    args = parse_arguments()
    config_path = args.config

    spark = get_spark_session("Consumption_Recommendation")

    try:
        config = load_yaml_config(config_path)
        recommendation_config = config.get("recommendation", {})

        seller_catalog_hudi_path = recommendation_config.get("seller_catalog_hudi")
        company_sales_hudi_path = recommendation_config.get("company_sales_hudi")
        competitor_sales_hudi_path = recommendation_config.get("competitor_sales_hudi")
        output_csv_path = recommendation_config.get("output_csv")

        if not all([seller_catalog_hudi_path, company_sales_hudi_path,
                   competitor_sales_hudi_path, output_csv_path]):
            raise ValueError("Missing required configuration in recommendation section")

        seller_catalog_df = read_hudi_table(spark, seller_catalog_hudi_path, "seller_catalog_hudi")
        company_sales_df = read_hudi_table(spark, company_sales_hudi_path, "company_sales_hudi")
        competitor_sales_df = read_hudi_table(spark, competitor_sales_hudi_path, "competitor_sales_hudi")

        company_top_items = get_top_items_per_category(company_sales_df, top_n=10)
        competitor_aggregated = aggregate_competitor_sales(competitor_sales_df)
        competitor_top_items = competitor_aggregated.orderBy(desc("total_units_sold")).limit(10)

        missing_items_df = identify_missing_items(
            seller_catalog_df,
            company_top_items,
            competitor_top_items
        )

        recommendations_df = calculate_recommendations(
            missing_items_df,
            seller_catalog_df,
            company_sales_df,
            competitor_sales_df,
            company_top_items,
            competitor_aggregated
        )

        write_recommendations_to_csv(recommendations_df, output_csv_path)

    except Exception as e:
        print(f"Error in consumption pipeline: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        raise
    finally:
        spark.stop()


if __name__ == "__main__":
    main()

