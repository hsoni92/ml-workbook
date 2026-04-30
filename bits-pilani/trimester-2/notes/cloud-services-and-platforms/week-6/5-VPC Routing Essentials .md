# VPC Routing Essentials

## How route tables work
- Each subnet is associated with one route table.
- The local route for the VPC CIDR is automatically present and enables internal VPC communication.
- Most specific route wins: /24 beats /16, which beats 0.0.0.0/0.

## Common route targets
- Internet Gateway for public internet paths.
- NAT Gateway for private subnet outbound internet.
- VPC peering connection for another VPC CIDR.
- Virtual private gateway or transit gateway for hybrid and multi-VPC networks.

## Troubleshooting route issues
- No route means packets have no valid next hop.
- Correct route but wrong firewall means traffic still fails.
- Return path matters: both sides must have routes back, especially across peering/VPN.
