"""
ETL Pipeline for Seller Catalog Data
This script processes seller catalog data through bronze, silver, and gold layers
with data quality checks and quarantine handling.
"""

import sys
from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col, trim, initcap, when, isnan,
    lower, concat_ws
)
from utils import (
    get_spark_session,
    load_yaml_config,
    parse_arguments,
    write_to_quarantine,
    get_quarantine_path
)


def standardize_category(category_col):
    """
    Standardize category labels to common formats.

    Args:
        category_col: Column containing category values

    Returns:
        Column with standardized category values
    """
    # Normalize to lowercase first, then apply title case
    # Handle common variations
    normalized = lower(trim(category_col))

    # Map common variations to standard labels
    return when(normalized.isin(['electronics', 'electronic', 'elec']), 'Electronics') \
        .when(normalized.isin(['apparel', 'clothing', 'clothes', 'fashion']), 'Apparel') \
        .when(normalized.isin(['home', 'home & garden', 'homegarden', 'home_garden']), 'Home & Garden') \
        .when(normalized.isin(['sports', 'sport', 'sports & outdoors']), 'Sports') \
        .when(normalized.isin(['books', 'book']), 'Books') \
        .when(normalized.isin(['toys', 'toy', 'toys & games']), 'Toys') \
        .when(normalized.isin(['beauty', 'beauty & personal care']), 'Beauty') \
        .when(normalized.isin(['automotive', 'auto', 'car']), 'Automotive') \
        .otherwise(initcap(trim(category_col)))  # Default to title case


def clean_seller_catalog_data(df: DataFrame) -> DataFrame:
    """
    Clean seller catalog data (Silver Layer).

    Performs:
    - Trim whitespace in string columns
    - Normalize casing (item_name → Title Case, category → Standardized)
    - Convert types (marketplace_price → DOUBLE, stock_qty → INT)
    - Fill missing stock_qty with 0
    - Remove duplicates based on (seller_id + item_id)

    Args:
        df: Raw DataFrame from bronze layer

    Returns:
        Cleaned DataFrame
    """
    print("Starting data cleaning (Silver Layer)...")

    # Trim whitespace in string columns
    cleaned_df = df.withColumn("seller_id", trim(col("seller_id"))) \
                   .withColumn("item_id", trim(col("item_id"))) \
                   .withColumn("item_name", trim(col("item_name"))) \
                   .withColumn("category", trim(col("category")))

    # Normalize casing: item_name → Title Case
    cleaned_df = cleaned_df.withColumn("item_name", initcap(col("item_name")))

    # Standardize category labels
    cleaned_df = cleaned_df.withColumn("category", standardize_category(col("category")))

    # Convert types: marketplace_price → DOUBLE, stock_qty → INT
    cleaned_df = cleaned_df.withColumn("marketplace_price",
                                      col("marketplace_price").cast("double")) \
                           .withColumn("stock_qty",
                                      col("stock_qty").cast("int"))

    # Fill missing stock_qty with 0
    cleaned_df = cleaned_df.fillna({"stock_qty": 0})

    # Remove duplicates based on (seller_id + item_id)
    # Keep first occurrence
    cleaned_df = cleaned_df.dropDuplicates(["seller_id", "item_id"])

    print(f"Data cleaning completed. Records after cleaning: {cleaned_df.count()}")
    return cleaned_df


def perform_dq_checks(df: DataFrame, quarantine_path: str) -> DataFrame:
    """
    Perform data quality checks (Gold Layer) and quarantine failed records.

    DQ Checks:
    - seller_id IS NOT NULL
    - item_id IS NOT NULL
    - marketplace_price >= 0
    - stock_qty >= 0
    - item_name IS NOT NULL
    - category IS NOT NULL

    Args:
        df: Cleaned DataFrame from silver layer
        quarantine_path: Base path for quarantine zone

    Returns:
        DataFrame with records that passed all DQ checks
    """
    print("Starting data quality checks (Gold Layer)...")
    dataset_name = "seller_catalog"
    valid_df = df

    # DQ Check 1: seller_id IS NOT NULL
    failed_seller_id = valid_df.filter(col("seller_id").isNull())
    write_to_quarantine(failed_seller_id, quarantine_path, dataset_name, "missing_seller_id")
    valid_df = valid_df.filter(col("seller_id").isNotNull())

    # DQ Check 2: item_id IS NOT NULL
    failed_item_id = valid_df.filter(col("item_id").isNull())
    write_to_quarantine(failed_item_id, quarantine_path, dataset_name, "missing_item_id")
    valid_df = valid_df.filter(col("item_id").isNotNull())

    # DQ Check 3: marketplace_price >= 0 (and not null)
    failed_price = valid_df.filter(
        col("marketplace_price").isNull() |
        isnan(col("marketplace_price")) |
        (col("marketplace_price") < 0)
    )
    write_to_quarantine(failed_price, quarantine_path, dataset_name, "invalid_price")
    valid_df = valid_df.filter(
        col("marketplace_price").isNotNull() &
        ~isnan(col("marketplace_price")) &
        (col("marketplace_price") >= 0)
    )

    # DQ Check 4: stock_qty >= 0 (and not null)
    failed_stock = valid_df.filter(
        col("stock_qty").isNull() |
        (col("stock_qty") < 0)
    )
    write_to_quarantine(failed_stock, quarantine_path, dataset_name, "invalid_stock_qty")
    valid_df = valid_df.filter(
        col("stock_qty").isNotNull() &
        (col("stock_qty") >= 0)
    )

    # DQ Check 5: item_name IS NOT NULL
    failed_item_name = valid_df.filter(col("item_name").isNull())
    write_to_quarantine(failed_item_name, quarantine_path, dataset_name, "missing_item_name")
    valid_df = valid_df.filter(col("item_name").isNotNull())

    # DQ Check 6: category IS NOT NULL
    failed_category = valid_df.filter(col("category").isNull())
    write_to_quarantine(failed_category, quarantine_path, dataset_name, "missing_category")
    valid_df = valid_df.filter(col("category").isNotNull())

    print(f"DQ checks completed. Valid records: {valid_df.count()}")
    return valid_df


def write_to_hudi(df: DataFrame, hudi_output_path: str, table_name: str = "seller_catalog_hudi"):
    """
    Write DataFrame to Hudi table with overwrite mode.

    Args:
        df: DataFrame to write
        hudi_output_path: Output path for Hudi table
        table_name: Name of the Hudi table
    """
    print(f"Writing to Hudi table at {hudi_output_path}...")

    # Create composite record key from seller_id + item_id
    # Hudi requires a single record key field, so we concatenate seller_id and item_id
    df_with_key = df.withColumn("record_key", concat_ws("_", col("seller_id"), col("item_id")))

    # Write to Hudi with overwrite mode
    hudi_options = {
        'hoodie.table.name': table_name,
        'hoodie.datasource.write.recordkey.field': 'record_key',  # Composite key as single field
        'hoodie.datasource.write.partitionpath.field': '',  # No partitioning
        'hoodie.datasource.write.table.type': 'COPY_ON_WRITE',
        'hoodie.datasource.write.operation': 'insert_overwrite_table',  # Overwrite entire table
        'hoodie.datasource.write.precombine.field': 'seller_id',
        'hoodie.cleaner.policy': 'KEEP_LATEST_COMMITS',
        'hoodie.cleaner.commits.retained': 1
    }

    df_with_key.write \
        .format("org.apache.hudi") \
        .options(**hudi_options) \
        .mode("overwrite") \
        .save(hudi_output_path)

    print(f"Successfully wrote {df.count()} records to Hudi table")


def main():
    """Main ETL pipeline execution."""
    # Parse command-line arguments
    args = parse_arguments()
    config_path = args.config

    # Initialize Spark session
    spark = get_spark_session("ETL_Seller_Catalog")

    try:
        # Load configuration
        print(f"Loading configuration from {config_path}...")
        config = load_yaml_config(config_path)
        seller_catalog_config = config.get("seller_catalog", {})

        input_path = seller_catalog_config.get("input_path")
        hudi_output_path = seller_catalog_config.get("hudi_output_path")
        # Use container path for quarantine when running in Docker
        quarantine_path = "/opt/spark/work-dir/quarantine"

        if not input_path or not hudi_output_path:
            raise ValueError("Missing required configuration: input_path or hudi_output_path")

        print(f"Input path: {input_path}")
        print(f"Hudi output path: {hudi_output_path}")
        print(f"Quarantine path: {quarantine_path}")

        # Bronze Layer: Read raw data from CSV
        print("\n=== Bronze Layer: Reading raw data ===")
        bronze_df = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(input_path)

        print(f"Raw records read: {bronze_df.count()}")
        print("Schema:")
        bronze_df.printSchema()

        # Silver Layer: Data cleaning
        print("\n=== Silver Layer: Data cleaning ===")
        silver_df = clean_seller_catalog_data(bronze_df)

        # Gold Layer: DQ checks and quarantine
        print("\n=== Gold Layer: Data quality checks ===")
        gold_df = perform_dq_checks(silver_df, quarantine_path)

        # Write to Hudi
        print("\n=== Writing to Hudi table ===")
        write_to_hudi(gold_df, hudi_output_path)

        print("\n=== ETL Pipeline completed successfully ===")

    except Exception as e:
        print(f"Error in ETL pipeline: {str(e)}", file=sys.stderr)
        raise
    finally:
        spark.stop()


if __name__ == "__main__":
    main()

