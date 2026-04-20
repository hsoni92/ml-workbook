# EBS Snapshots and Backup Basics

## Learning Objectives

- Define EBS snapshot and point-in-time backup semantics.
- Explain incremental snapshot behavior.
- Design a backup policy using frequency, retention, and criticality.
- Understand snapshot restore flow to EC2.

---

## What is an EBS Snapshot?

An EBS snapshot captures block-level state of a volume at a specific point in time.

It is the core AWS-native backup primitive for EBS-backed data.

---

## Why Snapshots are Needed

Failure and error scenarios are unavoidable:

- accidental deletion
- failed updates
- corruption events
- operational mistakes

Snapshots provide rollback and recovery safety.

---

## Incremental Snapshot Model

- First snapshot: full baseline
- Subsequent snapshots: store only changed blocks

Benefits:

- Lower storage overhead
- Faster recurring backups
- Better cost efficiency over time

---

## Backup Strategy Questions (from transcript, expanded)

1. **What to back up?**
   Critical volumes, databases, config/state disks.
2. **How often?**
   RPO-driven cadence: hourly/daily/weekly based on business impact.
3. **How long to retain?**
   Compliance and recovery window requirements.

Automate snapshots; do not rely on manual memory.

---

## Restore Flow (Important)

```mermaid
flowchart LR
  S[Snapshot] --> V[Create new EBS volume]
  V --> A[Attach to EC2 instance]
  A --> R[Mount and recover data]
```

For root disk recovery, you can also launch a new instance from snapshot-derived image workflow.

---

## Design Best Practices

- Tag snapshots by app/env/owner/retention class.
- Test restore drills periodically (backup without restore test is incomplete).
- Encrypt snapshots for sensitive data.
- Replicate strategy across failure domains when required.

---

## Quick Revision Checklist

- [ ] Define snapshot as point-in-time backup.
- [ ] Explain incremental snapshot economics.
- [ ] Describe 3-question backup strategy framework.
- [ ] Outline snapshot -> volume -> attach restore path.
