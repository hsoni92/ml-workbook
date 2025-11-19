
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
    """Clean competitor sales data."""
    cleaned_df = df.withColumn("item_id", trim(col("item_id"))) \
                   .withColumn("seller_id", trim(col("seller_id")))

    cleaned_df = cleaned_df.withColumn("seller_id", initcap(col("seller_id")))

    cleaned_df = cleaned_df.withColumn("units_sold", col("units_sold").cast("int")) \
                           .withColumn("revenue", col("revenue").cast("double")) \
                           .withColumn("marketplace_price", col("marketplace_price").cast("double")) \
                           .withColumn("sale_date", to_date(col("sale_date"), "yyyy-MM-dd"))

    cleaned_df = cleaned_df.fillna({"units_sold": 0, "revenue": 0, "marketplace_price": 0})
    cleaned_df = cleaned_df.dropDuplicates(["seller_id", "item_id"])

    return cleaned_df


def perform_dq_checks(df: DataFrame, quarantine_path: str) -> DataFrame:
    """Perform data quality checks and quarantine failed records."""
    dataset_name = "competitor_sales"
    valid_df = df

    failed_item_id = valid_df.filter(col("item_id").isNull())
    write_to_quarantine(failed_item_id, quarantine_path, dataset_name, "missing_item_id")
    valid_df = valid_df.filter(col("item_id").isNotNull())

    failed_seller_id = valid_df.filter(col("seller_id").isNull())
    write_to_quarantine(failed_seller_id, quarantine_path, dataset_name, "missing_seller_id")
    valid_df = valid_df.filter(col("seller_id").isNotNull())

    failed_units = valid_df.filter(
        col("units_sold").isNull() |
        (col("units_sold") < 0)
    )
    write_to_quarantine(failed_units, quarantine_path, dataset_name, "invalid_units_sold")
    valid_df = valid_df.filter(
        col("units_sold").isNotNull() &
        (col("units_sold") >= 0)
    )

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

    failed_date = valid_df.filter(
        col("sale_date").isNull() |
        (col("sale_date") > current_date())
    )
    write_to_quarantine(failed_date, quarantine_path, dataset_name, "invalid_sale_date")
    valid_df = valid_df.filter(
        col("sale_date").isNotNull() &
        (col("sale_date") <= current_date())
    )

    return valid_df


def write_to_hudi(df: DataFrame, hudi_output_path: str, table_name: str = "competitor_sales_hudi"):
    """Write DataFrame to Hudi table."""
    df_with_key = df.withColumn("record_key", concat_ws("_", col("seller_id"), col("item_id")))

    hudi_options = {
        'hoodie.table.name': table_name,
        'hoodie.datasource.write.recordkey.field': 'record_key',
        'hoodie.datasource.write.partitionpath.field': '',
        'hoodie.datasource.write.table.type': 'COPY_ON_WRITE',
        'hoodie.datasource.write.operation': 'insert_overwrite_table',
        'hoodie.datasource.write.precombine.field': 'seller_id',
        'hoodie.cleaner.policy': 'KEEP_LATEST_COMMITS',
        'hoodie.cleaner.commits.retained': 1
    }

    df_with_key.write \
        .format("org.apache.hudi") \
        .options(**hudi_options) \
        .mode("overwrite") \
        .save(hudi_output_path)


def main():
    """Main ETL pipeline execution."""
    args = parse_arguments()
    config_path = args.config

    spark = get_spark_session("ETL_Competitor_Sales")

    try:
        config = load_yaml_config(config_path)
        competitor_sales_config = config.get("competitor_sales", {})

        input_path = competitor_sales_config.get("input_path")
        hudi_output_path = competitor_sales_config.get("hudi_output_path")
        quarantine_path = "/opt/spark/work-dir/quarantine"

        if not input_path or not hudi_output_path:
            raise ValueError("Missing required configuration: input_path or hudi_output_path")

        bronze_df = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(input_path)

        silver_df = clean_competitor_sales_data(bronze_df)
        gold_df = perform_dq_checks(silver_df, quarantine_path)
        write_to_hudi(gold_df, hudi_output_path)

    except Exception as e:
        print(f"Error in ETL pipeline: {str(e)}", file=sys.stderr)
        raise
    finally:
        spark.stop()


if __name__ == "__main__":
    main()

