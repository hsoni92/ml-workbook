# Sample Question Paper

## BITS Digital Comprehensive Test

| Field | Value |
|-------|-------|
| Course No. | |
| Course Title | Big Data Platforms and Analytics |
| Nature of Exam | Closed Book (No Internet) |
| Weightage | 40% |
| Duration | 2.5 Hours |
| Date of Exam | |

### Note to Students

1. Please follow all the Instructions to Candidates given on the cover page of the answer book.
2. Read each question carefully and write to-the-point answer.
3. All parts of a question should be answered consecutively. Each answer should start from a fresh page.
4. Assumptions made if any, should be stated clearly at the beginning of your answer.
5. Show all the calculations/derivations in fair and box/highlight the final answer.

---

## Scenario Context

You are the **Principal Big Data Architect** for a global e-commerce enterprise processing over **500 million user interaction events** (clicks, searches, cart additions, purchases) per day. You are tasked with designing and optimizing a scalable data platform to compute **real-time product recommendations** and analyze **historical purchasing behavior** across global regions.

> *Assume a data model and create a sample mock data, or feel free to download sample e-commerce data from any open-source data provider.*

---

## Q.1

### Q.1.1 — Vertical vs. Horizontal Scaling for Clickstreams (5 Marks)

The enterprise's legacy clickstream analytics engine relies on a high-end vertically scaled (Scale-Up) database server. Explain the **physical hardware limitations** (e.g., memory wall, bus bandwidth, power/thermal constraints) and **economic constraints** that make vertical scaling unsustainable for high-velocity web clickstreams. Justify why transitioning to a horizontally scaled commodity cluster (Scale-Out) is necessary for this platform, linking your reasoning to the **Volume** and **Velocity** dimensions of Big Data.

#### Answer

**Vertical scaling (scale up)** means making a single existing machine more powerful — more RAM, faster CPU, larger disk — while the software stack stays unchanged. The course frames it as "buying a bigger and bigger truck." It hits **three walls** that make it unsustainable for clickstreams:

| Wall | Physical / economic basis | Why clickstreams break it |
|------|---------------------------|---------------------------|
| **Price wall** | Cost rises **exponentially**, not linearly (e.g., 16 GB → 32 GB RAM is modest, but high-performance 1 TB → 2 TB RAM costs \$20,000+). | 500 M events/day needs terabyte-scale RAM + fast disks; the top tier of every component costs a fortune. |
| **Hardware wall** | Motherboards have finite CPU sockets and RAM DIMM slots; memory **bus bandwidth** and **power/thermal** ceilings limit throughput per box. Once every slot is filled, you must replace the entire machine. | A single server's memory bandwidth and I/O bus physically cannot ingest 500 M events/day at low latency. |
| **Risk wall** | One super-server = **single point of failure**; if it fails, the business stops. | Clickstream analytics is always-on; an outage at peak sales loses revenue. |

**Economic constraint:** vertical cost is **exponential** while the data grows **linearly** — the two curves cross quickly. For the 3Vs, **Volume** (petabytes of events) exceeds any single box's memory/disk, and **Velocity** (continuous high-rate ingestion) saturates a single machine's CPU, bus, and network pipe.

**Transition to horizontal scaling (scale out)** — a cluster of standard **commodity nodes**:

- **Linear cost** — $\text{total cluster cost} \approx n \times \text{cost per commodity node}$; when data doubles, cost roughly doubles instead of exploding.
- **Fault tolerance** — if one of 100 nodes fails, the other 99 keep serving; frameworks (Hadoop/Spark) detect the dead node and **reassign its work** to survivors.
- **Effectively unlimited growth** — add nodes, not a bigger box; matches unbounded clickstream Volume and Velocity.

**Assumption:** the "legacy engine" is a single RDBMS-style server with no built-in distribution, so scale-up is the only option it offers today.

**Pro tip:** The mark skeleton is the **three walls (price, hardware, risk)** + the **cost-curve contrast (exponential vs linear)** + the **3Vs link**. Name at least one *physical* limit explicitly (memory wall, bus bandwidth, power/thermal — the question lists them, so tick each off). Always close with the fault-tolerance point — that is the operational reason scale-out wins, not just cost. If asked "when is vertical still right?", say small/bounded workloads, short-term fixes, and low-availability requirements.

---

### Q.1.2 — ACID vs BASE and the CAP Theorem (5 Marks)

For core user checkout transactions and account balances, the platform enforces an **ACID** consistency model. However, for the clickstream analytics and product recommendation engine, you propose a **BASE** model. Contrast the **ACID** and **BASE** models. Using the **CAP Theorem**, explain why adopting a BASE model is acceptable and more performant for the recommendation engine workload.

#### Answer

**ACID** (relational databases) and **BASE** (distributed systems) are two consistency philosophies:

| Dimension | ACID | BASE |
|-----------|------|------|
| Priority | **Accuracy** — the truth must be exact | **Scalability & availability** |
| Consistency | Immediate, strict | **Eventually** consistent |
| During faults | May reject requests / error page | Stays online, serves slightly stale data |
| Write latency | High (coordination overhead) | Low (local writes) |
| Scale ceiling | Limited by coordination across nodes | Billions of users |

**ACID** = Atomicity, Consistency, Isolation, Durability. Checkout needs it: a payment is all-or-nothing (atomicity), balances obey integrity rules (consistency), concurrent withdrawals don't interfere (isolation), and a committed order survives a crash (durability).

**BASE** = Basically Available, Soft state, Eventual consistency:
- **Basically Available** — serve *some* data rather than nothing (a slightly stale recommendation beats a crash).
- **Soft state** — state changes without new user input (background replication syncs replicas).
- **Eventual consistency** — if writes stop, all nodes converge to the same value.

**Why BASE is acceptable here — the CAP theorem.** CAP says a distributed system can provide at most **2 of 3**: Consistency, Availability, Partition Tolerance. Because network **partitions are inevitable** in a cluster, **P is mandatory**, so the real choice is **CP vs AP**:

$$\text{During a partition: } C \uparrow \Rightarrow A \downarrow \quad \text{or} \quad A \uparrow \Rightarrow C \downarrow$$

- **Checkout/accounts = CP** — during a partition, refuse the read (or return an error) rather than risk a wrong balance.
- **Recommendation engine = AP** — during a partition, serve a slightly stale recommendation rather than fail. A product suggestion from 5 minutes ago is acceptable; a missing checkout confirmation is not.

**Why BASE is more performant:** ACID's strict guarantees require **massive coordination** at cluster scale — distributed locking (isolation), two-phase commit (atomicity), synchronous replication (durability). That coordination is the **network tax** that slows every write. BASE avoids most of it: writes go to local replicas and propagate asynchronously, so the recommendation engine sustains the high write throughput of 500 M events/day without grinding to a halt.

**Pro tip:** Contrast tables earn marks — one row per ACID/BASE property plus one row for *failure behaviour* and *scale ceiling*. Then the CAP reasoning must be explicit: *P mandatory → the only choice is CP vs AP → map each workload to its side*. The killer sentence is the stale-vs-fail trade-off: "a 5-minute-old recommendation is acceptable; an uncertain account balance is not." Never confuse **ACID Consistency** (integrity rules) with **CAP Consistency** (reads see latest write) — that conflation is the course's most-cited exam trap.

---

## Q.2

### Q.2.1 — MapReduce Data Flow for Revenue Aggregation (5 Marks)

You need to execute a batch job to calculate the **total transaction revenue per `product_category`**. Map out the logical data flow using the **MapReduce** programming model. Clearly define what happens to the transaction dataset during the **Split, Map, Shuffle, Sort, and Reduce** phases.

#### Answer

The pipeline is **Split → Map → Shuffle → Sort → Reduce**, with final results written to the distributed file system (HDFS).

| Phase | What happens to the transaction data |
|-------|--------------------------------------|
| **1. Split** | The framework breaks the raw transaction file into **input splits** (typically 64–128 MB chunks, aligned with HDFS block size). One map task is created per split; a 10 TB file yields ~80,000 splits → 80,000 parallel map tasks. |
| **2. Map** | Each worker reads its local split and applies the map logic independently — parse each record and **emit intermediate key-value pairs** `(product_category, transaction_amount)` to its local buffer. Mappers do **not** communicate with each other. |
| **3. Shuffle** | The framework **partitions** the intermediate pairs so all values for the same key reach the same reducer: $\text{reducer\_id} = \text{hash}(product\_category) \bmod R$. This is the **network-intensive** phase — the "network tax" — moving data across racks/switches. |
| **4. Sort** | At each reducer, values are **grouped by key** into ordered lists — `("Electronics", [49.99, 120.00, 79.50, ...])` — so the reducer reads a perfectly organized stream, one key at a time. |
| **5. Reduce** | Each reducer **aggregates** its complete list for a key — here, $\text{sum}$ of all amounts — producing the globally correct total per category, e.g. `("Electronics", 4,200,000.00)`. Output is written to HDFS. |

The reduce phase is the **compression funnel**: 10 TB of raw events collapses to a few megabytes of per-category totals.

**Assumption:** a single reduce aggregation suffices (no multiple-output partitioning needed); combiner optional for local pre-aggregation.

**Pro tip:** Order is sacred — always **map → shuffle → sort → reduce**, never reduce before shuffle. State the partitioning formula $\text{hash}(key) \bmod R$ explicitly; it is the single most-tested artifact of this phase. Connect each phase to *why* it exists: split = parallelism, map = transform, shuffle = colocate keys, sort = organize values, reduce = aggregate. Mentioning that shuffle is the **bottleneck** and that tuning focuses on *minimizing shuffle data* (filter early, use combiners) is the expert extra.

---

### Q.2.2 — Hadoop vs Spark for Iterative Workloads (5 Marks)

The recommendation system utilizes iterative Machine Learning algorithms (such as **K-Means clustering** for customer segmentation). Explain the specific **disk-bound I/O limitations** of Hadoop's MapReduce when executing iterative workloads. Detail how Apache Spark's **in-memory computing architecture** and **Resilient Distributed Datasets (RDDs)** resolve this operational bottleneck.

#### Answer

**K-Means is the canonical iterative workload:** assign each point to the nearest centroid, recompute centroids as the mean of assigned points, repeat until convergence — typically **10–100+ iterations**, each reading the *same* dataset.

**Hadoop's disk-bound limitation.** In Hadoop, **every iteration is a separate MapReduce job** with a full disk round-trip:

$$\text{Per iteration: Read HDFS} \rightarrow \text{Process} \rightarrow \text{Write HDFS} \rightarrow \text{Repeat}$$

$$\text{Total I/O} \approx N \times (|D|_{\text{read}} + |D|_{\text{write}})$$

For 100 iterations, that is 99 unnecessary HDFS reads + 99 unnecessary HDFS writes in the middle iterations. **Disk I/O time frequently exceeds computation time** — CPUs sit idle waiting for storage. This is not a tuning problem; it is an **architectural constraint**: disk is the primary workspace, and every intermediate result is **materialised** to disk between stages.

**Spark's in-memory fix.** Spark treats **RAM as the primary workspace**:

1. **Iteration 1:** read HDFS once → **cache** the dataset in executor memory → compute.
2. **Iterations 2–N:** compute entirely **in memory** — zero disk reads, zero disk writes.

| Metric | Hadoop (100 iters) | Spark (100 iters) |
|--------|--------------------|-------------------|
| HDFS reads (middle iterations) | 99 | **0** |
| HDFS writes (middle iterations) | 99 | **0** |
| Data in RAM after iteration 1 | No | **Yes** |
| Typical speedup | Baseline | **10×–100×** |

**RDDs** (Resilient Distributed Datasets) are the mechanism: immutable, partitioned collections that can be **persisted/cached** in memory and reused across iterations. The speedup is purely **architectural** — both run identical K-Means logic; Spark just stops round-tripping through disk.

**Cost trade-off:** Spark's speed requires **RAM-heavy clusters** (memory is the most expensive resource per GB); Hadoop is cheaper per TB of storage. Choose Spark when the algorithm **repeatedly touches the same data**; Hadoop remains cost-effective for one-pass ETL/archival.

**Pro tip:** This is the benchmark question — show the I/O formula $N \times (|D|_{read} + |D|_{write})$ and the 99-vs-0 table; both are almost verbatim from the course's K-Means benchmark. The differentiator sentence: *"the algorithm is identical; only the execution architecture differs."* Never claim "Spark is always 100× faster" — that figure applies to **iterative** workloads, and single-pass ETL sees only modest gains. Mentioning the RAM-cost trade-off covers the "engineer's judgment" mark.

---

### Q.2.3 — PySpark: Revenue Aggregation Coding Task

Write the **PySpark code** to process a historical transaction dataset containing records of `(user_id, product_category, transaction_amount)`. Your code must:

- filter out transactions under `$20`,
- map the remaining data to key-value pairs of `(product_category, transaction_amount)`,
- calculate the aggregate revenue per category.

> *Along with your code, provide a written analysis addressing Q.3.1–Q.3.3 below.*

#### Answer

```python
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("revenue-per-category").getOrCreate()

transactions = spark.read.csv(
    "s3://ecom-data/transactions/", header=True,
    schema="user_id string, product_category string, transaction_amount double"
)

# 1. Filter out transactions under $20   (narrow dependency)
filtered = transactions.filter(F.col("transaction_amount") >= 20)

# 2. Map to key-value pairs (product_category, transaction_amount)
pairs = filtered.select("product_category", "transaction_amount")

# 3. Aggregate revenue per category      (wide dependency — shuffle)
revenue_by_category = pairs.groupBy("product_category").agg(
    F.sum("transaction_amount").alias("total_revenue")
).orderBy(F.desc("total_revenue"))

revenue_by_category.show(truncate=False)
```

**Assumption:** the CSV has a header row; amounts are in a single currency; `user_id` is not needed for this aggregation, so it is dropped at the `select` step.

**Pro tip:** When a question says "write the PySpark code," the marks go to the **three operations in the right order** — filter (≥ 20, i.e., keep ≥ 20 → drop < 20), map (project the key-value pair), aggregate (group + sum). Keep the code minimal and comment the dependency type of each step (narrow/wide) since Q.3.2 re-uses it. Always state the `>= 20` boundary interpretation and any schema/header assumption — the paper explicitly rewards stated assumptions.

---

## Q.3

### Q.3.1 — Lazy Evaluation and Query Optimization (3 Marks)

Explain the performance mechanics of **Lazy Evaluation** in Apache Spark. Why does Spark delay physical execution until an **action** is called, and how does this benefit overall query optimization (e.g., via **predicate pushdown** and **pipelining**)?

#### Answer

**Lazy evaluation = transformations are recorded, not executed.** When you chain `map`, `filter`, `flatMap`, Spark does **not** touch the data. It builds a **lineage graph** — a logical plan ("recipe") of operations. Only an **action** (`count`, `collect`, `take`, `save`) triggers compilation of the physical plan and cluster execution. Analogy: the kitchen waits for the *complete order* before cooking, so it can coordinate shared prep.

**Why delay? Whole-program optimisation.** An eager system executes each step immediately, materialising to disk between steps, and can only optimise locally. Because Spark sees the *entire* chain before anything runs, it can optimise globally:

- **Predicate pushdown** — move `filter` as early as possible, even toward the read stage, so irrelevant rows are never loaded or parsed. *Filter-before-join shrinks the shuffle.*
- **Pipelining** — fuse multiple **narrow** transformations into a **single in-memory pass** within one stage; no intermediate RDD materialisation to disk (the read-map-write-read-filter-write pattern of eager MapReduce collapses to one read + one memory pass).
- **Catalyst optimizer** (DataFrame/SQL) — applies rule-based rewrites and picks the cheapest physical plan (e.g., broadcast join vs sort-merge join).

**Assumption:** the question targets the RDD/DataFrame execution model generally; Catalyst specifics apply to the SQL/DataFrame API.

**Pro tip:** Structure the answer as *mechanism → trigger → benefit*. Mechanism: "transformations are recipes; actions are orders." Trigger: an action returns a value or writes out. Benefits: name **predicate pushdown** and **pipelining** explicitly, and add *join reordering/projection pruning* for the final mark. One trap to pre-empt: pipelining works **within** a stage (narrow deps only) — wide dependencies (shuffles) break the pipeline. Also mention that repeated actions without `cache()` **re-execute** the whole lineage.

---

### Q.3.2 — Narrow vs Wide Dependencies and Stages (4 Marks)

In your written code, explicitly identify which operations represent **narrow dependencies** and which represent **wide dependencies**. Explain how the Spark engine uses these dependency definitions to break down a logical **DAG** into physical execution **Stages**.

#### Answer

**In the code from Q.2.3:**

| Operation | Dependency | Why |
|-----------|------------|-----|
| `filter` (amount ≥ 20) | **Narrow** (one-to-one) | Each parent partition feeds **at most one** child partition; no data leaves the node. |
| `select` (key-value pair) | **Narrow** (one-to-one) | Pure per-record projection — same partition mapping. |
| `groupBy` + `sum` | **Wide** | All values for a `product_category` must be **colocated** on one partition → **shuffle** required. |

**Narrow dependency:** each partition of the parent RDD contributes to at most one partition of the child (e.g., `map`, `filter`, `flatMap`, `union`). Properties: **no shuffle**, operations can be **pipelined** in a single memory sweep, tasks run fully in parallel.

**Wide dependency:** one parent partition may be needed by **multiple** child partitions (e.g., `groupByKey`, `reduceByKey`, `join`, `repartition`, `distinct`). The framework must redistribute data so related keys land on the same node — a **shuffle** (serialise → write local disk buffers → transfer over network → read by receiving tasks).

**DAG → Stages.** Every **wide dependency creates a shuffle boundary**, and each boundary splits the DAG into a new **stage**:

- Narrow transformations queue up **within** one stage — "everything we can do locally before we must talk to the network."
- At the wide dependency, Spark stops, shuffles, and starts a **new stage**.
- Each stage is then decomposed into **tasks** (one per partition) scheduled on executors.

For our job: Stage 1 = `read → filter → select` (pipelined, narrow); shuffle boundary at `groupBy`; Stage 2 = `groupBy → sum → orderBy` (the aggregation and final ordering).

**Pro tip:** The table maps the code to the two dependency classes — that is the heart of the marks. Know the canonical lists: narrow = `map/filter/flatMap/union`; wide = `groupByKey/reduceByKey/join/repartition/distinct`. The sentence examiners want: *"a wide dependency is a shuffle, a shuffle is a stage boundary, a stage is the maximal pipeline between shuffle boundaries."* A refined extra: use `reduceByKey` instead of `groupByKey` to pre-aggregate locally before the shuffle (less data moved).

---

### Q.3.3 — Data Skew, Salting, and Custom Partitioning (3 Marks)

During peak sales events, certain viral product categories experience extreme volume, leading to **severe data skew** during the aggregate shuffle phase. Implement a **salting** strategy in your PySpark logic (or explain its code-level implementation) to mitigate skew, and explain how **custom partitioning** balances the workload across cluster nodes.

#### Answer

**The problem.** Spark's default hash partitioner sends every record sharing a key to the same partition. If `Electronics` has 10× the volume of other categories, one reducer handles the viral key while the others finish early and idle — a **straggler** that slows the whole job.

**Salting (two-phase aggregation).** Since this is aggregation (not a join), break the heavy key into $N$ salted sub-keys, aggregate partial sums per sub-key, then strip the salt and sum the partials:

```python
from pyspark.sql import functions as F
import random

# 1. Add a random salt to the key of heavy categories (e.g., [0, N-1])
salted = pairs.withColumn(
    "salted_key",
    F.concat(F.col("product_category"),
             F.lit("_"),
             (F.rand() * 10).cast("int"))
)

# 2. First aggregation: partial sums per salted key — shuffle spreads across 10x partitions
partial = salted.groupBy("salted_key").agg(F.sum("transaction_amount").alias("partial"))

# 3. Strip the salt and aggregate the partials to the true per-category total
result = partial.withColumn(
    "product_category",
    F.regexp_replace("salted_key", r"_\d+$", "")
).groupBy("product_category").agg(F.sum("partial").alias("total_revenue"))
```

- One heavy key becomes $N$ distinct keys → the shuffle distributes its rows across ~$N$ partitions instead of one.
- Choose $N$ to match the parallelism you want for the heavy key (e.g., number of cores/partitions). Too few → residual skew; too many → overhead of many small partial partitions.

**Custom partitioning.** Instead of (or in addition to) salting, supply a **custom partitioner** — for the RDD API, a subclass of `Partitioner` that overrides `getPartition(key)` — to route data by a business rule rather than the default hash. Example: partition *viral* categories into many partitions while grouping long-tail categories together, so each node gets a comparable slice of the real-world, imbalanced distribution.

```python
from pyspark.rdd import Partitioner

class CategoryPartitioner(Partitioner):
    def __init__(self, num_parts, hot_keys):
        super().__init__(num_parts, None)
        self.hot_keys = hot_keys
    def numPartitions(self):
        return self.numParts
    def getPartition(self, key):
        if key in self.hot_keys:
            return hash(key) % (self.numParts // 2)      # spread hot keys widely
        return (self.numParts // 2) + hash(key) % (self.numParts // 2)  # group the rest

rdd = pairs.rdd.partitionBy(CategoryPartitioner(100, {"Electronics"}))
```

**Assumption:** salting is applied to the *aggregation* path (two-phase sum, no join partner to explode); for a join, the small table would also need to be exploded/replicated to match the salted keys.

**Pro tip:** The answer is the three-step recipe: *identify the skewed key → add a random salt → aggregate twice (partial per salted key, then final over stripped key)*. State the key design choice: salt range $N$ ≈ desired parallelism. The trap to call out: in a **join**, salting only the large table fails — the small table must be **exploded** to match every salt value. Mentioning custom partitioners as the *RDD-API* alternative (vs salting at the DataFrame level) shows you know both mechanisms and when each fits.

---

## Q.4

### Q.4.1 — Data Locality: Move Code, Not Data (3 Marks)

Transferring massive e-commerce datasets across network switches introduces high latency. Explain Spark's architectural philosophy of **Data Locality** ("move code, not data") and describe how the Spark driver schedules tasks relative to data placement (**PROCESS_LOCAL, NODE_LOCAL, RACK_LOCAL**) to minimize network overhead.

#### Answer

**The network bottleneck.** Moving terabytes across a 10 Gbps network is slow: $\frac{10 \text{ TB}}{1.25 \text{ GB/s}} \approx 2.3 \text{ hours}$ — CPUs idle before a single line of computation runs. Traditional programming moves *data to code*; at petabyte scale that is unaffordable.

**Spark's inversion: move code to data.** Code (a serialized map/filter function) is kilobytes; data partitions are megabytes to gigabytes. Spark ships the cheap thing (code) to the expensive thing (data):

- The DAG scheduler is **storage-aware**: it asks HDFS/S3 *"where does this partition live?"* (e.g., DataNode Server A, Rack 1), then schedules that partition's task on an executor **on that node**.
- Network pipes carry **kilobytes of code, not gigabytes of data**.

**Locality levels — driver's scheduling preference order:**

| Level | Meaning | Performance |
|-------|---------|-------------|
| `PROCESS_LOCAL` | Data in the **same JVM** as the executor | Best |
| `NODE_LOCAL` | Data on the **same node**, different JVM | Good |
| `RACK_LOCAL` | Data in the **same rack** | Acceptable |
| `NO_PREF` | No preference | Neutral |
| `ANY` | Data anywhere in the cluster | Worst (network transfer) |

The driver tries `PROCESS_LOCAL` first; if the preferred executor is busy, it **falls back** to `NODE_LOCAL`, then `RACK_LOCAL`, then `ANY` — trading locality for scheduling progress.

**Where locality applies:** narrow transformations (map/filter) run where the input lives — zero network transfer for input. Wide transformations (shuffle) **intentionally break locality** to colocate keys by design.

**Assumption:** HDFS-backed data (block-locality aware); `parallelize()` on the driver has no locality advantage since data is shipped to workers.

**Pro tip:** Quote the ordering `PROCESS_LOCAL > NODE_LOCAL > RACK_LOCAL > ANY` verbatim — it is a direct recall point. The insight that ties it together: *partitioning provides parallelism, data locality makes that parallelism efficient*. Two traps to pre-empt: (1) locality does **not** mean zero network traffic — shuffles deliberately move data; (2) HDFS has strong block locality, S3 (remote object storage) has weaker locality.

---

### Q.4.2 — Lineage vs Replication: Spark's Fault Tolerance (3 Marks)

Assume a worker node fails midway through processing a stage. Contrast Spark's **Lineage-based fault tolerance** mechanism with Hadoop HDFS's standard **data replication** strategy. Explain how Spark rebuilds lost RDD partitions without paying the continuous bandwidth and storage penalty of block replication.

#### Answer

Two fault-tolerance philosophies:

| Dimension | Replication (HDFS) | Lineage / recomputation (Spark) |
|-----------|--------------------|---------------------------------|
| What is stored | **Copies of the data** (default 3×) | **Metadata "recipe"** — the DAG of transformations |
| Recovery | Switch to a replica (near-instant) | Trace lineage backward, **recompute** the lost partition |
| Steady-state cost | **Continuous** — every write is 3× network + disk traffic | Near-zero — logging a few KB of metadata |
| Storage footprint | 3× data size (1 PB data → 3 PB storage) | Grows with *logic complexity*, not data size |
| Failure cost | Near-zero (read local replica) | Proportional to **DAG depth** |

**Analogy:** replication = photocopying every document into three offices; lineage = storing a *recipe card* and re-cooking on demand.

**On a mid-stage worker failure**, Spark:
1. Detects the lost partition(s).
2. Consults the **lineage DAG** to find the nearest reliable ancestor (HDFS block, cached parent, or checkpoint).
3. **Re-executes** the transformations to rebuild only the lost partition(s) — using **CPU instead of storage/bandwidth**.

**Why recomputation is correct (and avoids replication's penalty):**
- **Immutability** — RDDs never change once created; each transformation produces a new fixed snapshot.
- **Determinism** — rerunning the same code on the same input yields identical output.
- These two properties guarantee the recomputed partition is *identical* to the lost one.

So Spark does not maintain redundant copies of every intermediate in memory (which would halve its usable RAM and multiply write traffic); it keeps RAM lean and pays the recompute cost **only when a failure actually occurs**. Lineage's footprint stays ~KB–MB even at petabyte scale.

**Trade-off:** replication wins on **recovery latency** (instant switch); recomputation wins on **steady-state performance** (no continuous copying). For deep DAGs (50+ stages), recomputation gets slow — which is why checkpointing (Q.4.3) exists.

**Pro tip:** This is a *two-column contrast* question — the table earns most of the marks, plus the three-word promise: **immutability + determinism = safe recomputation**. Emphasise *when* each cost is paid: replication pays *always*, lineage pays *on failure only*. The expert sentence: "Spark spends CPU instead of bandwidth; the cost is proportional to DAG depth, not data size."

---

### Q.4.3 — Liability of Lineage and Checkpointing (4 Marks)

If your recommendation pipeline updates user interaction profiles through thousands of iterative state transitions, the RDD **lineage graph** will grow exceptionally long. Explain the technical risks associated with this "liability of lineage" (such as **StackOverflowError** exceptions and extended recovery times). Detail how implementing a **Checkpointing** strategy resolves this by truncating the Directed Acyclic Graph (DAG), and strictly differentiate **Checkpointing** from standard **RDD Caching / Persistence**.

#### Answer

**Why lineage becomes a liability.** In shallow DAGs, lineage gives near-instant recovery with tiny metadata. Beyond ~100 stages it turns into a liability through three failure modes:

1. **Linear recovery cost** — recovery replays the whole chain: losing a partition at stage 100 recomputes 99 previous steps. $\text{Recovery time} \propto N$ (stage count). A "quick fix" becomes minutes-to-hours.
2. **StackOverflowError (hard crash)** — each RDD holds a reference to its parent, so **serialization is recursive** (`RDD_100 → parent RDD_99 → ... → RDD_1`). When the driver serializes a task, the JVM traverses the chain; at 100+ depth the **JVM call stack is exhausted**. PageRank/ALS/gradient-descent loops (100–1000 iterations) are the primary victims.
3. **Driver bottleneck (soft degradation)** — every RDD object (with parent refs + metadata) is held in driver memory and cannot be garbage-collected while the chain lives. The driver spends CPU on dependency tracking instead of scheduling, and memory pressure grows with lineage depth, not data size.

**Checkpointing as the fix.** `sc.setCheckpointDir(...)` + `rdd.checkpoint()` **truncates the DAG**:

- Spark writes the RDD to **reliable distributed storage (HDFS/S3)** via an immediate background job (**eager**, not lazy).
- It then **severs the parent references** — the checkpointed RDD becomes a **leaf node** with no history.
- Recovery now reads from the checkpoint file: a 100-stage recovery becomes a **1-stage recovery**, and the driver can garbage-collect the severed ancestors (freeing memory).

**Checkpointing vs Caching / Persistence — strictly different:**

| Dimension | Caching / Persistence | Checkpointing |
|-----------|----------------------|---------------|
| Lineage | **Preserved** | **Truncated (destroyed)** |
| Storage | Memory / local executor disk | HDFS / S3 (distributed, replicated) |
| Execution | **Lazy** (materialised on first action) | **Eager** (immediate background job) |
| Session scope | Dies with the Spark session | **Persists across sessions** |
| On executor failure | Cached data on that executor is **lost** → recompute full chain | Safe — read from distributed storage |
| Primary purpose | **Speed and reuse** | **Stability and lineage management** |

The key trap: **caching does not solve deep-lineage problems.** Caching preserves the lineage graph, so if cached data is lost, Spark still replays the entire DAG. Only checkpointing severs the chain. Rule of thumb: *cache for speed in reuse; checkpoint for stability in long iterative pipelines.*

**Pro tip:** Cover all three risks with names — *linear recovery cost, StackOverflowError from recursive serialization, driver memory bottleneck* — then the fix, then the strict differentiation. The single most-cited exam distinction: **caching preserves lineage (lazy, memory, session-scoped); checkpointing destroys lineage (eager, HDFS/S3, cross-session).** Also mention the "ticking time bomb" pattern — a 200-iteration job looks healthy for 50 iterations, then crashes suddenly; checkpointing is *mandatory* for iterative workloads, not optional.
