# BatchNorm Statistics and Diagnostics - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain what BatchNorm running statistics represent.
2. Describe why those statistics are useful diagnostic signals.
3. Interpret differences in BatchNorm behavior across layers correctly.

---

## Why BatchNorm Statistics Matter

Batch normalization layers maintain internal statistics that summarize the feature distributions seen during training.

In particular, the lesson focuses on:

- **running mean**
- **running variance**

These are useful because they give visibility into how internal activations are behaving even when loss and accuracy do not reveal a problem clearly.

---

## What This Lesson Examines

The transcript inserts BatchNorm layers between linear layers and activations, then records the running means and variances during training.

The goal is not to prove that BatchNorm always fixes training. The goal is to understand what its internal statistics can tell us about the network's hidden dynamics.

---

## What the Running Statistics Tell Us

BatchNorm statistics summarize the internal feature distributions seen during training.

Monitoring them can help detect:

- unstable internal feature behavior,
- layers that may not be learning properly,
- and changes in internal distributions that would otherwise remain hidden.

This makes BatchNorm a useful diagnostic window into the model.

---

## Interpreting Differences Across Layers

One of the most important messages in this lesson is that **different BatchNorm layers are expected to have different statistics**.

The transcript explicitly warns against a common misconception:

> BatchNorm statistics do not need to converge to the same value in every layer.

Why not?

Because different layers operate at different abstraction levels and therefore naturally learn different feature scales and distributions.

So variation across layers is often **normal**, not evidence of failure.

---

## Common Misconceptions to Avoid

The lesson highlights three useful cautions:

1. **BatchNorm statistics do not need to match across layers.**
2. **Small variance is not automatically bad.**
3. **These statistics are diagnostic tools, not absolute correctness tests.**

This is important because diagnostics is about interpretation, not blind thresholding.

---

## What Healthy BatchNorm Behaviour Looks Like

In the transcript's example:

- running means and variances differ across layers,
- those differences are treated as expected,
- and the overall pattern suggests controlled internal dynamics.

So the healthy interpretation is not "all layers look identical."

It is:

> each layer shows its own statistics, but nothing suggests instability or breakdown.

---

## Why This Fits into the Bigger Module

By this point in the module, we have already inspected:

- gradients,
- activations,
- and weights.

BatchNorm adds another layer of visibility by telling us how feature distributions evolve inside normalization layers. That makes it a useful complement rather than a replacement for the earlier diagnostics.

---

## Key Takeaways

- BatchNorm running mean and variance provide a view into internal feature distributions.
- Monitoring them can reveal hidden instability that loss curves may miss.
- Different BatchNorm layers are expected to behave differently.
- These statistics should be interpreted carefully, not as one-size-fits-all correctness checks.

**Bridge to the next topic:** after examining healthy internal statistics, the module next looks for **parameter anomalies** such as frozen layers and under-trained components.
