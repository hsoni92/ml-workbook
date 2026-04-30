# Pipeline Triggers and Testing

## Triggers
- Push trigger runs pipeline after commits.
- Pull request trigger validates change before merge.
- Schedule trigger runs periodic checks.
- Manual trigger supports controlled release approval.

## Testing layers
- Unit tests validate functions/classes quickly.
- Integration tests validate service boundaries.
- End-to-end tests validate user workflows.
- Security/policy tests catch unsafe dependencies and infrastructure changes.

## Exam rules
- Run cheap/fast tests earlier.
- Do not deploy if critical tests fail.
- Production deployment should include post-deploy verification and rollback criteria.
