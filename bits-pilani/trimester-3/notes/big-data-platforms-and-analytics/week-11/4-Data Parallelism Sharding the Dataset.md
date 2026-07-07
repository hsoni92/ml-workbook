# Data Parallelism – Sharding the Dataset (Week 11 – Foundations of Distributed ML)

## Learning Objectives
By the end of this lesson you will be able to:
- Explain the core principle of data parallelism in distributed machine learning
- Describe how data sharding enables parallel training across multiple workers
- Implement mini-batch creation from partitioned data shards
- Coordinate gradient aggregation across workers to maintain model consistency
- Evaluate the scalability benefits and limitations of data parallelism

## Core Concept: Data Sharding Fundamentals
Data parallelism is the most common strategy for scaling machine learning workloads when:
- The **model** fits within a single GPU/CPU's memory
- The **dataset** is too large for practical training on a single machine
- You need to increase effective batch size for better convergence

### Sharding Process
1. **Dataset Partitioning**: Split the full dataset into equal-sized shards
   - Example: 100M records → 10 shards of 10M records each
   - Partition count typically matches number of workers (e.g., 8 GPUs → 8 shards)

2. **Independent Processing**: Each worker receives exactly one shard
   - No worker sees data from other shards initially
   - Each processes its shard locally to compute gradients

3. **Parameter Synchronization**: Periodic gradient aggregation step
   - Workers communicate gradients → compute global model update
   - Updated parameters broadcast back to all workers

### Mini-Batch Creation from Shards
- Each worker creates mini-batches from its assigned shard
- Batch size scales with worker count (enabling larger effective batch sizes)
- Example: 32 workers × 32 examples = 1024 effective batch size
- Benefits:
  - Smoother gradient estimates
  - Better generalization through larger batches
  - Faster convergence compared to single-worker training

### Gradient Aggregation Mechanics
```python
# Pseudocode for one training step
local_gradients = compute_gradients(shard_mini_batch)
broadcast_gradients = AllReduce(local_gradients)  # Distributed sum
global_update = apply_update(broadcast_gradients)
# Update shared model parameters with global_update
```

### Performance Characteristics
| Metric | Single-Worker | Data Parallel (N workers) |
|--------|---------------|---------------------------|
| Effective Batch Size | Limited by one device memory | Scales linearly with worker count |
| Training Throughput | Fixed | Increases nearly linearly (until communication saturates) |
| Memory Footprint per Worker | Full model + full data | Full model + 1/N data shard |
| Communication Overhead | None | O(model_size) per iteration |

### When to Choose Data Parallelism
- Model fits in single GPU memory
- Large datasets requiring distributed processing
- Need for increased effective batch size
- Training jobs where communication overhead is manageable
- Goal: Maximize hardware utilization while maintaining model simplicity

### Limitations and Mitigations
- **Communication Saturation**: As worker count grows, gradient sync becomes bottleneck
- **Straggler Impact**: Slow shard processing delays entire iteration
- **Memory Constraints**: Model must still fit on each worker
- **Mitigations**:
  - Gradient compression techniques
  - Asynchronous updates (trade accuracy for speed)
  - Overlap computation/communication
  - Adaptive batch size scheduling