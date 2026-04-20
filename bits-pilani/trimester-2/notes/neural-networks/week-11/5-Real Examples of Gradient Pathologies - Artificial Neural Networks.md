# Real Examples of Gradient Pathologies - Artificial Neural Networks

## Learning Objective

Recognize common gradient failures from their **observable signatures** instead of treating every broken run as a mystery.

---

## Why This Lesson Matters

So far, the module has introduced gradient flow conceptually and shown how to measure it. This lesson asks a more practical question:

> Given a broken training run, how do I identify which gradient problem I am seeing?

That is the real diagnostic skill. In practice, we do not debug abstract definitions. We debug **patterns**.

---

## Controlled Failure Cases

The transcript keeps the dataset fixed and also keeps the same deep network architecture. Only the configuration is changed. This is good diagnostic practice because it isolates the cause of failure.

Three cases are demonstrated:

1. **Vanishing gradients**
2. **Exploding gradients**
3. **Dead gradient paths**

Each produces a different signature in the layer-wise gradient plots.

---

## Case 1: Vanishing Gradients

In this case, the model uses a deep network with settings that encourage gradient decay.

### Signature

- gradient magnitudes are extremely small in earlier layers,
- gradients become larger only near the output side,
- and the overall pattern shows clear decay as we move backward.

### Interpretation

This means the learning signal weakens as it propagates through depth. The early layers therefore learn very slowly or may stop learning altogether.

### Practical symptom

Training may appear to progress slightly, but the foundational layers that should learn useful features are barely being updated.

---

## Case 2: Exploding Gradients

This case deliberately uses a very high learning rate in a deep network.

### Signature

- gradients are not uniformly large at first,
- instead they show **uneven amplification**,
- with much larger values appearing in later layers.

The transcript makes an important point here: exploding gradients often do not appear instantly as a dramatic blow-up. They may begin as a pattern of rapidly increasing gradient magnitudes across layers.

### Interpretation

This uneven amplification is an early warning sign of instability. If training continues with the same setup, it can develop into full gradient explosion and unstable updates.

---

## Case 3: Dead Gradient Paths

This case uses extremely small initialization values.

### Signature

- gradient norms are effectively zero across all layers,
- the gradient signal is absent rather than merely weak.

### Interpretation

This is different from vanishing gradients.

- In **vanishing gradients**, the signal decays numerically through depth.
- In **dead gradient paths**, the signal is blocked altogether due to a configuration or architectural problem.

Possible causes mentioned in the transcript include:

- bad initialization,
- frozen layers,
- or explicit gradient blocking.

---

## How to Distinguish the Patterns

| Failure mode | What you see | What it means |
|---|---|---|
| **Vanishing gradients** | Early layers go dark, later layers retain signal | Learning signal decays backward |
| **Exploding gradients** | Magnitudes grow sharply and unevenly | Updates are becoming unstable |
| **Dead gradient paths** | Gradients are essentially zero everywhere | Signal is blocked, not just weakened |

This comparison is one of the most useful exam-ready distinctions in the lesson.

---

## The Main Diagnostic Habit

The lesson teaches a very important workflow:

1. Observe the training symptoms.
2. Inspect the layer-wise gradients.
3. Match the observed pattern to a known failure signature.
4. Only then think about fixes.

In other words, **diagnostics comes before intervention**.

---

## Key Takeaways

- Gradient failures leave identifiable signatures.
- Many training problems come from configuration choices rather than code bugs.
- Layer-wise measurement helps distinguish between decay, instability, and complete blockage.
- Good debugging starts by recognizing the pattern, not by randomly changing hyperparameters.

**Bridge to the next topic:** after diagnosing gradient failures, the module moves to activation-level failures, beginning with **dead ReLUs**.
