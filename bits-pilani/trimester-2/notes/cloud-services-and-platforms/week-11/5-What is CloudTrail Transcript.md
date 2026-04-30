# What Is CloudTrail

## Purpose
- CloudTrail records AWS API activity for governance, compliance, and incident investigation.
- It answers who did what, when, from where, and against which resource.
- Management events are central for account and control-plane audit.

## Event types
- Management events track control-plane actions like CreateUser or AuthorizeSecurityGroupIngress.
- Data events track high-volume resource operations like S3 object access or Lambda invocation when enabled.
- Insights events detect unusual API activity patterns.

## Exam distinction
- CloudTrail is not performance monitoring; that is CloudWatch.
- CloudTrail is the service to identify who changed IAM, security groups, routes, or buckets.
- Store trails securely with log file validation for audit integrity.
