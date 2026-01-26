# DSP Question Paper 1

## Question 1
**5 Marks**

Explain the difference between OLTP data stores and OLAP data stores. In your answer, describe their primary purpose, typical workloads, and give one example technology for each.

### Answer:

**OLTP (Online Transaction Processing) Data Stores:**
- **Primary Purpose**: Designed for managing day-to-day operational transactions and real-time business processes. They support high-frequency, short-duration transactions that are critical for business operations.
- **Typical Workloads**:
  - High volume of small, simple transactions (INSERT, UPDATE, DELETE)
  - Real-time data processing (e.g., processing orders, updating inventory)
  - Concurrent read/write operations with ACID compliance
  - Point queries and lookups by primary key
- **Example Technology**: PostgreSQL, MySQL, Oracle Database

**OLAP (Online Analytical Processing) Data Stores:**
- **Primary Purpose**: Optimized for complex analytical queries and business intelligence. They support decision-making through data analysis, reporting, and data mining.
- **Typical Workloads**:
  - Complex analytical queries with aggregations and joins
  - Read-heavy workloads with infrequent writes
  - Large-scale data scanning and analysis
  - Historical data analysis and trend identification
- **Example Technology**: Snowflake, Amazon Redshift, Google BigQuery

**Key Differences:**
- OLTP uses normalized schemas for data integrity, while OLAP uses denormalized/star/snowflake schemas for query performance
- OLTP prioritizes transaction speed and consistency, while OLAP prioritizes query performance and analytical capabilities
- OLTP handles current operational data, while OLAP stores historical and aggregated data

---

## Question 2
**10 Marks**

A retail chain wants to build a single view of inventory by combining data from:
- Store POS systems (multiple branches)
- Online sales platform
- Warehouse management system

### a)
**3 Marks**

Describe the key challenges in designing a data pipeline that integrates these heterogeneous data sources (mention at least data format, latency, and data quality).

**Answer:**

1. **Data Format Challenges:**
   - Store POS systems may use relational databases (SQL Server, Oracle) with structured schemas
   - Online sales platform might use NoSQL databases (MongoDB, DynamoDB) or REST APIs returning JSON
   - Warehouse management system could use flat files (CSV, EDI), XML, or proprietary formats
   - Need for schema mapping, data type conversions, and format standardization

2. **Latency Challenges:**
   - Store POS systems: Near real-time or batch updates (hourly/daily)
   - Online sales platform: Real-time or near real-time updates
   - Warehouse management: Batch updates (daily/weekly) or event-driven
   - Balancing real-time requirements with batch processing capabilities
   - Handling different update frequencies and ensuring data freshness

3. **Data Quality Challenges:**
   - Schema inconsistencies: Different field names, data types, and structures across sources
   - Missing or null values: Incomplete records from different systems
   - Duplicate records: Same transaction appearing in multiple systems
   - Data inconsistencies: Conflicting inventory counts across systems
   - Data validation: Ensuring referential integrity and business rule compliance
   - Timestamp synchronization: Different time zones and clock synchronization issues

### b)
**7 Marks**

Suggest a high-level pipeline architecture (staging → transformation → serving layer) and appropriate types of data stores for each layer.

**Answer:**

**High-Level Pipeline Architecture:**

**1. Staging Layer (Data Ingestion):**
- **Purpose**: Raw data landing zone where data is ingested from all sources in its original format
- **Data Store Type**: Object storage or distributed file system
- **Examples**:
  - Amazon S3, Azure Data Lake Storage (ADLS), Google Cloud Storage
  - HDFS (Hadoop Distributed File System)
- **Characteristics**:
  - Schema-on-read approach
  - Stores raw, unprocessed data
  - Supports multiple formats (JSON, CSV, Parquet, Avro)
  - Cost-effective for large volumes
  - Partitioned by source system and ingestion timestamp

**2. Transformation Layer (ETL/ELT Processing):**
- **Purpose**: Data cleaning, validation, standardization, and business logic application
- **Processing Framework**:
  - Apache Spark, Databricks, Apache Flink (for streaming)
  - ETL tools: Apache Airflow, Talend, Informatica
- **Key Operations**:
  - Schema mapping and data type conversion
  - Data quality checks and validation
  - Deduplication and conflict resolution
  - Data enrichment and aggregation
  - Business rule application (e.g., inventory reconciliation)
- **Output Storage**:
  - Processed data stored in columnar formats (Parquet, Delta Lake, Iceberg)
  - Stored in the same object storage or a separate processed zone

**3. Serving Layer (Analytics & Consumption):**
- **Purpose**: Fast query access for analytics, reporting, and applications
- **Data Store Type**: Analytical database or data warehouse
- **Examples**:
  - Cloud data warehouses: Snowflake, Amazon Redshift, Google BigQuery
  - Lakehouse platforms: Databricks SQL, Delta Lake with Spark SQL
  - OLAP databases: ClickHouse, Apache Druid (for real-time analytics)
- **Characteristics**:
  - Optimized for analytical queries (columnar storage)
  - Supports SQL-based access
  - Fast query performance with indexing and partitioning
  - Supports both batch and real-time analytics
  - Can serve BI tools, dashboards, and applications

**Additional Components:**
- **Metadata Management**: Data catalog (e.g., Apache Atlas, AWS Glue Catalog) for schema registry and lineage
- **Orchestration**: Workflow scheduler (e.g., Apache Airflow) for pipeline coordination
- **Monitoring**: Data quality monitoring and pipeline health checks

---

## Question 3
**10 Marks**

An online retail company wants to store raw clickstream logs, cleaned transactional data, and aggregated sales reports in a single platform that supports both cheap large storage and fast SQL analytics.

### a)
**5 Marks**

Briefly design a lakehouse architecture for this use case. Mention the main layers (e.g., raw, cleaned, aggregated) and what type of data is stored in each.

**Answer:**

**Lakehouse Architecture Design:**

**1. Raw/Bronze Layer:**
- **Data Type**: Raw clickstream logs in their original format
- **Storage Format**: JSON, CSV, or log files (e.g., Apache Log Format)
- **Characteristics**:
  - Unprocessed, immutable data
  - Preserves all original information
  - Partitioned by date/time and source
  - Used for data lineage and reprocessing
- **Example**: Raw web server logs, event streams from Kafka

**2. Cleaned/Silver Layer:**
- **Data Type**: Cleaned transactional data
- **Storage Format**: Columnar formats like Parquet, Delta Lake, or Iceberg
- **Characteristics**:
  - Data quality checks applied (removed duplicates, null handling)
  - Schema validation and standardization
  - Data type conversions and normalization
  - Enriched with reference data (e.g., product catalog, customer info)
  - Partitioned and optimized for query performance
- **Example**: Cleaned sales transactions, validated customer orders, standardized product data

**3. Aggregated/Gold Layer:**
- **Data Type**: Aggregated sales reports and business metrics
- **Storage Format**: Pre-aggregated tables in Parquet/Delta format
- **Characteristics**:
  - Business-level aggregations (daily/weekly/monthly sales)
  - Pre-computed metrics and KPIs
  - Star/snowflake schema for dimensional modeling
  - Optimized for fast analytical queries
- **Example**: Daily sales by product category, monthly revenue reports, customer lifetime value metrics

**Technology Stack:**
- **Storage**: Object storage (S3, ADLS) with Delta Lake or Apache Iceberg for ACID transactions
- **Processing**: Apache Spark or Databricks for transformations
- **Query Engine**: Spark SQL, Databricks SQL, or Presto/Trino for SQL analytics
- **Metadata**: Delta Lake transaction log or Apache Iceberg metadata for schema evolution

### b)
**5 Marks**

Explain two benefits of using a lakehouse instead of keeping a separate data lake and data warehouse.

**Answer:**

**Benefit 1: Unified Data Storage and Reduced Data Duplication**
- **Traditional Approach**: Data is stored in both the data lake (raw/processed files) and data warehouse (structured tables), leading to duplication and increased storage costs
- **Lakehouse Approach**: Single storage layer (object storage) serves both purposes. Raw data, cleaned data, and aggregated data all reside in the same storage system
- **Advantages**:
  - Eliminates data duplication and reduces storage costs
  - Single source of truth for all data
  - No need for ETL processes to copy data from lake to warehouse
  - Easier data governance and lineage tracking

**Benefit 2: ACID Transactions and Schema Enforcement with Cost-Effective Storage**
- **Traditional Approach**: Data lakes lack ACID transactions and schema enforcement, requiring a data warehouse for reliable analytics. However, data warehouses are expensive for large-scale storage
- **Lakehouse Approach**: Technologies like Delta Lake and Apache Iceberg provide ACID transactions, schema enforcement, and time travel capabilities on top of cost-effective object storage
- **Advantages**:
  - Supports concurrent reads and writes with ACID guarantees
  - Schema evolution and enforcement without data warehouse costs
  - Time travel and versioning capabilities for data auditing
  - Combines the cost benefits of data lakes with the reliability of data warehouses
  - Enables both batch and streaming workloads on the same platform

---

## Question 4
**10 Marks**

Assume a Kafka topic `clicks` received the following three messages within the same 10-second window:

**Text is as follows:**
- home
- product
- home

**Spark code:**
```scala
import org.apache.spark.sql.functions._
import spark.implicits._

val df = spark.readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "localhost:9092")
  .option("subscribe", "clicks")
  .load()

val clicks = df.selectExpr("CAST(value AS STRING) as page")
  .withColumn("ts", current_timestamp())

val counts = clicks
  .groupBy(
    window($"ts", "10 seconds"),
    $"page"
  )
  .count()
  .orderBy("page")

val query = counts.writeStream
  .outputMode("complete")
  .format("console")
  .start()
```

### a)
**7 Marks**

Assuming all three messages fall into the same 10-second window, what is the output for each page and count? (You can ignore the exact window start/end times.)

**Answer:**

Given that all three messages ("home", "product", "home") fall into the same 10-second window, and the code uses `outputMode("complete")` with `groupBy(window($"ts", "10 seconds"), $"page")`, the output will be:

```
+------------------------------------------+-------+-----+
| window                                   | page  | count |
+------------------------------------------+-------+-----+
| [2024-01-01 10:00:00, 2024-01-01 10:00:10] | home    | 2    |
| [2024-01-01 10:00:00, 2024-01-01 10:00:10] | product | 1    |
+------------------------------------------+-------+-----+
```

**Output Summary:**
- **home**: count = 2 (appears twice in the three messages)
- **product**: count = 1 (appears once in the three messages)

The results are ordered by "page" as specified in the `.orderBy("page")` clause, so "home" appears before "product".

### b)
**3 Marks**

Briefly explain why the output has those counts for home and product based on how the `groupBy(window($"ts", "10 seconds"), $"page")` works.

**Answer:**

The `groupBy(window($"ts", "10 seconds"), $"page")` operation works as follows:

1. **Window Function**: `window($"ts", "10 seconds")` creates tumbling windows of 10-second duration. Since all three messages arrive within the same 10-second window, they are grouped into a single window.

2. **Page Grouping**: The `groupBy` operation groups records by both the window and the page value. This means:
   - All records with the same window and page="home" are grouped together
   - All records with the same window and page="product" are grouped together

3. **Count Aggregation**: The `.count()` function counts the number of records in each group:
   - The group (window, "home") contains 2 records (the first "home" and the second "home")
   - The group (window, "product") contains 1 record (the single "product" message)

4. **Complete Output Mode**: With `outputMode("complete")`, Spark outputs the complete aggregated results for each window, showing all groups (home and product) with their respective counts, even if a group has zero records in subsequent windows.

Therefore, the output correctly shows home=2 and product=1, reflecting the actual count of each page type within the 10-second window.
