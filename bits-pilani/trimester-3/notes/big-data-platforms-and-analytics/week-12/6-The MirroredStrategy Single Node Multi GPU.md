# The MirroredStrategy – Single-Node Multi-GPU Training (Week 12 – TensorFlow Distributed Strategies)

## Learning Objectives
By the end of this lesson you will be able to:
- Explain the purpose and scope of TensorFlow's `MirroredStrategy` API
- Describe how model variables are mirrored across GPUs on a single machine
- Outline the execution flow: data split → local forward/backward → gradient aggregation → synchronous update
- Identify the communication backend (NCCL) that makes intra-node scaling efficient
- Determine when `MirroredStrategy` is the appropriate choice vs. multi-worker strategies

## Core Concept: Synchronous Data Parallelism on One Machine
`MirroredStrategy` is TensorFlow's **entry-level distributed training strategy** for a single host equipped with multiple GPUs (2–8). It implements **synchronous data parallelism**:
- Each GPU gets a **replica** of the full model (variables are *mirrored*).
- The input batch is **split evenly** across replicas.
- Each replica computes **local gradients** on its shard.
- Gradients are **aggregated (all-reduce)** across all GPUs.
- The **same updated parameters** are written back to every replica, keeping the model perfectly in sync.

## Execution Flow (Per Training Step)
```
1. Data Batch
      │
      ▼
┌─────┴─────┐          ┌─────────────┐
│ Split     │──► GPU 0 │ Forward/Back│
│ Evenly    │          │ Local Grad  │
│           │          └──────┬──────┘
│           │                 │
│           ▼                 ▼
│      ┌────┴────┐      ┌────┴────┐
│      │ GPU 1   │ ...  │ GPU N   │
│      │ Forward │      │ Forward │
│      │ Backward│      │ Backward│
│      └────┬────┘      └────┬────┘
└───────────┼────────────────┼───────────
            ▼                ▼
      ┌─────┴─────┐    ┌─────┴─────┐
      │ All-Reduce│    │ (NCCL)    │
      │ Sum/Mean  │◄───│ High-Speed│
      │ Gradients │    │ GPU Link  │
      └─────┬─────┘    └─────┬─────┘
            │                │
            ▼                ▼
      ┌─────┴─────┐    ┌─────┴─────┐
      │ Apply     │    │ Apply     │
      │ Identical │    │ Identical │
      │ Update    │    │ Update    │
      └───────────┘    └───────────┘
```

## Key Characteristics
| Attribute | Detail |
|-----------|--------|
| **Topology** | Single host, 2–8 GPUs (NVLink / PCIe) |
| **Communication** | NVIDIA NCCL (optimized collective ops) |
| **Synchronization** | Synchronous (all GPUs wait at all-reduce) |
| **Model Replication** | Full copy on each GPU (mirrored variables) |
| **Batch Scaling** | Global batch = per-GPU batch × #GPUs |
| **Code Changes** | Minimal – wrap model creation in `strategy.scope()` |

## Typical Usage Pattern
```python
import tensorflow as tf

strategy = tf.distribute.MirroredStrategy()
print(f"Number of devices: {strategy.num_replicas_in_sync}")

with strategy.scope():
    model = create_model()          # Variables created inside scope are mirrored
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

model.fit(train_dataset, epochs=10, batch_size=global_batch_size)
```

## Performance Considerations
- **NCCL** leverages NVLink / PCIe for **tens of GB/s** intra-node bandwidth.
- **Synchronous barrier** means the slowest GPU dictates step time → keep GPUs balanced.
- **Batch size** should be scaled up (linear scaling rule) to maintain convergence.
- **Memory**: Each GPU holds a full model copy → model must fit in *single-GPU* memory.

## When to Use MirroredStrategy
✅ **Ideal for**:
- Single workstation / cloud instance with 2–8 GPUs
- Models that fit in one GPU's memory
- Quick scaling with minimal code changes
- Prototyping before moving to multi-node

❌ **Not suitable for**:
- Models exceeding single-GPU memory (need model parallelism / `MultiWorkerMirroredStrategy` with sharding)
- Clusters spanning multiple machines (use `MultiWorkerMirroredStrategy`)
- Asynchronous training requirements

## Summary
`MirroredStrategy` provides **zero-effort synchronous data parallelism** on a single multi-GPU node. By mirroring variables and using NCCL for ultra-fast all-reduce, it delivers near-linear scaling for a wide range of models—making it the default first step when moving from one GPU to many on the same machine.

*Next lesson: scaling beyond one machine with `MultiWorkerMirroredStrategy`.*