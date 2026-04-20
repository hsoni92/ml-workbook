# Density-Based Clustering and DBSCAN (Concepts)

## 1. Motivation

**k-means** assumes roughly **spherical** groups around centroids and is **outlier-sensitive**. **Hierarchical** methods are **expensive** at large \(n\) and depend on **linkage** choice.

**Density-based** view: a **cluster** is a **dense** region of points separated by **sparse** regions—supports **arbitrary** shapes and explicit **noise** labels.

**DBSCAN** = *Density-Based Spatial Clustering of Applications with Noise*.

---

## 2. Density parameters

| Parameter | Role |
|-----------|------|
| **eps (\(\varepsilon\))** | Radius of neighborhood around a point |
| **minPts** (MinPts) | Minimum **count** of points (including center) in \(\varepsilon\)-ball to call the neighborhood “dense enough” for a **core** point |

**Intuition:** a **city center** is “dense” if many people live within a fixed radius; a **desert** is sparse.

---

## 3. Point types

- **Core:** \(\varepsilon\)-neighborhood contains **≥ minPts** points (per common definition counting the point itself—implementations vary slightly).
- **Border:** not core, but lies in \(\varepsilon\)-neighborhood of **some** core point.
- **Noise / outlier:** neither core nor border.

---

## 4. Density-reachability (foundation)

- **Directly density-reachable:** \(q\) is core and \(p\) lies within \(\varepsilon\) of \(q\) \(\Rightarrow\) \(p\) is reachable **from** \(q\) in one hop (**asymmetric**: border may not reach back).
- **Density-reachable:** chain of core points linking \(q\) to \(p\).
- **Density-connected:** \(p\) and \(q\) both density-reachable from some **o** \(\Rightarrow\) **symmetric** relation useful for tying border regions of one cluster.

These definitions underpin how DBSCAN **grows** clusters from seeds.

---

## Common Pitfalls / Exam Traps

- Using **same** \(\varepsilon\) for **all** densities—DBSCAN struggles with **varying density** clusters.
- Miscounting **minPts** (center included or not)—always check **library** docs.

---

## Quick Revision Summary

- **Density clustering:** dense regions + sparse separators; **non-convex** shapes possible.
- **DBSCAN** uses **\(\varepsilon\)** and **minPts** to define density.
- **Core / border / noise** classification.
- **Reachability** chains build clusters; **connectivity** relates border points.
- **Global** \(\varepsilon\) is a limitation for **multi-density** data.
