# GitHub Actions

## How Actions is structured
- Workflow is YAML file stored under .github/workflows.
- Event triggers workflow: push, pull_request, schedule, workflow_dispatch.
- Job runs on runner and contains ordered steps.
- Action is reusable unit used inside a step.

## Common CI/CD usage
- Checkout code.
- Set up runtime.
- Install dependencies.
- Run tests/lint/security scans.
- Build artifact or Docker image.
- Deploy using cloud credentials or OIDC role.

## Important cautions
- Use secrets or OIDC, never hardcode keys.
- Pin third-party actions where supply-chain risk matters.
- Use environments and approvals for production deployments.
