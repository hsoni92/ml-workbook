# Week 8 – Checkpointing & Lineage Management (Module 8)

## Module Introduction

This module explores the **tipping point** where Spark's powerful lineage mechanism becomes a liability, and introduces **checkpointing** as the solution for stability in long-running pipelines.

---

## 1. When Lineage Becomes a Liability

### The Problem: Deep Lineage Chains
- **Linear Cost Increase**: Recovery time ∝ DAG depth (N stages)
- **Driver Bottleneck**: Metadata (lineage graph) grows with every transformation
- **Reliability Paradox**: Longer pipeline = more failure points + more expensive recovery

### Real-World Scenario
```
Stage 1 → Stage 2 → ... → Stage 37
```
If partition fails at Stage 37, Spark may need to recompute 36 previous stages.

---

## 2. Stack Overflow & Performance Degradation

### Stack Overflow Error
- **Root Cause**: RDD serialization is recursive (RDD → parent → parent...)
- **JVM Stack Limit**: Exceeded at ~100+ recursive lineage depth
- **Common In**: Iterative algorithms (PageRank, ALS, K-Means)

### Performance Degradation (Even Without Crash)
- **Driver CPU Overhead**: Spends more time traversing lineage than scheduling tasks
- **Recovery Latency Spikes**: Task failure turns into minutes/hours of recomputation
- **Memory Pressure**: Driver OOM from thousands of lineage metadata objects

---

## 3. Breaking the Family Tree: Checkpointing

### How Checkpointing Works
1. **Eager Operation**: Immediately triggers background write job
2. **Physical Save**: Writes RDD partitions to HDFS/S3
3. **Lineage Truncation**: **Removes all parent references** from checkpointed RDD
4. **New Leaf Node**: Checkpointed RDD becomes fresh starting point
5. **GC Cleanup**: Old parent RDDs become eligible for garbage collection

### Visual Effect
```
Before:  A → B → C → D → E (E knows about A,B,C,D)
After:   [Checkpoint] E' (E' has NO parents, is new leaf)
```

### Recovery Benefit
- **Without Checkpointing**: Failure at stage 100 = replay 100 stages
- **With Checkpointing**: Failure at stage 100 = replay from last checkpoint (e.g., 10 stages)

---

## 4. Caching vs Checkpointing: Critical Differences

| Aspect | Caching (`persist()`) | Checkpointing (`checkpoint()`) |
|--------|----------------------|--------------------------------|
| **Lineage** | **Preserved** – RDD keeps full history | **Truncated** – History wiped, new leaf node |
| **Storage** | Memory / Local Disk (fast, session-bound) | HDFS / S3 (durable, session-independent) |
| **Reliability** | Lost if executor fails | Fault-tolerant (distributed storage) |
| **Persistence** | Session-scoped | Survives session/cluter restarts |
| **Trigger** | Lazy (on first Action) | **Eager** (immediate background job) |
| **Recovery** | Recompute from source | Read from checkpoint file |
| **Best For** | Short pipelines, frequent reuse | Long iterative pipelines, stability |

### Decision Matrix
```
IF pipeline is short & data reused often → CACHE
IF pipeline is long/iterative (ML, graph) → CHECKPOINT
IF need both speed AND durability → CACHE + CHECKPOINT
```

---

## 5. Checkpoint Storage Backends

### HDFS (On-Premise)
```python
sc.setCheckpointDir("hdfs://namenode:9000/checkpoints")
```
- **Pros**: Low latency (co-located with workers), high throughput
- **Cons**: Tied to cluster lifecycle, manual management

### S3 / Object Stores (Cloud-Native)
```python
sc.setCheckpointDir("s3a://my-bucket/spark-checkpoints")
```
- **Pros**: Decoupled from compute lifecycle, extreme durability, unlimited scale
- **Cons**: Slightly higher write latency (network hop)

### Mandatory Setup
```python
# MUST configure BEFORE calling checkpoint()
sc.setCheckpointDir("hdfs:///checkpoints")  # or s3://...
rdd.checkpoint()  # Now works
```

---

## 6. Internal Mechanics: DAG Truncation

### Step-by-Step Process
1. **Mark for Checkpointing**: `rdd.checkpoint()` sets internal flag
2. **Background Job Launched**: Eager execution to materialize RDD
3. **Write to Storage**: Partitions saved to configured checkpoint directory
4. **Create ReliableRDD**: New RDD subclass pointing to checkpoint files
5. **Sever Lineage**: `rdd.dependencies = []` (clears parent references)
6. **Update Depth**: `rdd.depth = 0` (becomes leaf node)
7. **Garbage Collection**: Old parent RDDs freed from driver memory

### Memory Impact
- **Before**: Driver holds O(N) metadata objects for N stages
- **After**: Driver holds O(1) for checkpointed section
- **Result**: Prevents driver OOM in long-running jobs

---

## 7. Trade-off Analysis: Recomputation vs I/O

### Cost Model
```
Total Cost = Checkpoint I/O Cost + Expected Recovery Cost
```

### Visual Analysis
```
Recovery Time
    │
    │        Red: No Checkpointing (Linear growth)
    │       /
    │      /
    │     /  Blue: With Checkpoints (Flat after each checkpoint)
    │    /______
    │   /|    |
    │  / |    |
    │ /  |    |
    └───┴────┴─── Lineage Depth (N)
        ↑    ↑
       CP1  CP2
```

### The Tipping Point
- **Small N**: Checkpoint overhead > recovery cost
- **Large N**: Recovery cost > checkpoint overhead
- **Rule of Thumb**: Checkpoint every **10-20 iterations** in iterative algorithms

### Decision Framework
| Scenario | Checkpoint Frequency |
|----------|---------------------|
| Iterative ML (PageRank, ALS) | Every 5-10 iterations |
| Graph Processing | Every 10 iterations |
| Long ETL Pipeline (>50 stages) | Every 15-20 stages |
| Streaming (micro-batch) | Every N micro-batches |
| Ad-hoc Analytics | Usually unnecessary |

### Insurance Analogy
> "You're buying insurance against failure. The more expensive the recomputation, the higher the I/O premium you should pay."

---

## 8. Module Summary

### Core Concepts
| Concept | Key Insight |
|---------|-------------|
| **Lineage Liability** | Deep DAGs cause driver OOM, stack overflow, slow recovery |
| **Checkpointing** | Eager I/O that truncates DAG, creates new leaf node |
| **Caching ≠ Checkpointing** | Cache for speed (preserves lineage), Checkpoint for stability (breaks lineage) |
| **Storage Backends** | HDFS (on-prem speed), S3 (cloud durability) |
| **Internal Effect** | Severed dependencies → GC cleanup → driver memory relief |
| **Cost Trade-off** | Fixed I/O cost vs. linear recovery cost |

### Production Patterns
```python
# 1. Configure early
sc.setCheckpointDir("s3://bucket/checkpoints")

# 2. In iterative loop
for i in range(100):
    rdd = rdd.map(iteration_logic)
    if i % 10 == 0:  # Checkpoint every 10 iterations
        rdd.checkpoint()

# 3. Final action
result = rdd.collect()
```

### Strategic Takeaway
> **Checkpointing transforms unbounded linear recovery risk into bounded, constant-time recovery.** It's not optional for production iterative workloads – it's the difference between a job that completes and one that crashes at hour 47 of a 50-hour run.