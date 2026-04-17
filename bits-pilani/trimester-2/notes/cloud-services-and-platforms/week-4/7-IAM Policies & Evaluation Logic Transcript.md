# IAM Policies and Evaluation Logic (Week 4)

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
- **IAM policies** are the rules that decide what is allowed and what is not allowed in AWS.
- Whenever anyone performs an AWS action (create, access, delete, etc.), AWS **checks policies first**.
- **Identities** (users, groups, roles) are *who*; **policies** define *what they can do*.
- AWS follows a **security-first model**: **deny by default**.
- Fundamental rule: **An explicit deny always wins** over any allow.

## Terminology and Definitions
- **IAM Policy**: A document describing who can do what on which resource and under what conditions.
- **Statement**: The building block of a policy.
- **Effect**: Either **Allow** or **Deny**.
- **Action**: The AWS operation (e.g., `s3:GetObject`).
- **Resource**: The AWS entity the action applies to (e.g., an S3 bucket).
- **Condition**: Optional constraint controlling when a statement applies.
- **Explicit Deny**: A policy statement with effect Deny that always wins.
- **Explicit Allow**: A statement that grants permission; required for any action to succeed.
- **Deny by Default**: If nothing explicitly allows an action, it is denied.
- **JSON**: The format used to write IAM policies.

## Detailed Explanations
### What an IAM Policy Is
- A **document** that tells AWS:
  - Who can do what.
  - On which resource.
  - Under what conditions.
- Written in **JSON**.
- Each policy contains **statements**; every statement has:
  - **Effect** (Allow / Deny).
  - **Action**.
  - **Resource**.
  - Optionally, **Conditions**.
- Policies grant the permissions that identities (users, groups, roles) use.
- Without policies, identities can do nothing.

### Why IAM Policies Matter
- AWS is **security-first**: nothing is allowed unless explicitly permitted.
- Policies help:
  - Enforce **least privilege**.
  - Reduce security risk.
  - Make access **predictable and auditable**.

### Allow vs Deny
- AWS works on a **deny-by-default** principle.
- If there is no explicit allow → **access is denied**.
- Most important rule: **An explicit deny always wins**.
  - Even if multiple policies allow something, a single deny blocks the entire action.

### How AWS Evaluates a Request
- Simple evaluation logic:
  1. Look for an **explicit deny**.
     - If found → **reject** the request immediately.
  2. If no deny, look for an **explicit allow**.
     - If found → **allow** the request.
  3. If nothing matches → **deny by default**.

### Office Building Analogy
- All doors are **locked by default**.
- Only the rooms you've been explicitly given access to can be entered.
- Security can always **override permissions** — the deny "master switch."

## Workflows / Process Steps
### Policy Evaluation Flow
1. Request arrives at AWS.
2. AWS collects all applicable policies for the identity and resource.
3. Is there an explicit deny? → If yes, request is rejected.
4. Is there an explicit allow? → If yes, request is allowed.
5. Otherwise → request is denied by default.

### Visualizing the Evaluation
```
Request ──► Explicit Deny?  ── yes ──► DENY
                │no
                ▼
            Explicit Allow? ── yes ──► ALLOW
                │no
                ▼
           DENY (by default)
```

## Examples and Use Cases
- **Read-only developer on S3**:
  - Policy allows read actions; does not allow delete.
  - Reading works.
  - Deleting fails automatically.
- Administrator has broad Allow, but a specific Deny blocks delete actions on audit logs — the Deny wins even for admins.
- Missing policy → identity can do nothing at all (even if it exists in IAM).

## Comparison Tables
### Allow vs Deny
| Effect | Behaviour |
|---|---|
| Allow | Grants permission when no Deny overrides it |
| Deny | Always wins; blocks the action even if Allows exist |
| (none) | Implicit deny — request rejected |

### Policy Components
| Component | Purpose |
|---|---|
| Effect | Decides Allow or Deny |
| Action | What operation is targeted |
| Resource | Which entity the action applies to |
| Condition | When the statement applies (optional) |

## Key Takeaways and Summary
- IAM policies are the rules AWS consults on every action.
- Identities (users, groups, roles) need **policies** to actually do anything.
- AWS evaluation is **deny-first**, then **allow**, otherwise **deny**.
- **Explicit Deny always wins** — the most important rule.
- Policies are written in **JSON**; understand structure (effect, action, resource, condition) rather than memorizing syntax.
- Policies enforce **least privilege** and keep access **auditable**.

## Quick Revision Notes and Memory Aids
- AWS default = **DENY**.
- Evaluation order: **DENY → ALLOW → DEFAULT DENY**.
- Statement = **Effect + Action + Resource (+ Condition)**.
- **Deny beats Allow. Always.**
- Office analogy: **doors locked by default, security can always override.**

## Exam Tips and Common Pitfalls
- If asked "what happens when one policy allows and another denies?" → **Deny wins**.
- If no matching statement exists, the result is **deny**, not allow.
- Do not memorize the JSON syntax — focus on **evaluation logic**.
- Policies alone do nothing without being **attached** to an identity.
- "Security-first" = explicit allow required; implicit denial is the default posture.
