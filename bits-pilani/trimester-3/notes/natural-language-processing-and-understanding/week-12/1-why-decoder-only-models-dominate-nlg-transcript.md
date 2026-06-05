# Why Decoder-Only Models Dominate NLG

## The Generation Problem

Natural Language Generation (NLG) requires producing coherent, fluent text one token at a time. Not all transformer architectures are equally suited to this task. **Decoder-only** models — the architecture behind GPT, Gemini, and Llama — dominate NLG because their training objective directly matches how text is produced.

---

## Autoregressive Next-Token Prediction

Decoder-only transformers model the probability of the **next token** given all preceding tokens:

$$P(t_n \mid t_1, t_2, \ldots, t_{n-1})$$

Generation is **sequential and autoregressive**:

1. Given context, predict token $t_1$
2. Append $t_1$ to context; predict $t_2$
3. Append $t_2$; predict $t_3$
4. Continue until an end-of-sequence token or length limit

```mermaid
flowchart LR
    C[Context] --> T1[Token 1]
    C --> T1 --> T2[Token 2]
    C --> T1 --> T2 --> T3[Token 3]
    C --> T1 --> T2 --> T3 --> TN[Token N ...]
```

Each generated token becomes part of the context for the next prediction. The model learns: *given this sequence so far, what is the most likely next token?*

---

## Why This Architecture Wins for NLG

| Property | Decoder-Only | Encoder-Only (BERT) | Encoder-Decoder (T5) |
|----------|--------------|---------------------|----------------------|
| Training objective | Next-token prediction | Masked token prediction | Seq2seq (input → output) |
| Natural for text generation | Yes — same as inference | No — bidirectional, not generative | Yes, but more complex |
| Scales with data and parameters | Extremely well | Good for understanding | Good for translation/summarisation |
| Dominant in chat/completion APIs | Yes (GPT, Gemini, Llama) | No | Moderate (specialised tasks) |

The simplicity of next-token prediction scales remarkably well with model size and training data — a key reason decoder-only models power modern chatbots, code assistants, and content generators.

---

## Contrast with Encoder-Only Models

BERT-style encoder-only models use **masked language modelling** — predicting missing tokens using bidirectional context. This excels at understanding (classification, NER, embeddings) but does not naturally generate text left-to-right. Decoder-only models are trained exactly as they are used at inference time.

---

## Common Pitfalls / Exam Traps

- **Claiming BERT is used for open-ended text generation** — BERT is encoder-only; GPT-style decoder-only models dominate NLG.
- **Confusing autoregressive with parallel generation** — tokens are generated one at a time; parallelism happens only across batch items, not within a single sequence.
- **Assuming the model "plans" the full answer first** — each token is chosen based only on prior tokens; there is no lookahead.
- **Mixing up encoder-decoder and decoder-only** — T5/BART use both components; GPT/Gemini/Llama use decoder-only stacks.

---

## Quick Revision Summary

- Decoder-only transformers dominate NLG because they model next-token probability.
- Generation is autoregressive: each token is appended to context for the next prediction.
- Training objective (next-token prediction) matches inference behaviour exactly.
- This simple objective scales well with parameters and data.
- Encoder-only models (BERT) excel at understanding, not open-ended generation.
- GPT, Gemini, and Llama are decoder-only architectures.
