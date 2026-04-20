# Vanishing and Exploding Gradients: Layer-wise Behaviour - Artificial Neural Networks

## Learning Objective

Recognize **vanishing** and **exploding** gradients from their **layer-wise signatures**, not just from textbook definitions.

---

## Why Layer-wise Behaviour Matters

Vanishing and exploding gradients are fundamentally **depth-dependent** problems.

That means they cannot be understood well from a single global number. A network may look fine on average while some layers are receiving almost no signal and others are receiving extremely large updates.

So the correct question is not just:

> "Are the gradients small or large?"

It is:

> "How do the gradients change as we move from the output side back toward the earlier layers?"

---

## Demo Setup in This Lesson

The transcript deliberately uses a **deep network** so that gradient transport becomes visible.

Two contrasting initialization strategies are used:

- **very small weights** to demonstrate vanishing gradients,
- **very large weights** to demonstrate exploding gradients.

The diagnostic signal being tracked is the **average gradient magnitude for each layer**.

---

## Vanishing Gradients

In the vanishing case, the plot shows that gradients become dramatically smaller as we move toward the earlier layers.

### What this means

- The backward learning signal is being attenuated repeatedly.
- Earlier layers receive tiny updates.
- Those earlier layers therefore learn very slowly or may effectively stop learning.

### Why this is harmful

The earlier layers are often responsible for building the basic features used by the rest of the network. If they do not learn, later layers are forced to work with weak internal representations.

### Layer-wise signature

- later layers: visible gradient signal,
- earlier layers: much smaller gradient magnitudes,
- overall pattern: clear decay with depth.

---

## Exploding Gradients

In the exploding case, gradients become extremely large, with values rising to very high magnitudes.

### What this means

- The backward signal is being amplified instead of attenuated.
- Parameter updates become unstable.
- Training can collapse even if the code is technically correct.

### Why this is harmful

Large gradients lead to large updates. Once updates become too aggressive, optimization becomes erratic and the model may fail to converge.

### Layer-wise signature

- some layers show very large gradient magnitudes,
- values grow aggressively as we move backward,
- training becomes vulnerable to instability and collapse.

---

## Comparing the Two Failure Modes

| Pattern | Main effect | Typical layer-wise sign |
|---|---|---|
| **Vanishing gradients** | Learning signal dies out | Gradients shrink toward earlier layers |
| **Exploding gradients** | Updates become unstable | Gradients grow excessively across layers |

The important point is that both problems are best diagnosed by **tracking each layer separately**.

---

## What the Demo Teaches

This lesson is not mainly about re-deriving theory. It is about building visual intuition.

When you inspect a layer-wise gradient plot, you should immediately ask:

1. Are early layers receiving useful gradients?
2. Are gradients reasonably scaled across depth?
3. Is there evidence of sharp amplification or dramatic decay?

That habit turns gradient theory into a practical debugging skill.

---

## Practical Takeaway

Gradient problems are not abstract pathologies. They leave visible traces:

- vanishing gradients make early layers go quiet,
- exploding gradients create unstable large updates,
- and both can be detected by monitoring gradients **layer by layer**.

This is why the lesson ends by motivating better:

- initialization,
- activation choices,
- and normalization techniques.

**Bridge to the next topic:** after seeing the visual signatures of failure, the next step is to learn **how to measure gradient flow systematically during real training**.
