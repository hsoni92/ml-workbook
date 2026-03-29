# Backpropagation and Training Dynamics – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **Understand** the central question: how does a neural network **improve** using data?
2. **Describe** the training loop: forward pass → loss → gradients → parameter update.
3. **Recognize** **backpropagation** as the process that distributes **responsibility for error** across the network.
4. **See** the shift from **structure and forward computation** to **adaptation, learning, and optimization**.

---

## The Central Question

- So far: how networks are **structured** and how they **compute outputs** (forward pass); MLPs, hidden layers, activation functions.
- **Missing:** When the network makes a mistake, how does it know **what went wrong** and **what to change**?
- **Answer:** Training adjusts **weights and biases** so predictions improve; the math that makes this possible is **backpropagation**.

---

## Training Steps

1. **Forward pass:** Compute predictions from the model.
2. **Loss computation:** Compare predictions with ground truth → measure **error**.
3. **Gradient computation:** Compute gradients of the loss w.r.t. each parameter → **how much** each parameter contributes to the error.
4. **Parameter update:** Correct parameters gradually using these gradients.

**Backpropagation** is the process that determines how **responsibility for error** is distributed across the entire network.

---

## What This Module Covers

- **What** backpropagation actually computes.
- How **gradients flow** through multiple layers.
- Why **initial values** of weights matter for stability.
- How **loss functions** influence learning.
- Why deep networks suffer from **vanishing and exploding gradients** and how to **diagnose and mitigate** them.

---

## Conceptual Shift

- **Earlier modules:** Network **structure**, representations, **forward** computation.
- **This module:** **Adaptation**, learning, optimization — connecting forward computation, **error signals**, and **gradient-based** parameter updates into one **unified learning process**.
