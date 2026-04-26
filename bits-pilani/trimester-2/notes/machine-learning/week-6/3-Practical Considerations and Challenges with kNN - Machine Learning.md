# Practical Considerations and Challenges with kNN

## 1. Distance and similarity choices

| Data type | Common measures | Notes |
|-----------|-----------------|-------|
| **Numeric** (real vectors) | **Euclidean** (L2), **Manhattan** (L1), **Minkowski** | Euclidean is standard; L1 robust to outliers in coordinates |
| **Categorical** | **Hamming** distance (mismatch count), overlap 0/1 | Cannot apply raw Euclidean to unordered categories without encoding |

**Hamming (per position).** For two tuples of categorical attributes, count positions where values **differ**; more mismatches ⇒ more dissimilar.

---

## 2. Feature scaling (mandatory for mixed-scale numeric data)

Distance sums contributions from **every dimension**. If one feature ranges $0$–$1$ and another $10^4$–$10^5$, the large-scale dimension **dominates** the distance; the small-scale feature is effectively ignored.

**Examples (cloud / systems).** Latency (ms) vs request count vs binary flags in **API abuse** scoring; without scaling, “count” swamps “latency.”

**Remedies:**

- **Min–max:** $x' = (x - x_{\min})/(x_{\max} - x_{\min})$ to a fixed range (e.g. $\left[0,\, 1\right]$).
- **Z-score (standardization):** $x' = (x - \mu)/\sigma$ per feature.

Fit scaling statistics on **training** data; apply the same transform at inference.

---

## 3. Choosing k: bias–variance intuition

| k | Bias | Variance | Behavior |
|---|------|----------|----------|
| **1** | Low | **High** | Follows noise; unstable boundary |
| **Large** | **Higher** | Lower | Smoother; may underfit local structure |
| **N** | High | Low | Near-constant **majority** prediction |

**Practical selection:** **cross-validation** over candidate **k** values on held-out folds; no closed-form universal optimum.

---

## 4. Curse of dimensionality

As dimension **d** grows:

- Distances require **O(d)** work per pair.
- In high dimensions, **all pairwise distances** can become similar (concentration), so “nearest” is less meaningful without **many** samples.
- Mitigations: **feature selection**, **PCA** or other reductions, domain-specific embeddings.

**Analogy:** log monitoring with hundreds of engineered features—kNN without reduction often **degrades** and **slows**.

---

## 5. Complexity sketch

Per query (naive): **O(Nd)** for all distances; plus **O(N log k)** or **O(N)** to pick **k** smallest.

Overall: depends heavily on **N**, **d**, and whether **indexing** is used.

---

## 6. Interpretability and when to use kNN

- **Interpretability:** weak—you can cite neighbors, but not a compact global rule.
- **Strengths:** simple, strong **nonlinear** boundaries in low–moderate **d**, no training phase.
- **Good fit:** **low–moderate** dimension, clean scaling, moderate **N** (or ANN infrastructure).

---

## Common Pitfalls / Exam Traps

- Using **Euclidean** on **unencoded** categorical data.
- **Forgetting normalization** on numeric mixed-scale features.
- Choosing **k** without validation; using **k = N** expecting “best” accuracy.
- Ignoring **curse of dimensionality** in high-dimensional text/embeddings without reduction.

---

## Quick Revision Summary

- **Numeric:** Euclidean / Manhattan common; **categorical:** Hamming-type mismatch counts.
- **Scale features** (min–max or z-score) so no dimension dominates L2/L1.
- **k** trades variance (small k) vs bias (large k); tune via **CV**.
- **High d:** expensive distances + weaker neighborhood semantics; reduce features.
- Complexity scales with **N** and **d**; indexing/ANN helps at scale.
- kNN offers **flexible** boundaries but **weak** global interpretability vs rule lists.
