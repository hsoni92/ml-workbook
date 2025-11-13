# Docker Setup Guide

This guide explains how to use Docker Compose to run Apache Spark for the Ecommerce Seller Recommendation System assignment.

**Note**: This setup uses `bitnami/spark:3.5.0` image which includes Python/PySpark support. The image uses `/opt/bitnami/spark` as the base path instead of `/opt/spark`.

## Prerequisites

- Docker Desktop installed and running
- Docker Compose (usually included with Docker Desktop)
- At least 4GB of available RAM (for Spark workers)

## Architecture

The docker-compose setup includes:

1. **spark-master**: Spark Master node (coordinates jobs)
   - Web UI: http://localhost:8080
   - Master Port: 7077

2. **spark-worker-1**: First Spark Worker node (executes tasks)
   - Web UI: http://localhost:8081

3. **spark-worker-2**: Second Spark Worker node (executes tasks)
   - Web UI: http://localhost:8082

## Quick Start

### 1. Start the Spark Cluster

```bash
# Start all containers
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f spark-master
```

### 2. Verify Spark Cluster is Running

- Spark Master UI: http://localhost:8080
- You should see 2 workers registered

### 3. Run Your ETL Pipelines

#### Option A: Run from Host Machine (Recommended)

```bash
# Make sure Spark is installed locally or use Docker exec
docker exec -it spark-master spark-submit \
  --master spark://spark-master:7077 \
  --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 \
  --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
  --conf spark.sql.legacy.timeParserPolicy=LEGACY \
  /opt/bitnami/spark/work-dir/src/etl_seller_catalog.py \
  --config /opt/bitnami/spark/work-dir/configs/ecomm_prod.yml
```

#### Option B: Use Modified Scripts

Update your spark-submit scripts to use the container:

```bash
# Example: scripts/etl_seller_catalog_spark_submit.sh
docker exec -it spark-master spark-submit \
  --master spark://spark-master:7077 \
  --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 \
  --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
  --conf spark.sql.legacy.timeParserPolicy=LEGACY \
  /opt/bitnami/spark/work-dir/src/etl_seller_catalog.py \
  --config /opt/bitnami/spark/work-dir/configs/ecomm_prod.yml
```

### 4. Stop the Cluster

```bash
# Stop containers
docker-compose down

# Stop and remove volumes (cleans up logs)
docker-compose down -v
```

## Directory Structure

The following directories are mounted as volumes:

```
./src          → /opt/bitnami/spark/work-dir/src          (Your Python scripts)
./configs      → /opt/bitnami/spark/work-dir/configs      (YAML config files)
./scripts      → /opt/bitnami/spark/work-dir/scripts      (Shell scripts)
./data         → /opt/bitnami/spark/work-dir/data         (Input/output data)
./quarantine   → /opt/bitnami/spark/work-dir/quarantine  (Failed records)
```

**Important**: Make sure your `ecomm_prod.yml` uses paths that match the container paths:
- Input paths: `/opt/bitnami/spark/work-dir/data/raw/...`
- Output paths: `/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/...`

## Configuration

### Update Config File for Docker

Your `configs/ecomm_prod.yml` should use container paths:

```yaml
seller_catalog:
  input_path: "/opt/bitnami/spark/work-dir/data/raw/seller_catalog/seller_catalog_clean.csv"
  hudi_output_path: "/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/seller_catalog_hudi/"

company_sales:
  input_path: "/opt/bitnami/spark/work-dir/data/raw/company_sales/company_sales_clean.csv"
  hudi_output_path: "/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/company_sales_hudi/"

competitor_sales:
  input_path: "/opt/bitnami/spark/work-dir/data/raw/competitor_sales/competitor_sales_clean.csv"
  hudi_output_path: "/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/competitor_sales_hudi/"

recommendation:
  seller_catalog_hudi: "/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/seller_catalog_hudi/"
  company_sales_hudi: "/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/company_sales_hudi/"
  competitor_sales_hudi: "/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/competitor_sales_hudi/"
  output_csv: "/opt/bitnami/spark/work-dir/data/<rollnumber>/processed/recommendations_csv/seller_recommend_data.csv"
```

## Troubleshooting

### Check Container Logs

```bash
# All containers
docker-compose logs

# Specific container
docker-compose logs spark-master
docker-compose logs spark-worker-1
```

### Restart Containers

```bash
# Restart all
docker-compose restart

# Restart specific service
docker-compose restart spark-master
```

### Access Container Shell

```bash
# Access spark-master shell
docker exec -it spark-master bash

# Check Spark version
docker exec -it spark-master spark-submit --version
```

### Common Issues

1. **Workers not connecting to master**
   - Check if master is running: `docker-compose ps`
   - Check master logs: `docker-compose logs spark-master`
   - Verify network: `docker network ls`

2. **Port conflicts**
   - Change ports in docker-compose.yml if 8080, 7077, etc. are already in use

3. **Out of memory**
   - Reduce `SPARK_WORKER_MEMORY` in docker-compose.yml
   - Reduce number of workers

## Monitoring

- **Spark Master UI**: http://localhost:8080
  - View cluster status
  - Monitor running applications
  - Check worker status

- **Worker UIs**:
  - Worker 1: http://localhost:8081
  - Worker 2: http://localhost:8082

## Resource Requirements

- **Minimum**: 4GB RAM, 2 CPU cores
- **Recommended**: 8GB RAM, 4 CPU cores
- Adjust `SPARK_WORKER_CORES` and `SPARK_WORKER_MEMORY` in docker-compose.yml based on your system

## Alternative: Single Container Setup

If you want a simpler setup with just one Spark container:

```bash
docker run -it \
  -p 8080:8080 \
  -p 7077:7077 \
  -v $(pwd)/src:/opt/bitnami/spark/work-dir/src \
  -v $(pwd)/configs:/opt/bitnami/spark/work-dir/configs \
  -v $(pwd)/data:/opt/bitnami/spark/work-dir/data \
  apache/spark-py:3.5.0 \
  bin/spark-class org.apache.spark.deploy.master.Master
```

But docker-compose is recommended for better resource management and scalability.

