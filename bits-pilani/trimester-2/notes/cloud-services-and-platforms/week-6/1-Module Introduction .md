# Week 6: VPC Networking Foundation

## Build the mental model
- A VPC is your private network boundary inside an AWS Region.
- Subnets split that address space by availability zone and exposure level.
- Route tables decide where packets go; security groups and NACLs decide whether traffic is allowed.
- Most exam questions are about reachability: public route, private route, firewall rule, or address conflict.

## Design order
- Choose CIDR first and avoid overlap with future peering, VPN, or Direct Connect ranges.
- Create public subnets only for internet-facing entry points such as load balancers or bastion hosts.
- Place application and database tiers in private subnets by default.
- Use NAT only when private workloads need outbound internet access.

## Exam grip
- Public subnet means route to Internet Gateway, not merely public IP.
- Private subnet can still reach the internet through NAT, but internet cannot initiate inbound connections through NAT.
- Security groups are stateful; NACLs are stateless and apply at subnet boundary.
