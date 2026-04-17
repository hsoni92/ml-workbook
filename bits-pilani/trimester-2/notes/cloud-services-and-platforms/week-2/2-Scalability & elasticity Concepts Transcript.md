# Scalability and Elasticity Concepts (Week 2)

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
- **Scalability** and **elasticity** are two foundational cloud concepts that determine whether a system can grow, adapt to changing demand, and remain stable under pressure.
- Scalability is about capacity for growth.
- Elasticity adds automation and responsiveness to both increases and decreases in demand.
- Cloud environments strongly favor **horizontal scaling** and **elastic architectures**.

## Terminology and Definitions
- **Scalability**: A system's ability to handle growth in users, requests, or data without failing to meet performance expectations.
- **Vertical Scalability (Scale-Up)**: Increasing the power of a single machine by adding CPU, memory, or faster storage.
- **Horizontal Scalability (Scale-Out)**: Adding more machines and distributing the workload across them.
- **Elasticity**: A system's ability to scale up and down automatically based on demand, without manual intervention.
- **Autoscaling Group / Autoscaler**: Cloud service that monitors metrics (e.g., CPU usage, request volume) and adjusts capacity automatically.
- **Over-Provisioning**: Running more resources than needed, wasting cost.
- **Under-Provisioning**: Running fewer resources than needed, hurting performance and user experience.

## Detailed Explanations
### Why Scalability Matters
- Real-world traffic is unpredictable.
- Applications may perform well under normal load but fail during sudden spikes (e.g., sales, viral events).
- If the architecture cannot handle growth, the system fails.
- Scalability ensures continued performance as demand rises.

### Vertical Scalability (Scale-Up)
- Increases the power of a **single machine** by adding:
  - More CPUs
  - More memory
  - Faster storage
- **Pros**:
  - Simple to implement.
  - Often requires little to no application change.
- **Cons**:
  - Hardware has physical limits.
  - Scaling typically requires **downtime**.
  - High-end machines are expensive.
- **Common Use Cases**: Traditional databases, monolithic applications.

### Horizontal Scalability (Scale-Out)
- Adds **more machines** and distributes workload across them.
- **Pros**:
  - No theoretical upper limit.
  - Improves availability.
  - Increases fault tolerance.
  - Scaling happens **without downtime**.
- **Common Use Cases**: Web applications, microservices, NoSQL databases.
- Cloud environments **strongly favor** horizontal scaling.

### Elasticity
- Scalability answers **can it grow?**; elasticity answers **can it grow and shrink automatically based on demand?**
- Elastic systems scale **up** when traffic increases and **down** when traffic drops, with **no manual intervention**.
- Critical because cloud workloads fluctuate constantly.
- Cloud platforms provide elasticity through:
  - **Autoscaling groups**
  - **Autoscalers**
- These tools monitor metrics such as **CPU usage** and **request volume** and adjust capacity automatically.

### Why Elasticity Matters
- Avoids two failure modes:
  - **Over-provisioning** wastes money on unused resources.
  - **Under-provisioning** hurts performance and user experience.
- Elastic systems balance these by delivering performance when needed and saving cost when demand drops.

## Workflows / Process Steps
### Elasticity Control Loop
1. Autoscaler monitors metrics (e.g., CPU, request volume).
2. When threshold is exceeded, capacity is increased (scale-out).
3. When demand drops, capacity is reduced (scale-in).
4. Continuous adjustment happens without manual intervention.

## Examples and Use Cases
- **Food delivery applications** – demand peaks at meal times.
- **Ride-sharing services** – demand spikes during rush hours and events.
- **Streaming platforms** – traffic surges during launches and live events.
- **Flash sales** – large, short-lived traffic spikes.
- **Traditional databases / monolithic apps** – often rely on vertical scaling.
- **Web apps, microservices, NoSQL databases** – designed for horizontal scaling.

## Comparison Tables
### Vertical vs Horizontal Scalability
| Dimension | Vertical (Scale-Up) | Horizontal (Scale-Out) |
|---|---|---|
| Approach | Make one machine stronger | Add more machines |
| Upper limit | Hardware-bound | No theoretical upper limit |
| Downtime during scaling | Often required | Not required |
| Cost curve | High-end hardware is expensive | Uses commodity instances |
| Application changes | Minimal / none | Needs distributed design |
| Availability / fault tolerance | Limited | Improved |
| Typical use cases | Traditional databases, monoliths | Web apps, microservices, NoSQL |

### Scalability vs Elasticity
| Aspect | Scalability | Elasticity |
|---|---|---|
| Question answered | Can the system grow? | Can it grow *and* shrink automatically? |
| Direction | Primarily growth | Growth and contraction |
| Automation | Not required | Required |
| Cost behavior | May leave idle capacity | Optimizes cost continuously |
| Cloud-native preference | Foundation | Extension of scalability |

## Key Takeaways and Summary
- **Scalability enables growth**; a scalable system meets performance expectations under rising demand.
- **Horizontal scaling is preferred** in the cloud: no upper limit, better availability, no downtime.
- **Elasticity adds automation and cost efficiency** by scaling both up and down automatically.
- Together, **scalability + elasticity** form the foundation of **cloud-native architecture**.

## Quick Revision Notes and Memory Aids
- **Vertical = one stronger worker; Horizontal = more workers**.
- Scalability = **grow**; Elasticity = **grow + shrink automatically**.
- Elastic systems use **autoscaling groups / autoscalers** triggered by **CPU and request-volume** metrics.
- Cloud workloads fluctuate, so **elasticity ≠ luxury, it is cost control**.

## Exam Tips and Common Pitfalls
- Do not confuse scalability with elasticity; elasticity requires **automatic** bidirectional adjustment.
- Vertical scaling often requires downtime — mention this when comparing.
- Remember: cloud platforms **strongly prefer horizontal scaling**.
- Over-provisioning and under-provisioning are **opposite failure modes** that elasticity solves.
- Examples of elastic workloads in the exam typically include **food delivery, ride-sharing, streaming, flash sales**.
