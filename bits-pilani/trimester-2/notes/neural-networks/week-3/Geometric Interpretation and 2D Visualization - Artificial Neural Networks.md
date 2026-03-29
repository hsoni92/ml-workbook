# Geometric Interpretation and 2D Visualization – Artificial Neural Networks (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Visualize** Perceptron decision boundaries in **2D**.
2. **Understand** the geometric roles of **weights** and **bias**.
3. **Identify** the geometric limits of linear classification.

---

## Decision Boundary in 2D

In two dimensions, the Perceptron decision function is:
\[
w_1 x_1 + w_2 x_2 + b = 0
\]
This is the **equation of a straight line** in the \( (x_1, x_2) \) plane.

- Every point that **satisfies** this equation lies **on** the decision boundary.
- Points on **one side** of the line → output **+1**.
- Points on the **other side** → output **-1**.
- So in 2D, the Perceptron is literally a **straight-line classifier**.

---

## Half-Spaces and Classification

- The decision boundary splits the plane into two **half-spaces**.
- For any input \( \mathbf{x} \):
  - If \( \mathbf{w}^T \mathbf{x} + b > 0 \) → class **+1**
  - If \( \mathbf{w}^T \mathbf{x} + b < 0 \) → class **-1**
- Classification is a **sign test**: which side of the line the point lies on. There is **no** notion of distance, probability, or confidence yet — only **side-of-the-line** membership.

---

## Dot Product View

- \( \mathbf{w}^T \mathbf{x} \) measures **alignment** between the input vector and the weight vector.
- If alignment is **positive** and large enough → output +1.
- If **negative** → output -1.
- So classification is based on **vector alignment** between the input and the **learned** weight vector.

---

## Geometric Role of the Weight Vector

- The **weight vector \( \mathbf{w} \)** determines the **orientation** of the decision boundary.
- **Changing the direction of \( \mathbf{w} \)** **rotates** the boundary.
- In geometry, \( \mathbf{w} \) is the **normal vector** to the line: it is **perpendicular** to the decision boundary.
- The direction in which \( \mathbf{w} \) points is the direction of **increasing** Perceptron activation, and it always points **toward** the region classified as **+1**.
- So weights do not only scale features — they **control the orientation** of the separating line in space.

---

## Geometric Role of the Bias

- **Bias \( b \)** controls the **position** of the decision boundary, **not** its orientation.
- Changing the bias **shifts** the line **parallel to itself** (no rotation).
- **Increase** \( b \) → line moves in one direction.
- **Decrease** \( b \) → line moves in the opposite direction.

---

## Worked Example

- **Weights:** \( \mathbf{w} = (1, 1)^T \), **bias:** \( b = 0 \).
- **Decision boundary:** \( x_1 + x_2 = 0 \) (line through origin with slope -1).

**Point (2, 1):** \( x_1 + x_2 = 3 > 0 \) → lies on the “positive” side → class **+1**.

**Point (2, -1):** \( x_1 + x_2 = 1 > 0 \) → class **+1**. (Adjust with a different point if needed for -1; the idea is: sign of \( \mathbf{w}^T \mathbf{x} + b \) decides the class.)

---

## When the Perceptron Must Fail

- Not all datasets can be separated by **one** straight line, no matter how we rotate or shift it.
- If **no** single line can separate the two classes, the Perceptron **must** fail — not because of bad training, but because the **geometry** of the problem makes linear separation **impossible**.
- This geometric limitation leads directly to the **XOR problem** and to the need for **multi-layer** neural networks.

---

## Summary (Quick Revision)

| Concept | Detail |
|---------|--------|
| **2D** | Perceptron draws a **straight line** in the input space. |
| **Weights** | Set the **orientation** of the line; \( \mathbf{w} \) is perpendicular to the boundary. |
| **Bias** | Sets the **position** of the line (parallel shift). |
| **Classification** | Half-space test: which side of the line the point lies on. |
| **Success** | When data can be separated by one line. **Failure** when no such line exists. |

> **Exam tip:** In 2D, \( \mathbf{w} \) is normal to the decision line and points toward the +1 region; \( b \) only shifts the line.
