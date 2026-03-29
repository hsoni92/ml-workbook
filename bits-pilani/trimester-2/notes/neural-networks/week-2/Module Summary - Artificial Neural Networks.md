# Neural Networks – Module 2 Summary: Artificial Neural Networks

## Purpose of This Module

Module 2 builds the **mathematical foundation** needed to understand how neural networks **learn** from data. The emphasis is on **linear algebra**, **calculus**, and **numerical computation** — not on specific models yet. This module is the bridge between “what a neural network is” and “how it is trained.”

---

## What We Learned (Flow of Module 2)

| Topic | Content |
|-------|--------|
| **Linear algebra** | Vectors, matrices, tensors, dot products, matrix operations — the language in which neural network computations are written. |
| **Derivatives and partial derivatives** | How outputs change when inputs or parameters change (sensitivity). |
| **Gradient vector** | Collects all partial derivatives; points in direction of steepest increase; negative gradient = steepest decrease. |
| **Chain rule** | How sensitivities propagate through **compositions** of functions and intermediate variables — the backbone of backpropagation. |
| **Numerical stability** | Overflow, underflow, log-sum-exp trick, and other techniques so that training does not silently fail. |

With this toolkit we are ready to study **concrete neural models** (e.g. perceptron, logistic neuron) and connect the math to actual learning.

---

## Key Intuitions to Retain (Exam-Ready)

1. **Vectors** carry information; **matrices** connect layers; **tensors** generalize to higher dimensions. **Shapes** must be tracked at every layer.
2. **Dot product** measures alignment/similarity; each neuron computes (input · weights) + bias, then an activation.
3. **One layer** = one matrix multiplication (\( \mathbf{W}\mathbf{x} \)) + bias vector \( \mathbf{b} \).
4. **Derivatives** = sensitivity; **partial derivatives** = sensitivity to one variable with others fixed.
5. **Gradient** = vector of partial derivatives; points in direction of steepest increase; **negative gradient** used for minimization.
6. **Chain rule** = total derivative as product of local derivatives along the path; essential for multi-layer (deep) networks.
7. **Numerical stability** is mandatory: use log-sum-exp, work in log domain, avoid overflow/underflow.

---

## Bridge to Module 3

In Module 3 we use this math to study **real models**:

- **Perceptron** — simple linear classifier; linear separability and the **XOR limitation**.
- **Logistic neuron** — smooth, probabilistic output.
- **Multi-layer networks** — why they are needed and how they solve XOR.

So the shift is: **mathematical tools (Module 2)** → **first neural models and limitations (Module 3)**.

---

## Quick Revision Checklist

- [ ] Vectors, matrices, tensors: definition, shape, role in neural nets.
- [ ] Dot product: algebraic formula and geometric interpretation (alignment).
- [ ] Layer computation: \( \mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b} \); correct shapes (\( m \times n \), \( n \times 1 \), \( m \times 1 \)).
- [ ] Derivative vs partial derivative; why partials are needed for learning.
- [ ] Gradient: definition, direction of steepest increase, role in minimization.
- [ ] Chain rule: \( \frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx} \); application to two-layer example.
- [ ] Overflow, underflow, log-sum-exp trick and why numerical stability matters.
