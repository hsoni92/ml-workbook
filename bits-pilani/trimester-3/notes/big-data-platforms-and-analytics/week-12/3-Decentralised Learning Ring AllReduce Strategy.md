# Decentralised Learning – Ring AllReduce Strategy (Week 12 – Foundations of Distributed Intelligence)

## Learning Objectives
By the end of this lesson you will be able to:
- Explain the architectural motivation behind decentralised all‑reduce strategies  
- Describe how a logical ring enables bandwidth‑optimal gradient synchronization across many workers  
- Identify the communication pattern (successor‑successor‑... ) and its scalability properties  
- Evaluate when ring‑allreduce is preferable to parameter‑server or multi‑node mirrored strategies  
- Recognise implementation considerations such as state‑ful vs. stateless workers  

## Core Concept: From Centralised Servers to a Logical Ring
In large‑scale distributed training we need to aggregate gradients from **hundreds** of workers.  
A **parameter‑server** architecture centralises this aggregation, creating a single point of contention and potential network bottleneck.  

### Decentralised Alternative: Ring Topology
- Each worker holds **one copy** of the model (variables are *stateful* across the ring).  
- Workers are arranged in a **directed ring** (worker i → worker i+1 → … → worker N → worker 0).  
- In each iteration:  
  1. **Send**: Worker i sends its local gradients to worker i+1 (its successor).  
  2. **Add**: The successor adds its own gradients to the received batch.  
  3. **Forward**: Result passes to the next successor.  
  4. **Double‑Pass**: After two rounds around the ring, every worker has accumulated the **full sum of all gradients**.  
- Because each worker only communicates with **two neighbours** (predecessor & successor), the total data sent/received is **independent of the total number of workers** – making the pattern **bandwidth‑optimal**.

## Communication Flow (Simplified)
```
Worker 0 ──►│ Worker 1 ──►│ Worker 2 ──► … │ Worker N (back to 0)
   ↑       │       ↓       │       ↓       │
   └───────┴─────→ (Add) ←───┘       │
                         Add Gradients Twice
```
- **Round 1**: Gradient passes *forward* around the ring.  
- **Round 2**: Gradient passes *backward* around the ring, completing the global sum at every node.  

## Advantages Over Parameter‑Server
| Aspect | Parameter‑Server | Ring AllReduce |
|--------|------------------|----------------|
| **Scalability** | Communication ∝ #workers (central bottleneck) | Communication ∝ constant (per‑worker) |
| **Network Utilisation** | Saturates a single server link | Utilises all inter‑connect links fully |
| **Fault Isolation** | Failure of server crashes whole run | Failures are local; can tolerate stragglers via gossip/redirection |
| **Hardware Fit** | Works well for sparse models | Ideal for dense updates on modern GPU clusters (NVLink, InfiniBand) |

## When to Use Ring AllReduce
- ✅ **Dense** model updates (e.g., vision, NLP, recommender systems) where gradients are large.  
- ✅ **Multi‑node clusters** (10 – 100 + workers) where network topology is high‑speed (InfiniBand) and can form efficient rings.  
- ✅ Scenarios where **communication efficiency** is the primary goal and some extra implementation complexity is acceptable.  

## Implementation Sketch
```python
# pseudo‑code for a worker in a ring of size N
def ring_allreduce_step(local_grad, ring_nodes):
    # Step 1: send to successor
    grad_from_predecessor = recv(predecessor_address)
    # Step 2: add locally & forward
    updated_grad = local_grad + grad_from_predecessor
    send(updated_grad, successor_address)   # forward pass
    
    # Step 2 (reverse): receive from successor, add, send forward again
    grad_from_successor = recv(successor_address)
    final_grad = updated_grad + grad_from_successor
    send(final_grad, predecessor_address)   # backward pass
    
    # After two passes every node has final_grad (the global sum)
    return final_grad
```
- Modern frameworks (Horovod, DeepSpeed) expose this pattern via simple APIs (`hvd.allreduce`, `tensorflow.distribute.RingMaster`).  

## Summary
- **Ring AllReduce** replaces a central server with a **fully distributed, peer‑to‑peer communication pattern**.  
- The logical ring ensures each worker only exchanges with two neighbours, achieving **O(1)** per‑worker communication regardless of cluster size.  
- This makes ring all‑reduce the **communication‑optimal** choice for many‑node dense‑gradient workloads.  
- While newer frameworks hide the complexity behind simple API calls, understanding the underlying pattern is essential for debugging network bottlenecks and designing resilient training pipelines.  

*Next lesson will transition to the practical side: low‑level graph partitioning and device placement in TensorFlow.*