# Google Cloud Architecture Framework (Week 2)

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
- The **Google Cloud Architecture Framework** reflects how Google designs and operates some of the **largest distributed systems in the world**.
- It is **not theoretical** — it is based on **decades of experience** running services like:
  - Google Search.
  - YouTube.
  - Gmail.
  - Google Maps.
  - Many other globally scaled services.
- Core goals of the framework:
  - Reliable systems.
  - Scalable systems.
  - Cost-efficient systems.
  - Sustainable systems.
- Strong emphasis on **automation** and **operational discipline**.

## Terminology and Definitions
- **Google Cloud Architecture Framework**: Google Cloud's authoritative architectural framework.
- **Site Reliability Engineering (SRE)**: Google's engineering discipline treating reliability as a measurable engineering problem.
- **Service Level Indicator (SLI)**: A measurable metric representing an aspect of service behavior.
- **Service Level Objective (SLO)**: A target value or range for an SLI.
- **Error Budget**: The amount of failure tolerated within a given time window (derived from SLOs).
- **Automation-First Operations**: Automated recovery, rollback, and self-healing without human intervention.
- **Self-Healing Systems**: Systems designed to recover automatically from failure.
- **Global Load Balancing**: Distributing traffic across regions to achieve low latency and high availability.
- **Multi-Region Deployment**: Deploying workloads to multiple regions by default.
- **BigQuery**: Google Cloud's serverless data warehouse for analytics.
- **Pub/Sub**: Google Cloud's messaging service.
- **Dataflow**: Google Cloud's stream and batch data processing service.
- **Vertex AI**: Google Cloud's ML/AI platform.
- **Carbon-Aware Workload Placement**: Scheduling workloads to reduce carbon impact.

## Detailed Explanations
### What the Framework Delivers
- Helps teams design systems that are:
  - **Reliable**.
  - **Scalable**.
  - **Cost-efficient**.
  - **Sustainable**.
- Strong emphasis on **automation** and **operational discipline**.

### Focus Areas of the Framework
The framework is organized around several key focus areas:
- **Operational excellence**.
- **Security and compliance**.
- **Reliability**.
- **Performance optimization**.
- **Cost optimization**.
- **Sustainability**.

### Site Reliability Engineering (SRE)
- Google's unique approach, one of its most important contributions to modern cloud architecture.
- Reliability is treated as a **measurable engineering problem**, not a vague goal.
- Teams define:
  - **Service-Level Indicators (SLIs)**.
  - **Service-Level Objectives (SLOs)**.
  - **Error Budgets** — how much failure is acceptable.
- This creates a **balance between innovation and stability**:
  - Systems are designed to **fail safely** and **recover automatically**.
  - The focus is not chasing **perfect uptime**.

### Automation-First Operations
- Automation plays a **central role**.
- Manual recovery steps are **completely discouraged**.
- Systems are designed to:
  - **Heal themselves**.
  - **Roll back to previous versions automatically**.
  - **Respond to failures without human intervention**.
- Failure is **not an exception** — it is an **expected condition** the system must handle carefully.

### Global Networking and Performance
- Google operates one of the **largest private fiber networks** in the world.
- Allows applications to deliver **low latency** and **high performance** across regions.
- The framework encourages designs that are **global by default** using:
  - **Multi-region deployments**.
  - **Global load balancing**.

### Data and AI Focus
- Google Cloud is optimized for:
  - Analytics.
  - Streaming.
  - Machine learning workloads.
- Common services used in architectures:
  - **BigQuery** — data warehouse / analytics.
  - **Pub/Sub** — messaging.
  - **Dataflow** — event/stream data processing.
  - **Vertex AI** — ML platform.
- Used to build **scalable, event-driven data pipelines** and **intelligent applications**.

### Cost Optimization and Sustainability
- Both are **deeply integrated** in the framework.
- Framework promotes:
  - **Auto-scaling**.
  - **Serverless models**.
  - **Efficient resource usage**.
  - **Carbon-aware workload placement**.
- The goal is not only **reducing cost**, but **operating responsibly and efficiently at scale**.

## Workflows / Process Steps
### SRE Reliability Workflow
1. Identify critical behaviors for users.
2. Define **SLIs** measuring those behaviors.
3. Set **SLOs** (targets) aligned to business needs.
4. Derive an **error budget** from the SLO.
5. Balance innovation vs stability using the error budget.
6. Automate recovery, rollback, and self-healing.
7. Measure, adjust, and continuously improve.

### Global-by-Default Workflow
1. Deploy workloads across multiple regions.
2. Use global load balancing to route users to nearest/healthiest backend.
3. Leverage Google's private fiber network for low latency.
4. Minimize synchronous cross-region calls.

## Examples and Use Cases
- Running global services (Search, YouTube, Gmail, Maps scale) that influenced this framework.
- Using **error budgets** to allow calculated risk during releases.
- Building **data pipelines** with **Pub/Sub → Dataflow → BigQuery**.
- Training and serving ML models using **Vertex AI**.
- **Carbon-aware workload placement** to reduce environmental impact.

## Comparison Tables
### Framework Focus Areas
| Focus Area | Description |
|---|---|
| Operational Excellence | Run and improve systems via automation and discipline |
| Security and Compliance | Protect systems and meet regulatory requirements |
| Reliability | Measurable, SRE-driven |
| Performance Optimization | Global scale, low latency |
| Cost Optimization | Auto-scaling, serverless, efficient use |
| Sustainability | Carbon-aware placement, efficient operations |

### SRE Core Constructs
| Term | Meaning |
|---|---|
| SLI | Measurable metric |
| SLO | Target for an SLI |
| Error Budget | Allowable failure within a window |

### Framework Signatures (Cross-Provider Context)
| Provider | Distinctive Emphasis |
|---|---|
| AWS Well-Architected | Six pillars, broad architectural review model |
| Azure Architecture Center | Reference architectures, patterns and anti-patterns |
| Google Cloud Architecture Framework | SRE discipline, automation-first, global-by-default, data/AI strength |

## Key Takeaways and Summary
- Google's framework is rooted in **real-world, global-scale operations**.
- **SRE** transforms reliability into a **measurable engineering problem** with **SLIs, SLOs, and error budgets**.
- **Automation-first** operations are mandatory — **manual recovery is discouraged**.
- **Global-by-default** design is enabled by Google's private fiber network, multi-region deployments, and global load balancing.
- Strong **data and AI focus**: BigQuery, Pub/Sub, Dataflow, Vertex AI.
- Cost optimization and sustainability are **integrated**, not optional.
- Understanding this framework alongside AWS and Azure helps architects design **across providers**.

## Quick Revision Notes and Memory Aids
- Remember: **SRE = SLI + SLO + Error Budget**.
- Google design principle: **Global by default**.
- Data stack: **Pub/Sub → Dataflow → BigQuery; ML via Vertex AI**.
- Framework focus areas: **Ops, Security/Compliance, Reliability, Performance, Cost, Sustainability**.
- Automation over manual recovery.

## Exam Tips and Common Pitfalls
- **SRE** is a Google-specific framing of reliability, but its concepts apply broadly.
- Error budget does **not** mean "we plan to break things" — it is a **controlled failure tolerance**.
- Global load balancing is a **distinct Google strength**.
- Carbon-aware placement is part of sustainability — new but testable.
- Manual recovery steps are a **red flag** in Google's framework.
