# CloudWatch Metrics

## Metric basics
- Metric is a time-series measurement such as CPUUtilization, Invocations, Latency, or ErrorCount.
- Namespace groups metrics by service/application.
- Dimensions identify a metric variant such as instance ID, function name, or load balancer.

## AWS and custom metrics
- Many AWS services publish default metrics automatically.
- Custom metrics let applications publish business or internal health signals.
- Resolution affects cost and granularity.

## Exam use
- Metrics answer what is happening numerically.
- Use metrics for alarms, dashboards, autoscaling policies, and trend analysis.
- If you need log text, use CloudWatch Logs, not Metrics.
