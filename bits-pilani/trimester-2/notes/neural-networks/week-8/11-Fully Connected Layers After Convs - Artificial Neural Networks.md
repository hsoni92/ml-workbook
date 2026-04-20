# Fully Connected Layers After Convs - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Explain why convolutional features alone are not the final prediction.
2. Describe the role of **flattening**.
3. Explain how **fully connected layers** perform global reasoning.
4. Distinguish between the CNN **feature extractor** and the prediction **head**.

---

## Why CNNs Need a Final Prediction Stage

After several convolutional blocks, the network produces feature maps that say:

- what patterns appear,
- where they appear,
- and how strongly they appear.

That is excellent for representation learning, but many tasks such as **classification** or **regression** require a final global decision.

For example, image classification usually needs one class prediction for the whole image, not just a collection of local responses.

---

## Convolutional Layers vs Fully Connected Layers

It helps to separate the CNN into two conceptual parts:

1. **Backbone / feature extractor**: convolutional blocks that learn spatial features.
2. **Head / predictor**: layers that combine those features and produce the final output.

Convolutional layers are strong at local and spatial feature extraction. Fully connected layers are useful when the model must combine many learned cues into a single decision.

---

## What Flattening Does

Before dense layers can be applied in the classical CNN pipeline, the spatial feature maps must be reshaped into a vector.

If the final feature tensor has shape:

`H x W x C`

then flattening converts it to a vector of length:

`H * W * C`

Important point:

- **flattening does not learn anything**,
- it is only a structural transformation.

It acts as the bridge from **spatial representation** to **vector-based decision making**.

---

## What Fully Connected Layers Do

Once the representation is flattened, fully connected layers can:

- combine information from all positions and channels,
- learn global decision boundaries,
- map the extracted features to the final output.

At this stage, the network behaves similarly to the multilayer perceptrons studied earlier in the course, except the input to the dense layers is now a learned feature representation instead of raw pixels.

---

## End-to-End Pipeline

```text
image
  -> convolutional blocks extract spatial features
  -> final feature maps
  -> flattening converts them to a vector
  -> fully connected layers combine global evidence
  -> output prediction
```

This pipeline shows how CNNs move from **spatial feature extraction** to **decision making**.

---

## Modern Note

Many modern CNNs reduce the use of large dense layers because they can be parameter-heavy.

A common alternative is **global average pooling**, followed by a smaller classifier head. But the conceptual need remains the same:

- the network still needs a final stage that converts learned features into predictions.

So the exact implementation may differ, but the idea of a **prediction head** remains essential.

---

## Common Confusions

- Flattening is **not** a learned operation.
- Convolutional layers alone do not usually produce the final global decision for standard classification pipelines.
- Fully connected layers are not the only possible head, but **some prediction head is always needed**.

---

## Summary

- Convolutional layers extract structured spatial features.
- Flattening reshapes those features into a vector.
- Fully connected layers combine global evidence and produce final outputs.
- A CNN can be viewed as **feature extractor + prediction head**.

**Bridge to the next note:** besides convolution and dense layers, modern CNNs rely on other supporting components such as **activations**, **batch normalization**, and **dropout**.
