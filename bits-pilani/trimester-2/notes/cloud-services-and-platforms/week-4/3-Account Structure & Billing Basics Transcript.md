# Account Structure and Billing Basics (Week 4)

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
- Three important AWS fundamentals:
  1. **AWS Account**
  2. **Root User**
  3. **Billing Basics**
- AWS uses **accounts as strong boundaries** for **security**, **billing**, and **isolation**.
- The **root user** has full, unrestricted access and must be **protected, not used daily**.
- Billing follows a **pay-as-you-go** model; running resources always cost money, even if unused.

## Terminology and Definitions
- **AWS Account**: The basic container where every AWS resource lives (servers, storage, buckets, databases, users, etc.).
- **Root User**: A special user automatically created when an AWS account is created; has full and unrestricted access.
- **Multi-Factor Authentication (MFA)**: Additional authentication factor beyond a password; used to protect privileged accounts.
- **Pay-As-You-Go**: Billing model where you pay only for what you use.
- **Billing Dashboard**: AWS interface showing usage and charges.
- **IAM User**: Non-root user representing a human or application.
- **Multi-Account Strategy**: Using separate AWS accounts for development, testing, and production environments.

## Detailed Explanations
### AWS Account
- The basic **container** where everything in AWS lives.
- Every server, storage bucket, database, or user created belongs to an AWS account.
- AWS uses accounts as **strong boundaries** for:
  - **Security**.
  - **Billing**.
  - **Isolation**.
- Organizations often use **multiple accounts**:
  - One for **development**.
  - One for **testing**.
  - One for **production** (accessible to customers).
- Separation helps:
  - Limit mistakes.
  - Control access.
  - Track costs clearly.

### Root User
- Automatically created when an AWS account is created.
- Has **full and unrestricted access** to the entire account.
- Can do things no other user can, such as:
  - Closing the account.
  - Changing billing ownership.
  - And more.
- Because of this power, the **root user should never be used for daily work**.
- If root user credentials are compromised, the **entire account is exposed**.
- **Best practice**:
  - Secure the root user with **MFA**.
  - Use it **only for critical account-level tasks**.

### Billing Basics
- AWS follows a **pay-as-you-go** model.
- You pay only for what you use.
- **No upfront commitment** required for most services.
- This makes AWS **flexible** but **easy to misuse** if you're not careful.
- Important to understand for beginners:
  - **Running a resource always costs money**.
  - Even if you're not actively using them, they may still generate charges.
- Best practice:
  - **Check the billing dashboard**.
  - **Clean up unused resources**.

### Office Building Analogy
- **AWS account** = the building.
- **Root user** = the owner.
- **IAM users** = the employees.
- **Billing** = the monthly expense.
- Just as you don't give everyone the building owner's keys, **do not use the root user for daily work**.

## Workflows / Process Steps
### Good Practice After Creating an AWS Account
1. Note and securely store account ID, email, and password.
2. Enable **MFA** on the root user.
3. Create an **IAM user** for daily work (non-root).
4. Use non-root IAM user for day-to-day activities.
5. Separate accounts for development, testing, and production as the org grows.
6. Monitor the **billing dashboard** regularly.
7. Clean up unused resources to avoid unnecessary charges.

## Examples and Use Cases
- Creating **dev, test, and production** AWS accounts for environment isolation.
- Using the **root user only for closing the account or updating billing ownership**.
- Checking the **billing dashboard** periodically to identify unused resources.
- Enabling **MFA** for the root user as the first security measure.

## Comparison Tables
### Boundaries Provided by AWS Accounts
| Boundary | Purpose |
|---|---|
| Security | Isolation of privileges and data |
| Billing | Clear cost tracking per account |
| Isolation | Containment of mistakes and access |

### Root User vs IAM User
| Aspect | Root User | IAM User |
|---|---|---|
| Created automatically | Yes | No, created by admin |
| Access | Full and unrestricted | Permission-based |
| Usage | Critical account tasks only | Daily work |
| Risk if compromised | Entire account exposed | Limited to permissions |

### Office Building Analogy
| AWS Concept | Office Analogy |
|---|---|
| AWS Account | The building |
| Root User | The building owner |
| IAM User | Employees |
| Billing | Monthly expense |

## Key Takeaways and Summary
- An AWS account is the **container and boundary** for security, billing, and isolation.
- Organizations commonly use **multiple accounts** (dev/test/prod) to reduce risk and track costs.
- The **root user is powerful and dangerous** — protect with MFA, use only for critical tasks.
- AWS is **pay-as-you-go**; resources cost money whenever they run.
- Regular **billing reviews and resource cleanup** are essential.

## Quick Revision Notes and Memory Aids
- Accounts provide: **Security, Billing, Isolation**.
- Root user: **Never daily work; MFA always**.
- Billing: **Pay-as-you-go; running = charged**.
- Analogy: **Building / Owner / Employees / Monthly expense**.

## Exam Tips and Common Pitfalls
- Using the root user for daily work is a **security anti-pattern**.
- Idle but running resources still incur charges — common beginner mistake.
- Multi-account strategies are about **isolation and cost control**, not complexity.
- Root user does specific tasks **no IAM user can** — be able to name an example (e.g., closing the account).
