# CP vs AP Systems – Trade-offs in the Real World

## Learning Objectives

By the end of this lesson you will:

1. **Understand** the business logic behind choosing CP or AP
2. **Analyze** the banking (CP) vs social media (AP) classic examples
3. **Apply** a decision framework for your specific application
3. **Recognize** that as an architect, you manage user trust, not just servers

---

## Introduction: The Famous Dilemma

We established that **partition tolerance (P) is mandatory** in clusters. This leaves the most famous dilemma in data engineering:

> **When a network partition occurs: CP (Consistency + Partition Tolerance) or AP (Availability + Partition Tolerance)?**

The right answer depends **entirely on what problem you're trying to solve**.

---

## CP Systems: Consistency Over Availability

### Definition
A **CP system** chooses **consistency** over availability during a network partition.

### The Banking Example

**Scenario**: You have $1,000 in a joint account.
- **You** withdraw $1,000 at ATM in New York
- **Spouse** simultaneously withdraws $1,000 in London
- **Network partition** occurs between NY and London servers

**CP Behavior**: 
- Bank says: *"If I can't guarantee both servers know the exact balance, I'll stop"*
- London ATM shows: **"System Unavailable"**
- Transaction rejected

### Why CP for Banking?

| Reason | Explanation |
|--------|-------------|
| **Financial Integrity** | A stale balance is unacceptable |
| **Legal Requirements** | Regulations demand accuracy |
| **Trust** | Users must trust their money is safe |
| **Cost of Error** | Overdraft = lawsuits, reputation loss |

**Key Principle**: *A bank would rather be offline than wrong.*

---

## AP Systems: Availability Over Consistency

### Definition
An **AP system** chooses **availability** over consistency during a partition.

### The Social Media Like Counter Example

**Scenario**: Viral YouTube video / Instagram post
- Network partition between servers in India and US

**AP Behavior**:
- *"It's OK if count is slightly off for a few minutes, as long as user can still click"*
- User in India sees: **1,000 likes**
- User in US sees: **950 likes**
- System stays **available and responsive**
- Once network fixed → servers sync → eventually agree on **1,050**

### Why AP for Social Media?

| Reason | Explanation |
|--------|-------------|
| **User Experience** | Button must work, even if count is approximate |
| **Scale** | Billions of users = constant partitions |
| **Error Cost** | Wrong like count ≠ financial loss |
| **Engagement** | Broken button = user leaves |

**Key Principle**: *In social media, being fast and always on > perfectly accurate every microsecond.*

---

## Decision Framework: How to Choose

### Choose CP When Data Involves:
- 💰 **Money** (banking, payments, trading)
- 📦 **Inventory** (e-commerce stock, reservations)
- ⚖️ **Legal Records** (contracts, compliance, audit trails)
- 🏥 **Health Records** (patient safety, prescriptions)

**You cannot afford to be inconsistent.**

### Choose AP When Data Involves:
- 📊 **Analytics** (dashboards, metrics, reporting)
- 💬 **Comments/Reviews** (social interactions)
- 📡 **Sensor Logs** (IoT telemetry, monitoring)
- 🔍 **Search Indexes** (eventual consistency acceptable)
- 📈 **Recommendations** (approximate is fine)

**You cannot afford for your system to look broken to users.**

---

## Real-World Hybrid Examples

### Amazon (Both!)
- **Shopping Cart / Checkout**: CP (inventory, payments)
- **Product Reviews / Recommendations**: AP (availability, scale)

### Netflix
- **Playback Control (pause/seek)**: CP (user state must be correct)
- **Recommendations / Browsing**: AP (stale suggestions OK)

### Uber
- **Ride Matching / Payment**: CP (financial correctness)
- **Driver Location / ETA**: AP (approximate location fine)

---

## The Architect's Responsibility

> **As an architect, you aren't just managing servers – you're managing the user's trust.**

The CAP theorem gives you the **framework to decide which type of trust is most important**:
- **Trust in correctness** → CP
- **Trust in availability** → AP

---

## Summary

| Dimension | CP (Consistency) | AP (Availability) |
|-----------|-----------------|-------------------|
| **During Partition** | Returns error / blocks | Returns stale data |
| **Priority** | Correctness | Uptime |
| **Use Case** | Banking, Inventory, Legal | Social, Analytics, Logging |
| **User Trust** | "My data is accurate" | "The system works" |
| **Cost of Error** | Catastrophic | Annoying |

---

## What's Next

We've seen that **P forces us to trade C for A**. But how do we actually **build** these systems? 

Next: **ACID vs BASE** – the two competing philosophies for data integrity that implement these trade-offs in practice.