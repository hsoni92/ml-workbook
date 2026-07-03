# Week 3 – MapReduce Programming Model (Part 3)

## The Reduce Operation: Aggregating State

### Concept
Reduce consolidates multiple values sharing the same key into a single result.

### Formal Definition
```
reduce(key, List(values)) → List(values)
```

### Example: URL Popularity Counter
- **Input**: (URL, [1, 1, 1, 1, ...]) - list of all 1s for that URL
- **Process**: Sum all values in the list
- **Output**: (URL, total_count)

### Key Properties
1. **Aggregation**: Combines values with identical keys
2. **Fold Operation**: Mathematical concept of reducing list to single value
3. **Complete View**: Reducer sees ALL instances of a key across cluster
4. **Massive Data Reduction**: Terabytes → Megabytes of actionable insight

### Comparison: Map vs Reduce

| Aspect | Map | Reduce |
|--------|-----|--------|
| Input | Single key-value | Key + List of values |
| Processing | Independent per element | Aggregation per key |
| Communication | None between mappers | Coordination via shuffle |
| Output | Many pairs | Fewer summarized pairs |
| Scaling | Perfect horizontal | Limited by key distribution |

### Business Value
Transforms "noise" (individual clicks) into "signal" (total page views).
Real-world: 10TB web logs → ranked list of top 100 URLs in MBs.