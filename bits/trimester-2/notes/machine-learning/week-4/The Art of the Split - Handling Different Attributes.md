# The Art of the Split – Handling Different Attributes – Machine Learning (Module 4)

## Learning Objectives

By the end of this video you will:

1. **State** that decision tree construction follows a **greedy** strategy (local optimization, no backtracking).
2. **List** the three questions: which attribute, how to split, when to stop.
3. **Describe** how to split **nominal** attributes: **multi-way** vs **binary** split.
4. **Describe** how to split **ordinal** attributes (order must be preserved when grouping).
5. **Describe** how to split **continuous** attributes: **discretization** (bins) vs **binary** split (e.g. threshold).

---

## Greedy Strategy

- At **each** node we choose the **best attribute (and split)** **at that moment**, using a **local** criterion (e.g. maximum information gain, or minimum Gini in children).
- We **do not** look ahead or **backtrack**. Once we split on attribute A at the root, we do not later replace A with B at the root.
- **Consequence:** Decision trees **do not** guarantee a **globally optimal** tree; they optimize **locally** at each step.

---

## Three Questions (Recap)

1. **Which attribute** to choose? → Use impurity reduction (e.g. information gain, Gini) — see “Finding the Best Split.”
2. **How to split** that attribute? → **Depends on attribute type** (this note).
3. **When to stop?** → Stopping conditions — see “From Induction to Application.”

---

## Splitting by Attribute Type

We treat attributes as **nominal**, **ordinal**, or **continuous** (interval/ratio grouped as continuous for splitting).

---

## 1. Nominal Attribute

- **Property:** Only **distinctness** (same/different). No order, no magnitude.
- **Options:**

### Multi-way split

- **One branch per distinct value** (e.g. Car type: Family, Sports, Luxury → 3 branches). All samples with that value go to that child.
- **Pros:** Simple, intuitive. **Cons:** Many branches → few samples per child; can hurt performance.

### Binary split

- Partition the **set of values** into **two non-overlapping subsets**; two branches.  
  E.g. {Family, Sports} vs {Luxury}, or {Family} vs {Sports, Luxury}.
- **Challenge:** For **k** values there are **2^(k−1) − 1** ways to form two subsets. Finding the **optimal** binary split can be expensive; heuristics are used.

---

## 2. Ordinal Attribute

- **Property:** Values can be **ordered** (e.g. small &lt; medium &lt; large). **Order** must be respected when grouping.
- **Options:** Again **multi-way** (one branch per value) or **binary**.
- **Rule for binary (or grouping):** When combining values into one branch, **do not break the order**.  
  **Valid:** {Small, Medium} vs {Large}. **Invalid:** {Small, Large} vs {Medium} (order broken).

---

## 3. Continuous Attribute

- **Property:** **Infinite** possible values (e.g. age, taxable income, temperature).
- **Options:**

### Discretization (multi-way)

- Define **bins** (e.g. Age: 1–25, 26–50, 51–75, 76–100). Each bin → one branch; samples go to the bin that contains their value.
- **Binary** version: e.g. “Age ≤ 25” vs “Age &gt; 25” (one threshold).

### Binary split (threshold)

- Choose a **threshold** (e.g. Taxable income &gt; 80K). Two branches: **yes** and **no**. Very common in practice (e.g. CART).
- We can also use **multiple thresholds** (several bins) like discretization.

---

## Summary Table

| Attribute type | Multi-way split | Binary split | Constraint |
|----------------|------------------|---------------|------------|
| **Nominal** | One branch per value | Partition values into 2 subsets | Subsets disjoint |
| **Ordinal** | One branch per value | Partition into 2 subsets | **Preserve order** when grouping |
| **Continuous** | Bins (discretization) | Single (or multiple) threshold(s) | — |

---

## Exam-Oriented Points

- Tree construction is **greedy** (local choice, no backtracking).
- **Nominal:** Multi-way or binary; optimal binary split is combinatorial (2^(k−1)−1).
- **Ordinal:** Multi-way or binary; **order must be preserved** in groupings.
- **Continuous:** Discretization (bins) or binary (e.g. “attribute &gt; threshold”).

Use this note for “how do we split nominal/ordinal/continuous” and “what is greedy strategy.”
