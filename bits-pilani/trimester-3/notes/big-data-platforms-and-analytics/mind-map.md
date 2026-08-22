# Big Data Platforms & Analytics — Revision Mind Map

> Everything important, in acronyms and one-liners. Pair with the course module summaries and exam patterns.

## Big Data & Scaling

```
BIG DATA = 3Vs: Volume (size) × Velocity (speed) × Variety (types)
```

- **Vertical scaling (scale up)** — bigger box (more CPU/RAM); hits a wall (cost, hardware limits)
- **Horizontal scaling (scale out)** — many commodity machines in a cluster; the big-data answer
- **Cluster computing** — economics of commodity hardware: cheap, parallel, fault-tolerant
- **Constraints** — CPU, RAM, I/O; bigger boxes eventually fail → must scale out

## Distributed Systems

- **Fallacies of distributed computing** — assume network is reliable, latency is zero, bandwidth infinite, etc. (all false)
- **CAP Theorem** — pick **2 of 3**: Consistency, Availability, Partition Tolerance

```
During a partition:  C ↑ ⟹ A ↓   OR   A ↑ ⟹ C ↓
P is MANDATORY in clusters → real choice is CP vs AP
```

- **C** = every read sees latest write or error (correctness) · **A** = always respond, possibly stale (uptime) · **P** = works during network partition (resilience)
- **CP** — banking, inventory · **AP** — social media, analytics · **CA** — single-node only
- **ACID** — Atomicity, Consistency, Isolation, Durability (relational DBs)
- **BASE** — Basically Available, Soft state, Eventual consistency (distributed/NoSQL)
- **Conflict resolution** — last-write-wins, version vectors, merges (in eventually-consistent systems)

## MapReduce & Hadoop

- **MapReduce** — map (transform each record) → **shuffle & sort** (bridge) → reduce (aggregate)

```
MAP:  (k1,v1) → list(k2,v2)
SHUFFLE/SORT: group by key
REDUCE: (k2, list(v2)) → list(k3,v3)
```

- **HDFS** — files split into **blocks** (128 MB default), **replicated** (default 3×), **rack-aware** placement for fault tolerance
- **Hadoop bottleneck** — every map/reduce intermediate result written to **disk** (materialisation) → high I/O latency
- **MapReduce fault tolerance** — failed tasks **re-run** from input splits (stateless)

## Spark: In-Memory Batch

- **Key shift** — Hadoop = disk-bound; **Spark = in-memory** primary workspace → 10–100× faster for iterative jobs
- **RDD** — **Resilient Distributed Dataset**; immutable, partitioned, distributed; resilience via **lineage** (recompute), not replication
- **DAG** — directed acyclic graph of transformations; **lazy evaluation** (nothing runs until an action)
- **Transformations vs Actions** — transform = build plan (map, filter, flatMap); action = trigger run (count, collect, save)

| Dependency | Meaning | Recovery |
|------------|---------|----------|
| **Narrow** | One parent → one child (map, filter) | Fast, local, isolated |
| **Wide** | Many parents → many children (groupByKey, join) | Needs **shuffle**, expensive |

- **Execution** — DAG broken into **stages** (wide deps) → **tasks** (per partition); one partition = one task
- **Shuffle** — data movement across nodes; the performance killer in joins/grouping
- **Caching vs Checkpointing** — cache = keep in memory (fast, lost on failure); checkpoint = truncate lineage to **reliable storage** (HDFS/S3), breaks deep-DAG stack-overflow risk

## Partitioning & Optimisation

- **Partitioning = parallelism** (split data) vs **Replication = fault tolerance** (copies) — different problems!
- **Hash partitioning** — $P = \text{hash}(\text{key}) \mod N$; deterministic, uniform, great for point lookups/joins; breaks on **skewed keys** (nulls, low-cardinality)
- **Range partitioning** — ordered key ranges; great for analytics (dates, alphabetical); boundary issues as ranges shift
- **Custom partitioning** — manual override for real-world skew
- **Data skew / hotspots** — one partition gets 90% → **straggler** (overloaded node, idle others)
- **Salting** — add random suffix to skewed keys to break them across partitions, then aggregate
- **Broadcast join** — send small table to all nodes; **eliminates shuffle** for asymmetric joins
- **Data co-location** — partition both tables by the same key so joins are shuffle-free

## Distributed ML

- **Communication overhead** — data movement between workers dominates; stragglers slow sync convergence
- **Data parallelism** — shard the **dataset** across workers (each has full model copy)
- **Model parallelism** — split the **network** across devices (each holds a slice)
- **SGD** — stochastic gradient descent; the optimisation engine; distributed via **push-update-pull**

```
Push gradients → update parameters → pull new weights
```

- **Sync vs async aggregation** — sync (barrier; consistent but straggler-bound) vs async (fast but stale gradients) vs local SGD
- **Parameter server** — centralised weight store (sparse models, embeddings)
- **Ring all-reduce** — decentralised, bandwidth-optimal (dense models, CV/NLP)
- **TensorFlow strategies** — **MirroredStrategy** (single node, multi-GPU, NCCL) vs **MultiWorkerMirroredStrategy** (multi-node, needs `TF_CONFIG`)

## Stream Processing

- **Shift** — batch ("what happened yesterday?") → stream ("what is happening now?")
- **Stream pillars** — low latency (ms–s), **unbounded** data, **actionability**
- **Windowing** — tumbling (fixed non-overlap), sliding (fixed overlap), session (activity-based gaps)
- **Global state** — persistent accumulators, user context, online ML updates
- **Kafka** — durable, fault-tolerant **event log** backbone (NOT a message queue — messages persist, replayable)

| Kafka concept | Meaning |
|---------------|---------|
| **Topic** | Named feed of messages |
| **Partition** | Ordered, immutable sequence in a topic |
| **Offset** | Position within a partition |
| **Broker** | Server storing partitions |
| **Consumer group** | Consumers jointly reading a topic |

- **Kafka decouples** producers from consumers — write once, many consumers, replay from any offset; replication factor ≥ 3
- **Storm** — real-time **topology** of **spouts** (sources) + **bolts** (processing); ultra-low latency
- **One partition = one task** — balanced alignment = peak performance; imbalance = stragglers

## Formula Cheat Sheet

| Formula | Expression |
|---------|-----------|
| Hash partitioning | $P = \text{hash}(\text{key}) \mod N$ |
| CAP trade-off | During partition: $C \uparrow \Rightarrow A \downarrow$ (or vice versa) |
| Kafka replication | factor ≥ 3 |
