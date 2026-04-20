# Vanishing Gradient Problem in RNNs - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Explain** how RNNs are trained using **backpropagation through time (BPTT)**.
2. **Describe** why gradients can shrink across many recurrent steps.
3. **Relate** vanishing gradients to failure on **long-term dependencies**.
4. **Distinguish** vanishing gradients from **exploding gradients**.

---

## Why Training RNNs Is Harder Than It Looks

When an RNN is trained, errors from later time steps must be propagated backward to earlier ones. Because the same recurrent computation is repeated many times, the network behaves like a **deep model in time**.

This means the learning signal must travel through many sequential transformations, which creates the risk of gradient decay.

---

## Backpropagation Through Time

RNNs are trained using **backpropagation through time (BPTT)**.

The idea is:

1. **Unroll** the RNN across the full sequence.
2. Compute the loss.
3. Propagate gradients backward through each recurrent step.

So the gradient for an earlier hidden state depends on a chain of repeated multiplications:

```text
dL/dh_k = (dL/dh_T) * product of recurrent Jacobians from k+1 to T
```

If those repeated factors are often smaller than 1 in magnitude, the product shrinks rapidly toward 0.

---

## Core Intuition

The intuition is simple:

- multiply by a number less than 1 once -> it gets smaller,
- multiply by similar numbers many times -> it becomes tiny.

That is exactly what can happen to gradients in long recurrent chains.

Activation functions such as `sigmoid` or `tanh` can worsen this because their derivatives are often small, especially in saturated regions.

---

## What Vanishing Gradients Mean in Practice

If the gradient reaching early time steps is extremely small, then those earlier states receive almost **no useful learning signal**.

Practical result:

- the model learns mostly from **recent inputs**,
- important information from far earlier steps is not used effectively,
- and plain RNNs struggle to learn **long-term dependencies**.

So the model may appear to have memory, but during training it cannot easily learn how to use that memory over long spans.

---

## Why This Is a Structural Problem

It is important not to trivialize this issue.

Vanishing gradients are **not primarily caused by**:

- too little data,
- poor hyperparameters,
- or insufficient training time.

They arise from the **repeated temporal structure** of the RNN itself. As the sequence gets longer, the effective depth grows, and the optimization problem becomes much harder.

---

## Vanishing vs Exploding Gradients

| Problem | What happens mathematically | What you observe |
|---|---|---|
| **Vanishing gradient** | Repeated factors smaller than 1 shrink the gradient | Slow learning of distant dependencies |
| **Exploding gradient** | Repeated factors larger than 1 amplify the gradient | Unstable updates, loss spikes, numerical issues |

Both come from repeated multiplication through time, but their effects are opposite.

---

## Forward and Backward View

```text
Forward:   x1 -> h1 -> h2 -> ... -> hT -> loss
Backward:  loss -> ... -> h2 -> h1

The longer the path, the harder it is to preserve a useful gradient signal.
```

This is why unrolling is not just a drawing trick. It reveals the training difficulty clearly.

---

## Why This Topic Matters

The vanishing gradient problem explains why a plain RNN often fails even when the idea of recurrent memory seems correct. The architecture can, in principle, carry information forward, but training cannot easily assign credit to events far back in the sequence.

That gap between **theoretical memory** and **trainable memory** is what motivates gated architectures.

---

## Common Misconceptions

- **More epochs will fix vanishing gradients.** If the gradient is near zero, repeated training still provides almost no update.
- **Only the activation function is to blame.** Activation choice matters, but the deeper issue is repeated recurrence over time.
- **LSTMs and GRUs eliminate all gradient problems.** They greatly improve the situation, but do not remove every training difficulty.

---

## Exam-Ready Takeaways

- RNNs are trained with **BPTT**, which propagates gradients backward through many time steps.
- Repeated multiplication by small derivatives causes gradients to **shrink exponentially**.
- Earlier time steps then receive weak learning signal, making long-term dependency learning difficult.
- This is a **structural optimization problem** that motivates **LSTM** and **GRU**.

**Bridge to the next note:** to reduce this problem, sequence models were redesigned with explicit memory control, leading to the **Long Short-Term Memory (LSTM)** architecture.
