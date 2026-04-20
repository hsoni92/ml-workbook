# Limitations of RNNs - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Identify** the main limitations of **RNN-based models**.
2. **Explain** why these limitations remain even with **LSTM** and **GRU**.
3. **Connect** those limitations to the motivation for **attention-based models**.

---

## Why This Discussion Matters

RNNs were a major breakthrough because they introduced memory into sequence modeling. LSTMs and GRUs improved them further by making memory control more effective.

But this does **not** mean recurrent models solved the sequence problem completely.

To understand why newer architectures were developed, we need to see what bottlenecks still remain.

---

## Limitation 1: Sequential Computation

An RNN processes time step `t` only after computing time step `t - 1`.

That means:

- computation is inherently **serial**,
- training on long sequences is slower,
- and the model cannot fully exploit modern hardware that prefers **parallel computation**.

This becomes a major issue at scale.

---

## Limitation 2: Long-Range Dependency Learning Is Still Hard

Even with LSTM and GRU, very long-range dependencies can remain difficult.

Why?

- information still has to travel across many time steps,
- distant context is still harder to preserve and use,
- and performance often degrades when important relationships span long intervals.

So gating improves recurrence, but it does not fully remove the burden of transporting information through time.

---

## Limitation 3: Hidden-State Bottleneck

In recurrent models, the history of the sequence is repeatedly compressed into a hidden representation.

That creates an **information bottleneck**:

```text
long history
   -> compressed into hidden state
   -> updated again and again
   -> final representation must carry what matters
```

As sequences become longer or more complex, it becomes harder for a fixed-size state to preserve all relevant details.

---

## Limitation 4: Weak Global Context Access

RNNs are better at handling nearby temporal relationships than directly linking distant parts of a sequence.

If the meaning of one element depends on something far earlier in the sequence, the information must pass through many intermediate states before it can be used.

This makes **global reasoning** harder than local sequential reasoning.

---

## Limitation 5: Training Burden

RNNs rely on **backpropagation through time**, which is computationally heavy and can be unstable on long sequences.

This leads to:

- slower training,
- more difficult optimization,
- and sensitivity to sequence length and gradient behavior.

So the limitations are not only about representation. They are also about **trainability**.

---

## Even LSTM and GRU Do Not Fully Solve These Problems

LSTM and GRU improve memory retention and help with vanishing gradients. However, they still remain:

- **sequential** in computation,
- dependent on **state compression**,
- and less effective than modern attention methods on very long or globally structured sequences.

This is why the story does not end with gated recurrence.

---

## Summary Table

| Limitation | Why it happens | Practical consequence |
|---|---|---|
| **Poor parallelization** | Each step depends on the previous step | Slow training on long sequences |
| **Long-range difficulty** | Information must travel through many steps | Distant dependencies may be missed |
| **Information bottleneck** | History compressed into finite hidden state | Relevant details can be lost |
| **Weak global access** | Distant elements are connected indirectly | Harder sequence-wide reasoning |
| **Training instability** | BPTT through long chains | Optimization becomes harder |

---

## Common Misconceptions

- **LSTM/GRU solved sequence modeling once and for all.** They were major improvements, not the final answer.
- **RNN limitations are only about hardware speed.** No. Some are also representational and optimization-related.
- **A bigger hidden state fixes everything.** More capacity helps, but it does not eliminate serial processing or the need for better retrieval of distant information.

---

## Exam-Ready Takeaways

- RNN-based models are foundational, but they have important unresolved bottlenecks.
- The biggest issues are **sequential computation**, **long-range dependency difficulty**, and the **hidden-state bottleneck**.
- LSTM and GRU reduce some problems, but they do not remove them completely.
- These remaining issues directly motivate the introduction of **attention mechanisms**.

**Bridge to the next note:** instead of forcing all past information into one evolving state, attention asks a new question: **can the model learn where to look when it needs specific information?**
