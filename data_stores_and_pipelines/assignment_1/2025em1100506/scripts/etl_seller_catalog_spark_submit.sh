#!/bin/bash

# ETL Pipeline for Seller Catalog
# This script runs the seller catalog ETL pipeline using Docker

docker exec -it spark-master bash -c "mkdir -p /opt/spark/.ivy2/cache && export IVY_HOME=/opt/spark/.ivy2 && /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 \
  --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
  --conf spark.sql.legacy.timeParserPolicy=LEGACY \
  /opt/spark/work-dir/src/etl_seller_catalog.py \
  --config /opt/spark/work-dir/configs/ecomm_prod.yml"

