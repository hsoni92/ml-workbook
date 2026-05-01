# Finding the Best Split — The Wedding Planner Story 🪑

## Context
**Source:** [ml-workbook/week-4/2-Finding the Best Split.md](https://github.com/hsoni92/ml-workbook/blob/main/bits-pilani/trimester-2/notes/machine-learning/week-4/2-Finding%20the%20Best%20Split.md)
**Topic:** Decision Tree splitting criteria — Entropy, Gini, Information Gain
**Date:** 2026-05-01

---

## The Story

Imagine you're a **wedding planner**. Your job? Seat 100 guests at tables so that every table has people who **actually like each other**. No awkward silences. No forced small talk. Every table = one tribe.

That's literally what a decision tree does — it's a seating planner.

---

### The Core Problem

You're standing in the hall. 100 guests. Some are **friendly**, some are **not**. You need to split them into groups.

- **Pure table** = everyone is the same type (all friendly OR all not). You stop here — no more splitting needed.
- **Impure table** = mix of both types. Keep splitting.

**Goal:** Choose the attribute (column) that makes your child tables as pure as possible.

---

### Meet the Three Chaos Meters

You have three ways to measure how "messy" a table is. They all agree on one thing: **50/50 split = maximum chaos**. **All same side = zero chaos.**

#### 1. Entropy — The Loudness Meter 🔊

Entropy measures **uncertainty**. How chaotic is this table?

```
Entropy = −Σ pᵢ × log₂(pᵢ)
```

Where pᵢ = proportion of each class.

Think of it like **volume**. A 50/50 table is shouting loud (entropy = 1 for binary). A table with everyone friendly is dead silent (entropy = 0).

**Example:** Table with 7 friendly, 3 not:
- p_friendly = 0.7, p_not = 0.3
- Entropy = −(0.7 × log₂(0.7) + 0.3 × log₂(0.3)) ≈ **0.881**

**Information Gain** = Entropy(parent) − weighted avg Entropy(children)

The attribute that **drops entropy the most** wins.

---

#### 2. Gini Index — The Misclassification Meter 🎯

Gini asks: *"If I randomly picked one guest and assigned them to a class based on the majority... what's the chance I'm wrong?"*

```
Gini = 1 − Σ pⱼ²
```

Same table: 7 friendly, 3 not → Gini = 1 − (0.7² + 0.3²) = **0.42**

- Pure table: Gini = 0
- 50/50: Gini = 0.5

**Gini Split** = weighted average of child Ginis. Choose the attribute that **minimizes** weighted Gini in children.

> Used by **CART** and is the default in **scikit-learn**.

---

#### 3. Misclassification Error — The Simple Meter ⚡

The laziest meter. Just asks: *"What proportion is NOT the majority class?"*

```
Error = 1 − max(pᵢ)
```

Same table: Error = 1 − 0.7 = **0.3**

---

### The Three Meters Compared

| Table Composition | Entropy | Gini | Misclass Error |
|---|---|---|---|
| 100% Friendly | 0 | 0 | 0 |
| 70% / 30% | 0.881 | 0.42 | 0.30 |
| 50% / 50% | **1** (max) | **0.5** (max) | **0.5** (max) |

> **Key difference:** Entropy goes up to 1. Gini and Misclassification max out at 0.5 for binary. All three tell the same story.

---

### The Algorithm in One Sentence

> **At every node, try every attribute. Compute impurity of resulting children. Pick the attribute that produces the purest children (lowest weighted impurity).**

- For Entropy → maximize **Information Gain** (IG = Entropy_parent − weighted_avg Entropy_children).
- For Gini → minimize **Gini Split** (weighted avg Gini of children).

---

### Decision Tree Algorithms

| Algorithm | Measure Used |
|---|---|
| **ID3** | Entropy → Information Gain |
| **C4.5** | Entropy → Information Gain (uses gain ratio) |
| **CART** | Gini Index |

Most libraries (scikit-learn) default to **Gini** because it's computationally cheaper (no logarithms).

---

### The One-Liner You'll Never Forget

**A decision tree is a wedding planner that keeps splitting tables until every table has only one type of guest — and it picks the split that reduces maximum chaos.**

Entropy, Gini, and Misclassification Error are just three different ways to measure that chaos. Information Gain and Gini Split are the scores you compare to pick the best attribute.
