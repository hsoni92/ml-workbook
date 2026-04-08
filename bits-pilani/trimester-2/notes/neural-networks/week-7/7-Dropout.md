# Dropout – Artificial Neural Networks (Module 7)

## Learning Objectives

By the end of this video you will:

1. **Explain** the **intuition** for Dropout: breaking **co-adaptation** among neurons.
2. **Describe** how Dropout acts as **stochastic regularization** during training.
3. **Distinguish** **training** vs **inference** behavior and **scaling** of activations.
4. **Recall** typical **dropout rate** ranges and practical caveats.

---

## Motivation: Co-adaptation

- As networks grow, **overfitting** risk rises.
- **Co-adaptation:** neurons **depend heavily** on specific other neurons to produce correct outputs.
- The model becomes **fragile**: predictions hinge on a **narrow** set of activations.
- **Dropout** reduces reliance on **any single neuron** by randomly **disabling** units during training.

---

## Core Mechanism (Training)

- Each training step (often per **mini-batch**), a **random subset** of neurons is **dropped**: they do **not** participate in the **forward** pass (and corresponding **backward** pass) for that step.
- The effective **subnetwork** **changes** from step to step.
- The model **cannot** depend on one fixed set of hidden features; it is pushed toward **redundant**, **distributed** representations.
- Viewed another way, Dropout injects **noise** into training, discouraging **over-precise** fit to the training set.

---

## Mathematical View (Mask)

- Let **M** be a **binary mask** (per neuron or per connection, depending on implementation details).
- Each kept unit’s output is multiplied by **M** where **M ~ Bernoulli(p)** (or “keep probability” **p**; some texts define **p** as drop probability—always check convention in code/docs).
- **M = 1:** neuron **active**; **M = 0:** neuron **dropped**.

---

## Training vs Inference

- **Training:** Dropout **on**—random masks applied each step.
- **Inference:** **All** neurons **active**; we need **consistent** expected scale of activations vs training.

**Scaling:**

- If a neuron is kept with probability **p**, its expected contribution is scaled by **p** during training unless we compensate.
- **Inverted dropout (common in practice):** during **training**, activations of kept units are **scaled up** (e.g. divide by **p** or equivalent) so that at **test time** **no** extra scaling is needed—**inference** uses the **full** network **without** dropout and **without** a separate scaling pass.

---

## Hyperparameters and Practice

- Typical **keep** probabilities (lecture-style ranges—implementations vary):
  - **Input** layers: often **lower dropout** (e.g. keep around **0.7–0.9**, i.e. drop ~0.1–0.3 if drop prob is used).
  - **Hidden** layers: **moderate** dropout (e.g. keep **0.5–0.7** as a common ballpark).
- Dropout helps **less** on **very small** networks.
- Often **combined** with **L2** or other regularizers; rates usually need **tuning**.

---

## Summary

- **Dropout** = random neuron dropping during training → **less co-adaptation**, **more robust** distributed features, **implicit** regularization via noise.
- **Training** samples many **thinned** networks; **inference** uses the **full** network with **consistent scaling** (often via **inverted** dropout in training).
- **Next:** **Batch normalization**—stability during optimization and **implicit** regularization from batch statistics.

---

## Exam-style cues

- **Define** co-adaptation and how dropout mitigates it.
- **Contrast** training and test-time dropout behavior.
- **Explain** why scaling (or inverted dropout) is needed between train and inference.
