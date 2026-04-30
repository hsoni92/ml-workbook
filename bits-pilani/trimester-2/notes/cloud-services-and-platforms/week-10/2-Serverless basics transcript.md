# Serverless Basics

## What changes operationally
- No EC2 fleet to patch, size, or manually scale.
- Billing is tied to requests, duration, memory, and connected service usage.
- Scaling is automatic within account/service limits.

## What does not disappear
- Bad IAM can still leak or break systems.
- Bad code can still timeout, retry, duplicate writes, or overload downstream databases.
- Observability must still be designed with logs, metrics, traces, and alarms.

## Good use cases
- Event-driven automation.
- Bursty APIs and backend functions.
- Scheduled jobs and data transformations.
- Glue logic between managed services.
