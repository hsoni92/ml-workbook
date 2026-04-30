# Kubernetes Architecture Overview

## Control plane
- API server is the front door for all cluster operations.
- etcd stores cluster state.
- Scheduler places pods on nodes.
- Controller manager runs reconciliation loops.

## Worker node
- Kubelet talks to API server and ensures assigned pods run.
- Container runtime starts containers.
- Kube-proxy or CNI handles service networking rules.

## Exam mistakes
- Do not place application pods in etcd; etcd stores metadata/state.
- Scheduler chooses node but does not run container itself.
- Kubelet runs on worker nodes, not only on control plane.
