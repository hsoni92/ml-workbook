# What Are Sequence Models? - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Define** what a **sequence model** is.
2. **Recognize** what makes data genuinely **sequential**.
3. **Identify** common **sequence-learning task types**.
4. **Explain** why flattening a sequence into one fixed vector is often inadequate.

---

## Why We Need a Separate Category of Models

In many problems, the input is not just a collection of values. It is an **ordered stream** where later interpretation depends on earlier context.

Examples:

- a **sentence** in natural language,
- an **audio waveform** over time,
- a **sensor stream** from a machine,
- a **user action history** in a recommendation system.

In all of these, the question is not just **what values occurred**, but also **in what order** and **with what context**.

---

## What Makes Data Sequential

Sequential data has three key properties:

1. **Order matters**
   If you rearrange the elements, the meaning often changes.

2. **Context accumulates over time**
   The meaning of the current element often depends on previous elements.

3. **Length can vary**
   Different examples may have different numbers of time steps or tokens.

This is why sequence data is different from standard fixed-feature tabular input.

---

## Formal Definition

A **sequence model** is a model designed to process ordered data **step by step** while maintaining some representation of **past information**.

At a high level:

```text
h0 = initial state
for t = 1 to T:
  ht = f(xt, ht-1)
output = g(h1, h2, ..., hT) or g(hT)
```

Here:

- `x_t` = current input element,
- `h_t` = internal state after processing step `t`,
- `h_t` acts as a running summary of what the model has seen so far.

The key point is that the output depends not only on the **current input**, but also on the **history**.

---

## Intuition: Why State Matters

Suppose you read the phrase:

- **"This movie was ..."**

At that point, sentiment is unclear. When the next words are:

- **"not good"**

the interpretation changes. A useful model must carry forward the effect of **"not"** so it can correctly interpret **"good"** later.

That is exactly what the evolving state is meant to capture.

---

## Common Task Forms

| Task type | Input | Output | Example |
|---|---|---|---|
| **Sequence-to-one** | Whole sequence | One label or value | Sentiment classification, activity recognition |
| **Sequence-to-sequence** | Sequence | Sequence | Translation, speech transcription |
| **Sequence labeling** | Sequence | Label at each step | Part-of-speech tagging, named entity recognition |

Although these tasks differ, they all require the model to capture **dependencies across time or position**.

---

## Why Not Just Convert the Sequence to a Fixed Vector?

A common idea is to collapse the entire sequence into one fixed-length vector and then use a standard model. This is often unsatisfactory because:

- **order information can be lost,**
- **timing relations become blurred,**
- **long-range dependencies are hard to preserve,**
- and the representation may fail to capture which earlier element matters for a later decision.

So the limitation is not only about data format. It is about losing the **temporal structure** of the problem.

---

## Important Distinction

Do not confuse these two statements:

- **"The input is a list of values."**
- **"The input is a sequence."**

A sequence is not just a list. It is an ordered object where **position and dependency structure are meaningful**.

---

## Common Misconceptions

- **Sequence means only time series.** Text, speech, biological signals, event logs, and user actions are also sequences.
- **If I add position features, an MLP is enough.** It may help, but models built for sequential dependencies usually handle the problem more naturally.
- **The hidden state remembers everything perfectly.** In practice, state is limited by model capacity and training dynamics.

---

## Exam-Ready Takeaways

- Sequence models are neural networks designed for **ordered, context-dependent, variable-length** data.
- They process data **step by step** and maintain an internal **state** summarizing previous inputs.
- Sequence tasks include **sequence-to-one**, **sequence-to-sequence**, and **sequence labeling**.
- Flattening a sequence into a fixed vector often destroys the very structure we want the model to use.

**Bridge to the next note:** now that we know what sequence models are, we can ask why ordinary **feed-forward networks** are structurally mismatched to sequence data.
