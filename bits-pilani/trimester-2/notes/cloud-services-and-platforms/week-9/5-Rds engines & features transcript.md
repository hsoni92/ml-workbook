# RDS Engines and Features

## Supported engines
- Amazon RDS supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora.
- Engine choice depends on app compatibility, licensing, SQL features, and operational expectations.
- Aurora offers cloud-native storage replication and faster failover characteristics.

## Core features
- Automated backups and snapshots support recovery.
- Multi-AZ deployment improves availability.
- Read replicas improve read scalability.
- Parameter groups and option groups customize behavior.

## Exam cautions
- RDS is managed but not serverless by default.
- You choose instance class/storage unless using Aurora Serverless-like options.
- License cost and engine compatibility matter for Oracle/SQL Server choices.
