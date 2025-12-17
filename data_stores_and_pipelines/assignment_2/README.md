# Food Delivery Streaming Pipeline

## Overview

This project implements a real-time streaming pipeline for a Food Delivery platform using PostgreSQL, Kafka, and Spark Structured Streaming. The pipeline detects new orders in PostgreSQL, publishes them to Kafka, and processes them into a Data Lake in Parquet format.

## Architecture

```
PostgreSQL → CDC Producer (Spark) → Kafka → Spark Structured Streaming → Data Lake (Parquet)
```

## Prerequisites

- Docker and Docker Compose installed
- At least 8GB RAM available for containers
- Ports 5432, 9092, 2181, 8080, 7077 available

## Project Structure

- `docker-compose.yml` - Docker Compose configuration
- `db/orders.sql` - PostgreSQL table creation and initial data
- `producers/orders_cdc_producer.py` - CDC simulation and Kafka producer
- `consumers/orders_stream_consumer.py` - Spark Structured Streaming consumer
- `scripts/producer_spark_submit.sh` - Producer execution script
- `scripts/consumer_spark_submit.sh` - Consumer execution script
- `configs/orders_stream.yml` - Pipeline configuration
- `datalake/food/2025em1100506/output/orders/` - Processed Parquet files
- `datalake/food/2025em1100506/checkpoints/orders/` - Spark checkpoint data
- `datalake/food/2025em1100506/lastprocess/orders/` - Last processed timestamp
- `README.md` - This file

## Setup Instructions

### 1. Start Docker Containers

```bash
# Start all services (PostgreSQL, Zookeeper, Kafka, Spark)
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f [service_name]
```

### 2. Verify Services

```bash
# Check PostgreSQL
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "\dt"

# Check Kafka topics
docker exec -it food_delivery_kafka kafka-topics --bootstrap-server localhost:9092 --list

# Check Spark UI
curl http://localhost:4040
```

### 3. Create Kafka Topic

```bash
docker exec -it food_delivery_kafka kafka-topics --create \
  --bootstrap-server localhost:9092 \
  --topic 2025em1100506_food_orders_raw \
  --partitions 1 \
  --replication-factor 1
```

### 4. Verify Initial Data

The PostgreSQL table should be automatically created with 12 initial records when the container starts (via `db/orders.sql`).

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c 'SELECT COUNT(*) FROM "2025em1100506_orders";'
```

## Running the Pipeline

### Step 1: Start Consumer (Terminal 1)

The consumer runs continuously and processes messages from Kafka:

```bash
./scripts/consumer_spark_submit.sh
```

### Step 2: Start Producer (Terminal 2)

The producer polls PostgreSQL every 5 seconds and publishes new records to Kafka:

```bash
./scripts/producer_spark_submit.sh
```

## Testing Incremental Ingestion

### Insert New Records

Connect to PostgreSQL and insert new orders:

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db
```

```sql
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES
('Test User 1', 'Test Restaurant', 'Test Item 1', 100.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 2', 'Test Restaurant', 'Test Item 2', 200.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 3', 'Test Restaurant', 'Test Item 3', 300.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 4', 'Test Restaurant', 'Test Item 4', 400.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 5', 'Test Restaurant', 'Test Item 5', 500.00, 'PLACED', CURRENT_TIMESTAMP);
```

### Verify Pipeline

1. **Check Kafka Messages:**
```bash
docker exec -it food_delivery_kafka kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic 2025em1100506_food_orders_raw \
  --from-beginning
```

2. **Check Data Lake:**
```bash
# View Parquet files
ls -la datalake/food/2025em1100506/output/orders/

# View partitioned directories
find datalake/food/2025em1100506/output/orders/ -type d
```

3. **Query Parquet Files (using Spark):**
```bash
docker exec -it food_delivery_spark /opt/spark/bin/spark-shell
```

```scala
val df = spark.read.parquet("/datalake/food/2025em1100506/output/orders")
df.show()
df.count()
```

## Configuration

Edit `configs/orders_stream.yml` to modify:
- PostgreSQL connection details
- Kafka broker and topic
- Data Lake paths
- Streaming batch interval

**Note:** For container-to-container communication, service names (`postgres`, `kafka`) are used. For host-to-container, use `localhost`.

## Data Cleaning

The consumer automatically:
- Removes records with null `order_id`
- Removes records with negative `amount`
- Partitions data by date (`date=YYYY-MM-DD`)

## Monitoring

### Spark UI
Access at: http://localhost:4040 (when Spark jobs are running)

### View Logs
```bash
# Producer logs
docker logs -f food_delivery_spark

# Consumer logs
docker logs -f food_delivery_spark

# All services
docker-compose logs -f
```

## Troubleshooting

### Services Not Starting
```bash
# Check service health
docker-compose ps

# View detailed logs
docker-compose logs [service_name]

# Restart services
docker-compose restart
```

### Reset Everything
```bash
# Stop and remove all containers, volumes, networks
docker-compose down -v

# Restart
docker-compose up -d
```

### Check Last Processed Timestamp
```bash
cat datalake/food/2025em1100506/lastprocess/orders
```

### Access Container Shells
```bash
# PostgreSQL
docker exec -it food_delivery_postgres bash

# Kafka
docker exec -it food_delivery_kafka bash

# Spark
docker exec -it food_delivery_spark bash
```

## Assignment Deliverables

All required deliverables are present:

- `db/orders.sql` - PostgreSQL table creation and initial data
- `producers/orders_cdc_producer.py` - CDC simulation and Kafka producer
- `consumers/orders_stream_consumer.py` - Spark Structured Streaming consumer
- `scripts/producer_spark_submit.sh` - Producer execution script
- `scripts/consumer_spark_submit.sh` - Consumer execution script
- `configs/orders_stream.yml` - Pipeline configuration
- `README.md` - This file

## Roll Number

**Roll Number:** 2025em1100506
**Name:** Himanshu Soni

## Notes

- The pipeline uses local filesystem for Data Lake storage
- All services run in Docker containers
- Spark jobs run inside the Spark container
- Data is partitioned by date in format `date=YYYY-MM-DD`
- Checkpointing ensures exactly-once processing semantics




