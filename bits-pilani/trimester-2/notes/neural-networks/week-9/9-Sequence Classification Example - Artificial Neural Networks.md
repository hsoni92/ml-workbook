# Sequence Classification Example - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Define** what a **sequence classification** task is.
2. **Explain** how a sequence model builds context step by step.
3. **Show** why the final prediction depends on the **whole sequence**, not isolated elements.
4. **Explain** why **LSTM** and **GRU** often outperform plain RNNs on such tasks.

---

## What Is Sequence Classification?

In sequence classification:

- the **input** is a sequence,
- but the **output** is a **single label or value**.

Examples include:

- **sentiment classification** of a sentence,
- **activity recognition** from sensor readings,
- **time-series classification** for patterns or events.

The important point is that the prediction must be based on the **entire ordered sequence**.

---

## Why This Is Not Ordinary Classification

In standard classification on fixed vectors, each feature is usually treated as part of a single static input. In sequence classification, the meaning emerges **over time** as the model reads the sequence.

So the model must decide:

- what to remember,
- what to ignore,
- and how earlier context changes the interpretation of later elements.

---

## Worked Example: Sentiment Classification

Consider the sentence:

**"The movie was not good."**

If the model treats words independently, the word **"good"** may dominate and produce a positive prediction. But the true sentiment depends on remembering the earlier negation **"not"**.

This makes sequence classification a memory problem as much as a classification problem.

---

## Step-by-Step Processing Intuition

```text
t1: "The"   -> little sentiment information
t2: "movie" -> topic context accumulates
t3: "was"   -> still mostly neutral
t4: "not"   -> critical negation cue must be retained
t5: "good"  -> interpreted using earlier context

final state -> classifier -> negative
```

The key step is not merely seeing the word **"good"**, but interpreting it in light of the earlier word **"not"**.

---

## Typical Sequence Classification Pipeline

| Stage | Role | What can go wrong |
|---|---|---|
| **Embedding / representation** | Convert tokens or signals into vectors | Weak representation quality |
| **Sequence encoder** | Accumulate context over time | Important earlier context may fade |
| **Sequence summary** | Produce one representation for the full sequence | Final summary may miss decisive information |
| **Classifier head** | Map summary to a final label | Can be confidently wrong if context is poor |

This pipeline helps you organize exam answers and practical implementations alike.

---

## Why Hidden States Matter

In an RNN-style model, the hidden state acts as a running summary of the sequence. For sequence classification, the final prediction is typically made from:

- the **final hidden state**, or
- a pooled summary of hidden states.

So the model succeeds only if the summary still contains the information most relevant to the final decision.

---

## Why LSTM and GRU Often Help

Plain RNNs may forget earlier but important signals, especially in longer sequences. LSTM and GRU improve this by using gates that help the model:

- keep useful context,
- discard irrelevant details,
- and preserve cues until they are needed later.

In the example above, gating helps ensure that **"not"** still influences the interpretation of **"good"**.

---

## Important Distinction

Do not confuse:

- **sequence classification** with
- **sequence labeling**.

In sequence classification, the entire sequence maps to **one output**.
In sequence labeling, each element in the sequence gets **its own output label**.

That difference matters for architecture design and evaluation.

---

## Common Misconceptions

- **The final token determines the class.** Often false; earlier context may reverse the meaning.
- **If the model sees all words, it understands the sentence.** Seeing is not enough; it must retain and integrate the right information.
- **Accuracy alone is enough to judge the model.** You should also inspect failure patterns, especially on negation, long-range context, or rare sequence structures.

---

## Exam-Ready Takeaways

- Sequence classification maps an **entire sequence** to a **single output**.
- The final decision depends on how well the model accumulates and preserves context over time.
- Hidden states or pooled summaries must carry the relevant information needed for the final label.
- LSTM and GRU usually improve sequence classification by retaining important cues better than plain RNNs.

**Bridge to the next note:** even with LSTM and GRU, recurrent models still have important drawbacks. That is why we next study the **limitations of RNN-based models** more broadly.
