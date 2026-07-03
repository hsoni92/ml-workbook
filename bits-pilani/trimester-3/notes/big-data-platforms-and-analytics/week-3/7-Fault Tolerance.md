# Week 3 – MapReduce Programming Model (Part 7)

## Fault Tolerance: Design for Failure in Action

### The Reality
- 1000 commodity servers → hardware failure is statistically certain
- Hard drives crash, power supplies fail, network cables unplug

### MapReduce's Implementation

#### 1. Heartbeat Monitoring
- Master node tracks worker health via periodic heartbeats
- Failed check-in = heartbeat failure
- Master doesn't cancel job - it reassigns tasks

#### 2. Task Reassignment
- Master identifies failed node's tasks from metadata map
- HDFS 3x replication provides backup data location
- New worker picks up from same split

#### 3. Functional Purity Enables Reliability
- **Pure Functions**: Same input → same output, no side effects
- **Determinism**: Rerunning task produces identical results
- **Calculator Analogy**: 5+5=10 always, regardless of calculator state

### Why This Works
```
Failure Detection → Task Identification → Backup Data Location → Rerun on New Node
     ↓                   ↓                    ↓                   ↓
 Heartbeat           Metadata              HDFS 3x            Pure Functions
 Timeout             Map                   Replication        = Identical Output
```

### The Trade-off
> "MapReduce achieves fault tolerance not by using expensive, unbreakable hardware, but by using smart software."

- **Pro**: Commodity hardware + software resilience
- **Con**: Performance cost from disk-based checkpointing