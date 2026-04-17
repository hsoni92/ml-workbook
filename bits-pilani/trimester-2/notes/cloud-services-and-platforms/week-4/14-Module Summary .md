# Module Summary (Week 4)

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
- Module 4 covered **AWS Foundations and IAM**.
- Key areas revisited:
  - AWS **global design** (regions, availability zones, edge locations).
  - AWS **accounts** as security and billing boundaries.
  - **IAM** (users, groups, roles, policies).
  - **Least privilege**.
  - **Trust relationships** for roles.
  - **Policy evaluation** with explicit deny always winning.
  - **AWS Organizations** for multi-account governance.
- Core takeaway: **strong AWS foundations + well-designed IAM = a secure cloud environment**.

## Terminology and Definitions
- **Region**: A geographic area containing multiple availability zones.
- **Availability Zone**: Isolated data center(s) within a region providing fault isolation.
- **Edge Location**: Location used for content delivery and low-latency services.
- **AWS Account**: Security and billing boundary; every account has a root user.
- **Root User**: Account-creation identity with full access — should not be used for daily work.
- **IAM (Identity and Access Management)**: Service controlling who can access what in AWS.
- **IAM User**: Long-lived identity for a person or application.
- **IAM Group**: Collection of users sharing permissions.
- **IAM Role**: Temporary identity assumed by services, applications, or accounts; has no password.
- **Trust Relationship**: Defines who may assume a role.
- **IAM Policy**: JSON document controlling allowed actions on resources.
- **Explicit Deny**: A deny statement that always wins in evaluation.
- **AWS Organizations**: Central multi-account management service.

## Detailed Explanations
### AWS Global Design
- AWS is built globally from:
  - **Regions**.
  - **Availability zones**.
  - **Edge locations**.
- This design provides:
  - **High availability**.
  - **Fault isolation**.
  - **Low latency** for users around the world.

### AWS Accounts
- Each account acts as both a:
  - **Security boundary**.
  - **Billing boundary**.
- Accounts are isolated.
- Every account has a **root user** with full access.
- Best practice:
  - **Avoid using the root user** for daily work.
  - **Protect** the root user carefully.

### IAM as the Core of the Module
- IAM determines:
  - **Who** can access AWS.
  - **What resources** they can use.
  - **What actions** they can perform.

### IAM Users and Groups
- IAM users = individual identities.
- IAM groups simplify permission management as teams grow.
- **Least privilege**: grant only the permissions that are truly required and nothing more.

### IAM Roles (Different from Users)
- Roles:
  - Provide **temporary access**.
  - Do **not** have passwords.
  - Are widely used by AWS services and applications.
- **Trust relationships** define who is allowed to assume these roles — making roles both **powerful and secure**.

### IAM Policies (High-Level)
- AWS evaluates permissions through policies.
- The cardinal rule: **explicit deny always takes priority** over any allow.

### AWS Organizations
- Allows companies to manage **multiple AWS accounts** centrally.
- Central management of:
  - **Billing**.
  - **Governance**.
  - **Security**.
- Important at real-world scale.

## Workflows / Process Steps
### Module 4 Learning Journey
1. Understand AWS global infrastructure (regions, AZs, edge locations).
2. Learn how AWS accounts isolate security and billing.
3. Protect the root user; use non-root IAM users for daily work.
4. Create and manage IAM **users** and **groups**.
5. Apply **least privilege** across all identities.
6. Use **IAM roles** with **trust relationships** for service-to-service access.
7. Understand **IAM policy evaluation** (explicit deny wins).
8. Use **AWS Organizations** to govern multiple accounts centrally.

### What Comes Next
- Module 5 shifts beyond foundations into **hands-on services** and **real-world use cases**.

## Examples and Use Cases
- Using regions and AZs to architect for **high availability** and **low latency**.
- Keeping the **root user** offline for daily operations.
- Creating **groups** like developers, DevOps, DBAs for scalable permission management.
- Attaching **roles** to EC2 instances to access S3 without embedding credentials.
- Using **SCPs** in AWS Organizations to prevent deletion of audit logs.

## Comparison Tables
### Key Module Building Blocks
| Layer | Purpose |
|---|---|
| Regions / AZs / Edge locations | Global reach, resilience, low latency |
| AWS Account | Security + billing boundary |
| Root User | Full access; protected, rarely used |
| IAM Users / Groups | Human and application identities |
| IAM Roles | Temporary, password-less identity for services |
| IAM Policies | Rules for allowed actions |
| AWS Organizations | Multi-account governance |

### Users vs Roles Recap
| Aspect | Users | Roles |
|---|---|---|
| Password | Yes | No |
| Credential lifetime | Long-lived | Temporary |
| Typical use | Humans | Services, apps, cross-account |
| Preferred | For login | For automation and service interaction |

### Policy Evaluation Summary
| Rule | Result |
|---|---|
| No matching allow | Deny (default) |
| Any explicit deny | Deny (wins) |
| Allow without deny | Allow |

## Key Takeaways and Summary
- **Strong AWS foundation + well-designed IAM = secure cloud environment**.
- Global design (regions, AZs, edge locations) delivers **HA, fault isolation, and low latency**.
- Each AWS account is a **security + billing boundary**; protect the root user.
- IAM users and groups enable scalable **least-privilege** access management.
- IAM roles provide **temporary, secure** access without passwords.
- Explicit deny always wins in policy evaluation.
- AWS Organizations enables **multi-account governance** for billing, security, and policy.
- Next: move beyond foundations to **hands-on services** and **real-world use cases**.

## Quick Revision Notes and Memory Aids
- **Global → Account → Root → IAM → Policy → Organizations**.
- **Root user = protect, don't use daily**.
- **Roles = temporary**, **Users = long-lived**.
- **Explicit Deny Always Wins**.
- AWS Organizations = **multi-account HQ**.

## Exam Tips and Common Pitfalls
- Remember: **regions, AZs, and edge locations** are the core of global design.
- Each **account = security + billing boundary** — a very common exam phrasing.
- Do not rely on the root user for operational work.
- Roles and users are **different identity types** — avoid mixing their characteristics.
- **Explicit deny beats any allow** — memorize this phrase.
- AWS Organizations provides **central** control across multiple accounts; it's a **foundational** enterprise service.
