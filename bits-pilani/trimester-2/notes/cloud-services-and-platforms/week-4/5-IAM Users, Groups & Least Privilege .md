# IAM Users, Groups and Least Privilege (Week 4)

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
- AWS controls access using **IAM users**, **IAM groups**, and the **principle of least privilege**.
- IAM is central to AWS security — **every security issue in AWS eventually ties back to IAM**.
- **IAM** = **Identity and Access Management**: decides **who** can access AWS and **what** they can do.
- Analogy: IAM acts like **access control in an office building** — not everyone should enter every room or hold the master keys.
- **Groups** simplify permission management by attaching permissions once and adding users into the group.

## Terminology and Definitions
- **IAM (Identity and Access Management)**: AWS service that controls authentication and authorization.
- **IAM User**: A single identity (usually a person, sometimes an application) with login credentials and optionally access keys.
- **IAM Group**: A collection of users to which permissions are attached for easier management.
- **Access Keys**: Credentials used for programmatic access (API-based calls) to AWS.
- **Least Privilege**: Granting only the permissions an identity needs to do its job, and nothing more.
- **Programmatic Access**: Interacting with AWS via APIs instead of the console.

## Detailed Explanations
### What IAM Does
- IAM's job is simple: **decide who can access AWS and what they can do**.
- Every request to AWS is evaluated by IAM.
- IAM provides the foundation for **authentication** (who) and **authorization** (what).

### IAM Users
- An IAM user represents a **single identity**:
  - Usually a person.
  - Sometimes an application.
- Each user can have:
  - **Login credentials** for console access.
  - **Access keys** for programmatic API-based access.
- Access keys are required because **all AWS services can be accessed via API**.
- Best practice: **One IAM user = one real identity**.
- Sharing users across a team is **risky** and should be avoided.

### IAM Groups
- An IAM group is simply a **collection of users**.
- Purpose: **make permission management easier**.
- Instead of assigning permissions user-by-user:
  1. Attach permissions to a group.
  2. Add users to that group.
- Users in a group automatically inherit the group's permissions.

### Principle of Least Privilege
- Grant only the **minimum required permissions** for an identity to do its task.
- Restrict further beyond the minimum if possible.
- Reduces blast radius of compromised credentials.
- A core AWS security-first philosophy.

## Workflows / Process Steps
### Granting Access with IAM (Best Practice Flow)
1. Create an IAM user for each person or application.
2. Group users by role or function (e.g., developers, DBAs).
3. Attach permissions to groups, not individuals.
4. Assign users to the appropriate groups.
5. Apply least privilege — start with minimal permissions, expand only when needed.

## Examples and Use Cases
- **Office analogy**:
  - Not everyone needs master keys.
  - Rooms (AWS resources) require specific access based on role.
- **Team structure**:
  - Developers → "developers" group.
  - Database administrators → "dba" group with restricted (often read-only) permissions.
  - DevOps engineers → "devops" group with broader admin-level access.
- An application performing programmatic actions would use access keys (or, more safely, a role — covered later).

## Comparison Tables
### IAM Users vs IAM Groups
| Aspect | IAM User | IAM Group |
|---|---|---|
| Purpose | Represents a single identity | Represents a collection of users |
| Credentials | Login + optional access keys | None of its own |
| Permission Assignment | Directly (not recommended) or via group | Permissions attached once for all members |
| Scaling | Hard to manage at scale | Simpler at scale |

### Permission Assignment Strategies
| Strategy | Description | Recommended? |
|---|---|---|
| Attach permission to user directly | One-off permissions | Discouraged for teams |
| Attach permission to a group | Permission inherited by all members | Recommended |
| Share a user between team members | Loses individual accountability | Avoid |

## Key Takeaways and Summary
- IAM controls **who** accesses AWS and **what** they can do.
- **IAM users** represent **individual identities**; **one user = one person**.
- **Access keys** enable programmatic access to AWS APIs.
- **IAM groups** simplify permissions management by allowing permission assignment at the group level.
- **Least privilege** is the foundational principle — only give what is necessary.
- Sharing users among team members is risky and should not be done.

## Quick Revision Notes and Memory Aids
- **IAM = Identity + Access Management**.
- **User = person**; **Group = bucket of users**.
- **Access keys** = for **API/programmatic** access.
- Rule: **One user per real identity**.
- Principle: **Least Privilege** = only what's needed, nothing more.

## Exam Tips and Common Pitfalls
- Do not attach permissions to users individually when groups exist.
- Access keys are for **programmatic** access, not console login.
- Sharing an IAM user across a team is an anti-pattern.
- IAM is the root cause of most AWS security incidents — remember this framing on exam questions.
- IAM itself is **global**; user and group scope is not region-specific.
