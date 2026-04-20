# Model Diagnostics - Artificial Neural Networks

## Learning Objectives

By the end of this module, you should be able to:

1. Explain the difference between **evaluating** a model and **diagnosing** a model.
2. Identify the three main internal signals used for debugging deep networks: **gradients**, **activations**, and **parameters**.
3. Describe why deep neural networks often fail **silently** even when code executes without errors.
4. Build a structured mindset for moving from a visible symptom to a likely internal cause.

---

## Why This Module Matters

In the previous module, the main question was: **How good is the model?**

In this module, the question becomes: **Why is the model behaving this way?**

That shift is important. A model may show poor accuracy, unstable loss, or weak generalization, but those external metrics only tell us that something is wrong. They do not tell us **where** the problem is or **what mechanism** caused it.

Neural networks are difficult to debug because they are:

- **deep**, with many interacting layers,
- **non-linear**, so small internal changes can have large effects,
- and often **silent in failure**, meaning training appears to run even when learning has effectively stopped.

So model diagnostics is about opening the black box and learning how to read the internal signals left behind by failure.

---

## Evaluation vs Diagnostics

This is the central contrast of the module:

| Question | Evaluation | Diagnostics |
|---|---|---|
| Main goal | Measure performance | Explain behavior |
| Typical signals | Accuracy, loss, calibration, robustness | Gradients, activations, weights, normalization statistics |
| What it tells you | **What** went wrong | **Where** and **why** it went wrong |

A useful way to remember this:

- **Evaluation** is outcome-focused.
- **Diagnostics** is mechanism-focused.

Both are necessary, but diagnostics becomes essential once a training run looks suspicious and the loss curve alone is no longer enough.

---

## The Three Diagnostic Levels

Throughout this module, we inspect neural networks at three internal levels.

### 1. Gradients

Gradients tell us whether the learning signal is actually flowing backward through the network.

- If gradients vanish, earlier layers learn very slowly.
- If gradients explode, updates become unstable.
- If some layers receive almost no gradient, training may look normal from the outside while part of the model is effectively frozen.

### 2. Activations

Activations tell us whether neurons are responding meaningfully to data.

- ReLU units can become permanently inactive.
- Sigmoid and tanh units can saturate near their limits.
- A network may therefore stop learning not because the optimizer failed, but because the neurons stopped operating in useful regimes.

### 3. Parameters and Internal Statistics

Parameters reveal whether the model is actually changing during training.

- Weight distributions and norms show whether learning is balanced across layers.
- BatchNorm running statistics reveal hidden instability in internal feature distributions.
- Frozen or abnormal parameters often expose configuration mistakes that do not appear clearly in metrics.

---

## Module Roadmap

This module follows a clear progression:

1. Start with **gradient flow**, because gradients are the most direct signal of whether learning is happening.
2. Move to **activation pathologies**, such as dead ReLUs and saturation.
3. Examine **parameter behavior**, including weight drift, norms, BatchNorm statistics, and anomalies.
4. Bring everything together into a **structured debugging workflow** supported by tools like TensorBoard and experiment tracking.

This makes the module intentionally practice-driven. The point is not just to memorize definitions, but to build **diagnostic intuition**.

---

## Big Picture Takeaway

When a neural network fails, the cause is often visible inside the model before it becomes obvious in the final metrics.

The goal of this module is therefore simple:

- do not guess,
- do not rely only on loss curves,
- and do not treat every failure as random.

Instead, inspect the internal signals, form a hypothesis, and verify it with evidence.

**Bridge to the next topic:** we begin with the most fundamental internal signal of all, **gradient flow**, and why it is often the first thing to inspect in a deep network.
