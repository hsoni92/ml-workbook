# Identifying Data Skew and Hotspots (Week 10 – Advanced Partitioning)

## Learning Objectives
By the end of this lesson you will be able to:
- Formally define data skew and identify its symptoms in distributed workloads
- Detect hotspots using cluster resource metrics and Spark UI indicators
- Distinguish between normal task duration variance and pathological stragglers
- Apply diagnostic techniques to isolate skewed partitions before optimization

## Core Concept: Formal Definition of Data Skew
Data skew occurs when a small subset of partitions contains a disproportionately large portion of the data. This creates an **imbalance in processing load** that manifests as:

- One or few partitions holding >50% of total records
- A small number of keys appearing far more frequently than others
- Partition size variance exceeding 3× between largest and smallest partitions

## Symptom Patterns: How to Spot Skew in Practice
### 1. Resource Utilization Anomalies
- **CPU Hotspots**: One executor reaches 100% CPU while others remain idle (<10% utilization)
- **Memory Pressure**: Single task experiences excessive GC pressure or OOM events
- **Network Asymmetry**: Disproportionate network I/O on specific nodes

### 2. Spark UI Indicators
- **Task Duration Disparity**: Large gap between `max` and `median` task times in stage summary
- **Shuffle Skew**: One reducer receives vastly more data than others
- **Skewed Partition Size**: Significant deviation in partition byte sizes shown in diagnostics

### 3. Temporal Patterns
- **Progress Stalling**: Job stuck at 99% completion for extended periods
- **Tail Latency**: Median task completes quickly, but final 1% takes disproportionately long
- **Stage Time Distribution**: One stage dominates total execution time asymmetrically

## Diagnostic Methodology
1. **Profile Cluster Metrics**: Use Ganglia/CloudWatch to monitor per-node CPU/memory utilization
2. **Analyze Spark UI**: Navigate to Stages tab → examine task duration distributions
3. **Check Shuffle Metrics**: Review shuffle read/write bytes per task to identify imbalanced data movement
4. **Validate with Sample Data**: Sample key frequencies to confirm disproportionate key occurrences

## Practical Example: Real-World Log Analysis
- **Observation**: Job completes 99% in 2 minutes, then stalls for 10+ minutes at final stage
- **Spark UI Check**: Max task time = 12 minutes, Median task time = 2 seconds → extreme skew
- **Root Cause**: One partition contained 87% of join key occurrences
- **Solution Path**: Apply salting technique (introduced in next lesson) to redistribute load

## Key Takeaway
Data skew is a **diagnosable performance killer** that masquerades as normal execution. By systematically monitoring resource utilization, task duration patterns, and Spark UI metrics, you can **identify hotspots early** and apply targeted mitigation strategies before they cause production failures.