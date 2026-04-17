# IAM Roles and Trust Basics (Week 4)

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
- **IAM roles** are one of the most important and widely used security concepts in AWS.
- A role is **not a user** — no username, no password, no permanent access keys.
- A role is a **temporary identity** that can be **assumed** when needed.
- Roles allow an application or an AWS service to **temporarily act with certain permissions**.
- Every IAM role has **two sides**:
  - **Permission policy** — defines *what* actions are allowed.
  - **Trust policy** (trust relationship) — defines *who* can assume the role.

## Terminology and Definitions
- **IAM Role**: A temporary identity that can be assumed by users, AWS services, or external identities.
- **Assume a Role**: To temporarily adopt the role's permissions; AWS issues short-lived credentials.
- **Temporary Credentials**: Credentials with a limited lifetime; automatically managed and renewed by AWS.
- **Trust Relationship / Trust Policy**: Defines which identities are allowed to assume a role.
- **Permission Policy**: Defines which AWS actions and resources the role is allowed to access.
- **External Identity System**: An identity provider outside AWS (e.g., federated identity, third-party).

## Detailed Explanations
### Why IAM Roles Exist
- Earlier, applications stored AWS access keys directly inside servers or code.
- This led to serious security problems:
  - Keys could be deleted, reused incorrectly, or leaked.
- IAM roles solve this:
  - Provide **temporary credentials** automatically managed by AWS.
  - **No secrets** are stored.
  - Credentials **expire** automatically and are **renewed** automatically.
- Roles are the **preferred way to grant access** in AWS.

### Roles vs Users
- Roles do **not** have:
  - A username.
  - A password.
  - Permanent access keys.
- Instead, a role is a **temporary identity** assumed when needed.

### Trust Relationships
- Permissions alone are **not enough** — roles also need trust.
- Two-sided model:
  - **Permission policy**: defines *what* the role can do (e.g., read from storage, write to a database).
  - **Trust policy**: defines *who* can step into the role.
- Without a trust relationship, a role **cannot be used even if it has permissions**.
- Memorable phrase:
  - **Trust policy** decides **who can enter**.
  - **Permission policy** decides **what they can do once inside**.

### Who Can Be Trusted
- Roles can trust:
  - AWS services (e.g., EC2, Lambda).
  - Other AWS accounts.
  - External identity systems.

### Why Roles Are Preferred
- More **secure** — no long-lived secrets.
- More **flexible** — can be assumed by many entity types.
- Better for **automation** — applications obtain credentials on demand.

## Workflows / Process Steps
### Using an IAM Role
1. Create a role and attach a **permission policy** describing allowed actions/resources.
2. Define a **trust policy** specifying who can assume the role.
3. The trusted entity (service, account, or user) **assumes** the role.
4. AWS returns **temporary credentials** to the entity.
5. The entity uses those credentials to perform allowed actions.
6. Credentials expire automatically; AWS renews them as needed.

### EC2 Accessing S3 (Canonical Example)
1. An EC2 instance needs to access an S3 bucket.
2. Instead of embedding an IAM user's keys into the instance, create a role with S3 permissions.
3. Attach the role to the EC2 instance.
4. EC2 assumes the role and receives temporary credentials.
5. EC2 calls the S3 API using those credentials.

## Examples and Use Cases
- EC2 instance reading from an S3 bucket via an attached role.
- Lambda function writing to a database through an assumed role.
- Cross-account access: a service in Account A assumes a role in Account B.
- Federated users from an external identity system assuming AWS roles.

## Comparison Tables
### IAM User vs IAM Role
| Aspect | IAM User | IAM Role |
|---|---|---|
| Username / Password | Yes | No |
| Permanent access keys | Possible | No |
| Credentials type | Long-lived | Temporary (auto-renewed) |
| Who uses it | Humans or applications | Services, applications, accounts, external IDs |
| Preferred for automation | No | Yes |
| Secrets stored in code | Risk exists | Not needed |

### Two Sides of a Role
| Policy Type | Question it Answers | Role |
|---|---|---|
| Trust Policy | Who can assume this role? | Gatekeeper |
| Permission Policy | What can it do once inside? | Authorization |

## Key Takeaways and Summary
- IAM roles = **temporary identities** assumed by services, accounts, or external identities.
- AWS created roles to remove the need for **hard-coded access keys** in code.
- **Temporary credentials** are automatically managed and renewed.
- Every role has **two policies**: **trust** (who) and **permission** (what).
- Without a trust policy, a role **cannot be used**, even with permissions.
- Roles are the **preferred and most secure** way to grant access in AWS.

## Quick Revision Notes and Memory Aids
- **Role = temporary identity, no password**.
- **Trust = who**; **Permission = what**.
- **No keys in code** — use roles instead.
- Use roles for: **EC2 → S3**, **Lambda → DB**, **Account A → Account B**.

## Exam Tips and Common Pitfalls
- Do not confuse roles with users — roles have **no credentials of their own**.
- Both trust **and** permission policies are required for a role to be usable.
- Roles issue **short-lived credentials**, not permanent keys.
- Explicit trust is **mandatory** — implicit trust does not exist.
- Remember: **trust policy gates entry**; **permission policy gates actions**.
