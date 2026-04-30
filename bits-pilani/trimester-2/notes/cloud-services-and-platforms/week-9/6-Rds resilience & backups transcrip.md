# RDS Resilience and Backups

## Backup types
- Automated backups enable point-in-time recovery within retention window.
- Manual snapshots persist until deleted.
- Snapshots are useful before risky changes and for environment cloning.

## Availability design
- Multi-AZ keeps synchronous standby for automatic failover.
- Backups restore data but do not provide instant continuity by themselves.
- Cross-region backups/replicas help disaster recovery planning.

## Exam distinctions
- Backup solves recovery after data loss/corruption.
- Multi-AZ solves infrastructure/AZ failure availability.
- Read replica can be promoted, but replication lag can affect recovery point.
