# Review of Stochastic Gradient Descent (SGD) (Week 11 – Foundations of Distributed ML)

## Learning Objectives
By the end of this lesson you will be able to:
- Recall the core mathematical formulation of Stochastic Gradient Descent (SGD)
- Identify why distributed SGD requires modifications for cluster coordination
- Map the distributed SGD workflow onto a push‑update‑pull cycle
- Recognize the bottlenecks introduced by gradient communication
- Appreciate the trade‑offs between synchronous and asynchronous aggregation

## Core Concept: Elementary SGD Refresh
Standard (single‑node) SGD updates model weights **θ** by:
```
θ_{t+1} = θ_t – η ∇_θ L(θ_t)
```
- **θ_t** – current parameter vector  
- **∇_θ L(θ_t)** – gradient of the loss on a mini‑batch  
- **η** – learning rate (step size)  
- Goal: iteratively move toward the loss minimum

## Distributed SGD Workflow (4‑Step Cycle)
When multiple workers collaborate, each performs the same steps locally and then synchronizes:

| Step | Operation | Detail |
|------|-----------|--------|
| **1. Local Gradient Calculation** | Each worker computes a gradient on its own mini‑batch | Gradients differ due to data partitioning |
| **2. Gradient Push (Communication)** | Workers send their local gradients to a central parameter server (or use collective communication) | Communication volume = **model size** per worker |
| **3. Global Update** | Parameter server (or all‑reduce) averages/aggregates the received gradients | Produces a single global update direction |
| **4. Model Pull (Broadcast)** | Updated parameters are broadcast back to all workers | Workers replace stale local copies with the new model |

### Visual Workflow
```
Worker A            Worker B            Worker C
  |  Compute grad    │        │           │
  |  ────► (push)    ├────────┼─────►      │
  └──────────────────►  Parameter Server ◄───────┘
          ▲                     │
          │                     ▼
      (average) ◄─────► Global Gradient ◄───────┘
          │                     │
          ▼                     ▼
   Pull updated model   ←  Broadcast new weights
```

## Aggregation Strategies Overview
- **Parameter Server**: Central server collects and redistributes updates
- **All‑Reduce**: Collective operation where gradients are summed across all workers (e.g., NVIDIA NCCL)
- **Gossip / Peer‑to‑Peer**: Gradient mixing among neighbors (asynchronous variants)

### Key Bottlenecks
- **Network Transfer Cost**: Communication volume scales with model size × number of workers
- **Synchronization Latency**: Workers must wait for all-to-one and one-to-all phases
- **Straggler Impact**: Slow workers delay the entire aggregation step
- **Out‑of‑Date Gradients**: If update takes multiple iterations to propagate, steps become stale

## Summary of This Module
- **SGD Core**: Accurate, iterative descent using gradient information
- **Distributed Extension**: Replicates the single‑node algorithm across many nodes
- **Coordination Mechanism**: Push‑gradient → aggregate → broadcast loop
- **Scalability Constraint**: Communication speed often dictates overall throughput

The next lesson will evaluate two concrete aggregation patterns:
- **Synchronous SGD** – workers wait for all updates before proceeding  
- **Asynchronous SGD** – workers update parameters as soon as their gradients arrive  

We'll explore the trade‑offs in speed, convergence behavior, and model stability these patterns introduce.