# The Fallacies of Distributed Computing – Distributed Systems (Module 2)

## Learning Objectives

By the end of this video you will:

1. **List** the eight fallacies of distributed computing
2. **Explain** why assuming network reliability is the biggest mistake
3. **Describe** the latency and bandwidth fallacies with real-world analogies
4. **Understand** why security, topology, and administration assumptions are dangerous
5. **Adopt** a "design for failure" pessimist mindset for distributed systems architecture

---

## Introduction: Why Big Data Projects Fail

Many big data projects fail before they even start because developers carry over assumptions from single-machine programming into distributed systems. These assumptions are **common sense things that developers assume are true, but in the world of distributed systems, they are dangerous lies.**

---

## The Eight Fallacies of Distributed Computing

### Fallacy #1: The Network is Reliable

**The Assumption**: On a laptop, saving a file to hard drive works 99.999% of the time.

**The Reality**: In a cluster, messages travel through wires, routers, and switches. 
- Cables can be accidentally unplugged
- Switches can overheat
- Network partitions occur regularly

**The Consequence**: If your code assumes messages always arrive, your system will crash at the first glitch.

**The Fix**: **Design your system to expect that messages will be lost.**

### Fallacy #2: Latency is Zero

**The Assumption**: Moving data from memory to CPU is nearly instantaneous.

**The Reality**: Sending a request to another node takes time.
- **Analogy**: Difference between asking someone in the same room for a pen vs. sending a letter across the country
- Even if the letter travels fast, the round trip takes time

**The Impact**: Every distributed call adds latency that doesn't exist in single-node systems.

### Fallacy #3: Bandwidth is Infinite

**The Assumption**: We have fiber optics, so bandwidth is unlimited.

**The Reality**: Even giant pipes have limits.
- **Analogy**: No matter how big a water pipe is, if you try to push the entire ocean through it at once, it'll burst
- Moving a petabyte of data across the network for a simple calculation clogs the system

**The Solution**: **Data locality** (learned in Module 1) - move computation to data, not data to computation, because bandwidth is precious.

### Fallacy #4: The Network is Secure

**The Assumption**: Internal networks are safe from attacks.

**The Reality**: Networks are constantly being hacked, probed, and compromised.

### Fallacy #5: Topology Doesn't Change

**The Assumption**: The network structure remains constant.

**The Reality**: Servers are added and removed daily. Topology changes continuously.

### Fallacy #6: There is One Administrator

**The Assumption**: A single person/team manages the entire network.

**The Reality**: Different teams manage different parts. No one person has the master key.

### Fallacy #7: Transport Cost is Zero

**The Assumption**: Moving data has negligible cost.

**The Reality**: Serialization, deserialization, encryption, and network overhead all add significant cost.

### Fallacy #8: The Network is Homogeneous

**The Assumption**: All network components are the same.

**The Reality**: Mixed hardware, protocols, and generations create complexity.

---

## The Pessimist's Mindset

### Key Takeaway
**To be a successful big data architect, you have to be a bit of a pessimist.**

You must assume:
- The network **will** fail
- Latency **will** be high
- Bandwidth **will** be limited

### Why Pessimism Wins
- **Optimistic systems** crash when reality violates assumptions
- **Pessimistic systems** survive because they expect and handle failures

---

## Real-World Impact

### Single-Node vs. Cluster
| Assumption | Single Node | Cluster |
|------------|-------------|---------|
| Network reliability | 99.999% | Not guaranteed |
| Latency | Near zero | Milliseconds to seconds |
| Bandwidth | Near infinite | Constrained by pipes |
| Security | Controlled | Constantly attacked |
| Topology | Static | Dynamic |
| Administration | Centralized | Distributed |

---

## What's Next

In the next lesson, we'll look at how we build systems that survive these fallacies by **defining partition tolerance** - learning how to keep the system running even when the roads between our servers are completely blocked.

---

## Summary

The fallacies of distributed computing are not academic curiosities - they are the difference between systems that work in production and systems that fail catastrophically. The first step to becoming a distributed systems architect is **unlearning** the assumptions that work on a single machine but are dangerous lies in a cluster.

**Remember**: The network is not reliable, latency is not zero, and bandwidth is not infinite. Design accordingly.