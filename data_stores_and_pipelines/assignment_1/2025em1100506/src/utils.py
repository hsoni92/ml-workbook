"""
Utility functions for ETL pipelines and data processing.
This module provides common functions used across all ETL scripts.
"""

import yaml
import argparse
from datetime import datetime
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import lit
from typing import Dict, Any


def get_spark_session(app_name: str) -> SparkSession:
    """
    Initialize Spark session with required configurations for Hudi and data processing.

    Args:
        app_name: Name of the Spark application

    Returns:
        Configured SparkSession instance
    """
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
    """
    Load and parse YAML configuration file.

    Args:
        config_path: Path to the YAML configuration file

    Returns:
        Dictionary containing configuration values

    Raises:
        FileNotFoundError: If the config file doesn't exist
        yaml.YAMLError: If the YAML file is malformed
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file {config_path}: {str(e)}")


def parse_arguments():
    """
    Parse command-line arguments for config file path.

    Returns:
        argparse.Namespace: Parsed arguments containing config path
    """
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
    """
    Write failed records to quarantine zone with metadata.

    The quarantine zone stores records that failed data quality checks.
    Each record is enriched with:
    - dataset_name: Name of the source dataset
    - dq_failure_reason: Reason for failure
    - quarantine_timestamp: When the record was quarantined

    Args:
        df: DataFrame containing failed records to quarantine
        quarantine_path: Base path for quarantine zone (e.g., "quarantine/")
        dataset_name: Name of the dataset (e.g., "seller_catalog", "company_sales")
        failure_reason: Reason for quarantine (e.g., "missing_seller_id", "negative_price")

    Returns:
        None (writes data to disk)
    """
    if df is None:
        return

    # Check if DataFrame is empty
    if df.rdd.isEmpty():
        print(f"No records to quarantine for {dataset_name} with reason: {failure_reason}")
        return

    # Add metadata columns
    quarantined_df = df.withColumn("dataset_name", lit(dataset_name)) \
                       .withColumn("dq_failure_reason", lit(failure_reason)) \
                       .withColumn("quarantine_timestamp", lit(datetime.now().isoformat()))

    # Construct full quarantine path: quarantine_path/dataset_name/failure_reason/timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    full_quarantine_path = f"{quarantine_path}/{dataset_name}/{failure_reason}/{timestamp}"

    # Write to CSV with overwrite mode
    quarantined_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(full_quarantine_path)

    print(f"Quarantined {df.count()} records to {full_quarantine_path}")


def get_quarantine_path(base_path: str = "quarantine") -> str:
    """
    Get the base quarantine path. Can be overridden via config if needed.

    Args:
        base_path: Base path for quarantine zone

    Returns:
        Quarantine path string
    """
    return base_path

