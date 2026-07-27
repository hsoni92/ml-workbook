# Assignment — Architecting and Implementing a Resilient Global Telemetry Platform

---

## Context

You are the lead data engineer for a global logistics company. Your fleet of 500,000 vehicles streams telemetry data (engine heat, speed, location, battery efficiency) 24/7. You are tasked with building a scalable platform to process this massive influx of data for both:

- **Real-time monitoring**
- **Historical predictive maintenance**

Please refer to the **Big Data Platforms & Analytics [Handout and COD].xlsx** document for foundational concepts while completing this assignment.

---

## Part 1: System Architecture & Data Paradigms (Modules 1 & 2)

### 1. Scaling Strategy

Explain the physical hardware limitations of single-node systems (the "Wall" in Hardware). Justify why **horizontal scaling (Scale-Out)** is required for this telemetry platform over vertical scaling.

Ensure you address the core architectural constraints — the **Three Vs of Big Data** — in your justification.

### 2. Consistency Models

For the high-velocity ingestion of vehicle coordinates:

- Contrast the **ACID** and **BASE** consistency models
- Using the **CAP Theorem**, explain which model you would choose for this specific workload and why

---

## Part 2: Batch Processing & MapReduce (Modules 3 & 4)

### 1. Logical Flow

Design a MapReduce logical data flow to aggregate the total miles driven per vehicle model. Clearly map out the phases:

```
Split → Map → Shuffle → Sort → Reduce
```

### 2. Hadoop vs. Spark

Iterative machine learning algorithms will eventually run on this data. Explain why Spark's in-memory computing model overcomes Hadoop's disk-bound I/O bottlenecks for these iterative algorithms.

---

## Part 3: PySpark Implementation & Resilience (Modules 5 & 8)

Write the PySpark code to process a historical batch dataset of this telemetry data. Your code and accompanying explanation must address the following:

### 1. Transformations and Actions

- Ingest the data and calculate the average engine temperature per vehicle model
- Identify which parts of your code represent **narrow dependencies** (no shuffle) and which represent **wide dependencies** (forcing a network shuffle)

### 2. Optimization

Some specific delivery trucks generate 1000× more logs than others, causing severe data skew.

- Implement a **salting strategy** in your PySpark code to mitigate this skew during aggregation
- Define your **partitioning strategy** (e.g., hash vs range partitioning) to optimize the shuffle phase

### 3. Fault Tolerance

Distributed memory is volatile. Explain how Spark uses **Resilient Distributed Datasets (RDDs)** and **lineage graphs** to maintain fault tolerance without heavy data replication.

### 4. Checkpointing

In your code, simulate a scenario where the lineage depth grows excessively long due to iterative processing.

- Implement a strategic **checkpointing** mechanism to truncate the DAG
- Explain how this prevents `StackOverflow` errors and stabilizes recovery time

---

## Part 4: Advanced Execution Mechanics & Resilience Strategies (Modules 5–8)

To complete the pipeline, architect the underlying execution and resilience strategies for your Spark application.

### 1. The Execution Model & DAGs (Module 6)

Spark does not execute your transformations immediately.

- Explain the performance mechanics of **lazy evaluation**
- As your telemetry data is processed, map out how the Spark engine constructs a **Directed Acyclic Graph (DAG)**
- Explain exactly how it uses **wide dependencies** to decompose the logical plan into physical execution **stages**

### 2. Data Locality & Fault Tolerance (Modules 5 & 7)

Moving massive amounts of telemetry data across a network is incredibly slow.

- Explain Spark's **"Don't move data, move code"** philosophy and how **data locality** minimizes network congestion
- Contrast Spark's **lineage-based recovery** with Hadoop's **data replication** strategy
- Explain how Spark maintains stability without the heavy I/O bandwidth cost of copying data

### 3. Mitigating Lineage Liability (Module 8)

Assume you are running a highly iterative calculation on the telemetry data that updates its state hundreds of times.

- Explain the **"Liability of Lineage"** in this scenario, specifically addressing the risks of `StackOverflow` errors and degraded recovery times
- Detail how implementing a **checkpointing** strategy breaks the family tree (truncates the DAG) to solve this
- Strictly differentiate how checkpointing behaves compared to standard Spark **caching**

---

## Evaluation Rubric

**Rubric name:** Graded Assignment
**Total score:** 20 points (5 criteria × 4 points each)

| Criterion | Level 4 (3.1–4.0) | Level 3 (2.1–3.0) | Level 2 (1.1–2.0) | Level 1 (0.0–1.0) | Max |
| --- | --- | --- | --- | --- | ---: |
| **Architectural Design & Scaling Strategy (Modules 1 & 2)** | Flawlessly evaluates hardware limitations and justifies horizontal scaling using the Three Vs. Provides a highly accurate comparison of ACID vs BASE models, perfectly applying the CAP theorem to the specific scenario. | Solid architectural design with clear understanding of scaling, but contains minor gaps in the application of the CAP theorem or consistency models. | Architecture has significant flaws; misunderstands the trade-offs between BASE and ACID, or misidentifies the technical differences between horizontal and vertical scaling. | Incorrect architectural design; fails to address core Big Data constraints or physical hardware limitations. | / 4 |
| **Code Effectiveness & Distributed Optimization (Modules 3, 4, 5)** | Writes highly efficient PySpark and MapReduce code. Expertly utilizes optimal partitioning strategies (e.g., hash/range partitioning) and flawlessly implements salting to mitigate data skew. Demonstrates a deep understanding of lazy evaluation and DAG optimization. | Code is functional and correct but lacks advanced partitioning strategies or has minor inefficiencies in handling data skew. | Code runs but suffers from severe network shuffling bottlenecks, ignores data locality, or misuses wide vs narrow dependencies. | Code is incomplete, fails to execute, or completely misunderstands distributed in-memory processing. | / 4 |
| **Fault Tolerance & Resilience Implementation (Modules 5 & 8)** | Perfectly implements lineage tracking concepts and uses strategic checkpointing to truncate DAGs, ensuring state recovery without the risk of driver StackOverflow errors. | Implements basic resilience, but the checkpointing strategy is sub-optimal or creates unnecessary disk I/O overhead. | Misunderstands lineage liability; fails to address node failures adequately or over-relies on replication instead of recomputation. | No fault tolerance considerations; system design is vulnerable to a single point of failure. | / 4 |
| **Advanced Execution Mechanics & Resilience Strategies (Modules 5, 6, 7, 8)** | Flawlessly explains Spark's lazy evaluation and DAG construction, accurately identifying how wide dependencies trigger stage boundaries. Expertly contrasts lineage-based recovery with data replication, highlighting network/I/O trade-offs, and provides a technically precise explanation of how checkpointing truncates DAGs to prevent StackOverflow errors. | Strong understanding of Spark's execution model and DAGs, but contains minor gaps in explaining the specific mechanics of data locality or the architectural differences between caching and checkpointing. | Demonstrates basic knowledge of Spark operations but misidentifies stage boundaries, confuses narrow and wide dependencies, or struggles to explain the liability of lineage. | Fails to accurately describe Spark's execution model, DAG decomposition, or fault tolerance mechanisms. | / 4 |
| **Documentation & Explanation** | Crystal clear documentation explaining the logical data flow (Split, Map, Shuffle, Sort, Reduce), dependency types, and code logic. | Good documentation but missing some explanations of complex operations or DAG construction. | Sparse documentation; hard to follow the developer's intent or architectural choices. | No meaningful documentation provided. | / 4 |
| **Total** | | | | | **/ 20** |

### Overall Score

| Overall level | Minimum total points (out of 20) |
| --- | ---: |
| **Level 4** | 11 |
| **Level 3** | 8 |
| **Level 2** | 5 |
| **Level 1** | 0 |
