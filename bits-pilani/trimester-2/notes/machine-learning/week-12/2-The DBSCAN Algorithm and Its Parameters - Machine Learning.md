# The DBSCAN Algorithm: Steps, Strengths, and Limits

## 1. Cluster definition (informal)

A **DBSCAN cluster** satisfies **connectivity** via density-reachable points from a **core** seed and **maximality** (all density-reachable points from any core in the component are included). Implementation details follow these principles to grow regions.

---

## 2. High-level algorithm

1. Label every point **core / border / noise** using \(\varepsilon\) and **minPts**.
2. Pick an **unvisited core** point; start a new cluster; **expand** by adding all **density-reachable** points via **breadth/depth** search over **core** neighbors within \(\varepsilon\).
3. Repeat for unassigned cores. Border points attach to adjacent clusters; noise stays unassigned.

---

## 3. Strengths

- **Arbitrary** shapes (rings, moons) if separated by **low density**.
- **Noise** points explicitly identified—useful for **cleaning** telemetry.
- **No k** required—number of clusters **emerges**.

**Example:** anomaly-heavy **API** logs where normal traffic forms dense manifolds and attacks are sparse.

---

## 4. Weaknesses

- **Varying density:** fixed \(\varepsilon\) may merge dense and sparse regions incorrectly or fragment one natural cluster.
- Parameter tuning: **heuristics** (e.g. **minPts** \(\geq d+1\) as a starting rule of thumb for \(d\) dimensions), domain knowledge, grid search on validation criteria.
- **Complexity:** naive neighborhood queries can approach **O(n²)** in worst cases; **spatial indexes** help.

---

## 5. When not to use DBSCAN

Uniform **globular** blobs with **no** noise may be **simpler** with k-means. **Huge**, **ultra-high-D** sparse data may need specialized NN structures or other methods.

---

## Common Pitfalls / Exam Traps

- Expecting DBSCAN to **auto-tune** \(\varepsilon\)**—it does not.
- Ignoring **spatial index** when \(n\) is large.
- Applying to **uniform random** data—everything becomes noise or one blob depending on params.

---

## Quick Revision Summary

- DBSCAN **labels** points then **expands** from **core** seeds.
- Finds **arbitrary** shapes and **noise** without **k**.
- **Fixed** \(\varepsilon\), **minPts** limit **multi-density** data.
- Tuning is **heuristic** + domain.
- **Complexity** manageable with indexing; naive can be **quadratic**.
