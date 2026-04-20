# Blue-green & Rolling Deployments

## Why This Topic Matters

This note formalizes DevOps and CI/CD practices for safe, repeatable, and high-velocity software delivery.

## Learning Objectives

- Build first-principles understanding of `Blue-green & Rolling Deployments`.
- Connect concepts to architecture decisions in real cloud systems.
- Evaluate security, reliability, performance, and cost trade-offs rigorously.
- Prepare for scenario-based exam and interview questions.

## Intuition Before Mechanics

- Start from workload requirements before choosing services or architecture patterns.
- Prefer managed primitives for undifferentiated heavy lifting where practical.
- Evaluate every design through security, reliability, performance, and cost trade-offs.

## Architecture / Relationship View

```mermaid
flowchart LR
  Commit[Commit] --> Repo[GitHub]
  Repo --> CI[Build + Test]
  CI --> Artifact[Artifact]
  Artifact --> CD[Deployment Pipeline]
  CD --> Prod[Production]
  Prod --> Feedback[Observability Feedback]
```

## Comparison and Decision Framework

| Strategy | Traffic shift | Rollback speed | Cost overhead |
|---|---|---|---|
| Rolling | Gradual instance replacement | Moderate | Low |
| Blue-Green | Switch between full environments | Very fast | Higher |

## How It Works in Practice

1. Adopt branch + pull-request workflow with review and policy checks.
2. Automate build, unit/integration tests, and quality gates in CI.
3. Publish immutable, versioned artifacts for reproducible releases.
4. Deploy progressively (rolling/blue-green/canary) with health-based promotion.
5. Use production feedback to refine tests, rollback policy, and release cadence.

## Real-World Example

A team enforces pull requests and CI checks, then promotes canary releases based on production metrics before full rollout.

## Common Pitfalls / Exam Traps

- Calling workflow CI/CD while tests remain manual.
- Long-lived branches causing late merge conflicts.
- Deployments without rollback criteria.
- No post-deploy SLO verification.

## Quick Revision Summary

- Define the primary architecture problem solved by this topic.
- Explain one reliability and one security trade-off.
- State one cost optimization opportunity and one risk.
- Describe a production scenario where this design is appropriate.
- Identify a likely misconfiguration and its operational impact.
