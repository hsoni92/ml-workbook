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
- **Short lineage** (e.g., single filter) = near-instant recovery
- **Long lineage** = recovery time proportional to graph depth

### Structure
- **Leaf Nodes**: Base RDDs from source data (HDFS, S3, etc.)
- **Intermediate Nodes**: Transformations (map, filter, join, etc.)
- **Root Nodes**: Final result RDDs

---

## 5. Lineage Walkthrough: Sales Analysis Example

### Scenario
Calculate total sales amount per category from:
- `sales.csv` (tracking_id, product_id, amount)
- `products.csv` (product_id, category)

### Lineage Graph Construction
```
Step 1: Ingest Data → Base RDDs (leaf nodes)
  RDDA1 ← sales.csv
  RDDB1 ← products.csv

Step 2: Parse CSV (narrow dependency - 1:1 mapping)
  RDDA2 ← RDDA1.map(parse_csv)
  RDDB2 ← RDDB1.map(parse_csv)

Step 3: Join by Key (WIDE DEPENDENCY - shuffle required)
  RDD_joined ← RDDA2.join(RDDB2)  // Wide dependency!

Step 4: Reshape Tuple (narrow dependency)
  RDD_reshaped ← RDD_joined.map(reshape_to_category_amount)

Step 5: Aggregate by Category (WIDE DEPENDENCY - shuffle)
  RDD_result ← RDD_reshaped.reduceByKey(sum_amounts)

Step 5: Save Output
  RDD_result.saveAsTextFile("output/")
```

### Dependency Classification
| Operation | Dependency Type | Reason |
|-----------|----------------|--------|
| `map(parse_csv)` | Narrow | 1:1 partition mapping, no data movement |
| `join()` | **Wide** | Shuffle to bring same keys together |
| `reshape_to_category_amount` | Narrow | Local transformation on shuffled data |
| `reduceByKey(sum)` | **Wide** | Shuffle to group by new key (category) |

---

## 6. Narrow Dependency Recovery (Fast Path)

### Characteristics
- **1:1 mapping**: Each parent partition maps to exactly one child partition
- **Operations**: `map`, `filter`, `flatMap`, `mapPartitions`

### Recovery Advantages
1. **Isolation**: To restore lost partition C2, only rerun transformation on parent P2
2. **No Shuffle**: No network data movement between nodes during recovery
3. **Local Recovery**: Spark schedules task to recompute P2 on healthy executor
4. **Contained Failure**: Other partitions (P1, P3, C1, C3) completely unaffected

### Design Principle
> Chain as many narrow transformations together as possible – keeps recovery cost extremely low.

---

## 7. Wide Dependency Recovery (Complex Path)

### Characteristics
- **Many-to-many mapping**: Child partition contains data from multiple parent partitions
- **Operations**: `groupByKey`, `reduceByKey`, `join`, `repartition`, `coalesce`

### Recovery Challenges
1. **Cascading Recovery**: Lost partition C2 requires data from P1, P2, P3
2. **Shuffle Interruption**: If parents not in memory, must recompute entire upstream stage
3. **Expensive**: Shuffles are the most expensive part of Spark jobs

### Mitigation: Checkpointing
- **Purpose**: Truncate lineage by saving intermediate state to reliable storage (HDFS/S3)
- **Effect**: Creates "save point" – failure only rolls back to last checkpoint
- **Trade-off**: Extra I/O cost during execution for bounded recovery time

---

## 8. Demo: Triggering Recomputation in PySpark

### Forcing Lineage Materialization
```python
# Create lineage
rdd = sc.textFile("logs/*.log")
filtered = rdd.filter(lambda l: "ERROR" in l)
mapped = filtered.map(extract_user)
count = mapped.count()  # Action triggers execution

# Force checkpoint (writes to HDFS/S3)
mapped.checkpoint()  # Requires sc.setCheckpointDir()
```

### Observing Recovery
- Kill an executor process
- Spark automatically schedules recomputation of lost partitions
- Driver uses lineage graph to determine what to rerun
- No data loss – deterministic replay guarantees correctness

---

## 9. Module Summary

### Key Takeaways

| Concept | Insight |
|---------|---------|
| **Lineage vs Replication** | Metadata (KB) vs Data (TB) – massive storage savings |
| **Three Pillars** | Immutability + Ancestry + Determinism = Reliable Recovery |
| **Recovery Cost** | Proportional to DAG depth (N steps) |
| **Narrow Dependencies** | Fast, isolated, no-shuffle recovery |
| **Wide Dependencies** | Expensive, cascading, mitigated by checkpointing |
| **Checkpointing** | Eager I/O operation that truncates DAG for stability |

### Design Principles
1. **Prefer narrow transformations** – chain them for performance and fast recovery
2. **Strategic checkpointing** – every 10-20 iterations for iterative algorithms
3. **Monitor lineage depth** – deep DAGs signal recovery risk
4. **Understand shuffle boundaries** – wide transformations are where failures hurt most

### The Big Picture
> Spark's lineage graph is a "logical roadmap" that turns volatile RAM into a resilient, recoverable computing platform. By storing recipes instead of copies, Spark achieves both speed AND reliability – the fundamental breakthrough enabling production big data analytics.