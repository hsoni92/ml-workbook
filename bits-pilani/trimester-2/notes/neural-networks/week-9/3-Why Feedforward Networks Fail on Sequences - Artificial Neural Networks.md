# Why Feed-Forward Networks Fail on Sequences - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Recall** the core assumptions behind **feed-forward networks**.
2. **Explain** why those assumptions break for **sequence data**.
3. **Distinguish** between an **optimization problem** and an **architectural mismatch**.
4. **Motivate** why sequence models need explicit **memory and temporal computation**.

---

## The Central Mismatch

Feed-forward networks such as MLPs are designed for inputs that can be treated as:

- **fixed-size vectors**, and
- processed **independently** of surrounding context.

Sequence problems violate both assumptions. In a sequence:

- **order matters,**
- meaning changes with **context,**
- and examples often have **variable length**.

So the issue is not that feed-forward networks are "weak." The issue is that they are built for a **different problem class**.

---

## What Feed-Forward Networks Actually Do

A feed-forward network computes a mapping like:

```text
x -> layer 1 -> layer 2 -> ... -> output
```

There is **no recurrent loop**, no evolving hidden state, and no built-in memory of earlier steps.

If the same input vector appears again, the network produces the same output, regardless of what came before it.

---

## Why This Fails for Sequences

In sequential data, the current element often cannot be interpreted correctly without earlier context.

Example:

- **"good"** usually suggests positive sentiment.
- In **"not good"**, the earlier word **"not"** changes the meaning.

A plain feed-forward model has no natural mechanism to carry the effect of **"not"** forward in time unless we manually encode that context into the input representation.

That is the core failure: **no memory, no temporal dependency modeling**.

---

## Structural Limits of Feed-Forward Models on Sequences

- **No built-in memory** of earlier inputs.
- **No temporal recursion** from one step to the next.
- **No native handling of variable-length inputs** without external tricks.
- **Dependence on feature engineering** if context must be manually inserted.

This makes feed-forward models awkward for tasks where information unfolds over time.

---

## Why Better Training Does Not Solve It

This point is important:

**The limitation is structural, not just due to bad optimization.**

More epochs, more data, or better hyperparameters cannot magically create temporal memory in an architecture that does not contain it. If the model class lacks stateful transitions, it cannot naturally represent sequence dynamics.

---

## Feed-Forward vs Sequence Models

| Property | Feed-forward network | Sequence model |
|---|---|---|
| **Input view** | Fixed vector | Ordered stream of elements |
| **Memory of past** | None | Internal state or attention-based retrieval |
| **Variable-length support** | Indirect | Natural |
| **Context sensitivity** | Must be engineered | Built into the architecture |
| **Long-range dependency modeling** | Weak | Designed for it |

---

## A Useful Distinction

Do not confuse:

- **"The model can classify a vector well"**
- with
- **"The model can model a sequence naturally."**

A feed-forward network may work if you carefully hand-design features or use fixed windows, but that is very different from having an architecture whose computation itself is **history-aware**.

---

## Common Misconceptions

- **Adding more dense layers gives memory.** More depth adds representational power, but not temporal state.
- **A sliding window solves sequence modeling.** It only gives local context and can miss dependencies outside the window.
- **If results are poor, hyperparameters are the main issue.** Often the deeper problem is that the architecture does not match the data structure.

---

## Exam-Ready Takeaways

- Feed-forward networks assume **independent, fixed-size inputs**.
- Sequence data violates that assumption because **order and context matter**.
- The main limitation is **architectural**, not merely a training issue.
- Sequence models are introduced because they provide explicit **memory and temporal computation**.

**Bridge to the next note:** the first major architecture designed to fix this gap is the **recurrent neural network (RNN)**, which carries information forward through a hidden state.
