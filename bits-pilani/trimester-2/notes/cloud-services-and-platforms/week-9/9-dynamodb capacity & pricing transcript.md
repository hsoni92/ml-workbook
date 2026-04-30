# DynamoDB Capacity and Pricing

## Capacity modes
- On-demand charges per request and fits unpredictable/spiky workloads.
- Provisioned capacity sets read/write units and fits predictable steady workloads.
- Autoscaling can adjust provisioned capacity within configured bounds.

## Read and write units
- Write capacity depends on item size and write rate.
- Read capacity depends on item size and consistency mode.
- Strongly consistent reads cost more capacity than eventually consistent reads.

## Cost traps
- Indexes consume separate read/write capacity.
- Scans are expensive compared to targeted key queries.
- Poor partition key design can throttle even if table-level capacity looks sufficient.
