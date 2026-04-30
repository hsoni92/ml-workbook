# Lambda Limitations and Best Practices

## Key limits
- Maximum timeout is 15 minutes.
- Deployment package/image size, environment variables, concurrency, payload, and file descriptor limits affect design.
- Account-level concurrency can throttle functions if not managed.

## Best practices
- Keep functions single-purpose and small.
- Initialize SDK clients outside handler to reuse connections.
- Use least-privilege execution roles.
- Configure retries, DLQ/failure destinations, and alarms.

## When to avoid Lambda
- Long-running compute beyond timeout.
- Workloads needing custom OS/kernel control.
- Predictable high constant load where containers/EC2 may be cheaper.
- Low-latency workloads sensitive to cold starts unless mitigated.
