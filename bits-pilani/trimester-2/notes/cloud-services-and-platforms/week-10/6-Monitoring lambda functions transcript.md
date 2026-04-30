# Monitoring Lambda Functions

## Default telemetry
- CloudWatch Logs captures stdout/stderr from function execution.
- CloudWatch Metrics includes invocations, errors, duration, throttles, and concurrent executions.
- AWS X-Ray can trace downstream calls and latency segments.

## What to alarm on
- Error rate above baseline.
- Duration approaching timeout.
- Throttles indicating concurrency pressure.
- Dead-letter queue or failure destination message growth.

## Debugging approach
- Start with request ID and logs for failing invocation.
- Check timeout, memory, and downstream latency.
- Look for retries causing duplicate work or amplified load.
