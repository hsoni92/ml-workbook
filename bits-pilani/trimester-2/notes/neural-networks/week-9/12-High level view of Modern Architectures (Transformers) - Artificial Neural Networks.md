# High-Level View of Modern Architectures (Transformers) - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Define** what a **transformer** is at a high level.
2. **Explain** how transformers differ conceptually from **recurrent models**.
3. **State** why transformers became dominant in modern sequence modeling.
4. **Recognize** the main trade-offs and misconceptions around transformers.

---

## Where Transformers Fit in the Story

This module moved through a clear sequence:

1. Sequence data needs memory and context.
2. RNNs introduced recurrent hidden state.
3. LSTM and GRU improved recurrent memory.
4. Attention changed sequence modeling from **memory compression** to **selective retrieval**.

Transformers are the next step in that progression:

**they build sequence models around attention rather than recurrence.**

---

## High-Level Definition

A **transformer** is a sequence model whose core operation is **self-attention**.

Unlike RNNs:

- it does **not** process tokens strictly one by one through recurrence,
- and it does **not** rely on a single hidden state carrying history forward step by step.

Instead, it lets different positions in the sequence interact more directly.

---

## High-Level Transformer Pipeline

```text
Token embeddings + positional information
              ->
Self-attention
              ->
Feed-forward sublayers
              ->
Repeated transformer blocks
              ->
Task-specific output head
```

This note stays intentionally high-level. The goal here is conceptual understanding, not detailed transformer mechanics.

---

## Why Positional Information Is Needed

Because transformers do not use recurrence, they need some explicit way to know the position or ordering of sequence elements.

That is why **positional information** is added to token representations.

So:

- **attention** tells the model which elements relate to each other,
- **positional information** tells the model where those elements occur in the sequence.

---

## The Key Conceptual Shift

| Recurrent models | Transformers |
|---|---|
| Process sequence step by step | Process sequence more globally |
| Carry information through hidden state | Use attention to relate positions directly |
| Access distant information indirectly | Access distant information more directly |

This is one of the most important conceptual transitions in modern deep learning.

---

## Why Transformers Became Dominant

Transformers became central because they offer several major advantages:

1. **Better parallelism**
   Tokens can be processed much more efficiently on modern hardware than in strict recurrent pipelines.

2. **Direct long-range interaction**
   Distant elements can relate through attention without passing through many recurrent steps.

3. **Strong scaling behavior**
   Transformers have shown excellent performance as model size and dataset size increase.

4. **Broad applicability**
   They are now used not only in NLP, but also in speech, vision, multimodal learning, and time-series settings.

---

## Recurrent Models vs Transformers

| Property | RNN-based models | Transformers |
|---|---|---|
| **Computation style** | Sequential | More parallel |
| **Long-range dependency modeling** | Indirect through recurrence | Direct through self-attention |
| **Hidden-state bottleneck** | Stronger | Reduced |
| **Scalability on modern hardware** | Limited | Strong |

This table captures why transformers replaced recurrence in many large-scale applications.

---

## Trade-Offs and Constraints

Transformers are not perfect. Important limitations include:

- **self-attention can be expensive** for very long sequences,
- **large models need substantial data and compute,**
- and long-context efficiency may require specialized variants.

So transformers became dominant because they solved key recurrent bottlenecks, not because they have no drawbacks.

---

## Common Misconceptions

- **Transformers have no notion of order.** False. Positional information is explicitly injected.
- **Transformers are only for NLP.** False. They are widely used across many domains.
- **Attention alone guarantees good performance.** False. Data quality, optimization, scale, and evaluation still matter.

---

## Module Wrap-Up

Week 9 can be summarized as one architectural journey:

```text
Need to model ordered context
   -> RNN
   -> vanishing-gradient problem
   -> LSTM / GRU
   -> remaining recurrent bottlenecks
   -> attention
   -> transformers
```

This is the exam-ready narrative of the entire module.

---

## Exam-Ready Takeaways

- Transformers are modern sequence models built primarily around **attention** rather than **recurrence**.
- Their main advantages are **parallel computation**, **direct long-range interaction**, and strong **scaling**.
- They still need **positional information** because order is not provided by recurrence.
- They became dominant because they address key limitations of recurrent architectures at scale.
