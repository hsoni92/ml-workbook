# Matrix Operations Used in Neural Networks – Artificial Neural Networks (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Explain** why matrices are fundamental to neural network computation.
2. **Represent** a neural network layer using a **weight matrix** and a **bias vector**.
3. **Compute** layer outputs using **matrix multiplication**.
4. **Track and verify** matrix dimensions and shapes correctly.

---

## Why Neural Networks Use Matrices

- A **single neuron** computes **one** dot product: \( \mathbf{w}^T \mathbf{x} \) (input vector · weight vector).
- A **layer** has **many neurons** operating in parallel. Computing each dot product separately would be **very slow**.
- **Matrix operations** let us compute **all** neuron dot products in **one** mathematical operation. That is why matrices are central to neural network computation.

---

## From Single Neurons to a Layer

**Setup:**

- One **input vector** \( \mathbf{x} \in \mathbb{R}^n \).
- \( m \) neurons with weight vectors \( \mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_m \).

**Outputs:**

- Neuron 1: \( z_1 = \mathbf{w}_1^T \mathbf{x} \)
- Neuron 2: \( z_2 = \mathbf{w}_2^T \mathbf{x} \)
- …
- Neuron \( m \): \( z_m = \mathbf{w}_m^T \mathbf{x} \)

Writing these separately is repetitive. **Matrix notation** compresses them into one operation.

---

## Weight Matrix: Stack Weights as Rows

- **Stack** the weight vectors of all neurons as **rows** of a single matrix \( \mathbf{W} \):
  \[
  \mathbf{W} = \begin{bmatrix} — \mathbf{w}_1^T — \\ — \mathbf{w}_2^T — \\ \vdots \\ — \mathbf{w}_m^T — \end{bmatrix}
  \]
- **Shape:** \( \mathbf{W} \in \mathbb{R}^{m \times n} \):
  - \( m \) = number of neurons (output size),
  - \( n \) = number of input features.

This is exactly how neural network parameters are stored in practice.

---

## Layer Output in One Matrix Multiplication

\[
\mathbf{z} = \mathbf{W} \mathbf{x}
\]

- This **single** multiplication computes the dot product of \( \mathbf{x} \) with **every row** of \( \mathbf{W} \).
- So it gives the **outputs of all \( m \) neurons at once**.
- **Output:** \( \mathbf{z} \in \mathbb{R}^m \) — one value per neuron.

---

## Numerical Example

- \( \mathbf{W} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 1 \end{bmatrix} \) (shape \( 3 \times 2 \))
- \( \mathbf{x} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} \) (shape \( 2 \times 1 \))
- Inner dimensions (2 and 2) match → multiplication is valid.

\[
\mathbf{W} \mathbf{x} = \begin{bmatrix} 1\cdot 1 + 0\cdot 2 \\ 0\cdot 1 + 1\cdot 2 \\ 1\cdot 1 + 1\cdot 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
\]

So \( \mathbf{z} = [1,\ 2,\ 3]^T \).

---

## Tracking Dimensions (Essential)

| Quantity | Shape | Note |
|----------|--------|------|
| Input | \( n \times 1 \) or \( (n,) \) | \( n \) input features |
| Weight matrix | \( m \times n \) | \( m \) neurons, each with \( n \) weights |
| Output \( \mathbf{z} = \mathbf{W}\mathbf{x} \) | \( m \times 1 \) or \( (m,) \) | One value per neuron |

- **Rule:** Weight matrix must be \( m \times n \) when input has \( n \) dimensions and the layer has \( m \) neurons. Any mismatch makes the computation **invalid**.
- Many neural network bugs come from **shape mismatches**; always check dimensions at each layer.

---

## Bias in a Full Layer

- Bias is **not** a single number for the whole layer. There is **one bias per neuron**.
- **Bias vector:** \( \mathbf{b} = [b_1,\ b_2,\ \ldots,\ b_m]^T \in \mathbb{R}^m \).

**Full linear computation for one layer:**

\[
\mathbf{z} = \mathbf{W} \mathbf{x} + \mathbf{b}
\]

- Each \( b_i \) shifts the output of the \( i \)-th neuron independently.
- So each neuron has its own **baseline level of activation**.

---

## Batch Processing (Multiple Inputs at Once)

- In practice we rarely process **one** input at a time.
- **Batch:** Stack multiple input vectors as **columns** of a matrix \( \mathbf{X} \).
- Then **one** multiplication \( \mathbf{Z} = \mathbf{W} \mathbf{X} \) computes the outputs for **all** inputs in the batch.
- This **batching** is a key reason **GPUs** and parallel hardware are so effective for deep learning.

---

## Summary (Quick Revision)

| Idea | Detail |
|------|--------|
| **One neuron** | One dot product (\( \mathbf{w}^T \mathbf{x} \)). |
| **One layer** | One matrix multiplication (\( \mathbf{W} \mathbf{x} \)) + bias vector \( \mathbf{b} \). |
| **Bias** | Added as a **vector** (one entry per neuron). |
| **Batch processing** | Many inputs in \( \mathbf{X} \) → one \( \mathbf{W} \mathbf{X} \) gives all outputs in parallel. |
| **Backbone** | These operations form the **linear algebra backbone** of neural networks. |

In the next lesson we move from **linear algebra** to **calculus**: how **derivatives and gradients** allow these weights to be **learned from data**.
