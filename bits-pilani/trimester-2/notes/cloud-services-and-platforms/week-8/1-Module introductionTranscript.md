# Week 8: Cloud Storage and S3 Foundation

## Storage decision mindset
- Start with access pattern: object, block, or shared file.
- Then evaluate durability, latency, throughput, sharing, compliance, and cost.
- Cloud storage exams usually ask which service fits a workload, not a definition.

## AWS storage map
- S3: object storage for buckets, files, backups, static assets, data lakes.
- EBS: block storage attached to EC2 for OS disks and low-latency volumes.
- EFS: elastic shared NFS file system for multiple Linux clients.

## High-yield distinctions
- Object storage is accessed by API, not mounted as normal disk.
- Block storage is best for databases and boot volumes.
- File storage is best when multiple servers need shared directory semantics.
