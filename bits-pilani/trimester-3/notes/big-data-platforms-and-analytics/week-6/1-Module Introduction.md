# Week 6 – Spark Execution Engine Deep Dive

## Module Introduction

This module covers Spark's execution model, focusing on how high-level transformations become optimized distributed tasks.

### Key Components
1. **Driver Program** - Hosts SparkContext, builds DAG, orchestrates job
2. **Cluster Manager** - Allocates CPU/RAM resources (YARN, Mesos, Standalone, Kubernetes)
3. **Executors** - Worker processes on nodes that execute tasks, cache data, report results

---

## 1. Lazy Evaluation: Why Spark Waits

### Core Principle
> Transformations are recorded but not executed until an Action is called.

### Benefits
- **Optimization**: Spark analyzes entire transformation chain before execution
- **Pipeline Efficiency**: Multiple narrow transformations combined into single stage
- **Fault Tolerance**: Lost data recomputed from lineage
- **Cost Reduction**: Avoids unnecessary computation if result not needed

### Example
```python
# Transformations (recorded, NOT executed)
rdd = sc.textFile("logs/*.log")
filtered = rdd.filter(lambda l: "ERROR" in l)
mapped = filtered.map(lambda l: extract_user(l))

# ACTION triggers execution
error_count = mapped.count()
```

---

## 2. Transformation Types: Narrow vs Wide

### Narrow Transformations
- **Definition**: One parent partition → one child partition
- **No network shuffle**
- **Examples**: `map()`, `filter()`, `flatMap()`, `mapPartitions()`
- **Performance**: Fast, local processing

### Wide Transformations
- **Definition**: Data from many partitions contributes to single output partition
- **Requires network shuffle**
- **Examples**: `groupByKey()`, `reduceByKey()`, `join()`, `repartition()`, `coalesce()`
- **Performance**: Expensive, network-bound

---

## 3. DAG and Stage Decomposition

### DAG (Directed Acyclic Graph)
- Represents complete logical flow of transformations
- Prevents cycles (no feedback loops)
- Built before any execution

### Stage Boundaries
- Created at **shuffle boundaries** (wide transformations)
- Each stage = set of narrow transformations that can be pipelined
- **Stage** = logical unit of work between shuffles

### Task Execution
- **Task** = smallest unit of parallel work (one partition)
- Multiple tasks per stage run in parallel on executors
- Executors reuse JVM across multiple tasks

---

## 4. Fault Recovery Mechanisms

### Lineage-Based Recovery
- Every RDD knows how it was created
- Failed task recomputed from parent partitions
- No checkpointing needed by default

### Narrow Dependency Recovery
- **Fast**: Only recompute affected partition
- **Local**: No network data movement
- **Isolated**: Other partitions unaffected

### Wide Dependency Recovery
- **Expensive**: Must recompute entire upstream stage
- **Shuffle Re-execution**: All parent partitions needed
- **Mitigation**: Checkpointing breaks lineage, provides save points

---

## 5. Performance Optimization Strategies

### Minimize Wide Transformations
- Prefer `reduceByKey()` over `groupByKey()`
- Use `combineByKey()` for complex aggregations
- Broadcast joins for small datasets

### Partition Management
- Target 2-4 partitions per executor core
- Use `coalesce()` instead of `repartition()` when reducing partitions
- Avoid extremely small/large partitions

### Caching Strategy
```python
rdd.persist(StorageLevel.MEMORY_AND_DISK)  # Reuse expensive computations
rdd.unpersist()  # Free memory when done
```

---

## Summary

| Concept | Key Insight |
|---------|-------------|
| **Lazy Evaluation** | Strategic delay enables optimization |
| **DAG Scheduler** | Converts logical plan to physical stages |
| **Narrow vs Wide** | Determines shuffle boundaries and cost |
| **Stage Boundaries** | Created at wide transformation boundaries |
| **Fault Tolerance** | Lineage enables recomputation without checkpoints |
| **Narrow Recovery** | Fast, local, isolated |
| **Wide Recovery** | Expensive, cascading, mitigated by checkpointing |

---

## Next Steps
Module 7 will explore Resilience & Fault Tolerance in depth, covering checkpointing strategies, lineage graphs, and production-ready recovery patterns.