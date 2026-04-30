# GitHub Overview and Repository Workflows

## GitHub role
- Hosts Git repositories and collaboration workflow.
- Pull requests provide review, discussion, checks, and controlled merge.
- Issues/projects help track work around code.

## Repository controls
- Branch protection can require reviews and passing CI checks.
- CODEOWNERS can request reviewers automatically.
- Actions secrets store sensitive CI/CD values for workflows.

## Workflow pattern
- Feature branch -> PR -> automated checks -> review -> merge -> deploy pipeline.
- Direct commits to main are usually blocked in mature workflows.
- PR history gives audit trail for why a change happened.
