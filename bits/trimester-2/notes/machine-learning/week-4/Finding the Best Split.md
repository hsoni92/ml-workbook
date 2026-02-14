# Finding the Best Split – Machine Learning (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Define** **node impurity** and **pure vs impure** (homogeneous vs heterogeneous) nodes.
2. **State** the goal: choose the attribute that leads to the **most homogeneous (pure) child nodes**.
3. **Define** and **compute** **entropy** for a node; relate to **information gain**.
4. **Define** and **compute** **Gini index** (and **Gini split**).
5. **Define** **misclassification error** and compare all three (entropy, Gini, misclassification) for binary classification.

---

## Three Questions in Tree Construction

1. **Which attribute** to choose for splitting (e.g. at root)?
2. **How** to split that attribute (multi-way, binary, by threshold)? (Depends on attribute type — see “Art of the Split.”)
3. **When** to stop (stopping condition)? (See “From Induction to Application.”)

This note focuses on **question 1: which attribute to choose.**

---

## Goal: Homogeneous (Pure) Child Nodes

- After a split we get **child nodes**. We want them to be as **pure** as possible:
  - **Pure/homogeneous:** (Almost) all tuples in the node are of **one class** (e.g. all C0 or all C1). Then we can **stop** and assign that class at a leaf.
  - **Impure/heterogeneous:** Mix of classes (e.g. 5 C0 and 5 C1). We **cannot** decide; we need to **split further**.

So we **choose the attribute** that **most reduces impurity** (or equivalently, most increases “purity”) in the children.

---

## Measuring Impurity

- **Impurity measure:** A function that takes the **class distribution** in a node (e.g. proportions p₁, p₂ for two classes) and returns a **number**.
  - **Pure node** → impurity = **0** (or minimum).
  - **Impure node** (e.g. 50–50) → impurity = **maximum** (for that measure).

We **compare** attributes by the **impurity of the resulting child nodes** (often using a **weighted average** by number of samples in each child). **Best attribute** = one that gives the **lowest** (weighted) impurity in children, or **largest reduction** from parent.

---

## 1. Entropy

- From **information theory**: measures **uncertainty / randomness / chaos**.
- **High entropy** → high impurity (mixed classes). **Low entropy** → low impurity (one class dominates).
- **Formula (binary or multi-class):**  
  **Entropy = − Σ pᵢ log₂(pᵢ)**  
  where **pᵢ** = proportion of class **i** in the node.

**Example:** Node with 3 of class A and 7 of class B → p_A = 0.3, p_B = 0.7 → Entropy ≈ 0.88.

**Pure node:** One class has proportion 1, others 0 → Entropy = 0. **Maximum entropy (binary):** p = 0.5 → Entropy = 1.

### Information Gain (used with Entropy)

- **Information Gain (IG)** of an attribute = **Entropy(parent) − weighted average of Entropy(children)**.
- **Larger IG** = **better** attribute (more reduction in uncertainty). We **choose the attribute with highest IG**.

---

## 2. Gini Index

- **Gini** = probability that a **randomly chosen** element in the node is **misclassified** if we label it according to the class distribution in the node.
- **Formula:**  
  **Gini(node) = 1 − Σ pⱼ²**  
  (sum over classes; pⱼ = proportion of class j).

**Pure node:** One pⱼ = 1 → Gini = 0. **Binary, 50–50:** Gini = 0.5.

### Gini Split

- Like IG for entropy: we compute **weighted average of Gini** of child nodes. **Higher** Gini (or we use **reduction** in Gini from parent) → we can rank attributes. In many implementations we **minimize** weighted Gini of children (i.e. choose split that **reduces** Gini the most). (Some software uses “Gini gain” or “Gini impurity decrease.”)

**Used in:** CART; often **default** in scikit-learn for decision trees.

---

## 3. Misclassification Error

- **Error(node) = 1 − max(pᵢ)**  
  i.e. 1 minus the proportion of the **majority** class.
- **Pure node:** max(pᵢ) = 1 → Error = 0. **Binary, 50–50:** Error = 0.5.

**Comparison (binary classification, horizontal axis = proportion of one class):**

- **Entropy:** 0 at p=0 and p=1; **maximum 1** at p=0.5.
- **Gini:** 0 at p=0 and p=1; **maximum 0.5** at p=0.5.
- **Misclassification error:** 0 at p=0 and p=1; **maximum 0.5** at p=0.5.

So for **binary** classification:  
**Entropy** range [0, 1]; **Gini** and **misclassification error** range [0, 0.5].

---

## How We Use These

- At each node we have a set of **candidate attributes** (e.g. A, B, C).
- For each attribute we **split** the data (according to that attribute’s type and chosen split). We get **child nodes**.
- We compute **impurity** (entropy, Gini, or misclassification) for each child and then a **combined** measure:
  - **Entropy** → **Information Gain** = Entropy(parent) − weighted_avg(Entropy(children)). **Choose attribute with maximum IG.**
  - **Gini** → **Gini split** (weighted Gini of children) or **decrease in Gini**; choose attribute that **minimizes** child Gini (or maximizes decrease).
  - **Misclassification** → similarly compare weighted error of children; choose attribute that **minimizes** it.

We **iterate** until a **stopping condition** (pure node, no gain, or pre-pruning).

---

## Summary

- **Pure node** = one class (impurity 0); **impure** = mixed (impurity &gt; 0). We want **splits that create purer children**.
- **Entropy:** −Σ pᵢ log₂(pᵢ). Use **Information Gain** = Entropy(parent) − weighted Entropy(children). **Max IG** → best attribute. Used in ID3, C4.5.
- **Gini:** 1 − Σ pⱼ². Use **Gini split** (weighted Gini of children). **Minimize** child Gini (or maximize decrease). Used in CART; default in many libraries.
- **Misclassification error:** 1 − max(pᵢ). Simpler; ranges 0–0.5 for binary.

Use this note for computing entropy/Gini/error and for choosing the best attribute by IG or Gini.
