# CIDR and IP Addressing

## CIDR basics
- CIDR notation combines network address and prefix length, for example 10.0.0.0/16.
- Smaller prefix number means larger network: /16 is larger than /24.
- AWS reserves five IP addresses in every subnet, so usable addresses are less than the raw CIDR count.

## Planning addresses
- Use larger VPC CIDR blocks when future subnet growth is likely.
- Do not overlap CIDR ranges across VPC peering, VPN, Direct Connect, or on-prem networks.
- Common pattern: VPC /16, subnets /24 or /20 depending on expected workload scale.

## Exam shortcuts
- /16 is about 65k addresses; /24 is 256 raw addresses; /28 is the smallest AWS subnet size.
- Public/private is not decided by CIDR; it is decided by route table.
- CIDR mistakes show up later as failed peering, limited scaling, or impossible hybrid connectivity.
