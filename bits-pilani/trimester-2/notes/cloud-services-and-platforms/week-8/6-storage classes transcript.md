# S3 Storage Classes

## Frequent access
- S3 Standard is for frequently accessed data needing low latency and high availability.
- S3 Intelligent-Tiering moves objects between tiers based on access pattern.
- Use these when access pattern is active or unknown.

## Infrequent and one-zone
- Standard-IA is cheaper storage with retrieval cost for infrequently accessed data.
- One Zone-IA stores in one AZ and is cheaper but less resilient to AZ loss.
- Good for reproducible or secondary copies, not critical sole data.

## Archive classes
- Glacier Instant Retrieval for archive needing milliseconds access.
- Glacier Flexible Retrieval for minutes-to-hours retrieval.
- Glacier Deep Archive for lowest-cost long-term retention with slow retrieval.
