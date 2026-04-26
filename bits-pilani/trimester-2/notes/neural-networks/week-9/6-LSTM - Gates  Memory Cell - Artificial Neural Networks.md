# LSTM: Gates and Memory Cell - Artificial Neural Networks

## Learning Objectives

By the end of this note you should be able to:

1. **Explain** why **LSTMs** were introduced after plain RNNs.
2. **Describe** the roles of the **cell state** and **hidden state**.
3. **Interpret** the **forget**, **input**, and **output** gates.
4. **Explain** how the LSTM design helps with **long-term dependency learning**.

---

## Why LSTM Was Needed

Plain RNNs can, in principle, carry information forward through the hidden state. In practice, however, they struggle to learn long-range dependencies because gradients often vanish over long sequences.

The LSTM was introduced to provide a **more controlled form of memory**:

- one part of the architecture is responsible for **storing information**,
- and learned gates decide **what to keep, add, or expose**.

This makes memory handling much more explicit than in a basic RNN.

---

## Two States Instead of One

An LSTM maintains two related quantities at each time step:

- **Cell state `c_t`**: the long-term memory channel.
- **Hidden state `h_t`**: the current exposed representation used for output and downstream computation.

This separation is important. It means the model can **store** information without having to fully **expose** it at every step.

---

## Main Gate Equations

At time step `t`, a standard LSTM computes:

$$
\begin{aligned}
f_t &= \sigma\big(W_f [h_{t-1},\, x_t] + b_f\big) \\
i_t &= \sigma\big(W_i [h_{t-1},\, x_t] + b_i\big) \\
g_t &= \tanh\big(W_g [h_{t-1},\, x_t] + b_g\big) \\
c_t &= f_t \odot c_{t-1} + i_t \odot g_t \\
o_t &= \sigma\big(W_o [h_{t-1},\, x_t] + b_o\big) \\
h_t &= o_t \odot \tanh(c_t)
\end{aligned}
$$

You do not need to memorize every symbol immediately. What matters first is the logic behind the gates.

---

## Gate Intuition

| Gate | Main question | Intuition |
|---|---|---|
| **Forget gate** | What old information should be kept or discarded? | Prevents outdated memory from accumulating forever |
| **Input gate** | What new information should be written? | Lets relevant new evidence enter memory |
| **Output gate** | What part of memory should influence the current hidden state? | Controls how much stored information is revealed now |

Together, these gates act like learned controllers of memory flow.

---

## Why the Cell State Helps

The key design improvement is the update:

$$c_t = f_t \odot c_{t-1} + i_t \odot g_t$$

This update contains an **additive path** through the cell state. That matters because gradients can propagate through this path more easily than through a long chain of repeated nonlinear transformations.

So the LSTM does not magically remove all difficulty, but it creates a much better route for:

- preserving important information,
- and learning dependencies over longer spans.

---

## Worked Intuition

Consider the sentence:

- **"The movie was not good."**

An LSTM can:

- store the effect of **"not"** in its memory,
- carry that information forward,
- and then use it when processing **"good"**.

This is exactly the kind of situation where plain RNNs often struggle and gated memory helps.

---

## Information Flow at a Glance

```text
old cell state c_{t-1} --(forget gate)----\
                                           +--> new cell state c_t
new candidate memory ----(input gate)-----/

new cell state c_t --(output gate)--> hidden state h_t
```

This diagram highlights the central idea: **memory storage and memory usage are related, but not identical**.

---

## Important Distinction

Do not confuse:

- **cell state** with
- **hidden state**.

The **cell state** is the longer-term memory pathway.
The **hidden state** is the part currently exposed to the rest of the network.

That distinction is one of the main reasons LSTMs are more expressive than plain RNNs.

---

## Common Misconceptions

- **LSTMs remember everything forever.** No. They learn what to forget as well as what to retain.
- **The cell state is the same as the output.** No. Output is mediated through the hidden state and output gate.
- **LSTMs always outperform GRUs.** Not necessarily; performance depends on data, sequence structure, and compute budget.

---

## Exam-Ready Takeaways

- LSTMs were introduced to address the long-term dependency problem in plain RNNs.
- They separate **memory storage** (`c_t`) from **current exposed representation** (`h_t`).
- The forget, input, and output gates control memory flow in a learned way.
- The additive cell-state pathway helps gradients propagate more effectively across time.

**Bridge to the next note:** LSTM improves recurrent memory, but it is still relatively complex. The next architecture, **GRU**, keeps the gating idea while simplifying the design.
