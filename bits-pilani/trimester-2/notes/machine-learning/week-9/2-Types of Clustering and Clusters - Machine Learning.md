# Types of Clustering Methods and Types of Clusters

## 1. Ambiguity: how many clusters?

The same point set may admit **2**, **4**, or **6** “natural” groupings depending on **scale** and **similarity definition**. Cluster count is partly a **user** / **domain** choice.

---

## 2. Hard vs soft clustering

| Type | Assignment |
|------|------------|
| **Hard** | Each point in **exactly one** cluster (e.g. k-means) |
| **Soft** | Points may belong to **several** clusters with **weights** (e.g. Gaussian mixture) |

**Soft clustering extras:** **degree** (max number of clusters per point), **strength** of membership.

---

## 3. Flat vs hierarchical

| Type | Structure |
|------|-----------|
| **Flat (partitional)** | Single partition into **k** non-overlapping groups (k-means) |
| **Hierarchical** | **Nested** tree of clusters (merge or split) |

**Hierarchical modes:**

- **Agglomerative (bottom-up):** start with points as singletons; **merge** similar groups.
- **Divisive (top-down):** start with one cluster; **split** recursively.

**Dendrogram:** tree recording merge/split order and **heights** (often dissimilarity).

---

## 4. Similarity basis

- **Distance:** close \(\Rightarrow\) similar (Euclidean, Manhattan, …).
- **Connectivity:** points link if **reachable** along dense paths (density-based methods).

---

## 5. Sequential vs simultaneous algorithms

**k-means** iterations are **sequential** (assign then update). Some steps in other pipelines can be **parallelized** (e.g. distance blocks)—implementation-dependent.

---

## 6. Types of cluster **shapes** (conceptual)

| Type | Idea |
|------|------|
| **Center-based** | Point closer to its cluster **centroid** than to other centroids (k-means view) |
| **Well-separated** | Every point closer to **all** in-cluster points than to any out-of-cluster point |
| **Contiguous (chain)** | Similarity along **chains** of neighbors; allows **non-convex** shapes |
| **Density-based** | Cluster = region reachable through **dense** corridors (DBSCAN family) |

---

## Common Pitfalls / Exam Traps

- Confusing **hierarchical structure** with **soft** assignment—they are orthogonal axes.
- Assuming **k-means** finds **density** or **arbitrary** shapes—it targets **centroid** compactness.

---

## Quick Revision Summary

- **Hard/soft**, **flat/hierarchical**, **distance/connectivity** are independent design choices.
- **Agglomerative** merges; **divisive** splits; **dendrogram** visualizes hierarchy.
- Cluster **types:** center-based, well-separated, contiguous, density-based.
- **Ambiguity** in cluster count is normal—depends on scale and task.
