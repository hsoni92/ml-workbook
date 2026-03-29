# ReLU Family – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **Define** the **ReLU** activation function.
2. **Explain** why ReLU replaced sigmoid and tanh in most deep learning systems.
3. **Identify** main **variants** of ReLU (Leaky ReLU, PReLU).
4. **Understand** practical advantages and limitations of ReLU-based activations.

---

## Motivation for ReLU

- Sigmoid and tanh introduce non-linearity but **saturate** for large \( |z| \) → **vanishing gradients** and difficulty training very deep networks.
- We need an activation that: stays **non-linear**, **avoids saturation** in a large region, and allows **faster, more stable** training → **ReLU family**.

---

## ReLU (Rectified Linear Unit)

**Definition:**
\[
f(z) = \max(0, z) = \begin{cases} z & \text{if } z > 0 \\ 0 & \text{if } z \leq 0 \end{cases}
\]

- **Piecewise linear**, very cheap to compute.
- For **positive** inputs, ReLU **does not saturate** (unlike sigmoid/tanh).
- This property is very effective for training **deep** networks.

---

## Why ReLU Became Default

1. **No saturation** for \( z > 0 \) → gradients and information flow more easily through many layers.
2. **Faster and more stable** training than sigmoid/tanh.
3. **Sparse activations:** many neurons output exactly 0 → can help generalization and reduce computation.
4. **Computationally cheap** to evaluate.

---

## Dying ReLU

- For \( z \leq 0 \), ReLU outputs **0**.
- If during training a neuron’s parameters shift so that its **input is always negative**, it will **always** output 0.
- The neuron then **stops participating** in the network (“dead” ReLU).
- This motivated **variants** that keep ReLU’s benefits while reducing the risk of dead neurons.

---

## Leaky ReLU

- For \( z < 0 \), instead of 0, use a **small negative slope**: \( \alpha z \) with \( \alpha \) small (e.g. 0.01).
\[
f(z) = \begin{cases} z & z > 0 \\ \alpha z & z \leq 0 \end{cases}
\]
- Even for negative inputs the neuron gives a **small non-zero** output → less likely to “die”.
- Keeps most advantages of ReLU with better robustness.

---

## PReLU (Parametric ReLU)

- Same form as Leaky ReLU, but the slope \( \alpha \) in the negative region is **learned** (a parameter updated during training).
- Gives the model flexibility to adapt how much information flows in the negative region.
- Used in some high-performance vision models; adds a few extra parameters.

---

## Comparison

| Activation | Negative region | Notes |
|------------|------------------|--------|
| **ReLU**   | 0                | Default for most hidden layers |
| **Leaky ReLU** | Small fixed slope \( \alpha z \) | Reduces dying ReLU |
| **PReLU**  | Learnable slope  | More flexibility, extra parameters |

All three keep: **non-linearity**, **efficiency**, and **stable** behaviour in deep networks.

---

## Practical Guidelines

- **ReLU** as the first baseline for almost all hidden layers.
- If many **inactive** neurons are observed, try **Leaky ReLU**.
- **PReLU** when a small performance gain justifies extra parameters.
- In most pipelines, **standard ReLU** remains the default.

---

## Summary

- **ReLU:** \( f(z) = \max(0, z) \); avoids saturation for \( z > 0 \); enables fast, stable training; default in modern deep learning.
- Main drawback: **dying ReLU**; addressed by **Leaky ReLU** and **PReLU**.
- The ReLU family is the **backbone** of most current neural network architectures.
