# S3 Buckets, Objects, and Folder Structure

## Bucket and object model
- Bucket is the top-level container with a globally unique name.
- Object is the stored item: data plus metadata plus key.
- S3 has a flat namespace; folders are key prefixes, not real directories.

## Keys and prefixes
- Object key can look like logs/2026/app.log.
- Console displays prefixes as folders for human convenience.
- Prefix design affects organization, lifecycle rules, and analytics workflows.

## Exam details
- Bucket names must be globally unique and DNS-compatible.
- S3 object overwrite behavior depends on versioning status.
- Do not assume POSIX rename/append semantics; S3 is object storage.
