# Sigmoid and Tanh Activation Functions – Artificial Neural Networks (Module 4)

## Learning Objectives

By the end of this video you will:

1. **State** the mathematical definitions of **sigmoid** and **tanh**.
2. **Interpret** their output ranges and shapes.
3. **Understand** their **saturation** behaviour.
4. **Compare** where each is used in practice.

---

## Why Sigmoid and Tanh First?

- They are the **classical** activation functions used in early neural networks.
- They provide **smooth, continuous** non-linearity and help us understand the **limitations** that led to modern activations like ReLU.
- **Sigmoid** is tied to logistic regression; **tanh** was a standard choice for hidden layers in early deep networks.

---

## Sigmoid

**Definition:**
$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$
- Maps any real input to the range $(0, 1)$.
- **S-shaped** curve.
- Output can be interpreted as a **probability** → commonly used in the **output layer** for **binary classification**.

**Behaviour:**

- $z$ large and positive → output close to **1**.
- $z$ large and negative → output close to **0**.
- Around $z = 0$, sigmoid changes **most rapidly**.
- Sigmoid turns a real-valued score into a **soft** yes/no (probability) rather than a hard threshold.

---

## Tanh (Hyperbolic Tangent)

**Definition:**
$$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$
- Like sigmoid, an **S-shaped** curve.
- Output range: $(-1, +1)$ → **zero-centered**.
- Tanh is a **rescaled and shifted** version of sigmoid.
- Historically used in **hidden layers** of classical neural networks.

---

## Zero-Centering: Sigmoid vs Tanh

- **Sigmoid:** Output always **positive** $(0, 1)$.
- **Tanh:** Output **centered at 0** $(-1, +1)$.
- Zero-centered activations often give **better optimization** during training because activations can be balanced between positive and negative; **tanh** was often preferred over sigmoid in hidden layers for this reason.

---

## Saturation

- **Both** sigmoid and tanh **saturate**: when $|z|$ is large, the output changes **very slowly** even when $z$ changes a lot.
- During training, **gradients** at saturated neurons become **very small**.
- This is a main cause of the **vanishing gradient** problem in deep networks.
- Even before studying gradients in detail, it is important to know: **saturation** makes training deep networks with sigmoid/tanh **difficult**.

---

## Use in Practice

- **Sigmoid:** Most common in the **output layer** for **binary classification** (output as probability).
- **Tanh:** Historically used in **hidden layers** (early architectures).
- In **modern** deep learning, both are used **sparingly** in hidden layers because of **saturation** and **vanishing gradients**; ReLU and its variants have largely replaced them there.

---

## Summary

- **Sigmoid** and **tanh** are smooth nonlinear activation functions.
- Sigmoid: $(0, 1)$; tanh: $(-1, +1)$, zero-centered.
- Both **saturate** for large $|z|$, leading to small gradients and training difficulties in deep nets.
- These limitations motivated **ReLU** and related activations, which we study next.
