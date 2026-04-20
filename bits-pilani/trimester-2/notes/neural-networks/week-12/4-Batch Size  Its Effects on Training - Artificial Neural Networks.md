# Batch Size: Its Effects on Training - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Explain** what batch size controls during training.
2. **Describe** how batch size changes gradient noise, stability, and optimization behavior.
3. **Compare** small, medium, large, and full-batch regimes.
4. **Explain** why batch size must be studied with a controlled experiment and tuned together with learning rate.

---

## What Batch Size Actually Changes

Batch size is the number of training samples used to compute one gradient update.

This changes the character of optimization:

- **Small batch** -> noisy but frequent updates
- **Large batch** -> smoother and less noisy updates
- **Full batch** -> nearly deterministic updates using the whole dataset

The most important conceptual point is:

**Batch size does not change the objective function. It changes the path taken through the loss landscape.**

That distinction is easy to miss, but it is central.

---

## Intuition: Noise vs Stability

Smaller batches use less data to estimate the gradient, so each update contains more randomness. Larger batches average over more examples, so the update direction becomes smoother.

This creates a classic trade-off:

- more noise can help the optimizer **explore**,
- less noise can make descent more **stable**.

So a noisier curve is not automatically bad, and a smoother curve is not automatically better.

---

## Controlled Experiment Setup

The lecture explicitly studies batch size using a controlled experiment. To do that properly, keep fixed:

- the dataset and split,
- the model architecture,
- the optimizer,
- the learning rate,
- and the training duration.

Then vary only batch size, for example:

`16 -> 64 -> 256 -> full batch`

This is the only way to attribute differences to batch size rather than to some other changing factor.

---

## Observed Batch-Size Regimes

The transcript compares small, medium, large, and full-batch training and tracks both training loss and gradient norms.

| Batch Size | Loss Curve Pattern | Gradient Variability | Typical Interpretation |
|---|---|---|---|
| Small | Noisy | High | More stochastic exploration, less stable |
| Medium | Moderately smooth | Moderate | Good balance between noise and stability |
| Large | Smooth | Low | Stable optimization, less stochasticity |
| Full batch | Smoothest | Very low | Nearly deterministic updates, less frequent parameter changes |

The lecture also highlights that **full-batch training is smooth but updates are less frequent**, which is an important practical distinction.

---

## Why Gradient Noise Matters

The demo measures not only loss but also **gradient norm variability**. That is useful because it makes the role of batch size visible:

- **small batches** produce high variation in gradient magnitude,
- **large batches** produce smoother gradient behavior,
- **full batch** is almost deterministic.

This helps explain why small-batch training can sometimes escape sharp regions more easily, while large-batch training can appear calmer but may settle differently.

---

## Stability-Exploration Trade-off

You can summarize the effect of batch size as:

`decrease batch size -> more gradient noise -> more exploration, less stability`

`increase batch size -> less gradient noise -> more stability, less exploration`

This is the main exam-ready intuition behind batch size.

---

## Why Batch Size and Learning Rate Must Be Tuned Together

The lecture repeatedly connects batch size with learning rate. That is because both shape update behavior:

- batch size affects how noisy the gradient estimate is,
- learning rate affects how large the update step is.

Together, they determine whether updates are:

- stable,
- erratic,
- slow,
- or aggressively overshooting.

| Batch-Size Change | Typical Implication for Learning Rate |
|---|---|
| Increase batch size | May allow a larger learning rate or a different effective update scale |
| Decrease batch size | May require more care because noisy gradients and large steps can combine badly |

So it is not enough to ask, "What is the best batch size?" The better question is, "What batch size works well with this learning rate and model?"

---

## Practical Decision Factors

In real systems, batch size is not chosen only for theory. It is also constrained by:

- available memory,
- hardware throughput,
- training time per update,
- and overall stability of optimization.

So the best batch size is usually a compromise between **optimization behavior** and **compute reality**.

---

## Common Mistakes

- Changing batch size and learning rate together without a controlled comparison.
- Assuming smoother loss always means better generalization.
- Ignoring the role of gradient noise in shaping optimization behavior.
- Treating batch size as only a hardware decision and not a learning decision.

---

## Summary

- Batch size controls **how many samples define one update**.
- Its main effect is on **gradient noise**, which creates a trade-off between **exploration** and **stability**.
- Proper conclusions about batch size require controlled experiments and should always consider its interaction with learning rate.

**Bridge to the next note:** once we understand the main hyperparameters, the next step is to run a full hyperparameter tuning experiment in a systematic way.
