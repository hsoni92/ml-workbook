# Practical Lab: AWS Account Setup Walkthrough (Week 4)

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
- Hands-on lab setting up a **personal AWS account** used throughout the program for both theoretical and practical learning.
- The setup flow spans **five steps** in total for AWS account creation.
- After account creation, the **first action** is to set a **budget** to avoid unexpected billing.

## Terminology and Definitions
- **AWS Account**: The container for all AWS resources; created by signing up via the AWS website.
- **Root User**: Automatically created when the account is created; logs in using **email + password**.
- **Free Plan**: AWS's free-tier plan for beginners (6-month window); avoids charges while learning.
- **UPI Auto Pay**: Payment method option using a UPI ID for auto payments.
- **Account ID**: A unique identifier for the AWS account; required alongside IAM credentials.
- **Budget**: A configuration that triggers notifications when spending exceeds a threshold.
- **Zero Spend Budget**: A built-in budget template that alerts on any charge above $0.01.
- **Monthly Cost Budget**: A budget template for defined monthly spending limits.
- **Billing and Cost Management**: AWS console area for managing bills and budgets.

## Detailed Explanations
### Creating the AWS Account
- Search **"create AWS account"** in a browser.
- Click **Create Account** (top right of the AWS page).
- Provide:
  - A personal, active email address.
  - A name (a valid, recognizable name).
- Click **Verify Email Address** — an OTP is sent to the provided email.
- Enter the OTP to authenticate.
- Set a **password** meeting AWS's complexity requirements.
- AWS checks the password; avoid:
  - Repetitive or common passwords.
  - Personal identifiers (names, mobile numbers).
  - Simple patterns (e.g., "ABC", "8123").
- Use a random, complex password.
- Click **Continue**.

### Plan, Contact, and Payment
- Choose the **Free Plan** (six months) to avoid unnecessary charges while learning.
- Select **Personal** (either option is fine for individual learners).
- Provide:
  - Full name.
  - Valid mobile number.
  - Country.
  - Address.
  - City.
  - Postal code.
- Agree to terms and continue (Step 2 of 5).
- Payment options:
  - **UPI Auto Pay** (recommended for easy authentication; lower complexity).
  - **Credit or Debit Card** (must be **enabled for international transactions**, otherwise errors occur).
- On payment submission:
  - A small amount (around ₹2) is deducted for verification and refunded.
  - Verifies the bank is active for international transactions.
- Provide a **mobile number**; AWS sends an OTP to verify.
- Choose a **support plan** (select the one with **free-tier support**).
- On completion, an end page confirms the account is **up and active**.
- Activation typically takes up to **15 minutes** (often within 2 minutes; waiting 5-10 minutes is safe).

### Signing in the First Time
- Sign in as **root user** on the AWS console sign-in page.
- Provide:
  - Email ID used for account creation.
  - Password.
- The console interface appears empty at first since no services have been used.

### Key Details to Save
- After logging in, always **copy and save**:
  - **Account ID**.
  - **Email ID** used for root user.
  - **Password**.
- These details are critical.
- AWS does not offer typical "forgot password" style recovery, so losing them while resources are running can lead to ongoing billing and a complex recovery process.
- Save details securely:
  - Write them down.
  - Or use a secure email account (e.g., Gmail).
  - Choose a secure, private approach.

### Exploring the Console
- The console shows different service categories:
  - Compute (various services).
  - Database (multiple services).
  - IoT, ML, and more.
- Services can be listed alphabetically using **All Services**.
- Throughout the program, focus remains on **important AWS services**.

### Setting a Budget (First Priority After Account Creation)
- Purpose: avoid unexpected billing.
- Navigate:
  - Click **Account ID** (top right).
  - Select **Billing and Cost Management**.
- In the left navigation, find **Budgets**.
- Click **Create Budget**.
- Template options:
  - **Zero Spend Budget** — alert triggered when charges exceed approximately $0.01 (best for pure learning).
  - **Monthly Cost Budget** — useful later for projects with defined monthly budgets.
- Configure:
  - Provide a unique, meaningful name (e.g., learning, demo, introduction variant of the default).
  - Enter an email ID to receive notifications when threshold is crossed.
  - Click **Create Budget**.
- Result:
  - The budget shows unhealthy when charges exceed the threshold.
  - Notifications are sent to the configured email.
  - Status can be reviewed anytime from **Billing and Cost Management → Budgets**.

### Monitoring the Budget Over Time
- Review forecasts and cumulative usage frequently.
- Download reports when managing multiple budgets.

## Workflows / Process Steps
### Account Creation Workflow
1. Go to the AWS "Create Account" page.
2. Enter a valid email and verify with the OTP.
3. Set a strong, complex, unique password.
4. Provide personal details (name, mobile, address).
5. Choose **Free Plan** (personal account).
6. Provide payment method (**UPI Auto Pay** preferred).
7. Complete mobile OTP verification.
8. Choose free-tier support plan.
9. Wait up to ~15 minutes for activation (usually a few minutes).
10. Sign in as **root user** using email and password.
11. Save **Account ID**, email, and password securely.

### Budget Setup Workflow
1. From Account ID menu, select **Billing and Cost Management**.
2. Navigate to **Budgets** on the left panel.
3. Click **Create Budget**.
4. Choose **Zero Spend Budget** template (ideal for learning).
5. Provide a meaningful name.
6. Add notification email.
7. Click **Create Budget**.
8. Monitor under **Budgets** regularly.

## Examples and Use Cases
- A student creating a personal learning account with minimal payment exposure (UPI auto-pay).
- Setting a **Zero Spend Budget** to ensure any accidental usage triggers an email alert.
- Using the AWS Free Plan for six months to practice without incurring costs.
- Keeping the account ID and root credentials safely stored in a secure location.

## Comparison Tables
### Payment Options During Signup
| Method | Pros | Cons |
|---|---|---|
| UPI Auto Pay | Familiar, low complexity | Requires a UPI-enabled account |
| Credit / Debit Card | Widely accepted | Must be enabled for international transactions; errors if disabled |

### Budget Templates
| Template | Purpose |
|---|---|
| Zero Spend Budget | Alerts on any charge above ~$0.01 (best for practice without any spend) |
| Monthly Cost Budget | Alerts against a defined monthly cost limit (useful for projects) |

### What to Save vs What Not to Save
| Save Securely | Do Not Expose |
|---|---|
| Account ID | Passwords in plain view |
| Root email and password | Payment details outside official AWS forms |
| IAM credentials (for later use) | Any credentials to friends/classmates |

## Key Takeaways and Summary
- AWS account creation is a **5-step** process ending with an **active account**.
- **Save account ID, email, and password** safely — AWS lacks typical password-recovery UX that makes lost credentials recoverable easily.
- Sign in as the **root user** initially; avoid daily use of the root user beyond this lab.
- **First priority after account creation** is setting up a **Zero Spend Budget** to get alerts on any charge.
- UPI Auto Pay is the recommended payment method for simplicity during signup.
- Activation usually completes within minutes; wait briefly before signing in.

## Quick Revision Notes and Memory Aids
- Steps: **Email → Password → Plan → Contact → Payment → OTP → Support → Activate**.
- Payment: **UPI easier; cards require international transactions enabled**.
- Save: **Account ID + Email + Password**.
- First task after login: **Create Zero Spend Budget**.

## Exam Tips and Common Pitfalls
- Remember the root user sign-in requires **email**, not a username.
- A small transaction (~₹2) during signup is **normal and refundable**.
- Budgets must be **configured** — they are not set automatically.
- Losing root credentials while resources are running leads to **ongoing billing** and **complex recovery**.
- Zero Spend Budget is configured to alert above ~$0.01 charges, not zero dollars exactly.
