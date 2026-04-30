# Activity Auditing with CloudTrail

## Audit workflow
- Enable multi-region trail for complete visibility.
- Send logs to dedicated S3 bucket with restricted access.
- Optionally deliver to CloudWatch Logs for alerting.
- Query events through Event history, Athena, CloudWatch Logs Insights, or SIEM.

## Important fields
- eventName tells API action.
- userIdentity identifies principal.
- sourceIPAddress shows origin.
- requestParameters and responseElements show resource details.

## Incident examples
- Unexpected security group opening.
- Root user activity.
- IAM policy changes.
- S3 bucket policy made public.
