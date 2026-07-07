# Synchronisation and Convergence Issues (Week 11 – Foundations of Distributed ML)

## Learning Objectives
By the end of this lesson you will be able to:
- Explain how stragglers impact distributed training performance and convergence
- Analyze gradient staleness and its effects on model stability
- Evaluate the challenges of hardware heterogeneity in large-scale clusters
- Design strategies to balance workloads across heterogeneous hardware
- Understand the trade-offs between synchronous and asynchronous coordination patterns

## Core Concept: The Straggler Problem
Even with perfect network conditions, distributed training is limited by its **slowest participants**. 

### Straggler Dynamics
- **Definition**: A node that completes its computation significantly slower than peers
- **Causes**: 
  - Temporary network congestion
  - Background system processes
  - Resource contention from other jobs
  - Hardware degradation or variance
- **Impact**:
  - Entire stage waits for straggler → massive compute resource idle time
  - Wasted capital expenditure on unused GPU/CPU cycles
  - Reduced effective throughput despite high cluster capacity

### Real-World Example
- 100 GPUs launched for training
- 99 finish in 1 second
- 1 straggler takes 10 seconds
- Result: 92 GPUs sit idle for 9 seconds each iteration
- Effective utilization drops from 100% → ~10%

## Gradient Staleness: The Cost of Delayed Updates
When using asynchronous updates to mitigate stragglers:

### Mechanism
- Workers push gradients as soon as they're computed
- No waiting for full synchronization

### Problem: Stale Gradients
- By the time a slow worker's gradient reaches the parameter server, 
  multiple model updates may have already occurred
- Resulting update may be **outdated** relative to current model state
- **Consequences**:
  - Slower convergence rates
  - Potential divergence or oscillation in loss surface
  - Suboptimal model parameters

### Mitigation Strategies
1. **Gradient Discarding**: Ignore very old gradients
2. **Learning Rate Scheduling**: Reduce LR over time to accommodate staleness
3. **Elastic Averaging SGD**: Maintain local copies and periodically average
4. **Timeout Mechanisms**: Drop gradients that exceed a maximum age

## Hardware Heterogeneity: The Load Balancing Challenge
Production clusters rarely consist of homogeneous hardware:

### Sources of Variability
- Different GPU models (V100 vs A100 vs T4)
- Mixed CPU/GPU deployments
- Older vs newer server generations
- Varying memory configurations

### Load Balancing Difficulties
- Fixed data partitioning may overload slower nodes
- Equal work distribution leads to stragglers
- Dynamic partitioning requires runtime monitoring and adjustment

### Engineering Approaches
- **Speculative Execution**: Launch duplicate tasks for slow nodes
- **Adaptive Work Scheduling**: Monitor progress and rebalance
- **Heterogeneous Resource Allocation**: Assign smaller workloads to slower nodes
- **Resource Tagging**: Tag nodes by performance class for targeted job placement

## Summary Checklist
- [ ] **Identify stragglers** using Spark UI task duration gaps
- [ ] **Measure gradient staleness** impact on convergence behavior
- [ ] **Assess hardware heterogeneity** through profiling and monitoring
- [ ] **Choose coordination pattern** (sync vs async) based on workload characteristics
- [ ] **Implement mitigation techniques** appropriate to your scale and hardware mix

> *"Distributed training success depends not just on raw compute power, but on how well you manage timing, coordination, and heterogeneity."*

*Transition to next lesson where we'll explore the two primary strategies for splitting ML workloads: data parallelism versus model parallelism.*