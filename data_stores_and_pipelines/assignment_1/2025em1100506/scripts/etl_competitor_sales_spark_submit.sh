#!/bin/bash

# ETL Pipeline for Competitor Sales
# This script runs the competitor sales ETL pipeline using Docker

PYTHON_SCRIPT="etl_competitor_sales.py"

docker exec -it spark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 \
  --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
  --conf spark.sql.legacy.timeParserPolicy=LEGACY \
  --driver-java-options '-Divy.home=/opt/spark/.ivy2' \
  /opt/spark/work-dir/src/$PYTHON_SCRIPT \
  --config /opt/spark/work-dir/configs/ecomm_prod.yml

