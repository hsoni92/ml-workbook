# Managed vs self-managed databases

## Why This Topic Matters

This note focuses on managed database design where consistency model, schema strategy, and scaling pattern determine correctness and performance.

## Learning Objectives

- Build first-principles understanding of `Managed vs self-managed databases`.
- Connect concepts to architecture decisions in real cloud systems.
- Evaluate security, reliability, performance, and cost trade-offs rigorously.
- Prepare for scenario-based exam and interview questions.

## Intuition Before Mechanics

- Start from workload requirements before choosing services or architecture patterns.
- Prefer managed primitives for undifferentiated heavy lifting where practical.
- Evaluate every design through security, reliability, performance, and cost trade-offs.

## Architecture / Relationship View

```mermaid
flowchart LR
  App[Application] --> DAL[Data Access Layer]
  DAL --> RDS[(RDS)]
  DAL --> DDB[(DynamoDB)]
  RDS --> Replica[Read Replica]
  DDB --> Streams[DynamoDB Streams]
```

## Comparison and Decision Framework

| Aspect | Managed DB | Self-managed DB |
|---|---|---|
| Ops burden | Lower | Higher |
| Control | Moderate | Maximum |
| Reliability effort | Provider-assisted | Team-owned |
| Cost mix | Service premium, lower labor | Lower service fee, higher labor |

## How It Works in Practice

1. Capture workload requirements and constraints first.
2. Choose topology and services that match those requirements.
3. Apply security and policy controls before exposing traffic.
4. Validate behavior with realistic workload and failure tests.
5. Operate with observability and optimize iteratively from production signals.

## Real-World Example

A transaction-heavy service uses RDS for ACID integrity and DynamoDB for low-latency high-scale user session workloads.

## Common Pitfalls / Exam Traps

- Selecting DB type without query and consistency analysis.
- Ignoring partition-key behavior in DynamoDB.
- Relying on backups without restore drills.
- Underestimating failover and replica lag behavior.

## Quick Revision Summary

- Define the primary architecture problem solved by this topic.
- Explain one reliability and one security trade-off.
- State one cost optimization opportunity and one risk.
- Describe a production scenario where this design is appropriate.
- Identify a likely misconfiguration and its operational impact.
- Memorize when each side of the comparison is preferred.
