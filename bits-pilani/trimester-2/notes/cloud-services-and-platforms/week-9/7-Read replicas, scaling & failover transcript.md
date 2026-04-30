# Read Replicas, Scaling, and Failover

## Read replicas
- Asynchronous copies used to offload read-heavy traffic.
- Can exist in same region or cross-region depending engine support.
- May have replication lag; not suitable for immediately consistent reads.

## Scaling options
- Vertical scaling changes DB instance size.
- Storage autoscaling can expand capacity.
- Read scaling uses replicas; write scaling usually requires app/data model changes or different database design.

## Failover clarity
- Multi-AZ standby is for automatic failover, not read traffic in standard RDS.
- Read replica promotion is manual/controlled DR option in many cases.
- Application connection handling must tolerate failover DNS/connection interruption.
