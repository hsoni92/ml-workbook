# Neural Networks – Module 5 Summary: Artificial Neural Networks

## Purpose of This Module

Module 5 focuses on **backpropagation** and **training dynamics**: how neural networks **learn** by computing gradients and updating parameters. The goal is to connect **forward computation**, **loss**, **gradient flow**, and **stability** into a single learning process.

---

## What We Learned (Flow of Module 5)

| Topic | Content |
|-------|--------|
| **Backpropagation** | Computes **gradients** of the loss w.r.t. every parameter; gradients = sensitivity/responsibility signals; backprop does **not** perform optimization, only gradient computation. |
| **Computational graphs** | Represent computation as nodes and edges; **local gradients** at each edge; **global** gradients = product of locals along paths (chain rule); one graph for forward and backward. |
| **Backprop step-by-step** | Forward pass and caching; backward pass from output; gradients for output layer, then propagated to hidden layer through activation; gradients for first-layer weights and biases. |
| **Gradient flow** | How learning signals move **backward** through depth; **vanishing** (gradients → 0) and **exploding** (gradients → ∞); early layers farthest from error, most affected. |
| **Initialization** | Zero **weights** break learning (symmetry); zero **bias** OK; **Xavier** for sigmoid/tanh; **He** for ReLU; goal = stable variance forward and backward. |
| **Loss functions** | **MSE** for regression (squared distance); **softmax + cross-entropy** for classification; MSE poor for classification (geometry, saturation, weak penalties). |
| **Loss and gradients** | Loss **shapes** gradients; cross-entropy gives stronger, better-shaped gradients for classification than MSE, especially when wrong. |
| **Vanishing/exploding** | Chain rule multiplies many derivatives; &lt; 1 → vanish, &gt; 1 → explode; activation and initialization are key. |
| **Mitigation** | Initialization (Xavier, He), ReLU family, **gradient clipping**, **normalization** (batch, layer). |

---

## Key Intuitions to Retain (Exam-Ready)

1. **Backpropagation** = gradient computation only; **optimization** uses those gradients to update parameters.
2. **Gradient** = how sensitive the loss is to a parameter; sign (direction) and magnitude (strength).
3. **Computational graph** + **local** gradients + **chain rule** = efficient backprop.
4. **Gradient flow** must reach all layers; **vanishing** and **exploding** break training.
5. **Initialization** (Xavier/He) and **activation** (ReLU family) are foundational for stable flow.
6. **MSE** for regression; **softmax + cross-entropy** for classification; wrong loss → bad gradients and slow or stuck learning.
7. **Gradient clipping** and **normalization** are standard tools for stability in deep nets.

---

## Bridge to Module 6

In Module 6 we move from **how gradients behave** to **how we use them**:

- **Optimizers:** momentum, RMSProp, Adam.
- **Learning rate** scheduling.
- **Practical** training dynamics: convergence, pitfalls, gradient clipping in context, choosing optimizers.

These concepts help **debug**, **speed up**, and **stabilize** training in real applications.
