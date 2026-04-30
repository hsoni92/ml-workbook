# Infrastructure as Code Basics

## What IaC solves
- Manual console setup is slow, hard to review, and difficult to reproduce.
- IaC makes infrastructure changes visible in code review.
- Same definitions can create dev/stage/prod with parameter changes.

## Benefits
- Repeatability, auditability, consistency, faster recovery, and safer collaboration.
- Changes can pass through CI checks before apply.
- Disaster recovery improves because infrastructure can be rebuilt from code.

## Responsibilities
- Code quality matters: modules, variables, naming, and review discipline.
- Secrets must not be committed.
- IaC controls infrastructure but does not automatically validate application behavior.
