# Assignment Plan: Ecommerce Top-Seller Items Recommendation System

## Overview
Build a recommendation system that analyzes sales data and recommends top-selling items to sellers that they don't currently have in their catalog.

## Project Structure Setup

### Step 1: Create Project Directory Structure
```
<rollnumber>/ecommerce_seller_recommendation/<s3 or local>/
├── configs/
│   └── ecomm_prod.yml
├── src/
│   ├── etl_seller_catalog.py
│   ├── etl_company_sales.py
│   ├── etl_competitor_sales.py
│   └── consumption_recommendation.py
├── scripts/
│   ├── etl_seller_catalog_spark_submit.sh
│   ├── etl_company_sales_spark_submit.sh
│   ├── etl_competitor_sales_spark_submit.sh
│   └── consumption_recommendation_spark_submit.sh
└── README.md (optional)
```

---

## Phase 1: Configuration Setup

### Step 2: Create Configuration File (`configs/ecomm_prod.yml`)
- Define input paths for raw CSV files (seller_catalog, company_sales, competitor_sales)
- Define Hudi output paths for each ETL pipeline
- Define Hudi input paths and CSV output path for consumption layer
- Use the sample structure provided in ASSIGNMENT.md

---

## Phase 2: ETL Pipelines (3 separate pipelines)

### Step 3: Create Common Utilities Module
**File:** `src/utils.py` (optional helper module)
- Function: `get_spark_session(app_name)` - Initialize Spark session with required configs
- Function: `load_yaml_config(config_path)` - Load and parse YAML config
- Function: `write_to_quarantine(df, quarantine_path, dataset_name, failure_reason)` - Write failed records to quarantine zone

### Step 4: ETL Pipeline 1 - Seller Catalog (`src/etl_seller_catalog.py`)

**Input:** CSV file from `seller_catalog.input_path` in config

**Process:**
1. **Read raw data** from CSV
2. **Bronze Layer:** Load raw data as-is
3. **Data Cleaning (Silver Layer):**
   - Trim whitespace: seller_id, item_id, item_name, category
   - Normalize casing:
     - item_name → Title Case
     - category → Standardized labels (Electronics, Apparel, etc.)
   - Convert types: marketplace_price → DOUBLE, stock_qty → INT
   - Fill missing stock_qty with 0
   - Remove duplicates based on (seller_id + item_id)
4. **DQ Checks (Gold Layer):**
   - Check seller_id IS NOT NULL → Quarantine if fails
   - Check item_id IS NOT NULL → Quarantine if fails
   - Check marketplace_price >= 0 → Quarantine if fails
   - Check stock_qty >= 0 → Quarantine if fails
   - Check item_name IS NOT NULL → Quarantine if fails
   - Check category IS NOT NULL → Quarantine if fails
5. **Quarantine Zone:**
   - Write failed records to quarantine path with:
     - Original record
     - Dataset name: "seller_catalog"
     - dq_failure_reason (e.g., "missing_seller_id", "negative_price")
6. **Write to Hudi:**
   - Use Hudi with overwrite mode
   - Key: seller_id + item_id
   - Output to `seller_catalog.hudi_output_path`

### Step 5: ETL Pipeline 2 - Company Sales (`src/etl_company_sales.py`)

**Input:** CSV file from `company_sales.input_path` in config

**Process:**
1. **Read raw data** from CSV
2. **Bronze Layer:** Load raw data as-is
3. **Data Cleaning (Silver Layer):**
   - Trim strings: item_id
   - Convert types: units_sold → INT, revenue → DOUBLE, sale_date → DATE
   - Fill missing units_sold or revenue with 0
   - Standardize sale_date format
   - Remove duplicates based on item_id
4. **DQ Checks (Gold Layer):**
   - Check item_id IS NOT NULL → Quarantine if fails
   - Check units_sold >= 0 → Quarantine if fails
   - Check revenue >= 0 → Quarantine if fails
   - Check sale_date IS NOT NULL AND sale_date <= current_date() → Quarantine if fails
5. **Quarantine Zone:**
   - Write failed records with dataset name "company_sales" and failure reason
6. **Write to Hudi:**
   - Use Hudi with overwrite mode
   - Key: item_id
   - Output to `company_sales.hudi_output_path`

### Step 6: ETL Pipeline 3 - Competitor Sales (`src/etl_competitor_sales.py`)

**Input:** CSV file from `competitor_sales.input_path` in config

**Process:**
1. **Read raw data** from CSV
2. **Bronze Layer:** Load raw data as-is
3. **Data Cleaning (Silver Layer):**
   - Trim strings: item_id, seller_id
   - Normalize casing: seller_id
   - Convert types: units_sold → INT, revenue → DOUBLE, marketplace_price → DOUBLE, sale_date → DATE
   - Fill missing numeric fields (units_sold, revenue, marketplace_price) with 0
   - Remove duplicates based on (seller_id + item_id)
4. **DQ Checks (Gold Layer):**
   - Check item_id IS NOT NULL → Quarantine if fails
   - Check seller_id IS NOT NULL → Quarantine if fails
   - Check units_sold >= 0 → Quarantine if fails
   - Check revenue >= 0 → Quarantine if fails
   - Check marketplace_price >= 0 → Quarantine if fails
   - Check sale_date IS NOT NULL AND sale_date <= current_date() → Quarantine if fails
5. **Quarantine Zone:**
   - Write failed records with dataset name "competitor_sales" and failure reason
6. **Write to Hudi:**
   - Use Hudi with overwrite mode
   - Key: seller_id + item_id
   - Output to `competitor_sales.hudi_output_path`

---

## Phase 3: Consumption Layer

### Step 7: Create Consumption Pipeline (`src/consumption_recommendation.py`)

**Input:** 3 Hudi tables from previous ETL pipelines

**Process:**
1. **Read Hudi Tables:**
   - Read seller_catalog_hudi
   - Read company_sales_hudi
   - Read competitor_sales_hudi

2. **Data Transformations:**
   - **Aggregate Company Sales:**
     - Group by item_id and category
     - Calculate total units_sold per item
     - Find top 10 selling items per category

   - **Aggregate Competitor Sales:**
     - Group by item_id
     - Calculate total units_sold per item
     - Find top-selling items in the market
     - Get marketplace_price (average or latest)

   - **Identify Missing Items:**
     - For each seller:
       - Get their current catalog items (from seller_catalog_hudi)
       - Compare with company top-selling items → find missing
       - Compare with competitor top-selling items → find missing
       - Combine both sets of missing items

3. **Recommendation Calculation:**
   For each missing item per seller:
   - **market_price:** Get from competitor_sales or company_sales (prefer competitor if available)
   - **expected_units_sold:**
     ```
     expected_units_sold = total units sold for the item / number of sellers selling this item
     ```
   - **expected_revenue:**
     ```
     expected_revenue = expected_units_sold * marketplace_price
     ```
   - Get item_name and category from company_sales or competitor_sales

4. **Output:**
   - Columns: seller_id, item_id, item_name, category, market_price, expected_units_sold, expected_revenue
   - Write to CSV with overwrite mode
   - Output path: `recommendation.output_csv`

---

## Phase 4: Spark Submit Scripts

### Step 8: Create Spark Submit Scripts

**For each ETL pipeline (`scripts/etl_*_spark_submit.sh`):**
```bash
spark-submit \
  --packages org.apache.hudi:hudi-spark3.5-bundle_2.12:0.15.0,org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262 \
  --conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
  --conf spark.sql.legacy.timeParserPolicy=LEGACY \
  <rollnumber>/ecommerce_seller_recommendation/src/<program name>.py \
  --config configs/ecomm_prod.yml
```

**Create 4 scripts:**
- `etl_seller_catalog_spark_submit.sh`
- `etl_company_sales_spark_submit.sh`
- `etl_competitor_sales_spark_submit.sh`
- `consumption_recommendation_spark_submit.sh`

---

## Phase 5: Implementation Checklist

### ETL Pipelines Checklist:
- [ ] YAML config loading implemented
- [ ] CSV reading with Spark
- [ ] Bronze layer: Raw data loading
- [ ] Silver layer: Data cleaning (trim, normalize, type conversion, deduplication)
- [ ] Gold layer: DQ checks implemented
- [ ] Quarantine zone: Failed records written with metadata
- [ ] Hudi write with overwrite mode
- [ ] Schema evolution support (Hudi handles this automatically)
- [ ] Incremental upsert capability (Hudi handles this)

### Consumption Pipeline Checklist:
- [ ] Read all 3 Hudi tables
- [ ] Aggregate company sales (top 10 per category)
- [ ] Aggregate competitor sales (top-selling items)
- [ ] Identify missing items per seller
- [ ] Calculate market_price
- [ ] Calculate expected_units_sold
- [ ] Calculate expected_revenue
- [ ] Output to CSV with overwrite mode

### Testing Checklist:
- [ ] Test with sample data
- [ ] Verify quarantine zone captures bad records
- [ ] Verify Hudi tables are created correctly
- [ ] Verify recommendations output format
- [ ] Test with incremental data (if applicable)

---

## Phase 6: Execution Order

1. **Run ETL Pipelines (can run in parallel or sequentially):**
   ```bash
   ./scripts/etl_seller_catalog_spark_submit.sh
   ./scripts/etl_company_sales_spark_submit.sh
   ./scripts/etl_competitor_sales_spark_submit.sh
   ```

2. **Run Consumption Pipeline (after all ETL pipelines complete):**
   ```bash
   ./scripts/consumption_recommendation_spark_submit.sh
   ```

---

## Key Technical Points

### Apache Hudi Configuration:
- Use `COPY_ON_WRITE` or `MERGE_ON_READ` table type
- Set record key appropriately (seller_id+item_id or item_id)
- Use overwrite mode for initial loads
- Enable schema evolution

### Medallion Architecture:
- **Bronze:** Raw data as-is
- **Silver:** Cleaned data (after data cleaning steps)
- **Gold:** Validated data (after DQ checks)
- **Quarantine:** Failed records with metadata

### Data Quality Checks:
- Implement each DQ rule as a filter condition
- Collect failed records before filtering
- Write failed records to quarantine with failure reason
- Only pass records that pass all DQ checks to gold layer

### Recommendation Logic:
- Top 10 items per category from company sales
- Top-selling items from competitor sales
- Missing items = items not in seller's catalog but in top-selling lists
- Calculate expected metrics based on historical performance

---

## Deliverables Summary

1. ✅ Project structure with all directories
2. ✅ `configs/ecomm_prod.yml` configuration file
3. ✅ 3 ETL Python scripts (seller_catalog, company_sales, competitor_sales)
4. ✅ 1 Consumption Python script (recommendation)
5. ✅ 4 Spark submit shell scripts
6. ✅ Optional README.md

---

## Notes

- All pipelines should be idempotent (can run multiple times safely)
- Use Hudi version 0.15.0 as specified
- Ensure S3 buckets have global access if using S3
- Test with sample data before final submission
- Follow the exact project structure provided

