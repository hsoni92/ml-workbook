# Neural Networks — Training Architecture

```
NN Training
│
├── Activation Functions
│ ├── Sigmoid / Tanh
│ ├── ReLU family
│ └── Softmax
│
├── Loss Functions
│ ├── MSE
│ └── Cross-Entropy
│
├── Backprop & Gradients
│ ├── Backpropagation
│ ├── Vanishing / Exploding
│ └── Initialization (Xavier / He)
│
├── Optimization
│ ├── Gradient Descent
│ │ ├── Batch
│ │ ├── SGD
│ │ └── Mini-batch
│ ├── Momentum
│ ├── RMSProp
│ └── Adam
│
├── Optimization Support
│ ├── Learning Rate Schedules
│ └── Gradient Clipping
│
├── Normalization
│ ├── BatchNorm
│ └── LayerNorm
│
├── Regularization
│ ├── L1 / L2
│ ├── Dropout
│ ├── Early Stopping
│ └── Data Augmentation
│
└── Evaluation & Diagnostics
  ├── Train / Val / Test
  ├── Bias–Variance
  ├── Gradient Monitoring
  └── Loss Landscape
```

## Quick Reference

### Activation Functions
| Function | Formula | Range | Use Case |
|---|---|---|---|
| Sigmoid | `σ(x) = 1/(1+e⁻ˣ)` | (0, 1) | Binary classification output |
| Tanh | `tanh(x)` | (-1, 1) | Hidden layers (legacy) |
| ReLU | `max(0, x)` | [0, ∞) | Default hidden layer |
| Leaky ReLU | `max(0.01x, x)` | (-∞, ∞) | Dead neuron fix |
| Softmax | `eˣⁱ/Σeˣʲ` | (0, 1)³ | Multi-class output |

### Loss Functions
| Loss | Formula | Used For |
|---|---|---|
| MSE | `(1/n)Σ(y - ŷ)²` | Regression |
| Cross-Entropy | `-Σ y·log(ŷ)` | Classification |

### Optimization Landscape
```
Gradient Descent variants
├── Batch GD     — Whole dataset per step (slow, stable)
├── SGD          — One sample per step (fast, noisy)
└── Mini-batch   — Batches of 32/64/128 (default choice)

Momentum-based methods
├── Vanilla Momentum — Accumulate past gradients
├── RMSProp         — Per-parameter adaptive LR (divide by EMA of gradients)
└── Adam            — Combines Momentum + RMSProp (default for most tasks)

Adam = Momentum (first moment) + RMSProp (second moment scaling)
```

### Regularization Summary
| Technique | What it does |
|---|---|
| L1 (Lasso) | Adds `λ|ω|₁` — promotes sparsity (feature selection) |
| L2 (Ridge) | Adds `λ|ω|₂²` — shrinks weights (default weight decay) |
| Dropout | Randomly zero out neurons during training |
| Early Stopping | Stop when validation loss starts increasing |
| Data Augmentation | Artificially expand training data (flip, crop, noise) |

### Normalization Comparison
| Method | Normalizes | Typical Use |
|---|---|---|
| BatchNorm | Across batch dimension | CNNs, hidden layers |
| LayerNorm | Across features per sample | Transformers, RNNs |
| InstanceNorm | Per sample, per channel | Style transfer |
| GroupNorm | Per sample, groups of channels | When batch size is small |

### Bias–Variance Diagnosis
```
High Bias (Underfitting)     — Training loss ≈ Val loss, both high
                               → Larger model, more epochs, better features

High Variance (Overfitting)  — Val loss >> Training loss
                               → More data, dropout, L2, early stopping

Just Right                    — Training and val loss close and low
                               → Sweet spot
```

### Vanishing / Exploding Gradients
| Problem | Cause | Fix |
|---|---|---|
| Vanishing | Sigmoid/tanh gradients < 1, deep networks | ReLU, residual connections, BatchNorm |
| Exploding | Large weights, deep networks | Gradient clipping, proper initialization, smaller LR |