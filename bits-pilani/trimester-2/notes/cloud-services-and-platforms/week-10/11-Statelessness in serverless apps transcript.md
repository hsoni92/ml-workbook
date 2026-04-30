# Statelessness in Serverless Apps

## Meaning of stateless
- A function should not rely on memory or local disk from previous invocation.
- Any durable state belongs in an external system such as DynamoDB, S3, RDS, ElastiCache, or Step Functions.
- Execution environment reuse is an optimization, not a contract.

## Why it matters
- Stateless functions scale horizontally because any invocation can run anywhere.
- Retries become safer when state changes are idempotent.
- Deployments and cold starts are less risky when no local mutable state is required.

## Exam traps
- Storing user sessions in Lambda memory is wrong.
- /tmp can cache temporary data but is not durable system state.
- Duplicate events require idempotency keys or conditional writes.
