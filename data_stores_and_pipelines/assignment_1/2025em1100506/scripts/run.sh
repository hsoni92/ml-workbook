# !/bin/bash

# Run the ETL pipeline
./scripts/etl_seller_catalog_spark_submit.sh

# Run the company sales pipeline
./scripts/etl_company_sales_spark_submit.sh

# Run the competitor sales pipeline
./scripts/etl_competitor_sales_spark_submit.sh

# Run the consumption recommendation pipeline
./scripts/consumption_recommendation_spark_submit.sh

# Run the visualization script
./scripts/visualize_recommendations.sh
