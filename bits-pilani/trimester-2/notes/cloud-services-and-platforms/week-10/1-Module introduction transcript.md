# Week 10: Serverless and Lambda Foundation

## Serverless mental model
- Serverless means the provider manages server provisioning, scaling, and routine infrastructure operations.
- You still own code, IAM permissions, event contracts, error handling, and data design.
- Lambda is event-driven compute: code runs because something invokes it.

## Where Lambda fits
- Short-lived tasks, event processing, API backends, automation, file processing, and stream consumers.
- Pairs naturally with API Gateway, S3, EventBridge, SQS, DynamoDB Streams, and CloudWatch.
- Not ideal for long-running processes, stable ultra-low latency without tuning, or workloads needing full host control.

## Exam anchors
- Stateless design is mandatory; store state in S3/DynamoDB/RDS/cache.
- Execution role grants permissions to the function.
- Timeout, memory, concurrency, retries, and idempotency decide production behavior.
