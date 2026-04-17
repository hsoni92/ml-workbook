# Understanding AWS Global Infrastructure (Week 4)

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
- AWS does not run from one big data center.
- It uses a **global infrastructure** made up of:
  1. **Regions**
  2. **Availability Zones (AZs)**
  3. **Edge Locations**
- Each plays a **different role** and together they solve **three different problems**:
  - Regions → **location and compliance**.
  - AZs → **availability and fault tolerance**.
  - Edge Locations → **speed and performance**.

## Terminology and Definitions
- **AWS Region**: A geographical area where AWS has data centers. Each region is completely independent.
- **Availability Zone (AZ)**: One or more data centers inside a region, with its **own power, networking, and cooling**, and **physically separated** from other AZs.
- **Edge Location**: A location placed very close to end users, used to **deliver content faster** and **reduce latency**.
- **CloudFront**: AWS's content delivery network (CDN) leveraging edge locations.
- **High Availability (HA)**: Designing applications to remain available despite component failures.
- **Compliance**: Legal/regulatory requirements that may dictate where data is stored.

## Detailed Explanations
### AWS Regions
- A region is a **geographical area** where AWS has its data centers.
- Each region is **completely independent** from others.
- Independence is intentional, allowing AWS to:
  - **Isolate large-scale failures**.
  - Meet **country-specific compliance** requirements.
- When you create resources in AWS, the **first decision** is always **which region to use**.
- That choice affects:
  - **Performance**.
  - **Cost**.
  - **Legal compliance**.

### Availability Zones (AZs)
- Inside each region, AWS has one or more AZs.
- An AZ is **one or more data centers**.
- Each AZ has:
  - Its **own power**.
  - Its **own networking**.
  - Its **own cooling**.
- AZs are **physically separated** from one another.
- Idea: if one data center fails, **another AZ in the same region should continue running**.
- This enables **high availability**.
- **Important**: High availability **does not happen automatically**. The application must be **designed** to use multiple AZs.

### Edge Locations
- Placed **very close to end users**.
- Mainly used to:
  - Deliver content faster.
  - Reduce latency.
- Instead of every user request traveling far to the region, content is **cached** and placed at the **nearest edge location**.
- Services like **CloudFront** use edge locations to make websites and videos load faster.

### Retail Company Analogy
- **Region** = main warehouse in a country.
- **Availability Zones** = separate buildings inside that warehouse campus.
- **Edge Locations** = small delivery hubs close to customers.

### What They Solve Together
- **Regions** → **location and compliance**.
- **Availability Zones** → **availability and fault tolerance**.
- **Edge Locations** → **speed and performance**.

## Workflows / Process Steps
### Designing with AWS Global Infrastructure
1. Choose the **region** that meets user proximity, compliance, and cost needs.
2. Deploy workloads across **multiple AZs** in the region to achieve high availability.
3. Use **edge locations** (e.g., CloudFront) to cache content closer to users.
4. Verify compliance, latency, and resilience.

### Application-Level HA Workflow (AZ-based)
1. Deploy application servers in at least **two AZs**.
2. Add a load balancer spanning AZs.
3. Replicate database across AZs for redundancy.
4. Validate failover by simulating an AZ outage.

## Examples and Use Cases
- Deploying in an India-based region for better performance and compliance with local users.
- Designing a **multi-AZ** web application to tolerate data center failure.
- Using **CloudFront edge locations** to accelerate video streaming and website delivery.

## Comparison Tables
### AWS Global Infrastructure Components
| Component | Purpose | Analogy |
|---|---|---|
| Region | Location + compliance | Main warehouse in a country |
| Availability Zone | Availability + fault tolerance | Separate buildings in a warehouse campus |
| Edge Location | Speed + performance | Delivery hub close to customers |

### Who Solves What
| Problem | Solved By |
|---|---|
| Location & compliance | Regions |
| Availability & fault tolerance | AZs |
| Speed & performance for end users | Edge locations |

### Region-Level Decisions Impact
| Region Choice Impacts |
|---|
| Performance |
| Cost |
| Legal compliance |

## Key Takeaways and Summary
- AWS runs globally through **regions, AZs, and edge locations**.
- Regions are **completely independent** (isolation + compliance).
- AZs are **physically separated** inside a region to enable **high availability** — but the **application must be designed to use them**.
- Edge locations **speed up content delivery** via services like **CloudFront**.
- These three components solve three distinct problems: **location/compliance, availability/fault tolerance, and speed/performance**.

## Quick Revision Notes and Memory Aids
- Region = **city / warehouse**; AZ = **building**; Edge = **neighborhood hub**.
- Region choice affects: **performance, cost, compliance**.
- AZ benefits require **multi-AZ design**.
- Edge locations accelerate content via **CloudFront**.

## Exam Tips and Common Pitfalls
- **High availability is not automatic** — must be **designed** with multiple AZs.
- Region selection is the **first architectural decision**.
- Edge locations deliver **cached content**, not run full applications.
- Regions are **independent**, not synchronized by default.
