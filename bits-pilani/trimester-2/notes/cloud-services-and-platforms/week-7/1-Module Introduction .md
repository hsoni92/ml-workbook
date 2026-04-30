# Week 7: Containers, Registries, and Kubernetes

## Why containers matter
- Containers package application code and dependencies into a repeatable runtime unit.
- They reduce environment drift between developer laptop, CI, and production.
- Containers are not mini-VMs; they share the host kernel and isolate processes.

## Week flow
- Docker image creation comes before registry publishing.
- Registry stores and distributes images.
- Kubernetes schedules, scales, heals, and exposes containers across nodes.

## Exam lens
- Know image vs container, VM vs container, registry vs orchestrator.
- Know Kubernetes control plane vs worker-node components.
- Expect scenario questions about portability, scaling, and rollout recovery.
