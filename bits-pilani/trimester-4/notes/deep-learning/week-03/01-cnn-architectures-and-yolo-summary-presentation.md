# CNN Architectures and YOLO

## How CNN Designs Evolved

| Model | Idea |
| --- | --- |
| LeNet-5 | Yann LeCun's digit and document recognizer. Two convolutions, two pooling stages, and fully connected layers. The template later CNNs follow. |
| AlexNet | Won ILSVRC 2012 with GPU training. ReLU, dropout, 8 layers, about $60$ million parameters. |
| VGGNet | Stacks of $3 \times 3$ convolutions add depth without a blow-up in parameters. |
| GoogLeNet | The Inception module runs $1 \times 1$, $3 \times 3$, and $5 \times 5$ filters in parallel. 22 layers and about $5$ million parameters, roughly $12\times$ fewer than AlexNet. |
| ResNet | Skip connections stop the degradation problem and vanishing gradients. 152 or more layers, $3.57\%$ top-5 error on ILSVRC 2015. |
| DenseNet | Each layer receives every preceding feature map. Features are reused, gradients flow further, and the parameter count stays lower. |
| EfficientNet | Scales depth, width, and resolution together, so accuracy rises without wasting compute. |

The shift is from "deeper at any cost" to "deeper and more efficient."

## AlexNet

ImageNet held more than $15$ million images. The ILSVRC subset used about $1.2$ million images in $1{,}000$ classes, which is what made a deep model trainable in 2012.

AlexNet has 5 convolutional layers and 3 fully connected layers. The dense layers are 4096 units wide and end in a 1000-way softmax. Max pooling downsamples selected feature maps while the channel count grows.

ReLU, $f(x) = \max(0, x)$, replaced tanh and sigmoid. Training was about $6\times$ faster, and positive inputs do not saturate.

Regularization and the result:

- Dropout with $p = 0.5$ on the two fully connected layers, needed because the model has about $60$ million parameters.
- Augmentation: random flips, $224 \times 224$ crops from $256 \times 256$ images, and PCA color jitter. Test-time scoring averages 10 crops.
- Local response normalization adds a further generalization effect.
- The 2012 result is the break that led to VGG, GoogLeNet, ResNet, and routine transfer learning.

## VGG

VGG asked whether going deeper than AlexNet would raise accuracy. At ILSVRC 2014 it placed 1st in localization and 2nd in classification.

Every convolution uses a $3 \times 3$ kernel and every pooling layer is $2 \times 2$ max pooling. Three stacked $3 \times 3$ layers see a $7 \times 7$ field but use $27$ weights instead of $49$ (about $45\%$ fewer), and each stack adds a ReLU.

A VGG block repeats that pattern. After each pool, the channel count doubles: $64 \rightarrow 128 \rightarrow 256 \rightarrow 512$.

| Variant | Convolutional layers | Fully connected layers |
| --- | --- | --- |
| VGG-11 | 8 | 3 |
| VGG-16 | 13 | 3 |
| VGG-19 | 16 | 3 |

Training uses mini-batch SGD with momentum $0.9$, L2 weight decay, and dropout $0.5$ on the fully connected layers. Deeper variants are initialized from a trained VGG-11, and training uses multiple image scales. The convolutional trunk is reused as a feature extractor in medical imaging, detection, and style transfer.

### VGG-16 vs VGG-19

Simonyan and Zisserman (Oxford, 2014) replaced large kernels such as $11 \times 11$ with stacks of $3 \times 3$.

| | VGG-16 | VGG-19 |
| --- | --- | --- |
| Convolutional layers | 13 | 16 |
| Parameters | about $138$ million | about $144$ million |
| Shared tail | 5 stages, then 3 fully connected layers and a softmax | same |

VGG-19 is only slightly more accurate, and it is slower and heavier. VGG-16 is the one used in practice.

The published recipe: batch size $256$, momentum $0.9$, learning rate $0.01$ halved when validation plateaus, L2 penalty $5 \times 10^{-4}$, dropout $0.5$, plus flips and RGB shifts.

Top-5 error along the timeline: AlexNet 2012 at $15.3\%$, VGG 2014 at $7.3\%$, GoogLeNet in 2014, ResNet 2015 at $3.57\%$.

Pretrained VGG adapts to specialized tasks. It remains a teaching baseline and a frozen backbone, including in Faster R-CNN.

## YOLO

Two-stage detectors such as R-CNN propose regions and then classify each region. That is slow and awkward to train end to end.

YOLO treats detection as one regression. A single CNN, in one forward pass, predicts boxes and class probabilities from the raw pixels.

The image is split into an $S \times S$ grid. Each cell predicts $B$ boxes and a confidence for each box.

| Fact | Value |
| --- | --- |
| Base YOLO speed | $45$ frames per second |
| Fast YOLO | $155$ frames per second |
| Trade-off | Higher input resolution helps small objects and lowers the frame rate. Localization error is higher than in two-stage detectors. |
| Strength | Far fewer false positives on background. |

The loss adds localization, confidence, and classification terms. $\lambda_{\text{coord}}$ and $\lambda_{\text{noobj}}$ set their relative weights. Later versions from YOLOv1 through YOLOv8 improved speed, accuracy, and what the detector can handle.

### Grid, boxes, and the output tensor

In YOLOv1 the grid is $7 \times 7$. The cell that contains an object's center is the cell responsible for that object.

Each box is $(x, y, w, h, \text{confidence})$. The center $(x, y)$ is relative to the cell. Width and height are relative to the image. Confidence is $\Pr(\text{Object}) \times \text{IoU}(\text{pred}, \text{truth})$: it says both whether an object is present and how well the box matches.

The decoded tensor is $7 \times 7 \times 30$: a $7 \times 7$ grid, 2 boxes, and 20 classes.

Training details and limits:

- Localization uses squared error on $x$, $y$, $w$, and $h$, plus confidence and classification terms.
- Non-maximum suppression drops overlapping boxes and leaves one detection per object.
- YOLOv1 to YOLOv3 added anchor boxes, multi-scale prediction, and batch normalization.
- Remaining weak spots are small objects, crowded scenes, unusual aspect ratios, and localization error from the squared-error box loss.

## Real-Time Detection and IoU

The reason for a one-pass detector is latency. Region-proposal pipelines were too slow for live video. YOLO emits boxes, labels, and confidence at $45$ or more frames per second. Each grid cell outputs box coordinates, an objectness score, and class probabilities.

Intersection over union is overlap area divided by union area, a score from $0$ to $1$. A detection is kept only when $\text{IoU} \ge$ a threshold, often $0.5$.

| Measure | Meaning |
| --- | --- |
| Precision | Fraction of detections that are correct. |
| Recall | Fraction of real objects that were found. |
| mAP at IoU $0.50$ | A lenient match threshold. |
| mAP averaged from $0.50$ to $0.95$ | The same score averaged over stricter overlaps. |

IoU is used when scoring a prediction, when filtering duplicates, and when computing the metric. Safety-critical systems raise the threshold. The same family of models is used in autonomous driving, medical imaging, surveillance, and retail.

## U-Net

Segmentation labels every pixel, and biomedical sets usually have few annotated images. A sliding-window CNN is slow, works patch by patch, and loses the wider context.

U-Net predicts a full mask in one encoder-decoder pass:

- **Contracting path** ("what"): $3 \times 3$ convolutions, ReLU, and $2 \times 2$ pooling. Spatial size halves and the channel count doubles.
- **Expanding path** ("where"): transposed convolutions restore resolution.
- **Skip connections** concatenate the encoder map at each level into the matching decoder level, which puts fine detail back.
- **Augmentation** uses elastic deformations plus rotation, flips, and scaling to stretch a small labeled set.
- **Weighted loss** puts extra weight on border pixels so boundaries stay sharp.

The useful properties are pixel-level output, the symmetric U, the skips, and the ability to train from limited labels.

---

**← [Previous](../week-02/01-convolutional-neural-networks-summary-presentation.md) · [Index](../README.md) · [Next](../week-04/01-recurrent-neural-networks-roadmap-and-character-level-lstm-lab-transcript.md) →**
