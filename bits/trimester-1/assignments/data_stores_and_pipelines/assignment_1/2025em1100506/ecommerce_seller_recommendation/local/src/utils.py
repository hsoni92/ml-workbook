import yaml
import argparse
from datetime import datetime
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import lit
from typing import Dict, Any


def get_spark_session(app_name: str) -> SparkSession:
    """Initialize Spark session."""
    spark = (
        SparkSession.builder
        .appName(app_name)
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config("spark.sql.legacy.timeParserPolicy", "LEGACY")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")
    return spark


def load_yaml_config(config_path: str) -> Dict[str, Any]:
    """Load and parse YAML configuration file."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def parse_arguments():
    """Parse command-line arguments for config file path."""
    parser = argparse.ArgumentParser(description='ETL Pipeline')
    parser.add_argument(
        '--config',
        type=str,
        required=True,
        help='Path to YAML configuration file'
    )
    return parser.parse_args()


def write_to_quarantine(
    df: DataFrame,
    quarantine_path: str,
    dataset_name: str,
    failure_reason: str
) -> None:
    """Write failed records to quarantine zone."""
    if df is None:
        return

    if df.rdd.isEmpty():
        return

    quarantined_df = df.withColumn("dataset_name", lit(dataset_name)) \
                       .withColumn("dq_failure_reason", lit(failure_reason)) \
                       .withColumn("quarantine_timestamp", lit(datetime.now().isoformat()))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_quarantine_path = f"{quarantine_path}/{dataset_name}/{failure_reason}/{timestamp}"

    quarantined_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(full_quarantine_path)

    print(f"Quarantined {df.count()} records to {full_quarantine_path}")


def get_quarantine_path(base_path: str = "quarantine") -> str:
    """Get the base quarantine path."""
    return base_path

