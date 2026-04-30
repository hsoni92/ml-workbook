# Containers vs Virtual Machines

## Virtual machines
- VM virtualizes hardware and runs a full guest OS.
- Strong isolation but heavier boot time and resource footprint.
- Good for mixed OS kernels, legacy workloads, and strict isolation.

## Containers
- Container virtualizes at OS level and shares host kernel.
- Starts quickly and packs more workloads per host.
- Best for portable services, microservices, and CI/CD workflows.

## Exam comparison
- VM = full OS per workload; container = process isolation on shared kernel.
- Containers improve density but require image hygiene and runtime isolation controls.
- If different OS kernels are required, choose VM, not container.
