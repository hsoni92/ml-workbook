# Weight Distribution Drift - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why monitoring **weight distributions** gives insight beyond loss curves.
2. Describe what **stable** weight behavior looks like across layers and across time.
3. Interpret weight drift as a parameter-level diagnostic signal.

---

## Why Look at Weights?

After gradients and activations, this lesson moves one level deeper into the model: the parameters themselves.

The key motivation is simple:

> if learning is happening, the parameters should change in a meaningful and controlled way.

Weight distributions help answer questions such as:

- Are all layers learning in a balanced way?
- Are some layers effectively untrained?
- Are weights growing in a stable way or drifting toward instability?

These issues may not be obvious from the loss alone.

---

## What the Lesson Examines

The transcript uses a moderately deep feed-forward network and trains it with a stable configuration so that we can first understand **healthy behavior**.

Two views are emphasized:

1. **Weight distributions across layers at the final epoch**
2. **Weight distribution evolution of a layer across time**

This mirrors the same diagnostic logic used earlier for gradients and activations.

---

## Healthy Weight Distributions Across Layers

At the final epoch, the plot shows:

- similar weight distributions across layers,
- no extreme spread,
- no obvious collapse,
- and no single layer dominating in magnitude.

### Interpretation

This suggests that learning is **balanced across the network**.

If one layer had drastically larger or smaller weights than the rest, that could indicate that optimization pressure is uneven or that some part of the model is behaving abnormally.

---

## Healthy Weight Evolution Over Time

The transcript then tracks how one layer's weight distribution changes over multiple epochs.

In the healthy run:

- the distribution remains largely stable,
- changes are gradual rather than abrupt,
- and there is no runaway growth or collapse.

### Why this matters

Learning should change parameters, but it should do so in a **controlled** way. Weight drift is expected during training. The issue is not drift itself, but **unstable drift**.

So a good mental model is:

- **some movement** is healthy,
- **wild movement** is suspicious,
- **no movement at all** may mean under-training or a frozen component.

---

## Why Weight Diagnostics Complement Other Signals

Gradient diagnostics tell us whether learning signals are flowing.

Activation diagnostics tell us whether neurons are responding meaningfully.

Weight diagnostics tell us whether those signals are producing **actual parameter change**.

So weights give a useful parameter-level confirmation of what the training process is doing internally.

---

## Practical Interpretation

When monitoring weight distributions, ask:

1. Do the layers show broadly balanced parameter scales?
2. Are the distributions stable over time?
3. Is any layer collapsing, exploding, or staying oddly unchanged?

If the answers look healthy, optimization is likely well behaved.

If not, the weight distributions can expose silent instability before the final performance metrics become obviously bad.

---

## Key Takeaways

- Weight distributions provide visibility into how learning accumulates inside the model.
- Stable distributions across layers suggest balanced learning.
- Stable evolution over time suggests controlled optimization.
- Monitoring weights helps catch silent problems that loss curves alone may miss.

**Bridge to the next topic:** weight distributions show the full parameter picture. The next lesson compresses that picture into a simpler signal: **weight norms**.
