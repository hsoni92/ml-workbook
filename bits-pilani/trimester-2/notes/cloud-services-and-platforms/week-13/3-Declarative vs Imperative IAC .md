# Declarative vs Imperative IaC

## Declarative approach
- Describe desired end state.
- Tool decides operation order from dependency graph.
- Terraform, CloudFormation, and Kubernetes manifests are common declarative examples.

## Imperative approach
- Describe exact steps/commands to run.
- Scripts such as shell/Python/CLI sequences are imperative.
- Useful for procedural tasks but harder to reason about drift and final state.

## Exam comparison
- Declarative: what should exist.
- Imperative: how to create/change it step by step.
- Terraform plan works because Terraform compares desired config, state, and real provider objects.
