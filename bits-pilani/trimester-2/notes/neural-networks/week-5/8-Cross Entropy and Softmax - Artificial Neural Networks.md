# Cross Entropy and Softmax – Artificial Neural Networks (Module 5)

## Learning Objectives

By the end of this video you will:

1. **Explain** why **MSE** is not suitable for classification.
2. **Recall** the **softmax** function and its role.
3. **Define** **cross-entropy** loss and how it measures quality of predicted probabilities.
4. **See** how **softmax + cross-entropy** together form the standard loss for classification.

---

## Why MSE Fails for Classification

1. **Wrong geometry:** MSE treats class labels as numbers on a line (0, 1, 2…). Class 2 is not “twice” class 1; there is no natural distance between classes → wrong decision boundaries.
2. **Weak penalty for confident mistakes:** Predicting 0.2 vs 0.01 for the true class gives similar MSE. We need **strong** feedback when the model is **confidently wrong**.
3. **Vanishing gradients with sigmoid/softmax:** Near 0 or 1, derivatives are tiny. When the model is confidently wrong, MSE sends **almost no** corrective signal → very slow learning. Example: $y = 1$, $\hat{y} = 0.99$ ⇒ MSE $= (1 - 0.99)^2 = 0.0001$ — too small.

---

## From Logits to Probabilities

- For classification we need a **probability distribution** over classes.
- The network outputs **raw scores** (logits): can be positive/negative, do not sum to 1.
- **Softmax** converts logits to probabilities: exponentiate each logit and normalize by the sum. Outputs are **positive** and **sum to 1** → valid probability distribution. Larger logit ⇒ larger probability.

---

## Cross-Entropy Loss

- For the **true** class $y$, cross-entropy is: $-\log(p_y)$, where $p_y$ is the predicted probability for class $y$.
- It measures how “surprised” the model is that the true class occurred.
- **High** probability for correct class → **small** loss; **low** probability → **large** loss.
- Example (true class = cat): 90% for cat → loss ≈ 0.1; 50% → larger loss; 1% (confidently wrong) → loss &gt; 4.6. So cross-entropy **strongly** penalizes confident mistakes.

---

## Softmax + Cross-Entropy in Practice

- We do **not** compute softmax and then take log separately.
- We use a **single combined** expression: $\mathcal{L} = -z_y + \log \sum_j e^{z_j}$.
- This avoids extra computation and is **numerically stable**. Frameworks (PyTorch, TensorFlow) implement this combined form when you call “cross-entropy loss”; it **includes** softmax.

---

## Why Softmax + Cross-Entropy Is Standard

- Produces **strong**, well-shaped gradients.
- Pushes the network to assign **high** probability to the correct class.
- **Heavily** penalizes confident mistakes.
- Scales naturally to **multi-class** problems.
- Trains **faster** and more **reliably** than MSE for classification. Used in CNNs, RNNs, transformers, and almost every modern classifier.

---

## Summary

- **MSE** fails for classification: wrong geometry, weak penalties, vanishing gradients with sigmoid/softmax.
- **Softmax** turns logits into probabilities.
- **Cross-entropy** measures how well those probabilities match the true class.
- The **combined** softmax + cross-entropy formulation is the standard loss for classification; libraries implement the stable version internally.
