# Interpretability vs Explainability - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Define** interpretability and explainability clearly.
2. **Compare** intrinsic transparency with post-hoc explanation.
3. **Decide** when each approach is more appropriate in practice.

---

## Why This Distinction Matters

In many AI discussions, the words *interpretability* and *explainability* are used as if they mean the same thing. They do not.

Confusing them creates bad expectations. A team may ask for an "interpretable deep model" when what they really want is a powerful model plus tools that help explain its outputs.

This distinction matters for:

- system design,
- regulatory compliance,
- stakeholder trust,
- model selection in high-stakes applications.

---

## Core Definitions

### Interpretability

Interpretability means the model is understandable **by its own structure**.

A person can inspect the model directly and reason about how inputs affect outputs.

Typical examples:

- linear models,
- small decision trees,
- rule-based systems.

These models are often easier to understand globally, but they may have limited expressive power on very complex tasks.

### Explainability

Explainability means the model itself may be opaque, but we use additional methods to produce useful explanations **after training**.

Typical examples of explanation tools:

- feature attribution,
- saliency maps,
- LIME,
- SHAP.

So explainability is usually a workflow built around a complex model rather than a property of the model class itself.

---

## The Key Difference

The simplest way to remember the distinction is:

- **Interpretability is intrinsic.**
- **Explainability is external.**

Interpretability gives direct transparency.
Explainability gives post-hoc evidence about why a prediction may have happened.

---

## Comparison Table

| Dimension | Interpretability | Explainability |
|---|---|---|
| Nature | Built into the model | Added after training |
| Typical model types | Linear models, small trees, rule systems | Deep networks, ensembles, complex black-box models |
| Usual scope | Often global understanding | Often local, prediction-level insight |
| Main advantage | Direct transparency | Allows analysis of high-performance complex models |
| Main limitation | May sacrifice predictive power | Does not give full transparency or causal proof |

---

## An Intuitive Example

Suppose you are building a system for loan approval.

- With an **interpretable model**, you might directly inspect coefficients or decision rules and understand how income, debt, and repayment history influence the decision.
- With an **explainable black-box model**, you may not understand the full model structure, but you can still explain why one applicant was rejected by showing which features were most influential for that prediction.

So both approaches help understanding, but they help in different ways.

---

## When Each Is More Appropriate

### Prefer interpretability when:

- strict transparency is required,
- the task can be handled by a simple model,
- regulators or domain experts must inspect the full logic directly.

### Prefer explainability when:

- the task requires a more expressive model,
- performance demands deep learning or other complex architectures,
- local decision support is more realistic than full structural transparency.

In practice, some systems use a hybrid strategy: a powerful model for performance, supported by explanation tools for auditing and debugging.

---

## Important Limitation

Post-hoc explanation does **not** turn a black-box model into a fully transparent one.

An explanation is helpful evidence, but it is still an approximation of behavior. That is why explainability should be used carefully and not confused with perfect understanding.

---

## Common Misunderstandings

- **"Interpretability and explainability are interchangeable."**
  They solve related but different problems.

- **"Post-hoc explanations make any model transparent."**
  They provide insight, not full structural understanding.

- **"Interpretable models are always better."**
  Sometimes they are preferred, but sometimes they cannot achieve the required performance.

---

## Summary and Exam-Ready Takeaways

- Interpretability means the model is understandable by design.
- Explainability means using additional methods to analyze a complex model after training.
- Interpretability is intrinsic; explainability is post-hoc.
- Interpretable models often provide global transparency, while explainability often gives local insight.
- Choosing between them is a design decision shaped by performance needs, regulation, and deployment risk.

---

## Bridge to the Next Note

With the distinction clear, we can now study concrete explanation methods, starting with the most intuitive family:

**feature importance and saliency maps**.
