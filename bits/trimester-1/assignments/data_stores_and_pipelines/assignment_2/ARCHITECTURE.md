# Architecture Documentation

## Overview

This project implements a **real-time streaming data pipeline** for a Food Delivery platform using a modern data engineering stack. The pipeline captures new orders from PostgreSQL, streams them through Kafka, and processes them into a Data Lake using Spark Structured Streaming.

## High-Level Architecture

```
┌─────────────────┐
│   PostgreSQL    │  Source Database (Food Orders)
│   (Source)      │
└────────┬────────┘
         │
         │ Polling (every 5 seconds)
         │ JDBC Query (created_at > last_timestamp)
         ▼
┌─────────────────────────────────────┐
│   CDC Producer                      │
│   (Spark Batch Job)                 │
│   - Detects new records             │
│   - Converts to JSON                │
│   - Maintains last_timestamp        │
└────────┬────────────────────────────┘
         │
         │ Publish JSON events
         ▼
┌─────────────────┐
│     Kafka        │  Message Broker
│   (Topic)        │  <rollnumber>_food_orders_raw
└────────┬────────┘
         │
         │ Consume stream
         ▼
┌─────────────────────────────────────┐
│   Stream Consumer                   │
│   (Spark Structured Streaming)      │
│   - Parse JSON                      │
│   - Data cleaning                   │
│   - Partition by date               │
└────────┬────────────────────────────┘
         │
         │ Write Parquet files
         ▼
┌─────────────────┐
│   Data Lake      │  Parquet Format
│   (Local FS)     │  Partitioned by date
└─────────────────┘
```

## Component Architecture

### 1. Infrastructure Layer (Docker Compose)

The entire infrastructure runs in Docker containers orchestrated via Docker Compose:

#### 1.1 PostgreSQL Service
- **Image**: `postgres:15`
- **Purpose**: Source database storing food delivery orders
- **Port**: `5432` (exposed to host)
- **Database**: `food_delivery_db`
- **Credentials**: `student/student123`
- **Initialization**: Auto-executes SQL scripts from `./db/` directory on first start
- **Persistence**: Data stored in Docker volume `postgres_data`
- **Health Check**: Uses `pg_isready` to ensure database is ready

#### 1.2 Zookeeper Service
- **Image**: `confluentinc/cp-zookeeper:latest`
- **Purpose**: Coordination service for Kafka cluster management
- **Port**: `2181`
- **Role**: Manages Kafka broker metadata, leader election, and configuration

#### 1.3 Kafka Service
- **Image**: `confluentinc/cp-kafka:7.4.0`
- **Purpose**: Distributed message broker for event streaming
- **Ports**: 
  - `9092` - External access (from host)
  - `29092` - Internal access (container-to-container)
- **Topic**: `<rollnumber>_food_orders_raw`
- **Configuration**:
  - Single broker setup (development)
  - Auto-create topics enabled
  - Replication factor: 1
- **Persistence**: Kafka data stored in Docker volume `kafka_data`
- **Network**: Uses internal listener `kafka:29092` for container communication

#### 1.4 Spark Service
- **Image**: `apache/spark-py:latest`
- **Purpose**: Processing engine for both batch (producer) and streaming (consumer) jobs
- **Ports**:
  - `8080` - Spark UI (when jobs are running)
  - `7077` - Spark Master port
- **Volume Mounts**:
  - `.:/workspace` - Entire project directory
  - `./datalake:/datalake` - Data Lake storage
- **Dependencies**: Installs Python packages (`psycopg2-binary`, `kafka-python`, `pyyaml`)
- **Mode**: Runs as master node, executes jobs in local mode

### 2. Application Layer

#### 2.1 CDC Producer (`producers/orders_cdc_producer.py`)

**Architecture Pattern**: Change Data Capture (CDC) Simulation using Polling

**How It Works**:

1. **Initialization**:
   - Creates SparkSession with PostgreSQL and Kafka connectors
   - Loads configuration from YAML file
   - Reads last processed timestamp from file system

2. **Polling Loop**:
   ```
   While True:
     ├─ Read last_timestamp from file
     ├─ Query PostgreSQL: WHERE created_at > last_timestamp
     ├─ If new records found:
     │   ├─ Convert DataFrame to JSON format
     │   ├─ Publish to Kafka topic
     │   └─ Update last_timestamp file
     └─ Sleep for batch_interval (5 seconds)
   ```

3. **Key Features**:
   - **Incremental Processing**: Only fetches new records using timestamp comparison
   - **Idempotency**: Maintains `last_processed_timestamp` to prevent duplicates
   - **JSON Serialization**: Converts PostgreSQL rows to JSON matching exact schema
   - **Error Handling**: Continues polling even on errors

4. **Data Flow**:
   ```
   PostgreSQL Table → Spark JDBC Read → DataFrame → JSON Conversion → Kafka Write
   ```

5. **Timestamp Management**:
   - Stores last processed timestamp in: `/datalake/food/<rollnumber>/lastprocess/orders`
   - Format: ISO timestamp string
   - Used for incremental query: `WHERE created_at > '{last_timestamp}'`

#### 2.2 Stream Consumer (`consumers/orders_stream_consumer.py`)

**Architecture Pattern**: Spark Structured Streaming with Micro-batch Processing

**How It Works**:

1. **Stream Initialization**:
   - Creates SparkSession with Kafka connector
   - Configures checkpoint location for fault tolerance
   - Defines JSON schema for order data

2. **Streaming Pipeline**:
   ```
   Kafka Topic → ReadStream → Parse JSON → Data Cleaning → Date Extraction → Partition → Write Parquet
   ```

3. **Processing Steps**:

   a. **Kafka Source**:
      - Subscribes to topic: `<rollnumber>_food_orders_raw`
      - Reads from earliest offset (on first run)
      - Uses Kafka connector for Spark Structured Streaming

   b. **JSON Parsing**:
      - Parses JSON string using defined schema
      - Extracts fields: `order_id`, `customer_name`, `restaurant_name`, `item`, `amount`, `order_status`, `created_at`

   c. **Data Cleaning**:
      - Filters out records with `null` order_id
      - Filters out records with negative `amount`
      - Ensures data quality before storage

   d. **Date Partitioning**:
      - Converts `created_at` string to timestamp
      - Extracts date component
      - Formats as `YYYY-MM-DD`
      - Creates partition column: `date`

   e. **Parquet Write**:
      - Writes in append mode (only new data)
      - Partitions by `date` column
      - Format: Parquet (columnar storage)
      - Uses checkpointing for exactly-once semantics

4. **Checkpointing**:
   - Location: `/datalake/food/<rollnumber>/checkpoints/orders`
   - Stores: Kafka offsets, query progress, metadata
   - Enables: Fault tolerance, exactly-once processing, recovery from failures

5. **Output Structure**:
   ```
   /datalake/food/<rollnumber>/output/orders/
   └── date=YYYY-MM-DD/
       └── part-*.parquet
   ```

### 3. Data Storage Architecture

#### 3.1 PostgreSQL (Source)
- **Schema**: Single table `<rollnumber>_orders`
- **Columns**:
  - `order_id` (SERIAL PRIMARY KEY)
  - `customer_name` (VARCHAR)
  - `restaurant_name` (VARCHAR)
  - `item` (VARCHAR)
  - `amount` (NUMERIC)
  - `order_status` (VARCHAR) - Values: PLACED, PREPARING, DELIVERED, CANCELLED
  - `created_at` (TIMESTAMP) - Used for incremental processing

#### 3.2 Kafka (Stream Buffer)
- **Topic**: `<rollnumber>_food_orders_raw`
- **Format**: JSON strings
- **Retention**: Configurable (default: 7 days)
- **Partitions**: 1 (single broker setup)
- **Replication**: 1 (no replication in dev setup)

#### 3.3 Data Lake (Sink)
- **Format**: Parquet (columnar, compressed)
- **Location**: `/datalake/food/<rollnumber>/output/orders`
- **Partitioning**: By date (`date=YYYY-MM-DD`)
- **Benefits**:
  - Efficient columnar storage
  - Query optimization (partition pruning)
  - Compression (smaller file sizes)
  - Schema evolution support

#### 3.4 Metadata Storage
- **Checkpoints**: `/datalake/food/<rollnumber>/checkpoints/orders`
  - Spark streaming state
  - Kafka offsets
  - Query progress metadata

- **Last Timestamp**: `/datalake/food/<rollnumber>/lastprocess/orders`
  - Producer state
  - Last processed timestamp
  - Enables incremental processing

## Data Flow Details

### End-to-End Flow

```
1. INSERT INTO PostgreSQL
   └─> New row with created_at = CURRENT_TIMESTAMP

2. Producer Polls (every 5 seconds)
   └─> Query: SELECT * WHERE created_at > last_timestamp
   └─> Returns new rows

3. Producer Processes
   └─> Convert DataFrame to JSON
   └─> Publish to Kafka topic
   └─> Update last_timestamp file

4. Consumer Reads from Kafka
   └─> Spark Structured Streaming micro-batch
   └─> Parse JSON → DataFrame

5. Consumer Processes
   └─> Data cleaning (filter nulls, negative amounts)
   └─> Extract date from created_at
   └─> Partition by date

6. Consumer Writes
   └─> Parquet files in date-partitioned directories
   └─> Update checkpoint (Kafka offsets)

7. Data Available in Data Lake
   └─> Ready for analytics queries
   └─> Partitioned by date for efficient querying
```

### Message Format

**Kafka Message (JSON)**:
```json
{
  "order_id": 101,
  "customer_name": "John Doe",
  "restaurant_name": "Burger Junction",
  "item": "Veg Burger",
  "amount": 220.0,
  "order_status": "PLACED",
  "created_at": "2025-01-15T12:24:00Z"
}
```

## Network Architecture

### Container Communication

All services run on a Docker bridge network (`food_delivery_network`):

```
┌─────────────────────────────────────────┐
│   food_delivery_network (bridge)        │
│                                         │
│  ┌──────────┐    ┌──────────┐         │
│  │PostgreSQL │◄───┤  Spark   │         │
│  │ :5432     │    │          │         │
│  └──────────┘    └────┬──────┘         │
│                       │                │
│                  ┌────▼──────┐         │
│                  │   Kafka   │         │
│                  │ :29092    │         │
│                  └────┬──────┘         │
│                       │                │
│                  ┌────▼──────┐         │
│                  │ Zookeeper │         │
│                  │ :2181     │         │
│                  └───────────┘         │
└─────────────────────────────────────────┘
```

### Connection Strings

- **Container-to-Container**: Use service names
  - PostgreSQL: `jdbc:postgresql://postgres:5432/food_delivery_db`
  - Kafka: `kafka:29092`

- **Host-to-Container**: Use `localhost` with mapped ports
  - PostgreSQL: `localhost:5432`
  - Kafka: `localhost:9092`

## Configuration Management

### Configuration File (`configs/orders_stream.yml`)

Centralized configuration using YAML format:

```yaml
postgres:
  jdbc_url: "jdbc:postgresql://postgres:5432/food_delivery_db"
  host: postgres
  port: 5432
  db: "food_delivery_db"
  user: "student"
  password: "student123"
  table: "2025em1100506_orders"

kafka:
  brokers: "kafka:29092"
  topic: "2025em1100506_food_orders_raw"

datalake:
  path: "/datalake/food/2025em1100506/output/orders"
  format: "parquet"

streaming:
  checkpoint_location: "/datalake/food/2025em1100506/checkpoints/orders"
  last_processed_timestamp_location: "/datalake/food/2025em1100506/lastprocess/orders"
  batch_interval: 5  # seconds
```

**Benefits**:
- Single source of truth
- Environment-specific configurations
- Easy parameter tuning
- No hardcoded values

## Processing Patterns

### 1. Incremental Processing (Producer)

- **Pattern**: Poll-based CDC simulation
- **Mechanism**: Timestamp-based filtering
- **Query**: `WHERE created_at > last_timestamp`
- **State**: Stored in file system
- **Frequency**: Configurable (default: 5 seconds)

### 2. Stream Processing (Consumer)

- **Pattern**: Micro-batch processing (Spark Structured Streaming)
- **Mechanism**: Continuous query execution
- **Processing Mode**: Append-only
- **State**: Managed via checkpoints
- **Latency**: Near real-time (depends on batch interval)

### 3. Exactly-Once Semantics

- **Producer**: Idempotent writes (timestamp-based deduplication)
- **Consumer**: Checkpoint-based offset management
- **Guarantee**: At-least-once delivery (can be upgraded to exactly-once with idempotent writes)

## Scalability Considerations

### Current Setup (Development)
- Single Kafka broker
- Single Spark executor (local mode)
- Single PostgreSQL instance
- No replication

### Production Considerations

1. **Kafka**:
   - Multiple brokers (3+)
   - Topic replication factor: 3
   - Multiple partitions for parallelism

2. **Spark**:
   - Cluster mode (YARN/Kubernetes)
   - Multiple executors
   - Dynamic resource allocation

3. **PostgreSQL**:
   - Read replicas for query load
   - Connection pooling
   - Proper indexing on `created_at`

4. **Data Lake**:
   - Object storage (S3, Azure Blob, GCS)
   - Partition optimization
   - Compaction strategies

## Fault Tolerance

### Producer Resilience
- Continues polling on errors
- Retries on connection failures
- Timestamp persistence ensures no data loss

### Consumer Resilience
- Checkpoint-based recovery
- Automatic offset management
- Restart capability from last checkpoint

### Infrastructure Resilience
- Health checks for all services
- Docker restart policies
- Persistent volumes for data

## Monitoring & Observability

### Available Interfaces

1. **Spark UI**: `http://localhost:8080`
   - Job progress
   - Stage details
   - Executor metrics

2. **Kafka Tools**:
   - `kafka-console-consumer` - View messages
   - `kafka-topics` - Topic management

3. **PostgreSQL**:
   - `psql` - Query interface
   - Logs via Docker

### Logging
- Spark logs: Container stdout/stderr
- Application logs: Print statements
- Docker logs: `docker-compose logs`

## Security Considerations

### Current Setup (Development)
- Plaintext connections
- Hardcoded credentials
- No encryption

### Production Recommendations
- SSL/TLS for all connections
- Secrets management (Vault, AWS Secrets Manager)
- Network policies
- Authentication/authorization
- Encryption at rest

## Performance Characteristics

### Latency
- **Producer Poll Interval**: 5 seconds (configurable)
- **Consumer Processing**: Micro-batch (typically < 1 second)
- **End-to-End**: ~5-10 seconds (from INSERT to Data Lake)

### Throughput
- Depends on:
  - Kafka broker capacity
  - Spark executor resources
  - Network bandwidth
  - Parquet write performance

### Storage Efficiency
- Parquet compression: ~70-80% size reduction
- Columnar format: Efficient for analytics queries
- Partitioning: Query optimization

## Deployment Architecture

### Development (Current)
```
Host Machine
├── Docker Compose
│   ├── PostgreSQL Container
│   ├── Zookeeper Container
│   ├── Kafka Container
│   └── Spark Container
└── Local Filesystem
    └── Data Lake (mounted volume)
```

### Production (Recommended)
```
Cloud Infrastructure
├── Managed PostgreSQL (RDS, Cloud SQL)
├── Managed Kafka (MSK, Confluent Cloud)
├── Spark Cluster (EMR, Databricks, Kubernetes)
└── Object Storage (S3, Azure Blob, GCS)
```

## Key Design Decisions

1. **Polling vs. True CDC**: Chosen polling for simplicity; production would use Debezium or native CDC
2. **Spark for Both**: Unified technology stack simplifies operations
3. **Parquet Format**: Columnar storage optimized for analytics
4. **Date Partitioning**: Enables efficient time-based queries
5. **Local Filesystem**: Development convenience; production uses object storage
6. **Docker Compose**: Easy local development and testing

## Extension Points

1. **Additional Data Sources**: Add more producers for other tables
2. **Stream Processing**: Add real-time aggregations, joins
3. **Data Quality**: Add validation rules, schema evolution
4. **Monitoring**: Integrate Prometheus, Grafana
5. **Alerting**: Set up alerts for failures, latency
6. **Multi-tenancy**: Support multiple roll numbers/topics

