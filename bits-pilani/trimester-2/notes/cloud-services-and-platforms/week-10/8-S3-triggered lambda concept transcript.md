# S3-Triggered Lambda

## Flow
- Object event occurs in S3 bucket.
- S3 sends event notification to Lambda or another target.
- Lambda reads bucket/key from event payload and processes the object.

## Typical use cases
- Generate thumbnails after image upload.
- Validate or transform uploaded files.
- Extract metadata and write to DynamoDB/RDS.
- Move or tag objects based on content.

## Design cautions
- Avoid writing output back to same prefix without filters or you can trigger loops.
- Function role needs S3 read/write permissions only for required bucket/prefix.
- Large files may need streaming, multipart strategy, or Step Functions for longer workflows.
