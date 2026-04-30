# DynamoDB Concepts

## Data model
- Table contains items; item contains attributes.
- Partition key determines physical distribution and required access path.
- Sort key enables range queries and composite primary key patterns.

## Indexes
- Local Secondary Index uses same partition key with different sort key.
- Global Secondary Index uses different key schema for alternate access pattern.
- Indexes cost capacity and must be planned from query requirements.

## Operational behavior
- DynamoDB is serverless and automatically partitions data.
- Hot partitions happen when one key receives too much traffic.
- Design access patterns first; DynamoDB is not designed for ad hoc joins.
