# AWS Lambda Fundamentals

## Function anatomy
- Handler is the entry point Lambda calls.
- Event object carries trigger payload.
- Context object exposes runtime metadata like request ID and remaining time.
- Deployment package or container image contains code and dependencies.

## Runtime behavior
- Lambda may reuse execution environments across invocations.
- Cold start happens when new environment must initialize.
- Memory setting also influences CPU allocation.

## Configuration to know
- Timeout max is 15 minutes.
- Environment variables store non-secret config; secrets should use Secrets Manager/Parameter Store.
- Reserved concurrency caps or guarantees capacity for a function.
