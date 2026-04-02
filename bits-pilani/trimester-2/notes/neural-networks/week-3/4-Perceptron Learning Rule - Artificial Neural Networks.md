# Perceptron Learning Rule – Artificial Neural Networks (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Explain** why a learning rule is needed to adjust weights and bias from data.
2. **Define** the **classification error condition** for a Perceptron.
3. **Apply** the Perceptron **weight and bias update** equations.
4. **Understand** the **convergence behavior** and key **limitations** of the learning rule.

---

## Why a Learning Rule?

- The Perceptron **model** (linear score + threshold) alone is not enough. It has **parameters** — weights \( \mathbf{w} \) and bias \( b \) — and these are **not** known in advance.
- We need a **systematic way** to set these parameters from **data**. That process — automatically adjusting parameters based on examples — is **learning**. The **goal** of the learning rule is: **adjust weights and bias so that the Perceptron correctly classifies the training data.**

---

## Training Setup

- **Training set:** Pairs \( (\mathbf{x}_i, y_i) \), \( i = 1, \ldots, n \).
  - \( \mathbf{x}_i \) = input (feature) vector.
  - \( y_i \in \{+1, -1\} \) = true label.
- For each example, the Perceptron computes a **prediction** \( \hat{y}_i \).
- Learning is driven by **comparing** \( \hat{y}_i \) with \( y_i \):
  - If they **match** → do nothing.
  - If they **do not match** → update the model.

---

## When Does a Mistake Occur?

- Prediction: \( \hat{y}_i = \text{sgn}(\mathbf{w}^T \mathbf{x}_i + b) \).
- A convenient way to express “misclassification” is:
  \[
  y_i \cdot (\mathbf{w}^T \mathbf{x}_i + b) \leq 0
  \]
  - If this product is **positive** → the example is **correctly** classified (correct side of the boundary).
  - If it is **negative or zero** → the example is **misclassified**. **Updates happen only in this case.** So the Perceptron learning rule is **mistake-driven**, not a continuous optimization over all examples.

---

## Update Equations

When a **mistake** occurs:

\[
\mathbf{w} \leftarrow \mathbf{w} + \eta \cdot y \cdot \mathbf{x}
\]
\[
b \leftarrow b + \eta \cdot y
\]

- \( \eta > 0 \) = **learning rate** (controls step size).
- The update depends on: current input \( \mathbf{x} \), true label \( y \), and current parameters. **Updates occur only when the model makes a mistake.**

---

## Why This Update Makes Sense

**Case 1: Positive example misclassified as negative**

- \( y = +1 \), but \( \mathbf{w}^T \mathbf{x} + b \leq 0 \) (model said negative).
- Update: add \( \eta \cdot \mathbf{x} \) to \( \mathbf{w} \). This **increases** the alignment between \( \mathbf{x} \) and \( \mathbf{w} \), so \( \mathbf{w}^T \mathbf{x} \) tends to increase → more likely to classify as +1 next time.

**Case 2: Negative example misclassified as positive**

- \( y = -1 \), but \( \mathbf{w}^T \mathbf{x} + b > 0 \) (model said positive).
- Update: add \( \eta \cdot (-1) \cdot \mathbf{x} \) to \( \mathbf{w} \), i.e. **subtract** a multiple of \( \mathbf{x} \) from \( \mathbf{w} \). This **reduces** alignment → pushes the decision toward negative.

So **every update** nudges the decision boundary in the direction that **corrects** the observed mistake.

---

## Learning as Boundary Adjustment

- Start with **random** weights and bias → some **initial** decision boundary.
- Each time a **misclassified** example is seen, the update **slightly shifts and/or rotates** this boundary.
- After many such updates, the boundary **gradually aligns** with the structure of the data.
- **Learning stops** when the model **no longer makes mistakes** on the training set (for the given pass through the data).

---

## Convergence Theorem

- **If the data is linearly separable**, the Perceptron learning algorithm is **guaranteed to converge** in a **finite** number of updates: it will eventually find weights and bias that **perfectly** classify the training data.
- **If the data is not linearly separable**, the algorithm **will not** fully converge: weights will keep updating indefinitely because the model can **never** remove all errors. This is a structural limitation, not a bug.

---

## Limitations (Motivation for Logistic Neuron)

- The Perceptron does **not** perform **smooth optimization** (no gradients, no loss function).
- It does **not** produce **probabilistic** outputs or confidence scores.
- These limitations motivate the **logistic neuron** and more general gradient-based learning.

---

## Summary (Quick Revision)

| Concept | Detail |
|---------|--------|
| **Goal** | Adjust \( \mathbf{w} \) and \( b \) so the Perceptron classifies training data correctly. |
| **Mistake condition** | \( y_i (\mathbf{w}^T \mathbf{x}_i + b) \leq 0 \). |
| **Updates** | Only on mistakes: \( \mathbf{w} \leftarrow \mathbf{w} + \eta y \mathbf{x} \), \( b \leftarrow b + \eta y \). |
| **Convergence** | Guaranteed in finite steps **only if** data is linearly separable. |
| **Limitation** | No smooth optimization, no probabilities → leads to logistic neuron and gradient-based methods. |

> **Exam tip:** Perceptron updates are mistake-driven; update direction uses the **true label** \( y \) and the **input** \( \mathbf{x} \); convergence only for linearly separable data.
