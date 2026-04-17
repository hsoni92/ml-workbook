# Trade-Offs in Cloud Architecture (Week 2)

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
- A **trade-off** means improving one part of the system usually affects another part.
- There is **no cloud architecture** that is simultaneously the **cheapest, fastest, most resilient, and simplest**.
- Cloud architecture is **not about perfect solutions**; it's about **balanced decisions**.
- Architects must understand:
  - What they are optimizing for.
  - What they are sacrificing.
  - What decision fits the business.

## Terminology and Definitions
- **Trade-off**: A situation where improving one system quality negatively impacts another.
- **Latency**: Response time of an application to users.
- **Resilience**: Ability of a system to survive failures.
- **Right Sizing**: Selecting resources that match workload requirements — not the biggest, not the smallest, but the right fit.
- **Redundancy**: Duplicating components to improve resilience.
- **Replication**: Maintaining copies of data across locations.
- **Failover Mechanism**: Automated redirection of traffic to healthy components.
- **Monolithic Architecture**: A simple, single-deployment system.
- **Distributed System / Microservices**: Scalable but more complex architectures.

## Detailed Explanations
### Why Trade-offs Matter
- Every design decision has a cost elsewhere in the system.
- Architects cannot maximize every quality at once; they must make **informed choices**.

### Trade-off 1: Latency vs Cost
- Reducing latency means making the application respond faster.
- To reduce latency, architects often:
  - Deploy services closer to users.
  - Use multiple regions.
  - Replicate data globally.
- All of these improve speed **but increase cost** (more infrastructure, more data copies, region-specific charges).
- **Low latency → higher cost**; **Lower cost → higher latency**.

### Trade-off 2: Cost vs Resilience
- Resilience is improved by adding:
  - Redundancy.
  - Multiple servers.
  - Multiple backups.
  - Failover mechanisms.
- Every backup server costs money; every replicated database costs money.
- **Higher resilience → higher cost**; **lower cost → higher risk**.

### Trade-off 3: Performance vs Cost
- High performance often requires:
  - Larger machines.
  - Faster storage.
  - Caching systems.
  - Premium networking.
- These increase cloud bills.
- Minimizing cost too aggressively results in slow applications and poor user experience.
- Good architects aim for **right sizing**: not biggest, not smallest — **the right fit**.

### Trade-off 4: Simplicity vs Scalability
- **Simple** architectures are easy to build and understand, but don't scale well.
- **Scalable** architectures (distributed systems, microservices) handle growth but are harder to design, operate, and debug.
- Early-stage systems often start simple; as scale increases, **complexity becomes unavoidable**.

### Architect's Mindset
- Cloud architecture is about **intentional trade-offs**.
- Architects must clearly articulate:
  - What is being optimized.
  - What is being sacrificed.
  - Why the decision fits the business.
- **No perfect architecture** — only **informed, well-justified decisions**.

## Workflows / Process Steps
### Evaluating a Trade-off
1. Identify the quality being improved (e.g., latency).
2. Identify what is being sacrificed (e.g., cost, complexity).
3. Assess **business impact** and user expectations.
4. Quantify cost/complexity delta.
5. Choose the option that aligns with business priorities.
6. Document the trade-off and its rationale.

## Examples and Use Cases
- **Global gaming platform** — willingly pays more to reduce latency for users worldwide.
- **Internal company tool** — accepts higher latency to save money since internal use has low business impact.
- **Banking system** — invests heavily in resilience (redundancy, backups, failover).
- **Startup MVP** — may accept downtime to stay within budget.
- Moving from a **monolith** to **microservices** as scale grows, accepting operational complexity for scalability.

## Comparison Tables
### Trade-off Summary
| Trade-off | Gain | Cost |
|---|---|---|
| Latency ↓ | Faster response | Higher cost (more regions/replication) |
| Cost ↓ | Lower cloud bill | Higher risk or higher latency |
| Resilience ↑ | Better survival of failures | Higher cost (redundancy, replication, failover) |
| Performance ↑ | Better response under load | Higher cost (bigger machines, caches, premium networking) |
| Simplicity ↑ | Easy build/operate | Limited scalability |
| Scalability ↑ | Handles growth | Higher complexity (distributed systems, microservices) |

### Scenarios and Choices
| Scenario | Priority | Trade-off Accepted |
|---|---|---|
| Global gaming platform | Low latency | Higher cost |
| Internal tool | Low cost | Higher latency |
| Banking system | Resilience | Higher cost |
| Startup MVP | Low cost | Potential downtime |
| Early product | Simplicity | Limited scalability |
| Scaled product | Scalability | Higher complexity |

## Key Takeaways and Summary
- Every cloud architecture involves **trade-offs**: latency vs cost, cost vs resilience, performance vs cost, simplicity vs scalability.
- **Right sizing** is the discipline of matching resources to actual workload needs.
- Cloud architecture is about **intentional, well-justified decisions**, not perfection.
- Business context determines the correct balance.

## Quick Revision Notes and Memory Aids
- Four core trade-offs: **Latency vs Cost**, **Cost vs Resilience**, **Performance vs Cost**, **Simplicity vs Scalability**.
- Mantra: **"Right size, not biggest, not smallest."**
- **No perfect architecture** — only balanced ones.
- Match **trade-off to business priority**.

## Exam Tips and Common Pitfalls
- Don't propose maximizing **all** qualities; mention which is prioritized and which is sacrificed.
- Associate scenarios with typical choices (e.g., banking → resilience; MVP → cost).
- Remember: **microservices are not always better** — they trade simplicity for scalability.
- "Right sizing" is the preferred answer over "biggest instance" for cost vs performance questions.
- Trade-offs should be **explicitly stated** in architectural decisions.
