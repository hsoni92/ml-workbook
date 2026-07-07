# Week 7 – Resilience & Fault Tolerance (Module 7)

## Module Introduction

This module explores Spark's revolutionary approach to fault tolerance: **lineage-based recomputation** instead of traditional **data replication**.

### Core Insight
> Spark achieves 100× speed advantage over Hadoop by avoiding the 3× replication penalty while maintaining full fault tolerance through deterministic recomputation.

---

## 1. Why Resilience Matters in Big Data

### The Problem Space
- **1000+ node clusters**: Hardware failure is a daily statistical certainty
- **Network partitions**: Transient outages can isolate data mid-computation
- **Distributed Memory (RAM)**: Unlike HDFS's disk storage, Spark's in-memory data is instantly lost on node failure
- **Multi-hour jobs**: Cannot afford to restart from scratch on every hiccup

### The Imperative
> "Cluster failure is not an option. We need a system that can heal itself on the fly."

---

## 2. The Two Recovery Paradigms

### Replication-Based (Traditional: HDFS, MapReduce)
| Aspect | Details |
|--------|---------|
| **Strategy** | Copy data to 3 nodes |
| **Storage Cost** | 3× (or more) raw data size |
| **Network Cost** | Massive bandwidth for replica sync |
| **Recovery Speed** | Near-instant (switch to replica) |
| **Scalability** | Poor – footprint grows with data size |

### Lineage-Based (Spark)
| Aspect | Details |
|--------|---------|
| **Strategy** | Store DAG "recipe" of how to recreate data |
| **Storage Cost** | O(1) – only kilobytes of metadata |
| **Network Cost** | Minimal – only during recovery |
| **Recovery Speed** | Depends on DAG depth |
| **Scalability** | Excellent – footprint grows with logic complexity, not data volume |

---

## 3. The Three Pillars of Lineage Reliability

### 1. Immutability
- RDDs are read-only snapshots – never change after creation
- Each transformation produces a new RDD
- No worry about data changing midstream

### 2. Ancestry
- Every RDD maintains reference to its parent RDD(s)
- Creates chain of custody back to source data
- Enables precise identification of what to recompute

### 3. Determinism
- Same code + same input = identical output, always
- Pure functions without side effects
- Guarantees replay produces correct data

---

## 4. Anatomy of a Lineage Graph

### Mathematical Model
**Recovery Cost = Σ(time to execute each operation in partition's history)**

- **N** = number of transformation steps in lineage chain
- **Short lineage** (e.g., single filter = near-instant recovery
- **Long lineage** = recovery time proportional to graph depth

### Structure
- **Leaf Nodes**: Base RDDs from source data (HDFS, S3, local files)
- **Intermediate Nodes**: Transformation results
- **Edges**: Dependencies (narrow = 1-to-1, wide = many-to-many)

---

## 5. Lineage Walkthrough: Sales Analysis Example

### Scenario
Calculate total sales amount per category from `sales.csv` (transaction_id, product_id, amount) and `products.csv` (product_id, category).

### Spark Pipeline
```python
# 1. Ingest (leaf RDDs)
sales = sc.textFile("sales.csv")  # RDD_A1
products = sc.textFile("products.csv")  # RDD_B1

# 2. Parse (narrow: map)
sales_kv = sales.map(parse_sales)    # narrow
prod_kv = products.map(parse_product) # narrow

# 3. Join by product_id (wide: shuffle)
joined = sales_kv.join(prod_kv)  # WIDE DEPENDENCY

# 4. Reshape (narrow: map)
reshaped = joined.map(to_category_amount)  # narrow

# 5. Aggregate (wide: reduceByKey)
result = reshaped.reduceByKey(lambda a,b: a+b)  # WIDE DEPENDENCY

# 6. Save
result.saveAsTextFile("output/")
```

### Dependency Classification
| Step | Operation | Dependency | Why |
|------|-----------|------------|-----|
| 1 | `textFile` | Leaf | Source data |
| 2 | `map(parse)` | Narrow | 1 input row → 1 output row |
| 3 | `join` | **Wide** | Must bring same keys together |
| 4 | `map(reshape)` | Narrow | Local tuple transformation |
| 5 | `reduceByKey` | **Wide** | Group by category for sum |
| 6 | `saveAsTextFile` | Action | Triggers execution |

---

## 6. Recovery in Narrow Dependencies (1-to-1)

### Scenario
Lost node holding partition **C2**. Lineage shows C2 derived solely from parent **P2**.

### Recovery Process
1. Driver consults lineage: C2 ← P2
2. Schedules recomputation of P2 → C2 on healthy executor
3. No other partitions touched
4. No network data movement required

### Advantages
- **Isolation**: Failure contained to single partition
- **Local**: Zero network shuffle
- **Speed**: Extremely low recovery cost

### Design Implication
> Chain narrow transformations together to make pipelines resilient.

---

## 7. Recovery in Wide Dependencies (Shuffle-Heavy)

### Scenario
Lost partition **C2** from `reduceByKey`/`join` output. C2 depends on **P1, P2, P3** from multiple parents.

### Recovery Complexity: Cascading Recovery
1. C2 needs data from P1, P2, P3
2. If parents not in memory, must recompute them first
3. Failure **cascades** upstream through shuffle boundary
4. Often requires re-executing **entire preceding stage**

### The Shuffle Interruption Problem
- Shuffles move massive data across network
- Mid-shuffle failure often means **full stage re-execution**
- Expensive recovery cost

### Mitigation: Checkpointing
```python
rdd.checkpoint()  # Saves to disk, truncates lineage
```

### Trade-off
| Checkpointing | Without Checkpointing |
|---------------|----------------------|
| Saves state to disk | Pure in-memory lineage |
| Breaks lineage chain | Long lineage → slow recovery |
| I/O cost during execution | Zero I/O until failure |
| Prevents cascading failures | Risk of full-job restart |

---

## 8. Demo: Triggering Recomputation in PySpark

### Key Concepts
- **Deterministic transformations**: Guarantee identical replay
- **Lazy evaluation**: Lineage built at transformation time
- **Action triggering**: Only at action does computation occur
- **Partition-level granularity**: Recovery at partition level, not RDD level

### PySpark Example
```python
# Build lineage
rdd = sc.textFile("logs/*.log")
clean = rdd.filter(valid_log)
parsed = clean.map(parse_line)
enriched = parsed.join(lookup_table)

# Checkpoint before expensive operation
enriched.checkpoint()  # Truncates lineage

# Final action
enriched.saveAsTextFile("output/")

# Simulate failure recovery:
# 1. Kill executor process
# 2. Spark driver detects missing partition
# 3. Recomputes from last checkpoint or source
# 4. Continues without full restart
```

---

## 9. Module Summary & Key Takeaways

### Core Architectural Shift
| Traditional (Replication) | Spark (Lineage) |
|---------------------------|-----------------|
| 3× storage overhead | Minimal metadata |
| Instant recovery | Computed recovery |
| Disk-bound | Memory-optimized |
| Bandwidth heavy | CPU-bound recovery |

### Design Principles for Resilient Spark Jobs
1. **Minimize Wide Dependencies**: Reduce shuffle boundaries
2. **Use Checkpointing Strategically**: Break long lineages
3. **Prefer Narrow Transformations**: `filter`, `map` over `groupBy`, `join` where possible
4. **Understand Recovery Cost**: DAG depth = recovery time
5. **Monitor Executor Health**: Proactive failure detection

### Performance vs Resilience Balance
- **Development Phase**: Full lineage (no checkpointing)
- **Production Phase**: Strategic checkpoints on long pipelines
- **Critical Jobs**: More frequent checkpoints
- **Iterative Algorithms**: Checkpoint every N iterations

---

## Strategic Insight
> **Spark's resilience is not about preventing failures – it's about making failure recovery deterministic, fast, and transparent.** The lineage graph is the "recipe" that makes this possible, turning volatile RAM into reliable computation.

---

## What's Next: Module 8

Next module will explore **Data Partitioning & Skew Handling** – how to distribute work evenly across executors, handle data skew, and optimize join strategies for production-scale workloads.