# Choosing k in k-Means: Heuristics, Complexity, and Best Practices

## 1. Why k is hard

In **low dimensions**, you may **see** natural groups. In **high dimensions**, visualization fails; **k** becomes a modeling choice tied to **business** actionability.

---

## 2. Elbow method (SSE vs k)

**Procedure:**

1. Run k-means for \(k = 1, 2, \ldots, K_{\max}\).
2. Record **total SSE** (or **inertia**) for each **k**.
3. Plot SSE vs **k**.
4. Look for an **elbow**—where marginal SSE drop **slows** (diminishing returns).

**Interpretation:** beyond the elbow, extra clusters **over-segment** without much error reduction.

**Caveats:**

- Elbow can be **unclear** (smooth curve).
- Does **not** guarantee optimal **k**—**heuristic** only.
- At \(k = n\), SSE \(\to 0\) (each point its own cluster)—meaningless.

**Domain pairing:** combine elbow with **expert** judgment (e.g. “we can run **three** marketing plays, not fifteen”).

---

## 3. Other signals

- **Silhouette** score (cohesion vs separation).
- **Stability** across bootstrap samples.
- **Business** constraints (segments must be **actionable**).

---

## 4. Pros and cons of k-means

**Pros:** simple, **fast** for moderate \(n\), **guarantees convergence**, scales reasonably with good implementations.

**Cons:** must set **k**, **local minima**, **sensitive** to outliers and scaling, **spherical** bias.

---

## 5. Time complexity (standard view)

Per iteration: assign each of \(n\) points to one of **k** centroids in \(d\) dims \(\Rightarrow\) **O(nkd)**.
With **I** iterations: **O(Iknd)**.

Derivation sketch: each point compares to **k** centroids (**k** distance computations in **d** dims); repeat for **n** points; repeat **I** times. Centroid update is **O(nd)** per iteration (aggregate then divide).

---

## 6. Best practices (summary)

- **Scale** features.
- Try **k-means++** and **multiple** restarts.
- Choose **k** via elbow / silhouette / domain.
- **Validate** clusters with stakeholders.

---

## Common Pitfalls / Exam Traps

- Treating elbow as **proof** of optimal **k**.
- Forgetting SSE **always** decreases with larger **k** until \(k=n\).
- Reporting **O(n²)** for standard k-means—wrong for textbook Lloyd’s per iteration.

---

## Quick Revision Summary

- **k** is user-chosen; high-D needs **heuristics + domain**.
- **Elbow:** plot **SSE vs k**; knee suggests **k**; not guaranteed.
- **Silhouette**, stability, and **experts** complement elbow.
- **Complexity:** **O(Iknd)** typical per run.
- **Strengths:** speed, simplicity; **weaknesses:** **k**, shape bias, outliers.
