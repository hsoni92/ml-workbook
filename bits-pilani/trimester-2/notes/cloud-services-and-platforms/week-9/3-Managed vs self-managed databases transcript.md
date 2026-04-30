# Managed vs Self-Managed Databases

## Managed database
- Provider handles infrastructure tasks such as provisioning, patching options, backups, monitoring hooks, and failover features.
- Examples: RDS, Aurora, DynamoDB.
- You still own schema, indexes, queries, access control, and data protection settings.

## Self-managed database
- You install and operate database on EC2 or your own servers.
- Gives maximum control over OS, engine version, plugins, and custom tuning.
- Also gives you patching, backup, HA, scaling, and incident responsibility.

## Exam selection
- Choose managed unless custom engine/control requirement is explicit.
- Choose self-managed for unsupported versions/extensions or unusual OS-level control.
- Managed does not remove shared responsibility for data and IAM.
