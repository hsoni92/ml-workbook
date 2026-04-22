# Batch Normalization – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Explain** why **internal covariate shift** (changing activation distributions) makes deep training hard.
2. **Describe** how **batch normalization (BN)** normalizes activations **per mini-batch** and **re-scales** them with learnable parameters.
3. **State** practical benefits: **stability**, **learning rate**, **initialization** sensitivity, **convergence**.
4. **Explain** how **batch statistics noise** can act as **implicit regularization**.

---

## Problem: Unstable Activations Across Layers

- In deep nets, as **lower layers** update, the **distribution** of inputs to **higher layers** can **shift** even from **small** changes below.
- That **internal** change in activation statistics makes optimization **harder**: slower convergence, more sensitivity to **learning rate** and **initialization**.
- **Batch normalization** was introduced to stabilize training by **standardizing** layer inputs (typically **pre-activation** or **post-activation** depending on architecture convention—frameworks differ; the **idea** is normalizing a chosen tensor along the **batch** dimension).

---

## Core Idea

- For each **mini-batch**, compute **mean** and **variance** of activations (over the batch, and typically per feature/channel).
- **Normalize** to approximately **zero mean** and **unit variance**, with a small **$\epsilon$** for **numerical stability** when dividing by standard deviation:

$$
\hat{x} = \frac{x - \mu_{\text{batch}}}{\sqrt{\sigma_{\text{batch}}^2 + \epsilon}}
$$

- This keeps activations in a **stable** range across iterations and can help **gradient flow** behave more predictably.

---

## Learnable Scale and Shift

- Pure normalization could **limit** what the layer can represent.
- BN adds **learnable** parameters **$\gamma$** (scale) and **$\beta$** (shift):

$$
y = \gamma \hat{x} + \beta
$$

- The network can **recover** needed scaling and bias, so expressive power is **not** arbitrarily restricted.

### Visual: BN block inside a layer

```mermaid
flowchart LR
  xin[Activations x] --> norm[Normalize using batch mean and var]
  norm --> gamma[Scale by gamma]
  gamma --> beta[Shift by beta]
  beta --> yout[Output y to next op]
```

---

## Implicit Regularization

- Normalization uses statistics from **mini-batches**; different batches give **slightly different** $\mu$, $\sigma$.
- That **randomness** injects **noise** into the forward pass—**similar in spirit** to dropout’s stochasticity, but arising from **batch estimation**.
- In practice this noise can **help generalization** (implicit regularizer), though BN’s main motivation is **optimization stability**.

---

## Practical Advantages (Lecture Summary)

- Often allows **higher learning rates**.
- Reduces sensitivity to **initialization**.
- Frequently **speeds up** convergence.
- Stabilizing effect can **reduce** reliance on **other** regularizers in **some** settings (not always—still task-dependent).

---

## Summary

- **BN** stabilizes layer input statistics by **batch-wise** normalization + **$\gamma,\beta$** recovery.
- **Batch statistic noise** can improve **generalization** as **implicit** regularization.
- **Next:** **Early stopping**—a simple, effective way to **limit** overfitting by **when** we stop training.

---

## Exam-style cues

- **Explain** why shifting activation distributions complicates deep optimization.
- **Write** the normalize-then-scale-shift form of BN.
- **Contrast** BN’s implicit regularization with **dropout** (source of randomness).
