# Access Keys and Security Best Practices (Week 4)

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
- **Access keys** are credentials that let AWS interact with tools and services **outside AWS**.
- They act as a **bridge** between AWS and third-party tools or external services (e.g., Terraform, GitHub).
- Access keys consist of two parts: **Access Key** and **Secret Key**.
- The **secret key is shown only once** — if lost, it cannot be retrieved, only replaced.
- Security is the user's responsibility: **AWS only makes security easy; the user must enforce it**.

## Terminology and Definitions
- **Access Key**: The public part of a credential pair used for programmatic AWS access.
- **Secret Key**: The private counterpart of the access key; never re-displayed after creation.
- **CLI (Command Line Interface)**: Tool for interacting with AWS using commands rather than the console.
- **Third-party Tool**: Any service outside AWS that needs to talk to AWS (e.g., Terraform, GitHub).
- **Command Prompt**: The terminal shell on Windows.
- **Tag**: Metadata label (key-value) used to organize AWS resources and access keys.
- **CSV File**: Format in which access keys can be downloaded once.

## Detailed Explanations
### What Access Keys Are
- Credentials used when AWS must interact with anything **outside** AWS.
- Two possible consumers:
  1. **AWS CLI** — running commands locally.
  2. **Third-party services or tools** — such as Terraform or GitHub integrations.
- Access keys enable programmatic access (API calls, automation).

### Where Access Keys Live
- Access keys belong to an IAM **user**, not to roles.
- Navigation:
  - IAM → Users → select user → **Security credentials** tab → scroll to **Access keys**.

### Where Access Keys Are Used
- **AWS CLI**:
  - Any operation you performed in the console (creating a user, group, role) can be done via the CLI with commands.
  - AWS provides documentation on the commands required to create, modify, or manage services.
  - Commonly used by developers working heavily with code.
- **Third-party services**:
  - Use access keys as authentication when integrating AWS with external tools such as GitHub or Terraform.
- **Access from different locations**:
  - Lets you interact with the AWS console/services from any machine using your personal laptop.

### Creating Access Keys
- From the user's **Security credentials** tab:
  - Click to **create access key**.
  - Choose an intended purpose:
    - CLI.
    - Local code.
    - Third-party service.
  - Most developers pick **CLI** — it's the easiest and most common.
  - Check the acknowledgement box.
  - Click **Next**.
  - Add a **meaningful tag** (e.g., `GitHub keys` for GitHub integration, etc.).
  - Click **Create key**.
- AWS generates:
  - **Access Key**.
  - **Secret Key**.
- Both are required to integrate AWS with a third-party service.

### Handling Access Keys Safely
- The keys (especially the secret) are shown **only once**:
  - Use **Show** to view them during creation.
  - Or **download the CSV file** with both keys.
- **Never expose these keys** to:
  - Classmates.
  - Friends or family.
  - Publicly (e.g., committing to a public repo).
- Exposed keys = account misuse risk.

### Rotating and Revoking Keys
- If keys are suspected compromised:
  - Go to **actions** next to the key.
  - **Deactivate** the key, then **delete** it.
- AWS requires typing the key name to confirm deletion.
- After deletion, no one can use those keys anymore.
- Always clean up or replace keys if there is any suspicion of compromise.

### Mac vs Windows CLI
- **Mac**: Terminal.
- **Windows**: **Command Prompt**.
- Both allow you to type commands that interact with AWS services.

### Why Security Matters
- Billing in your AWS account is tied to a UPI, credit card, or debit card.
- Charges are **auto-debited**:
  - You may not notice until a significant amount is deducted.
- Always:
  - Delete or clean up any resources you created.
  - Delete suspicious credentials immediately.
  - Confirm deletion when prompted.
- **AWS only makes security easier; managing it is the user's responsibility**.

## Workflows / Process Steps
### Create an Access Key
1. Go to **IAM → Users → <your user> → Security credentials**.
2. Scroll to **Access keys → Create access key**.
3. Choose intended use (e.g., CLI).
4. Check the acknowledgement.
5. Click **Next**.
6. Add a meaningful **tag** (e.g., `GitHub keys`).
7. Click **Create key**.
8. Immediately **record** both keys:
   - Click **Show** and copy them, **or**.
   - **Download the CSV** file.

### Rotate / Revoke an Access Key
1. Navigate to the user's **Security credentials** tab.
2. Click **Actions** next to the access key.
3. Click **Deactivate**.
4. Click **Delete**.
5. Type the access key name to confirm.
6. The key is permanently removed.

### Delete Any Compromised Resource
1. Go to the relevant resource list (users, roles, etc.).
2. Select the suspicious resource.
3. Click **Delete**.
4. Type **confirm** when prompted.
5. Resource is removed.

## Examples and Use Cases
- Integrating AWS with **Terraform** for infrastructure automation.
- Connecting AWS to **GitHub** for CI/CD workflows.
- Using the **AWS CLI** to script service creation, configuration, or cleanup.
- Rotating keys immediately after a suspected compromise to prevent billing abuse.

## Comparison Tables
### Console vs CLI (Same Outcome, Different Interface)
| Console | CLI |
|---|---|
| Click buttons and navigate GUI | Run commands in terminal / command prompt |
| Good for learning and discovery | Preferred for automation and scripting |
| No credentials needed beyond login | Requires access + secret key pair |

### Access Key Use Cases
| Intended Use | Typical Scenario |
|---|---|
| CLI | Local command-line automation |
| Local code | Developer's machine interacting with AWS |
| Third-party service | GitHub, Terraform, or other integrations |

### Safe Handling
| Do | Don't |
|---|---|
| Download the CSV immediately | Share keys with others |
| Use meaningful tags | Commit keys to public repos |
| Rotate/delete when compromised | Leave unused keys active |
| Delete resources no longer needed | Ignore suspicious activity |

## Key Takeaways and Summary
- Access keys = **bridge between AWS and the outside world** (CLI + third-party tools).
- Created under each IAM user's **Security credentials**.
- Include **access key + secret key**; secret shown **only once**.
- Most common use case: **AWS CLI**.
- **Never share keys**; rotate or delete if compromised.
- **Security is your responsibility** — billing is tied to a real payment method; misuse costs real money.

## Quick Revision Notes and Memory Aids
- Access key = **public**; Secret key = **private, shown once**.
- Pair used for **CLI + third-party integrations**.
- Location: **IAM → Users → Security credentials**.
- Rotation path: **Deactivate → Delete**.
- Mantra: **AWS makes security easy; managing it is on you**.

## Exam Tips and Common Pitfalls
- Access keys belong to **IAM users**, not roles.
- The **secret key cannot be recovered** after creation — only regenerated.
- Do not embed access keys in source code.
- Losing or exposing keys can result in **automatic billing losses** tied to your card/UPI.
- Rotation process: **deactivate first, then delete**.
- CLI terminology differs on Mac vs Windows (Terminal vs Command Prompt) but functionality is equivalent.
