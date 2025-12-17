#!/bin/bash

# Producer Spark Submit Script
# Runs the CDC producer inside the Spark container

docker exec -it food_delivery_spark /opt/spark/bin/spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0,org.postgresql:postgresql:42.7.1 \
  --master local[*] \
  /workspace/producers/orders_cdc_producer.py \
  --config /workspace/configs/orders_stream.yml





