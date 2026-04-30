# Billing Dashboard and AWS Pricing

## Billing dashboard
- Shows current month spend, forecast, and service-wise cost summary.
- Good first stop for bill shock investigation.
- Needs IAM billing permissions; billing access is separate from ordinary service access in many setups.

## Pricing basics
- AWS pricing is usage-based but each service has its own dimensions.
- Common dimensions include compute time, requests, storage GB-month, data transfer, provisioned capacity, and support plan.
- Free tier is limited and not a production cost strategy.

## Exam angle
- Identify cost driver before optimization.
- Data transfer and logs are common hidden costs.
- Pricing calculator estimates before deployment; Cost Explorer analyzes after usage.
