# Neural Networks – Module 3 Summary: Artificial Neural Networks

## Purpose of This Module

Module 3 focuses on the **first building blocks** of neural networks: the **Perceptron** and the **Logistic Neuron**. The goal is to build a clear understanding of **linear classification**, **model limitations**, and the **motivation for deeper architectures**.

---

## What We Learned (Flow of Module 3)

| Topic | Content |
|-------|--------|
| **Perceptron** | Simplest computational model of a neuron: linear score \( \mathbf{w}^T \mathbf{x} + b \) + **hard threshold** → binary output (+1 / -1). Linear binary classifier. |
| **Geometry** | One straight decision boundary (line/hyperplane); **weights** = orientation, **bias** = position. |
| **Linear separability** | Perceptron works when data **can** be separated by one line; **fails** when it cannot. |
| **XOR** | Classic **non–linearly separable** problem; single Perceptron **cannot** solve it (structural limit). |
| **Hidden layer** | Multiple linear splits → recombined at output → **non-linear** decision regions; solves XOR. |
| **Logistic neuron** | Replaces **hard** threshold with **sigmoid**; **continuous** output in (0,1), interpretable as **probability**; same **linear** decision boundary, **smooth** transition across it. |
| **Perceptron vs logistic** | Same linear score; different activation (step vs sigmoid); logistic gives **confidence** and allows **gradient-based** training. |

---

## Key Intuitions to Retain (Exam-Ready)

1. **Perceptron** = linear score + **step** function → binary classifier; one linear boundary.
2. **Linearly separable** = one line (hyperplane) can separate the two classes; Perceptron can converge.
3. **XOR** = same-class points diagonally opposite → **no** single line → Perceptron fails; motivates **multi-layer** networks.
4. **Hidden layer** = multiple linear boundaries combined → **more expressive** than single Perceptron.
5. **Logistic neuron** = same linear score + **sigmoid** → **probability** and **smooth** optimization; core building block of modern neural nets.

---

## Big Picture

We moved from:
- **Perceptron** as a basic linear classifier  
→ **Geometric limits** (XOR)  
→ **Architectural** motivation for **hidden layers**  
→ **Logistic neuron** as the smooth, probabilistic building block of modern neural networks.

---

## Bridge to the Next Module

In the next module we build on this foundation to study:

- **Architecture** of multi-layer Perceptrons (MLPs).
- How **hidden layers** and **forward** passes work.
- **Non-linearity** and **activation functions** in depth.
- **Practical** issues in training and design.

---

## Quick Revision Checklist

- [ ] Define Perceptron: equation, output (+1 / -1), decision boundary (line/hyperplane).
- [ ] Explain linear separability and the condition \( y_i(\mathbf{w}^T \mathbf{x}_i + b) > 0 \) for all \( i \).
- [ ] Describe XOR and why a single Perceptron cannot solve it.
- [ ] State Perceptron learning rule: when to update, update equations, convergence only for linearly separable data.
- [ ] Define logistic neuron: sigmoid, output as probability, decision boundary still linear.
- [ ] Compare Perceptron vs logistic: hard vs smooth, label vs probability, why logistic is preferred.
- [ ] Explain how a hidden layer solves XOR (multiple linear boundaries combined).
