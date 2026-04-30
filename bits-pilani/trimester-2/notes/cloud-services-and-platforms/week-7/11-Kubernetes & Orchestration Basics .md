# Kubernetes and Orchestration Basics

## Why orchestration exists
- Single-container management fails at scale when containers must be scheduled, healed, scaled, and updated.
- Kubernetes manages desired state: you declare what should run and controllers reconcile reality.
- It abstracts a cluster of machines into a workload platform.

## Basic objects
- Pod is the smallest deployable unit.
- Deployment manages replicas and rolling updates.
- Service gives stable networking for pods.
- Namespace groups resources logically.

## Exam clarity
- Kubernetes is not a registry and not a Docker replacement alone.
- It solves scheduling and lifecycle control.
- Managed Kubernetes such as EKS reduces control-plane operations but worker/app design remains your responsibility.
