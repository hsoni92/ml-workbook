# Week 3 – MapReduce Programming Model (Part 5)

## Logical Data Flow: Input Splits and Map Phase

### Stage 1: Input Splits
- **Problem**: 10TB file cannot be processed by one computer
- **Solution**: Auto-split into 64MB/128MB chunks (matching HDFS block size)
- **Analogy**: Encyclopedia → one chapter per student
- **Result**: Thousands of parallel tasks

### Stage 2: Map Phase
- **Assignment**: Each split to a worker node
- **Data Locality**: Run task where data lives (avoid network tax)
- **Processing**: Apply custom map logic to local split
- **Output**: Intermediate key-value pairs per split

### The Pipeline So Far
```
10TB File → Splits (128MB each) → Map Tasks (parallel) → Intermediate Pairs
```

### Key Design Principle
> "Move computation to data, not data to computation"

This is the practical application of the data locality principle from Module 1.