# Terraform Workflow

## Write
- Create .tf files for providers, resources, variables, outputs, and modules.
- Format with terraform fmt.
- Validate syntax and provider schema with terraform validate.

## Plan and apply
- terraform init prepares plugins/backend.
- terraform plan shows create/update/delete actions before changes.
- terraform apply executes the approved plan and records results in state.

## Operate
- Use remote backend and locking in teams.
- Review plans before production apply.
- Detect and correct drift by reconciling code/state/reality.
