# NACLs vs Security Groups

## Security groups
- Attach to ENIs/instances and act as stateful firewalls.
- Only allow rules are configured; anything not allowed is denied.
- Return traffic is automatically allowed for established flows.

## Network ACLs
- Attach at subnet boundary and are stateless.
- Support allow and deny rules with rule numbers evaluated in order.
- Inbound and outbound rules must both permit traffic, including ephemeral return ports.

## How to choose in exam answers
- Use SGs for normal workload access control.
- Use NACLs for subnet-wide guardrails or explicit deny cases.
- If request succeeds one way but return fails, suspect NACL stateless behavior.
