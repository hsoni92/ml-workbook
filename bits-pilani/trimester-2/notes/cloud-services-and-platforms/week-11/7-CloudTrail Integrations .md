# CloudTrail Integrations

## With S3
- Trail logs are commonly stored in S3 for durable retention.
- Bucket policy should prevent unauthorized delete or tampering.
- Lifecycle rules can archive old logs to reduce cost.

## With CloudWatch and EventBridge
- CloudTrail events can feed CloudWatch Logs for metric filters and alarms.
- EventBridge rules can react to specific API events near real time.
- Example: alert when root user logs in or security group allows 0.0.0.0/0 SSH.

## With analytics/security tools
- Athena queries CloudTrail logs in S3.
- Security Hub/GuardDuty can use activity signals for findings.
- SIEM integration centralizes investigation across accounts.
