# S3 Bucket Policies and IAM Permissions

## Policy types
- IAM policy attaches permissions to identities such as users, groups, or roles.
- Bucket policy attaches permissions directly to the S3 bucket resource.
- Access points can simplify policies for large/shared data sets.

## Evaluation logic
- Explicit deny always wins.
- Access requires an allow from relevant identity/resource policy and no explicit deny.
- Block Public Access can override accidental public exposure settings.

## Exam patterns
- Use bucket policy for cross-account bucket access.
- Use IAM role policy for application access from EC2/Lambda/ECS.
- Avoid ACLs unless legacy integration requires them.
