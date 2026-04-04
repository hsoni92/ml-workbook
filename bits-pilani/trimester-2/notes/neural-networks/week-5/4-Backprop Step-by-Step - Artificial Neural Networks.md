# Backprop Step-by-Step – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **Trace** the **forward pass** and identify all intermediate variables used in backprop.
2. **Apply** the chain rule to compute gradients for **every** weight and bias in a two-layer network.
3. **See** that backpropagation only **computes** gradients; it does **not** update parameters.

---

## Network Setup

- **Two-layer** network: one input $x$, one hidden neuron, one output neuron.
- **Layer 1:** $z_1 = w_1 x + b_1$, $h = \sigma(z_1)$.
- **Layer 2:** $z_2 = w_2 h + b_2$, $\hat{y} = z_2$.
- **Loss:** $E(\hat{y})$.
- “Two-layer” = one hidden layer + one output layer.

---

## Forward Pass and Caching

1. $z_1 = w_1 x + b_1$, then $h = \sigma(z_1)$ — **store** $z_1$, $h$.
2. $z_2 = w_2 h + b_2$, $\hat{y} = z_2$.
3. Compute $E(\hat{y})$.

**Cached:** $x, z_1, h, z_2, \hat{y}$. These make the backward pass possible.

**Goal:** Compute $\frac{\partial E}{\partial w_2}, \frac{\partial E}{\partial b_2}, \frac{\partial E}{\partial w_1}, \frac{\partial E}{\partial b_1}$.

---

## Backpropagation: Start at Output

- Backprop always **starts at the output**.
- $\hat{y} = z_2$ ⇒ $\frac{\partial E}{\partial \hat{y}} = \frac{\partial E}{\partial z_2}$. This is the initial gradient signal.

---

## Output Layer Parameters

- $z_2 = w_2 h + b_2$.
- $\frac{\partial E}{\partial w_2} = \frac{\partial E}{\partial z_2} \cdot \frac{\partial z_2}{\partial w_2} = \frac{\partial E}{\partial z_2} \cdot h$.
- $\frac{\partial E}{\partial b_2} = \frac{\partial E}{\partial z_2} \cdot \frac{\partial z_2}{\partial b_2} = \frac{\partial E}{\partial z_2} \cdot 1$.

Output layer is fully differentiated; $w_2$ and $b_2$ have their gradients.

---

## Propagate to Hidden Activation

- $\frac{\partial E}{\partial h} = \frac{\partial E}{\partial z_2} \cdot \frac{\partial z_2}{\partial h} = \frac{\partial E}{\partial z_2} \cdot w_2$.
- This is how much the **hidden** neuron contributed to the error. The hidden layer never sees the error directly; it only sees this **propagated** signal.

---

## Through the Activation Function

- $h = \sigma(z_1)$ ⇒ $\frac{\partial E}{\partial z_1} = \frac{\partial E}{\partial h} \cdot \frac{\partial h}{\partial z_1}$.
- $\frac{\partial h}{\partial z_1}$ is the **derivative of sigmoid** at $z_1$.
- The **activation function** directly affects how gradients flow; this step shows that clearly.

---

## First-Layer Parameters

- $z_1 = w_1 x + b_1$.
- $\frac{\partial E}{\partial w_1} = \frac{\partial E}{\partial z_1} \cdot \frac{\partial z_1}{\partial w_1} = \frac{\partial E}{\partial z_1} \cdot x$.
- $\frac{\partial E}{\partial b_1} = \frac{\partial E}{\partial z_1} \cdot \frac{\partial z_1}{\partial b_1} = \frac{\partial E}{\partial z_1} \cdot 1$.

All parameter gradients are now available.

---

## Visual Summary

- **Forward:** $x \to z_1 \to h \to z_2 \to \hat{y} \to E$.
- **Backward:** $E \to \hat{y}/z_2 \to h \to z_1$; from each pre-activation, gradients branch to the corresponding weights and biases.
- The **same** network used for prediction is reused **in reverse** to assign responsibility for the error.

---

## What We Did Not Do

- We **did not** update any parameters, use a learning rate, or apply an optimizer.
- Backpropagation is **only** the gradient computation step. Parameter updates come when we study **optimization**.

---

## Summary

- Backprop works by **chaining local derivatives** backward.
- **Output-layer** gradients are computed first; **hidden-layer** gradients come only via propagation.
- This small two-layer example contains the **full structure** of backprop in deep networks; everything in very deep nets is an extension of this same idea.
