# IAM Auditing with CloudTrail (Week 4)

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
- **CloudTrail** is used purely for **auditing** AWS account activity.
- It records **who performed what action, when, and on which resource**.
- Every event inside the AWS account — user creation, policy creation, password changes, role creation — is captured.
- Heavily used by teams and leadership to track unusual activity on the console.

## Terminology and Definitions
- **CloudTrail**: AWS service that records account-level activity for auditing.
- **Event History**: The CloudTrail view showing a time-ordered list of recorded events.
- **Auditing**: Examining records of system activity to detect anomalies, compliance issues, or unauthorized behaviour.
- **Event**: A single recorded activity (e.g., creating a role, changing a password).

## Detailed Explanations
### Purpose of CloudTrail
- Pure **auditing** purpose.
- Tracks:
  - What activities happened.
  - Who performed them.
  - When they were performed.
- Enables proper governance over the AWS account.

### What Gets Recorded
- Every little event performed inside the account is captured:
  - Account creation.
  - Policy creation.
  - Role creation.
  - User creation.
  - Group creation and group membership changes.
  - Password changes.
- Essentially, the audit trail captures the lifecycle of identity, permission, and operational activity.

### Accessing CloudTrail Event History
- Open **CloudTrail**.
- Click the **hamburger button** at the top left of the CloudTrail console.
- Select **Event history** — this is where the recorded history loads.
- You can browse through all the events.
- Example shown: the **EC2 read-only role** created in a previous demonstration appears in the event history.

### Managing Events
- CloudTrail supports:
  - **Filtering** events using multiple criteria (action, identity, resource, etc.).
  - **Deleting** specific events (with appropriate permissions).
  - **Restoring** events under certain conditions.
- These management capabilities help teams maintain clean, targeted audit views.

### Why Teams Use CloudTrail
- Management and leadership rely on it:
  - Track **unusual activity** on the console.
  - Investigate security incidents.
  - Support compliance requirements.
- Useful for **any team** that needs visibility into the account's activity.

## Workflows / Process Steps
### Review Activity in CloudTrail
1. Open **CloudTrail**.
2. Click the **hamburger** (top-left).
3. Click **Event history**.
4. Browse or filter events by action, identity, or time range.
5. Click on an event to see its details (user, time, resource, etc.).

### Investigate a Specific Action
1. In Event history, filter by event name or by the affected resource.
2. Inspect the detailed record to identify the actor and timestamp.
3. Use the information to verify legitimacy or to escalate.

## Examples and Use Cases
- Tracking every IAM user, group, role, and policy creation performed during a hands-on lab.
- Leadership reviewing activity to detect suspicious actions.
- Compliance teams reviewing audit trails to meet policy obligations.
- Debugging a permission misconfiguration by looking at who changed what and when.

## Comparison Tables
### CloudTrail Capabilities
| Capability | Description |
|---|---|
| Event history | Browsable log of account-level events |
| Filtering | Narrow by action, identity, resource, time |
| Event management | Delete and restore events (per permissions) |
| Auditability | Answers who/what/when questions |

### Who Uses CloudTrail
| Audience | Purpose |
|---|---|
| Teams | Track routine activities and changes |
| Management / Leadership | Investigate unusual activity |
| Compliance teams | Satisfy audit requirements |
| Individuals | Review personal activity in lab/learning |

## Key Takeaways and Summary
- CloudTrail = **auditing** for AWS.
- Captures every event: **who did what, when**.
- Event history is accessed via **CloudTrail → hamburger → Event history**.
- Supports **filtering**, **deleting**, and **restoring** events.
- Widely used by teams and management to track unusual activity and support compliance.

## Quick Revision Notes and Memory Aids
- CloudTrail = **trail of activities**.
- Key view = **Event history**.
- Answers: **who, what, when**.
- Three actions on events: **filter, delete, restore**.

## Exam Tips and Common Pitfalls
- CloudTrail is for **auditing**, not for real-time performance monitoring (that is CloudWatch).
- Event history is the **starting point** — remember its name.
- Don't confuse CloudTrail with CloudWatch — different purposes.
- Events can be **filtered** and **managed**; full deletion rights require appropriate permissions.
