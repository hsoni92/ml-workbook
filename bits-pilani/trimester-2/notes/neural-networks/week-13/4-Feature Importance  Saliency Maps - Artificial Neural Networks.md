# Feature Importance and Saliency Maps - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Explain** what feature importance means in local and global settings.
2. **Describe** the basic idea behind saliency maps in deep networks.
3. **Recognize** the strengths and limitations of saliency-based explanations.

---

## Why This Topic Matters

Once we decide that model predictions need explanation, the most natural question is:

**Which inputs mattered most?**

That question appears in many forms:

- Which words drove a sentiment prediction?
- Which patient variables influenced a diagnosis score?
- Which image regions pushed the model toward the label "cat" or "tumor"?

Feature importance tries to answer that question. In deep vision models, the answer is often shown using **saliency maps**.

---

## What Feature Importance Means

Feature importance identifies which parts of the input had the strongest influence on a prediction.

There are two common ways to ask for it:

| Type | Main question | Example |
|---|---|---|
| **Global feature importance** | Which features matter across the dataset? | Which variables matter most overall in a loan model? |
| **Local feature importance** | Which features mattered for this one prediction? | Why was this one applicant rejected? |

For images, local importance is usually visualized spatially. Instead of a ranked list of features, we get a heatmap over pixels or regions.

---

## Saliency Map Intuition

Saliency maps are usually built from gradients.

The idea is simple:

- If changing a pixel slightly causes a large change in the output score,
- then that pixel is locally important for the prediction.

So the model computes a sensitivity score for each input location, and we visualize the result as a heatmap.

This makes saliency one of the most intuitive explanation methods in deep learning.

---

## High-Level Workflow

1. Feed the input image into the network.
2. Select the class score of interest.
3. Compute how sensitive that score is to changes in each input pixel.
4. Convert those sensitivities into a heatmap.
5. Overlay the heatmap on the image to see where the network is focusing.

This does not show the model's full reasoning, but it shows where influence is concentrated.

---

## A Simple Example

Suppose an image classifier predicts **"dog."**

- If the saliency map highlights the dog's face and body, that is encouraging.
- If it highlights a background watermark that happened to appear in many dog images during training, that is a warning sign.

This is why saliency maps are useful for debugging shortcut learning.

---

## Why Saliency Maps Are Useful

Saliency maps are popular because they are:

- **fast** to compute,
- **visual** and easy to communicate,
- **useful for debugging** spurious focus,
- **helpful for local inspection** of one prediction at a time.

They are often the first tool practitioners try when they want a quick explanation of a deep vision model.

---

## What Saliency Maps Cannot Tell Us

Saliency maps have important limitations:

- They show **influence**, not causal proof.
- They can be **noisy** and hard to interpret.
- Small choices in smoothing or normalization can change the map.
- A visually appealing heatmap can still be misleading.

So saliency maps should be treated as **diagnostic tools**, not as definitive evidence that the model truly understands the task.

---

## Common Misunderstandings

- **"Highlighted pixels are the true cause of the prediction."**
  Saliency reflects local sensitivity, not intervention-based causality.

- **"One clean saliency map proves the model is valid."**
  A single visualization is never enough for full validation.

- **"Noisy saliency always means a bad model."**
  Sometimes the noise comes from the method itself, not only from the model.

---

## Summary and Exam-Ready Takeaways

- Feature importance asks which inputs influenced a prediction.
- It can be studied globally across many examples or locally for one example.
- Saliency maps are local visual explanations that usually rely on gradient-based sensitivity.
- They are useful for debugging and identifying suspicious focus regions.
- Saliency maps show influence, not full reasoning or causation, so they must be interpreted carefully.

---

## Bridge to the Next Note

Saliency uses gradients to study sensitivity. The next family of methods takes a different route:

**change the input, observe the output, and infer importance from the response.**

That leads us to **perturbation-based methods such as LIME and SHAP**.
