# Model Question Paper – Artificial Neural Networks (Practice Set)

**Time:** 2 hours
**Maximum marks:** 40

---

## Question 1 (5 + 5 marks)

### (a)

A dataset is not linearly separable.

- Explain why a single-layer perceptron fails in this case.
- How does introducing a hidden layer with non-linear activation solve this problem?

#### Answer

**Why a single-layer perceptron fails**

A single-layer perceptron (without a hidden layer) learns a **linear decision boundary**: it computes a weighted sum of inputs plus bias and applies a step or sign activation. Geometrically, it can only separate classes with a **hyperplane**. If the dataset is **not linearly separable** (for example XOR, or concentric clusters), **no single hyperplane** achieves zero training error. The perceptron convergence proof assumes linear separability; otherwise learning stalls or cycles.

**How a hidden layer with non-linear activation helps**

With one or more **hidden layers** and **non-linear activations** (sigmoid, tanh, ReLU, etc.), the network computes **compositions of non-linear functions**. That yields **non-linear decision boundaries** (curves, unions of regions) in input space. Intuitively, hidden units can detect **intermediate features** (for example “A and not B”), which a single linear separator cannot represent. Universal approximation results (for bounded width/depth under mild conditions) formalize that such networks can approximate complex functions, including those needed for non-linearly separable tasks.

### (b)

Consider a neuron with ReLU activation.

- Under what conditions does the neuron output become zero?
- Explain the “dying ReLU” problem and how it affects training.

#### Answer

**When the output is zero**

ReLU is $f(z) = \max(0, z)$ for pre-activation $z$. The neuron output is **zero when $z \leq 0$** (strictly, zero for $z < 0$ and also zero at $z = 0$ in the usual definition). So large negative weights, negative inputs, or a very negative bias can shut the unit off.

**Dying ReLU**

If a unit’s pre-activations are **consistently negative** (for example bad initialization, too aggressive learning rate, or bad data scale), the ReLU output stays **0**. The gradient of ReLU with respect to $z$ is **0 for $z < 0$**, so **no gradient flows backward** through that unit: weights feeding it **stop updating**. Many units can become permanently inactive, **shrinking effective capacity** and **slowing or stalling** training.

**Effect on training:** The network may underfit, converge slowly, or require restarts. Mitigations include better initialization (for example He init for ReLU nets), smaller learning rate, batch normalization, leaky ReLU / ELU, or monitoring dead units.

---

## Question 2 (6 + 4 marks)

### (a)

Explain the difference between:

- Underfitting
- Good fit
- Overfitting

Use bias–variance intuition in your explanation.

#### Answer

**Bias** measures how wrong the model class is on average even with infinite data (systematic error). **Variance** measures sensitivity to the particular training sample (spread of predictions across different training draws).

- **Underfitting:** **High bias**, often **low variance**. The model is too simple (or over-regularized) to capture the signal. Training and validation errors are **both high** and often **close**. Adding capacity or reducing excessive regularization helps.

- **Good fit:** **Low bias** and **moderate variance** in balance. The model captures real patterns without chasing noise. Training error is **low**; validation error is **near** training error and acceptable for the task.

- **Overfitting:** **Low bias**, **high variance**. The model fits **noise** and idiosyncrasies of the training set. **Training error is low** but **validation error is much higher** (large generalization gap). Remedies include more data, regularization, dropout, early stopping, or simpler architecture.

### (b)

Compare the following weight initialization strategies:

- Random initialization
- Xavier/Glorot initialization (intuitive explanation only)

How do better initialization methods improve training?

#### Answer

**Random initialization**

Weights are drawn from a simple distribution (for example uniform or Gaussian with fixed scale). If the scale is **too large**, activations and gradients can **explode** layer by layer. If **too small**, signals **shrink** and gradients **vanish** in deep networks. Training becomes **slow, unstable, or stuck** in poor regions.

**Xavier / Glorot initialization (intuitive idea)**

For sigmoid/tanh-like activations, Xavier scales initial weights using **fan-in** and/or **fan-out** of the layer so that, at the start of training, **activations and gradients** neither systematically grow nor shrink across layers—roughly **preserving variance** through forward and backward passes. (He initialization is the analogous idea tuned for ReLU.)

**How better initialization helps**

It places weights in a regime where **gradients flow** and **activations stay in useful ranges**, so optimization **starts in a viable basin**. That typically yields **faster convergence**, **more stable training**, and less need for ad hoc fixes compared with poorly scaled random init.

---

## Question 3 (6 + 4 marks)

### (a)

Explain how gradient descent behaves differently under:

- Very high learning rate
- Very low learning rate

What practical issues arise in both cases?

#### Answer

**Very high learning rate**

Updates $\theta \leftarrow \theta - \eta \nabla L$ are **large**. The optimizer can **oscillate** across a valley, **overshoot** minima, or **diverge** (loss explodes). Training loss may **jump erratically** or become NaN. In practice you see unstable metrics and poor final performance unless you reduce $\eta$, clip gradients, or use adaptive methods.

**Very low learning rate**

Steps are **tiny**. Convergence is **very slow**; training may **stall** in flat regions or **plateau** for long periods. You may also get stuck in **sharp but suboptimal** areas if escape requires larger moves. Wall-clock cost rises and you may stop early before reaching a good solution.

**Practical issues**

- High $\eta$: instability, divergence, wasted runs.
- Low $\eta$: long training times, under-trained models, sensitivity to stopping criteria.

Common responses: **learning rate schedules**, **warmup**, **grid search** for $\eta$, and optimizers that adapt step sizes per parameter.

### (b)

Compare any two optimization methods.

#### Answer

Compare **SGD with momentum** and **Adam**.

**SGD with momentum**

- Update maintains a **velocity** vector: exponentially averaged past gradients smooth the path and help escape shallow local minima and damp oscillations in ravines.
- **One learning rate** (and momentum hyperparameter) for all parameters; no per-parameter adaptive scaling.
- **Memory:** stores velocity, same size as parameters.
- **When used:** large-batch training, computer vision baselines, when you want simplicity and well-understood behavior.

**Adam (Adaptive Moment Estimation)**

- Maintains **per-parameter** estimates of **first moment** (mean gradient) and **second moment** (variance), with bias correction; effectively **adapts step sizes** per weight.
- Often **works well with default hyperparameters** on diverse problems; **fast early progress**.
- **Memory:** roughly **two** extra vectors per parameter (moments).
- **When used:** default choice for many deep learning experiments; can sometimes **generalize slightly worse** than tuned SGD on some tasks unless regularization or schedules are adjusted.

**Contrast:** Momentum improves raw SGD directionally but uses a **global** step scale; Adam **adapts** each parameter’s step using gradient statistics, often reducing manual $\eta$ tuning at the cost of extra state and different generalization trade-offs.

---

## Question 4 (5 + 5 marks)

### (a)

Discuss the key hyperparameters that are crucial for neural network training. Elaborate on how you will find the right set of hyperparameters while training your model.

#### Answer

**Important hyperparameters**

- **Learning rate** and **schedule** (constant, step decay, cosine, warmup): strongest lever on stability and speed.
- **Batch size:** affects noise in gradients, wall time, and sometimes generalization.
- **Network capacity:** number of layers, units per layer, choice of activation.
- **Regularization:** L2 weight decay, dropout rate, label smoothing.
- **Training length:** number of epochs with **early stopping** on a validation set.
- **Optimizer-specific:** momentum, $\beta_1/\beta_2$ for Adam, etc.

**Finding a good set**

1. **Baseline:** reasonable architecture, default optimizer, mid-range batch size.
2. **Tune learning rate** first (wide search, few epochs), using validation loss.
3. **Random or Bayesian search** over a modest grid for depth/width, dropout, weight decay (more efficient than exhaustive grid for many knobs).
4. **Monitor** train vs validation curves: gap indicates overfitting; both high indicates underfitting.
5. **Early stopping** to cap epochs and reduce overfitting cost.
6. Optionally **nested** validation or a held-out **test** set used **once** for final reporting.

Document chosen values and seed for reproducibility.

### (b)

Explain the different gates present in LSTM and how they help address the problems faced with RNNs.

#### Answer

**Problems with vanilla RNNs**

Long sequences suffer **vanishing or exploding gradients** when backpropagating through time, so the model **struggles to retain information** over many steps. Short-term memory dominates; **long-range dependencies** are hard to learn.

**LSTM core idea**

An LSTM cell maintains a **cell state** $c_t$ (slow highway) and a **hidden state** $h_t$. **Gated** multiplicative units control what to forget, store, and expose.

**Gates (typical naming)**

1. **Forget gate** $f_t$: decides **what to erase** from the cell state (outputs values in $(0,1)$ via sigmoid, elementwise multiply with $c_{t-1}$).
2. **Input gate** $i_t$ (and candidate $\tilde{c}_t$): decides **what new information** to **write** into the cell state.
3. **Output gate** $o_t$: decides **what part of the cell state** becomes the **hidden output** $h_t$ after tanh squashing.

(Some formulations also describe **input** as combining gate + candidate; the exam expects the roles: forget, input/update, output.)

**Why this helps**

Multiplicative gates allow **additive updates** to $c_t$ along a path where gradients can **flow more steadily** (constant error carousel intuition), mitigating vanishing gradients compared with naive RNN recurrence. The network can **selectively remember** or **discard** information over long horizons, improving modeling of long-range structure in sequences.
