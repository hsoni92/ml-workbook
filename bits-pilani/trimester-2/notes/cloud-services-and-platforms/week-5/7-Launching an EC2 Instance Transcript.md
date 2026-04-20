# Launching an EC2 Instance

## Learning Objectives

- Walk through complete EC2 launch flow.
- Understand configuration impact of each launch option.
- Connect launch decisions to security, connectivity, and storage behavior.
- Avoid beginner mistakes during first deployment.

---

## Launch Means "Provision a New Virtual Server"

An EC2 launch creates a ready-to-run VM from selected templates and configuration.

Core launch inputs:

1. AMI (software blueprint)
2. Instance type (resource capacity)
3. Key pair (secure access)
4. Security group (network allowlist)
5. Storage config (EBS root volume)

---

## End-to-End Launch Sequence

```mermaid
flowchart LR
  A[Choose AMI] --> B[Choose instance type]
  B --> C[Select/create key pair]
  C --> D[Set security group rules]
  D --> E[Review EBS root volume]
  E --> F[Launch instance]
  F --> G[Get instance ID + IP]
```

---

## Deep Dive by Step

| Step | What you decide | Why it matters |
|---|---|---|
| AMI | Linux/Ubuntu/Windows/custom image | Determines OS/runtime compatibility |
| Instance type | vCPU, RAM, bandwidth profile | Controls performance and cost |
| Key pair | SSH identity material | Needed for secure admin access |
| Security group | allowed ports/sources | Controls who can reach instance |
| EBS | root volume size/type | Persistence and storage performance |

---

## Transcript Concepts Expanded

- Small instances (for learning) are typically enough for command-line experimentation.
- Security groups should expose only required ports (`22`, `80`, `443` etc.).
- Root EBS volume is attached by default at launch.
- AWS quickly assigns identifiers (instance ID/IP), enabling immediate access operations.

---

## Example: Minimal Web Server Launch

- AMI: Amazon Linux
- Type: small general-purpose
- SG inbound: `22` (admin from office IP), `80` (web traffic)
- EBS: default root volume
- Result: low-cost starter server for practice/prototype deployment

---

## Common Launch Errors

1. Launching without secure key management.
2. Forgetting inbound `22` -> SSH not reachable.
3. Opening admin ports to whole internet unnecessarily.
4. Choosing oversized instance for tiny workloads.

---

## Quick Revision Checklist

- [ ] List the five core EC2 launch inputs.
- [ ] Explain how AMI and instance type differ.
- [ ] State why key pair is critical.
- [ ] Describe how SG impacts reachability after launch.
