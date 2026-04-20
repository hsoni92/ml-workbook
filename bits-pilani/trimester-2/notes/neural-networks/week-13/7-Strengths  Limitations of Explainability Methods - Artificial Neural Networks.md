# Strengths and Limitations of Explainability Methods - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Compare** the main strengths of common explainability methods.
2. **Recognize** their major limitations and failure modes.
3. **Adopt** a responsible way to use explanations in practice.

---

## Why This Topic Matters

Explainability methods are useful, but they are easy to over-trust.

That is dangerous because explanations often look convincing. A colorful heatmap or a neat feature ranking can create the illusion of full understanding even when the explanation is incomplete or unstable.

So an important skill in responsible AI is not only knowing explanation methods, but also knowing **how far to trust them**.

---

## What Explainability Methods Are Good At

Across the methods studied so far, explainability is valuable because it can:

- improve transparency,
- help debug models,
- reveal spurious correlations,
- support communication with domain experts,
- strengthen trust in regulated or high-stakes settings.

In other words, explanations are often excellent **diagnostic tools**.

---

## Different Methods, Different Strengths

| Method family | Typical strength | Typical weakness |
|---|---|---|
| **Saliency / gradient methods** | Fast, intuitive, visual | Noisy and unstable |
| **Perturbation methods** | Model-agnostic and flexible | Can be computationally expensive and perturbation-sensitive |
| **Model-specific methods** | Use deep network structure well | Often depend on architecture and design choices |

No single method dominates on every criterion because different methods optimize different goals.

---

## The Main Limitations to Remember

Most explanation methods share several important limitations:

### 1. They are often local

Many methods explain one prediction, not the entire model.

### 2. They can be unstable

Two very similar inputs may produce noticeably different explanations.

### 3. They depend on assumptions

Sampling choices, baselines, smoothing, layers, and perturbation design can all change the explanation.

### 4. They are not causal

An explanation may show influence or association without proving true cause.

These limitations do not make explanations useless, but they do mean explanations must be interpreted with caution.

---

## The Biggest Risk: Overconfidence

One of the most common mistakes is to believe an explanation simply because it looks intuitive.

That is risky because:

- visually plausible explanations may still be wrong,
- highlighted features may not be true causes,
- one method may agree with our intuition for the wrong reason.

So the right attitude is:

**curiosity plus skepticism**

We should treat explanations as hypotheses to investigate, not facts to accept blindly.

---

## A Better Workflow for Responsible Use

A safer approach is to combine methods and look for stable patterns:

1. Run one explanation method.
2. Run a second method if possible.
3. Check whether the results are reasonably consistent.
4. Compare the explanation with domain knowledge.
5. Use evaluation results and error analysis together with the explanation.

This multi-method view helps reduce false confidence.

---

## Focus on Patterns, Not Only Anecdotes

Another good practice is to avoid relying only on isolated examples.

A single explanation can be interesting, but repeated patterns across many samples are more informative.

For example:

- if many explanations consistently highlight irrelevant background regions,
- or one subgroup repeatedly shows suspicious attribution behavior,

then we have stronger evidence of a systematic issue.

---

## Common Misunderstandings

- **"If the explanation looks intuitive, it must be true."**
  Visual plausibility is not the same as validity.

- **"One method is enough."**
  Method disagreement can itself reveal uncertainty or weakness.

- **"Explainability removes uncertainty."**
  It reduces uncertainty, but it does not eliminate it.

---

## Summary and Exam-Ready Takeaways

- Explainability methods are valuable for debugging, transparency, and stakeholder trust.
- Different method families have different strengths and different weaknesses.
- Most explanations are local, assumption-dependent, and non-causal.
- Overconfidence is one of the biggest practical risks.
- Responsible practitioners use multiple methods, compare results with domain knowledge, and treat explanations as investigative evidence.

---

## Bridge to the Next Note

So far, we have focused on understanding individual predictions. The next topic broadens the lens:

**How can AI systems be biased or unfair even when they seem accurate overall?**
