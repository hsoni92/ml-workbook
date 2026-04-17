# Performance Considerations in Cloud (Week 2)

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
- **Performance** in the cloud is not just about making systems fast.
- It is about making them **consistently responsive** even as traffic patterns change.
- Performance answers:
  - How quickly does the system respond?
  - Does it remain stable under load?
  - Does it use resources efficiently while doing so?
- In cloud environments, performance problems usually come from **architectural decisions**, not from lack of hardware.

## Terminology and Definitions
- **Performance**: How responsive, stable, and efficient a system is under varying load.
- **Compute Family**: A category of machines (e.g., virtual machines) suited for specific workload profiles.
- **CPU-heavy workload**: Bound by processing.
- **Memory-heavy workload**: Bound by RAM.
- **GPU workload**: Needs specialized GPU compute (AI/ML, rendering).
- **Latency**: Time taken to respond.
- **IOPS**: Input/output operations per second (storage throughput in ops).
- **Throughput**: Data transferred per unit time.
- **Object Storage**: Scalable, durable storage (not optimized for low latency).
- **Block Storage**: Storage volumes ideal for databases and I/O-intensive workloads.
- **In-memory Storage**: Volatile, extremely fast storage (e.g., caches).
- **Caching**: Storing frequently accessed data closer to the application or user.
- **CDN (Content Delivery Network)**: Distributed caching at the edge to reduce latency.
- **Load Balancer**: Distributes traffic across multiple servers to prevent hotspots.
- **Data Locality**: Placing data close to where it is consumed.
- **Chatty Service**: Architecture making many small synchronous calls; amplifies latency.

## Detailed Explanations
### Why Performance Matters
- User expectations are extremely high today.
- Slow applications cause users to leave.
- Unreliable performance under peak load erodes trust.
- In the cloud, problems typically come from **architecture**, not hardware scarcity.

### Components of Cloud Performance
#### 1. Compute Performance
- Choose the right **compute family** (machine type) for the workload.
- Workload types behave very differently:
  - **CPU-heavy** tasks.
  - **Memory-heavy** tasks.
  - **GPU workloads**.
- Using a **large general-purpose instance for a memory-intensive workload** results in poor performance and wasted cost.
- Cloud performance begins with **matching workload to compute family**.

#### 2. Storage Performance
- One of the most common bottlenecks.
- Depends on:
  - **Latency**
  - **IOPS**
  - **Throughput**
- Storage choices:
  - **Object storage** — excellent for durability and scale; not ideal for low-latency access.
  - **Block storage** — ideal for databases.
  - **In-memory storage** — fastest access; volatile.
- Using the wrong storage type can slow even the best-designed application.

#### 3. Network Performance
- In distributed cloud systems, **network latency adds up quickly**.
- Cross-zone or cross-region calls introduce delay.
- A **chatty service** magnifies the problem.
- Key architectural principle: **minimize synchronous network calls** and **keep related services close together**.

#### 4. Caching and Data Locality
- Caching is one of the most effective ways to improve performance.
- Storing frequently accessed data closer to the application or user:
  - Reduces database load.
  - Improves response time.
- Essential tools:
  - **CDNs (Content Delivery Networks)**.
  - **Distributed systems caching**.
  - **Application-level caching**.

#### 5. Load Balancing
- Distributes traffic evenly.
- Prevents **hotspots** and ensures no single server is overwhelmed.
- One of the pillars of cloud architecture.
- Advanced routing techniques can direct users to the **closest or fastest backend**, improving global performance.

### Scalability vs Performance
- They are **related but not the same**.
- **Scalability** — can the system grow?
- **Performance** — how well it behaves at any point in time?
- A system can scale beautifully and still perform poorly if it's poorly designed.

## Workflows / Process Steps
### Performance Design Workflow
1. Profile the workload (CPU, memory, GPU, I/O).
2. Select the right **compute family** for that workload.
3. Choose the appropriate **storage type** (object/block/in-memory) based on latency, IOPS, throughput.
4. Minimize **synchronous network calls**; co-locate tightly coupled services.
5. Introduce **caching** (CDN, distributed, application-level) for hot data.
6. Apply **load balancing** and advanced routing to distribute traffic.
7. Continuously monitor and tune as traffic patterns evolve.

## Examples and Use Cases
- Using **in-memory cache** to reduce database hits for a hot product catalog.
- Placing an API close to its database to reduce **cross-zone latency**.
- Using a **CDN** to serve static assets close to end users globally.
- Selecting a **memory-optimized instance** for large in-memory analytics instead of general-purpose VMs.
- Using **block storage** for transactional databases and **object storage** for large media files.

## Comparison Tables
### Storage Types
| Storage Type | Strengths | Weaknesses | Typical Use |
|---|---|---|---|
| Object | Durable, scalable | Higher latency | Media, backups, archives |
| Block | Low latency, high IOPS | Not as scalable as object | Databases, transactional systems |
| In-memory | Fastest access | Volatile | Caches, session stores |

### Compute Performance Choices
| Workload Type | Optimal Compute | Wrong Choice Symptom |
|---|---|---|
| CPU-heavy | CPU-optimized instances | High CPU saturation, slow response |
| Memory-heavy | Memory-optimized instances | Swapping, latency spikes |
| GPU workloads | GPU instances | Severe slowness on CPU-only VMs |

### Scalability vs Performance
| Aspect | Scalability | Performance |
|---|---|---|
| Question | Can the system grow? | How well does it behave at any moment? |
| Focus | Capacity | Responsiveness, stability, efficiency |
| Possible gap | Can scale poorly-performing designs | Can perform well but not scale |

## Key Takeaways and Summary
- Cloud performance depends on:
  - Choosing the **right compute**.
  - Using the **correct storage type**.
  - Designing **efficient network paths**.
  - **Caching intelligently**.
  - **Distributing traffic effectively**.
- Performance problems in the cloud are typically **architectural**.
- Scalability and performance are complementary but distinct.

## Quick Revision Notes and Memory Aids
- **5 Pillars of Cloud Performance**: Compute, Storage, Network, Caching, Load Balancing.
- Storage choice matters: **Object (durable), Block (databases), In-memory (fastest)**.
- Network rule: **Keep related services close; avoid chatty synchronous calls**.
- Caching tools: **CDN, distributed cache, app-level cache**.
- **Scalability ≠ Performance**.

## Exam Tips and Common Pitfalls
- Don't pick "bigger VM" as the performance fix; the right **compute family** matters more.
- Object storage for databases is a classic wrong answer — use **block storage**.
- In-memory storage is **volatile**; don't propose it for persistence.
- Cross-region calls are a common hidden cause of latency.
- Remember: **chatty services amplify latency** even with small individual hops.
