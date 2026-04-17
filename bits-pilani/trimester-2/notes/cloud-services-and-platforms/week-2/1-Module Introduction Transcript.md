# Module Introduction (Week 2)

## Table of Contents
- [Core Concepts](#core-concepts)
- [Terminology and Definitions](#terminology-and-definitions)
- [Detailed Explanations](#detailed-explanations)
- [Workflows / Process Steps](#workflows--process-steps)
- [Examples and Use Cases](#examples-and-use-cases)
- [Module Roadmap](#module-roadmap)
- [Key Takeaways and Summary](#key-takeaways-and-summary)
- [Quick Revision Notes and Memory Aids](#quick-revision-notes-and-memory-aids)
- [Exam Tips and Common Pitfalls](#exam-tips-and-common-pitfalls)

## Core Concepts
- Module 2 shifts focus from **what** the cloud is to **how** cloud systems are designed.
- This module centers on **cloud architecture and design principles** that guide every high-quality cloud system used in the real world.
- Module 1 established foundations; Module 2 introduces the architect's mindset: planning, decision-making, and trade-off analysis.
- Cloud work is not just provisioning virtual machines; it is about designing systems that:
  - Scale smoothly under growing demand.
  - Perform efficiently under varying workloads.
  - Survive component and zone failures.
  - Remain secure throughout their lifecycle.
- The module covers core architectural principles and industry-standard frameworks representing decades of real-world engineering experience.

## Terminology and Definitions
- **Cloud Architecture**: The structured design of cloud systems, covering components, interactions, and trade-offs to meet scalability, reliability, performance, and security goals.
- **Design Principle**: A proven guideline used when making architectural decisions (e.g., redundancy, elasticity, least privilege).
- **Scalability**: A system's ability to handle growth without degrading.
- **Elasticity**: A system's ability to automatically grow and shrink in response to demand.
- **High Availability (HA)**: Designing systems to remain operational most of the time by recovering quickly from failures.
- **Fault Tolerance (FT)**: Designing systems to continue operating without interruption even when components fail.
- **Multi-tenancy**: A model where one shared application and infrastructure serve multiple customers (tenants) with logical isolation.
- **Well-Architected Framework**: An industry set of guiding pillars (originally AWS) used to review and improve cloud systems.
- **Azure Architecture Center**: Microsoft's official guidance platform for designing Azure cloud architectures.
- **Google Cloud Architecture Framework**: Google Cloud's official framework reflecting SRE practices and global-scale design.

## Detailed Explanations
### Purpose of the Module
- Build the **mindset and vocabulary of a cloud architect**.
- Teach **why** certain systems succeed under heavy load while others fail.
- Clarify why some applications scale naturally while others struggle to do so.
- Show how organizations design cloud environments that are both resilient and cost-effective.

### Topics Introduced
- Scalability and elasticity.
- High availability vs fault tolerance.
- Multi-tenancy and its architectural trade-offs.
- Reliability in cloud architecture.
- Performance considerations.
- Trade-offs across cost, latency, resilience, and complexity.
- Six pillars of the Well-Architected Framework.
- AWS Well-Architected Framework (deep dive across two parts).
- Azure Architecture Center (Microsoft perspective).
- Google Cloud Architecture Framework (Google/SRE perspective).
- Cross-cloud architecture principles that apply universally.

### Outcomes by End of Module
- Ability to think like a cloud architect.
- Vocabulary to discuss architectural quality attributes.
- Understanding of why systems succeed or fail under load.
- Knowledge of how resilient and cost-effective cloud environments are designed.

## Workflows / Process Steps
### How the Module Progresses
1. Start with individual design principles (scalability, elasticity, HA vs FT, multi-tenancy).
2. Extend into system-wide qualities (reliability, performance, trade-offs).
3. Introduce the Well-Architected Framework and its six pillars.
4. Deep dive into AWS pillars in two parts.
5. Compare architectural perspectives across Azure and Google Cloud.
6. Conclude with cross-cloud principles that remain stable regardless of provider.

## Examples and Use Cases
- Systems that succeed under heavy load because of correct architectural decisions.
- Applications that fail because they were not designed for scale, failure, or shared infrastructure.
- Enterprises designing resilient, cost-effective cloud environments using frameworks.

## Module Roadmap
```
Week 2 Flow
 ─────────────────────────────────────────────
 Principles  →  Qualities  →  Frameworks  →  Cross-Cloud
 Scalability      Reliability    6 Pillars      Universal
 Elasticity       Performance    AWS (P1+P2)    Principles
 HA vs FT         Trade-offs     Azure AC
 Multi-tenancy                   GCP Framework
```

## Key Takeaways and Summary
- Module 2 is dedicated to **cloud architecture and design principles**.
- It covers both **principles** (scalability, elasticity, HA, FT, multi-tenancy) and **frameworks** (AWS, Azure, GCP).
- The module aims to develop architect-level thinking about scale, resilience, security, and cost.
- Architectural frameworks represent **decades of real-world engineering experience** rather than theoretical guidance.

## Quick Revision Notes and Memory Aids
- Module 1 = **What is cloud?**
- Module 2 = **How cloud is designed?**
- Four architect goals: **Scale, Perform, Survive, Secure**.
- Frameworks to know: **AWS Well-Architected, Azure Architecture Center, GCP Architecture Framework**.
- Mnemonic for topics in order: **S-E-HA-FT-MT-R-P-T-6P-AWS-Azure-GCP-Cross**.

## Exam Tips and Common Pitfalls
- Remember that cloud architecture is about **balanced decisions**, not perfect ones.
- Do not equate cloud architecture with merely "spinning up VMs."
- Frameworks are **not vendor-exclusive ideas**; principles are universal.
- Expect comparative questions across AWS, Azure, and GCP frameworks.
