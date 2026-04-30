# Connecting Resources Across Subnets

## Default connectivity
- Subnets in the same VPC can route to each other through the local route.
- No Internet Gateway or NAT is required for private communication inside a VPC.
- Traffic still must pass security groups and NACLs.

## Layered design
- Web tier accepts traffic from load balancer security group.
- App tier accepts traffic only from web/load balancer tier.
- DB tier accepts traffic only from app tier on database port.

## Common failure points
- Missing SG reference between tiers.
- NACL missing ephemeral port range for return traffic.
- Resources placed in different VPCs without peering/transit connectivity.
