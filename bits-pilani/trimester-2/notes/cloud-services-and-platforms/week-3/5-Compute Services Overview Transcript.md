# Compute Services Overview (Week 3)

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
- **Compute** = the **processing power that runs applications**.
- Anytime an app runs, an API responds, or a job is processed, compute resources are involved behind the scenes.
- Across all cloud providers, compute usually takes the form of **virtual machines (VMs)**:
  - Behave like physical servers.
  - Can be **created, resized, scaled, and destroyed in minutes**.
- Compute choices directly impact:
  - Application **speed**.
  - **Scalability**.
  - **Cost**.
  - **Reliability**.
  - **Operational complexity**.
- Most cloud problems eventually trace back to a **compute decision**.

## Terminology and Definitions
- **Compute**: Processing power that runs applications.
- **Virtual Machine (VM)**: Software-simulated server with CPU, memory, disk, and networking.
- **Instance Family / Type**: A compute category optimized for a specific profile (general-purpose, memory-optimized, GPU, etc.).
- **Custom Machine Type**: A Google Cloud feature allowing precise selection of vCPUs and memory.
- **AWS EC2**: AWS's compute service.
- **Azure Virtual Machines**: Azure's compute service.
- **Google Compute Engine (GCE)**: Google's compute service.
- **Hybrid Cloud**: Workload distributed across on-premise and cloud.

## Detailed Explanations
### AWS EC2
- **Oldest cloud compute service** and **most feature-rich**.
- Offers a **massive variety of instance types** from small general-purpose to high-end GPU servers.
- Gives architects significant control:
  - Instance family.
  - CPU architecture.
  - Memory profile.
  - Networking performance.
- Extremely flexible but **many choices to understand**.
- Commonly used when teams need **flexibility and support for many different workload types**.

### Azure Virtual Machines
- Heavily **optimized for enterprise environments**, especially those already using Microsoft technologies.
- Integrates very well with:
  - Windows Server.
  - Active Directory.
  - SQL Server.
  - .NET applications.
- Shines in **hybrid cloud scenarios** (some systems run on-premise, others in the cloud).
- For enterprises migrating existing data centers, Azure VMs often feel like a **natural extension** of what they already know.

### Google Compute Engine (GCE)
- Reflects Google's internal engineering culture: **performance, simplicity, automation**.
- Standout feature: **custom machine types** — choose exactly how many CPUs and how much memory are needed, nothing more or less.
- Popular for:
  - Data-intensive workloads.
  - Analytics.
  - Machine learning.
  - Performance-sensitive systems.
- Benefits from **Google's global network** for strong performance characteristics.

### Shared Principle + Differences
- All three providers give you **virtual machines** — same core idea.
- Differences are in **positioning**:
  - **AWS** → breadth and flexibility.
  - **Azure** → enterprise and Microsoft integration.
  - **Google Cloud** → performance and data workloads.
- **Analogy**: Different **rental car companies** — you're renting a car in all cases, but the experience, options, and strengths vary.

### How Architects Choose Compute
- Architects rarely ask which cloud is "better."
- They ask:
  - What workload am I running?
  - Do I need performance or flexibility?
  - Am I cost sensitive?
  - How important is enterprise integration?
  - What does my team already know?
- Those answers guide the compute decision.

## Workflows / Process Steps
### Choosing a Compute Service
1. Characterize the workload (CPU, memory, GPU, I/O).
2. Evaluate sensitivity to cost and performance.
3. Consider enterprise integration and skill set.
4. Pick provider based on:
   - Breadth/flexibility → **AWS EC2**.
   - Enterprise / Microsoft-heavy → **Azure VMs**.
   - Data / performance → **GCE**.
5. Select appropriate instance family (general-purpose, memory-optimized, GPU, etc.).
6. Validate with workload benchmarks and cost analysis.

## Examples and Use Cases
- Running varied workloads across multiple instance types on **EC2**.
- Migrating on-premise Microsoft workloads to **Azure VMs** for familiarity and integration.
- Running ML training on custom-sized VMs in **GCE** to match workload precisely.
- Using GPU instances across providers for deep-learning or rendering workloads.

## Comparison Tables
### Compute Services Across Providers
| Provider | Service | Key Strength | Typical Fit |
|---|---|---|---|
| AWS | EC2 | Most feature-rich, widest instance variety | Flexibility and broad workload types |
| Azure | Virtual Machines | Microsoft ecosystem, hybrid cloud | Enterprises on Microsoft stack |
| Google Cloud | Compute Engine (GCE) | Performance, simplicity, custom machine types | Data-intensive and ML workloads |

### Positioning Summary
| Provider | Focus |
|---|---|
| AWS | Breadth and flexibility |
| Azure | Enterprise and Microsoft integration |
| GCP | Performance and data workloads |

### Selection Criteria
| Question | Implication |
|---|---|
| What is the workload type? | Determines instance family |
| Need flexibility? | Lean AWS |
| Heavy Microsoft integration? | Lean Azure |
| Data/ML focus? | Lean GCP |
| Cost-sensitive? | Consider right-sizing, pricing models |
| Team skill? | Favor provider team knows best |

## Key Takeaways and Summary
- All three providers offer VMs — same core capability.
- **AWS EC2** is the oldest and most feature-rich, ideal for flexibility.
- **Azure VMs** are optimized for enterprise and Microsoft ecosystems.
- **Google Compute Engine** prioritizes performance, simplicity, and custom sizing.
- Compute decisions shape **performance, scalability, cost, and reliability** — choose based on workload, not hype.

## Quick Revision Notes and Memory Aids
- AWS EC2 → **most feature-rich, widest variety**.
- Azure VMs → **Microsoft integration + hybrid**.
- GCE → **performance + custom machine types**.
- All = **VMs created/resized/scaled/destroyed in minutes**.
- Analogy: **Different rental car companies**.

## Exam Tips and Common Pitfalls
- Custom machine types is a **GCE-specific** feature — don't associate with AWS/Azure.
- Hybrid cloud integration is a signature **Azure** strength.
- AWS's strength is **variety**, not necessarily lowest cost.
- Compute decisions ripple into cost, scalability, reliability — always consider downstream effects.
