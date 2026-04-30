# Public vs Private Subnets

## Real difference
- A public subnet has a route to an Internet Gateway for 0.0.0.0/0 or ::/0.
- A private subnet has no direct route to an Internet Gateway.
- Subnet label/name does not matter; route table association does.

## Where resources belong
- Public subnet: load balancer, NAT gateway, bastion host if used.
- Private app subnet: application servers, containers, internal services.
- Private data subnet: databases, caches, queues, and storage endpoints where possible.

## Exam scenarios
- Instance has public IP but no IGW route: not truly internet-reachable.
- Private instance needs OS updates: use NAT Gateway or VPC endpoints depending on destination.
- Database should never sit in public subnet just because SG restricts access; subnet placement is part of defense-in-depth.
