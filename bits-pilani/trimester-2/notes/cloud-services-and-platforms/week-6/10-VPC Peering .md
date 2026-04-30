# VPC Peering

## What peering does
- Privately connects two VPCs so resources can communicate using private IPs.
- Works across accounts and Regions where supported.
- Traffic stays on AWS network and does not require public internet.

## Hard rules
- CIDR blocks must not overlap.
- Peering is non-transitive: A-B and B-C does not mean A-C.
- Both VPC route tables must include routes to the peer CIDR through the peering connection.

## When not to use it
- Many-to-many VPC networks are better handled with Transit Gateway.
- Shared services at scale become messy with full mesh peering.
- Peering does not provide centralized routing inspection by itself.
