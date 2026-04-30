# Choosing the Right Storage Type

## Choose S3 when
- Data is accessed as objects through API/HTTP.
- You need durable, scalable storage for static assets, backups, logs, or data lakes.
- You can tolerate object semantics rather than block-device writes.

## Choose EBS when
- EC2 needs a boot disk or low-latency attached volume.
- Database/filesystem expects block storage.
- Workload is tied to one AZ and one primary instance at a time.

## Choose EFS when
- Multiple Linux instances need shared filesystem access.
- Capacity should grow/shrink automatically.
- NFS semantics matter more than lowest possible latency.
