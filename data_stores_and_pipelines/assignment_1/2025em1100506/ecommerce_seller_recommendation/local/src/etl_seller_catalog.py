
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
    """Standardize category labels to common formats."""
    normalized = lower(trim(category_col))

    return when(normalized.isin(['electronics', 'electronic', 'elec']), 'Electronics') \
        .when(normalized.isin(['apparel', 'clothing', 'clothes', 'fashion']), 'Apparel') \
        .when(normalized.isin(['home', 'home & garden', 'homegarden', 'home_garden']), 'Home & Garden') \
        .when(normalized.isin(['sports', 'sport', 'sports & outdoors']), 'Sports') \
        .when(normalized.isin(['books', 'book']), 'Books') \
        .when(normalized.isin(['toys', 'toy', 'toys & games']), 'Toys') \
        .when(normalized.isin(['beauty', 'beauty & personal care']), 'Beauty') \
        .when(normalized.isin(['automotive', 'auto', 'car']), 'Automotive') \
        .otherwise(initcap(trim(category_col)))


def clean_seller_catalog_data(df: DataFrame) -> DataFrame:
    """Clean seller catalog data."""
    cleaned_df = df.withColumn("seller_id", trim(col("seller_id"))) \
                   .withColumn("item_id", trim(col("item_id"))) \
                   .withColumn("item_name", trim(col("item_name"))) \
                   .withColumn("category", trim(col("category")))

    cleaned_df = cleaned_df.withColumn("item_name", initcap(col("item_name")))
    cleaned_df = cleaned_df.withColumn("category", standardize_category(col("category")))

    cleaned_df = cleaned_df.withColumn("marketplace_price",
                                      col("marketplace_price").cast("double")) \
                           .withColumn("stock_qty",
                                      col("stock_qty").cast("int"))

    cleaned_df = cleaned_df.fillna({"stock_qty": 0})
    cleaned_df = cleaned_df.dropDuplicates(["seller_id", "item_id"])

    return cleaned_df


def perform_dq_checks(df: DataFrame, quarantine_path: str) -> DataFrame:
    """Perform data quality checks and quarantine failed records."""
    dataset_name = "seller_catalog"
    valid_df = df

    failed_seller_id = valid_df.filter(col("seller_id").isNull())
    write_to_quarantine(failed_seller_id, quarantine_path, dataset_name, "missing_seller_id")
    valid_df = valid_df.filter(col("seller_id").isNotNull())

    failed_item_id = valid_df.filter(col("item_id").isNull())
    write_to_quarantine(failed_item_id, quarantine_path, dataset_name, "missing_item_id")
    valid_df = valid_df.filter(col("item_id").isNotNull())

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

    failed_stock = valid_df.filter(
        col("stock_qty").isNull() |
        (col("stock_qty") < 0)
    )
    write_to_quarantine(failed_stock, quarantine_path, dataset_name, "invalid_stock_qty")
    valid_df = valid_df.filter(
        col("stock_qty").isNotNull() &
        (col("stock_qty") >= 0)
    )

    failed_item_name = valid_df.filter(col("item_name").isNull())
    write_to_quarantine(failed_item_name, quarantine_path, dataset_name, "missing_item_name")
    valid_df = valid_df.filter(col("item_name").isNotNull())

    failed_category = valid_df.filter(col("category").isNull())
    write_to_quarantine(failed_category, quarantine_path, dataset_name, "missing_category")
    valid_df = valid_df.filter(col("category").isNotNull())

    return valid_df


def write_to_hudi(df: DataFrame, hudi_output_path: str, table_name: str = "seller_catalog_hudi"):
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

    spark = get_spark_session("ETL_Seller_Catalog")

    try:
        config = load_yaml_config(config_path)
        seller_catalog_config = config.get("seller_catalog", {})

        input_path = seller_catalog_config.get("input_path")
        hudi_output_path = seller_catalog_config.get("hudi_output_path")
        quarantine_path = "/opt/spark/work-dir/quarantine"

        if not input_path or not hudi_output_path:
            raise ValueError("Missing required configuration: input_path or hudi_output_path")

        bronze_df = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(input_path)

        silver_df = clean_seller_catalog_data(bronze_df)
        gold_df = perform_dq_checks(silver_df, quarantine_path)
        write_to_hudi(gold_df, hudi_output_path)

    except Exception as e:
        print(f"Error in ETL pipeline: {str(e)}", file=sys.stderr)
        raise
    finally:
        spark.stop()


if __name__ == "__main__":
    main()

