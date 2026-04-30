# Public IPs vs Elastic IPs

## Public IPv4 address
- Can be auto-assigned to an instance launched in a public subnet.
- Usually changes when an instance is stopped and started.
- Useful for temporary labs, not stable production endpoints.

## Elastic IP address
- Static public IPv4 address allocated to your AWS account.
- Can be remapped to another instance or network interface.
- Charged when allocated but not properly associated/used.

## Exam choices
- Use Elastic IP when a fixed public address is explicitly required.
- Prefer DNS/load balancers over direct instance public IPs for production.
- Public IP alone is insufficient without public subnet route and security rules.
