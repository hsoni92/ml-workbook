# Week 9: Managed Databases and Data Models

## Database choice mindset
- Start with query pattern, consistency need, schema shape, and scaling requirement.
- Managed databases reduce patching, backups, failover, and operational burden.
- Wrong data model creates long-term pain that infrastructure tuning cannot fix.

## AWS map
- RDS for relational engines and SQL workloads.
- Aurora for cloud-optimized relational scale/availability.
- DynamoDB for key-value/document access at very high scale.
- Redshift is analytics warehouse, not OLTP replacement.

## Exam focus
- Multi-AZ is availability, read replica is read scale.
- NoSQL is not automatically better; it depends on access pattern.
- Backups matter only if restore works within RPO/RTO.
