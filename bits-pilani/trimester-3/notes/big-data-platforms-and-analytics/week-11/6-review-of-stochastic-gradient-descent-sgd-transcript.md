# Stochastic Gradient Descent: The Optimisation Engine of ML

## 1. Why SGD Matters for Distributed ML

Infrastructure (networking, parallelism strategies) enables scale, but **stochastic gradient descent (SGD)** is the mathematical engine that makes learning possible. Every distributed training system ultimately implements a variant of: compute gradients locally, aggregate, update weights globally.

## 2. The Optimisation Problem

SGD minimises a **loss function** $L(\theta)$ by iteratively updating model weights $\theta$.

**Intuition:** Imagine a 3D loss landscape. The goal is to find the lowest point (global minimum). At each step, compute the gradient — the direction of steepest ascent — and take a step in the **opposite** direction (steepest descent).

```mermaid
flowchart LR
    Start[Current weights θ_t] --> Grad[Compute ∇L(θ_t)]
    Grad --> Step[Step opposite to gradient]
    Step --> New[Updated weights θ_{t+1}]
    New --> Start
```

## 3. The SGD Update Rule

$\theta_{t+1} = \theta_t - \eta \cdot \nabla L(\theta_t)$

| Symbol | Meaning |
|--------|---------|
| $\theta_t$ | Current model weights at step $t$ |
| $\nabla L(\theta_t)$ | Gradient (slope of loss at current position) |
| $\eta$ | Learning rate — controls step size |
| $\theta_{t+1}$ | Updated weights after one step |

**Learning rate $\eta$:** Too large → overshoot minimum, diverge. Too small → slow convergence, may get stuck in local minima.

## 4. SGD on a Single Machine

1. Sample a small **mini-batch** of data (not the full dataset — that would be batch gradient descent; not one sample — that would be pure SGD)
2. Compute loss on the mini-batch
3. Calculate gradient $\nabla L(\theta_t)$ via backpropagation
4. Update weights using the formula above
5. Repeat thousands or millions of times until loss converges

**"Stochastic"** refers to the randomness introduced by sampling mini-batches — each gradient estimate is noisy but unbiased on average.

## 5. What Changes in Distributed ML

On a single machine, one gradient is computed per step. In distributed ML:

- Multiple workers stand on **different parts of the data**
- Each computes its own **local gradient** simultaneously
- The challenge: combine local gradients into one accurate **global step**

$\nabla L_{\text{global}} \approx \frac{1}{W} \sum_{i=1}^{W} \nabla L_i(\theta_t)$

where $W$ is the number of workers and $\nabla L_i$ is the gradient computed on worker $i$'s mini-batch.

## 6. Mini-Batch SGD vs Full Batch vs Pure SGD

| Variant | Data per step | Gradient quality | Speed per step |
|---------|---------------|------------------|----------------|
| Full batch | Entire dataset | Exact | Slow |
| Mini-batch SGD | Small batch (32–512) | Noisy but useful | Fast |
| Pure SGD | One sample | Very noisy | Fastest per step |

Distributed training typically uses mini-batch SGD with the effective batch size scaled by worker count.

## 7. Connection to Distributed Training

The distributed SGD cycle:

1. Each worker computes local gradient on its shard
2. Gradients are pushed to central/collective point
3. Global gradient computed (average)
4. Master weights updated
5. Updated weights pulled to all workers
6. Repeat

The mathematics is the same; the engineering challenge is steps 2–5 happening fast enough that workers do not idle.

## Common Pitfalls / Exam Traps

- **Confusing SGD with gradient descent on full data** — SGD uses mini-batches; "stochastic" means sampled.
- **Forgetting learning rate when scaling workers** — effective batch size changes; may need to scale $\eta$.
- **Assuming local gradient equals global gradient** — local gradients are estimates; aggregation averages them.
- **Treating $\nabla L$ as a scalar** — it is a vector (same dimension as $\theta$); update applies element-wise.
- **Ignoring that distributed SGD is still SGD mathematically** — aggregation strategy (sync/async) changes behaviour but not the core update formula.

## Quick Revision Summary

- SGD minimises loss by iteratively stepping opposite to the gradient.
- Update rule: $\theta_{t+1} = \theta_t - \eta \cdot \nabla L(\theta_t)$.
- $\eta$ = learning rate; controls step size and convergence stability.
- Single machine: one mini-batch, one gradient, one update per step.
- Distributed: multiple local gradients aggregated into one global update.
- Global gradient ≈ average of local gradients across workers.
- SGD is the mathematical foundation underlying all distributed training cycles.
