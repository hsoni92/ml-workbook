# A Systematic Experimentation Workflow - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Describe** a complete workflow for training neural networks in a disciplined way.
2. **Explain** why a baseline model is required before tuning begins.
3. **Distinguish** the roles of validation and test evaluation in the workflow.
4. **Argue** why structured experimentation is an engineering necessity, not optional process overhead.

---

## Why Workflow Matters

This lecture brings the full module together. The point is no longer to discuss isolated concepts such as learning rate or batch size separately. The point is to understand how model development is done **professionally**.

Deep learning systems are:

- highly stochastic,
- highly sensitive to hyperparameters,
- and often expensive to train.

Because of that, training once and getting a good result is not enough. What matters is building a **process** that can reliably produce, compare, and justify good models.

---

## The End-to-End Workflow

The module's professional workflow can be summarized as:

`define the problem and metric -> build a baseline -> decide what to tune -> run controlled experiments -> track metrics and checkpoints -> choose by validation -> evaluate once on the test set`

This is the main operational story of Week 12.

---

## Step-by-Step Breakdown

| Step | Main Question | Why It Matters |
|---|---|---|
| **Problem definition** | What task are we solving, on what data, and with which metric? | Without this, tuning has no clear target |
| **Baseline model** | What simple reproducible model can serve as a reference? | Establishes whether the pipeline works and what "improvement" means |
| **Tuning plan** | Which hyperparameters matter and what ranges should be explored? | Prevents random, unstructured search |
| **Controlled execution** | Are runs using fixed conditions and proper tracking? | Makes comparisons fair and reproducible |
| **Model selection** | Which model performs best on validation data? | Selects the strongest candidate without using the test set |
| **Final evaluation** | How does the chosen model perform on the test set? | Provides an unbiased estimate of generalization |

---

## Why the Baseline Comes First

The transcript strongly emphasizes the baseline.

A baseline is necessary because it:

- tells you whether the pipeline works at all,
- gives you a reference point,
- and prevents you from mistaking random fluctuation for real improvement.

Without a baseline, even a "better" result is hard to interpret because there is no stable starting comparison.

---

## What Usually Fails in Real Projects

The lecture explicitly says that controlled execution is where many projects fail.

Typical reasons include:

- no fixed seeds,
- no tracked hyperparameters,
- no saved checkpoints,
- unclear metrics,
- or many uncontrolled changes happening at once.

When that happens, experiments may still produce numbers, but those numbers are hard to trust.

---

## Validation vs Test Set

This distinction is one of the most important ideas in the workflow.

### Validation set

Used during experimentation for:

- comparing runs,
- selecting hyperparameters,
- and choosing the best model candidate.

### Test set

Used only at the end for:

- one final, unbiased estimate of real-world performance.

This separation matters because repeated tuning on the test set leaks information and can make the final estimate overly optimistic.

---

## What Should Be Tracked During the Workflow

The lecture calls for controlled experimentation, which implies keeping track of:

- hyperparameter settings,
- validation performance,
- saved checkpoints,
- and other run metadata needed to compare experiments later.

In practice, this turns model development from a vague process into an auditable one.

---

## Exam-Ready Narrative

If asked to describe a professional experimentation workflow, a strong answer should include:

1. a clearly defined problem and evaluation metric,
2. a simple baseline,
3. a planned hyperparameter search,
4. controlled and reproducible experimentation,
5. validation-based model selection,
6. and a single final test evaluation.

That sequence shows both technical understanding and process discipline.

---

## Common Mistakes

- Beginning tuning before defining the success metric.
- Skipping the baseline model.
- Using the test set for repeated comparison.
- Failing to track experiment settings and artifacts.
- Changing multiple factors together and then drawing strong conclusions.

---

## Summary

- Strong models come from **structured experimentation**, not isolated lucky runs.
- The baseline, validation protocol, reproducibility controls, and final test evaluation each serve a different purpose.
- Workflow discipline is part of good ML engineering, not administrative overhead.

**Bridge to the next note:** the module summary pulls these ideas together into one exam-ready picture of hyperparameter tuning, reproducibility, and disciplined experimentation.
