"""
CDC Simulation & Kafka Producer
Polls PostgreSQL for new orders and publishes them to Kafka
"""

import sys
import json
import time
import argparse
from datetime import datetime
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_json, struct
import yaml


def load_config(config_path):
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


def get_last_processed_timestamp(config):
    """Read last processed timestamp from file"""
    timestamp_path = Path(config['streaming']['last_processed_timestamp_location'])
    
    # If path is a directory, use a default filename
    if timestamp_path.exists() and timestamp_path.is_dir():
        timestamp_file = timestamp_path / "last_timestamp.txt"
    else:
        timestamp_file = timestamp_path
        # Ensure parent directory exists
        timestamp_file.parent.mkdir(parents=True, exist_ok=True)
    
    if timestamp_file.exists() and timestamp_file.is_file():
        with open(timestamp_file, 'r') as f:
            timestamp_str = f.read().strip()
            if timestamp_str:
                return timestamp_str
    return None


def save_last_processed_timestamp(config, timestamp):
    """Save last processed timestamp to file"""
    timestamp_path = Path(config['streaming']['last_processed_timestamp_location'])
    
    # If path is a directory, use a default filename
    if timestamp_path.exists() and timestamp_path.is_dir():
        timestamp_file = timestamp_path / "last_timestamp.txt"
    else:
        timestamp_file = timestamp_path
        # Ensure parent directory exists
        timestamp_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(timestamp_file, 'w') as f:
        f.write(timestamp)


def poll_and_publish(spark, config):
    """Poll PostgreSQL for new records and publish to Kafka"""

    pg_config = config['postgres']
    kafka_config = config['kafka']
    batch_interval = config['streaming']['batch_interval']
    
    print(f"Starting CDC Producer - Polling every {batch_interval} seconds")
    print(f"PostgreSQL: {pg_config['jdbc_url']}")
    print(f"Kafka Topic: {kafka_config['topic']}")
    
    while True:
        try:
            # Get last processed timestamp
            last_timestamp = get_last_processed_timestamp(config)
            
            # Build query (quote table name if it starts with a number)
            table_name = pg_config['table']
            if table_name[0].isdigit():
                table_name = f'"{table_name}"'
            
            if last_timestamp:
                query = f"(SELECT * FROM {table_name} WHERE created_at > '{last_timestamp}' ORDER BY created_at) AS new_orders"
            else:
                # First run - get all records
                query = f"(SELECT * FROM {table_name} ORDER BY created_at) AS all_orders"
            
            # Read from PostgreSQL
            df = spark.read \
                .format("jdbc") \
                .option("url", pg_config['jdbc_url']) \
                .option("dbtable", query) \
                .option("user", pg_config['user']) \
                .option("password", pg_config['password']) \
                .option("driver", "org.postgresql.Driver") \
                .load()
            
            # Get count of new records
            new_count = df.count()
            
            if new_count > 0:
                print(f"Found {new_count} new record(s)")
                
                # Convert to JSON format matching the required schema
                df_json = df.select(
                    col("order_id").cast("int").alias("order_id"),
                    col("customer_name").alias("customer_name"),
                    col("restaurant_name").alias("restaurant_name"),
                    col("item").alias("item"),
                    col("amount").cast("double").alias("amount"),
                    col("order_status").alias("order_status"),
                    col("created_at").cast("string").alias("created_at")
                )
                
                # Convert to JSON string
                df_with_json = df_json.select(
                    to_json(struct([col(c) for c in df_json.columns])).alias("value")
                )
                
                # Publish to Kafka
                df_with_json.write \
                    .format("kafka") \
                    .option("kafka.bootstrap.servers", kafka_config['brokers']) \
                    .option("topic", kafka_config['topic']) \
                    .save()
                
                # Get the latest timestamp from the batch
                latest_timestamp = df.agg({"created_at": "max"}).collect()[0][0]
                
                if latest_timestamp:
                    # Save last processed timestamp
                    save_last_processed_timestamp(config, str(latest_timestamp))
                    print(f"Published {new_count} record(s) to Kafka. Last timestamp: {latest_timestamp}")
                else:
                    print(f"Published {new_count} record(s) to Kafka")
            else:
                print("No new records found")
            
            # Wait for next poll
            time.sleep(batch_interval)
            
        except Exception as e:
            print(f"Error in polling: {str(e)}")
            import traceback
            traceback.print_exc()
            time.sleep(batch_interval)


def main():
    parser = argparse.ArgumentParser(description='CDC Producer for Food Orders')
    parser.add_argument('--config', required=True, help='Path to configuration YAML file')
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)

    # Create Spark session
    spark = SparkSession.builder \
        .appName("FoodOrdersCDCProducer") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0,org.postgresql:postgresql:42.7.1") \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("WARN")
    
    try:
        poll_and_publish(spark, config)
    except KeyboardInterrupt:
        print("\nShutting down producer...")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()

