# Reliability in Cloud Architecture (Week 2)

## Table of Contents
- [Core Concepts](#core-concepts)
- [Terminology and Definitions](#terminology-and-definitions)
- [Detailed Explanations](#detailed-explanations)
- [Workflows / Process Steps](#workflows--process-steps)
- [Examples and Use Cases](#examples-and-use-cases)
- [Comparison Tables](#comparison-tables)
- [Key Takeaways and Summary](#key-takeaways-and-summary)
- [Quick Revision Notes and Memory Aids](#quick-revision-notes-and-memory-aids)
- [Exam Tips and Common Pitfalls](#exam-tips-and-common-pitfalls)

## Core Concepts
- **Reliability** is one of the most critical qualities of any cloud system.
- Reliability = **the ability to continue operating correctly even when parts of the system fail**.
- In the cloud, **failure is an expectation, not an exception**.
- Possible failure modes include:
  - Hardware failure.
  - Network issues.
  - Software bugs.
  - Entire availability zone outages.
- A reliable cloud system **anticipates failures and recovers automatically** with minimal user impact.

## Terminology and Definitions
- **Reliability**: A system's ability to function correctly over time, including how it handles and recovers from failures.
- **Availability**: Whether the system is up at a given moment.
- **Redundancy**: Duplicating critical components so a replacement can take over on failure.
- **Fault Isolation**: Ensuring a failure affects only a small portion of the system, not everything.
- **Automatic Failover**: Traffic is automatically routed to a healthy component when another becomes unhealthy.
- **Replication**: Storing data in more than one location.
- **Synchronous Replication**: Writes go to multiple locations at the same time (minimal data loss).
- **Asynchronous Replication**: Writes are propagated with some delay (better performance).
- **Backups and Disaster Recovery (DR)**: Protection against large-scale failures (e.g., region outages or accidental deletion).
- **Recovery Time Objective (RTO)**: How quickly recovery must happen.
- **Recovery Point Objective (RPO)**: How much data loss is acceptable.
- **Designing for Failure**: Mindset assuming failure will happen and focusing on recovery.
- **Self-Healing**: Systems that automatically detect and remediate failures.
- **Graceful Degradation**: Non-critical features fail without bringing down the whole system.

## Detailed Explanations
### Why Reliability Matters
- Cloud systems are **distributed and constantly changing**, increasing the chance of something going wrong.
- When reliability is poor, impact is **immediate**:
  - Downtime
  - Revenue loss
  - Broken trust
  - Missed SLAs

### Core Building Blocks of Reliable Systems
#### Redundancy
- Critical components are **duplicated** so that if one fails, another takes over.
- Examples:
  - Multiple application servers.
  - Multiple database replicas.
  - Multiple load balancers.

#### Fault Isolation
- Failure affects only a **small part** of the system.
- Examples:
  - Spreading applications across **availability zones**.
  - **Isolating services** from each other.

#### Automatic Failover
- When a component becomes unhealthy, traffic is automatically redirected to a healthy one.
- No human intervention required → essential for **fast recovery**.

#### Replication
- Data is stored in more than one location to prevent data loss.
- **Synchronous replication** → minimal data loss but may affect performance.
- **Asynchronous replication** → better performance but may allow some data loss.

#### Backups and Disaster Recovery
- Protect against large-scale failures such as:
  - Region outages.
  - Accidental deletion.
- Driven by two metrics:
  - **RTO** — how quickly recovery must happen.
  - **RPO** — how much data loss is acceptable.

### Design-for-Failure Mindset
- Assume failure **will happen**; focus on recovering quickly.
- Key mechanisms:
  - **Health checks**.
  - **Self-healing** mechanisms.
  - **Graceful degradation** of non-critical features.

### Reliability vs Availability
- **Availability** asks: *Is the system up right now?*
- **Reliability** asks: *Does it function correctly over time and recover from failures?*

## Workflows / Process Steps
### Reliability Design Checklist
1. Identify critical components and duplicate them (**redundancy**).
2. Spread services across multiple availability zones (**fault isolation**).
3. Configure **health checks** and **automatic failover**.
4. Choose replication strategy: **synchronous** vs **asynchronous** based on performance/data-loss needs.
5. Define **RTO** and **RPO** from business requirements.
6. Implement **backups** and **disaster recovery** plans.
7. Build **self-healing** and **graceful degradation** logic.
8. Continuously test failure scenarios.

## Examples and Use Cases
- Multi-AZ deployment of web servers with load balancer failover.
- Multiple database replicas with automatic promotion on primary failure.
- Asynchronous cross-region replication for backup purposes.
- Graceful degradation — non-critical features (e.g., recommendations) disabled during overload, while core features remain.

## Comparison Tables
### Reliability vs Availability
| Aspect | Availability | Reliability |
|---|---|---|
| Question | Is the system up right now? | Does it function correctly over time? |
| Time frame | Point-in-time | Long-term behavior |
| Focus | Uptime | Correct operation + recovery |
| Example metric | Uptime % | MTBF, MTTR, RTO, RPO |

### Synchronous vs Asynchronous Replication
| Attribute | Synchronous | Asynchronous |
|---|---|---|
| Data loss risk | Minimal | Some possible |
| Performance impact | Higher | Lower |
| Typical use | Financial / transactional workloads | Read replicas, cross-region backups |

### RTO vs RPO
| Metric | Meaning | Business Driver |
|---|---|---|
| RTO | How quickly the system must recover | Tolerable downtime |
| RPO | How much data loss is acceptable | Tolerable data loss |

## Key Takeaways and Summary
- Reliable cloud systems are built by:
  - **Expecting failures**.
  - **Automating recovery**.
  - **Isolating faults**.
  - **Protecting data**.
  - **Minimizing user impact**.
- Reliability is **not just a technical concern** — it is a **fundamental business requirement**.
- Cloud architects must combine **redundancy, replication, failover, backups, and DR** guided by **RTO** and **RPO**.

## Quick Revision Notes and Memory Aids
- **Reliability ≠ Availability**: availability = up now; reliability = works correctly over time.
- **Design for failure**, not against it.
- Core building blocks: **Redundancy, Fault Isolation, Failover, Replication, Backups/DR**.
- Two metrics to remember: **RTO (time) and RPO (data loss)**.
- Choose replication mode based on: **data-loss tolerance vs performance**.

## Exam Tips and Common Pitfalls
- Do not confuse RTO and RPO — **RTO = time**, **RPO = data**.
- Synchronous replication ≠ always better; it adds **performance cost**.
- Graceful degradation preserves critical features; don't describe it as "everything fails."
- Reliability requires **automation** — manual recovery does not count as reliable design.
- Mentioning only redundancy is insufficient; mention **failover, replication, and DR** too.
