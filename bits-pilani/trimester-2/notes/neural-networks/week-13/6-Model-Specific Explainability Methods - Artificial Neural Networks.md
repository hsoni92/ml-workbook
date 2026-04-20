# Model-Specific Explainability Methods - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Explain** why some explanation methods are designed specifically for deep networks.
2. **Describe** the core intuition behind Grad-CAM and Integrated Gradients.
3. **Compare** when each method is most useful and what its main limitations are.

---

## Why Model-Specific Methods Exist

Model-agnostic methods are flexible, but they ignore the rich internal structure of deep networks.

A deep neural network contains:

- layers,
- activations,
- gradients,
- feature maps,
- hierarchical internal representations.

Model-specific methods try to use that structure directly. The idea is simple:

**if the model already contains useful internal signals, why not exploit them for explanation?**

---

## Two Important Examples

This note focuses on:

- **Grad-CAM**
- **Integrated Gradients**

Both are powerful, but they answer slightly different questions.

| Method | Best suited for | Main question it answers |
|---|---|---|
| **Grad-CAM** | CNN-based image models | Which regions of the image mattered most for this class? |
| **Integrated Gradients** | General feature attribution settings | How much did each input feature contribute to the prediction? |

---

## Grad-CAM Intuition

Grad-CAM stands for **Gradient-weighted Class Activation Mapping**.

It was designed especially for convolutional neural networks.

The core idea:

1. Look at a convolutional layer's feature maps.
2. Compute how the class score changes with respect to those maps.
3. Use those gradients to decide which feature maps matter most.
4. Combine them into a class-specific heatmap.

The result is a visual explanation showing where the model focused in the image.

This is why Grad-CAM is so intuitive in computer vision tasks.

---

## Integrated Gradients Intuition

Integrated Gradients takes a different approach.

Instead of using one gradient at the input, it accumulates gradients along a path from:

- a **baseline input** and
- the **actual input**.

This helps produce a more principled attribution for each feature.

You can think of it like this:

- start from a neutral reference point,
- move gradually toward the real example,
- measure how the prediction changes along the way,
- add up those contributions.

The result is a feature-level attribution score.

---

## A Useful Comparison

### Grad-CAM

- Very visual
- Natural for CNN image models
- Good for answering "where did the model look?"

### Integrated Gradients

- More general
- Works at the feature level
- Good for answering "which inputs contributed how much?"

So these methods are complementary, not interchangeable.

---

## Example Intuition

Suppose a CNN predicts **"cat"** for an image.

- **Grad-CAM** may highlight the ears, eyes, and face region, showing the spatial focus of the model.
- **Integrated Gradients** may assign contributions to specific pixels or input features, showing which parts pushed the prediction toward the class.

Both provide useful evidence, but one emphasizes localization and the other emphasizes attribution.

---

## Important Limitations

These methods are still not perfect.

- They are still based on gradients, so they can be noisy.
- Grad-CAM depends on layer choice and is most natural for convolutional models.
- Integrated Gradients depends strongly on the choice of baseline.
- Neither method gives causal proof or complete transparency.

So even though they often produce more informative explanations than generic black-box tools, they should still be treated as diagnostic aids.

---

## Common Misunderstandings

- **"Grad-CAM shows exactly what the model understands."**
  It shows important regions, not complete reasoning.

- **"Integrated Gradients is baseline-free."**
  Baseline choice is one of its most important design decisions.

- **"Model-specific methods provide ground truth explanations."**
  They provide useful evidence, but not final truth.

---

## Summary and Exam-Ready Takeaways

- Model-specific explanation methods exploit the internal structure of deep networks.
- Grad-CAM is especially useful for CNN image models and highlights important spatial regions.
- Integrated Gradients attributes prediction influence across input features using a baseline-to-input path.
- Grad-CAM and Integrated Gradients solve related but different explanation problems.
- Both methods are powerful, but both still require careful interpretation.

---

## Bridge to the Next Note

At this point, we have seen several explanation families. The next question is critical:

**How much should we trust any of them?**

That leads to the strengths and limitations of explainability methods.
