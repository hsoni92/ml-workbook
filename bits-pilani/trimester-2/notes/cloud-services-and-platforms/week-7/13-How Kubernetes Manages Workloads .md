# How Kubernetes Manages Workloads

## Desired state loop
- You submit manifests describing desired replicas, images, and policies.
- Controllers compare desired state with actual state.
- When pods fail, controllers create replacements.

## Workload primitives
- Deployment for stateless replicated apps.
- StatefulSet for stable identity/storage needs.
- DaemonSet for one pod per node agents such as log collectors.
- Job/CronJob for finite or scheduled tasks.

## Exam scenarios
- Need rolling update and rollback for stateless API: Deployment.
- Need stable network identity for database-like workload: StatefulSet.
- Need node-level monitoring agent everywhere: DaemonSet.
