# Nacls vs Security Groups

## Why This Topic Matters

This note builds networking intuition for secure and reachable cloud systems. Network decisions define exposure boundaries, routing behavior, and fault isolation.

## Learning Objectives

- Build first-principles understanding of `Nacls vs Security Groups`.
- Connect concepts to architecture decisions in real cloud systems.
- Evaluate security, reliability, performance, and cost trade-offs rigorously.
- Prepare for scenario-based exam and interview questions.

## Core Concepts and Definitions

- `Security Group`: a stateful virtual firewall attached to ENIs or instances that allows explicitly permitted traffic.
- `NACL`: a stateless subnet-level packet filter that evaluates ordered allow and deny rules.

## Intuition Before Mechanics

- Start from workload requirements before choosing services or architecture patterns.
- Prefer managed primitives for undifferentiated heavy lifting where practical.
- Evaluate every design through security, reliability, performance, and cost trade-offs.
- Key technologies here: `Security Group`, `NACL`.

## Architecture / Relationship View

```mermaid
flowchart LR
  Internet[Internet] --> IGW[Internet Gateway]
  IGW --> Pub[Public Subnet]
  Pub --> ALB[Load Balancer]
  ALB --> App[Private App Subnet]
  App --> DB[Private DB Subnet]
  App --> NAT[NAT Gateway]
  NAT --> Internet
```

## Comparison and Decision Framework

| Aspect | Security Group | NACL |
|---|---|---|
| Scope | Instance/ENI level | Subnet level |
| State model | Stateful | Stateless |
| Rule style | Allow only | Ordered allow + deny |
| Typical use | Fine-grained workload control | Coarse subnet guardrails |

## How It Works in Practice

1. Capture workload requirements and constraints first.
2. Choose topology and services that match those requirements.
3. Apply security and policy controls before exposing traffic.
4. Validate behavior with realistic workload and failure tests.
5. Operate with observability and optimize iteratively from production signals.

## Real-World Example

A production web platform keeps only load balancers in public subnets while app and database tiers remain private with controlled NAT egress.

## Common Pitfalls / Exam Traps

- Overlapping CIDR blocks that block peering/hybrid growth.
- Mixing up route-table and firewall issues while debugging connectivity.
- Exposing private tiers due to incorrect subnet placement.
- Overly broad network rules enabling lateral movement.

## Quick Revision Summary

- Define the primary architecture problem solved by this topic.
- Explain one reliability and one security trade-off.
- State one cost optimization opportunity and one risk.
- Describe a production scenario where this design is appropriate.
- Identify a likely misconfiguration and its operational impact.
- Memorize when each side of the comparison is preferred.
- Recall precise definitions for: Security Group, NACL.
