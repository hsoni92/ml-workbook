# What Are Containers

## Container concept
- A container is a running process isolated with OS features such as namespaces and cgroups.
- It includes application code, libraries, runtime, and configuration needed to run consistently.
- It shares the host OS kernel, which makes it lighter than a VM.

## What containers solve
- Dependency conflicts across environments.
- Slow and inconsistent deployments.
- Packaging microservices and ML inference services for repeatable release.

## Limits to remember
- Containers are not security boundaries as strong as separate VMs.
- Local container filesystem should be treated as ephemeral.
- Persistent state belongs in volumes, databases, or object storage.
