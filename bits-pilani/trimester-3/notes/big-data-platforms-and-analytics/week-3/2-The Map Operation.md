# Week 3 – MapReduce Programming Model (Part 2)

## The Map Operation: Transforming Data

### Concept
The map phase transforms raw data into structured key-value pairs. Each element is processed independently.

### Formal Definition
```
map(key, value) → List(key, value)
```

### Example: URL Extraction from Web Logs
- **Input**: Raw server log lines
- **Process**: Parse each line, extract URL, emit (URL, 1)
- **Output**: Sea of (URL, 1) pairs

### Key Properties
1. **Independence**: No communication between mappers
2. **Parallelism**: Scales linearly with nodes
3. **Determinism**: Pure functions produce same output for same input

### Data Locality
- Framework runs map tasks on nodes storing the data split
- Avoids network transfer of raw data
- Major performance optimization

### Scaling Behavior
> "If you have twice as much data, you don't need a faster computer. You just add more nodes and the mapping finishes in the same amount of time."

### Why It Works at Scale
- Each mapper handles its own split
- No coordination needed during map phase
- Pure functional transformations enable perfect horizontal scaling