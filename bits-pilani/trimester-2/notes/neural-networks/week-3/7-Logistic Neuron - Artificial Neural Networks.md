# Logistic Neuron – Artificial Neural Networks (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Explain** the limitations of the Perceptron’s **hard threshold** and why a **smooth** alternative is needed.
2. **Understand** the **sigmoid function** and its key properties.
3. **Interpret** the logistic neuron’s output as a **probability**.
4. **Recognize** that the **decision boundary remains linear** while the **output** becomes smooth.

---

## Limitations of the Perceptron

- The Perceptron uses a **hard threshold**: output jumps abruptly from -1 to +1.
- It gives only a **class label**, not **how confident** it is.
- Because of this hard threshold, the Perceptron has three main limitations:
  1. **No notion of uncertainty.**
  2. **No probabilistic interpretation.**
  3. **Hard to use for smooth, continuous optimization** (e.g. gradient descent), because the step function is not differentiable everywhere.

To address these we introduce a **smooth** alternative: the **logistic neuron**.

---

## Sigmoid Function

At the heart of the logistic neuron is the **sigmoid** (logistic) function:

\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

**Properties:**

- **Smooth:** No sudden jumps; it changes **gradually** between 0 and 1.
- **Bounded:** For any real \( z \), \( \sigma(z) \in (0, 1) \).

**Key values:**

| \( z \) | \( \sigma(z) \) |
|---------|------------------|
| \( z = 0 \) | \( \frac{1}{1+1} = 0.5 \) |
| \( z \to +\infty \) | \( e^{-z} \to 0 \) ⇒ \( \sigma(z) \to 1 \) |
| \( z \to -\infty \) | \( e^{-z} \to +\infty \) ⇒ \( \sigma(z) \to 0 \) |

So any real input is mapped to a value **strictly between 0 and 1** — ideal for soft decisions and gradual transitions instead of hard switching.

---

## Logistic Neuron: Definition

- **Structure:** Same as the Perceptron — we still compute a linear combination:
  \[
  z = \mathbf{w}^T \mathbf{x} + b
  \]
- **Only change:** Instead of a **hard step**, we apply the **sigmoid**:
  \[
  \hat{y} = \sigma(z) = \frac{1}{1 + e^{-z}}
  \]
- So the **only** difference from the Perceptron is the **activation function**. But this change **radically** alters the behavior of the output.

---

## Output: Continuous and Probabilistic

- Instead of only +1 or -1, the logistic neuron outputs a **continuous** value in \( (0, 1) \).
- This can be **interpreted as a probability**:
  \[
  \hat{y} = P(y = 1 \mid \mathbf{x})
  \]
  - \( \hat{y} \approx 1 \) → model is confident class 1.
  - \( \hat{y} \approx 0 \) → model is confident class 0.
  - \( \hat{y} \approx 0.5 \) → model is **uncertain**.
- So we get not just a class label but a **confidence score**. This probabilistic view is central to modern machine learning.

---

## Decision Boundary: Still Linear

- Even though the **output** behavior is different, the **geometry** of the classifier does **not** change.
- The **decision boundary** is still defined by where the **score** is exactly at the “decision” value. For the sigmoid, the natural choice is where \( \hat{y} = 0.5 \), which corresponds to \( z = 0 \), i.e. \( \mathbf{w}^T \mathbf{x} + b = 0 \).
- So the **decision boundary** is still the **same** line (or hyperplane) as in the Perceptron. What changes is **not** the location of the boundary, but **how sharply** the decision changes **across** that boundary: instead of an abrupt flip, the output **smoothly** goes from near 0 to near 1. The logistic neuron gives a **smooth transition** across the boundary.

---

## Summary (Quick Revision)

| Concept | Detail |
|---------|--------|
| **Logistic neuron** | Replaces hard threshold with **sigmoid** \( \sigma(z) = \frac{1}{1+e^{-z}} \). |
| **Output** | Continuous in \( (0, 1) \), interpretable as **probability** \( P(y=1 \mid \mathbf{x}) \). |
| **Decision boundary** | Still **linear** (\( \mathbf{w}^T \mathbf{x} + b = 0 \)); transition across it is **smooth**. |
| **Role** | Core building block of modern multi-layer neural networks (smooth, differentiable, probabilistic). |

In the next video we **compare** the logistic neuron with the Perceptron in terms of decision behavior and smoothness.
