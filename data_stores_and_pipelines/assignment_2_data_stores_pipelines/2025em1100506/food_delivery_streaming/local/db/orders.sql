-- Create orders table for food delivery platform
CREATE TABLE IF NOT EXISTS "2025em1100506_orders" (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    restaurant_name VARCHAR(255) NOT NULL,
    item VARCHAR(255) NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    order_status VARCHAR(50) NOT NULL CHECK (order_status IN ('PLACED', 'PREPARING', 'DELIVERED', 'CANCELLED')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial sample records (at least 10 records)
INSERT INTO "2025em1100506_orders" (customer_name, restaurant_name, item, amount, order_status, created_at) VALUES
('Rajesh Kumar', 'Paradise Biryani', 'Chicken Biryani', 280.00, 'PLACED', '2025-01-15 10:30:00'),
('Priya Sharma', 'Saravana Bhavan', 'Masala Dosa', 120.00, 'PREPARING', '2025-01-15 11:15:00'),
('Amit Patel', 'Bikaner Sweets', 'Chole Bhature', 150.00, 'DELIVERED', '2025-01-15 09:45:00'),
('Anjali Reddy', 'Karims', 'Butter Chicken', 350.00, 'PLACED', '2025-01-15 12:00:00'),
('Vikram Singh', 'Haldiram', 'Raj Kachori', 180.00, 'PREPARING', '2025-01-15 12:30:00'),
('Kavita Nair', 'Paradise Biryani', 'Mutton Biryani', 420.00, 'DELIVERED', '2025-01-15 10:00:00'),
('Rahul Gupta', 'Saravana Bhavan', 'Idli Sambar', 90.00, 'PLACED', '2025-01-15 13:00:00'),
('Meera Iyer', 'Karims', 'Chicken Korma', 380.00, 'PREPARING', '2025-01-15 13:30:00'),
('Suresh Menon', 'Bikaner Sweets', 'Pav Bhaji', 140.00, 'DELIVERED', '2025-01-15 11:00:00'),
('Deepika Joshi', 'Haldiram', 'Chaat Platter', 200.00, 'PLACED', '2025-01-15 14:00:00'),
('Arjun Malhotra', 'Paradise Biryani', 'Veg Biryani', 220.00, 'PREPARING', '2025-01-15 14:30:00'),
('Sunita Desai', 'Saravana Bhavan', 'Uttapam', 110.00, 'PLACED', '2025-01-15 15:00:00');

-- Verify table creation and data
SELECT COUNT(*) as total_orders FROM "2025em1100506_orders";
SELECT * FROM "2025em1100506_orders" ORDER BY created_at;

