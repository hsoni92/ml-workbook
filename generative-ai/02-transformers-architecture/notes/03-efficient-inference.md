# Efficient inference

Training and serving transformers stress memory bandwidth. Production systems lean on caching, grouped heads, and kernel fusion.

## KV cache

During autoregressive decoding, past token keys and values are fixed. Store them in a **KV cache** and only compute $Q, K, V$ for the new token. Memory grows with:

$$\text{cache size} \propto 2 \times L \times h_{\text{kv}} \times d_{\text{head}} \times \text{seq\_len}$$

($L$ layers, $h_{\text{kv}}$ KV heads after grouping.)

## Grouped-query attention (GQA)

Use fewer key/value heads than query heads; repeat or share $K/V$ across query groups. Cuts cache size with modest quality impact — common in modern open models.

## FlashAttention (idea)

Fuse softmax and matmuls in tiled GPU kernels to reduce HBM round-trips. You rarely implement this yourself; frameworks and runtimes expose it when shapes and hardware align.

## Mixture of experts (MoE)

Replace dense FFN with routed **experts**; only a subset activates per token. Increases parameter count without proportional FLOPs per token — routing and load balancing become engineering concerns.
