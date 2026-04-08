# Shared Responsibility Model

## Why This Topic Is Critical
Many cloud security incidents occur due to misunderstanding responsibility boundaries. The shared responsibility model defines who secures what.

## Core Principle
- **Provider is responsible for security of the cloud.**
- **Customer is responsible for security in the cloud.**

## Provider Responsibilities (Security of the Cloud)
- Physical data center security
- Hardware and server protection
- Networking infrastructure protection
- Power, cooling, and environmental controls
- Hypervisor and foundational virtualization security
- Core platform availability and resilience mechanisms

## Customer Responsibilities (Security in the Cloud)
- Data classification and protection
- Identity and access management
- Correct resource permissions and policy settings
- Network security configurations (security groups, firewalls, routing intent)
- Encryption strategy and key management choices
- OS patching (where applicable, especially in IaaS)
- Secure application design and vulnerability management

## Important Risk Insight
Cloud platforms may be secure by design, but misconfiguration by customers can still expose data.

### Example Scenario
- Storage service is securely operated by provider.
- Customer sets incorrect public permissions.
- Result: data exposure occurs due to customer-side configuration error.

## Apartment Analogy
- Building security (guards, gates, CCTV) = provider responsibilities.
- Locking your apartment door and protecting valuables = customer responsibilities.

## Security Implications by Service Model
- **IaaS:** customer responsibilities are larger.
- **PaaS:** some platform operations shift to provider.
- **SaaS:** provider handles most technical controls, customer still manages user access and data governance.

## Exam-Focused Takeaways
- Distinguish clearly between "of the cloud" and "in the cloud."
- Explain at least one real misconfiguration example.
- Link shared responsibility to service model choice.

## Quick Revision
- Cloud security is a partnership model.
- Misunderstanding boundaries leads to preventable incidents.
- Correct configuration and IAM discipline are central customer duties.
