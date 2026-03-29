# Perceptron – A Simple Linear Classifier – Artificial Neural Networks (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Define** what a Perceptron is and understand its role in neural networks.
2. **Interpret** the Perceptron equation for **binary classification**.
3. **Explain** both the **capability** and the **limitation** of a single Perceptron.

---

## What Is a Perceptron?

- The **Perceptron** is the **simplest computational model** of a neuron and the **first** true neural network model in machine learning.
- **Introduced by:** Frank Rosenblatt (late 1950s).
- **Purpose:** **Binary classification** — assign each input to one of two classes.
- Despite its simplicity, the Perceptron is the **conceptual foundation** of all modern neural networks.

---

## Mathematical Definition

The Perceptron computes a **linear function** of the input, then applies a **threshold**:

**1. Linear score (pre-activation):**
\[
z = \mathbf{w}^T \mathbf{x} + b
\]
- \( \mathbf{w} \) = weight vector, \( \mathbf{x} \) = input vector, \( b \) = bias.
- This is a **weighted sum** of the inputs plus a bias.

**2. Output (activation):**
\[
\hat{y} = \text{sgn}(z)
\]
- **sgn** (sign or step function):
  - If \( z > 0 \) → output **+1**
  - If \( z < 0 \) → output **-1**
- So the Perceptron produces **exactly one of two outputs**: +1 or -1. It is a **binary decision unit**.

---

## Decision Boundary: Line, Plane, Hyperplane

- The equation \( \mathbf{w}^T \mathbf{x} + b = 0 \) defines:
  - In **2D**: a **line**
  - In **3D**: a **plane**
  - In higher dimensions: a **hyperplane**
- This boundary **divides the input space into two half-spaces**:
  - Points on one side → classified as **+1**
  - Points on the other side → classified as **-1**
- That is why the Perceptron is called a **linear classifier**.

---

## Capability: Linearly Separable Data

- Because the Perceptron uses a **single** straight line (or hyperplane), it can classify **only linearly separable** data.
- **Linearly separable** means: all points of one class can be separated from the other class using **one** straight line (or hyperplane).

---

## Limitation: Non–Linearly Separable Data

- If the data is **not** linearly separable, **no** choice of weights and bias can make the Perceptron classify it perfectly.
- **Example:** Two concentric circles (one class inside, one outside). No single line can separate the two classes without errors. The Perceptron **must** fail on such data. This is its **fundamental limitation**.

---

## Summary (Quick Revision)

| Concept | Detail |
|---------|--------|
| **Perceptron** | Simplest binary classifier: weighted sum + bias + **threshold** (sign function). |
| **Output** | Either +1 or -1 (binary). |
| **Decision boundary** | Line (2D), plane (3D), hyperplane (higher dimensions). |
| **Works when** | Data is **linearly separable**. |
| **Fails when** | Data is **not** linearly separable (e.g. two circles). |

In the next video we move from this algebraic view to a **geometric and visual** understanding of Perceptron decision boundaries in two dimensions.
