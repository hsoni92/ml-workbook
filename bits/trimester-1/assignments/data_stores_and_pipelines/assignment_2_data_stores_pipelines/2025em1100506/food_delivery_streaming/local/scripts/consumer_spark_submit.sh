#!/bin/bash

# Consumer Spark Submit Script
# Runs the Spark Structured Streaming consumer inside the Spark container

docker exec -it food_delivery_spark /opt/spark/bin/spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 \
  --master local[*] \
  /workspace/consumers/orders_stream_consumer.py \
  --config /workspace/configs/orders_stream.yml





