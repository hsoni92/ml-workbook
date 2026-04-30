# End-to-End Serverless Workflow

## Typical workflow
- Client calls API Gateway.
- Lambda validates request and executes business logic.
- Data persists in DynamoDB/RDS/S3.
- Events trigger async processing through SQS/EventBridge.
- CloudWatch monitors logs, errors, duration, and alarms.

## Reliability design
- Use queues to decouple spikes and retries.
- Make handlers idempotent because events may be retried.
- Use DLQ or failure destinations for failed async events.
- Split long workflows with Step Functions.

## Exam architecture answer
- Name trigger, compute, state store, failure path, and monitoring.
- Avoid putting state inside Lambda memory/local disk.
- Mention least-privilege IAM across every service call.
