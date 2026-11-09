# Convolutional Neural Networks

## Why a Fully Connected Net Fails on Images

Flattening a $256 \times 256$ image yields $65{,}536$ isolated numbers. Nearby pixels and far-away pixels are then treated the same, and the network has no notion of a 2D grid.

Connecting every flattened pixel to a hidden layer produces a huge dense matrix, often millions of parameters. That matrix overfits noise and is expensive in memory and compute.

## Filters, Hierarchy, and Invariance

| Idea | Meaning |
| --- | --- |
| Local receptive field | A small kernel, typically $3 \times 3$ or $5 \times 5$, slides across the map. |
| Weight sharing | The same filter weights are reused at every spatial position. |
| Early layers | Detect edges, oriented lines, and color blobs. |
| Deep layers | Combine those primitives into object parts and objects. |
| Translation invariance | The same feature can be detected wherever it appears in the image. |

## Dot Products and Feature Maps

A $K \times K$ kernel computes a local dot product at each position and emits one scalar. The filter covers the full input depth, so an RGB kernel is shaped like $5 \times 5 \times 3$, not $5 \times 5$.

Collecting those scalars gives a 2D feature map. $N$ different filters produce $N$ maps, stacked into a volume such as $28 \times 28 \times 6$.

## Stride and Padding

| Choice | Effect |
| --- | --- |
| Stride $1$ | The filter moves one pixel at a time and keeps fine spatial detail. |
| Stride $\ge 2$ | The filter jumps, the map shrinks, and the cost drops. |
| Valid padding | No border padding. Height and width shrink after every convolution. |
| Same padding | Zeros around the border keep the spatial size: $W_{\text{out}} = W_{\text{in}}$. |

## Pooling

| | Max pooling | Average pooling |
| --- | --- | --- |
| Operation | Takes the largest value in a window, often $2 \times 2$. | Takes the mean of the window. |
| Effect | Keeps strong responses and drops weak background noise. | Keeps a smoother summary, including texture that max pooling would discard. |
| Typical use | Default in AlexNet, VGG, and ResNet. | Global average pooling can replace a heavy fully connected classifier. |

Downsampling does four jobs at once:

1. **Spatial compression** reduces height and width, so later layers have fewer parameters and less activation memory.
2. **Receptive-field growth.** A unit deeper in the net sees a larger patch of the original image, for example a $64 \times 64$ region.
3. **Less overfitting.** Dropping exact pixel location pushes the net toward abstract structure.
4. **The usual cascade** is convolution, then ReLU, then pooling, then a dense head, then the class output.

## From Maps to a Vector

Until the head, activations stay in a height $\times$ width $\times$ depth volume. Convolution has already extracted local patterns. Flattening only reorders that volume into a vector. A $7 \times 7 \times 512$ map becomes a vector of length $25{,}088$, with no values thrown away.

## The Classification Head

The dense head connects every extracted signal so local parts can vote for a whole object. Each layer is a linear map plus a non-linearity, $\text{ReLU}(Wx + b)$, and the width typically shrinks, for example $4096 \rightarrow 1024 \rightarrow 10$. A softmax turns the final logits into class probabilities.

## Transfer Learning

Training a vision net from scratch needs a very large labeled set and a long GPU run, and it relearns edges and textures that existing models already know.

Transfer learning starts from those pretrained features:

- Freeze the convolutional trunk so the learned patterns stay put.
- Replace the top dense layers with a head for the new label set.
- Training then converges faster and works on much smaller datasets.

| | Feature extraction | Fine-tuning |
| --- | --- | --- |
| Trunk | Entire convolutional base stays frozen. | The top convolutional layers are unlocked. |
| What is trained | Only the new classifier head. | The head, plus a small update to the unlocked layers. |
| Learning rate | Ordinary rate on the new head. | A very small rate so pretrained weights move only slightly. |
| When | The target set is small. | There is enough target data to adapt the features. |
| Risk | Safer against overfitting on a niche task. | Specializes generic features to the new domain. |

## Confusion Matrix and Accuracy

| Cell | Meaning |
| --- | --- |
| True positive (TP) | Predicted yes, and the label is yes. |
| True negative (TN) | Predicted no, and the label is no. |
| False positive (FP) | Predicted yes, but the label is no (type I error). |
| False negative (FN) | Predicted no, but the label is yes (type II error). |

Accuracy is $(\text{TP} + \text{TN}) / \text{Total}$. It is easy to read when classes are balanced. On an imbalanced set it hides failure on the rare class: a model that always predicts the majority class can score $99\%$ and still be useless.

## Precision, Recall, and F1

| Metric | Formula | What it rewards |
| --- | --- | --- |
| Precision | $\text{TP} / (\text{TP} + \text{FP})$ | Positive predictions that are actually positive. Used when a false alarm is expensive (spam, legal flags). |
| Recall | $\text{TP} / (\text{TP} + \text{FN})$ | Real positives that are found. Used when a miss is expensive (disease, fraud, safety). |
| F1 | $2 \times (P \times R) / (P + R)$ | The harmonic mean. A collapse in either precision or recall pulls F1 down. |

## Dropout, Batch Normalization, and Augmentation

**Dropout.** Each pass randomly zeroes units with $p = 0.5$, so the net must build redundant features. At test time the active weights are scaled by $p$.

**Batch normalization.** Each mini-batch is normalized to zero mean and unit variance. That reduces internal covariate shift and speeds convergence. A learned scale $\gamma$ and shift $\beta$ restore the representation the layer needs.

**Augmentation** invents extra views of the same label:

- Random crops teach the net that position is not the object.
- Rotation and scaling teach orientation and size.
- Color jitter and contrast shifts teach the net to ignore lighting.
- Do not apply a transform that changes the label, such as a flip that turns a 6 into a 9.
- Augmentation and dropout together improve generalization.

---

**← [Previous](../week-01/01-module1-deep-learning-foundations-summary-presentation.md) · [Index](../README.md) · [Next](../week-03/01-module3-cnn-architectures-yolo-summary-presentation.md) →**
