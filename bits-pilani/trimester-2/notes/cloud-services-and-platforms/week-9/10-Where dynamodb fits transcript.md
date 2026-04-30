# Where DynamoDB Fits

## Strong fits
- User sessions, shopping carts, leaderboards, device telemetry, metadata, and high-scale lookup tables.
- Applications with known access patterns and need for single-digit millisecond latency.
- Serverless architectures where Lambda needs scalable key-value storage.

## Weak fits
- Complex joins and relational integrity requirements.
- Ad hoc reporting over many attributes.
- Frequent multi-item transactions across broad data sets.

## Exam decision
- Choose DynamoDB when the question emphasizes scale, low latency, serverless, and key-based access.
- Choose RDS when the question emphasizes SQL joins, ACID transactions, and relational constraints.
- Choose analytics services when the question asks about BI/reporting across large historical data.
