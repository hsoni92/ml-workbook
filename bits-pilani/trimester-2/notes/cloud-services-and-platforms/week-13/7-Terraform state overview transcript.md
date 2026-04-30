# Terraform State Overview

## Why state exists
- State maps Terraform resource addresses to real remote object IDs.
- It lets Terraform know what it created and what to update/delete.
- Without state, Terraform cannot reliably compare desired and existing infrastructure.

## State risk
- State may contain sensitive values.
- Local state is unsafe for team collaboration.
- Concurrent applies can corrupt expectations without locking.

## Best practice
- Use remote backend such as S3 for shared state.
- Use DynamoDB or backend-native locking where applicable.
- Restrict access and enable versioning/encryption on state storage.
