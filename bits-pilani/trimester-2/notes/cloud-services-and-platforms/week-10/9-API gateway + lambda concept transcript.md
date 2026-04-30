# API Gateway with Lambda

## Architecture role
- API Gateway exposes HTTPS endpoints to clients.
- Lambda implements request handling without managing web servers.
- Together they form a serverless API backend.

## Important features
- API Gateway handles routing, stages, throttling, request/response transformation, authorization integration, and custom domains.
- Lambda proxy integration forwards most request details to the function.
- CloudWatch logs/metrics show API and function behavior separately.

## Exam decisions
- Use this for lightweight/event-driven APIs with variable traffic.
- Use ALB/ECS/EC2 when long-running connections, full server control, or stable high-throughput economics dominate.
- Protect APIs with IAM/Cognito/Lambda authorizer/JWT authorizer depending requirement.
