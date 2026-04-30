# S3 Encryption Options

## Server-side encryption
- SSE-S3 uses AWS-managed S3 keys and is simplest.
- SSE-KMS uses AWS KMS keys, supports audit trails and key policies.
- SSE-C lets customer provide keys for each request; AWS does not store the key.

## Client-side encryption
- Application encrypts data before uploading to S3.
- Customer controls encryption process and key handling.
- Operational burden is higher because losing keys means losing data.

## Exam selection
- Need compliance audit of key usage: SSE-KMS.
- Need simplest default encryption: SSE-S3.
- Need provider not to manage keys at all: client-side or SSE-C depending requirement wording.
