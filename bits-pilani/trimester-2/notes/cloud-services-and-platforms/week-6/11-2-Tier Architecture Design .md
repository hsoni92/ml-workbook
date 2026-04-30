# Two-Tier Architecture Design

## Architecture shape
- Two-tier commonly means presentation/application tier plus database tier.
- Internet-facing entry point belongs in public subnet; database belongs in private subnet.
- Security group references should express tier relationships, not broad CIDR access.

## AWS mapping
- ALB or web server in public subnet receives user traffic.
- Application or database tier in private subnet accepts only required ports.
- NAT is optional and only for private tier outbound updates/API calls.

## Exam-safe answer
- Mention subnet placement, route tables, and SG flow.
- Use Multi-AZ for availability if production resilience is asked.
- Never expose database directly to the internet for convenience.
