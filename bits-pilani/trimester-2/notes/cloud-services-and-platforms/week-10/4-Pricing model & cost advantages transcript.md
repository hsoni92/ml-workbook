# Lambda Pricing Model and Cost Advantages

## Billing components
- You pay per request and compute duration measured in GB-seconds.
- Higher memory increases per-ms price but may reduce runtime if CPU-bound.
- Other services in the workflow still add cost: API Gateway, logs, NAT, S3, queues, databases.

## When Lambda is cheaper
- Spiky or unpredictable traffic.
- Low-to-medium volume APIs.
- Jobs that run briefly and intermittently.
- Automation where idle servers would waste money.

## Cost traps
- Chatty functions writing excessive CloudWatch logs.
- Private Lambda using NAT Gateway for internet calls can add fixed NAT cost.
- Retries and failures multiply invocations and downstream calls.
