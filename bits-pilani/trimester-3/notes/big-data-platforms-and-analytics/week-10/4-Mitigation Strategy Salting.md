# Mitigation Strategy: Salting (Week 10 – Advanced Partitioning)

## Learning Objectives
By the end of this lesson you will be able to:
- Explain the concept and purpose of data salting for hotspot mitigation
- Apply a systematic 3-step salting technique to redistribute skewed data
- Design appropriate salt ranges based on cluster capacity and skew characteristics
- Implement salting in Spark transformations while preserving join correctness
- Recognize trade-offs between salting benefits and added code complexity

## Core Concept: The Salting Technique
Salting artificially breaks large skewed partitions by adding random suffixes to keys, forcing an even data distribution across more workers.

### 3-Step Salting Process
1. **Identify Skewed Key**: Detect keys with disproportionately high frequency
2. **Add Salt**: Append a random suffix during processing
   - Example: `USA` → `USA_1`, `USA_2`, `USA_3` (using modulo operation on a salt range)
3. **Redistribute**: New unique keys spread across multiple partitions
   - Each salted variant routes to different hash buckets
   - Workload parallelized across previously overwhelmed nodes

### Salting Implementation Example
```python
def apply_salt(key, salt_range=100):
    salt_suffix = hash(key) % salt_range
    return f"{key}_s{salt_suffix}"
    
# In transformation pipeline
rdd = rdd.map(lambda row: (apply_salt(row.key), row.value))
```

### Trade-Offs and Considerations
- **Benefits**: Eliminates hot partitions, improves parallel execution
- **Complexity**: Requires key manipulation logic and post-processing adjustments
- **Replication**: Small lookup tables must be expanded to match salted keys
- **Best Practice**: Choose salt range based on target partition count and skew severity

## Salting in Join Operations
When salting join keys:
- **Expand Small Tables**: Replicate lookup data for each salted variant
- **Preserve Join Semantics**: Aggregate results and consolidate by original key
- **Example Workflow**:
  1. Salt both join keys
  2. Perform distributed joins on salted keys
  3. Aggregate results back to original key space

## When to Use Salting
- High-skew scenarios with >10:1 partition size ratios
- Join keys with extremely uneven distributions
- Production pipelines where job stability is critical
- Situations where broadcast joins are not applicable (large lookup tables)

## Summary
Salting is your **primary manual tool** for redistributing skewed data across the cluster. While it adds code complexity, it provides:
- Dramatic improvements in execution stability
- Near-linear scalability restoration
- A scalable solution when other optimizations (broadcast) are insufficient

"This technique transforms an unstable, straggler-prone pipeline into a robust, parallelized workflow."