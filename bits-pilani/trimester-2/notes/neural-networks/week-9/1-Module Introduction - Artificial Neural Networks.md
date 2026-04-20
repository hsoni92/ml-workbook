# Neural Networks - Module 9 Introduction: Artificial Neural Networks

## Learning Objectives

By the end of this module you should be able to:

1. **Explain** why sequence data needs models that account for **order, context, and history**.
2. **Describe** how **RNNs** process data over time using a recurrent hidden state.
3. **Explain** why plain RNNs struggle with **long-term dependencies**.
4. **Compare** **LSTM** and **GRU** as gated solutions to recurrent memory problems.
5. **Motivate** why **attention** and **transformers** became the dominant modern sequence models.

---

## Why This Module Matters

Earlier modules mainly dealt with settings where inputs can be treated as fixed vectors. Sequence data is different. In **text, speech, time series, clickstreams, and sensor logs**, the **order itself carries meaning**.

A simple example makes this obvious:

- **"dog bites man"**
- **"man bites dog"**

The same words appear in both cases, but the meaning changes because the **ordering changes**. That is the central reason this module exists: in sequence problems, understanding one element in isolation is usually **not enough**.

---

## From Independent Inputs to Sequence Modeling

Feed-forward networks such as MLPs process inputs **independently**. They have no built-in notion of:

- what came **before**,
- what should be **remembered**,
- or how earlier context should change the meaning of later inputs.

Sequence models introduce exactly this missing ingredient: a **state or memory** that evolves as the sequence unfolds.

---

## Storyline of Module 9

This module follows a clear progression:

```text
Feed-forward limitation on ordered data
        ->
Recurrent neural networks (RNNs)
        ->
Training difficulty: vanishing gradients
        ->
Gated recurrence: LSTM and GRU
        ->
Remaining recurrent bottlenecks
        ->
Attention mechanisms
        ->
Transformers
```

The logic is important for exams: each new architecture is introduced as a response to a **specific limitation** in the previous one.

---

## Big-Picture Comparison

| Architecture family | Main idea | Strength | Main limitation |
|---|---|---|---|
| **Feed-forward models** | Map fixed input to output | Simple and effective on static data | No temporal memory |
| **RNNs** | Carry a hidden state across time | Natural sequence processing | Weak long-range learning |
| **LSTM / GRU** | Use gates to control memory updates | Better retention of important context | Still sequential and harder to scale |
| **Attention / Transformers** | Retrieve relevant information directly | Strong long-range modeling and parallelism | Higher compute and memory cost |

---

## What This Module Will Teach You to Notice

When studying any sequence model, ask:

1. **How is past information stored?**
2. **How is relevant past information retrieved?**
3. **What breaks when sequences become long?**
4. **What architectural change is introduced to fix that problem?**

These questions tie the whole module together.

---

## Common Misconceptions

- **Sequence modeling is only for NLP.** It is also crucial in forecasting, activity recognition, biosignals, recommender systems, and control.
- **LSTM and GRU completely solve long-context learning.** They improve it substantially, but they do not remove sequential computation or all memory bottlenecks.
- **Transformers are always the best choice.** They are dominant at scale, but recurrent models can still be useful when data, latency, or compute is limited.

---

## Module Framing

This week is really about one core question:

**How should a neural network represent history?**

- Plain RNNs answer: **compress the past into a hidden state**.
- LSTM/GRU answer: **control memory with gates**.
- Attention answers: **do not only remember; retrieve what you need when you need it**.

---

## Exam-Ready Takeaways

- Sequence data differs from static data because **order and accumulated context matter**.
- Feed-forward models fail naturally on sequences because they lack **memory**.
- The path from **RNN -> LSTM/GRU -> Attention -> Transformer** is a path of solving increasingly important sequence-modeling bottlenecks.
- In long answers, always connect **architecture -> limitation -> next idea**.

**Bridge to the next note:** before studying RNNs, we first need a clear definition of **what sequence models are** and what makes data genuinely sequential.
