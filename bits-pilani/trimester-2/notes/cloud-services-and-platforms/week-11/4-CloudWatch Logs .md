# CloudWatch Logs

## Log structure
- Log group groups logs for app/service/function.
- Log stream usually represents source instance/container/invocation stream.
- Retention controls how long logs are stored and directly affects cost.

## Capabilities
- Logs Insights queries structured/unstructured logs.
- Metric filters convert log patterns into metrics.
- Subscription filters stream logs to Lambda, Kinesis, or other processors.

## Exam details
- Use logs for error messages, stack traces, and event details.
- Set retention; infinite retention can become expensive.
- For Lambda, stdout/stderr appears in CloudWatch Logs by default.
