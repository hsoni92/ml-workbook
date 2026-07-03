# Week 3 – MapReduce Programming Model (Part 4)

## The Shuffle and Sort Phase: The Bridge

### Concept
The shuffle and sort phase connects map output to reduce input by partitioning and grouping data by key.

### Two Critical Steps

#### 1. Partitioning
- **Formula**: `ReducerID = Hash(Key) % NumberOfReducers`
- **Guarantee**: All instances of same key go to same reducer
- **Example**: With 3 reducers, `hash("index.html") % 3 = 0` → all index.html to Reducer A

#### 2. Sorting
- **Grouping**: All values for same key are grouped together
- **Efficiency**: Reducer reads perfectly organized stream
- **Result**: Reducer processes one key at a time with all its values

### The Network Tax
> "Thousands of mappers sending data to hundreds of reducers simultaneously creates massive cross-cluster traffic."

- Most network-intensive phase
- Primary bottleneck in MapReduce jobs
- Where you "pay the network tax" from Module 1

### Performance Impact
- Often the slowest part of the job
- Performance tuning focuses on minimizing shuffle data
- Strategies: filter early, combine on map side, compress output