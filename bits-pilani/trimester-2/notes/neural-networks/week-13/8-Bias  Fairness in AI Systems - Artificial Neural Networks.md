# Bias and Fairness in AI Systems - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Define** bias in the context of AI systems.
2. **Identify** common sources of unfair behavior in machine learning pipelines.
3. **Explain** why fairness must be treated separately from overall accuracy.

---

## Why This Topic Matters

A model can be accurate overall and still be unfair.

That is one of the most important ideas in responsible AI.

If we only look at average performance, we may miss the fact that one group experiences:

- more false negatives,
- more false positives,
- fewer beneficial outcomes,
- more harmful errors.

So fairness asks a broader question than accuracy:

**Who is the model working well for, and who is carrying the cost of its mistakes?**

---

## What Bias Means in AI

In AI, bias does **not** necessarily mean bad intent or personal prejudice.

It usually means a **systematic difference** in how a model behaves across groups.

For example, imagine a loan approval model:

- overall accuracy is high,
- but one demographic group receives approval much less often than another group with similar financial profiles.

That system may look strong on average while still behaving unfairly.

---

## Why Accuracy and Fairness Are Different

Accuracy compresses all predictions into one average number.

Fairness asks how predictions and errors are distributed across groups.

This difference matters because a model can achieve strong overall accuracy while disproportionately harming one part of the population.

A good example is a medical diagnosis model:

- suppose it reaches 95% accuracy overall,
- but most of the missed cases occur in women or another underrepresented group.

The model is accurate in aggregate, but unfair in effect.

---

## Common Sources of Bias

Bias often enters through the data or deployment process rather than through malicious intent.

| Bias source | What it means | Example |
|---|---|---|
| **Historical bias** | Past inequality is reflected in training labels | Hiring decisions from an already biased process |
| **Representation bias** | Some groups are underrepresented in data | Face recognition trained on weak coverage of darker skin tones |
| **Measurement bias** | Features or labels are poor proxies | Zip code standing in for socioeconomic or racial information |
| **Deployment bias** | The real use context differs from training context | Model trained in one country but deployed in another |

This table is important because it shows that unfairness can arise at multiple stages of the pipeline.

---

## Why Fairness Is a Separate Concern

Fairness matters because AI systems influence real opportunities and risks.

Examples:

- in finance, unfair models can deny access to credit,
- in healthcare, they can delay or miss treatment,
- in legal or administrative systems, they can reinforce existing inequality.

That is why fairness is not only a technical topic. It is also an ethical, legal, and social responsibility.

---

## A Practical Mental Model

You can think of fairness analysis like this:

1. Start with the model's overall performance.
2. Break results down by relevant groups.
3. Compare error patterns and outcome rates.
4. Investigate whether disparities are acceptable, explainable, or harmful.

This is what moves us from average evaluation to responsible evaluation.

---

## Common Misunderstandings

- **"Bias means the developer intended harm."**
  In practice, bias is often structural and data-driven.

- **"High accuracy implies fairness."**
  Averages can hide serious subgroup disparities.

- **"Fairness is outside the engineering process."**
  Fairness must be considered in data collection, modeling, evaluation, and deployment.

---

## Summary and Exam-Ready Takeaways

- Bias in AI means systematic differences in behavior across groups.
- Unfairness is often caused by data, labels, proxies, or deployment context.
- Historical, representation, measurement, and deployment bias are all important sources.
- Accuracy and fairness are different because aggregate performance can hide unequal harm.
- Fairness must be measured directly and treated as a first-class quality criterion.

---

## Bridge to the Next Note

If fairness cannot be assumed from accuracy, the next question is obvious:

**How do we measure fairness in practice?**
