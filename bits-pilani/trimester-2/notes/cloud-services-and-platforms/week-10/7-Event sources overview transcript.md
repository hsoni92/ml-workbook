# Lambda Event Sources Overview

## Invocation models
- Synchronous invocation waits for response, common with API Gateway.
- Asynchronous invocation queues event and retries on failure, common with S3/EventBridge.
- Poll-based invocation reads from streams/queues, common with SQS, Kinesis, DynamoDB Streams.

## Common event sources
- API Gateway for HTTP APIs.
- S3 for object-created events.
- EventBridge for schedules and event bus rules.
- SQS for decoupled queue processing.
- DynamoDB Streams for table change events.

## Exam distinctions
- Retry behavior depends on event source type.
- Queue/stream sources need batch size and failure handling decisions.
- Use SQS between producer and Lambda to absorb spikes and protect downstream systems.
