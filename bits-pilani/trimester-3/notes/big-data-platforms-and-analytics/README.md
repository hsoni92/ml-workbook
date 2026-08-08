# Big Data Platforms And Analytics

## Week 1

1. [Big Data Platforms and Analytics: Course Roadmap](week-01/01-course-introduction-and-faculty-introduction-transcript.md)
1. [Big Data Constraints and Scaling: Module Overview](week-01/02-module-introduction-transcript.md)
1. [The Three Vs of Big Data: Volume, Velocity, and Variety](week-01/03-defining-volume-velocity-and-variety-transcript.md)
1. [How the Three Vs Reshape System Architecture](week-01/04-impact-of-the-3-vs-on-system-architecture-transcript.md)
1. [Hardware Constraints: CPU, RAM, and I/O](week-01/05-hardware-constraints-cpu-ram-and-io-transcript.md)
1. [Why Bigger Boxes Eventually Fail](week-01/06-why-bigger-boxes-eventually-fail-transcript.md)
1. [Vertical Scaling (Scale Up): Deep Dive](week-01/07-deep-dive-vertical-scaling-scale-up-transcript.md)
1. [Horizontal Scaling (Scale Out): Deep Dive](week-01/08-deep-dive-horizontal-scaling-scale-out-transcript.md)
1. [Introduction to Cluster Computing](week-01/09-introduction-to-cluster-computing-transcript.md)
1. [Economics of Commodity Hardware](week-01/10-economics-of-commodity-hardware-transcript.md)
1. [Module 1 Summary: Big Data Constraints and Scaling](week-01/11-module-summary-and-key-takeaways-transcript.md)

## Week 2

1. [Distributed Systems Challenges: Module Overview](week-02/01-module-introduction-transcript.md)
1. [The Fallacies of Distributed Computing](week-02/02-the-fallacies-of-distributed-computing-transcript.md)
1. [Network Partitions and Partition Tolerance](week-02/03-understanding-partitions-and-network-faults-transcript.md)
1. [The CAP Theorem: Consistency, Availability, and Partition Tolerance](week-02/04-defining-c-a-and-p-transcript.md)
1. [CP vs AP Systems: Choosing the Right Trade-Off](week-02/05-trade-offs-cp-vs-ap-systems-transcript.md)
1. [ACID Properties in Distributed Contexts](week-02/06-acid-properties-in-distributed-contexts-transcript.md)
1. [BASE: Basically Available, Soft State, Eventual Consistency](week-02/07-base-basically-available-soft-state-eventual-consistency-transcript.md)
1. [Conflict Resolution in Eventually Consistent Systems](week-02/08-how-storage-systems-handle-conflicts-transcript.md)
1. [Distributed Systems Fundamentals: Module Summary](week-02/09-module-summary-transcript.md)

## Week 3

1. [MapReduce Programming Model: Introduction](week-03/01-module-introduction-transcript.md)
1. [The Map Operation: Transforming Raw Data](week-03/02-the-map-operation-transforming-data-transcript.md)
1. [The Reduce Operation: Aggregating State](week-03/03-the-reduce-operation-aggregating-state-transcript.md)
1. [MapReduce Data Flow: Input Splits and Map Phase](week-03/04-data-flow-split-and-map-phases-transcript.md)
1. [Shuffle and Sort: The Bridge from Map to Reduce](week-03/05-the-magic-of-shuffling-and-sorting-transcript.md)
1. [Final Aggregation: The Reduce Phase in the Data Flow](week-03/06-final-aggregation-the-reduce-phase-transcript.md)
1. [Case Study: Analyzing Web Logs with MapReduce](week-03/07-analysing-web-logs-with-mapreduce-transcript.md)
1. [Fault Tolerance in MapReduce: Handling Node Failures](week-03/08-how-mapreduce-handles-node-failures-transcript.md)
1. [The Cost of Disk-Based Intermediate State](week-03/09-the-cost-of-disk-based-intermediate-state-transcript.md)
1. [MapReduce Module Summary](week-03/10-module-summary-transcript.md)

## Week 4

1. [Hadoop vs Spark: The Shift from Disk-Bound to In-Memory Batch Processing](week-04/01-module-introduction-transcript.md)
1. [HDFS Deep Dive: Blocks, Replication, and Rack-Aware Fault Tolerance](week-04/02-hdfs-deep-dive-blocks-and-replication-transcript.md)
1. [MapReduce Data Flow on HDFS: From Blocks to Final Output](week-04/03-the-mapreduce-data-flow-on-hdfs-transcript.md)
1. [High I/O Latency and Materialisation Cost: Hadoop's Performance Bottleneck](week-04/04-high-io-latency-and-materialisation-costs-transcript.md)
1. [Introduction to In-Memory Computing: RAM as Spark's Primary Workspace](week-04/05-introduction-to-in-memory-computing-transcript.md)
1. [How Spark Minimises Disk Read-Write Cycles: DAG, Lazy Evaluation, and Persistence](week-04/06-how-spark-minimises-disk-rw-cycles-transcript.md)
1. [Hadoop vs Spark for Iterative Algorithms: A K-Means Performance Benchmark](week-04/07-hadoop-vs-spark-iterative-algorithms-k-means-transcript.md)
1. [Module Summary: Hadoop vs Spark — Batch Processing Architecture Evolution](week-04/08-lesson-6-summary-and-assessment-transcript.md)

## Week 5

1. [Spark Core and RDD Fundamentals: Module Overview](week-05/01-module-introduction-transcript.md)
1. [Resilient Distributed Datasets (RDDs): Definition and Anatomy](week-05/02-introduction-to-rdds-transcript.md)
1. [RDD Resilience and Distribution: Lineage vs Replication](week-05/03-definition-and-resilience-explained-transcript.md)
1. [RDD Immutability: Why Spark Data Never Changes](week-05/04-immutability-why-rdds-never-change-transcript.md)
1. [RDD Partitioning: The Atomic Unit of Parallelism in Spark](week-05/05-how-partitioning-enables-parallelism-transcript.md)
1. [Data Locality and the Spark Cluster: Move Code, Not Data](week-05/06-data-locality-and-the-spark-cluster-transcript.md)
1. [Creating RDDs from Local Collections: parallelize()](week-05/07-parallelising-local-collections-transcript.md)
1. [Loading External Data: HDFS, S3, and Local Filesystems](week-05/08-loading-external-data-hdfs-s3-local-transcript.md)
1. [Module Summary: RDD Fundamentals](week-05/09-module-summary-transcript.md)

## Week 6

1. [Spark Execution Engine: Architecture Overview](week-06/01-module-introduction-and-the-spark-execution-engine-an-overview-transcript.md)
1. [Lazy Evaluation: Why Spark Waits](week-06/02-understanding-lazy-evaluation-why-wait-transcript.md)
1. [Benefits of Lazy Evaluation: Optimisation and Pipelining](week-06/03-benefits-query-optimisation-and-pipelining-transcript.md)
1. [Narrow vs Wide Dependencies: The Performance Skeleton](week-06/04-transformations-narrow-vs-wide-dependencies-transcript.md)
1. [Actions: Triggering Execution](week-06/05-actions-triggering-the-execution-transcript.md)
1. [Building the Directed Acyclic Graph (DAG)](week-06/06-building-the-directed-acyclic-graph-dag-transcript.md)
1. [Breaking the DAG into Stages and Tasks](week-06/07-breaking-the-dag-into-stages-and-tasks-transcript.md)
1. [Coding Walkthrough: Tracing a Job from Code to Tasks](week-06/08-coding-walkthrough-trace-a-job-from-code-to-tasks-transcript.md)
1. [Module Summary: Spark Execution Model](week-06/09-module-summary-transcript.md)

## Week 7

1. [Why Resilience Matters in Big Data Systems](week-07/01-why-resilience-matters-in-big-data-transcript.md)
1. [Challenges of Distributed Memory Recovery](week-07/02-challenges-of-distributed-memory-recovery-transcript.md)
1. [Recomputing vs Replicating Data: Two Fault-Tolerance Philosophies](week-07/03-recomputing-vs-replicating-data-transcript.md)
1. [Anatomy of an RDD Lineage Graph](week-07/04-anatomy-of-a-lineage-graph-transcript.md)
1. [RDD Lineage Graph Walkthrough: Sales Analysis by Category](week-07/05-walkthrough-an-example-of-rdd-lineage-graph-transcript.md)
1. [Recovery in Narrow Dependencies: Fast, Local, Isolated](week-07/06-recovery-in-narrow-dependencies-one-to-one-transcript.md)
1. [The Complexity of Wide Dependency Failures](week-07/07-the-complexity-of-wide-dependency-failures-transcript.md)
1. [Spark Execution Mechanics: Stages, Pipelining, and Shuffle Skew](week-07/08-demo-triggering-recomputation-in-pyspark-transcript.md)
1. [Spark Resilience: Module Summary and Key Takeaways](week-07/09-module-summary-transcript.md)

## Week 8

1. [When Lineage Becomes a Liability](week-08/01-when-lineage-becomes-a-liability-transcript.md)
1. [Stack Overflow and Performance Degradation from Deep Lineage](week-08/02-stack-overflow-and-performance-degradation-transcript.md)
1. [Breaking the Family Tree: Strategic Truncation via Checkpointing](week-08/03-breaking-the-family-tree-for-stability-transcript.md)
1. [Caching vs Checkpointing: Two Critical Resilience Mechanisms](week-08/04-the-key-differences-caching-vs-checkpointing-transcript.md)
1. [Writing Checkpoints to Reliable Storage: HDFS and S3](week-08/05-writing-to-reliable-storage-hdfs-and-s3-transcript.md)
1. [Internal Mechanics: How Spark Truncates the DAG During Checkpointing](week-08/06-internal-mechanics-truncating-the-dag-transcript.md)
1. [Recomputation Cost vs Storage IO Latency: The Checkpointing Trade-off](week-08/07-recomputation-cost-vs-storage-io-latency-transcript.md)
1. [Advanced Resilience Strategies: Module Summary](week-08/08-module-summary-transcript.md)

## Week 9

1. [Why Partitioning Is the Secret to Horizontal Scale](week-09/01-why-partitioning-is-the-secret-to-scale-transcript.md)
1. [Partitioning vs Replication: Complementary but Distinct](week-09/02-partitioning-vs-replication-transcript.md)
1. [How Partitions Enable Parallel Execution](week-09/03-how-partitions-enable-parallel-execution-transcript.md)
1. [Hash Partitioning Mechanics: The Modulo Operator and Uniformity](week-09/04-mechanics-the-modulo-operator-and-uniformity-transcript.md)
1. [Use Cases: When to Choose Hash Partitioning](week-09/05-use-cases-when-to-choose-hash-partitioning-transcript.md)
1. [Range Partitioning Mechanics: Key Ranges and Sorted Data](week-09/06-mechanics-key-ranges-and-sorted-data-transcript.md)
1. [Handling Dynamic Ranges and Boundary Issues](week-09/07-handling-dynamic-ranges-and-boundary-issues-transcript.md)
1. [When Default Partitioners Fail: Custom Partitioning Logic](week-09/08-when-default-partitioners-fail-transcript.md)
1. [Building Custom Partitioning Logic in PySpark](week-09/09-building-custom-logic-transcript.md)
1. [Data Partitioning Strategies: Module Summary](week-09/10-module-summary-transcript.md)

## Week 10

1. [Advanced Data Partitioning: Optimisation and Skew](week-10/01-module-introduction-transcript.md)
1. [Uniform Distribution versus Data Skew in Distributed Clusters](week-10/02-why-uniform-distribution-matters-transcript.md)
1. [Identifying Data Skew and Hotspots in Production Pipelines](week-10/03-identifying-data-skew-and-hotspots-transcript.md)
1. [Salting: Breaking Up Skewed Partitions for Balanced Execution](week-10/04-mitigation-strategy-salting-transcript.md)
1. [The Shuffle Problem in Large-Scale Joins](week-10/05-optimisation-the-shuffle-problem-in-large-joins-transcript.md)
1. [Broadcast Joins: Eliminating Network Shuffle for Asymmetric Joins](week-10/06-broadcast-joins-transcript.md)
1. [Data Co-location: Proactive Shuffle-Free Join Architecture](week-10/07-designing-for-data-co-location-transcript.md)
1. [Analysing Shuffle Performance and the Partition Count Dilemma](week-10/08-analysing-shuffle-performance-transcript.md)
1. [Data Partitioning Optimisation: Module Synthesis](week-10/09-module-summary-transcript.md)

## Week 11

1. [Distributed Machine Learning: Concepts and Algorithms Overview](week-11/01-module-introduction-transcript.md)
1. [Communication Overhead and Data Movement in Distributed ML](week-11/02-communication-overhead-and-data-movement-transcript.md)
1. [Synchronisation, Stragglers, and Convergence in Distributed Training](week-11/03-synchronisation-and-convergence-issues-transcript.md)
1. [Data Parallelism: Sharding the Dataset Across Workers](week-11/04-data-parallelism-sharding-the-dataset-transcript.md)
1. [Model Parallelism: Splitting the Network Across Devices](week-11/05-model-parallelism-splitting-the-network-transcript.md)
1. [Stochastic Gradient Descent: The Optimisation Engine of ML](week-11/06-review-of-stochastic-gradient-descent-sgd-transcript.md)
1. [Distributing Gradient Calculation: The Push-Update-Pull Cycle](week-11/07-distributing-the-gradient-calculation-transcript.md)
1. [Synchronous vs Asynchronous vs Local SGD Aggregation Strategies](week-11/08-synchronous-vs-asynchronous-aggregation-transcript.md)
1. [Module Summary: Distributed Machine Learning at Scale](week-11/09-module-summary-transcript.md)

## Week 12

1. [Architecting for Distributed Intelligence](week-12/01-architecting-for-distributed-intelligence-transcript.md)
1. [Centralised Learning: The Parameter Server Model](week-12/02-centralised-learning-the-parameter-server-model-transcript.md)
1. [Decentralised Learning: The Ring All-Reduce Strategy](week-12/03-decentralised-learning-the-ring-allreduce-strategy-transcript.md)
1. [Synchronous Training: Consistency and the Straggler Problem](week-12/04-synchronous-training-consistency-and-the-straggler-problem-transcript.md)
1. [Asynchronous Training: Speed vs Convergence Quality](week-12/05-asynchronous-training-speed-vs-convergence-quality-transcript.md)
1. [MirroredStrategy: Single-Node Multi-GPU Training](week-12/06-the-mirroredstrategy-single-node-multi-gpu-transcript.md)
1. [MultiWorkerMirroredStrategy: Multi-Node Cluster Training](week-12/07-multiworkermirroredstrategy-for-multi-node-clusters-transcript.md)
1. [Understanding Distributed Computational Graphs and Device Placement](week-12/08-understanding-distributed-computational-graphs-transcript.md)
1. [Module Summary: Distributed ML Architectures in TensorFlow](week-12/09-module-summary-transcript.md)

## Week 13

1. [The Shift to Real-Time Intelligence](week-13/01-the-shift-to-real-time-intelligence-transcript.md)
1. [Processing for Velocity: What Is a Stream?](week-13/02-processing-for-velocity-what-is-a-stream-transcript.md)
1. [Technical Differences: Windowing vs Global State](week-13/03-technical-differences-windowing-vs-global-state-transcript.md)
1. [Financial Services: Real-Time Fraud Detection](week-13/04-financial-services-real-time-fraud-detection-transcript.md)
1. [E-Commerce: Dynamic Pricing and Personalization](week-13/05-e-commerce-dynamic-pricing-and-personalization-transcript.md)
1. [Kafka as the Streaming Backbone](week-13/06-kafka-as-the-streaming-backbone-transcript.md)
1. [Real-Time Topology with Apache Storm](week-13/07-real-time-topology-with-apache-storm-transcript.md)
1. [Module Summary: Stream Processing Systems](week-13/08-module-summary-transcript.md)

## Stories

1. [Big Data Platforms and Analytics — Story-Based Learning](stories/Story-Based-Learning.md)
