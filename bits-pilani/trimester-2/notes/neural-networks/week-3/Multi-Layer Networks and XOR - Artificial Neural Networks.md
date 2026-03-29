# Multi-Layer Networks and XOR – Artificial Neural Networks (Module 3)

## Learning Objectives

By the end of this video you will:

1. **Explain** why a **single** Perceptron cannot solve the XOR problem.
2. **Understand** how a **hidden layer** enables **multiple linear splits**.
3. **Recognize** why **multi-layer** networks are **more expressive** than single-layer Perceptrons.

---

## Why a Single Perceptron Fails on XOR

- The Perceptron fails on XOR **not** because of poor learning, bad initialization, or lack of data. It is a **structural** limitation of the model.
- A **single** Perceptron can create **only one** linear decision boundary (one line in 2D, one hyperplane in higher dimensions). That boundary divides the input space into **only two** regions.
- XOR **requires** the input space to be split into **multiple** regions in a specific way (e.g. two diagonally opposite points in one class, the other two in the other class). **One** line can never achieve this. So a single Perceptron is **fundamentally incapable** of solving XOR.

---

## What Changes When We Add a Hidden Layer?

- A **hidden layer** allows us to create **multiple linear feature splits** instead of just one.
- **Each hidden neuron** can learn its **own** linear separator of the input space. These intermediate “linear features” are then passed to the **output** neuron, which **combines** them into a final decision.
- By **composing** multiple linear cuts in this way, the network can form **non-linear** decision regions in the original input space. This is the crucial **representational leap**: we are no longer restricted to a **single** straight boundary.

---

## Solving XOR with Two Linear Boundaries

- For XOR we can think of **two** lines in the 2D input space. For example:
  - One line separates one pair of opposite corners.
  - Another line separates the other structure.
- All points that lie in the “correct” combination of half-spaces (e.g. inside both lines, or in a specific configuration) can be classified as one class; the rest as the other.
- So XOR is solved by:
  1. **First** creating **two** (or more) linear partitions in a **hidden layer** (each hidden neuron implements one such partition).
  2. **Then** recombining those partitions into a **single** final decision at the **output** layer.
- This **requires at least one hidden layer**.

---

## Key Takeaway

- **Multi-layer** networks are **strictly more expressive** than a single Perceptron. They can represent functions that **no** single linear model can.
- This **increase in expressive power** — not just better learning rules — is the fundamental reason why **deeper** neural networks can outperform shallow ones. Architecture (depth, hidden layers) matters for **what** functions can be represented.

---

## Summary (Quick Revision)

| Concept | Detail |
|---------|--------|
| **XOR** | Requires splitting the space into **multiple** regions; **one** line is not enough. |
| **Single Perceptron** | Can draw only **one** linear boundary → cannot solve XOR. |
| **Hidden layer** | Allows **multiple** linear boundaries; output combines them. |
| **Multi-layer networks** | More **expressive** than single Perceptrons; can learn **non-linear** decision regions. |

In the next lesson we introduce the **logistic neuron** as the smooth, probabilistic building block used inside these multi-layer networks.
