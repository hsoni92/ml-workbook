# Providers, Resources, and Modules

## Provider
- Plugin that lets Terraform talk to an API such as AWS, Azure, GCP, Kubernetes, or GitHub.
- Provider block configures region, credentials behavior, and version constraints.
- Provider version pinning improves reproducibility.

## Resource
- Resource block declares one managed object such as aws_instance, aws_s3_bucket, or aws_vpc.
- Arguments configure desired properties.
- Terraform tracks each resource through state.

## Module
- Module is reusable collection of Terraform files.
- Root module is current working configuration.
- Child modules package repeatable patterns such as VPC, ECS service, or S3 bucket baseline.
