# Terraform with AWS Provider

## AWS provider role
- The AWS provider translates Terraform resources into AWS API calls.
- Region and credentials must be configured through provider block or environment/CLI profile.
- Provider version should be constrained for stable behavior.

## Typical AWS resources
- aws_vpc, aws_subnet, aws_security_group, aws_instance, aws_s3_bucket, aws_iam_role.
- Resource arguments map to AWS service settings.
- Tags should be applied consistently through provider default_tags or module variables.

## Exam/practice issues
- IAM permission errors happen at apply time if caller lacks AWS rights.
- Changing certain attributes forces resource replacement.
- Remote state and locking are especially important for shared AWS environments.
