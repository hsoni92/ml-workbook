# Deep Dive: House Price Prediction Project
## In-Depth Technical Knowledge & Alternate Approaches

This document provides comprehensive technical knowledge, mathematical foundations, and alternate approaches for the House Price Prediction project. Use this to answer deep technical questions during interviews.

---

## Table of Contents

1. [Mathematical Foundations](#mathematical-foundations)
2. [Data Preprocessing: Deep Dive](#data-preprocessing-deep-dive)
3. [Feature Engineering: Theory & Alternatives](#feature-engineering-theory--alternatives)
4. [Feature Selection: Mathematical Foundations](#feature-selection-mathematical-foundations)
5. [Dimensionality Reduction: PCA Deep Dive](#dimensionality-reduction-pca-deep-dive)
6. [Regression Models: Algorithm Deep Dives](#regression-models-algorithm-deep-dives)
7. [Evaluation Metrics: Mathematical Foundations](#evaluation-metrics-mathematical-foundations)
8. [Alternate Approaches & Research Directions](#alternate-approaches--research-directions)
9. [Advanced Topics](#advanced-topics)

---

## Mathematical Foundations

### Probability Theory & Statistics

#### Skewness and Transformations

**Mathematical Definition:**
- **Skewness**: γ₁ = E[(X - μ)³ / σ³]
- **Interpretation**:
  - γ₁ = 0: Symmetric (normal distribution)
  - γ₁ > 0: Right-skewed (tail on right)
  - γ₁ < 0: Left-skewed (tail on left)

**Our Case:**
- SalePrice skewness = 1.88 (highly right-skewed)
- **Why problematic**: Many ML algorithms assume normal distribution
- **Solution**: Log transformation

**Log Transformation Mathematics:**
- **Log1p**: y' = log(1 + y)
- **Why log1p?**: Handles zero values gracefully, numerically stable
- **Inverse**: y = exp(y') - 1 = expm1(y')
- **Effect on distribution**:
  - Compresses large values more than small values
  - Reduces impact of outliers
  - Makes multiplicative relationships additive

**Alternate Transformations:**

1. **Box-Cox Transformation:**
   - y(λ) = (y^λ - 1) / λ if λ ≠ 0
   - y(λ) = log(y) if λ = 0
   - **Advantage**: Finds optimal λ automatically
   - **Disadvantage**: Requires positive values, more complex
   - **When to use**: When log transform isn't sufficient

2. **Yeo-Johnson Transformation:**
   - Handles negative values (Box-Cox doesn't)
   - More flexible than Box-Cox
   - **When to use**: When data contains zeros or negatives

3. **Square Root Transformation:**
   - y' = √y
   - Less aggressive than log
   - **When to use**: Moderate skewness (0.5 < skewness < 1.0)

4. **Power Transformations:**
   - y' = y^p where p < 1
   - **When to use**: Specific domain knowledge about power relationships

**Why We Chose Log:**
- SalePrice has no zeros (all positive)
- Skewness (1.88) is high enough to warrant log
- Standard practice for financial/price data
- Simple inverse transformation
- Better model performance (R² improved from ~0.85 to 0.90)

---

## Data Preprocessing: Deep Dive

### Missing Value Imputation: Theoretical Foundations

#### Missing Data Mechanisms (Rubin, 1976)

1. **MCAR (Missing Completely At Random):**
   - P(missing) is independent of observed and unobserved data
   - **Example**: Random data entry errors
   - **Imputation**: Mean/median/mode is unbiased

2. **MAR (Missing At Random):**
   - P(missing) depends only on observed data
   - **Example**: GarageType missing when GarageArea = 0
   - **Imputation**: Conditional imputation (e.g., median by group)

3. **MNAR (Missing Not At Random):**
   - P(missing) depends on unobserved values
   - **Example**: Expensive houses less likely to report price
   - **Imputation**: Complex methods (multiple imputation, model-based)

**Our Approach:**
- **Garage features missing → 'None'**: MNAR (missing = no garage)
- **Other categoricals → mode**: MCAR/MAR assumption
- **Numeric → median**: MCAR/MAR assumption, robust to outliers

#### Imputation Methods: Mathematical Comparison

**1. Mean/Median Imputation:**
- **Mean**: x̄ = (1/n) Σxᵢ
- **Median**: Middle value when sorted
- **Variance reduction**: Underestimates variance
- **Bias**: Can introduce bias if not MCAR

**2. Mode Imputation (Categorical):**
- **Mode**: Most frequent value
- **Use case**: Categorical variables
- **Limitation**: May not represent true distribution

**3. K-Nearest Neighbors (KNN) Imputation:**
- Find K most similar samples
- Use their values to impute
- **Advantage**: Preserves relationships
- **Disadvantage**: Computationally expensive, requires complete features

**4. Multiple Imputation:**
- Create M imputed datasets
- Analyze each, combine results
- **Advantage**: Accounts for imputation uncertainty
- **Disadvantage**: Complex, computationally expensive

**5. Model-Based Imputation:**
- Train model to predict missing values
- **Example**: Use other features to predict LotFrontage
- **Advantage**: Uses feature relationships
- **Disadvantage**: Risk of overfitting, circular dependencies

**Why We Used Median:**
- Robust to outliers (important for house prices)
- Simple and fast
- Works well when missing < 20%
- Numerically stable

**Alternate Approach:**
- Could use KNN imputation for numeric features
- Could use model-based imputation (e.g., predict LotFrontage from LotArea)
- Could use multiple imputation for uncertainty quantification

### Outlier Handling: Statistical Theory

#### Outlier Detection Methods

**1. IQR Method (Interquartile Range):**
- **IQR** = Q₃ - Q₁
- **Lower bound** = Q₁ - 1.5 × IQR
- **Upper bound** = Q₃ + 1.5 × IQR
- **Outliers**: Values outside [lower, upper]
- **Mathematical basis**: Based on quartiles, robust to outliers

**2. Z-Score Method:**
- **Z-score**: z = (x - μ) / σ
- **Outliers**: |z| > 3 (or 2.5)
- **Assumption**: Normal distribution
- **Problem**: Mean and std are sensitive to outliers (circular)

**3. Modified Z-Score (MAD):**
- **MAD** = median(|xᵢ - median(x)|)
- **Modified z** = 0.6745 × (x - median) / MAD
- **Outliers**: |modified z| > 3.5
- **Advantage**: Robust (uses median)

**4. Isolation Forest:**
- Unsupervised anomaly detection
- **Principle**: Outliers are easier to isolate
- **Advantage**: Detects multivariate outliers
- **Disadvantage**: Computationally expensive

**5. DBSCAN Clustering:**
- Density-based clustering
- **Outliers**: Points in low-density regions
- **Advantage**: Handles clusters of outliers
- **Disadvantage**: Sensitive to parameters

**Our Approach: Winsorization (Capping)**
- **Method**: Cap at 1st and 99th percentiles
- **Mathematical**: x' = clip(x, Q₀.₀₁, Q₀.₉₉)
- **Advantage**: Preserves information, reduces extreme impact
- **Why not removal**: With 1,460 samples, outliers may be legitimate luxury properties

**Alternate Approaches:**
1. **Robust Scaling**: Use robust scaler (median, IQR) instead of capping
2. **Transformations**: Log transform can naturally handle outliers
3. **Separate Models**: Train separate models for different price ranges
4. **Anomaly Detection**: Use Isolation Forest to identify true anomalies
5. **Domain Knowledge**: Manually review outliers, decide case-by-case

---

## Feature Engineering: Theory & Alternatives

### Feature Engineering Principles

#### 1. Domain Knowledge Integration

**Our Features:**
- **TotalSF**: Combines basement + 1st floor + 2nd floor
- **Rationale**: Total size matters more than individual floors
- **Mathematical**: TotalSF = Σ(floor areas)
- **Why works**: Single comprehensive size metric

**Alternate Approaches:**
- **Price per sqft**: SalePrice / TotalSF (target leakage if using future data)
- **Size ratios**: 2ndFlrSF / 1stFlrSF (two-story ratio)
- **Lot utilization**: TotalSF / LotArea (building density)

#### 2. Temporal Features

**Our Features:**
- **PropertyAge**: YrSold - YearBuilt
- **RemodAge**: YrSold - YearRemodAdd
- **Rationale**: Age affects value, recent remodels add value

**Mathematical Relationships:**
- **Depreciation**: Value decreases with age (exponential or linear)
- **Remodel impact**: Recent remodels increase value, old remodels less impactful
- **Non-linear**: Age effect may be quadratic (rapid initial depreciation, then stable)

**Alternate Temporal Features:**
- **Decade built**: Categorical (pre-1950, 1950s, 1960s, etc.)
- **Years since last sale**: If available
- **Market cycle**: Position in real estate cycle (boom/bust)
- **Seasonal**: Month sold (MoSold) - already in data

#### 3. Interaction Features

**Our Feature:**
- **QualityScore**: OverallQual × OverallCond
- **Rationale**: Multiplicative interaction captures non-linear effect
- **Mathematical**: If both high → very high score, if one low → low score

**Why Multiplicative vs Additive:**
- **Additive**: QualityScore = OverallQual + OverallCond
  - High quality (9) + Low condition (3) = 12
  - Medium quality (6) + Medium condition (6) = 12
  - **Problem**: Same score, but different meanings

- **Multiplicative**: QualityScore = OverallQual × OverallCond
  - High quality (9) × Low condition (3) = 27
  - Medium quality (6) × Medium condition (6) = 36
  - **Advantage**: Captures that both need to be high

**Alternate Interaction Features:**
- **Polynomial features**: TotalSF², OverallQual² (capture non-linearities)
- **Ratio features**: TotalSF / LotArea, GarageArea / LotArea
- **Conditional features**: QualityScore if HasGarage else 0
- **Cross features**: Neighborhood × OverallQual (location-quality interaction)

#### 4. Aggregation Features

**Our Features:**
- **TotalBath**: Weighted sum of all bathrooms
- **TotalPorchSF**: Sum of all porch areas
- **Rationale**: Aggregate related features into single metrics

**Mathematical:**
- **TotalBath**: Σ(wᵢ × bathᵢ) where wᵢ = 1.0 for full, 0.5 for half
- **TotalPorchSF**: Σ(porch_areas)

**Alternate Aggregations:**
- **Weighted averages**: Instead of sums, use averages
- **Max/Min**: Maximum or minimum of related features
- **Counts**: Number of features (e.g., number of porch types)
- **Diversity**: Number of unique categories

#### 5. Binary Features

**Our Features:**
- **HasGarage, HasBasement, HasFireplace, Has2ndFloor**
- **Rationale**: Presence/absence often matters more than exact values
- **Mathematical**: Binary indicator function I(x > 0)

**Why Binary vs Continuous:**
- **Binary**: Captures threshold effect (having garage matters, size less important)
- **Continuous**: Captures magnitude effect (larger garage = more value)
- **Our choice**: Binary for presence, keep continuous for size (both available)

**Alternate Binary Features:**
- **HasPool**: PoolArea > 0
- **HasDeck**: WoodDeckSF > 0
- **IsCornerLot**: LotConfig == 'Corner'
- **IsNewConstruction**: YearBuilt == YrSold

### Advanced Feature Engineering Techniques

#### 1. Target Encoding (Mean Encoding)

**Concept**: Encode categoricals using target variable statistics

**Mathematical:**
- For category c: encoding = mean(SalePrice | category = c)
- **Smoothing**: encoding = (n × mean + α × global_mean) / (n + α)
  - n = count in category
  - α = smoothing parameter

**Advantages:**
- Captures target relationship
- Handles high-cardinality categories
- Reduces dimensionality

**Disadvantages:**
- Risk of overfitting (target leakage if not careful)
- Requires careful cross-validation

**When to use:**
- High-cardinality categoricals (e.g., Neighborhood with 25 categories)
- When one-hot encoding creates too many features

**Our approach**: Used one-hot for important categoricals, label encoding for others
**Alternate**: Could use target encoding for Neighborhood

#### 2. Polynomial Features

**Concept**: Create polynomial combinations of features

**Mathematical:**
- For features [x₁, x₂]: polynomial degree 2 creates [x₁, x₂, x₁², x₁x₂, x₂²]
- **General**: All combinations up to degree d

**Advantages:**
- Captures non-linear relationships
- Interaction effects automatically

**Disadvantages:**
- Exponential growth in features (curse of dimensionality)
- Risk of overfitting

**When to use:**
- Known non-linear relationships
- Small number of important features
- With regularization (Ridge/Lasso)

**Our approach**: Didn't use (Gradient Boosting captures non-linearities automatically)
**Alternate**: Could use for Linear Regression to capture non-linearities

#### 3. Binning (Discretization)

**Concept**: Convert continuous to categorical

**Methods:**
- **Equal-width**: Fixed bin width
- **Equal-frequency**: Fixed samples per bin
- **Decision tree binning**: Optimal splits

**Advantages:**
- Handles non-linearities
- Robust to outliers
- Can capture threshold effects

**Disadvantages:**
- Information loss
- Sensitive to bin boundaries

**When to use:**
- Strong threshold effects
- Non-linear relationships
- With tree-based models (less needed)

**Our approach**: Didn't use (tree models handle continuous well)
**Alternate**: Could bin age into ranges (new, recent, old, very old)

---

## Feature Selection: Mathematical Foundations

### Filter Methods

#### 1. Mutual Information

**Mathematical Definition:**
- **MI(X, Y)** = Σ P(x, y) log(P(x, y) / (P(x) × P(y)))
- **Interpretation**: Measures how much knowing X reduces uncertainty about Y
- **Range**: [0, ∞), 0 = independent, higher = more dependent

**Properties:**
- **Non-negative**: MI ≥ 0
- **Symmetric**: MI(X, Y) = MI(Y, X)
- **Captures non-linear**: Unlike correlation, captures any dependence

**Estimation:**
- **Discrete**: Direct calculation from joint distribution
- **Continuous**: Requires discretization or kernel density estimation
- **sklearn**: Uses k-nearest neighbors estimator

**Why We Used It:**
- Captures non-linear relationships (important for house prices)
- Complements F-test (which only captures linear)

**Alternate Measures:**
- **Correlation**: Only captures linear relationships
- **Distance correlation**: Captures non-linear, but more complex
- **Maximal Information Coefficient (MIC)**: Normalized MI, comparable across features

#### 2. F-Test (F-Regression)

**Mathematical Definition:**
- Tests linear relationship: H₀: β = 0 vs H₁: β ≠ 0
- **F-statistic**: F = (MSR / MSE) where
  - MSR = Mean Square Regression = SSR / df_regression
  - MSE = Mean Square Error = SSE / df_error
- **Distribution**: F-distribution under H₀

**Interpretation:**
- **High F-score**: Strong linear relationship
- **Low p-value**: Relationship is statistically significant
- **Assumption**: Linear relationship, normal errors

**Why We Used It:**
- Fast computation
- Captures linear relationships (complements MI)
- Standard statistical test

**Limitations:**
- Only captures linear relationships
- Assumes normal distribution
- Sensitive to outliers

**Alternate Tests:**
- **Chi-square test**: For categorical features
- **ANOVA F-test**: For categorical vs continuous
- **Kruskal-Wallis**: Non-parametric alternative

### Wrapper Methods

#### Recursive Feature Elimination with Cross-Validation (RFECV)

**Algorithm:**
1. Start with all features
2. Train model, get feature importance
3. Remove least important feature
4. Evaluate with cross-validation
5. Repeat until optimal number of features

**Mathematical:**
- **Feature importance**: I(f) = Σ(imp(f, tree)) / n_trees
- **Removal criterion**: Remove argmin(I(f))
- **Stopping criterion**: Peak CV score

**Advantages:**
- Considers feature interactions
- Uses model performance (not just statistics)
- Cross-validation prevents overfitting

**Disadvantages:**
- Computationally expensive (O(n_features × n_models))
- Model-dependent (different models → different features)
- Greedy (may miss optimal subset)

**Our Results:**
- Selected 23 features
- R² = 0.8965 with CV
- Used Random Forest as base estimator

**Alternate Wrapper Methods:**
1. **Forward Selection**: Start empty, add features one by one
2. **Backward Elimination**: Start full, remove features one by one (what we did)
3. **Bidirectional Search**: Add and remove features
4. **Genetic Algorithms**: Evolutionary search for feature subsets
5. **Simulated Annealing**: Probabilistic search

### Embedded Methods

#### Lasso (L1 Regularization)

**Mathematical Formulation:**
- **Objective**: min ||y - Xβ||² + λ||β||₁
  - ||β||₁ = Σ|βᵢ| (L1 norm)
  - λ = regularization parameter

**Properties:**
- **Sparsity**: Sets some coefficients to exactly zero
- **Feature selection**: Zero coefficients = feature removed
- **Shrinkage**: Non-zero coefficients are shrunk toward zero

**Why L1 Creates Sparsity:**
- **Geometric intuition**: L1 penalty creates diamond-shaped constraint region
- **Corner solutions**: Optimal often at corners (some coefficients = 0)
- **L2 (Ridge)**: Creates circular constraint, no corner solutions (no sparsity)

**Tuning λ:**
- **Large λ**: More features removed (more regularization)
- **Small λ**: Fewer features removed (less regularization)
- **Optimal λ**: Cross-validation (we used default)

**Our Results:**
- Selected 23 features (non-zero coefficients)
- R² = 0.8977
- Similar to RFECV (23 features)

**Alternate Embedded Methods:**
1. **Ridge (L2)**: Doesn't select features (all coefficients non-zero)
2. **Elastic Net**: Combines L1 + L2: λ₁||β||₁ + λ₂||β||₂²
3. **Group Lasso**: Selects groups of features together
4. **Adaptive Lasso**: Weighted L1 penalty
5. **SCAD (Smoothly Clipped Absolute Deviation)**: Non-convex penalty

### Feature Selection Strategy Comparison

**Our Multi-Method Approach:**
1. **Filter (MI + F-test)**: Fast, model-agnostic, selected 35 features
2. **Wrapper (RFECV)**: Model-aware, considers interactions, selected 23 features
3. **Embedded (Lasso)**: Built-in selection, handles multicollinearity, selected 23 features
4. **Final**: Combined to 35 unique features

**Why Multiple Methods:**
- **Robustness**: Features selected by multiple methods are more reliable
- **Complementary**: Each method has strengths
- **Validation**: Agreement across methods increases confidence

**Alternate Strategies:**
1. **Single method**: Faster but less robust
2. **Ensemble feature selection**: Vote across methods
3. **Stability selection**: Select features stable across bootstrap samples
4. **Univariate only**: Fast but misses interactions
5. **Model-specific**: Optimize for specific model (e.g., tree-based)

---

## Dimensionality Reduction: PCA Deep Dive

### Principal Component Analysis (PCA)

#### Mathematical Foundation

**Goal**: Find linear combinations of features that capture maximum variance

**Mathematical Formulation:**
1. **Center data**: X_centered = X - μ (mean = 0)
2. **Covariance matrix**: C = (1/n) X_centeredᵀ X_centered
3. **Eigen decomposition**: C = VΛVᵀ
   - V = eigenvectors (principal components)
   - Λ = eigenvalues (variances)
4. **Projection**: Y = X_centered V

**Principal Components:**
- **First PC**: Direction of maximum variance
- **Second PC**: Direction of maximum variance orthogonal to first
- **And so on...**

**Variance Explained:**
- **k-th PC variance**: λₖ (k-th eigenvalue)
- **Total variance**: Σλᵢ
- **Proportion**: λₖ / Σλᵢ

**Our Results:**
- 35 features → 20 components
- 95% variance retained
- Performance maintained (R² = 0.8992 with Linear Regression)

#### Why PCA Works

**1. Handles Multicollinearity:**
- Correlated features → shared variance
- PCA creates orthogonal components (uncorrelated)
- Reduces redundancy

**2. Dimensionality Reduction:**
- Fewer components than original features
- Retains most information (95% variance)
- Faster training, less overfitting risk

**3. Noise Reduction:**
- Last components often capture noise
- Removing them improves signal-to-noise ratio

#### Limitations of PCA

**1. Linearity Assumption:**
- PCA finds linear combinations
- Misses non-linear relationships
- **Alternate**: Kernel PCA (non-linear)

**2. Interpretability Loss:**
- Components are linear combinations
- Hard to interpret (e.g., "0.3×TotalSF + 0.5×OverallQual - 0.2×PropertyAge")
- **Trade-off**: Performance vs interpretability

**3. Scale Sensitivity:**
- PCA is scale-dependent
- Must standardize features first
- **Our approach**: Used StandardScaler before PCA

**4. Assumes Gaussian Distribution:**
- Works best with normal distributions
- **Our approach**: Log-transformed target helps

#### Alternate Dimensionality Reduction Methods

**1. Independent Component Analysis (ICA):**
- Finds statistically independent components
- **Use case**: When independence matters more than variance
- **Limitation**: More complex, less common

**2. Factor Analysis:**
- Similar to PCA but with error terms
- **Model**: X = ΛF + ε
- **Use case**: When underlying factors are of interest
- **Advantage**: More interpretable than PCA

**3. t-SNE (t-Distributed Stochastic Neighbor Embedding):**
- Non-linear dimensionality reduction
- **Use case**: Visualization (2D/3D)
- **Limitation**: Not for feature reduction (only visualization)

**4. UMAP (Uniform Manifold Approximation and Projection):**
- Non-linear, preserves local and global structure
- **Use case**: Better than t-SNE for some cases
- **Limitation**: Computationally expensive

**5. Autoencoders (Neural Networks):**
- Neural network that learns compressed representation
- **Use case**: Non-linear dimensionality reduction
- **Advantage**: Can capture complex patterns
- **Disadvantage**: Requires more data, harder to interpret

**6. Kernel PCA:**
- Non-linear extension of PCA
- **Use case**: When non-linear relationships exist
- **Advantage**: Captures non-linear patterns
- **Disadvantage**: More complex, harder to interpret

**Why We Chose PCA:**
- Simple and well-understood
- Handles multicollinearity
- Fast computation
- Works well with our data size (1,460 samples)
- 95% variance retention is standard threshold

---

## Regression Models: Algorithm Deep Dives

### 1. Linear Regression

#### Mathematical Foundation

**Model:**
- y = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ + ε
- **Matrix form**: y = Xβ + ε

**Estimation (Ordinary Least Squares):**
- **Objective**: min ||y - Xβ||²
- **Solution**: β̂ = (XᵀX)⁻¹Xᵀy
- **Assumptions**:
  1. Linearity: E[ε|X] = 0
  2. Homoscedasticity: Var(ε|X) = σ² (constant variance)
  3. Independence: εᵢ independent
  4. Normality: ε ~ N(0, σ²) (for inference)

**Our Results:**
- R² = 0.8942 (on log scale)
- RMSE (log) = 0.1333
- **Interpretation**: Linear relationships explain 89.42% of variance

#### Limitations

**1. Linearity Assumption:**
- Assumes linear relationship
- **Problem**: House prices have non-linear relationships
- **Evidence**: Gradient Boosting (non-linear) performs better

**2. Multicollinearity:**
- Correlated features → unstable coefficients
- **Our solution**: Used PCA to create orthogonal components

**3. Outliers:**
- Sensitive to outliers
- **Our solution**: Log transformation, outlier capping

**Alternate Linear Methods:**
1. **Ridge Regression**: L2 regularization, handles multicollinearity
2. **Lasso Regression**: L1 regularization, feature selection
3. **Elastic Net**: Combines L1 + L2
4. **Robust Regression**: Less sensitive to outliers (Huber loss)
5. **Quantile Regression**: Predicts percentiles, not just mean

### 2. Gradient Boosting

#### Mathematical Foundation

**Boosting Concept:**
- Combine weak learners (small decision trees) into strong learner
- **Sequential learning**: Each tree corrects errors of previous trees

**Algorithm (Gradient Boosting for Regression):**

1. **Initialize**: F₀(x) = argmin_γ ΣL(yᵢ, γ) = mean(y) (for squared error)

2. **For m = 1 to M (number of trees):**
   a. **Compute residuals**: rᵢₘ = -[∂L(yᵢ, F(xᵢ))/∂F(xᵢ)] evaluated at Fₘ₋₁
      - For squared error: rᵢₘ = yᵢ - Fₘ₋₁(xᵢ)

   b. **Fit tree to residuals**: hₘ(x) = argmin_h Σ(rᵢₘ - h(xᵢ))²

   c. **Update model**: Fₘ(x) = Fₘ₋₁(x) + α × hₘ(x)
      - α = learning rate (shrinkage)

3. **Final model**: F_M(x) = F₀(x) + αΣhₘ(x)

**Mathematical Intuition:**
- **Gradient descent**: Each tree is a step in function space
- **Residuals**: Point in direction of steepest descent
- **Learning rate**: Controls step size (prevents overfitting)

**Our Hyperparameters:**
- **n_estimators = 200**: Number of trees (M)
- **learning_rate = 0.05**: Shrinkage factor (α)
- **max_depth = 5**: Limits tree complexity
- **min_samples_split = 10**: Minimum samples to split
- **subsample = 0.8**: Stochastic boosting (80% samples per tree)

**Why These Values:**
- **Low learning rate + many trees**: Better generalization
- **Max depth = 5**: Prevents overfitting, captures interactions
- **Subsample = 0.8**: Reduces variance (similar to bagging)

#### Advantages

1. **Non-linear Relationships**: Captures complex patterns
2. **Feature Interactions**: Automatically finds interactions
3. **Robust to Outliers**: Trees are robust
4. **Feature Importance**: Provides interpretability
5. **No Distribution Assumptions**: Non-parametric

#### Limitations

1. **Computational Cost**: Slower than linear models
2. **Hyperparameter Tuning**: Many parameters to tune
3. **Overfitting Risk**: Can overfit if not regularized
4. **Less Interpretable**: Than linear models

#### Alternate Boosting Methods

1. **XGBoost (Extreme Gradient Boosting):**
   - Optimized implementation
   - **Advantages**: Faster, better performance, built-in regularization
   - **When to use**: Large datasets, need speed

2. **LightGBM:**
   - Leaf-wise tree growth
   - **Advantages**: Very fast, low memory
   - **Our result**: R² = 0.9001 (slightly lower than GB)

3. **CatBoost:**
   - Handles categoricals natively
   - **Advantages**: No need for encoding, robust to overfitting
   - **When to use**: Many categorical features

4. **AdaBoost:**
   - Original boosting algorithm
   - **Limitation**: Less flexible than gradient boosting

5. **Histogram-Based Gradient Boosting:**
   - Uses histograms for speed
   - **Advantage**: Faster on large datasets

### 3. Support Vector Regression (SVR)

#### Mathematical Foundation

**Concept**: Find function f(x) that deviates from y by at most ε

**Formulation:**
- **Objective**: min (1/2)||w||² + CΣ(ξᵢ + ξᵢ*)
- **Constraints**:
  - yᵢ - f(xᵢ) ≤ ε + ξᵢ
  - f(xᵢ) - yᵢ ≤ ε + ξᵢ*
  - ξᵢ, ξᵢ* ≥ 0

**Parameters:**
- **ε (epsilon)**: Margin of tolerance (errors within ε are ignored)
- **C**: Regularization parameter (trade-off between margin and errors)
- **ξᵢ, ξᵢ***: Slack variables (allow errors outside ε-tube)

**Kernel Trick:**
- **Linear**: f(x) = wᵀx + b
- **Non-linear (RBF)**: f(x) = ΣαᵢK(xᵢ, x) + b
  - K(xᵢ, x) = exp(-γ||xᵢ - x||²) (RBF kernel)
  - Maps to infinite-dimensional space

**Our Hyperparameters (from GridSearchCV):**
- **kernel = 'rbf'**: Radial basis function (non-linear)
- **C = 1.0**: Moderate regularization
- **epsilon = 0.05**: Small margin (tight fit)
- **gamma = 'scale'**: Automatic scaling

**Results:**
- R² = 0.8801 (lowest of our models)
- RMSE (log) = 0.1419

#### Why SVR Performed Lower

1. **Sample Size**: SVR works better with smaller, well-separated data
2. **Feature Count**: Many features (20 PCA components) may not suit SVR
3. **Tree Models Better for Tabular Data**: Gradient Boosting excels at tabular data
4. **Hyperparameter Sensitivity**: SVR is sensitive to C, ε, γ

#### Alternate Kernel Methods

1. **Polynomial Kernel**: K(x, y) = (γxᵀy + r)ᵈ
2. **Sigmoid Kernel**: K(x, y) = tanh(γxᵀy + r)
3. **Laplacian Kernel**: K(x, y) = exp(-γ||x - y||₁)

---

## Evaluation Metrics: Mathematical Foundations

### R² (Coefficient of Determination)

**Definition:**
- R² = 1 - (SS_res / SS_tot)
  - SS_res = Σ(yᵢ - ŷᵢ)² (sum of squared residuals)
  - SS_tot = Σ(yᵢ - ȳ)² (total sum of squares)

**Interpretation:**
- **R² = 1**: Perfect predictions
- **R² = 0**: Model performs as well as predicting mean
- **R² < 0**: Model worse than mean (rare, indicates problems)

**Properties:**
- **Scale-invariant**: Same for original and transformed (if linear transform)
- **Comparable**: Can compare across models
- **Limitation**: Can be misleading with non-linear models

**Our Results:**
- Gradient Boosting: R² = 0.9043 (90.43% variance explained)

### RMSE (Root Mean Squared Error)

**Definition:**
- RMSE = √(1/n) Σ(yᵢ - ŷᵢ)²
- **Units**: Same as target variable

**Properties:**
- **Penalizes large errors**: Squared term amplifies large errors
- **Sensitive to outliers**: Outliers have disproportionate impact
- **Interpretable**: Average prediction error in original units

**Our Results (log scale):**
- Gradient Boosting: RMSE = 0.1267
- **Interpretation**: Average error of 0.1267 on log scale
- **Original scale**: After expm1, corresponds to ~12.7% error

### MAE (Mean Absolute Error)

**Definition:**
- MAE = (1/n) Σ|yᵢ - ŷᵢ|
- **Units**: Same as target variable

**Properties:**
- **Less sensitive to outliers**: Than RMSE
- **Interpretable**: Average absolute error
- **Robust**: Median absolute error even more robust

**Comparison RMSE vs MAE:**
- **RMSE ≥ MAE**: Always (Jensen's inequality)
- **When RMSE >> MAE**: Large errors present
- **When RMSE ≈ MAE**: Errors are relatively uniform

### MAPE (Mean Absolute Percentage Error)

**Definition:**
- MAPE = (1/n) Σ|yᵢ - ŷᵢ| / |yᵢ| × 100%
- **Units**: Percentage

**Properties:**
- **Scale-invariant**: Comparable across different scales
- **Interpretable**: "Average error is X%"
- **Limitation**: Undefined when yᵢ = 0, biased for small values

**Our Results:**
- MAPE = 0.76% (highly accurate)
- **Interpretation**: Average error is less than 1%

### Alternate Metrics

1. **Median Absolute Error (MedAE)**: More robust to outliers
2. **R² Adjusted**: Penalizes for number of features
3. **AIC/BIC**: Information criteria (penalize complexity)
4. **Cross-validated R²**: More robust estimate
5. **Quantile Loss**: For predicting percentiles

---

## Alternate Approaches & Research Directions

### 1. Deep Learning Approaches

#### Neural Networks for Regression

**Architecture:**
- Input layer: 20 features (PCA components)
- Hidden layers: 2-3 layers, 64-128 neurons each
- Output layer: 1 neuron (price prediction)
- Activation: ReLU for hidden, linear for output

**Advantages:**
- Can capture very complex non-linearities
- Automatic feature learning
- State-of-the-art for some problems

**Disadvantages:**
- Requires more data (we have 1,460 samples - borderline)
- Hyperparameter tuning complex
- Less interpretable
- Overfitting risk high

**When to Use:**
- Very large datasets (>10K samples)
- Complex non-linear relationships
- When interpretability less important

**Our Choice**: Didn't use (sample size too small, tree models sufficient)

#### Autoencoders for Feature Learning

**Concept**: Learn compressed representation of features

**Architecture:**
- Encoder: Features → Latent representation
- Decoder: Latent → Reconstructed features
- Use encoder for dimensionality reduction

**Advantages:**
- Learns optimal representation
- Non-linear (unlike PCA)

**Disadvantages:**
- Complex, requires tuning
- May overfit with small data

### 2. Ensemble Methods

#### Stacking

**Concept**: Train meta-learner on predictions of base models

**Algorithm:**
1. Train base models (GB, LightGBM, SVR, Linear)
2. Get predictions on validation set
3. Train meta-learner (e.g., Linear Regression) on predictions
4. Final prediction = meta-learner(base_predictions)

**Advantages:**
- Often improves performance
- Combines strengths of different models

**Disadvantages:**
- More complex
- Risk of overfitting meta-learner

**Our Approach**: Didn't use (single model sufficient)
**Alternate**: Could stack GB + LightGBM + Linear

#### Blending

**Similar to stacking but simpler:**
- Weighted average of model predictions
- Weights from validation performance

**Advantages:**
- Simple
- Often works well

**Disadvantages:**
- Less flexible than stacking

### 3. Bayesian Methods

#### Bayesian Linear Regression

**Concept**: Treat parameters as random variables

**Advantages:**
- Provides uncertainty estimates
- Handles small datasets well
- Regularization through priors

**Disadvantages:**
- More complex
- Requires prior specification
- Computationally expensive

#### Gaussian Process Regression

**Concept**: Non-parametric Bayesian method

**Advantages:**
- Provides uncertainty estimates
- Handles non-linear relationships
- No overfitting (by design)

**Disadvantages:**
- O(n³) complexity (slow for large n)
- Requires kernel selection

**When to Use:**
- Small datasets
- Need uncertainty estimates
- When interpretability important

### 4. Time Series Considerations

**Our Data**: Houses sold 2006-2010

**Time Series Aspects:**
- **Temporal trends**: Prices may change over time
- **Seasonality**: Prices may vary by month
- **Market cycles**: Boom/bust cycles

**Alternate Approaches:**
1. **Time-based features**: Year sold, month sold (we have MoSold, YrSold)
2. **Temporal validation**: Train on earlier years, test on later
3. **Time series models**: ARIMA, Prophet (if treating as time series)
4. **Market adjustment**: Adjust for inflation, market conditions

**Our Approach**: Used YrSold, MoSold as features
**Alternate**: Could use temporal cross-validation

### 5. Causal Inference

**Concept**: Understand causal relationships, not just correlations

**Methods:**
- **Instrumental variables**: Find instruments for endogenous variables
- **Difference-in-differences**: Compare treated vs control
- **Regression discontinuity**: Exploit thresholds

**Application to House Prices:**
- Does quality cause higher prices? (likely yes)
- Does neighborhood cause higher prices? (likely yes, but confounded)
- Does age cause lower prices? (likely yes, depreciation)

**Our Approach**: Predictive (not causal)
**Alternate**: Could use causal methods if research question is causal

---

## Advanced Topics

### 1. Uncertainty Quantification

#### Prediction Intervals

**Concept**: Provide range of likely values, not just point estimate

**Methods:**
1. **Quantile Regression**: Predict percentiles (10th, 50th, 90th)
2. **Bootstrap**: Resample data, get distribution of predictions
3. **Bayesian Methods**: Natural uncertainty from posterior
4. **Conformal Prediction**: Distribution-free intervals

**Why Important:**
- Users need to know confidence
- Risk assessment (e.g., "price likely between $150K-$200K")

**Our Approach**: Didn't provide (only point predictions)
**Alternate**: Could add quantile regression or bootstrap

### 2. Model Interpretability

#### SHAP (SHapley Additive exPlanations)

**Concept**: Game theory approach to feature importance

**Mathematical:**
- **Shapley value**: φᵢ = Σ(S! (n-S-1)! / n!) [f(S∪{i}) - f(S)]
  - Average marginal contribution across all feature subsets
- **Properties**: Efficiency, symmetry, dummy, additivity

**Advantages:**
- Theoretically grounded
- Provides local (per-prediction) and global importance
- Handles interactions

**Our Approach**: Didn't use (feature importance sufficient)
**Alternate**: Could use SHAP for individual predictions

#### LIME (Local Interpretable Model-agnostic Explanations)

**Concept**: Approximate complex model locally with simple model

**Algorithm:**
1. Sample points near prediction
2. Get predictions from complex model
3. Fit simple model (e.g., linear) to local predictions
4. Interpret simple model

**Advantages:**
- Model-agnostic
- Provides local explanations

**Disadvantages:**
- Approximate (not exact)
- Sensitive to sampling

### 3. Fairness and Bias

#### Fairness Metrics

**Concept**: Ensure model doesn't discriminate

**Metrics:**
- **Demographic parity**: Equal predictions across groups
- **Equalized odds**: Equal true/false positive rates
- **Calibration**: Equal accuracy across groups

**Application:**
- Check if model discriminates by neighborhood (proxy for demographics)
- Monitor predictions by property type

**Our Approach**: Didn't explicitly check
**Alternate**: Could audit for fairness

### 4. Online Learning

#### Concept: Update model incrementally with new data

**Methods:**
- **Stochastic Gradient Descent**: Update with each sample
- **Incremental Learning**: Update with batches
- **Adaptive Models**: Adjust to distribution shifts

**When to Use:**
- Streaming data
- Need to adapt quickly
- Limited storage

**Our Approach**: Batch learning (train once)
**Alternate**: Could implement online updates

### 5. Transfer Learning

#### Concept: Use knowledge from related domains

**Applications:**
- Train on multiple cities, fine-tune for specific city
- Use commercial real estate knowledge for residential
- Transfer from similar prediction tasks

**Our Approach**: Single dataset (Ames, Iowa)
**Alternate**: Could use data from other cities

---

## Key Takeaways for Interviews

### When Asked About Alternatives

1. **Always mention trade-offs**: Every method has pros/cons
2. **Justify your choice**: Explain why you chose current method
3. **Show awareness**: Mention you considered alternatives
4. **Be specific**: Give concrete examples

### When Asked About Mathematical Foundations

1. **Start with intuition**: Explain concept simply
2. **Then formalize**: Give mathematical formulation
3. **Connect to practice**: Show how it applies to your project
4. **Mention limitations**: Show critical thinking

### When Asked About Improvements

1. **Be realistic**: Consider data, time, resources
2. **Prioritize**: What would have biggest impact?
3. **Consider trade-offs**: Performance vs complexity vs interpretability
4. **Show learning**: What would you do differently?

---

## Conclusion

This deep dive covers:
- Mathematical foundations of all methods used
- Alternate approaches for each step
- Trade-offs and design decisions
- Advanced topics for research-level discussions

Use this document to:
- Answer deep technical questions
- Show comprehensive understanding
- Discuss alternatives and trade-offs
- Demonstrate research-level knowledge

**Remember**: Understanding why you made choices is as important as the choices themselves.

---

*Prepared for: Advanced Apex Project - Phase 4 VIVA*
*Project: House Price Prediction using Machine Learning*
*Last Updated: Based on protected_apex_project_phase4_deliverable.ipynb*

