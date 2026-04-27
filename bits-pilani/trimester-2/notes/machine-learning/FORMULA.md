# Machine Learning Formula Sheet (Numericals Focus)

Use this as a quick solve sheet. Symbols: number of samples $n$, number of features $d$, true value $y_i$, prediction $\hat{y}_i$.

## 1) Basic statistics

- Mean: $\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$
- Weighted mean: $\bar{x}_w=\frac{\sum_i w_i x_i}{\sum_i w_i}$
- Variance (population): $\sigma^2=\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2$
- Variance (sample): $s^2=\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2$
- Standard deviation: $\sigma=\sqrt{\sigma^2}$
- Covariance: $\mathrm{Cov}(X,Y)=\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})$
- Correlation: $r=\frac{\mathrm{Cov}(X,Y)}{\sigma_X\sigma_Y}$
- Z-score normalization: $z=\frac{x-\mu}{\sigma}$
- Min-max normalization to $[0,1]$: $x'=\frac{x-x_{\min}}{x_{\max}-x_{\min}}$

## 2) Train/test and model error

- Residual: $e_i=y_i-\hat{y}_i$
- Sum of Squared Errors (SSE): $\mathrm{SSE}=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$
- Mean Squared Error (MSE): $\mathrm{MSE}=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2$
- Root MSE: $\mathrm{RMSE}=\sqrt{\mathrm{MSE}}$
- Mean Absolute Error (MAE): $\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|$
- Coefficient of determination: $R^2=1-\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}{\sum_{i=1}^{n}(y_i-\bar{y})^2}$

## 3) Linear regression

- Hypothesis (single feature): $\hat{y}=\beta_0+\beta_1x$
- Hypothesis (multiple features): $\hat{y}=\beta_0+\sum_{j=1}^{d}\beta_jx_j$
- Slope (simple linear regression): $\beta_1=\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^{n}(x_i-\bar{x})^2}$
- Intercept (simple linear regression): $\beta_0=\bar{y}-\beta_1\bar{x}$
- Cost function: $J(\beta)=\frac{1}{2n}\sum_{i=1}^{n}(\hat{y}_i-y_i)^2$
- Gradient descent update (each parameter): $\beta_j\leftarrow\beta_j-\alpha\frac{\partial J}{\partial \beta_j}$
- For linear regression gradient: $\frac{\partial J}{\partial \beta_j}=\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)x_{ij}$
- Vector form (normal equation): $\beta=(X^\top X)^{-1}X^\top y$

## 4) Logistic regression and classification

- Sigmoid: $\sigma(z)=\frac{1}{1+e^{-z}}$
- Logistic model: $p(y=1\mid x)=\sigma(\beta_0+\beta^\top x)$
- Decision rule (default): predict class 1 if $p\ge 0.5$
- Binary cross-entropy loss: $\mathcal{L}=-\frac{1}{n}\sum_{i=1}^{n}\left[y_i\log(\hat{p}_i)+(1-y_i)\log(1-\hat{p}_i)\right]$

## 5) Confusion matrix metrics

- Accuracy: $\frac{TP+TN}{TP+TN+FP+FN}$
- Error rate: $\frac{FP+FN}{TP+TN+FP+FN}=1-\mathrm{Accuracy}$
- Precision: $\frac{TP}{TP+FP}$
- Recall / Sensitivity / TPR: $\frac{TP}{TP+FN}$
- Specificity / TNR: $\frac{TN}{TN+FP}$
- FPR: $\frac{FP}{FP+TN}=1-\mathrm{Specificity}$
- FNR: $\frac{FN}{FN+TP}=1-\mathrm{Recall}$
- F1-score: $\frac{2\cdot\mathrm{Precision}\cdot\mathrm{Recall}}{\mathrm{Precision}+\mathrm{Recall}}$

## 6) Decision trees

- Entropy of node $S$: $H(S)=-\sum_{k=1}^{c}p_k\log_2 p_k$
- Information gain for split by attribute $A$: $\mathrm{IG}(S,A)=H(S)-\sum_{v\in \mathrm{Values}(A)}\frac{|S_v|}{|S|}H(S_v)$
- Gini impurity: $\mathrm{Gini}(S)=1-\sum_{k=1}^{c}p_k^2$
- Misclassification impurity: $1-\max_k(p_k)$
- Weighted impurity after split: $\sum_v\frac{|S_v|}{|S|}\mathrm{Impurity}(S_v)$

## 7) k-Nearest Neighbors (kNN)

- Euclidean distance: $d(x,y)=\sqrt{\sum_{j=1}^{d}(x_j-y_j)^2}$
- Manhattan distance: $d(x,y)=\sum_{j=1}^{d}|x_j-y_j|$
- Minkowski distance: $d(x,y)=\left(\sum_{j=1}^{d}|x_j-y_j|^p\right)^{1/p}$
- Classification prediction: majority class among $k$ nearest points
- Regression prediction (uniform): $\hat{y}=\frac{1}{k}\sum_{i\in N_k(x)}y_i$
- Distance-weighted regression: $\hat{y}=\frac{\sum_{i\in N_k(x)}w_i y_i}{\sum_{i\in N_k(x)}w_i}$, often $w_i=\frac{1}{d_i+\epsilon}$

## 8) Clustering

### k-means

- Assignment step: assign point $x_i$ to cluster with nearest centroid
- Centroid update: $\mu_k=\frac{1}{|C_k|}\sum_{x_i\in C_k}x_i$
- Objective (WCSS / inertia): $J=\sum_{k=1}^{K}\sum_{x_i\in C_k}\|x_i-\mu_k\|^2$

### Hierarchical clustering (linkage distances)

- Single linkage: $d(A,B)=\min_{a\in A,b\in B}d(a,b)$
- Complete linkage: $d(A,B)=\max_{a\in A,b\in B}d(a,b)$
- Average linkage: $d(A,B)=\frac{1}{|A||B|}\sum_{a\in A}\sum_{b\in B}d(a,b)$

### DBSCAN

- Core point condition: $|N_\varepsilon(p)|\ge \mathrm{minPts}$
- $\varepsilon$-neighborhood: $N_\varepsilon(p)=\{q\mid d(p,q)\le \varepsilon\}$

## 9) Association rule mining

- Support of itemset $X$: $\mathrm{supp}(X)=\frac{\sigma(X)}{N}$
- Support count: $\sigma(X)=\#\{\text{transactions containing }X\}$
- Rule support: $\mathrm{supp}(X\Rightarrow Y)=\mathrm{supp}(X\cup Y)$
- Confidence: $\mathrm{conf}(X\Rightarrow Y)=\frac{\mathrm{supp}(X\cup Y)}{\mathrm{supp}(X)}$
- Lift: $\mathrm{lift}(X\Rightarrow Y)=\frac{\mathrm{supp}(X\cup Y)}{\mathrm{supp}(X)\mathrm{supp}(Y)}$
- Leverage: $\mathrm{lev}(X\Rightarrow Y)=\mathrm{supp}(X\cup Y)-\mathrm{supp}(X)\mathrm{supp}(Y)$

## 10) Dimensionality reduction (PCA basics)

- Data centering: $x_i'=x_i-\bar{x}$
- Covariance matrix (centered data): $\Sigma=\frac{1}{n-1}X^\top X$
- Eigen decomposition: $\Sigma v_j=\lambda_j v_j$
- Project onto first $m$ principal components: $z_i=V_m^\top x_i'$
- Explained variance ratio of component $j$: $\frac{\lambda_j}{\sum_{k=1}^{d}\lambda_k}$

## 11) Probability and Bayes (common in numericals)

- Conditional probability: $P(A\mid B)=\frac{P(A\cap B)}{P(B)}$
- Bayes theorem: $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$
- Total probability: $P(B)=\sum_i P(B\mid A_i)P(A_i)$

## 12) Quick checklist before solving

- Check if labels are categorical (classification) or continuous (regression).
- Build confusion matrix first before computing classification metrics.
- For distance-based methods (`kNN`, `k-means`), verify scaling/normalization.
- Keep denominator check: precision uses predicted positives, recall uses actual positives.
- In tree numericals, compute parent impurity first, then weighted child impurity, then gain.
