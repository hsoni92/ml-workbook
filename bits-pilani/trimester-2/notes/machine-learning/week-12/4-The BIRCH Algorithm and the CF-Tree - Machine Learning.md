# BIRCH: The CF-Tree and Insertion Mechanics

## 1. CF-tree role

A **CF-tree** is a **height-balanced** tree (often **B+-tree**-like) whose **leaves** hold **Clustering Features (CFs)** summarizing **tight** subclusters of the stream. **Internal** nodes store **aggregated** CFs of subtrees for **routing** new points.

**Purpose:** avoid **linear scan** over thousands of micro-clusters for each insertion—**logarithmic** path length in tree depth.

---

## 2. Branching factor and threshold

| Hyperparameter | Role |
|----------------|------|
| **Branching factor** | Max **children** / **entries** per node (breadth of tree) |
| **Threshold T** | Max **radius** (or diameter) of a **leaf** CF—controls **tightness** of micro-clusters |

**Insertion:** traverse from **root**, choose child whose **centroid** is **closest** until **leaf**; if point fits within **T** of a leaf CF, **absorb** (update **N, LS, SS**). Else **new** leaf CF or **split** node if over capacity \(\Rightarrow\) may **propagate** splits upward.

---

## 3. End-to-end flow

1. **Stream** points into CF-tree (Phase 1).
2. Optional **rebalance / condense** (Phase 2).
3. Cluster **leaf** CFs with a **batch** method (k-means, hierarchical, etc.) (Phase 3).
4. **Second scan:** assign every original point to nearest **final** cluster representative (Phase 4).

---

## 4. Limitations

- **Order-sensitive:** reordering inputs can change the tree and **micro-clusters**.
- **Spherical bias** at micro-cluster level (radius threshold).
- Approximate **global** structure—may miss some **non-convex** macro shapes unless micro-clusters are fine enough.

---

## Common Pitfalls / Exam Traps

- Setting **T** too large \(\Rightarrow\) **under**-segmented micro-clusters; too small \(\Rightarrow\) huge tree.
- Forgetting **Phase 4**—summary-only clustering without reassignment loses **point-level** accuracy.
- Using BIRCH when **exact** pairwise linkage is required.

---

## Quick Revision Summary

- **CF-tree** indexes **CF** summaries; **B+**-style balance reduces depth.
- **Branching factor** caps fan-out; **threshold T** caps micro-cluster **radius**.
- **Insert** by nearest-centroid routing; **splits** propagate like B-tree.
- **Global** clustering runs on **leaves**; **second pass** assigns raw points.
- **Limitations:** **order** dependence, **spherical** micro-clusters, approximation.
