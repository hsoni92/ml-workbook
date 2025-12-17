1. docker-compose up -d                    # Start infrastructure
2. docker-compose ps                        # Verify services
3. Create Kafka topic                       # One-time setup
4. ./scripts/consumer_spark_submit.sh      # Terminal 1: Start consumer
5. ./scripts/producer_spark_submit.sh      # Terminal 2: Start producer
6. Insert test data in PostgreSQL          # Test incremental ingestion
7. Monitor via Spark UI / logs             # Verify processing
8. Query Parquet files                     # Verify output