# AWS Storage Services Overview

## S3
- Regional object store with bucket/object model.
- Designed for very high durability and broad integration across AWS.
- Supports versioning, lifecycle, replication, event notifications, encryption, and policies.

## EBS
- AZ-scoped block volume attached to EC2.
- Snapshots are stored in S3-backed durable storage.
- Volume type selection affects IOPS, throughput, and cost.

## EFS and archive
- EFS gives regional shared NFS access across AZs.
- Glacier storage classes serve archival use cases through S3.
- Exam questions usually hide the answer in access pattern and retrieval time.
