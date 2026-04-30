# Rightsizing EC2 and Storage Optimization

## Rightsizing EC2
- Match instance family to bottleneck: compute, memory, storage, network, GPU.
- Use CloudWatch metrics and Compute Optimizer recommendations.
- Downsize idle/overprovisioned instances; scale horizontally when architecture supports it.

## Storage optimization
- Use correct EBS volume type and provisioned IOPS only when needed.
- Delete unattached EBS volumes and stale snapshots after retention review.
- Move S3 data through lifecycle policies to cheaper classes.

## Exam traps
- Reserved Instances do not fix oversized resources; rightsize first.
- Low CPU alone may not mean idle if memory/network is bottleneck.
- Storage cost includes snapshots, replication, logs, and retrieval fees.
