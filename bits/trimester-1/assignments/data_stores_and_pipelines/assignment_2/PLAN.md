# Project Implementation Plan

## Overview

This plan outlines the setup for a real-time streaming pipeline using Docker Compose to run PostgreSQL, Kafka, and Spark containers, with local filesystem for Data Lake storage.

## Architecture Components

1. **PostgreSQL** - Source database for food orders
2. **Kafka + Zookeeper** - Message broker for streaming events
3. **Spark** - Processing engine for streaming jobs
4. **Local Filesystem** - Data Lake storage (Parquet format)

## Docker Compose Setup

### Services Configuration

#### 1. PostgreSQL Service
- **Image**: `postgres:15`
- **Port**: `5432`
- **Database**: `food_delivery_db`
- **User**: `student`
- **Password**: `student123`
- **Volume**: Persistent storage for database data

#### 2. Zookeeper Service
- **Image**: `confluentinc/cp-zookeeper:latest`
- **Port**: `2181`
- **Purpose**: Required for Kafka coordination

#### 3. Kafka Service
- **Image**: `confluentinc/cp-kafka:latest`
- **Port**: `9092`
- **Dependencies**: Zookeeper
- **Purpose**: Message broker for order events

#### 4. Spark Service
- **Image**: `bitnami/spark:3.5` (or custom image with dependencies)
- **Ports**: 
  - `8080` - Spark UI
  - `7077` - Spark Master port
- **Purpose**: Run Spark Structured Streaming jobs
- **Volume Mounts**: 
  - Project code directory
  - Local Data Lake directory
  - Config files

## Directory Structure

```
<project_root>/
├── docker-compose.yml
├── db/
│   └── orders.sql
├── producers/
│   └── orders_cdc_producer.py
├── consumers/
│   └── orders_stream_consumer.py
├── scripts/
│   ├── producer_spark_submit.sh
│   └── consumer_spark_submit.sh
├── configs/
│   └── orders_stream.yml
├── datalake/                    # Local Data Lake (mounted in containers)
│   └── food/
│       └── <rollnumber>/
│           ├── output/
│           │   └── orders/
│           ├── checkpoints/
│           │   └── orders/
│           └── lastprocess/
│               └── orders/
└── README.md
```

## Docker Compose Configuration

### File: `docker-compose.yml`

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: food_delivery_postgres
    environment:
      POSTGRES_DB: food_delivery_db
      POSTGRES_USER: student
      POSTGRES_PASSWORD: student123
      PGDATA: /var/lib/postgresql/data/pgdata
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./db:/docker-entrypoint-initdb.d  # Auto-run SQL scripts on init
    networks:
      - food_delivery_network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U student -d food_delivery_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    container_name: food_delivery_zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "2181:2181"
    networks:
      - food_delivery_network
    healthcheck:
      test: ["CMD", "nc", "-z", "localhost", "2181"]
      interval: 10s
      timeout: 5s
      retries: 5

  kafka:
    image: confluentinc/cp-kafka:latest
    container_name: food_delivery_kafka
    depends_on:
      zookeeper:
        condition: service_healthy
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092,PLAINTEXT_INTERNAL://kafka:29092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_INTERNAL:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT_INTERNAL
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: "true"
    ports:
      - "9092:9092"
    volumes:
      - kafka_data:/var/lib/kafka/data
    networks:
      - food_delivery_network
    healthcheck:
      test: ["CMD", "kafka-broker-api-versions", "--bootstrap-server", "localhost:9092"]
      interval: 10s
      timeout: 5s
      retries: 5

  spark:
    image: bitnami/spark:3.5
    container_name: food_delivery_spark
    depends_on:
      postgres:
        condition: service_healthy
      kafka:
        condition: service_healthy
    environment:
      - SPARK_MODE=master
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no
    ports:
      - "8080:8080"  # Spark UI
      - "7077:7077"  # Spark Master
    volumes:
      - .:/workspace  # Mount entire project
      - ./datalake:/datalake  # Mount Data Lake directory
    working_dir: /workspace
    networks:
      - food_delivery_network
    command: >
      bash -c "
        pip install psycopg2-binary kafka-python pyyaml &&
        tail -f /dev/null
      "

volumes:
  postgres_data:
    driver: local
  kafka_data:
    driver: local

networks:
  food_delivery_network:
    driver: bridge
```

## Configuration Adjustments

### Updated `configs/orders_stream.yml`

Since services are in Docker containers, update connection strings:

```yaml
postgres:
  jdbc_url: "jdbc:postgresql://postgres:5432/food_delivery_db"  # Use service name
  host: postgres  # Use service name for container-to-container communication
  port: 5432
  db: "food_delivery_db"
  user: "student"
  password: "student123"
  table: <rollnumber>_orders

kafka:
  brokers: "kafka:29092"  # Use internal broker address for container communication
  topic: "<rollnumber>_food_orders_raw"

datalake:
  path: "/datalake/food/<rollnumber>/output/orders"  # Local filesystem path in container
  format: "parquet"

streaming:
  checkpoint_location: "/datalake/food/<rollnumber>/checkpoints/orders"
  last_processed_timestamp_location: "/datalake/food/<rollnumber>/lastprocess/orders"
  batch_interval: 5  # seconds
```

**Note**: For Spark jobs running inside the container, use service names (`postgres`, `kafka`). For jobs running on host machine, use `localhost` or `127.0.0.1`.

## Implementation Steps

### Step 1: Create Directory Structure

```bash
mkdir -p datalake/food/<rollnumber>/{output/orders,checkpoints/orders,lastprocess/orders}
mkdir -p db producers consumers scripts configs
```

### Step 2: Create Docker Compose File

Create `docker-compose.yml` with the configuration above.

### Step 3: Initialize PostgreSQL

1. Create `db/orders.sql` with table creation and initial data
2. Place it in `db/` directory (auto-executed on first container start)

### Step 4: Update Spark Submit Scripts

#### `scripts/producer_spark_submit.sh`

```bash
#!/bin/bash
docker exec -it food_delivery_spark spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,org.postgresql:postgresql:42.7.1 \
  --master local[*] \
  /workspace/producers/orders_cdc_producer.py \
  --config /workspace/configs/orders_stream.yml
```

#### `scripts/consumer_spark_submit.sh`

```bash
#!/bin/bash
docker exec -it food_delivery_spark spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
  --master local[*] \
  /workspace/consumers/orders_stream_consumer.py \
  --config /workspace/configs/orders_stream.yml
```

Make scripts executable:
```bash
chmod +x scripts/*.sh
```

### Step 5: Start Services

```bash
# Start all services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f [service_name]
```

### Step 6: Verify Services

```bash
# Check PostgreSQL
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "\dt"

# Check Kafka topics
docker exec -it food_delivery_kafka kafka-topics --bootstrap-server localhost:9092 --list

# Check Spark
curl http://localhost:8080
```

### Step 7: Create Kafka Topic

```bash
docker exec -it food_delivery_kafka kafka-topics --create \
  --bootstrap-server localhost:9092 \
  --topic <rollnumber>_food_orders_raw \
  --partitions 1 \
  --replication-factor 1
```

### Step 8: Run Spark Jobs

```bash
# Start consumer (runs continuously)
./scripts/consumer_spark_submit.sh

# In another terminal, start producer (runs continuously)
./scripts/producer_spark_submit.sh
```

## Data Lake Access

### From Host Machine

Data Lake is accessible at:
```
./datalake/food/<rollnumber>/
```

### From Spark Container

Data Lake is accessible at:
```
/datalake/food/<rollnumber>/
```

## Network Communication

- **Host → Containers**: Use `localhost` with mapped ports
- **Container → Container**: Use service names (`postgres`, `kafka`, `spark`)
- **Spark → PostgreSQL**: `jdbc:postgresql://postgres:5432/food_delivery_db`
- **Spark → Kafka**: `kafka:29092` (internal) or `localhost:9092` (from host)

## Troubleshooting

### Check Service Health

```bash
docker-compose ps
docker-compose logs [service_name]
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

### Reset Everything

```bash
# Stop and remove containers, networks, volumes
docker-compose down -v

# Restart
docker-compose up -d
```

### View Kafka Messages

```bash
docker exec -it food_delivery_kafka kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic <rollnumber>_food_orders_raw \
  --from-beginning
```

## Testing Workflow

1. **Start all services**: `docker-compose up -d`
2. **Verify PostgreSQL**: Check table exists and has initial data
3. **Create Kafka topic**: Use command from Step 7
4. **Start consumer**: Run consumer script (runs continuously)
5. **Start producer**: Run producer script (runs continuously)
6. **Insert test data**: Add new records to PostgreSQL
7. **Verify pipeline**: 
   - Check Kafka topic for messages
   - Check Data Lake for Parquet files
   - Verify data correctness

## Additional Notes

1. **Spark Dependencies**: The Spark container may need additional Python packages. Install them via:
   ```bash
   docker exec -it food_delivery_spark pip install <package>
   ```

2. **Persistent Storage**: Database and Kafka data persist in Docker volumes even after container removal.

3. **Resource Limits**: Add resource limits to `docker-compose.yml` if needed:
   ```yaml
   deploy:
     resources:
       limits:
         cpus: '2'
         memory: 4G
   ```

4. **Environment Variables**: Consider using `.env` file for sensitive data instead of hardcoding in `docker-compose.yml`.

