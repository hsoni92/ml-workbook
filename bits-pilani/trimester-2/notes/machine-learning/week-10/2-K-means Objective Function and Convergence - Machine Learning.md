# k-Means: Objective Function, Alternating Optimization, and Local Optima

## 1. Within-cluster sum of squared errors (SSE)

Let \(S_j\) be indices of points in cluster \(j\), centroid \(\boldsymbol{\mu}_j\).

\[
\text{SSE} = \sum_{j=1}^{k} \sum_{i \in S_j} \|\mathbf{x}_i - \boldsymbol{\mu}_j\|^2
\]

**k-means** seeks a partition and centroids that **minimize SSE** (non-convex global problem; algorithm finds **local** minima).

---

## 2. Alternating optimization

Each iteration fixes one part and optimizes the other:

| Step | Fixed | Optimized |
|------|-------|-----------|
| **Assignment** | Centroids | Each point to **nearest** centroid \(\Rightarrow\) **lowers** SSE given centroids |
| **Update** | Assignments | Centroid = **mean** \(\Rightarrow\) **optimal** center for assigned points (minimizes sum of squares to that set) |

**Monotonicity:** SSE **does not increase** each full iteration (typically decreases until convergence).

---

## 3. Local vs global optimum

k-means is **greedy** and **non-convex**: different **initializations** can yield **different** clusterings with **different** SSE.

**Symptom:** visually “wrong” partition (e.g. merging two natural blobs) while algorithm **converged**—no error thrown.

**Mitigations (preview):** multiple random restarts; **k-means++** initialization; better **k**.

---

## Common Pitfalls / Exam Traps

- Claiming k-means **always** finds **global** SSE minimum—**false**.
- Confusing **iteration** limit with **k**.
- Forgetting that **assignment** and **mean update** each **decrease or maintain** SSE.

---

## Quick Revision Summary

- **Objective:** minimize **SSE** of points to their cluster centroids.
- **Assignment** step minimizes distances given centroids; **update** sets **means**.
- **Alternating** descent on SSE; converges to **local** minimum.
- **Initialization** matters; global optimum **not guaranteed**.
- High-dimensional visualization hides bad local minima—use **SSE** and **domain** checks.
