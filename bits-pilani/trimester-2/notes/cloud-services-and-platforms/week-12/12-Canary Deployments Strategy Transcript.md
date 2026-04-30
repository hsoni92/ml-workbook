# Canary Deployment Strategy

## Canary idea
- Release new version to a small percentage of users/traffic first.
- Observe metrics such as error rate, latency, conversion, and resource use.
- Increase traffic gradually if healthy; rollback if signals degrade.

## Where it fits
- High-risk changes where full rollout is dangerous.
- Services with good traffic routing and observability.
- User-facing apps where behavior can be measured before broad exposure.

## Exam distinction
- Canary is traffic-percentage validation.
- Rolling is batch replacement of infrastructure.
- Blue-green is environment switch.
- Canary fails without monitoring because you cannot judge promotion.
