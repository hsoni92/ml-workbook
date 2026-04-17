# Cost, Compliance, and Global Availability (Week 3)

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
- Three factors almost always decide which cloud provider an organization chooses:
  1. **Cost**
  2. **Compliance**
  3. **Global availability**
- These are **not technical features** — they are **business decision drivers**.

## Terminology and Definitions
- **Pay-as-you-go Model**: You pay only for what you consume (compute time, storage used, data transferred).
- **Compliance**: Rules and regulations controlling how data is stored, processed, and protected (e.g., healthcare, financial, personal data).
- **Shared Responsibility (in Compliance)**: Provider ensures infrastructure meets compliance; customer ensures correct usage.
- **Global Availability**: How close an application is deployed to its users, measured by regions and reach.
- **Latency**: Delay between request and response — reduced by deploying closer to users.
- **Operational Cost of Global Reach**: More regions → more infrastructure, more replication, higher operational cost.

## Detailed Explanations
### 1. Cost
- Cloud uses a **pay-as-you-go** model:
  - Pay only for what you consume (compute time, storage, data transfer).
  - Removes the need to buy servers upfront.
- New risk: **If resources are left running unnecessarily, costs can grow very quickly**.
- **Analogy**: Cloud is like **electricity** — pay only for usage, but leaving lights and AC on generates a surprise bill.
- Provider-level differences:
  - **AWS** — most flexible services; without strong controls, it can become expensive.
  - **Azure** — often reduces cost for organizations already using Microsoft tools.
  - **GCP** — known for **automated discounts** when workloads run consistently.

### 2. Compliance
- Compliance is about **rules and regulations** controlling how data is stored, processed, and protected.
- Examples of regulated data:
  - Healthcare data.
  - Financial data.
  - Personal user data.
- **Common misunderstanding**: moving to cloud automatically makes you compliant. **Not true.**
- Cloud providers ensure their **infrastructure meets compliance standards**.
- **How you use that infrastructure** determines whether the application is compliant.
- Provider-level differences:
  - **AWS** — widest global compliance coverage.
  - **Azure** — very strong in government and enterprise-heavy industries.
  - **GCP** — particularly strong in data privacy and analytics-focused compliance.

### 3. Global Availability
- About **how close the application is to its users**.
- Multi-region deployment:
  - Reduces latency.
  - Improves user experience.
- But more regions mean:
  - More infrastructure.
  - More replication.
  - Higher operational cost.
- Provider-level differences:
  - **AWS** — largest number of regions globally.
  - **Azure** — follows closely, driven by enterprise demand.
  - **GCP** — fewer regions, but benefits from one of the **fastest global networks** in the world.

### Architectural Trade-off
- You usually **cannot optimize all three at once**:
  - Lower cost.
  - Strict compliance.
  - Global low-latency access.
- Architects must **prioritize based on business needs**:
  - Banking → compliance over cost.
  - Startup → cost over global reach.
  - Streaming platform → global availability above all else.

### Strategic Framing
- Cost, compliance, and global availability are **not cloud features**.
- They are **strategic design decisions**.
- Understanding how each provider approaches them helps architects choose the right cloud — not just the popular one.

## Workflows / Process Steps
### Business-Driven Provider Selection
1. Identify key business drivers: **cost, compliance, global reach**.
2. Rank priorities for the specific workload.
3. Map priorities to provider strengths:
   - Cost-conscious enterprise on Microsoft → **Azure**.
   - Consistent workloads seeking discounts → **GCP**.
   - Broad coverage and services → **AWS**.
4. Validate compliance fit for the target industry.
5. Design deployment (number of regions, replication) based on availability goals.
6. Continuously monitor cost and compliance posture.

## Examples and Use Cases
- **Banking system** → prioritizes **compliance** over cost and latency.
- **Startup** → prioritizes **cost** over global reach.
- **Streaming platform** → prioritizes **global availability** above everything else.
- **Enterprise already using Microsoft** → usually chooses Azure for cost and compliance alignment.
- **Consistent, predictable workloads** → benefit from GCP's automated discounts.

## Comparison Tables
### Provider Approach to Cost, Compliance, Global Availability
| Factor | AWS | Azure | GCP |
|---|---|---|---|
| Cost | Most flexible; requires strong cost controls | Often cheaper for Microsoft-centric orgs | Automated discounts for consistent workloads |
| Compliance | Widest global compliance coverage | Strong in government and enterprise-heavy industries | Strong in data privacy and analytics compliance |
| Global Availability | Largest number of regions | Follows closely, enterprise-driven | Fewer regions, extremely fast global network |

### Business Priority → Trade-off Choice
| Business Priority | Typical Trade-off |
|---|---|
| Banking / regulated | Compliance over cost |
| Startup / MVP | Cost over global reach |
| Streaming / global apps | Global availability first |
| Steady, predictable workloads | Cost via automated discounts |

## Key Takeaways and Summary
- Cost, compliance, and global availability are **business decision drivers**, not just technical features.
- Cloud uses **pay-as-you-go**; leaving resources on drives costs up fast.
- **Compliance is a shared responsibility** — infrastructure compliance ≠ application compliance.
- Providers differ meaningfully:
  - AWS → widest services and compliance coverage.
  - Azure → Microsoft-centric cost and governance strengths.
  - GCP → automated discounts + fastest global network.
- Architects must **prioritize** — you usually cannot optimize all three factors simultaneously.

## Quick Revision Notes and Memory Aids
- Three decision drivers: **Cost, Compliance, Global Availability**.
- Cloud bill analogy: **Electricity** — leave lights/AC on = surprise bill.
- AWS → **widest** on services and compliance.
- Azure → **best on Microsoft cost/compliance fit**.
- GCP → **automated discounts + fastest network**.
- Trade-off mantra: **pick 1-2, rarely all three**.

## Exam Tips and Common Pitfalls
- Don't describe cost/compliance/global availability as **features** — they are **business decisions**.
- Remember: cloud does **not** make an app compliant automatically.
- GCP has **fewer regions** but a very fast network — common distractor.
- Do not claim providers cover all three priorities equally — they differ meaningfully.
- Match provider strengths to **workload business profile** (banking, startup, streaming, etc.).
