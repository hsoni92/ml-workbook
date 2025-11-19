# Ecommerce Seller Recommendation

A Spark-based ETL pipeline for processing ecommerce data and generating seller recommendations.

## Prerequisites

- Docker and Docker Compose installed on your system

## How to Run

1. **Start the Spark cluster (As Container)**
   ```bash
   docker compose up -d
   ```

2. **Run the ETL pipeline and generate recommendations**

   Execute the ETL scripts in the following order:

   ```bash
   # Step 1: Process seller catalog data
   ./scripts/etl_seller_catalog_spark_submit.sh

   # Step 2: Process company sales data
   ./scripts/etl_company_sales_spark_submit.sh

   # Step 3: Process competitor sales data
   ./scripts/etl_competitor_sales_spark_submit.sh

   # Step 4: Generate seller recommendations
   ./scripts/consumption_recommendation_spark_submit.sh

   # Step 5: Visualize recommendations (optional)
   ./scripts/visualize_recommendations.sh
   ```

3. **View Spark Web UI** (optional)
   - Master: http://localhost:8080
   - Worker 1: http://localhost:8081
   - Worker 2: http://localhost:8082

4. **Stop the cluster** (when done)
   ```bash
   docker compose down -v
   ```

## What it does

The pipeline processes three datasets (seller catalog, company sales, competitor sales), performs data validation and cleaning, stores results in Hudi format, and generates seller recommendations with visualizations.

### Pipeline Components

1. **ETL Seller Catalog** (`etl_seller_catalog.py`)
   - Validates seller catalog data
   - Checks for missing item IDs and item names
   - Validates price and stock quantity fields
   - Stores clean data in Hudi format
   - Quarantines invalid records

2. **ETL Company Sales** (`etl_company_sales.py`)
   - Validates company sales transactions
   - Checks for missing item IDs
   - Validates sale dates and units sold
   - Stores clean data in Hudi format
   - Quarantines invalid records

3. **ETL Competitor Sales** (`etl_competitor_sales.py`)
   - Validates competitor sales data
   - Checks for missing seller IDs
   - Validates sale dates and marketplace prices
   - Stores clean data in Hudi format
   - Quarantines invalid records

4. **Consumption Recommendation** (`consumption_recommendation.py`)
   - Analyzes processed data from all three datasets
   - Generates seller recommendations based on sales performance
   - Outputs recommendations to CSV format

5. **Visualization** (`visualize_recommendations.py`)
   - Additional step to add some creativity and help visualize the final recommendation outcome per seller (S100-S150)
   - Creates visualizations of top products and sellers
   - Generates charts and graphs for analysis


## Configuration

The pipeline uses `configs/ecomm_prod.yml` to configure input and output paths. You can modify this file to change data locations or add new configurations.

## Output Locations

- **Processed Data (Hudi)**: `data/2025em1100506/processed/{dataset}_hudi/`
- **Recommendations**: `data/2025em1100506/processed/recommendations_csv/seller_recommend_data.csv`
- **Visualizations**: `data/2025em1100506/processed/recommendations_visualization/`
- **Quarantined Records**: `quarantine/{dataset}/{failure_reason}/{timestamp}/`

## Data Validation

The pipeline performs comprehensive data quality checks:

- **Missing Fields**: Records with missing required fields are quarantined
- **Invalid Dates**: Records with invalid date formats are quarantined
- **Invalid Numeric Values**: Records with negative or invalid numeric values are quarantined
- **Data Type Validation**: Ensures data types match expected schemas

All invalid records are automatically quarantined with metadata including:
- Dataset name
- Failure reason
- Quarantine timestamp
