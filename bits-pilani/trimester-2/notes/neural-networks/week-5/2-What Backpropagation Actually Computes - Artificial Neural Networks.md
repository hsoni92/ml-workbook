# What Backpropagation Actually Computes – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **State** what quantity backpropagation computes inside a neural network.
2. **Interpret** a gradient as a **sensitivity** or **responsibility** signal.
3. **Distinguish** backpropagation from **optimization**.
4. **Interpret** the **sign** and **magnitude** of a gradient using a simple example.

---

## The Problem Backpropagation Solves

- A network has many **parameters** (weights and biases).
- A forward pass uses all of them to produce **one prediction**.
- If the prediction is wrong: **which** parameters are responsible and **by how much**?
- **Backpropagation** computes a **responsibility signal** for **every** parameter.

---

## What We Need to Improve the Network

For every parameter we need:

1. **Direction:** Should it **increase** or **decrease**?
2. **Strength:** How **strongly** should it change?

This is exactly what a **gradient** (partial derivative of the error w.r.t. that parameter) provides.

---

## The Gradient

- **Gradient** = how **sensitive** the error is to that parameter.
- Question it answers: *If I change this parameter a little, how much does the error change?*
- Backpropagation computes **one gradient per parameter** (partial derivative of loss w.r.t. each weight and bias).
- These gradients are the **only** information needed by any learning algorithm to perform parameter updates.

---

## Interpreting the Gradient

For a parameter $\theta$:

- **Positive gradient:** Increasing $\theta$ **increases** the error → we should **decrease** $\theta$ (move opposite to the gradient).
- **Negative gradient:** Increasing $\theta$ **decreases** the error → we should **increase** $\theta$.
- **Zero gradient:** $\theta$ has no local effect on the error.
- **Magnitude:** How **strongly** the error reacts to that parameter.

---

## Simple Numerical Example

- Model: $y = wx$. Given $x = 2$, true $y = 10$. Initialize $w = 1$.
- Predicted $y = wx = 2$. Error: $E = (y - y_{\text{true}})^2 = (wx - 10)^2$.
- Gradient: $\frac{\partial E}{\partial w} = 2(wx - 10) \cdot x = 2(wx - 10) \cdot 2$.
- At $w = 1$: $\frac{\partial E}{\partial w} = 2(2 - 10) \cdot 2 = -32$.
- **Negative** → increasing $w$ reduces error; **magnitude 32** → strong sensitivity. This one number gives both **direction** and **strength** of the update.

---

## Backpropagation vs Optimization

- **Backpropagation:** Only **computes gradients**; it does **not** update parameters, use a learning rate, or implement an optimizer.
- **Optimization** (e.g. gradient descent, Adam) **uses** these gradients to **update** parameters.
- Without gradients, learning cannot proceed; every training algorithm starts from the gradients produced by backpropagation.

---

## Summary

- Backpropagation computes **gradients** of the error (loss) w.r.t. **every** parameter.
- A gradient encodes **sensitivity**: direction (increase/decrease) and strength of influence on the error.
- Backpropagation **does not** perform learning; it only **provides the information** required for learning.
