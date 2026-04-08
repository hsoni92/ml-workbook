# Comparing Cloud Service Models

## Objective
Compare IaaS, PaaS, and SaaS through responsibility layers and business use cases.

## Responsibility Stack
Typical layers in cloud stack:
- Networking
- Servers
- Storage
- Virtualization
- Operating System
- Runtime
- Application
- Data

How management shifts:
- In IaaS, customer manages more upper layers.
- In PaaS, provider manages more platform layers.
- In SaaS, provider manages almost everything.

## Model-by-Model Responsibility Split

### IaaS
- **Provider:** networking, servers, storage, virtualization
- **Customer:** OS, runtime, applications, data
- **Best for:** teams needing deep customization and control

### PaaS
- **Provider:** infra + OS + runtime + significant operations
- **Customer:** application code + data
- **Best for:** faster development and deployment with lower ops burden

### SaaS
- **Provider:** full stack including application
- **Customer:** product usage and business configuration
- **Best for:** quick adoption of ready-made business tools

## Control vs Convenience Trade-off
- **More control -> more responsibility** (IaaS)
- **More convenience -> less control** (SaaS)
- **PaaS** sits in the middle for many modern app teams

## Practical Selection Logic
- Choose IaaS for legacy migration, specialized security, and custom environments.
- Choose PaaS when developer productivity and release speed are priority.
- Choose SaaS when business function is more important than custom engineering.

## Common Real-World Pattern
Most organizations use a mixed portfolio:
- IaaS for custom workloads
- PaaS for in-house app development
- SaaS for commodity business capabilities (mail, CRM, collaboration)

## Exam-Oriented Summary Table
| Model | Control Level | Customer Effort | Typical Benefit |
|---|---|---|---|
| IaaS | High | High | Flexibility and customization |
| PaaS | Medium | Medium | Faster development |
| SaaS | Low | Low | Fastest adoption and simplicity |

## Quick Revision
- Service model comparison is fundamentally about "who manages what."
- No single model is universally best; choice depends on business context.
