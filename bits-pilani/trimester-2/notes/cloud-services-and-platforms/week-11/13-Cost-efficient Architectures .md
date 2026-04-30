# Cost-Efficient Architectures

## Design principles
- Use managed services when they reduce operations and idle capacity.
- Scale with demand instead of provisioning for rare peaks.
- Store data in the cheapest class that satisfies retrieval and durability requirements.

## Architecture levers
- Auto Scaling for variable compute.
- Serverless for intermittent event-driven workloads.
- Caching/CDN to reduce repeated expensive backend work.
- Lifecycle policies and compression for storage.

## Exam answer pattern
- First remove waste, then rightsize, then commit to discounts.
- Measure before optimizing.
- Do not trade away reliability or security for small cost savings unless requirement permits.
