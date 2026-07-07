# Architecting for Distributed Intelligence (Week 12 – TensorFlow Distributed Strategies)

## Learning Objectives
By the end of this lesson you will be able to:
- Explain why modern ML models (LLMs, recommendation engines) require multi-node training
- Identify the four primary goals of this module
- Contrast centralized vs. decentralized parameter synchronization
- Understand the role of TensorFlow's Strategy API in distributed training
- Recognize the trade-offs between synchronous and asynchronous training modes

## Core Concept: The Scale Imperative
Modern machine learning models have outgrown single-device capabilities:
- **Large Language Models**: Billions of parameters, petabytes of training data
- **Recommendation Engines**: Massive embedding tables, sparse updates
- **Single Device Limits**: Even the most powerful GPU cannot hold model + data + optimizer states

This forces a shift from **single-device intelligence** to **multi-node intelligence** where clusters work as a cohesive unit.

## Module Goals Overview
1. **Centralized vs. Decentralized Learning**: Parameter Server vs. Ring AllReduce
2. **Synchronous vs. Asynchronous Training**: Consistency vs. Speed trade-offs
3. **TensorFlow Strategies**: MirroredStrategy (single-node) → MultiWorkerMirroredStrategy (multi-node)
4. **Computational Graph Partitioning**: Device placement and graph distribution

## Centralized Learning: Parameter Server Model
- **Architecture**: Dedicated parameter servers hold global model state
- **Workers**: Compute gradients on data shards, push/pull from servers
- **Best For**: Large sparse models (e.g., recommendation systems with huge embedding tables)
- **Bottleneck Risk**: Central server becomes throughput limiter as worker count grows

## Decentralized Learning: Ring AllReduce
- **Architecture**: Workers form logical ring, each communicates only with neighbors
- **Mechanism**: Gradient chunks passed around ring twice → all workers get full aggregate
- **Advantage**: Bandwidth-optimal, eliminates central bottleneck
- **Best For**: Dense models (CNNs, Transformers) on high-speed GPU interconnects

## Training Mode Trade-offs
| Aspect | Synchronous | Asynchronous |
|--------|-------------|--------------|
| **Consistency** | Perfect (single-machine equivalence) | Stale gradients possible |
| **Straggler Impact** | Entire cluster waits for slowest | Fast workers never idle |
| **Throughput** | Lower (70% typical) | Higher (95%+ typical) |
| **Final Accuracy** | Higher, more stable | May converge to lower accuracy |
| **Preferred When** | Stable hardware, fast interconnect | Heterogeneous/unreliable clusters |

## TensorFlow Strategy API
- **MirroredStrategy**: Single-node multi-GPU, synchronous, uses NCCL
- **MultiWorkerMirroredStrategy**: Multi-node, synchronous, Ring AllReduce across workers
- **ParameterServerStrategy**: Centralized, for sparse models

## Computational Graph Distribution
- TensorFlow automatically partitions ops across devices
- Variable placement follows strategy rules
- Understanding device placement critical for performance debugging

---

*This lesson sets the architectural foundation for the practical TensorFlow strategies covered in subsequent lessons.*