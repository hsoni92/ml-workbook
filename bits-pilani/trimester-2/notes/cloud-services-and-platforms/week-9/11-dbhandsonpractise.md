# Database Hands-On Practice

## RDS practice flow
- Create subnet group using private subnets.
- Launch RDS with proper engine, credentials, backup retention, and security group.
- Connect only from allowed app/bastion source and verify port-specific access.

## DynamoDB practice flow
- Create table with partition key and optional sort key.
- Insert items that match planned access pattern.
- Query by key instead of scanning whole table.
- Observe capacity mode and request behavior.

## What to remember after lab
- Security group source rules are as important as DB endpoint.
- Backups/snapshots should be checked, not assumed.
- Hands-on exams often fail because networking access is wrong, not database engine itself.
