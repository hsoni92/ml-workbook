# Uncertainty: Softmax Entropy and Multi-class Probabilities - Artificial Neural Networks

## Learning Objectives

By the end of this note, you should be able to:

1. Distinguish between **confidence** and **uncertainty**.
2. Read multi-class **softmax probability vectors** meaningfully.
3. Explain how **entropy** acts as an uncertainty signal.
4. State what entropy can and cannot tell us about model trustworthiness.

---

## Why Multi-Class Outputs Need Interpretation

Neural networks do not just output labels. They often output a **probability distribution across classes**.

That distribution contains richer information than the final predicted class alone.

For example, these two predictions are very different even if both choose the same class:

- one may put almost all probability on one class,
- another may split probability across several plausible classes.

So to evaluate trust properly, we need to read the full output distribution.

---

## Confidence vs Uncertainty

- **Confidence** usually refers to the **largest predicted class probability**.
- **Uncertainty** refers to how **spread out** the probability mass is across classes.

These are related but not identical ideas.

A model can have:

- high confidence and low uncertainty,
- moderate confidence and moderate uncertainty,
- or, in some cases, misleading confidence that does not match reality.

---

## Reading Multi-Class Probability Vectors

| Probability Vector | Entropy Level | Interpretation |
| --- | --- | --- |
| `[0.97, 0.01, 0.01, 0.01]` | Low | Model is strongly concentrated on one class |
| `[0.40, 0.35, 0.20, 0.05]` | Medium | Model sees some ambiguity between top classes |
| `[0.26, 0.25, 0.24, 0.25]` | High | Model is highly uncertain |

The broader the distribution, the less decisive the model is.

---

## Entropy as an Uncertainty Measure

**Entropy** summarizes how spread out the class probabilities are.

- **Low entropy** means the distribution is concentrated, so the model appears more certain.
- **High entropy** means the distribution is spread out, so the model appears more uncertain.

This makes entropy useful for:

- ranking samples by uncertainty,
- flagging cases for human review,
- building abstain or fallback systems.

```text
Get softmax probabilities
-> compute entropy for each sample
-> compare entropy across predictions
-> use high-entropy samples as uncertainty flags
```

---

## Demo Insight from the Transcript

The transcript uses a **four-class classification** example and reports:

- baseline accuracy of about **86%**,
- average entropy for **correct predictions** around **0.17**,
- average entropy for **incorrect predictions** around **0.49**.

This supports the intuition that incorrect predictions are often more uncertain on average.

But notice the wording carefully: **often**, not **always**.

---

## What Entropy Can Tell Us

- whether a prediction distribution is concentrated or spread out,
- which samples look more ambiguous,
- where manual review may be useful.

Entropy is therefore a practical first-pass uncertainty signal.

---

## What Entropy Cannot Guarantee

Entropy is helpful, but it is not magical.

| Question | Can Entropy Answer It Reliably? | Why |
| --- | --- | --- |
| Is the model uncertain on many difficult samples? | Often yes | Spread-out probabilities reveal ambiguity |
| Does low entropy guarantee correctness? | No | A model can still be confidently wrong |
| Can entropy replace calibration analysis? | No | Calibration and uncertainty are related but different |

So entropy should be treated as a **signal**, not as proof.

---

## Practical Use

In real systems, uncertainty estimates are useful for:

- routing uncertain cases to a human,
- identifying ambiguous inputs,
- monitoring whether a model is under stress on new data,
- complementing calibration and robustness analysis.

This is especially important when fully automated decisions would be risky.

---

## Summary and Exam-Ready Takeaways

- Neural networks output **probability distributions**, not just labels.
- **Confidence** and **uncertainty** are related but different concepts.
- **Entropy** provides a compact uncertainty signal: lower entropy means more concentrated probabilities, higher entropy means more spread.
- Incorrect predictions often show **higher entropy on average**, but entropy does not guarantee correctness.
- Entropy should be used together with **calibration** and other evaluation tools.

**Bridge to next topic:** This completes the major evaluation dimensions in the module. The final note ties them together into one **holistic evaluation framework**.
