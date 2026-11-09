# Deep Learning — Revision Mind Map

> High-yield acronyms and one-liners across Weeks 1–7. Pair with each week's transcript and deck summary.

## Course arc (by week)

| Week | Block |
| --- | --- |
| 1 | Foundations: ML gaps, training loop, losses, hardware, churn lab |
| 2 | CNNs: conv, pool, transfer learning, metrics |
| 3 | CNN architectures: AlexNet → EfficientNet; YOLO; segmentation intro |
| 4 | RNNs, LSTM/GRU, seq2seq, attention; makeup: YOLO/U-Net |
| 5 | Transformers: self-attention, encoder-decoder, masks |
| 6 | BERT / GPT / T5, decoding, fine-tuning vs RAG vs scratch |
| 7 | Vision Transformer (ViT), DeiT, practice |

---

## Foundations (Week 1)

```
DEEP LEARNING = hierarchical features from raw data (no hand-built features)
TRAINING LOOP = forward → loss → backprop (chain rule) → weight update
```

| Traditional ML | Deep learning |
| --- | --- |
| Manual features, tabular focus | Learned features, unstructured data |
| Early saturation on fixed data | Scales with data and parameters |

- **Universal approximation** — one hidden layer + nonlinearity can approximate any continuous function (given width); **depth** composes abstractions faster than ultra-wide shallow nets
- **Chain rule** — $\partial L / \partial w = (\partial L / \partial y)(\partial y / \partial h)(\partial h / \partial w)$
- **Vanishing gradients** — saturated sigmoid/tanh; fixes: **ReLU**, **residual skips**
- **Learning rate** — too high: oscillate/diverge; too low: stall; **cosine annealing** decays step size
- **Optimizers** — SGD+momentum, RMSProp, **Adam** / **AdamW** (decoupled weight decay)
- **Regularization** — dropout, L1/L2, **batch norm** (stabilize activations per mini-batch)
- **Losses** — regression: MSE, MAE, Huber; classification: **cross-entropy**, **focal** (imbalance)
- **Linear layer** — $y = Wx + b$; params $M(N+1)$; memory = weights + activations + optimizer state (Adam $\approx 2\times$ extra)
- **Memory wall** — HBM bandwidth vs FLOPs; **arithmetic intensity**; quantisation (FP16/INT8), tensor cores, kernel fusion, FlashAttention

---

## Convolutional Neural Networks (Week 2)

- **Why not fully connected on images?** — parameter explosion, no spatial prior, overfits noise
- **Conv** — local receptive field, **weight sharing**, translation invariance
- **Feature hierarchy** — edges → textures → parts → objects
- **Stride / padding** — valid (shrink), same ($W_{\text{out}} = W_{\text{in}}$)
- **Pooling** — max (default) vs average; downsampling + receptive-field growth
- **Head** — flatten → dense → **softmax** logits
- **Transfer learning** — freeze trunk + train head (**feature extraction**) vs unlock top layers with **small LR** (**fine-tuning**)
- **Metrics** — confusion matrix; **precision** $= \text{TP}/(\text{TP}+\text{FP})$, **recall** $= \text{TP}/(\text{TP}+\text{FN})$, **F1** $= 2PR/(P+R)$
- **Regularization** — dropout ($p=0.5$, scale at test); batch norm ($\gamma$, $\beta$); **data augmentation**

---

## CNN Architectures and Detection (Weeks 3–4)

| Model | Hook |
| --- | --- |
| LeNet-5 | Template CNN |
| AlexNet (2012) | ReLU, dropout, GPU scale |
| VGG | Stacked $3\times3$, depth |
| GoogLeNet | Inception multi-scale |
| ResNet | **Skip connections**, very deep |
| DenseNet | Dense connections, reuse |
| EfficientNet | Compound scaling |

**YOLO** — single forward pass; $S \times S$ grid; confidence $\Pr(\text{obj}) \times \text{IoU}$; **NMS**; trade speed vs two-stage accuracy

**U-Net** — encoder-decoder + **skip connections**; pixel-wise segmentation; augmentation on small biomedical sets

$$\text{IoU} = \frac{\text{overlap}}{\text{union}}$$

---

## Recurrent Networks (Week 4)

- **RNN** — shared $W$, $U$, $V$; hidden state $h_t = f(W h_{t-1} + U x_t)$
- **Patterns** — many-to-one (sentiment), one-to-many (caption), many-to-many (MT)
- **BPTT** — unfold graph; **gradient clipping** (explode); **truncated BPTT** (memory vs long deps)
- **LSTM** — cell state + forget / input / output gates; additive update beats vanishing
- **GRU** — update + reset gates; fewer params than LSTM
- **BiRNN** — forward + backward; needs full sequence (not streaming decode)
- **Seq2seq bottleneck** — fixed context vector; **attention** = weighted encoder states per decoder step

---

## Transformers (Week 5)

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

- **Q/K/V** — query asks, key matches, value carries content
- **Multi-head** — parallel relation types; concat + $W_O$
- **Positional encoding** — inject order (sinusoidal or learned; RoPE/ALiBi for long context)
- **Encoder** — full self-attention + FFN + residual + layer norm
- **Decoder** — **masked** self-attention (causal) + **cross-attention** to encoder + FFN
- **Training** — next-token cross-entropy; causal mask matches inference

---

## LLM Variants and Transfer (Week 6)

| Variant | Stack | Best for |
| --- | --- | --- |
| **BERT** | Encoder-only, bidirectional | Classification, NER, search |
| **GPT** | Decoder-only, autoregressive | Generation, chat |
| **T5** | Encoder-decoder | Translation, summarization, QA |

- **MLM** — mask ~15% tokens (BERT); **NSP** — real vs random sentence pairs
- **Pre-train once, fine-tune** — default for industry; **RAG** — retrieve domain docs at inference (cheaper updates than re-pretraining)
- **Train from scratch** — giants only (data + compute)
- **Decoding** — greedy, beam; **temperature**, top-K, top-P
- **Tokenizers** — BPE, WordPiece, SentencePiece
- **Eval after fine-tune** — task metrics + check **catastrophic forgetting** on old tasks

---

## Vision Transformers (Week 7)

- **ViT** — split image into $16\times16$ **patches**; patch embeddings + position + transformer; needs large pre-training
- **DeiT** — **knowledge distillation** from CNN teacher; less data
- **Swin** — hierarchical patches, window + shifted-window attention (high resolution)
- **ViViT** — video + temporal attention (awareness level)
- **Fine-tune recipe** — load pretrained ViT, freeze or unfreeze backbone, train head on labelled set

---

## Exam traps

- Depth helps **composition**, not magic — still need data, regularization, and compute budget
- High **accuracy** on imbalanced classes is misleading — report precision/recall/F1
- **Transfer learning** on tiny data → freeze + small head; full fine-tune needs more data and low LR
- **Autoregressive** decoder cannot use future tokens — masked attention is mandatory at train and test
- **RAG** updates knowledge without full retrain; fine-tuning **bakes in** weights (forgetting risk if aggressive)
