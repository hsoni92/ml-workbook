# EFS Shared File Storage

## What EFS is
- Elastic File System is managed NFS shared storage for Linux workloads.
- Multiple EC2 instances across AZs can mount the same file system.
- Capacity grows and shrinks automatically as files are added/removed.

## Performance and access
- Mount targets are created in subnets/AZs for client access.
- Security groups control NFS access, commonly TCP 2049.
- Performance modes and throughput modes tune latency/throughput needs.

## When to choose EFS
- Shared web content, home directories, ML preprocessing files, and lift-and-shift NFS apps.
- Not ideal for Windows SMB requirement; use FSx for Windows File Server.
- Not a replacement for S3 object-scale data lakes.
