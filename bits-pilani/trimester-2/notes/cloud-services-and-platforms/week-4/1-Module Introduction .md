# Module Introduction (Week 4)

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
- Module 4 marks the official transition into **hands-on AWS** — an important step in the cloud learning journey.
- Previous modules focused on cloud concepts, architecture principles, and high-level provider comparison.
- This module starts working with **real cloud foundations**, specifically on AWS.
- Two major focus areas:
  1. **AWS Foundations** — how AWS is structured globally, including regions, availability zones, edge locations, and AWS account setup (recap + deeper coverage).
  2. **Identity and Access Management (IAM)** — controlling **who is allowed to do what** inside an AWS account.

## Terminology and Definitions
- **AWS Foundations**: The structural building blocks of AWS (regions, AZs, edge locations, accounts).
- **Identity and Access Management (IAM)**: AWS service that controls authentication and authorization — who can access AWS and what they can do.
- **Authentication**: Verifying identity.
- **Authorization**: Determining what an authenticated identity can do.

## Detailed Explanations
### Why Start With AWS Foundations
- Without understanding AWS structure, AWS often feels confusing.
- Once the structure is understood, everything else becomes much clearer.
- Structure covers:
  - Regions.
  - Availability zones.
  - Edge locations.
  - AWS account setup.

### Why IAM Is Central
- Every action in AWS (creating servers, deleting data, accessing services) is **controlled by IAM**.
- IAM is one of the **most important services** in AWS.
- Also one of the **most commonly misunderstood**.
- Many real-world cloud security incidents don't happen because AWS itself is insecure — they happen because of **IAM mistakes**.
- That is why IAM is introduced early in the learning path.

### Module Philosophy
- Stay **practical and straightforward**.
- Avoid unnecessary complexity.
- Focus on clarity.
- Prepare learners for **hands-on AWS usage**.

### Expected Outcomes
- Confidence in:
  - How AWS is organized.
  - How access is controlled.
  - Why IAM is central to cloud security.
- Ready to move into the first AWS concepts, starting with AWS global structure.

## Workflows / Process Steps
### Module Flow
1. **AWS Foundations** — global infrastructure: regions, AZs, edge locations, accounts.
2. **AWS Account Structure & Billing** — account boundaries, root user, pay-as-you-go model.
3. **Practical Lab** — AWS account setup.
4. **IAM Users, Groups & Least Privilege**.
5. **IAM Roles & Trust Basics**.
6. **IAM Policies & Evaluation Logic**.
7. **Hands-On**: creating users, groups, roles, MFA, password policies, access keys.
8. **AWS Organizations** for multi-account governance.
9. **Module Summary** recapping foundations and IAM.

## Examples and Use Cases
- Provisioning resources in a region closest to users for performance and compliance.
- Creating AWS accounts for dev, test, and production environments.
- Applying IAM to control both human users and applications.
- Strengthening AWS security by correctly using IAM rather than adding external tools.

## Comparison Tables
### Module 4 Focus Areas
| Focus Area | Purpose |
|---|---|
| AWS Foundations | Understanding how AWS is structured globally |
| Identity and Access Management (IAM) | Controlling who can do what in the AWS account |

### What This Module Is / Is Not
| Approach | This Module |
|---|---|
| Theoretical only | No |
| Practical + theoretical | Yes |
| Overly complex | No |
| Clear and focused | Yes |

## Key Takeaways and Summary
- Module 4 begins official AWS learning with **foundations + IAM**.
- AWS Foundations = **structure** (regions, AZs, edge, accounts).
- IAM = **control** (who can do what).
- IAM is central to AWS security; most incidents trace back to it.
- The module is deliberately **practical, clear, and hands-on**.

## Quick Revision Notes and Memory Aids
- Two focus areas: **Foundations + IAM**.
- IAM question: **Who is allowed to do what in my AWS account?**
- Cloud security truth: **Most incidents = IAM mistakes**, not AWS weakness.
- Mantra: **Understand structure first; everything else follows**.

## Exam Tips and Common Pitfalls
- Don't treat IAM as optional or "only for admins."
- Expect the exam to emphasize IAM's role in security.
- Foundation concepts (regions, AZs, edge) come up again in IAM/security scenarios.
- Module goal is **clarity + hands-on readiness**, not memorization.
