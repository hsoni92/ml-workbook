# AWS Databases Overview

## Relational services
- RDS supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Aurora.
- Aurora is AWS-designed relational engine compatible with MySQL/PostgreSQL APIs.
- Use relational services for OLTP systems needing transactions and SQL.

## NoSQL and specialty
- DynamoDB is serverless key-value/document database.
- ElastiCache accelerates reads with Redis/Memcached caching.
- Neptune handles graph relationships; DocumentDB handles MongoDB-compatible document workloads.

## Analytics distinction
- Redshift is columnar data warehouse for analytics.
- Athena queries data in S3 using SQL.
- Do not confuse OLTP database with analytics warehouse in scenario questions.
