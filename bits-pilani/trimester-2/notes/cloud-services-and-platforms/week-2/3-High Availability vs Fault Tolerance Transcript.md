# High Availability vs Fault Tolerance (Week 2)

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
- **High availability (HA)** and **fault tolerance (FT)** are both about handling failure — but approach it very differently.
- In distributed cloud systems, **failure is expected, not exceptional**:
  - Servers crash.
  - Networks break.
  - Zones go down.
  - Services become unavailable.
- The real architectural question is **not if failures happen, but how the system responds**.
- HA focuses on **fast recovery** with **brief downtime acceptable**.
- FT focuses on **no visible downtime at all**, absorbing failure instantly.

## Terminology and Definitions
- **High Availability (HA)**: Designing systems to remain available **most of the time**, with quick recovery from failures.
- **Fault Tolerance (FT)**: Designing systems to **continue operating without interruption** even when components fail.
- **Redundancy**: More than one instance of a component.
- **Load Balancer**: Distributes traffic across instances.
- **Health Check**: Mechanism for detecting failures.
- **Failover**: Automatic redirection of traffic when a component fails.
- **Availability Zone (AZ)**: Isolated data center zone within a region; applications are often deployed across multiple AZs.
- **Active-Active Architecture**: Multiple systems serving traffic simultaneously — the norm for FT.
- **Single Point of Failure (SPOF)**: A component whose failure stops the entire system.
- **Zero Downtime**: No interruption visible to users.

## Detailed Explanations
### Why This Topic Matters
- Cloud systems operate under the assumption that failures happen constantly.
- Design decisions define whether users notice failures.
- HA and FT are the two dominant strategies.

### High Availability (HA)
- **Goal**: available **most** of the time.
- Failures can still happen, but the system is built to **recover quickly** and restore service.
- Core idea: **minimize downtime**, even if you cannot eliminate it.
- Typical building blocks:
  - **Redundancy** — more than one instance of each component.
  - **Load balancers** — distribute traffic across instances.
  - **Health checks** — detect failures quickly.
  - **Failover** — redirect traffic away from failed components.
- In cloud:
  - Deploy applications across **multiple availability zones**.
  - If one zone fails, traffic routes to healthy zones.
  - There may be a **short interruption**, but service is restored quickly.

### Fault Tolerance (FT)
- **Stricter** approach than HA.
- **Goal**: continue operating **without interruption** even when components fail.
- Failure is **absorbed instantly**; users should not experience downtime, delays, or errors.
- Achieved through:
  - Running **duplicate components** simultaneously.
  - **Synchronizing data in real time**.
  - Eliminating **every single point of failure**.
- Typically uses **active-active** architectures with multiple systems serving traffic at the same time.
- **Goal = zero downtime**, which is ideal but costly.

### Cost & Complexity
- HA:
  - **Moderately complex**.
  - **Cost effective**.
  - Used **almost everywhere** in the cloud.
- FT:
  - **Extremely complex**.
  - **Expensive**.
  - Reserved for very specific **mission-critical systems**.

### Simple Analogy
- **HA** = **backup generator**:
  - Power may go out briefly but comes back quickly.
- **FT** = **two power supplies running at once**:
  - If one fails, the other takes over instantly.

## Workflows / Process Steps
### Designing for HA
1. Identify critical services.
2. Deploy across **multiple AZs**.
3. Add a **load balancer** in front.
4. Configure **health checks**.
5. Enable **automatic failover**.
6. Accept brief interruption during recovery as acceptable.

### Designing for FT
1. Identify mission-critical components where downtime is unacceptable.
2. Run **duplicate components** concurrently (active-active).
3. Synchronize data in **real time**.
4. Eliminate **single points of failure** across the stack.
5. Absorb failure without user-visible impact.

## Examples and Use Cases
- **HA-typical workloads**:
  - Web applications.
  - SaaS products.
  - Mobile backends and APIs.
- **FT-typical workloads**:
  - Banking and transactional systems.
  - Stock exchanges.
  - Air traffic control.
  - Medical monitoring systems.

## Comparison Tables
### HA vs FT
| Aspect | High Availability | Fault Tolerance |
|---|---|---|
| Downtime | Brief downtime acceptable | No visible downtime |
| Strategy | Recover quickly | Absorb failure instantly |
| Complexity | Moderate | Extremely high |
| Cost | Cost effective | Expensive |
| Architecture | Redundancy + failover | Active-active + real-time sync |
| Typical Use | Most cloud systems | Mission-critical systems |

### Analogy Recap
| Concept | Analogy |
|---|---|
| HA | Backup generator (brief outage, quick restart) |
| FT | Two power supplies running simultaneously |

## Key Takeaways and Summary
- Most cloud systems aim for **HA**, not full **FT**.
- FT is reserved for cases where **downtime is completely unacceptable**.
- HA minimizes downtime; FT eliminates it.
- As a cloud architect, the choice depends on **business impact, requirements, cost, and operational maturity** — not on chasing perfection.
- HA = fast recovery; FT = no interruption.

## Quick Revision Notes and Memory Aids
- **HA = recover quickly**, **FT = never fail**.
- HA = **backup generator**; FT = **dual power supplies**.
- HA = **moderate cost**; FT = **expensive**.
- FT implies **active-active + real-time sync + zero SPOF**.
- Most workloads aim for **HA**, not FT.

## Exam Tips and Common Pitfalls
- Do not conflate HA and FT — HA allows brief downtime; FT does not.
- FT almost always implies **active-active** systems.
- Remember the analogy: generator vs dual power supplies.
- In cloud, HA is usually realized via **multi-AZ deployments**, load balancers, and health checks.
- Choosing FT everywhere is wasteful; match the strategy to business-critical needs.
