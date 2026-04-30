# Build and Trigger Lambda

## Build steps
- Write handler function with clear input/output contract.
- Package dependencies or use container image/layers.
- Create execution role with least required permissions.
- Deploy function with runtime, memory, timeout, and environment config.

## Trigger setup
- For S3: configure bucket event notification and Lambda permission.
- For API Gateway: create route/method integration and deploy stage.
- For EventBridge: create rule and target.
- For SQS: create event source mapping.

## Verification checklist
- Invoke test event and inspect CloudWatch Logs.
- Confirm IAM failures are not hidden as app errors.
- Check retry behavior by forcing controlled failure.
- Set alarms before calling it production-ready.
