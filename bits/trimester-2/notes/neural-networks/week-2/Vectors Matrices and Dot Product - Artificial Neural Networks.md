# Vectors, Matrices, and Dot Product – Artificial Neural Networks (Module 2)

## Learning Objectives

By the end of this video you will:

1. **Identify** the vectors, matrices, and tensors used in neural networks.
2. **Understand** the importance of **shapes and dimensionality** in neural network computations.
3. **Compute** the dot product algebraically.
4. **Interpret** the dot product as a measure of **alignment and similarity**.

---

## The Language of Neural Networks

Before learning, gradients, or backpropagation, we must understand the **mathematical objects** neural networks are built from. Every computation inside a neural network uses:

- **Vectors**
- **Matrices**
- **Tensors**

Inputs, weights, activations, outputs, and gradients are all represented with these objects. Once you are comfortable with these three, the rest of neural network mathematics becomes **systematic and predictable**.

---

## Vectors

### Definition

A **vector** is an **ordered list of numbers**, usually represented as a **column** of values.

**Example:** \( \mathbf{x} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \) can represent an input vector.

### Notation and Shape

- **Notation:** \( \mathbf{x} \in \mathbb{R}^n \) means the vector has \( n \) real-valued components.
- **Shape:** \( n \times 1 \) (n rows, 1 column).

### Where Vectors Appear in Neural Networks

| Use | Meaning |
|-----|--------|
| **Single data sample** | One input instance (e.g. feature vector) |
| **Activations of a layer** | Outputs of all neurons in one layer |
| **Gradients** | Gradient with respect to parameters is a vector |

**Intuition:** A vector is the **basic carrier of information** in a neural network.

---

## Matrices

### Definition

A **matrix** is a **two-dimensional** collection of numbers arranged in **rows and columns**.

**Example (weight matrix):**

\[
\mathbf{W} = \begin{bmatrix} w_{11} & w_{12} & \cdots & w_{1n} \\
w_{21} & w_{22} & \cdots & w_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
w_{m1} & w_{m2} & \cdots & w_{mn} \end{bmatrix}
\]

- **Notation:** \( \mathbf{W} \in \mathbb{R}^{m \times n} \) → \( m \) rows, \( n \) columns.
- **Role in neural networks:** Matrices most commonly store the **weights** that connect **one layer of neurons to the next**.

---

## Tensors

- **Definition:** A **tensor** is a generalization of vectors and matrices to **higher dimensions**.
  - **Vector** = first-order tensor (1D).
  - **Matrix** = second-order tensor (2D).
  - **Higher-order tensor** = three or more dimensions.
- **Why they matter:** Real-world data is often multidimensional.
  - **Image:** 3D tensor (height × width × color channels).
  - **Video:** 4D tensor (time + image dimensions).
- Modern deep learning frameworks operate almost entirely on **tensors**.

---

## Shape Consistency (Critical for Implementation)

**Rule:** For a valid computation, **dimensions must align**.

- If **input vector** has shape \( n \times 1 \) and **weight matrix** has shape \( m \times n \), their product has shape **\( m \)** (one value per output neuron).
- If shapes do **not** align, the computation is **invalid** and will fail in code.
- **In practice:** Many implementation bugs in neural networks come from **shape mismatches**. Always track:
  - Input dimensionality  
  - Weight matrix dimensions  
  - Output dimensions at every layer  

> **Exam tip:** “Shape consistency” = inner dimensions must match for matrix-vector multiplication; output shape is determined by the outer dimensions.

---

## Dot Product

### Algebraic Definition

For vectors \( \mathbf{x} \) and \( \mathbf{w} \) of the same length \( n \):

\[
\mathbf{x} \cdot \mathbf{w} = \sum_{i=1}^{n} x_i w_i
\]

- **In words:** Multiply corresponding elements and sum the results.
- **Output:** Always a **single scalar**, regardless of dimension.

### Numerical Example

- \( \mathbf{x} = [2,\ 1,\ -1]^T \), \( \mathbf{w} = [3,\ -2,\ 4]^T \)
- \( \mathbf{x} \cdot \mathbf{w} = 2(3) + 1(-2) + (-1)(4) = 6 - 2 - 4 = 0 \)

### Geometric Interpretation

\[
\mathbf{x} \cdot \mathbf{w} = \|\mathbf{x}\| \,\|\mathbf{w}\| \cos\theta
\]

- \( \theta \) = angle between the two vectors.
- \( \cos\theta \) measures **alignment**:
  - **Same direction** → dot product **large and positive**.
  - **Opposite direction** → dot product **large and negative**.
  - **Perpendicular** → dot product **zero**.

### Worked Examples (2D)

| \( \mathbf{x} \) | \( \mathbf{w} \) | \( \mathbf{x} \cdot \mathbf{w} \) | Interpretation |
|------------------|------------------|------------------------------------|----------------|
| \( (2, 2) \)     | \( (3, 3) \)     | \( 2(3)+2(3)=12 \)                 | Same direction (angle 0°) |
| \( (2, 2) \)     | \( (-3, -3) \)   | \( 2(-3)+2(-3)=-12 \)              | Opposite direction (180°) |
| \( (1, 0) \)     | \( (0, 1) \)     | \( 1(0)+0(1)=0 \)                  | Perpendicular (90°) |

---

## Why the Dot Product Matters in Neural Networks

- **Every artificial neuron**, at its mathematical core, computes a **dot product** between the **input vector** and the **weight vector**.
- This single operation determines whether the neuron activates **strongly**, **weakly**, or **not at all**.
- Understanding the dot product = understanding what the neuron is doing.

### Full Neuron Computation

In practice we add a **bias** term:

\[
z = \mathbf{x} \cdot \mathbf{w} + b
\]

- **Dot product** → measures **similarity** (alignment) between input and weights.
- **Bias** → shifts the point at which the neuron starts to activate.
- **Together** → they give the **raw decision signal** \( z \), which is then passed through an **activation function** to produce the final (often non-linear) output.

So: **similarity** (dot product) + **sensitivity** (bias) control every neuron’s decision.

---

## Summary (Quick Revision)

| Concept | Takeaway |
|---------|----------|
| **Vectors** | Carry information (inputs, activations, gradients). |
| **Matrices** | Connect layers (weights). |
| **Tensors** | Generalize to higher dimensions (images, video). |
| **Shapes** | Must be tracked and consistent for correct computation. |
| **Dot product** | Measures alignment, similarity, and “strength of evidence” between two vectors. |
| **Neuron** | Computes dot product (input · weights) + bias, then applies a non-linear activation. |

In the next video we see how dot products generalize to **matrix operations**, so that **entire layers** of neurons are computed in one efficient step.
