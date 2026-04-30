# CloudWatch Alarms

## Alarm behavior
- Alarm watches a metric or math expression against a threshold.
- States are OK, ALARM, and INSUFFICIENT_DATA.
- Evaluation periods prevent one noisy datapoint from triggering false alarms.

## Actions
- Notify SNS topic.
- Trigger Auto Scaling action.
- Recover/stop/terminate EC2 where supported.
- Feed operational incident workflows.

## Exam choices
- Use alarm when action must happen at threshold breach.
- Dashboard alone is not enough for proactive alerting.
- Pick metric and threshold tied to user impact, not only infrastructure vanity metrics.
