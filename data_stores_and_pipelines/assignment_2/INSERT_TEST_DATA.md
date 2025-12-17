# How to Insert Test Data in PostgreSQL

This guide shows multiple ways to insert test data into the PostgreSQL database for testing the streaming pipeline.

## Prerequisites

- Docker containers must be running: `docker-compose up -d`
- PostgreSQL service must be healthy

## Method 1: Interactive psql Session (Recommended for Testing)

### Step 1: Connect to PostgreSQL

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db
```

### Step 2: Insert Test Data

Once connected, run SQL commands:

```sql
-- Insert single record
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) 
VALUES ('Test User 1', 'Test Restaurant', 'Test Item 1', 100.00, 'PLACED', CURRENT_TIMESTAMP);

-- Insert multiple records (recommended for testing)
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES
('Test User 1', 'Test Restaurant', 'Test Item 1', 100.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 2', 'Test Restaurant', 'Test Item 2', 200.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 3', 'Test Restaurant', 'Test Item 3', 300.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 4', 'Test Restaurant', 'Test Item 4', 400.00, 'PLACED', CURRENT_TIMESTAMP),
('Test User 5', 'Test Restaurant', 'Test Item 5', 500.00, 'PLACED', CURRENT_TIMESTAMP);
```

### Step 3: Verify Insertion

```sql
-- Check count
SELECT COUNT(*) FROM "2025em1100506_orders";

-- View recent records
SELECT * FROM "2025em1100506_orders" ORDER BY created_at DESC LIMIT 10;

-- View records with specific status
SELECT * FROM "2025em1100506_orders" WHERE order_status = 'PLACED';
```

### Step 4: Exit psql

```sql
\q
```

## Method 2: One-Line Command (Quick Insert)

Insert data directly without entering interactive mode:

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "INSERT INTO \"2025em1100506_orders\" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES ('Quick Test User', 'Quick Restaurant', 'Quick Item', 150.00, 'PLACED', CURRENT_TIMESTAMP);"
```

Insert multiple records:

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "INSERT INTO \"2025em1100506_orders\" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES ('Batch User 1', 'Batch Restaurant', 'Batch Item 1', 100.00, 'PLACED', CURRENT_TIMESTAMP), ('Batch User 2', 'Batch Restaurant', 'Batch Item 2', 200.00, 'PLACED', CURRENT_TIMESTAMP), ('Batch User 3', 'Batch Restaurant', 'Batch Item 3', 300.00, 'PLACED', CURRENT_TIMESTAMP);"
```

## Method 3: Using SQL File

### Step 1: Create a SQL file

Create `test_data.sql`:

```sql
-- Insert test records for incremental ingestion testing
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES
('Incremental Test 1', 'Test Restaurant', 'Test Item 1', 100.00, 'PLACED', CURRENT_TIMESTAMP),
('Incremental Test 2', 'Test Restaurant', 'Test Item 2', 200.00, 'PREPARING', CURRENT_TIMESTAMP),
('Incremental Test 3', 'Test Restaurant', 'Test Item 3', 300.00, 'DELIVERED', CURRENT_TIMESTAMP),
('Incremental Test 4', 'Test Restaurant', 'Test Item 4', 400.00, 'PLACED', CURRENT_TIMESTAMP),
('Incremental Test 5', 'Test Restaurant', 'Test Item 5', 500.00, 'CANCELLED', CURRENT_TIMESTAMP);
```

### Step 2: Execute the SQL file

```bash
docker exec -i food_delivery_postgres psql -U student -d food_delivery_db < test_data.sql
```

Or copy file into container first:

```bash
docker cp test_data.sql food_delivery_postgres:/tmp/test_data.sql
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -f /tmp/test_data.sql
```

## Method 4: Python Script (Programmatic)

Create a Python script `insert_test_data.py`:

```python
import psycopg2
from datetime import datetime

# Connection parameters
conn_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'food_delivery_db',
    'user': 'student',
    'password': 'student123'
}

# Connect to database
conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

# Insert test data
test_records = [
    ('Python Test 1', 'Python Restaurant', 'Python Item 1', 100.00, 'PLACED'),
    ('Python Test 2', 'Python Restaurant', 'Python Item 2', 200.00, 'PREPARING'),
    ('Python Test 3', 'Python Restaurant', 'Python Item 3', 300.00, 'DELIVERED'),
]

insert_query = """
INSERT INTO "2025em1100506_orders" 
(customer_name, restaurant_name, item, amount, order_status, created_at) 
VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
"""

cur.executemany(insert_query, test_records)
conn.commit()

print(f"Inserted {len(test_records)} records")

# Verify
cur.execute('SELECT COUNT(*) FROM "2025em1100506_orders"')
count = cur.fetchone()[0]
print(f"Total records in table: {count}")

cur.close()
conn.close()
```

Run it:

```bash
python3 insert_test_data.py
```

## Sample Test Data Templates

### Template 1: Basic Test Records

```sql
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES
('Alice Johnson', 'Burger King', 'Whopper', 250.00, 'PLACED', CURRENT_TIMESTAMP),
('Bob Smith', 'Pizza Hut', 'Pepperoni Pizza', 380.00, 'PREPARING', CURRENT_TIMESTAMP),
('Carol White', 'KFC', 'Chicken Bucket', 450.00, 'DELIVERED', CURRENT_TIMESTAMP),
('David Brown', 'Subway', 'Veggie Sub', 180.00, 'PLACED', CURRENT_TIMESTAMP),
('Emma Davis', 'McDonald''s', 'Big Mac', 220.00, 'CANCELLED', CURRENT_TIMESTAMP);
```

### Template 2: Different Order Statuses

```sql
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES
('Status Test 1', 'Restaurant A', 'Item A', 100.00, 'PLACED', CURRENT_TIMESTAMP),
('Status Test 2', 'Restaurant B', 'Item B', 200.00, 'PREPARING', CURRENT_TIMESTAMP),
('Status Test 3', 'Restaurant C', 'Item C', 300.00, 'DELIVERED', CURRENT_TIMESTAMP),
('Status Test 4', 'Restaurant D', 'Item D', 400.00, 'CANCELLED', CURRENT_TIMESTAMP);
```

### Template 3: Different Amounts (for Data Cleaning Tests)

```sql
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES
('Amount Test 1', 'Restaurant', 'Item 1', 50.00, 'PLACED', CURRENT_TIMESTAMP),
('Amount Test 2', 'Restaurant', 'Item 2', 0.00, 'PLACED', CURRENT_TIMESTAMP),
('Amount Test 3', 'Restaurant', 'Item 3', -10.00, 'PLACED', CURRENT_TIMESTAMP),  -- Should be filtered out
('Amount Test 4', 'Restaurant', 'Item 4', 1000.00, 'PLACED', CURRENT_TIMESTAMP);
```

## Verification Commands

### Check Total Record Count

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "SELECT COUNT(*) FROM \"2025em1100506_orders\";"
```

### View Recent Records

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "SELECT * FROM \"2025em1100506_orders\" ORDER BY created_at DESC LIMIT 10;"
```

### View Records by Status

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "SELECT order_status, COUNT(*) FROM \"2025em1100506_orders\" GROUP BY order_status;"
```

### View Records Created Today

```bash
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "SELECT * FROM \"2025em1100506_orders\" WHERE DATE(created_at) = CURRENT_DATE ORDER BY created_at DESC;"
```

## Testing Incremental Ingestion

### Step 1: Check Last Processed Timestamp

```bash
cat datalake/food/2025em1100506/lastprocess/orders
```

### Step 2: Insert New Records

Use any method above to insert new records with `CURRENT_TIMESTAMP`.

### Step 3: Wait for Processing

Wait 5-10 seconds for the producer to poll and process.

### Step 4: Verify Pipeline

```bash
# Check Kafka messages
docker exec -it food_delivery_kafka kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic 2025em1100506_food_orders_raw \
  --from-beginning \
  --max-messages 5

# Check Data Lake
ls -la datalake/food/2025em1100506/output/orders/
```

## Troubleshooting

### Table Not Found

If you get "relation does not exist" error:

```bash
# Check if table exists
docker exec -it food_delivery_postgres psql -U student -d food_delivery_db -c "\dt"

# If table doesn't exist, recreate it
docker exec -i food_delivery_postgres psql -U student -d food_delivery_db < db/orders.sql
```

### Connection Refused

```bash
# Check if PostgreSQL is running
docker-compose ps

# Check PostgreSQL logs
docker-compose logs postgres

# Restart PostgreSQL
docker-compose restart postgres
```

### Permission Denied

Make sure you're using the correct user (`student`) and database (`food_delivery_db`).

## Quick Reference

**Table Name**: `"2025em1100506_orders"` (note the quotes - required because it starts with a number)

**Required Fields**:
- `customer_name` (VARCHAR)
- `restaurant_name` (VARCHAR)
- `item` (VARCHAR)
- `amount` (NUMERIC)
- `order_status` (VARCHAR) - Must be: PLACED, PREPARING, DELIVERED, or CANCELLED
- `created_at` (TIMESTAMP) - Use CURRENT_TIMESTAMP for new records

**Auto-generated**: `order_id` (SERIAL PRIMARY KEY)

