# Positions and long context

Attention is permutation-equivariant without extra structure. Models need **positional information** so token order matters.

## Absolute vs relative schemes

- **Learned absolute positions**: add a position embedding to each token (classic).
- **Relative biases**: attend with terms that depend on distance between positions.
- **Rotary (RoPE)**: rotate $Q$ and $K$ by position-dependent angles so dot products encode relative distance.

## Context length

Training context length sets the distribution the model sees. Extending at inference time (longer KV cache) may need:

- Position schemes that extrapolate (RoPE scaling, YaRN, and similar).
- Memory proportional to sequence length $\times$ layers $\times$ head dimension $\times$ batch.

## ALiBi (sketch)

Attention logits receive a linear penalty by distance instead of explicit position embeddings — one approach to length extrapolation without adding position vectors.

## Study checklist

- Draw memory vs sequence length with and without KV cache.
- Compare parameter count: MHA vs GQA vs MQA for the same hidden size.
