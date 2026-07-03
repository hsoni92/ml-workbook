# Week 3 – MapReduce Programming Model (Part 8)

## Disk-Based Intermediate State: The 3x Write Penalty

### The Performance Cost of Reliability
To achieve fault tolerance, MapReduce writes ALL intermediate data to disk.

### The 3x Write Penalty
- **Map Output**: Written to local disk
- **HDFS Replication**: 3 copies across cluster for safety
- **Result**: 1TB intermediate data = 3TB actual disk writes

### I/O Latency Impact
- **Disk I/O**: Slowest component (from Module 1 hardware constraints)
- **Stop-and-Copy Rhythm**: CPU waits for 3x disk writes before shuffle begins
- **Massive Bottleneck**: Especially for multi-stage jobs

### Visualizing the Cost
```
Mapper Output: 1TB
HDFS Replication: ×3
Actual Disk Writes: 3TB
Time: Disk seek + write + fsync × 3 copies
```

### Optimization Strategy
> "Minimize intermediate state hitting the disk"

**Map-side filtering**:
- Remove junk data early
- Project only needed columns
- Combine before writing (combiner pattern)

### The Spark Connection
> "This exact disk overhead problem is what led to the creation of Apache Spark."

Spark keeps intermediate data in memory (RDDs) to avoid the 3x write penalty.

### Key Takeaway
**MapReduce is resilient BECAUSE it saves everything to disk. MapReduce is SLOW BECAUSE it saves everything to disk.**

Understanding this trade-off separates beginners from professional architects.