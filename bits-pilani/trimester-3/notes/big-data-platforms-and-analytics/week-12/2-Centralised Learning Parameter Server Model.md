# Centralised Learning – Parameter Server Model (Week 12 – TensorFlow Distributed Strategies)

## Learning Objectives
By the end of this lesson you will be able to:
- Describe the parameter server architecture and its two distinct roles
- Explain the training step workflow in a parameter server setup
- Identify the ideal use cases for parameter server (sparse, large-scale models)
- Recognize the central bottleneck limitation as worker count scales
- Contrast with decentralized alternatives (Ring AllReduce)

## Core Concept: Centralized Parameter Management
The parameter server model splits the cluster into two specialized roles:

### Roles
| Role | Responsibility | Analogy |
|------|----------------|---------|
| **Parameter Servers** | Store and update global model weights | "The Brain" – central repository |
| **Workers** | Process data, compute gradients, push/pull parameters | "The Muscles" – heavy lifting |

### Single Training Step Workflow
1. **Pull**: Worker fetches latest model parameters from server
2. **Compute**: Worker processes a data batch (forward + backward pass) → local gradients
3. **Push**: Worker sends gradients back to parameter server
4. **Update**: Server applies optimizer (e.g., SGD) to global weights

### Ideal Use Cases
- **Large Sparse Models**: Billions of parameters where only a small fraction updates per step
- **Recommendation Systems**: Massive embedding tables with sparse access patterns
- **Memory Efficiency**: Dedicated servers manage state without duplicating full model on every worker

### Scaling Limitation
- **Central Bottleneck**: As worker count increases, parameter server becomes throughput choke point
- **Contention**: Many workers simultaneously pulling/pushing saturates server network/CPU
- **Mitigation**: Shard parameter servers, but adds complexity

## Comparison Preview
| Aspect | Parameter Server | Ring AllReduce (Next Lesson) |
|--------|------------------|------------------------------|
| **Architecture** | Centralized | Decentralized (peer-to-peer ring) |
| **Best For** | Sparse models | Dense models (CNNs, Transformers) |
| **Bottleneck** | Central server | None (bandwidth-optimal) |
| **Communication** | All-to-one / one-to-all | Neighbor-to-neighbor |

## Summary
The parameter server model provides an intuitive centralized approach ideal for sparse, large-scale models where parameter updates are infrequent per dimension. However, its central coordination point becomes a scalability ceiling, motivating decentralized alternatives like Ring AllReduce for dense model training on high-speed interconnects.