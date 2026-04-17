# Multi-tenancy (Week 2)

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
- **Multi-tenancy** is a foundational concept behind almost every cloud and SaaS platform.
- It means **one application and infrastructure serves multiple customers (tenants)** while keeping each tenant's data and access isolated.
- A tenant can be:
  - An individual user.
  - A company.
  - An entire organization.
- The alternative — running a separate stack per customer — would be **extremely expensive and inefficient**.
- Multi-tenancy allows cloud platforms to:
  - Share resources.
  - Reduce cost.
  - Scale to millions of users.

## Terminology and Definitions
- **Multi-tenancy**: An architecture where a single instance of an application and its infrastructure serves many customers, with logical or physical separation between them.
- **Tenant**: A customer consuming the shared system (user, company, or organization).
- **Isolation**: Ensuring one tenant cannot access another tenant's data.
- **Fair Resource Usage**: Ensuring no tenant degrades performance for others.
- **Noisy Neighbor Problem**: When one tenant consumes excessive resources and impacts others.
- **Rate Limits (Quotas)**: Caps on how much of a resource a tenant can use.
- **Autoscaling**: Automatic resource adjustment to match demand.
- **Tiered Service Model**: Different service levels (performance/cost) offered to different tenants.

## Detailed Explanations
### Architectural Goals
Three architectural goals must be achieved **at the same time** for multi-tenancy to work correctly:
1. **Isolation** — One tenant must never access another tenant's data.
2. **Fair resource usage** — One tenant must not degrade performance for others.
3. **Scalability** — Tenants grow at different rates, and the system must handle it gracefully.

### Multi-Tenancy Models
Three models are common in practice:

#### 1. Shared Everything Model
- All tenants share the same application and database.
- Data is **logically** separated (e.g., tenant ID in every row).
- **Pros**: Highly scalable and cost-effective.
- **Cons**: Requires very careful isolation logic; a bug can expose tenants to each other.

#### 2. Shared Application with Separate Databases
- Tenants share the application but each has their **own database**.
- **Pros**: Improves isolation; simplifies backups.
- **Cons**: Increases cost and operational effort.

#### 3. Fully Isolated Tenancy
- Each tenant gets a **dedicated application and database**.
- **Pros**: Strongest isolation; preferred for regulated industries.
- **Cons**: Most expensive; hardest to scale.

### Noisy Neighbor Problem and Mitigation
- A major challenge in multi-tenant systems is when one tenant consumes excessive resources and affects others.
- Architects mitigate this with:
  - **Rate limits (quotas)**.
  - **Autoscaling**.
  - **Tiered service models** (covered in later modules).

### Security Risks in Multi-Tenancy
- Many tenants share the same system, so a single vulnerability can impact multiple users.
- Mitigations include:
  - **Strong access controls**.
  - **Encryption** (at rest and in transit).
  - **Tenant-aware security checks**.

### Why Multi-Tenancy Is a Core Architectural Decision
- Directly impacts:
  - Cost
  - Security
  - Scalability
  - Compliance
- Choice of model depends on **business needs**.

## Workflows / Process Steps
### Selecting a Multi-Tenancy Model
1. Define tenant profile (individual, company, enterprise, regulated industry).
2. Identify isolation requirements (regulatory, contractual, security).
3. Estimate scale (number of tenants, growth rate).
4. Choose model:
   - Cost and scale priority → **Shared Everything**.
   - Balanced isolation and simplicity → **Shared App, Separate DBs**.
   - Strong isolation / compliance → **Fully Isolated**.
5. Add safeguards: rate limits, autoscaling, tiered service levels, tenant-aware security.

## Examples and Use Cases
- **SaaS platforms** serving millions of small-business customers (shared everything).
- **Enterprise SaaS** with dedicated databases per enterprise customer.
- **Regulated industries** (finance, healthcare) with fully isolated tenancy.
- Mitigating **noisy neighbors** for tenants running heavy analytics workloads.

## Comparison Tables
### Multi-Tenancy Models
| Model | Isolation Level | Cost | Scalability | Complexity | Typical Use Case |
|---|---|---|---|---|---|
| Shared Everything | Logical only | Lowest | Highest | Requires careful isolation logic | High-scale SaaS |
| Shared App, Separate DB | Medium | Medium | Medium-High | Medium | Enterprise SaaS |
| Fully Isolated | Strongest | Highest | Lowest | Highest | Regulated / compliance-heavy |

### Goals vs Risks
| Goal | Key Risk if Violated |
|---|---|
| Isolation | Data leakage between tenants |
| Fair resource usage | Noisy neighbor impact |
| Scalability | Degraded performance as tenants grow |

## Key Takeaways and Summary
- Multi-tenancy enables cloud platforms to **share resources, reduce cost, and scale to millions**.
- It requires **isolation, fair resource usage, and scalability** simultaneously.
- Three models trade off cost vs isolation: **shared everything**, **shared app + separate DB**, and **fully isolated**.
- The **noisy neighbor problem** is mitigated with rate limits, autoscaling, and tiered services.
- Security requires **strong access controls, encryption, and tenant-aware checks**.
- Choice of model depends on **business and compliance needs**.

## Quick Revision Notes and Memory Aids
- **Three goals**: Isolation, Fair Usage, Scalability.
- **Three models**: Shared Everything → Shared App + Separate DB → Fully Isolated (strictness increases, cost increases).
- **Noisy Neighbor** = one tenant hogs resources → fix with **rate limits + autoscaling + tiered models**.
- **Security levers**: access control, encryption, tenant-aware checks.

## Exam Tips and Common Pitfalls
- Do not confuse multi-tenancy with multi-region or multi-cloud.
- When asked about regulated industries, the correct model is usually **fully isolated tenancy**.
- "Noisy neighbor" is a direct multi-tenancy term — expect it to be tested.
- Do not forget that multi-tenancy impacts **compliance**, not just cost and scale.
