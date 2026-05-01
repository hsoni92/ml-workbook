# Random Forest — The Village of Independent Experts 🌲🌲🌲

## Context
**Source:** [ml-workbook/week-7/3-Random Forest](https://github.com/hsoni92/ml-workbook/blob/main/bits-pilani/trimester-2/notes/machine-learning/week-7/3-Random%20Forest%20In-Depth%20Building%20an%20Ensemble%20of%20Diverse%20Trees%20-%20Machine%20Learning.md)
**Topic:** Random Forest — bagging + random feature selection, tree diversity, vs Bagging
**Date:** 2026-05-01

---

## The Story

### The Problem with Bagging Alone

Bagging creates many trees. But here's the catch: **all those trees still look similar**.

Think of it like this — you're asking 10 doctors to diagnose a patient independently. But every doctor went to the same medical school, read the same textbooks, and tends to always notice the same symptoms first (say, temperature). So even though each doctor saw a slightly different subset of data, they all arrive at the same conclusion.

That's bagging. The trees are diverse in **data** but not in **thinking**. The same strong feature keeps winning at the root across all trees, making them correlated. Averaging correlated predictions doesn't reduce variance much.

---

### Random Forest = Bagging + Feature Roulette 🎰

Random Forest fixes this by adding **one simple twist**:

> **At every split, each tree is only allowed to consider a random subset of features.**

Instead of every tree asking *"which of ALL features is best?"* — each tree only gets to pick from, say, 3 randomly chosen features at that split.

**Why this works:**
- Tree 1 might split on `age` → Tree 2 might split on `blood_type` → Tree 3 splits on `cholesterol`
- They genuinely think differently now, not just see different data
- The final vote is from trees that approached the problem from genuinely different angles

**The two sources of randomness in Random Forest:**

| Source | What it does |
|--------|-------------|
| **Bootstrap sampling** | Each tree trains on a random sample of data (with replacement) |
| **Random feature subset at each split** | At every node, only a random `m` features are considered |

Together, these make trees **decorrelated** — even if two trees see similar bootstrap data, they'll make different split decisions because they can't all use the same features.

---

### The Mechanism

```
For each tree (in parallel):
  1. Bootstrap sample: draw N samples with replacement
  2. Grow the tree:
     At each node:
       - Pick m features at random (e.g. √p for classification)
       - Find the best split among those m only
       - Split
  3. Done. Don't prune (let them grow deep)

To predict:
  - Every tree votes
  - Majority vote (classification) / average (regression)
```

**Key hyperparameters:**

| Parameter | Typical value | Effect |
|-----------|-------------|--------|
| `m` (features per split) | √p (classification), p/3 (regression) | Too high → like bagging; too low → weak trees |
| Number of trees | 100–500 | More = stabler, but beyond ~500 dim. returns |
| Depth | Unbounded | Can overfit if too deep — but RF is robust |

---

### Why Random Forest Beats Bagging

Imagine predicting house prices. The dominant feature might always be `sq_feet`. In regular bagging, every tree splits on `sq_feet` at the root — all trees look nearly identical. In Random Forest, some trees might never even see `sq_feet` at their root (it wasn't in their random feature subset), so they split on `location` or `num_bedrooms` instead. These trees are genuinely different — and averaging their predictions gives much better generalization.

---

### Strengths and Weaknesses

**Strengths:**
- Strong default for almost any tabular problem
- Robust to noise and irrelevant features (they can't dominate every tree)
- Finds arbitrary-shaped decision boundaries (piecewise axis-aligned splits)
- **Parallel training** — like bagging, trees are independent

**Weaknesses:**
- **Memory**: stores hundreds of full trees
- **Latency**: queries all trees at prediction time
- **Interpretability**: a single tree is readable; a forest of 300 trees is not
- Still axis-aligned splits — can't discover density-based clusters

**Tools to regain interpretability:** Feature importance plots, SHAP values

---

### Bagging vs Random Forest — The Deep Comparison

| Aspect | Bagging | Random Forest |
|--------|---------|---------------|
| Data sampling | Bootstrap | Bootstrap + random feature subset per split |
| Tree thinking | Same features, different data | Different features, different data |
| Tree correlation | High (same dominant features) | Low (decorrelated) |
| Variance reduction | Moderate | Better |
| Memory cost | High (many deep trees) | High |
| Parallel training | Yes | Yes |
| Typical base tree | Deep, unpruned | Deep, unpruned |

---

### The One-Liner You'll Never Forget

> **Bagging puts the same expert in different rooms. Random Forest puts different experts in different rooms — and at every question, each expert is only allowed to use a randomly assigned set of clues to make their decision.**

---

### Common Exam Traps

- **"RF = bagging + something extra"** — That something is random feature subsets at each split (the `m` parameter)
- **mtry too large** → approaches bagging (all features considered), loses diversity
- **mtry too small** → individual trees become very weak, even with many of them
- **"Non-parametric = simple"** — RF has many hyperparameters: tree count, depth, m, min_samples_leaf
- **Parallelism** — RF training is parallel like bagging (trees don't depend on each other). Boosting is NOT parallel.
