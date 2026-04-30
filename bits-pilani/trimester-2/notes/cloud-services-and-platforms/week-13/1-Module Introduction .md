# Week 13: Infrastructure as Code and Terraform Foundation

## IaC mental model
- Infrastructure as Code defines cloud resources in files that can be reviewed, versioned, tested, and repeated.
- Terraform is declarative: describe desired state and let Terraform plan changes.
- The core value is controlled, reproducible infrastructure change.

## Terraform flow
- Write .tf configuration.
- terraform init downloads providers and configures backend.
- terraform plan previews changes.
- terraform apply executes changes and updates state.
- terraform destroy removes managed infrastructure when intended.

## Exam focus
- State file is critical because it maps config to real resources.
- Remote state with locking is needed for teams.
- Manual console edits create drift.
