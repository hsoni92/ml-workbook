# The Hyperparameters That Matter - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Identify** the small set of hyperparameters that most strongly control training behavior.
2. **Explain** how these hyperparameters affect convergence, stability, capacity, and generalization.
3. **Distinguish** high-impact tuning choices from secondary configuration details.
4. **Describe** why hyperparameters must be tuned as an interacting system, not in isolation.

---

## Why This Topic Matters

Modern deep learning systems expose many tunable settings, which can make tuning feel overwhelming. But in practice, most knobs do not matter equally.

The key message of this lecture is:

**A small number of hyperparameters usually determine whether learning succeeds or fails.**

That is useful because it tells us where to focus our time. Instead of getting lost in dozens of minor options, we begin with the settings that most strongly affect training dynamics and model quality.

---

## The Four Hyperparameters That Dominate Training

According to the lecture, four hyperparameters control most of the important behavior:

1. **Learning rate**
2. **Batch size**
3. **Model capacity** (depth and width)
4. **Regularization strength**

If these are badly chosen, even a reasonable architecture or optimizer may not rescue training.

---

## What Each One Controls

| Hyperparameter | Main Question It Answers | Primary Effect on Training | Common Failure Mode |
|---|---|---|---|
| **Learning rate** | How big should each parameter update be? | Controls step size, convergence speed, and stability | Too high: divergence or oscillation; too low: slow learning |
| **Batch size** | How many samples should define one update? | Controls gradient noise and update frequency | Too small: unstable noisy updates; too large: weak exploration |
| **Model capacity** | How much complexity can the network represent? | Controls whether the model can fit the task | Too small: underfitting; too large: overfitting |
| **Regularization** | How strongly should we constrain the model? | Controls resistance to memorization | Too weak: overfitting; too strong: underfitting |

Together, these determine whether optimization is stable, whether learning progresses efficiently, and whether the final model generalizes beyond training data.

---

## Intuition: Why These Matter More Than Others

These four settings affect the training process at a very fundamental level:

- **Learning rate** decides whether updates are usable at all.
- **Batch size** changes the character of those updates: noisy or smooth.
- **Capacity** determines whether the model is powerful enough for the problem.
- **Regularization** determines whether that power is used sensibly or turns into memorization.

So while many secondary settings may refine performance, these four often decide whether the model will train properly in the first place.

---

## These Hyperparameters Interact

An important point from the transcript is that hyperparameters are **coupled**, not independent.

For example:

- A **larger learning rate** may require a **smaller batch size** or more care with stability.
- A **larger model** often needs **stronger regularization**.
- A **smaller dataset** usually calls for **less capacity** and more regularization.

This means tuning is not just about finding the "best value" for one knob. It is about balancing several forces at once.

### Short comparison

| Situation | Likely Consequence |
|---|---|
| Large model + weak regularization | Strong fit on training data, higher overfitting risk |
| Small model + strong regularization | Model may become too constrained to learn useful structure |
| Large batch + badly chosen learning rate | Stable-looking but ineffective or brittle optimization |
| Good learning rate + poor capacity choice | Optimization may work, but final model still underfits or overfits |

---

## Practical Prioritization Strategy

When compute is limited, a sensible tuning order is:

1. tune the **learning rate** first,
2. then tune **batch size** together with learning rate,
3. then revisit **model capacity**,
4. then tune **regularization strength**,
5. and only after that spend time on smaller secondary settings.

This ordering reflects leverage: some hyperparameters reshape the entire training process, while others mostly fine-tune it.

---

## What Counts as a Secondary Knob?

The lecture does not say secondary settings are useless. It says they are usually **less decisive** than the core four.

So the right mindset is:

- do **not** ignore secondary settings forever,
- but do **not** start there.

That is especially important in exams and practical work: a strong answer emphasizes the dominant factors first.

---

## Efficient Search Guidance

- Use a **coarse-to-fine** strategy: search broadly first, then refine promising regions.
- Prefer methods that spend budget on informative trials instead of exhaustive combinations.
- Judge configurations using **validation performance** and not just one lucky run.
- Remember that stable tuning depends on fair comparison conditions.

---

## Common Mistakes

- Spending most of the budget on minor settings before stabilizing learning rate.
- Treating hyperparameters as independent when they actually interact.
- Ignoring the role of dataset size when reasoning about model capacity.
- Reporting only the best run and hiding variability across trials.

---

## Summary

- Deep learning may expose many knobs, but only a few usually dominate training behavior.
- The most important ones are **learning rate, batch size, capacity, and regularization**.
- These settings should be understood as an **interacting system**, not four unrelated choices.

**Bridge to the next note:** the lecture next zooms in on the single most influential hyperparameter of all, the learning rate.
