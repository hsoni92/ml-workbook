# Create IAM Users and Groups (Week 4)

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
- Hands-on lab covering creation of **IAM users**, **IAM groups**, attaching **policies**, and logging in as a non-root user.
- In AWS, permissions are **never given directly to people** — identities, permissions, and access control are designed carefully.
- IAM is a **global service** — users, groups, roles, and policies apply across **all regions**, not tied to one region or AZ.
- Many services are cheaper in **US East 1 (Virginia)**, the first AWS data center region.
- Best practice: never access AWS from the **root user** for daily work. Create a personal **non-root user** and log in with that.

## Terminology and Definitions
- **IAM User**: Identity representing a person or an application.
- **IAM Group**: Collection of users sharing permissions.
- **Policy**: JSON document assigning permissions.
- **Auto-generated Password**: Random complex password produced by AWS at user creation.
- **Administrator Access**: AWS managed policy granting broad admin-level permissions.
- **Read-Only Access**: AWS managed policy granting only read permissions.
- **Region**: Geographic area with multiple AZs (17 regions mentioned, more planned).
- **Availability Zone (AZ)**: Logically isolated data centers inside a region (examples: Mumbai, Singapore, Seoul, Sydney, Tokyo in Asia Pacific; Frankfurt, Ireland, London, Paris in Europe).
- **Non-root User**: Any IAM user other than the account's root user.

## Detailed Explanations
### IAM Is a Global Service
- Applied across **all regions** — not region- or AZ-specific.
- Regions host **availability zones** (example mappings):
  - United States: 4 AZs.
  - Asia Pacific: Mumbai, Singapore, Seoul, Sydney, Tokyo.
  - Europe: Frankfurt, Ireland, London, Paris.
- Billing tip: many services are **cheaper in US East 1 (Virginia)** because it was the first AWS region; many projects use it for cost efficiency.

### Root vs Non-Root Users
- The root user (the email/password used during account creation) has **full permissions**.
- Best practice: do **not** use the root user for daily work.
- Create your **own personal non-root user** within your account and log in with it.
- In the lab environment, the instructor's logged-in account is **not the root** — it's a user managed by the BITS team's root account.

### Creating a New IAM User
- Navigate to **IAM → Users → Create user**.
- Provide a **meaningful username**:
  - Example: `non-root-user-1` or any recognizable, non-admin-sounding name.
- Check the box to allow **console access**.
- Password options:
  - Prefer **auto-generated password** (AWS produces a random pattern mixing lowercase, uppercase, symbols, numbers).
  - Recommended: enable **"user must create a new password at next sign in"**.
  - This is important because the auto-generated password is hard to remember and should only be used once; the user will reset it on first login.

### Setting Permissions During User Creation
- On the permissions screen, three options are available:
  1. **Add user to a group**.
  2. **Copy permissions** from another user.
  3. **Attach policies directly**.
- If no groups exist yet, use **attach policies directly**.
- For a personal user:
  - Choose **Administrator Access** to perform any action inside your own account (appropriate for personal learning).
- Click **Next**, review, and **Create user**.

### Reviewing the Created User
- AWS presents:
  - A console sign-in **URL**.
  - The **username**.
  - The **password** (displayed once; can be downloaded as a file or screenshot).
- Also requires the **account number** when signing in as a non-root user:
  - Non-root sign-in uses **Account ID + Username + Password** (not email).
- Password displayed is only useful **first time** — user will reset on first login.

### IAM Groups
- Purpose: provide a **shared set of permissions** to multiple users.
- Teams commonly have distinct permission needs:
  - Developers → admin access.
  - DevOps / Cloud engineers → admin access.
  - Database administrators → read-only access.
- Create multiple groups, each with its own permission set.

### Creating a Group (Example: cloud admins)
- Name the group (e.g., `cloud admins`).
- Optionally add existing users during creation (e.g., `non-root-user`).
- Choose permissions:
  - `AdministratorAccess` for full admin across all services.
  - Expanding this policy shows every service it covers (e.g., Amplify, Elastic Beanstalk, and many others).
- Click **Create user group**.
- Every user added to the group inherits these permissions.

### Attaching Additional Policies to a Group
- Add more policies at any time via **Attach policies**.
- Example: attach **RDS read-only** to admins so they cannot delete or modify relational databases.
- This lets you maintain broad admin capability while restricting sensitive operations.

### Logging In as the New User
- Use the sign-in URL + username + password (not email).
- On first login, the user is redirected to **change the password**.

## Workflows / Process Steps
### Create a Non-Root User
1. Sign in to AWS and open **IAM**.
2. Go to **Users → Create user**.
3. Enter a meaningful username (avoid admin-sounding names).
4. Enable console access.
5. Select **auto-generated password**.
6. Check **"user must create a new password at next sign in"**.
7. Click **Next**.
8. Attach policies directly (e.g., `AdministratorAccess` for personal use).
9. Review and click **Create user**.
10. Save the sign-in URL, username, and password (download or screenshot).

### Create an IAM Group
1. Go to **IAM → User groups → Create group**.
2. Give the group a meaningful name (e.g., `cloud admins`).
3. Optionally add users to the group.
4. Choose a permission set (e.g., `AdministratorAccess`).
5. Click **Create user group**.
6. Optionally attach additional policies (e.g., `AmazonRDSReadOnlyAccess`).

### First Login as Non-Root User
1. Open the sign-in URL.
2. Enter **Account ID**, **Username**, **Password**.
3. When prompted, reset the password to a memorable one.

## Examples and Use Cases
- Creating a personal, non-root IAM user to practice AWS safely.
- A `cloud admins` group receiving `AdministratorAccess` plus `AmazonRDSReadOnlyAccess` to safely prevent accidental DB modifications.
- Separating permissions per role: developers, DBAs (read-only), DevOps.
- Distributing admin permissions centrally through groups so new team members inherit them.

## Comparison Tables
### Root User vs Non-Root (IAM) User
| Aspect | Root User | Non-Root User |
|---|---|---|
| Sign-in Credentials | Email + password | Account ID + username + password |
| Permissions | Full, unrestricted | Only what's granted via IAM |
| Recommended for daily use | No | Yes |
| Can be deleted | No | Yes |

### Permission Assignment During User Creation
| Option | Description |
|---|---|
| Add user to a group | Inherits permissions from the group |
| Copy permissions | Clones permissions from an existing user |
| Attach policies directly | Assigns specific policies straight to the user |

### Role-Based Group Permissions
| Team | Typical Group Permission |
|---|---|
| Developers | Administrator-level (as appropriate) |
| DevOps / Cloud engineers | Administrator access |
| Database Administrators | Read-only on certain DB services |

## Key Takeaways and Summary
- Always create and use a **non-root IAM user** for daily work.
- IAM is a **global service** — not region-specific.
- US East 1 (Virginia) is often the **cheapest** region because it is AWS's oldest.
- Prefer **auto-generated passwords** with **forced reset on first login**.
- Manage permissions through **groups**, not individual users.
- Use **Administrator Access** for personal accounts and apply **least privilege** at the team level.
- Non-root sign-in uses **Account ID + username + password** (not email).

## Quick Revision Notes and Memory Aids
- IAM = **global service**, scope across regions.
- Cheaper region default: **US East 1 (Virginia)**.
- User login fields: **Account ID + Username + Password**.
- Password tip: **auto-generate + force reset at first sign-in**.
- Group workflow: **create group → attach policies → add users**.

## Exam Tips and Common Pitfalls
- Do not confuse root user sign-in (email) with non-root user sign-in (account ID + username).
- Remember that IAM resources are **global**, not tied to a region.
- Attaching policies **directly to users** is possible but not preferred — prefer **groups**.
- Auto-generated passwords are shown **only once** — capture them immediately.
- Even admin-level groups can be **restricted** through additional policies (e.g., RDS read-only).
