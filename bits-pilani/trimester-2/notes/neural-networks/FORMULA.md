# Neural Networks Formula Sheet (Numericals Focus)

Use this as a quick solve sheet. Symbols: number of samples $n$, input dimension $d$, layer index $l$, neurons in layer $l$ as $n^{[l]}$, weights $W^{[l]}$, biases $b^{[l]}$.

## 1) Single neuron and common activations

- Linear pre-activation: $z=w^\top x+b$
- Neuron output: $a=g(z)$
- Sigmoid: $\sigma(z)=\frac{1}{1+e^{-z}}$
- Sigmoid derivative: $\sigma'(z)=\sigma(z)\left(1-\sigma(z)\right)$
- Tanh: $\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}$
- Tanh derivative: $\frac{d}{dz}\tanh(z)=1-\tanh^2(z)$
- ReLU: $\mathrm{ReLU}(z)=\max(0,z)$
- ReLU derivative: $\mathrm{ReLU}'(z)=\begin{cases}1,&z>0\\0,&z\le 0\end{cases}$
- Leaky ReLU: $g(z)=\max(\alpha z,z)$
- Leaky ReLU derivative: $g'(z)=\begin{cases}1,&z>0\\\alpha,&z\le 0\end{cases}$

## 2) Forward propagation (deep network)

- Layer equations: $z^{[l]}=W^{[l]}a^{[l-1]}+b^{[l]}$, $a^{[l]}=g^{[l]}(z^{[l]})$
- Input layer activation: $a^{[0]}=x$
- Output for binary classifier: $\hat{y}=a^{[L]}=\sigma(z^{[L]})$
- Batch form (columns are samples): $Z^{[l]}=W^{[l]}A^{[l-1]}+b^{[l]}$

## 3) Loss functions

- Binary cross-entropy (single sample): $\mathcal{L}=-\left[y\log(\hat{y})+(1-y)\log(1-\hat{y})\right]$
- Binary cross-entropy (dataset): $J=\frac{1}{n}\sum_{i=1}^{n}\mathcal{L}^{(i)}$
- Mean squared error (regression): $J=\frac{1}{n}\sum_{i=1}^{n}\left(y_i-\hat{y}_i\right)^2$
- Categorical cross-entropy: $J=-\frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{K}y_{ik}\log(\hat{y}_{ik})$

## 4) Softmax output layer

- Softmax probability: $\hat{y}_k=\frac{e^{z_k}}{\sum_{j=1}^{K}e^{z_j}}$
- Stable softmax trick: use $z'_k=z_k-\max_j z_j$ before exponentials
- For softmax + cross-entropy: $\frac{\partial \mathcal{L}}{\partial z_k}=\hat{y}_k-y_k$

## 5) Backpropagation core equations

- Output layer error (binary sigmoid + BCE): $dZ^{[L]}=A^{[L]}-Y$
- General chain step: $dZ^{[l]}=dA^{[l]}\odot g'^{[l]}(Z^{[l]})$
- Weight gradient: $dW^{[l]}=\frac{1}{n}dZ^{[l]}(A^{[l-1]})^\top$
- Bias gradient: $db^{[l]}=\frac{1}{n}\sum_{i=1}^{n}dZ^{[l](i)}$
- Propagate to previous layer: $dA^{[l-1]}=(W^{[l]})^\top dZ^{[l]}$

## 6) Gradient descent updates

- Parameter update: $W^{[l]}\leftarrow W^{[l]}-\eta\, dW^{[l]}$
- Bias update: $b^{[l]}\leftarrow b^{[l]}-\eta\, db^{[l]}$
- Learning rate symbol: $\eta$ (or $\alpha$)

## 7) Mini-batch training

- Number of batches (size $m$): $\left\lceil\frac{n}{m}\right\rceil$
- Batch gradient estimate: average gradient over only the mini-batch
- Epoch: one complete pass over all training samples

## 8) Regularization

### L2 regularization (weight decay)

- Regularized cost: $J_{\mathrm{reg}}=J+\frac{\lambda}{2n}\sum_l \|W^{[l]}\|_F^2$
- Gradient with L2: $dW^{[l]}\leftarrow dW^{[l]}+\frac{\lambda}{n}W^{[l]}$
- Update with L2: $W^{[l]}\leftarrow\left(1-\eta\frac{\lambda}{n}\right)W^{[l]}-\eta\, dW^{[l]}$

### Dropout (inverted dropout)

- Apply mask: $A^{[l]}\leftarrow A^{[l]}\odot D^{[l]}$
- Scale at train time: $A^{[l]}\leftarrow \frac{A^{[l]}}{p_{\mathrm{keep}}}$
- During inference: no dropout mask

## 9) Weight initialization

- Xavier/Glorot (tanh/sigmoid): $\mathrm{Var}(W)\approx\frac{1}{n_{\mathrm{in}}}$ (or $\frac{2}{n_{\mathrm{in}}+n_{\mathrm{out}}}$)
- He initialization (ReLU): $\mathrm{Var}(W)\approx\frac{2}{n_{\mathrm{in}}}$
- Practical sampling (He): $W\sim\mathcal{N}\left(0,\frac{2}{n_{\mathrm{in}}}\right)$

## 10) Optimization variants

### Momentum

- Velocity: $v_t=\beta v_{t-1}+(1-\beta)g_t$
- Update: $\theta_t=\theta_{t-1}-\eta v_t$

### RMSProp

- Squared-grad average: $s_t=\beta s_{t-1}+(1-\beta)g_t^2$
- Update: $\theta_t=\theta_{t-1}-\eta\frac{g_t}{\sqrt{s_t}+\epsilon}$

### Adam

- First moment: $m_t=\beta_1 m_{t-1}+(1-\beta_1)g_t$
- Second moment: $v_t=\beta_2 v_{t-1}+(1-\beta_2)g_t^2$
- Bias correction: $\hat{m}_t=\frac{m_t}{1-\beta_1^t}$, $\hat{v}_t=\frac{v_t}{1-\beta_2^t}$
- Update: $\theta_t=\theta_{t-1}-\eta\frac{\hat{m}_t}{\sqrt{\hat{v}_t}+\epsilon}$

## 11) Batch normalization (training)

- Batch mean: $\mu_B=\frac{1}{m}\sum_{i=1}^{m}x_i$
- Batch variance: $\sigma_B^2=\frac{1}{m}\sum_{i=1}^{m}(x_i-\mu_B)^2$
- Normalize: $\hat{x}_i=\frac{x_i-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}$
- Scale and shift: $y_i=\gamma \hat{x}_i+\beta$

## 12) Evaluation metrics (classification)

- Accuracy: $\frac{TP+TN}{TP+TN+FP+FN}$
- Precision: $\frac{TP}{TP+FP}$
- Recall: $\frac{TP}{TP+FN}$
- F1-score: $\frac{2\cdot\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Precision}+\mathrm{Recall}}$

## 13) Parameter count (quick exam formula)

- Dense layer parameters from $n_{\mathrm{in}}$ to $n_{\mathrm{out}}$: $n_{\mathrm{out}}(n_{\mathrm{in}}+1)$
- Total network parameters: sum over all layers

## 14) Numerical stability and useful identities

- Log-sum-exp identity: $\log\sum_j e^{z_j}=c+\log\sum_j e^{z_j-c}$, choose $c=\max_j z_j$
- BCE clipping trick: clamp $\hat{y}\in[\epsilon,1-\epsilon]$ before $\log$
- Derivative of BCE with sigmoid output simplifies to: $dZ=\hat{y}-y$

## 15) Quick checklist before solving

- Write dimensions of $W^{[l]}$, $b^{[l]}$, $A^{[l]}$ first to avoid shape mistakes.
- In backprop, move right-to-left: $dZ \rightarrow dW,db \rightarrow dA_{\text{prev}}$.
- For multiclass classification, use softmax + categorical cross-entropy.
- For ReLU networks, prefer He initialization.
- If loss diverges, check learning rate, feature scaling, and initialization.
