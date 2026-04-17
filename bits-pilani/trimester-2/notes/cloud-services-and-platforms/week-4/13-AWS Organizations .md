# AWS Organizations (Week 4)

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
- **AWS Organizations** is how real companies manage AWS at **large scale**.
- Running everything in a single account is risky, messy, and hard to control.
- AWS Organizations allows **central management of multiple accounts**.
- Core building blocks:
  - **Management account**.
  - **Member accounts**.
  - **Organizational Units (OUs)**.
  - **Service Control Policies (SCPs)**.
  - **Consolidated billing**.
- Analogy: like a **company headquarters** that sets rules and budgets while departments work independently.
- Almost every production environment — including inside Amazon — uses AWS Organizations.

## Terminology and Definitions
- **AWS Organization**: Central framework to manage multiple AWS accounts.
- **Management Account**: The single control-plane account for billing, governance, and policies; **should never run workloads**.
- **Member Account**: A regular AWS account managed by the organization (used by teams or environments).
- **Organizational Unit (OU)**: A **logical grouping** of accounts within the organization.
- **Service Control Policy (SCP)**: Organization-level **guardrails** that limit the maximum permissions available to member accounts.
- **Consolidated Billing**: Single bill covering all accounts within the organization.
- **Governance**: Centralized control of security, compliance, and operational policies.

## Detailed Explanations
### Why Organizations Exist
- Companies don't run everything in a single AWS account because:
  - It becomes risky.
  - Easily becomes messy.
  - Hard to control at scale.
- AWS Organizations provides:
  - Central place to manage **security rules**, **billing settings**, and **restrictions**.
  - Single pane of control rather than configuring each account individually.

### Management Account
- The **control center** of the organization.
- Manages:
  - **Billing**.
  - **Governance**.
  - **Policies**.
- Rule: it **should never be used for running applications**.
- Keeping it free of workloads protects the organization's control plane.

### Member Accounts
- Regular AWS accounts used by teams or environments:
  - Development.
  - Testing.
  - Production.
- These accounts host real workloads.
- Centralized management but operational autonomy.

### Organizational Units (OUs)
- Logical groupings of accounts inside the organization.
- Help organize accounts by purpose, function, or team.
- Examples:
  - All **engineering** accounts under one OU.
  - All **security-related** accounts under another OU.

### Service Control Policies (SCPs)
- One of the most powerful AWS Organizations features.
- Act as **guardrails**.
- Key point: **SCPs do NOT grant permissions**.
- Instead, they **limit** what member accounts can do — **even if IAM permits it**.
- Examples:
  - Prevent anyone from **deleting audit logs**.
  - Restrict usage to specific **regions**.
  - Block certain **risky admin actions**.

### Consolidated Billing
- AWS Organizations produces **one bill for all accounts**.
- Makes billing centralized and easier to track.
- Also enables opportunities like aggregated volume discounts.

### The Headquarters Analogy
- Organization = **company headquarters**:
  - Sets rules.
  - Sets budgets.
- Departments (member accounts) **work independently** within those rules.

## Workflows / Process Steps
### Organizing a Company's AWS Footprint
1. Create a **management account** used only for governance.
2. Create **member accounts** for teams or environments (dev, test, prod).
3. Group accounts into **OUs** (e.g., engineering OU, security OU).
4. Attach **SCPs** to OUs to enforce guardrails.
5. Use **consolidated billing** for unified invoicing.
6. Manage applications within member accounts; never on the management account.

### Applying a Guardrail (Example Flow)
1. Identify an action that must be prevented (e.g., deleting audit logs).
2. Define an SCP with an explicit deny for that action.
3. Attach the SCP to the relevant OU or account.
4. Member accounts are now **unable** to perform the restricted action, regardless of IAM policies.

## Examples and Use Cases
- A company separating **engineering** and **security** accounts under distinct OUs.
- Restricting AWS usage to **approved regions** via an SCP.
- Preventing deletion of CloudTrail logs across all accounts.
- Generating **one consolidated bill** for every account in the organization.
- Amazon itself, and nearly every production environment, uses AWS Organizations.

## Comparison Tables
### Management Account vs Member Account
| Aspect | Management Account | Member Account |
|---|---|---|
| Purpose | Governance, billing, policy | Running workloads |
| Hosts applications? | No | Yes |
| Manages other accounts? | Yes | No |
| Count per organization | One | Many |

### IAM Permissions vs SCP Guardrails
| Aspect | IAM Permissions | SCPs |
|---|---|---|
| Grants permissions? | Yes | **No** |
| Limits permissions? | Through explicit deny | Always — as guardrails |
| Scope | Per account | Across OUs / accounts |

### Benefits of AWS Organizations
| Benefit | Description |
|---|---|
| Central governance | One place to set security + policy rules |
| Organizational Units | Logical account groupings |
| SCPs | Account-wide guardrails |
| Consolidated billing | Single bill for all accounts |
| Scale | Supports large, real-world enterprise usage |

## Key Takeaways and Summary
- AWS Organizations = **multi-account central management**.
- The **management account** controls policies, billing, governance — **no workloads**.
- **Member accounts** run the actual workloads.
- **OUs** group accounts logically for applying policies.
- **SCPs** are guardrails that **limit** (but never grant) what member accounts can do.
- **Consolidated billing** unifies invoicing across all accounts.
- It's a **foundational service** for security, governance, and scale in real production environments.

## Quick Revision Notes and Memory Aids
- **Management = HQ**, **Members = departments**.
- **OUs = folders for accounts**.
- **SCPs = guardrails**, not permission grants.
- **Consolidated billing = one bill**.
- Rule: management account never runs apps.

## Exam Tips and Common Pitfalls
- Do not say SCPs "grant" permissions — they only **limit** them.
- Do not run workloads on the **management account**.
- SCPs apply regardless of IAM policies — they can **override IAM allows**.
- Remember: **explicit deny beats allow** applies to SCPs too.
- OUs are **logical**, not physical — they're groupings of accounts, not separate infrastructure.
