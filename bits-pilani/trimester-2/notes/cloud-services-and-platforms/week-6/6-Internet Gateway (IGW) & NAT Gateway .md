# Internet Gateway and NAT Gateway

## Internet Gateway
- IGW attaches to a VPC and allows internet-routable traffic for resources with public IPs.
- It is horizontally scaled and highly available by design.
- A route to IGW plus public IP is required for direct internet access from EC2.

## NAT Gateway
- NAT Gateway lives in a public subnet and lets private subnet resources initiate outbound internet connections.
- It does not allow unsolicited inbound internet connections to private instances.
- For high availability, deploy NAT Gateway per AZ and route private subnets to same-AZ NAT.

## Exam contrast
- IGW = bidirectional internet path for public resources.
- NAT = outbound-only internet path for private resources.
- Gateway endpoint can replace NAT for S3/DynamoDB private access and reduce cost.
