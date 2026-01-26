"""
Spark Structured Streaming Consumer
Consumes orders from Kafka, cleans data, and writes to Data Lake (Parquet)
"""

import sys
import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_date, year, month, dayofmonth, concat_ws, lit, lpad
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType
import yaml


def load_config(config_path):
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def get_order_schema():
    """Define schema for order JSON"""
    return StructType([
        StructField("order_id", IntegerType(), True),
        StructField("customer_name", StringType(), True),
        StructField("restaurant_name", StringType(), True),
        StructField("item", StringType(), True),
        StructField("amount", DoubleType(), True),
        StructField("order_status", StringType(), True),
        StructField("created_at", StringType(), True)
    ])


def main():
    parser = argparse.ArgumentParser(description='Spark Structured Streaming Consumer for Food Orders')
    parser.add_argument('--config', required=True, help='Path to configuration YAML file')
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    kafka_config = config['kafka']
    datalake_config = config['datalake']
    streaming_config = config['streaming']
    
    # Create Spark session
    spark = SparkSession.builder \
        .appName("FoodOrdersStreamConsumer") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0") \
        .config("spark.sql.streaming.checkpointLocation", streaming_config['checkpoint_location']) \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("WARN")
    
    print("Starting Spark Structured Streaming Consumer")
    print(f"Kafka Topic: {kafka_config['topic']}")
    print(f"Data Lake Path: {datalake_config['path']}")
    print(f"Checkpoint Location: {streaming_config['checkpoint_location']}")
    
    try:
        # Read from Kafka
        kafka_df = spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", kafka_config['brokers']) \
            .option("subscribe", kafka_config['topic']) \
            .option("startingOffsets", "earliest") \
            .load()
        
        # Parse JSON
        schema = get_order_schema()
        orders_df = kafka_df.select(
            col("key").cast("string"),
            from_json(col("value").cast("string"), schema).alias("data"),
            col("timestamp")
        ).select("data.*")
        
        # Data Cleaning:
        # 1. Remove records with null order_id
        # 2. Remove records with negative amount
        cleaned_df = orders_df \
            .filter(col("order_id").isNotNull()) \
            .filter(col("amount") >= 0)
        
        # Convert created_at string to timestamp and extract date
        # Parse the timestamp string (format: "2025-01-15 10:30:00" or ISO format)
        orders_with_date = cleaned_df.withColumn(
            "order_timestamp",
            col("created_at").cast("timestamp")
        ).withColumn(
            "order_date",
            to_date(col("order_timestamp"))
        ).withColumn(
            "date",
            concat_ws("-", 
                year(col("order_date")).cast("string"),
                lpad(month(col("order_date")).cast("string"), 2, "0"),
                lpad(dayofmonth(col("order_date")).cast("string"), 2, "0")
            )
        )
        
        # Write to Data Lake with date partitioning (format: date=YYYY-MM-DD)
        checkpoint_path = streaming_config['checkpoint_location']
        output_path = datalake_config['path']
        
        # Ensure checkpoint directory exists
        from pathlib import Path
        Path(checkpoint_path).mkdir(parents=True, exist_ok=True)
        Path(output_path).mkdir(parents=True, exist_ok=True)
        
        query = orders_with_date \
            .writeStream \
            .outputMode("append") \
            .format("parquet") \
            .option("path", output_path) \
            .option("checkpointLocation", checkpoint_path) \
            .partitionBy("date") \
            .start()
        
        print("Streaming query started. Waiting for data...")
        print("Press Ctrl+C to stop")
        
        query.awaitTermination()
        
    except KeyboardInterrupt:
        print("\nShutting down consumer...")
    except Exception as e:
        print(f"Error in streaming: {str(e)}")
        import traceback
        traceback.print_exc()
    finally:
        spark.stop()


if __name__ == "__main__":
    main()

