# MFA Setup and Password Policies (Week 4)

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
- Two additional layers of security for IAM users:
  1. **Multi-Factor Authentication (MFA)**.
  2. **Password policies**.
- **MFA** protects against password compromise; **mandatory** in real companies for console access.
- **Password policies** enforce strength rules, rotation, and reuse behaviours across all users in an account.

## Terminology and Definitions
- **MFA (Multi-Factor Authentication)**: Requires an additional factor beyond username/password to authenticate.
- **Passkey / Passphrase**: A string-based secondary authentication factor.
- **Authenticator App**: Mobile app (e.g., Google Authenticator) that generates time-based OTPs.
- **Hardware MFA Device**: Physical security device (e.g., a YubiKey or similar) used for authentication.
- **Password Policy**: A set of account-wide rules controlling password composition and rotation.
- **Password Expiration**: Time after which a password must be changed.
- **Password Reuse Prevention**: Rule that stops users from reusing older passwords.

## Detailed Explanations
### Enabling MFA
- Go to the user → **Security credentials** tab.
- Scroll to **Assign MFA**.
- Provide a meaningful MFA name.
- Three MFA options are available:
  1. **Passphrase / Passkey**:
     - A combination of numbers (AWS offers a default or you can define your own).
  2. **Authenticator App**:
     - Install a mobile app like **Google Authenticator**.
     - Scan the QR code or enter OTPs generated inside the app.
  3. **Hardware Device**:
     - Physical security token.
     - Common in product-based or high-compliance companies.
     - Example: USB keys or hardware devices connected to a company-issued laptop for access to private networks.
- Pick one, configure it, and MFA is then enabled.

### Why MFA Matters
- Protects against **password compromise**.
- Without MFA, compromised credentials give direct account access.
- **Mandatory for console access** in real-world companies.
- Lab behaviour:
  - Newly created users show a highlighter warning when MFA is not set.
  - It can be enabled at any time.

### Password Policies
- Auto-generated passwords are used initially and replaced on first login.
- Password policy controls ongoing password requirements:
  - Composition rules.
  - Expiration.
  - Reuse prevention.
  - User self-service password changes.
- Similar concept to bank password rules (e.g., SBI rotates passwords monthly).

### Where to Configure Password Policy
- In IAM console, navigate to **Account settings → Password policy → Edit**.

### Password Policy Options
- **Default policy**:
  - Minimum 8 characters.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one number.
  - At least one symbol.
  - No expiration.
- **Custom policy** lets you:
  - Change minimum length (valid range: **6 to 128 characters**).
  - Remove character class requirements (uppercase, lowercase, symbol, number).
  - Enable **password expiration** (e.g., 365 days, 60 days).
  - **Prevent password reuse**.
  - **Allow/disallow users to change their own passwords**.
    - Disallowing is sometimes used by admins to prevent unauthorized changes.
    - Team-to-team variability is common.
- Save with **Save changes**.

## Workflows / Process Steps
### Enabling MFA
1. Go to **IAM → Users → <your user> → Security credentials**.
2. Scroll to **MFA** and click **Assign MFA**.
3. Name the device.
4. Select MFA method:
   - Passphrase / passkey.
   - Authenticator app.
   - Hardware device.
5. Complete the setup (e.g., scan QR or register device).
6. Confirm by entering a generated OTP (for app/device) or the configured passphrase.

### Configuring Password Policy
1. Navigate to **IAM → Account settings**.
2. Select **Password policy → Edit**.
3. Choose **default** or **custom**.
4. Configure:
   - Minimum length (6–128 characters).
   - Character classes required.
   - Password expiration duration (in days).
   - Reuse prevention.
   - Whether users can change their own passwords.
5. Click **Save changes**.

## Examples and Use Cases
- Enabling an **authenticator app** on a personal IAM user to protect learning account access.
- Using **hardware MFA tokens** in regulated or high-compliance companies.
- Setting a **60-day password expiration** for tightly controlled environments.
- Disabling self-service password change during onboarding so admins fully control credentials.

## Comparison Tables
### MFA Options
| Option | How It Works | Typical Use |
|---|---|---|
| Passphrase / Passkey | A static-ish phrase/combination | Simple setups, personal use |
| Authenticator App | Time-based OTP in mobile app | Most common for users |
| Hardware Device | Physical security key | High-compliance / enterprise use |

### Default vs Custom Password Policy
| Feature | Default | Custom |
|---|---|---|
| Minimum length | 8 | 6 to 128 |
| Character classes | Upper, lower, number, symbol required | Configurable |
| Expiration | None | Configurable (in days) |
| Reuse prevention | Not enforced | Configurable |
| User self-service change | Allowed | Configurable |

## Key Takeaways and Summary
- **MFA** adds a critical second factor beyond passwords; **mandatory** in real-world companies.
- Three MFA options: **passphrase, authenticator app, hardware device**.
- Password **policies** enforce composition, rotation, and reuse rules.
- Valid password length range is **6–128 characters**.
- Policies can also control whether users can change their own passwords.
- Both MFA and password policy combine to strengthen the **security layer for IAM users**.

## Quick Revision Notes and Memory Aids
- **MFA types: Passphrase, App, Hardware**.
- **Password min length range: 6 – 128**.
- Default = **8 chars, all classes, no expiry**.
- Password policies live under **IAM → Account settings**.
- Corporate high-compliance = **hardware MFA** (USB key style).

## Exam Tips and Common Pitfalls
- MFA is **not automatic** — users start without MFA; it must be enabled explicitly.
- Authenticator apps rely on **time-based OTPs**, not passwords stored anywhere.
- Remember: password length can go down to **6** characters (often lower than expected by candidates).
- Disallowing user password changes is an admin-control pattern — don't mark it as invalid.
- Password policies are **account-wide**, not per user.
