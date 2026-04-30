# Lambda Configuration and IAM Role Usage

## Execution role
- Lambda assumes an IAM role to call AWS APIs.
- Role policy should allow only required actions on required resources.
- Never place long-lived IAM user access keys inside Lambda code.

## Key settings
- Memory affects CPU and network performance.
- Timeout should match expected work and fail fast enough for callers.
- Environment variables hold runtime configuration.
- VPC attachment is needed only for private VPC resources, not for normal AWS public APIs.

## Exam traps
- Over-permissive role with wildcard actions/resources is bad design.
- Putting Lambda in VPC can introduce ENI/NAT/network complexity.
- Timeout failures often require code optimization, memory tuning, or workflow split.
