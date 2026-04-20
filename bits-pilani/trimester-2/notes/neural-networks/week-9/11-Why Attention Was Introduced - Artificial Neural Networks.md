# Why Attention Was Introduced - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Explain** the main motivation for introducing **attention mechanisms**.
2. **Describe** the high-level idea of attention as **selective focus**.
3. **Contrast** the recurrent view of memory with the attention-based view.
4. **Explain** why attention improves long-range and global dependency modeling.

---

## The Core Motivation

RNN-based models try to compress the past into an evolving hidden state. That works to some extent, but it creates two major problems:

- distant information is harder to preserve,
- and even when preserved, it may be hard to retrieve precisely when needed.

This leads to a powerful question:

**Instead of trying to remember everything in one moving summary, can the model directly look back at the relevant parts of the sequence?**

That question is the motivation for attention.

---

## Human Intuition

When people read a long sentence, they do not rely only on a compressed mental summary of everything they read earlier. They often mentally return to the most relevant part.

Example idea from the transcript:

- while reading the end of a long sentence,
- you may mentally revisit an earlier phrase such as **"the book"**
- because that earlier phrase is crucial for interpreting the current part correctly.

Attention brings this intuition into neural networks: **different earlier elements are not equally relevant at every moment**.

---

## High-Level Idea of Attention

Attention lets the model assign different importance weights to different parts of the sequence.

At a high level:

```text
query = what the model currently needs
keys  = what each position offers
values = the information stored at each position

query + keys
   -> similarity scores
   -> normalized attention weights
   -> weighted combination of values
```

The result is a **context vector** focused on the most relevant parts of the sequence.

---

## The Conceptual Shift

This is the key shift:

```text
RNN view: compress the past into memory
Attention view: keep representations and retrieve selectively when needed
```

So attention is not just a small improvement. It is a different way of thinking about sequence reasoning.

---

## Why Attention Helps

| Limitation of recurrent models | What attention changes | Benefit |
|---|---|---|
| Distant information is reached only indirectly | Relevant positions can be accessed directly | Better long-range dependency handling |
| History is compressed into one hidden state | Context is built dynamically from many positions | Reduced information bottleneck |
| Global context is hard to use | All positions can influence one another more flexibly | Better sequence-wide reasoning |

This is why attention made such a big impact.

---

## A Simple Example

Suppose a model is interpreting the last word of a long sentence. Under recurrence alone, the relevant earlier detail must survive through many hidden-state transitions.

With attention, the model can assign high weight directly to the earlier word or phrase that matters most for the current decision.

So the model learns **where to look**, not just **what to store**.

---

## What Attention Does Not Mean

Attention does **not** mean:

- no memory,
- no structure,
- or equal importance for all tokens.

Instead, it means memory access becomes **dynamic and context-dependent**.

---

## Common Misconceptions

- **Attention means the model no longer needs memory.** It still uses internal representations; attention changes how relevant information is accessed.
- **Attention is only useful for machine translation.** It is now central across NLP, speech, vision, and multimodal systems.
- **All tokens are weighted equally.** No. The weights depend on the current context and are learned.

---

## Exam-Ready Takeaways

- Attention was introduced to overcome the **retrieval and bottleneck limitations** of recurrent sequence models.
- It lets the model assign **context-dependent importance weights** to different positions in the sequence.
- The main conceptual change is moving from **compressed memory** to **selective retrieval**.
- This idea becomes the foundation of **transformer architectures**.

**Bridge to the next note:** transformers take this idea further by making **attention the central building block** of the entire sequence model.
