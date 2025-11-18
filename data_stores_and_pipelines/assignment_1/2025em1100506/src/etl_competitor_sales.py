"""
ETL Pipeline for Competitor Sales Data
This script processes competitor sales data through bronze, silver, and gold layers
with data quality checks and quarantine handling.
"""

import sys
from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col, trim, initcap, isnan, to_date, current_date, concat_ws
)
from utils import (
    get_spark_session,
    load_yaml_config,
    parse_arguments,
    write_to_quarantine,
    get_quarantine_path
)


def clean_competitor_sales_data(df: DataFrame) -> DataFrame:
    """
    Clean competitor sales data (Silver Layer).

    Performs:
    - Trim whitespace in string columns (item_id, seller_id)
    - Normalize casing: seller_id
    - Convert types (units_sold → INT, revenue → DOUBLE, marketplace_price → DOUBLE, sale_date → DATE)
    - Fill missing numeric fields (units_sold, revenue, marketplace_price) with 0
    - Remove duplicates based on (seller_id + item_id)

    Args:
        df: Raw DataFrame from bronze layer

    Returns:
        Cleaned DataFrame
    """
    print("Starting data cleaning (Silver Layer)...")

    # Trim whitespace in string columns
    cleaned_df = df.withColumn("item_id", trim(col("item_id"))) \
                   .withColumn("seller_id", trim(col("seller_id")))

    # Normalize casing: seller_id → Title Case
    cleaned_df = cleaned_df.withColumn("seller_id", initcap(col("seller_id")))

    # Convert types: units_sold → INT, revenue → DOUBLE, marketplace_price → DOUBLE, sale_date → DATE
    cleaned_df = cleaned_df.withColumn("units_sold", col("units_sold").cast("int")) \
                           .withColumn("revenue", col("revenue").cast("double")) \
                           .withColumn("marketplace_price", col("marketplace_price").cast("double")) \
                           .withColumn("sale_date", to_date(col("sale_date"), "yyyy-MM-dd"))

    # Fill missing numeric fields (units_sold, revenue, marketplace_price) with 0
    cleaned_df = cleaned_df.fillna({"units_sold": 0, "revenue": 0, "marketplace_price": 0})

    # Remove duplicates based on (seller_id + item_id)
    # Keep first occurrence
    cleaned_df = cleaned_df.dropDuplicates(["seller_id", "item_id"])

    print(f"Data cleaning completed. Records after cleaning: {cleaned_df.count()}")
    return cleaned_df


def perform_dq_checks(df: DataFrame, quarantine_path: str) -> DataFrame:
    """
    Perform data quality checks (Gold Layer) and quarantine failed records.

    DQ Checks:
    - item_id IS NOT NULL
    - seller_id IS NOT NULL
    - units_sold >= 0
    - revenue >= 0
    - marketplace_price >= 0
    - sale_date IS NOT NULL AND sale_date <= current_date()

    Args:
        df: Cleaned DataFrame from silver layer
        quarantine_path: Base path for quarantine zone

    Returns:
        DataFrame with records that passed all DQ checks
    """
    print("Starting data quality checks (Gold Layer)...")
    dataset_name = "competitor_sales"
    valid_df = df

    # DQ Check 1: item_id IS NOT NULL
    failed_item_id = valid_df.filter(col("item_id").isNull())
    write_to_quarantine(failed_item_id, quarantine_path, dataset_name, "missing_item_id")
    valid_df = valid_df.filter(col("item_id").isNotNull())

    # DQ Check 2: seller_id IS NOT NULL
    failed_seller_id = valid_df.filter(col("seller_id").isNull())
    write_to_quarantine(failed_seller_id, quarantine_path, dataset_name, "missing_seller_id")
    valid_df = valid_df.filter(col("seller_id").isNotNull())

    # DQ Check 3: units_sold >= 0 (and not null)
    failed_units = valid_df.filter(
        col("units_sold").isNull() |
        (col("units_sold") < 0)
    )
    write_to_quarantine(failed_units, quarantine_path, dataset_name, "invalid_units_sold")
    valid_df = valid_df.filter(
        col("units_sold").isNotNull() &
        (col("units_sold") >= 0)
    )

    # DQ Check 4: revenue >= 0 (and not null)
    failed_revenue = valid_df.filter(
        col("revenue").isNull() |
        isnan(col("revenue")) |
        (col("revenue") < 0)
    )
    write_to_quarantine(failed_revenue, quarantine_path, dataset_name, "invalid_revenue")
    valid_df = valid_df.filter(
        col("revenue").isNotNull() &
        ~isnan(col("revenue")) &
        (col("revenue") >= 0)
    )

    # DQ Check 5: marketplace_price >= 0 (and not null)
    failed_price = valid_df.filter(
        col("marketplace_price").isNull() |
        isnan(col("marketplace_price")) |
        (col("marketplace_price") < 0)
    )
    write_to_quarantine(failed_price, quarantine_path, dataset_name, "invalid_marketplace_price")
    valid_df = valid_df.filter(
        col("marketplace_price").isNotNull() &
        ~isnan(col("marketplace_price")) &
        (col("marketplace_price") >= 0)
    )

    # DQ Check 6: sale_date IS NOT NULL AND sale_date <= current_date()
    failed_date = valid_df.filter(
        col("sale_date").isNull() |
        (col("sale_date") > current_date())
    )
    write_to_quarantine(failed_date, quarantine_path, dataset_name, "invalid_sale_date")
    valid_df = valid_df.filter(
        col("sale_date").isNotNull() &
        (col("sale_date") <= current_date())
    )

    print(f"DQ checks completed. Valid records: {valid_df.count()}")
    return valid_df


def write_to_hudi(df: DataFrame, hudi_output_path: str, table_name: str = "competitor_sales_hudi"):
    """
    Write DataFrame to Hudi table with overwrite mode.

    Args:
        df: DataFrame to write
        hudi_output_path: Output path for Hudi table
        table_name: Name of the Hudi table
    """
    print(f"Writing to Hudi table at {hudi_output_path}...")

    # Create composite record key from seller_id + item_id
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
    spark = get_spark_session("ETL_Competitor_Sales")

    try:
        # Load configuration
        print(f"Loading configuration from {config_path}...")
        config = load_yaml_config(config_path)
        competitor_sales_config = config.get("competitor_sales", {})

        input_path = competitor_sales_config.get("input_path")
        hudi_output_path = competitor_sales_config.get("hudi_output_path")
        # Use container path for quarantine when running in Docker
        quarantine_path = "/opt/spark/work-dir/quarantine"

        if not input_path or not hudi_output_path:
            raise ValueError("Missing required configuration: input_path or hudi_output_path")

        print(f"Input path: {input_path}")
        print(f"Hudi output path: {hudi_output_path}")
        print(f"Quarantine path: {quarantine_path}")

        # Bronze Layer: Read raw data from input CSV
        print("\n=== Bronze Layer: Reading raw data ===")
        bronze_df = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(input_path)

        print(f"Total raw records: {bronze_df.count()}")
        print("Schema:")
        bronze_df.printSchema()

        # Silver Layer: Data cleaning
        print("\n=== Silver Layer: Data cleaning ===")
        silver_df = clean_competitor_sales_data(bronze_df)

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

