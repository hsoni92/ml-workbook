# Mitigation Strategies for Responsible AI - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. **Explain** where bias mitigation can occur in the ML lifecycle.
2. **Compare** pre-processing, in-processing, and post-processing approaches.
3. **Recognize** why fairness mitigation always involves trade-offs and ongoing monitoring.

---

## Why This Topic Matters

Detecting unfairness is not enough.

Once a disparity is found, we need to decide:

**What intervention is possible, and at what stage should we apply it?**

This is the purpose of bias mitigation.

Responsible AI is not only about measuring problems. It is also about taking deliberate action to reduce them.

---

## Three Places to Intervene

Bias mitigation can happen:

1. **Before training**
2. **During training**
3. **After prediction**

These correspond to three standard categories:

| Stage | Main idea | Example techniques |
|---|---|---|
| **Pre-processing** | Modify the data before the model learns from it | Reweighting, resampling, label correction |
| **In-processing** | Modify the learning objective or training procedure | Fairness constraints, adversarial debiasing |
| **Post-processing** | Adjust decisions after the model predicts | Threshold changes, calibration-based adjustments |

---

## Pre-Processing Strategies

Pre-processing tries to reduce bias before model training begins.

Common examples:

- rebalance underrepresented groups through resampling,
- reweight examples so underrepresented groups count more,
- correct biased labels if historical decisions were unfair.

This approach is attractive because it addresses the problem early. However, it may also change the effective training distribution, so we must be careful not to create unrealistic data or hide important task structure.

---

## In-Processing Strategies

In-processing changes the training procedure itself.

Examples:

- add a fairness penalty to the loss function,
- penalize large differences in error rates across groups,
- use adversarial debiasing so the model learns useful task information while making it harder to infer protected attributes from internal representations.

This approach is often powerful because fairness goals are built into the optimization process itself. The trade-off is that training becomes more complex.

---

## Post-Processing Strategies

Post-processing acts after the model has already produced scores or labels.

Example:

- use different decision thresholds to reduce disparities such as unequal false negative rates.

This can be the easiest approach operationally because it does not require retraining the full model. However, it may raise concerns about:

- transparency,
- policy justification,
- legal acceptability in some settings.

---

## Why Trade-Offs Are Unavoidable

One of the most important lessons in responsible AI is that mitigation is not purely a technical optimization problem.

Improving fairness may:

- reduce overall accuracy,
- improve outcomes for one group while affecting another,
- satisfy one fairness notion but not another.

So mitigation always depends on:

- application context,
- domain risk,
- stakeholder priorities,
- legal and policy constraints.

There is no universal fix.

---

## A Good Practical Workflow

A responsible mitigation workflow looks like this:

1. Detect and quantify disparities.
2. Decide which fairness goal matters most.
3. Choose an intervention stage: pre-, in-, or post-processing.
4. Re-evaluate both utility and fairness metrics.
5. Document the trade-offs and reasoning.
6. Continue monitoring after deployment.

This last step is essential because fairness can drift as the population, environment, or product usage changes.

---

## Common Misunderstandings

- **"One mitigation method solves every fairness problem."**
  Different bias sources require different interventions.

- **"Fairness mitigation is purely technical."**
  It also involves value judgments and institutional priorities.

- **"After mitigation, the system is permanently fair."**
  Fairness can change over time, so monitoring remains necessary.

---

## Summary and Exam-Ready Takeaways

- Bias mitigation can happen before training, during training, or after prediction.
- Pre-processing changes the data, in-processing changes learning, and post-processing changes decisions.
- Each stage has strengths and limitations.
- Fairness interventions often involve trade-offs with performance or with other fairness goals.
- Responsible AI requires explicit decisions, documentation, and ongoing monitoring rather than one-time fixes.

---

## Bridge to the Next Note

The module now shifts from responsible deployment concerns to modern architecture trends.

We begin with one of the biggest changes in AI systems:

**Why did transformers become the dominant modern architecture?**
