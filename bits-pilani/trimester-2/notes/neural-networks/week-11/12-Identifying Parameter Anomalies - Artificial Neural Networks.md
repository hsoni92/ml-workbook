# Identifying Parameter Anomalies - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Use parameter-level diagnostics to identify abnormal training behavior.
2. Compare anomalous layers against a **healthy baseline**.
3. Distinguish between frozen layers, unstable growth, and under-trained components.

---

## Why Parameter Anomalies Matter

By this stage of the module, we have seen what healthy training looks like:

- gradients are stable,
- activations are reasonable,
- weight norms evolve smoothly,
- and BatchNorm statistics are controlled.

This lesson deliberately breaks that healthy picture so we can learn how abnormal parameter behavior looks in practice.

The key idea is:

> anomalies are easiest to spot when you first know what healthy behavior looks like.

---

## Step 1: Establish a Healthy Baseline

The transcript first trains a healthy model and treats its weight norm evolution as the reference.

In the healthy case:

- weight norms grow smoothly,
- no layer looks frozen,
- and no layer grows explosively.

This baseline is crucial because diagnosis is often comparative. We do not ask only "Is this pattern strange?" We ask "How is this pattern different from the healthy reference?"

---

## Anomaly 1: Frozen Layer

The first anomaly is created by intentionally freezing one layer so its parameters do not update.

### Observed signature

- one layer shows an almost flat weight norm across epochs.

### Interpretation

This indicates that the layer is not receiving effective updates.

Possible reasons mentioned in the transcript include:

- `requires_grad = False`,
- optimizer-level misconfiguration,
- or a disconnected update path.

### Exam-ready intuition

If a layer's norm stays nearly flat while other layers evolve, suspect a **frozen or disconnected layer**.

---

## Anomaly 2: Exploding Weights

The second anomaly uses a very high learning rate to induce unstable updates.

### Observed signature

- weight norms grow rapidly,
- the growth is inconsistent across layers,
- and sharp spikes appear.

### Interpretation

This pattern indicates unstable optimization and a high risk of divergence. The transcript explicitly connects this to an excessively large learning rate.

### Exam-ready intuition

Rapid, irregular norm growth is a warning sign that training pressure is too aggressive.

---

## Anomaly 3: Under-trained Output Layer

The third anomaly assigns a much smaller learning rate to the output layer.

### Observed signature

- one layer's norm grows much more slowly than the others.

### Interpretation

This suggests a layer-specific learning issue rather than a whole-network failure.

The transcript associates this with:

- insufficient learning signal,
- layer-specific learning-rate mismatch,
- and a possible bottleneck in performance.

### Exam-ready intuition

When one layer evolves much more slowly than the rest, check whether its update rule differs from the others.

---

## Why Comparison Matters

This lesson repeatedly emphasizes comparison against the healthy baseline.

That is a strong debugging principle because the same absolute norm value may be harmless in one network and suspicious in another. What matters is the **pattern**:

- flat when it should change,
- exploding when it should grow smoothly,
- or lagging when peer layers are learning normally.

---

## Key Takeaways

- Weight norms are powerful signals for parameter anomalies.
- Flat norms suggest frozen or disconnected layers.
- Rapid norm growth suggests instability.
- Much slower growth in one layer suggests under-training or configuration imbalance.
- A healthy baseline makes anomaly detection much more reliable.

**Bridge to the next topic:** after learning to detect individual pathologies, the module brings everything together into **one structured debugging workflow**.
