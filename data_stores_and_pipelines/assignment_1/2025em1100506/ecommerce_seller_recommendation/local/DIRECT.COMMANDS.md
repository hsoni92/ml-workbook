# Local Spark Commands

## ETL Seller Catalog
spark-submit --master local[*] --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.legacy.timeParserPolicy=LEGACY src/etl_seller_catalog.py --config configs/ecomm_prod.yml

## ETL Company Sales
spark-submit --master local[*] --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.legacy.timeParserPolicy=LEGACY src/etl_company_sales.py --config configs/ecomm_prod.yml

## ETL Competitor Sales
spark-submit --master local[*] --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.legacy.timeParserPolicy=LEGACY src/etl_competitor_sales.py --config configs/ecomm_prod.yml

## Consumption Recommendation
spark-submit --master local[*] --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.legacy.timeParserPolicy=LEGACY src/consumption_recommendation.py --config configs/ecomm_prod.yml

## Visualization
python3 src/visualize_recommendations.py --csv-path data/2025em1100506/processed/recommendations_csv/seller_recommend_data.csv
