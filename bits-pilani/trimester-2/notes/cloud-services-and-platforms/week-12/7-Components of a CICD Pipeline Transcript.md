# Components of a CI/CD Pipeline

## Pipeline stages
- Source: change detected from repository event.
- Build: compile/package application or container image.
- Test: unit, integration, security, lint, or policy checks.
- Package: publish artifact/image.
- Deploy: promote artifact to environment.

## Artifacts and environments
- Artifact must be immutable so the same build moves across stages.
- Environment-specific config should be injected, not rebuilt into different artifacts.
- Dev/stage/prod promotion reduces surprise.

## Failure handling
- Fail fast on tests.
- Block deploy when quality gates fail.
- Support rollback or roll-forward with known artifact versions.
