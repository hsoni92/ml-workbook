# Module Introduction – HDFS Deep Dive (Module 4)

## Learning Objectives

By the end of this module you will:

1. **Explain** the architecture and internals of Hadoop Distributed File System (HDFS)
2. **Understand** block size configuration and its impact on system performance
3. **Describe** the replication factor (default 3x) and its role in fault tolerance
4. **Explain** the NameNode and DataNode components and their responsibilities
5. **Understand** data locality and its importance for performance
6. **Contrast** HDFS vs Ephemeral local storage in terms of durability and recovery

---

## Introduction: What Is HDFS?

**HDFS (Hadoop Distributed File System)** is the primary distributed storage layer of the Apache Hadoop project. It's designed to store very large datasets reliably across clusters of commodity hardware.

### Design Principles
- **Scalability**: Can scale to thousands of nodes and petabytes of data
- **Fault Tolerance**: Continues operating despite node failures
- **Commodity Hardware Friendly**: Runs on inexpensive, off-the-shelf servers
- **Write Once, Read Many**: Optimized for write-heavy, read-after-write patterns

---

## Block Structure and Replication

### Block Size Configuration

| Configuration | Default | Typical Use Case | Performance Characteristics |
|---------------|---------|------------------|-----------------------------|
| **Small Block Size** | 128 MB | OLTP workloads, low-latency reads | Better; more input splits, finer granularity |
| **Large Block Size** | 256 MB or 512 MB | Big data processing | Reduces number of tasks, better for sequential access |
| **Custom Block Size** | Configurable | Workload-specific | Optimal tuning for specific patterns |

### Block Replication Factor

- **Default Replication Factor**: 3x
- **Why 3?**: 
  - Provides redundancy against 2 simultaneous failures
  - Ensures data survives rack failures
  - Enables read scaling (3 concurrent reads)

### Replication Strategy
1. **First Replica**: Written to current node
2. **Second Replica**: Written to different machine in same rack
3. **Third Replica**: Written to machine in different rack
- **Rack Awareness**: Improves fault tolerance and network efficiency

### Recovery Mechanism
- **Heartbeats**: DataNodes report status to NameNode
- **Failure Detection**: NameNode detects unavailable DataNodes
- **Replication Adjustment**: Missing replicas are recreated on available nodes
- **Self-Healing**: HDFS automatically recovers from failures

---

## HDFS File System Layout

### File Access Process
1. **Client Request**: File system call (e.g., `open()`, `read()`)
2. **Metadata Fetch**: Client contacts NameNode to get file blocks locations
3. **Block Location**: NameNode returns list of DataNode addresses
4. **Data Access**: Client reads/writes directly to DataNodes

### Architecture Components
- **NameNode**: 
  - Master metadata service
  - Stores namespace metadata (file->block mappings)
  - Manages replication factor
  - Single point of metadata (critical component)
- **DataNode**:
  - Worker storage service
  - Stores actual block data
  - Handles read/write requests
  - Reports storage health to NameNode

---

## Data Flow Example

### Writing a New File
1. **Client** requests to create `/data/user123/transactions.log`
2. **NameNode** checks path, allocates block locations
3. **Block Size**: 128MB splits file into chunks
4. **DataNodes**: Receive blocks and store copies
5. **Replication**: Blocks are replicated across 3 nodes
6. **Completion**: NameNode confirms successful write

### Reading a File
1. **Client** requests to read `/data/user123/transactions.log`
2. **NameNode** provides list of DataNode locations
3. **Client** streams data directly from DataNodes
4. **Data Access**: Parallel reads from multiple nodes (if replication allows)

---

## Key Operational Considerations

### Block Management
- **Balancing**: HDFS redistributes blocks when nodes join/leave
- **Storage Utilization**: Automatically monitors free space
- **Decommissioning**: Safe removal of DataNodes with replication adjustment

### Failure Recovery
- **Common Failures**: 
  - **NameNode Crash**: Metadata loss risk
  - **DataNode Crash**: Block replication handled automatically
  - **Network Partition**: Affects read/write availability
- **Recovery Process**: 
  - Restart failed daemon
  - Replication factor restored automatically
  - No data loss due to replication

### Operational Best Practices
- **Monitoring**: Track replication lag, storage utilization
- **Backup**: Secondary NameNode for metadata redundancy
- **Tuning**: Adjust replication factor based on criticality
- **Encryption**: Secure data at rest and in transit

---

## HDFS in Context

### When to Use HDFS
- **Ideal For**:
  - Large, immutable datasets (data lakes)
  - Batch processing workloads
  - Write-once, read-many scenarios
  - Cost-sensitive storage at scale

### When to Consider Alternatives
- **Need Low Latency Reads**: HDFS not optimized for random small reads
- **High Change Rate Workloads**: Not designed for frequent updates
- **Strict ACID Requirements**: Not designed for transactional systems
- **Small File Problem**: Inefficient for many small files

### Complementary Systems
- **S3/ADLS**: Object storage solutions with similar durability
- **Alluxio**: Memory-centric storage layer for faster access
- **MinIO**: Modern S3-compatible object storage

---

## Operational Metrics to Track

| Metric | Importance | Target/Pattern |
|--------|------------|----------------|
| **Replication Factor** | Describes redundancy level | 3x default, adjust for criticality |
| **Storage Utilization** | % of capacity used | < 80% to avoid spills |
| **Heartbeat Frequency** | Health monitoring interval | 3-10 seconds |
| **Available Capacity** | Free space for new writes | > 20% headroom |
| **Replication Lag** | Delay in replication completion | Minimal (< 1 min) |
| **DataNode Degraded** | Nodes with partial replication | 0 |

---

## Summary of HDFS Design Philosophy

### 1. **Commodity Hardware Friendly**
- Runs on inexpensive, commodity servers
- Designed to tolerate hardware failures

### 2. **Scalability by Design**
- Scales linearly with cluster size
- Metadata operations remain performant

### 3. **Fault Tolerance Through Simplicity**
- Simple failure detection and recovery
- Self-healing replication mechanism
- No complex consensus protocols required

### 4. **Optimize for Sequential Access**
- Streaming large files efficiently
- Sequential read/write patterns favored

### 4. **Separation of Compute and Storage**
- Storage (HDFS) decoupled from compute (YARN/MapReduce)
- Enables independent scaling of storage vs processing

---

## Key Takeaways

- **HDFS is the Foundation**: The storage layer underpins all Hadoop-based processing
- **Durability Through Redundancy**: 3x replication ensures data safety
- **Performance Through Simplicity**: Avoids complex consensus protocols
- **Scalability Through Linearity**: Seamlessly handles growth in data/size
- **Operational Resilience**: Designed to survive hardware failures gracefully

HDFS represents the **storage backbone** of big data systems, enabling the massive scale required for modern data processing pipelines.

---