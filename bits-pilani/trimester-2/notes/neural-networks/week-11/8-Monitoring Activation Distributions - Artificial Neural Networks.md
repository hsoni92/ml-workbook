# Monitoring Activation Distributions - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain what activation distributions reveal about internal learning.
2. Compare activation behavior **across layers** and **across time**.
3. Interpret the fraction of zero activations in a ReLU network correctly.

---

## Why Monitor Activation Distributions?

Earlier lessons looked at specific activation failures such as dead ReLUs and saturation. This lesson moves from isolated cases to **systematic monitoring**.

The main idea is:

> activation distributions tell us how information is flowing through the network.

They help answer questions like:

- Are different layers behaving similarly or very differently?
- Are activations stable over training, or drifting toward unhealthy regimes?
- Is the network using its representational capacity well?

---

## What the Demo Tracks

The transcript uses a ReLU-based network and records activation outputs during training.

Three views are emphasized:

1. **Cross-layer comparison at the final epoch**
2. **Temporal evolution of one layer across epochs**
3. **Fraction of zero activations over time**

Together, these views make activation monitoring much more informative than a single snapshot.

---

## Healthy Cross-layer Behaviour

At the final epoch, the lesson examines box plots of activation values for different ReLU layers.

In the healthy case shown in the transcript:

- activation distributions across layers are broadly similar,
- the spread and median are comparable,
- and no layer shows severe collapse or extreme imbalance.

This suggests that activation behavior is stable across depth. In other words, no part of the network is obviously broken from the activation perspective.

---

## Healthy Temporal Behaviour

The lesson then tracks one layer's activation distribution across multiple epochs.

The important observation is not that the distribution is perfectly constant, but that it remains **stable enough**:

- no major collapse,
- no abrupt drift,
- and no obvious movement into a pathological regime.

This teaches an important diagnostic principle: internal signals should be read as **trends**, not single points.

---

## Interpreting the Fraction of Zero Activations

This is one of the most useful distinctions in the lesson.

The transcript explains that around **40 to 60 percent** zero activations can be common and even healthy in ReLU networks.

So a high fraction of zeros is **not automatically a problem**.

What matters more is the **trend**:

- a stable or slowly varying zero fraction often indicates normal ReLU sparsity,
- a gradual unbounded increase may indicate growing dead ReLUs,
- and a sharp rise suggests loss of representational capacity.

This is a very exam-ready comparison because it separates **healthy sparsity** from **pathological inactivity**.

---

## What Activation Monitoring Reveals

Activation diagnostics help catch problems that may stay hidden in the loss curve:

- structural imbalance across layers,
- gradual collapse over time,
- increasing dead ReLUs,
- or shifts in how the network is using its neurons.

This makes activations a natural companion to gradient monitoring.

---

## Key Takeaways

- Activation distributions reveal internal learning dynamics, not just final outputs.
- Healthy monitoring involves comparing layers and tracking trends across epochs.
- In ReLU networks, many zero activations can be normal; the **trend** is what matters most.
- Activation diagnostics help detect gradual failures before they become obvious externally.

**Bridge to the next topic:** after studying gradients and activations, the module moves deeper into the model and begins tracking **weight distributions during training**.
