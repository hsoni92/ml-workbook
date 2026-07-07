# Distributing the Gradient Calculation (Week 11 – Foundations of Distributed ML)

## Learning Objectives
By the end of this lesson you will be able to:
- Describe the 4-step cycle of a distributed SGD iteration
- Explain the role of parameter servers vs. all-reduce communication patterns
- Identify how local gradients are aggregated into a global update
- Analyze the network latency impact on training throughput
- Set the stage for synchronization strategy decisions

## Core Concept: The Push-Update-Pull Cycle
Distributed SGD implements the standard gradient update by distributing the computation across workers, then coordinating to produce a single global parameter update.

### 4-Step Distributed Iteration

#### Step 1: Local Calculation
- Each worker takes its assigned mini-batch
- Uses current model copy to perform forward/backward pass
- Computes **local gradient** = gradient of loss on its data shard
- This represents the optimal update direction *for that worker's data subset*

#### Step 2: Push (Gradient Communication)
- Workers send local gradients to aggregation point
- Two main communication patterns:
  - **Parameter Server**: Workers push to central server(s)
  - **All-Reduce**: Workers exchange directly via collective communication
- Goal: Gather all local gradients at a central/collective point

#### Step 3: Global Update (Aggregation)
- System computes **average of all local gradients**
- This average = **global gradient** representing full dataset
- Applied to master model copy using standard SGD formula:
  ```
  θ_global = θ_global - η * (1/N * Σ ∇L_i(θ))
  ```
- Guarantees mathematical equivalence to single-machine SGD on full batch

#### Step 4: Pull (Model Broadcast)
- Updated global parameters broadcast to all workers
- Workers replace their stale local copies
- Cycle complete – all workers synchronized for next iteration

### Communication Patterns Compared

| Pattern | Architecture | Scalability | Fault Tolerance |
|---------|--------------|-------------|-----------------|
| **Parameter Server** | Centralized coordinators | Limited by server bandwidth | Server failure = job failure |
| **All-Reduce** (Ring/Tree) | Decentralized peer-to-peer | Scales to thousands of nodes | More resilient, no single point |

### Network Bottleneck Reality
- **Critical Path**: Push + Pull latency directly adds to iteration time
- **If network slow**: Workers spend >50% time waiting for communication
- **Optimization Target**: Minimize gradient size, maximize bandwidth utilization
- **Techniques**: Gradient compression, quantization, sparse updates

## Summary
The distributed SGD cycle transforms a sequential algorithm into a coordinated parallel one:
1. **Compute** locally (embarrassingly parallel)
2. **Communicate** gradients (bandwidth-bound)
3. **Aggregate** centrally/collectively (reduce operation)
4. **Broadcast** updated parameters (bandwidth-bound)

This cycle repeats millions of times. The synchronization strategy (next lesson) determines *when* workers must wait for each other – the key trade-off between mathematical purity and hardware efficiency.