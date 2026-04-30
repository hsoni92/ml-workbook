# Amazon ECR Essentials

## What ECR is
- Elastic Container Registry is AWS managed container image registry.
- It integrates with IAM, ECS, EKS, CodeBuild, and vulnerability scanning.
- Repositories can be private or public.

## Important features
- Lifecycle policies delete old images to control cost and clutter.
- Image scanning helps identify package vulnerabilities.
- Cross-region/account patterns support distributed deployments.

## Exam usage
- Choose ECR when workloads run on AWS and IAM-integrated image storage is needed.
- ECR stores images; EKS/ECS run workloads.
- If pull fails from EKS/ECS, check IAM permissions and repository URI/tag.
