# VPC Security Best Practices

## Network exposure
- Keep only edge resources public; keep app and data tiers private.
- Avoid 0.0.0.0/0 inbound except required public ports on edge layers.
- Use separate subnets/security groups per tier for blast-radius control.

## Controls to combine
- Security groups for workload-level allow rules.
- NACLs for subnet guardrails and explicit deny patterns.
- VPC Flow Logs for traffic visibility and incident analysis.
- VPC endpoints to keep AWS service access private where possible.

## Exam red flags
- SSH/RDP open to the world is almost always wrong.
- Public DB subnet is wrong for normal production designs.
- No logging means weak auditability even if rules look correct.
