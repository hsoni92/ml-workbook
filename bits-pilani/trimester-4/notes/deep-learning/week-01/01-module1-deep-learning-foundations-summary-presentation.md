# Deep Learning Foundations

## Traditional Machine Learning vs Deep Learning

| Traditional machine learning | Deep learning |
| --- | --- |
| Manual feature engineering: domain experts build the feature vectors. | Automated extraction: the network learns hierarchical features from raw data. |
| Best suited to tabular, clean numerical data. | Dominates unstructured domains: vision, text, and audio. |
| Performance plateaus as the dataset grows. | Accuracy keeps improving as parameter scale grows. |

## Universal Approximation and Depth

| Idea | What it means |
| --- | --- |
| Universal approximation | A single hidden layer with non-linear activations can approximate any continuous function, given enough width. |
| Depth vs width | Deep networks compose abstractions exponentially faster than shallow wide networks, which need a huge number of parameters. |
| Hierarchical reuse | Lower layers capture primitive geometries. Deeper layers combine them into high-level semantic concepts. |

## The Four-Step Training Pipeline

1. **Forward pass.** Inputs propagate through the layers and produce predictions.
2. **Error calculation.** A loss function measures how far the prediction is from the target.
3. **Backpropagation.** The chain rule computes a gradient for every trainable weight.
4. **Weight update.** The optimizer steps the parameters opposite the gradient.

## The Chain Rule and Gradient Stability

For a composite loss $L = f(g(h(x)))$, backpropagation multiplies local derivatives backward:

$\partial L / \partial w = (\partial L / \partial y) \cdot (\partial y / \partial h) \cdot (\partial h / \partial w)$

| Problem or fix | Effect |
| --- | --- |
| Vanishing gradients | Saturated sigmoid or tanh units multiply slopes below 1, so the signal decays exponentially with depth. |
| ReLU | The derivative is 1 for positive inputs, so those units do not saturate. |
| Residual connections | The skip path lets the gradient bypass a deep block instead of passing through every layer. |

## Learning Rate

| Regime | What happens |
| --- | --- |
| Learning rate too large | Steps overshoot the minimum. The loss oscillates or diverges. |
| Learning rate too small | Progress stalls in shallow regions and training needs far too many epochs. |
| Cosine annealing | The step size decays smoothly as the optimizer approaches a minimum. |

## Optimizers and Regularization

**Optimizers**

- **SGD with momentum** keeps an exponential moving average of past gradients so the update can cross flat plateaus.
- **RMSProp** scales the learning rate down when recent gradient magnitudes are large.
- **Adam** combines momentum with an adaptive per-parameter variance estimate. **AdamW** uses the same idea with weight decay applied separately from the adaptive step.

**Regularization**

- **Dropout** randomly zeroes activations during training so units cannot co-adapt.
- **L1 and L2 penalties** constrain the size of the weight vector.
- **Batch normalization** normalizes each layer's inputs inside the mini-batch, which stabilizes training.

## Loss Functions

| Setting | Loss | Role |
| --- | --- | --- |
| Regression | Mean squared error | Penalizes large residuals quadratically. |
| Regression | Huber or mean absolute error | Uses a linear penalty on large errors, so noisy targets hurt less. |
| Classification | Cross-entropy | Negative log-likelihood of the target distribution. |
| Classification | Focal loss | Down-weights easy examples so rare classes still influence the gradient. |

## High-Dimensional Loss Landscapes

- In high dimensions, a point where the gradient is zero is usually a **saddle**, not a local minimum.
- Eigenvalues of the **Hessian** say which directions curve up, curve down, or are flat.
- Mini-batch sampling adds gradient noise. That noise helps the optimizer leave flat plateaus.

## The Linear Layer

A fully connected layer maps an input vector $x$ to an output by a rotation-and-scale plus a shift:

$y = Wx + b$

| Term | Role |
| --- | --- |
| Weight matrix $W$ | Scales, stretches, and rotates the feature space. |
| Bias $b$ | Shifts the decision boundary off the origin. |
| GEMM | The multiply is a general matrix multiplication, which GPUs execute efficiently. |

## Parameter Count and Memory

For a linear layer with $N$ inputs and $M$ outputs:

- Weights: $M \times N$
- Biases: $M$
- Total parameters: $M \times (N + 1)$

Training memory is more than the weights:

- **Parameters** are the static footprint of the FP32 or FP16 weights.
- **Activations** are the intermediate tensors stored for the backward pass.
- **Optimizer state**: Adam keeps two extra vectors per parameter, the first and second moments.

## The Memory Wall and the Roofline

Moving a value between high-bandwidth memory (HBM) and on-chip SRAM can cost on the order of $100\times$ more energy than an arithmetic operation.

**Arithmetic intensity** is FLOPs per byte moved. A low-intensity kernel is limited by memory bandwidth, not by peak FLOPs. Raising the mini-batch size raises intensity and keeps tensor cores busy.

## Hardware and Systems Tricks

| Technique | What it saves |
| --- | --- |
| Quantization (FP32 to FP16 or INT8) | Cuts weight bandwidth by about $2\times$ to $4\times$. |
| Tensor cores | Hardware units that run a $4 \times 4$ matrix multiply-accumulate in one step. |
| Kernel fusion | Runs neighboring elementwise ops on-chip and skips extra SRAM-to-HBM trips. |
| FlashAttention | Tiles the attention scores into SRAM so the full attention matrix is never written out to HBM. |

## Takeaways

- Deep networks replace hand-built features with hierarchical representations learned from raw data.
- Backpropagation and adaptive optimizers are how training moves through a high-dimensional loss surface.
- Scaling a model also means fitting its parameters, activations, and optimizer state into GPU memory bandwidth.

---

**← [Previous](../README.md) · [Index](../README.md) · [Next](../week-02/01-module2-convolutional-neural-networks-summary-presentation.md) →**
