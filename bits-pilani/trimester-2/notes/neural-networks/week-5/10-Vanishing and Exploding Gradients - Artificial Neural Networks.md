# Vanishing and Exploding Gradients – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **Explain** why gradients **shrink** or **grow** as they pass through many layers.
2. **See** how the **chain rule** creates these effects.
3. **Recognize** the **symptoms** of vanishing and exploding gradients during training.
4. **Understand** how **activation functions** and **initialization** influence gradient flow.

---

## Origin: Chain Rule in Depth

- In backpropagation, each layer contributes a **local derivative**.
- These derivatives are **multiplied** together through the chain rule.
- So the gradient at an early layer is a **product** of many local derivatives (and the loss derivative at the output).
- **If** most derivatives are **&lt; 1** → gradient **shrinks** (vanishing).
- **If** most are **&gt; 1** → gradient **grows** rapidly (exploding).

---

## Vanishing Gradients

- **When:** Most layer-wise derivatives are **less than 1**.
- **Causes:**
  1. **Saturating activations** (sigmoid, tanh): derivatives become very small, often near 0.
  2. **Weights initialized too small:** activations stay small → derivatives stay small.
- **Effect:** Multiply many numbers &lt; 1 → **exponential** shrinkage. Example: 0.5\(^{20}\) ≈ 10\(^{-6}\) ≈ 0. Early layers get **almost no** gradient → they **stop learning**.

---

## Exploding Gradients

- **When:** Most derivatives are **greater than 1** (e.g. weights too large, or activations amplifying inputs).
- **Effect:** Each layer multiplies the gradient by something &gt; 1; after 20–30 layers this becomes huge. Example: 1.5\(^{20}\) ≈ 3300. Updates become **enormous** → **unstable** or **divergent** training.

---

## Role of Activation Functions

- **Sigmoid:** Derivative ≤ 0.25, and **nearly 0** when saturated → strongly encourages **vanishing**.
- **Tanh:** Zero-centered but still **saturates** → derivatives near 0.
- **ReLU:** Derivative is **0** or **1** → does **not** shrink gradients (in the active region). But with **large** weights, even ReLU nets can have **exploding** gradients.
- So **activation choice** directly affects gradient flow.

---

## How to Recognize the Problem

**Vanishing:**
- First few layers **barely** change.
- Training accuracy **plateaus** very early.
- Loss decreases **very slowly**.

**Exploding:**
- Loss **suddenly** spikes or becomes **NaN**.
- Weight values become **very large**.
- Updates look **chaotic** and unstable.

Recognizing these symptoms helps **troubleshoot** training failures quickly.

---

## Summary

- Deep networks **repeatedly multiply** local derivatives; **&lt; 1** → vanishing, **&gt; 1** → exploding.
- Both make training **difficult** or **impossible**.
- **Activation** choice and **initialization** strongly influence gradient flow.
- Understanding these effects is the basis for building **more stable**, **deeper** networks.
