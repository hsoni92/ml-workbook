# Transformers I: Attention and Architecture

## Why Drop Recurrence

An RNN processes tokens strictly in order. Information has to survive a chain of hidden states, training cannot fill the GPU because steps wait on each other, and vanishing gradients make a deep RNN unreliable.

The Transformer (Vaswani et al., 2017) removes recurrence. Every token attends to every other token in one step. The path length between any pair of tokens is constant, however far apart they are.

Attention uses three projections of the same input:

- **Query** asks for something.
- **Key** is the label that gets matched.
- **Value** is the content that gets mixed.

The rest of the block is multi-head attention plus a positional signal, and the whole layer runs in parallel. That design is what BERT (2018), GPT-2 and GPT-3, and the Vision Transformer (2020) are built on. Parallelism is also why training scales with data and compute.

## Self-Attention

Think of a library. The query is the search, the key is the title used for matching, and the value is the book you actually take.

With learned matrices:

$Q = X W_Q,\quad K = X W_K,\quad V = X W_V$

Scores are dot products of queries and keys, divided by $\sqrt{d_k}$ so the softmax does not saturate. Softmax turns the scores into weights, and the output is the weighted sum of values:

$\text{Attention}(Q, K, V) = \text{softmax}(Q K^{T} / \sqrt{d_k}) \, V$

The scaling keeps the softmax out of the flat region where gradients vanish.

### Several heads, and a causal mask

One head can represent only one kind of association, and the softmax can concentrate on a single token. $h$ heads, each with its own weights, pick up different relations: syntax, coreference, semantics.

$\text{head}_i = \text{Attention}(X W_i^{Q},\; X W_i^{K},\; X W_i^{V})$

Head outputs are concatenated to width $h \cdot d_v$ and projected with $W_O$ back to $d_{\text{model}}$.

A **causal mask** sets future positions to $-\infty$ before the softmax, so those positions get weight $0$. A decoder-only model such as GPT then cannot read tokens it has not generated yet.

The same Q-K-V block is used in BERT, GPT, and T5, in Vision Transformers over image patches, in AlphaFold2, and as cross-attention in CLIP and Flamingo.

## Positional Encoding

Self-attention has no order. Without a position signal, "dog chased cat" and "cat chased dog" look the same.

Each token embedding is added to a position vector of the same size. The original encoding is sinusoidal: high-frequency dimensions change quickly and mark local position, low-frequency dimensions change slowly and mark global position. It adds no parameters, extends past the lengths seen in training, and nearby positions have similar vectors, so relative distance is available to the model.

| Encoding | Property |
| --- | --- |
| Fixed sinusoids | Deterministic, zero parameters, generalizes to longer sequences. |
| Learned position embeddings | Fit the training data, but they stop at the maximum length they were trained on. |
| RoPE, ALiBi, YaRN | Later schemes used to extend Transformers to long context. |

Choose by the trade-off you need: a learned embedding is flexible inside its training length, a fixed or relative scheme survives longer inputs.

## The Encoder Block

An encoder stack of $N$ identical layers builds a contextual vector for every token, all tokens at once. Each layer contains:

1. **Multi-head self-attention**, $\text{softmax}(Q K^{T} / \sqrt{d_k}) \, V$, with several heads.
2. A **residual** around the sublayer, $\text{Output} = \text{Sublayer}(x) + x$, so the gradient has a path that does not pass through the sublayer.
3. **Layer normalization** over each token's activations. Pre-norm (normalize, then the sublayer) is the more stable order in deep models.
4. A **position-wise feed-forward network** that expands the width by $4\times$ and applies ReLU or GELU, independently at each token.

Sinusoidal positions are added to the embeddings before the stack. Dropout with $p = 0.1$ is applied after attention, after the feed-forward network, and on the embeddings. Stacking layers is what produces the hierarchy used by BERT, ViT, and ESM-2.

## The Decoder Block

Generation is autoregressive: one token at a time, each output fed back in, until an end-of-sequence token.

Each decoder layer has three sublayers:

1. **Masked self-attention.** Future scores are set to $-\infty$, so token $i$ only sees positions $0$ through $i$.
2. **Cross-attention.** Decoder states are the queries. Encoder outputs are the keys and values.
3. **Feed-forward network.** Expand to $d_{\text{ff}}$, apply ReLU or SwiGLU, project back to $d_{\text{model}}$.

Residuals and layer norm wrap each sublayer. Post-norm applies the norm after the add. Pre-norm applies it before the sublayer and is what stabilizes deep stacks such as GPT-3 and LLaMA. The final projection is a distribution over the vocabulary.

## The Full Model and the Training Objective

The architecture is positional encoding, multi-head attention, residuals with layer norm, and a position-wise feed-forward network.

- The **encoder** is $N$ layers of self-attention then a feed-forward network. It builds a representation of the source.
- The **decoder** is masked self-attention, then cross-attention into the encoder, then a feed-forward network. It emits the target one token at a time.

Training uses cross-entropy against the true next token. Causal masking makes training match inference: the model may use only earlier context. Performance follows scaling laws in data, parameter count, and compute. The same Q-K-V attention implements self-attention, masked self-attention, and cross-attention. Only the mask and the source of $K$ and $V$ change.

---

**← [Previous](../week-04/02-cnn-architectures-yolo-and-u-net-roadmap-makeup-transcript.md) · [Index](../README.md) · [Next](01-transformers-part-1-architecture-attention-and-code-transcript.md) →**
