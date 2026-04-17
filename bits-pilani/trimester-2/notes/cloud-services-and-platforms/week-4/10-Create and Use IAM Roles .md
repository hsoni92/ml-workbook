# Create and Use IAM Roles (Week 4)

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
- **Users are for humans; roles are for AWS services**.
- Roles act like a **pass** at an event: different passes grant different privileges (e.g., VIP vs guest), and the "security guards" (AWS) decide what each pass can do.
- Roles enable **service-to-service interaction** within the **same account** or **across multiple accounts**.
- Roles are just **another type of identity** — but one that is **assumed temporarily**.

## Terminology and Definitions
- **Role**: An identity that AWS services or other accounts can **assume** to gain temporary permissions.
- **Trust Entity**: The type of principal allowed to assume the role (AWS service, AWS account, etc.).
- **Permission Policy**: Determines what actions the role is allowed to perform once assumed.
- **JSON Policy**: The JSON document representation of the permissions assigned to a role.
- **Read-Only Access**: Managed permission that only allows read operations on a service.
- **EC2**: Amazon's compute service.
- **S3**: Amazon's object storage service.
- **Aurora / RDS**: AWS database services used in the role-interaction examples.

## Detailed Explanations
### Users vs Roles (Restated)
- **Users**: humans who log in to the console and use services.
- **Roles**: identities for **services** — enable one service to interact with another.
- Example: if a compute service needs to interact with a database service, a **role** is created to allow that interaction.

### Role = Identity for Service-to-Service Communication
- A role is just another identity that lets two services interact.
- The two services can be:
  - **In the same AWS account**.
  - **Across different AWS accounts** (e.g., your account + another team's/company's account).

### Role Creation Options
- When creating a role, you select a **trusted entity type**:
  - **AWS service** (default, used for most common service-to-service setups).
  - **AWS account** (for cross-account roles):
    - Can enable **multi-factor authentication** for cross-account assumption.
  - Other options exist for advanced scenarios.
- Common choice: **AWS service**.

### Choosing the Service for the Role
- After selecting "AWS service," pick the specific service the role applies to:
  - Compute (EC2), storage, database, monitoring — nearly any AWS service is available.
- Typical prompt for EC2: *"allow EC2 to call AWS services on your behalf"*.
- This means EC2 can assume the role and act with its permissions.

### Attaching Permissions to the Role
- After choosing the service, assign one or more **permission policies** describing what actions the role allows.
- Example: attach **read-only access** so EC2 can only read, not modify or delete.
- Multiple policies can be attached; permissions are cumulative (subject to IAM evaluation logic).

### Naming and Reviewing
- Give a meaningful **name**, e.g., `EC2-readonly-role`.
- Provide an optional **description** so newcomers understand what the role does.
- AWS shows the resulting policy in **JSON format** automatically — no need to hand-write JSON.
- Click **Create role**.

### Cross-Account Role Usage (Why It Matters)
- Companies rarely run everything from a single account.
- They maintain multiple accounts within one cloud or across multiple clouds.
- Roles are the **foundation** for cross-account authentication:
  - Provide a secure, standardized way for services to interact.
  - Keep applications running across account boundaries without sharing long-lived credentials.

## Workflows / Process Steps
### Create an EC2 Read-Only Role
1. Open IAM → **Roles → Create role**.
2. Select **Trusted entity type → AWS service**.
3. Pick the service → **EC2**.
4. Keep the default use case ("EC2 calls AWS services on your behalf").
5. Click **Next**.
6. Attach a permission policy → choose **read-only** permissions for EC2.
7. Click **Next**.
8. Name the role (e.g., `EC2-readonly-role`) and add a description.
9. Review the JSON policy (auto-generated).
10. Click **Create role**.

### Using the Role
1. Attach the role to the service (e.g., launch or modify an EC2 instance to use this role).
2. The service assumes the role automatically and obtains temporary credentials.
3. The service can now act within the granted permission scope (read-only in this example).

## Examples and Use Cases
- **EC2 read-only**: EC2 instance interacts with AWS services in a read-only capacity.
- A compute service interacting with **Amazon Aurora or RDS** using a role.
- **Cross-account**: a service in Account A assuming a role in Account B to operate resources there.
- Cross-cloud orchestration scenarios where roles are central to service identity.

## Comparison Tables
### Users vs Roles (at a Glance)
| Aspect | Users | Roles |
|---|---|---|
| Meant for | Humans (console) | AWS services / applications |
| Credentials | Username + password + optional keys | Temporary credentials via assumption |
| Lifetime | Long-lived | Short-lived (auto-renewed) |
| Typical use | Login and perform actions | Service-to-service communication |

### Pass Analogy
| Pass Type | Access Level |
|---|---|
| VIP Pass | Extra privileges |
| Guest Pass | Seated audience / basic access |
| Role | AWS service "pass" with specific privileges |

### Role Trusted Entity Choices
| Option | When to Use |
|---|---|
| AWS service | Most service-to-service setups |
| AWS account | Cross-account access, optionally with MFA |
| Other | Advanced / federation use cases |

## Key Takeaways and Summary
- **Users = humans, Roles = services**.
- Roles allow services to communicate securely **without long-lived credentials**.
- Cross-account interactions are made safe and auditable via roles.
- Role creation is a simple 3-step flow: pick **trusted entity**, pick **service**, attach **permissions**.
- AWS auto-generates the JSON policy behind the scenes.
- Providing descriptive role names and descriptions improves team hand-offs.

## Quick Revision Notes and Memory Aids
- **Users = humans, Roles = services**.
- Steps: **Service → Permissions → Name → Create**.
- Analogy: **roles are VIP / Guest passes** the AWS security lets services wear.
- Cross-account: use **AWS account** trust type, optionally with **MFA**.

## Exam Tips and Common Pitfalls
- Roles do **not** have usernames or passwords.
- Attaching an IAM **user's access keys** to an EC2 instance is an anti-pattern — use a **role** instead.
- Always apply **least privilege** even when creating roles (read-only when possible).
- JSON view is informational — don't be intimidated; you can create roles entirely through the console.
- Remember cross-account roles allow safe **multi-account** operations — a very common real-world pattern.
