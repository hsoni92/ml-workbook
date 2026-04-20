# Perturbation based Methods - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Explain** the central idea behind perturbation-based explainability.
2. **Compare** LIME and SHAP at a conceptual level.
3. **Identify** the strengths and limitations of model-agnostic explanation methods.

---

## Why This Topic Matters

Gradient-based explanations are useful, but they are not the only way to inspect a model.

A very natural alternative is:

**change the input slightly and see how the prediction changes.**

If a small change in one feature produces a large change in output, that feature is likely important.

This is the basic idea behind perturbation-based explainability.

---

## The Core Intuition

Perturbation methods explain a prediction by probing the model with modified versions of the input.

Instead of looking inside the model, they ask:

- What happens if this word is removed?
- What happens if this feature value is changed?
- What happens if part of the image is masked?

Because they study the input-output behavior directly, these methods can work with many kinds of black-box models.

---

## Why These Methods Are Attractive

One major advantage is that they are **model-agnostic**.

They can be applied to:

- neural networks,
- tree-based systems,
- ensemble models,
- other predictive black boxes.

This makes them especially practical when we care more about explaining predictions than about the internal architecture.

---

## LIME and SHAP

The two most common examples in this family are **LIME** and **SHAP**.

| Method | Main idea | Strength | Limitation |
|---|---|---|---|
| **LIME** | Fit a simple interpretable model around one input | Fast and intuitive | Sensitive to sampling choices |
| **SHAP** | Estimate each feature's average contribution using Shapley values | Strong theoretical grounding | Often more computationally expensive |

---

## How LIME Works

LIME focuses on one prediction at a time.

High-level idea:

1. Take one input example.
2. Create many perturbed versions near that example.
3. Query the original black-box model on those perturbed samples.
4. Fit a simple local surrogate model, often linear.
5. Use the surrogate coefficients as the explanation.

So LIME does not directly explain the full black-box model. It explains a **local approximation** of behavior near one point.

---

## How SHAP Works

SHAP comes from cooperative game theory.

It treats each feature as a "player" contributing to the final prediction and asks:

**How much does each feature contribute on average across different feature combinations?**

This gives SHAP a more principled attribution framework. In exchange, the computation is often heavier than LIME.

Conceptually:

- **LIME** is more heuristic and practical.
- **SHAP** is more theoretically grounded and often more consistent.

---

## Example Intuition

Imagine a loan approval model.

- LIME may approximate the model locally and say: income and debt ratio were the strongest reasons this applicant was rejected.
- SHAP may assign additive contributions to each feature and show how much each one pushed the prediction toward approval or rejection.

Both are useful, but they answer the question through different mechanisms.

---

## An Important Warning: Plausible Perturbations Matter

Perturbation methods can become misleading when the modified inputs are unrealistic.

For example:

- masking words may create unnatural text,
- changing one feature independently may create an impossible tabular record,
- masking image regions may move the sample away from the true data manifold.

If the perturbed samples are unrealistic, the explanation may reflect strange model behavior on artificial inputs rather than meaningful reasoning on real ones.

---

## Common Misunderstandings

- **"Model-agnostic means automatically reliable."**
  Reliability still depends on how perturbations are generated.

- **"SHAP is always better than LIME."**
  SHAP is often more principled, but cost and workflow constraints still matter.

- **"A local explanation describes the whole model."**
  These methods usually explain one prediction at a time, not global behavior.

---

## Summary and Exam-Ready Takeaways

- Perturbation-based methods explain predictions by modifying inputs and observing output changes.
- They are attractive because they are model-agnostic.
- LIME fits a local surrogate model around one example.
- SHAP assigns feature contributions using a Shapley-value perspective.
- Both methods are useful, but both depend on the quality of the perturbation process.
- Local explanations should be interpreted carefully and not overgeneralized.

---

## Bridge to the Next Note

So far, we have seen gradient-based and model-agnostic explanation methods. The next step is to study methods that use the internal structure of deep networks directly:

**Grad-CAM and Integrated Gradients**.
