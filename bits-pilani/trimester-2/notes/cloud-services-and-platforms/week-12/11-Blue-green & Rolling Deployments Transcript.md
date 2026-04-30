# Blue-Green and Rolling Deployments

## Blue-green deployment
- Run two full environments: blue current, green new.
- Shift traffic to green after validation.
- Rollback is fast by switching traffic back to blue.
- Costs more because duplicate environment exists during release.

## Rolling deployment
- Replace instances/pods in batches.
- Maintains service while gradually updating fleet.
- Uses less extra capacity than blue-green.
- Rollback may be slower because versions are mixed during rollout.

## Exam comparison
- Need fastest rollback and near-zero downtime: blue-green.
- Need gradual low-extra-cost update: rolling.
- Both require health checks and version compatibility during transition.
