# Weight Norms and Training Signals - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain what a **weight norm** measures.
2. Use weight norms as a compact signal of training health.
3. Interpret different norm patterns across layers and across epochs.

---

## Why Weight Norms Are Useful

In the previous lesson, we looked at full weight distributions. That gives rich detail, but it can also be more information than we need for a quick diagnosis.

Weight norms provide a simpler summary.

They act like a compact training signal that tells us:

- how large the parameters are,
- whether learning pressure is balanced across layers,
- and whether weights are growing, shrinking, or staying flat.

The transcript describes them as a kind of **heartbeat** for training dynamics.

---

## What the Lesson Shows

The same dataset and general model setup are reused to maintain continuity.

The note focuses on two views:

1. **weight norms across layers at the final epoch**
2. **weight norm evolution across time**

This makes it possible to compare how different layers behave and how those behaviors change during training.

---

## Interpreting Weight Norms Across Layers

At the final epoch, most hidden layers show similar L2 norms.

### What this suggests

- learning pressure is fairly balanced across depth,
- no hidden layer appears grossly over-dominant,
- and the training process is behaving in a controlled way.

The transcript also points out that the **output layer** has a noticeably smaller norm.

That is not treated as a problem. In this example, it is expected because:

- the output layer maps learned representations to a single logit,
- it has fewer parameters,
- and its updates are directly tied to the supervised loss.

So this lesson also teaches an important diagnostic caution:

> not every difference across layers is a failure.

Some differences are structurally expected.

---

## Interpreting Weight Norms Over Time

Across epochs, the hidden layers show **smooth, gradual growth**.

That is the key healthy pattern.

### Why smooth growth matters

- It suggests stable optimization.
- It indicates that the model is learning without runaway instability.
- It gives confidence that updates are meaningful but not excessive.

The output layer again evolves more slowly and remains lower in magnitude, which is consistent with its smaller representational role in this setup.

---

## What Different Norm Patterns Mean

The transcript gives three especially useful interpretations:

- **flat norms** may mean layers are frozen or under-trained,
- **exploding norms** suggest unstable optimization,
- **smooth growth** usually indicates healthy learning.

This makes weight norms a convenient early warning signal.

---

## Why Norms Complement Distribution Diagnostics

Weight distributions give detailed shape information.

Weight norms compress that information into one number per layer, making them easier to monitor over time.

So the two diagnostics serve different purposes:

- use **distributions** when you want richer detail,
- use **norms** when you want a compact trend signal.

---

## Key Takeaways

- Weight norms summarize parameter scale in a compact way.
- Balanced norms across hidden layers often indicate healthy training.
- Smooth temporal growth is usually a good sign; flat or explosive behavior is not.
- Temporal trends matter more than memorizing a single absolute norm value.

**Bridge to the next topic:** after monitoring parameters directly, the module turns to a special internal component: **BatchNorm statistics**.
