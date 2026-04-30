# S3 Security Settings

## Public access controls
- S3 Block Public Access should usually stay enabled.
- Bucket policies can accidentally expose data if Principal is broad.
- Use least privilege and test with IAM Access Analyzer where available.

## Data protection
- Enable encryption at rest: SSE-S3 for default simplicity or SSE-KMS for key control/audit.
- Use TLS for data in transit.
- Versioning and MFA Delete help protect against accidental or malicious deletion.

## Audit and monitoring
- CloudTrail data events can record object-level API activity.
- Server access logs or CloudTrail help investigation.
- S3 Object Lock supports WORM retention for compliance cases.
