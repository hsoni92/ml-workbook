# Clustering Details: Proximity, Representations, and Algorithm Choice

## 1. Three ingredients for success

1. **Algorithm** (k-means, hierarchical, DBSCAN, BIRCH, …).
2. **Proximity** definition (distance, kernel, linkage).
3. **Evaluation** of cluster quality (internal indices, stability, domain checks).

No single algorithm fits **all** cluster shapes or scales.

---

## 2. Data matrix vs dissimilarity matrix

**Data matrix:** rows = **objects**, columns = **features** (standard table).

**Dissimilarity (proximity) matrix:** rows and columns = objects; entry \((i,j)\) = distance or dissimilarity \(d_{ij}\). Diagonal **0** if identical to self.

**Use:** hierarchical methods often start from **pairwise** dissimilarities (size \(n \times n\)).

---

## 3. Common distances (numeric)

| Name | Formula idea | Notes |
|------|----------------|-------|
| **Euclidean (L2)** | \(\sqrt{\sum (x_i-y_i)^2}\) | Default for continuous |
| **Manhattan (L1)** | \(\sum |x_i-y_i|\) | Axis-aligned paths; robust-ish |
| **Minkowski** | Generalizes L1/L2 | Parameter \(p\) |

**Categorical data:** Hamming-style mismatch counts; other measures after encoding.

---

## 4. Choosing an algorithm (criteria)

| Criterion | Implication |
|-----------|-------------|
| **Cluster shape** | Spherical \(\Rightarrow\) k-means; arbitrary / noise \(\Rightarrow\) DBSCAN |
| **Scalability** | Huge \(n\): BIRCH / sampling; agglomerative costly (\(O(n^3)\) naive) |
| **Noise** | k-means **sensitive** to outliers; DBSCAN labels noise |
| **Parameters** | k-means needs **k**; DBSCAN needs **eps**, **minPts** |
| **Order sensitivity** | Some algorithms (e.g. BIRCH) **vary** with input order |
| **In-memory vs disk** | k-means often assumes RAM-resident data |

**Ideal algorithm checklist** (theory): scalable, minimal parameters, noise-robust, arbitrary shapes—**no** method satisfies all simultaneously.

---

## 5. Internal quality (conceptual)

Good partitions: **high cohesion** within clusters, **high separation** between—measured via silhouette, SSE, linkage height, etc. (algorithm-specific).

---

## Common Pitfalls / Exam Traps

- Building a **full** \(n \times n\) matrix for **million** points—**quadratic** memory.
- Using **Euclidean** without **scaling** heterogeneous features.
- Picking k-means for **non-convex** clusters without transformation.

---

## Quick Revision Summary

- Success needs **algorithm + proximity + evaluation**.
- **Data matrix** vs **dissimilarity matrix** representations.
- **Euclidean / Manhattan** common for numeric data.
- Algorithm choice depends on **shape**, **scale**, **noise**, **parameters**.
- Full pairwise storage **does not scale** to huge \(n\).
