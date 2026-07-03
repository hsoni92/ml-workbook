# Week 3 – MapReduce Programming Model (Part 6)

## Real-World Case Study: Web Log Analysis

### Business Problem
Find the most popular URLs from 10TB of raw server logs.

### Three-Step MapReduce Solution

#### Step 1: Map Logic
```python
# Input: log line → Output: (URL, 1)
def map(line):
    url = extract_url(line)
    return [(url, 1)]
```

#### Step 2: Shuffle Logic (Automatic)
- Framework handles: `hash(URL) % num_reducers`
- All pairs for "google.com" → Reducer A
- All pairs for "bits.edu" → Reducer B

#### Step 3: Reduce Logic
```python
# Input: (URL, [1, 1, 1, ...]) → Output: (URL, total)
def reduce(url, counts):
    return [(url, sum(counts))]
```

### Results Achieved
1. **Scalability**: 10TB handled by adding nodes
2. **Simplicity**: Developer writes only extract + sum logic
3. **Resilience**: Failed mappers auto-restart without job failure

### End-to-End Flow
```
10TB HDFS → 128MB Splits → Map (extract URLs) → Shuffle (group by URL)
→ Reduce (sum counts) → Ranked URL List (MBs)
```

### Three Wins
- **Scalability**: Horizontal scaling via commodity hardware
- **Simplicity**: Pure functional logic, framework handles distribution
- **Resilience**: Automatic failure recovery through determinism