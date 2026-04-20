# RNN Architecture and Recurrent Computation - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Describe** the basic structure of a **recurrent neural network (RNN)**.
2. **Explain** how recurrent computation works across time steps.
3. **Interpret** the hidden state as a compact summary of past context.
4. **Explain** what **unrolling** means and why it is useful.

---

## Why RNNs Were Introduced

Feed-forward networks process each input independently. Sequence tasks need something more: a way to let the current computation depend on **what came before**.

RNNs introduce this by carrying forward a **hidden state** from one time step to the next. This hidden state acts as a running memory of the sequence so far.

---

## Core Computation of an RNN

At time step `t`, the model receives:

- the current input `x_t`,
- and the previous hidden state `h_{t-1}`.

It then computes:

```text
h_t = phi(W_x x_t + W_h h_{t-1} + b)
y_t = W_y h_t
```

where:

- `h_t` = updated hidden state,
- `phi` = nonlinearity such as `tanh`,
- `y_t` = output at that step, if the task requires per-step outputs.

The key idea is simple: **the next state depends on both the present input and the past summary**.

---

## Intuition: What the Hidden State Represents

The hidden state is not a perfect memory. It is a **compressed summary** of the important information seen so far.

So as the sequence progresses:

- earlier inputs influence `h_1`, `h_2`, `h_3`, ...
- later states indirectly carry information about earlier ones,
- and the model tries to use this evolving summary to make decisions.

This is what allows an RNN to model context over time.

---

## Why Parameter Sharing Matters

An important design choice is that the **same weights** are used at every time step.

This gives three major benefits:

| Benefit | Why it matters |
|---|---|
| **Parameter efficiency** | We do not need a separate model for each position in the sequence. |
| **Variable-length handling** | The same recurrent rule can be applied to short or long sequences. |
| **Temporal consistency** | Similar patterns can be recognized regardless of where they appear in the sequence. |

So an RNN is not a chain of different networks. It is **one recurrent cell reused over time**.

---

## Unrolling: A Visualization Tool

To understand recurrent computation, we often draw the RNN as if it were expanded over time:

```text
x1 -> [RNN cell] -> h1 -> y1
          |
x2 -> [RNN cell] -> h2 -> y2
          |
x3 -> [RNN cell] -> h3 -> y3
          |
... same parameters reused at every step ...
```

This is called **unrolling**.

Unrolling does **not** mean the model has separate parameters at each step. It simply makes the temporal flow visible so we can reason about:

- how information moves forward through the sequence,
- and how gradients move backward during training.

---

## Output Patterns

Different tasks use RNN outputs differently:

- **Sequence-to-sequence:** produce `y_t` at every step.
- **Sequence-to-one:** use the final hidden state `h_T` for a single final prediction.

This flexibility is one reason RNNs became a foundational sequence architecture.

---

## Limitations Already Visible

Even before discussing training, you should notice an important issue:

- the hidden state must compress past information,
- so distant details may get diluted,
- and long sequences make this compression increasingly difficult.

This observation prepares us for the next major topic: **why gradients become hard to propagate through long recurrent chains**.

---

## Common Misconceptions

- **RNNs see the whole sequence at once.** No. They process one step at a time.
- **Unrolling creates different networks.** No. The same parameters are reused throughout.
- **The final hidden state always contains everything important.** Not necessarily; early information may weaken or disappear.

---

## Exam-Ready Takeaways

- An RNN introduces **recurrence**, allowing the model to carry a hidden state across time.
- Each update uses both the **current input** and the **previous hidden state**.
- The hidden state is a **compressed memory**, not a perfect record.
- **Unrolling** is a visualization that makes temporal information flow and gradient flow explicit.

**Bridge to the next note:** once we unroll an RNN across many time steps, we can also see why training it becomes difficult, leading to the **vanishing gradient problem**.
