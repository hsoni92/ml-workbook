# From Induction to Application – Pruning, Overfitting and Advantages – Machine Learning (Module 4)

## Learning Objectives

By the end of this video you will:

1. **List** the **stopping conditions** for decision tree construction (pure node, no gain, early termination).
2. **Describe** **pre-pruning** (early termination) and typical **thresholds** (min samples, max depth, min improvement).
3. **Relate** **overfitting** and **underfitting** to tree **complexity** (e.g. depth) and to **train vs test error**.
4. **State** that we want a **generalized** tree (sweet spot) and **avoid** overfitting and underfitting.
5. **List** main **advantages** of decision trees (cost, speed, interpretability, comparable accuracy).

---

## Recap: Tree Induction

- **Three questions:** (1) Which attribute to choose? (2) How to split it? (3) When to stop?
- **Process (e.g. ID3-style):** Top-down. At each node: choose **best attribute** (e.g. by information gain), **split** into children, **assign** training examples to leaves. **Recurse** on each child until a **stopping condition** is met. **Greedy:** no backtracking.

---

## Stopping Conditions

We stop expanding a node when **any** of the following holds:

### 1. Pure node

- **All** tuples in the node belong to **one class** → impurity = 0. We can **stop** and make that node a **leaf** with that class label.

### 2. No significant gain

- **No attribute** gives a **significant** reduction in impurity (e.g. information gain or Gini decrease below a threshold). Further split is not justified → **stop** and declare a leaf (e.g. majority class).
- **Records indistinguishable:** Algorithm cannot separate them with available attributes → stop.

### 3. Early termination (pre-pruning)

- We **manually** stop growth using **thresholds**, e.g.:
  - **Minimum samples for split:** Do not split if the node has too few samples (avoids fitting noise).
  - **Maximum tree depth:** Do not grow beyond **n** levels (limits complexity and prediction cost).
  - **Minimum improvement:** Do not split unless impurity **decreases by at least** a given amount.

These help **avoid overfitting** and keep the tree **generalizable**.

---

## Overfitting and Underfitting in Decision Trees

- **Model complexity** for a tree can be thought of as **depth** (or number of nodes). Deeper tree = more complex.
- **Train error** tends to **decrease** as we allow more depth. **Test error** first **decreases** then **increases** (we overfit).

### Underfitting

- **Too shallow / too simple** tree (e.g. depth 1). **High train error**, **high test error**. Model cannot capture the pattern in the data.

### Overfitting

- **Too deep** tree; it **memorizes** training data (including noise and outliers). **Low train error**, **high test error**. Fails on new data.
- **Analogy:** Student memorizes exact practice answers; real exam has different questions → poor performance.

### Sweet spot

- **Moderate** depth (and/or other constraints) where **train and test error** are **both low** and **close**. Tree **generalizes** well.

**Ways to reach the sweet spot:** **Pre-pruning** (max depth, min samples, min improvement), and later **post-pruning** (not detailed here). Goal = **generalization**.

---

## Advantages of Decision Trees

| Advantage | Meaning |
|-----------|---------|
| **Relatively inexpensive to construct** | Time/complexity of building the tree is often **lower** than many other algorithms. |
| **Fast prediction** | For a new sample we only **traverse** from root to one leaf (few comparisons). **Very fast** at inference. |
| **Easy to interpret** | **White-box:** we can **trace the path** and explain why a prediction was made (root → … → leaf). |
| **Comparable accuracy** | In many problems, decision trees achieve **accuracy** comparable to other classifiers. |
| **Minimal pre-processing** | Often need **less** data cleaning and scaling than distance-based or gradient-based methods. |

---

## Summary

- **Stopping conditions:** (1) Pure node, (2) No significant impurity reduction / indistinguishable records, (3) Pre-pruning (min samples, max depth, min improvement).
- **Overfitting** = too complex tree, low train error and high test error; **underfitting** = too simple, high train and test error. Aim for **generalization** (sweet spot).
- **Pre-pruning** (early stopping) helps avoid overfitting.
- **Advantages:** Inexpensive to build, fast prediction, interpretable, often comparable accuracy, minimal pre-processing.

Use this note for “when do we stop building the tree,” “overfitting/underfitting in trees,” and “advantages of decision trees.”
