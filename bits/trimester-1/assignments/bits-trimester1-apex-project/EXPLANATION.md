# Code Explanation: House Price Prediction Project
## Critical Code Sections with Explanations

This document explains all critical code sections from `protected_apex_project_phase4_deliverable.ipynb` with simple and precise explanations.

---

## Table of Contents

1. [Data Acquisition](#1-data-acquisition)
2. [Data Audit](#2-data-audit)
3. [Exploratory Data Analysis](#3-exploratory-data-analysis)
4. [Data Cleaning](#4-data-cleaning)
5. [Feature Engineering](#5-feature-engineering)
6. [Feature Encoding](#6-feature-encoding)
7. [Feature Selection](#7-feature-selection)
8. [Dimensionality Reduction](#8-dimensionality-reduction)
9. [Model Training](#9-model-training)
10. [Model Evaluation](#10-model-evaluation)
11. [Results Export](#11-results-export)

---

## 1. Data Acquisition

### Cell 0: Kaggle API Setup

```python
# Step 1: Install Kaggle API
!pip install -q kaggle

# Step 2: Create kaggle.json with your credentials
import json
import os

kaggle_token = {
    "username": "himanshusoni001",
    "key": "7888d0ba07df9b4b51271fe3c97fac80"
}

# Write the token to the correct location
os.makedirs('~/.kaggle', exist_ok=True)
with open('~/.kaggle/kaggle.json', 'w') as f:
    json.dump(kaggle_token, f)

# Set permission
!chmod 600 ~/.kaggle/kaggle.json
```

**Explanation:**
- Installs Kaggle API package for dataset download
- Creates authentication file (`kaggle.json`) with username and API key
- Sets secure file permissions (600 = read/write for owner only)
- **Why**: Required for programmatic dataset access from Kaggle

### Cell 1: Dataset Download

```python
# Step 3: Download dataset using Kaggle API
import os
os.makedirs('data', exist_ok=True)
!kaggle competitions download -c house-prices-advanced-regression-techniques -p data/

# Step 4: Unzip the downloaded dataset
!unzip -o data/house-prices-advanced-regression-techniques.zip -d data/
```

**Explanation:**
- Downloads competition dataset using Kaggle CLI
- Creates `data/` directory if it doesn't exist
- Unzips the downloaded file to extract CSV files
- **Output**: `train.csv`, `test.csv`, `data_description.txt`, `sample_submission.csv`

### Cell 2: Data Loading and Library Imports

```python
# Step 5: Load and use the dataset
import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_notebook
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.layouts import gridplot, column, row
from bokeh.palettes import Viridis256, Category10
from bokeh.transform import linear_cmap
from scipy.stats import gaussian_kde
import warnings
warnings.filterwarnings('ignore')

# Enable Bokeh output in notebook
output_notebook()

data = pd.read_csv('data/train.csv')

# Optional: Preview data
data.head()
```

**Explanation:**
- Imports essential libraries: pandas (data manipulation), numpy (numerical operations), Bokeh (visualization)
- Loads training data from CSV file
- `output_notebook()` enables Bokeh plots to display in Jupyter notebook
- `warnings.filterwarnings('ignore')` suppresses warning messages for cleaner output

---

## 2. Data Audit

### Cell 5: Dataset Shape

```python
# 1. Shape of the dataset
print("\nShape of dataset:", data.shape)
```

**Explanation:**
- Returns dimensions: (rows, columns)
- **Output**: (1460, 81) = 1,460 houses with 81 features
- **Purpose**: Understand dataset size before processing

### Cell 6: Data Types Check

```python
# 2. Data types of each column
print("\nData types of each column:")
print(data.dtypes)
```

**Explanation:**
- Shows data type of each column (int64, float64, object)
- **Purpose**: Identify numeric vs categorical features
- **Why important**: Determines which preprocessing methods to apply

### Cell 7: Missing Values Analysis

```python
# 3. Missing values per column
print("\nMissing values per column:")
print(data.isnull().sum())
```

**Explanation:**
- Counts missing (NaN) values for each column
- **Purpose**: Identify columns requiring imputation
- **Why critical**: Missing values must be handled before modeling

### Cell 9: Negative Values Check

```python
# 5. Check for negative or invalid values
numeric_cols = data.select_dtypes(include=[np.number]).columns.tolist()
print(numeric_cols)
print("\nNegative values:")
for col in numeric_cols:
    if (data[col] < 0).any():
        print(f"\033[91mColumn '{col}' has negative values.\033[0m")
        print(data[data[col] < 0][[col]])
    else:
        print(f"\033[92mColumn '{col}' has no negative values.\033[0m")
```

**Explanation:**
- Selects only numeric columns
- Checks each column for negative values (invalid for house features)
- Uses color coding (red for errors, green for OK)
- **Purpose**: Data quality validation

### Cell 10: Duplicate Rows Check

```python
# 6. Duplicate rows
print("\nNumber of duplicate rows:", data.duplicated().sum())
```

**Explanation:**
- Counts completely duplicate rows
- **Output**: 0 (no duplicates found)
- **Purpose**: Ensure data quality, duplicates would bias the model

---

## 3. Exploratory Data Analysis

### Cell 12: Summary Statistics

```python
#Summary statistics for numeric columns
print("\nSummary statistics:")
print(data.describe())
```

**Explanation:**
- Generates descriptive statistics: count, mean, std, min, 25%, 50%, 75%, max
- **Purpose**: Understand data distribution, identify outliers, check ranges
- **Key insights**: Mean vs median differences indicate skewness

### Cell 13: Categorical Value Counts

```python
#Summary statistics for categorical columns
for col in data.columns:
    if (data[col].dtype=='object'):
        print(f"\n{col}:")
        print(data[col].value_counts())
    else:
        pass
```

**Explanation:**
- Iterates through all columns
- For categorical (object) columns, counts frequency of each category
- **Purpose**: Understand categorical distributions, identify rare categories
- **Why important**: Guides encoding strategy (one-hot vs label encoding)

### Cell 14: Price Analysis by Categories

```python
# Calculate average property prices across neighborhoods
average_price_by_neighborhood = data.groupby('Neighborhood')['SalePrice'].mean().sort_values()

# Identify the most affordable neighborhoods
affordable_neighborhoods = average_price_by_neighborhood.head(5)

# Identify the most expensive neighborhoods
expensive_neighborhoods = average_price_by_neighborhood.tail(5)

# Average property size and price by building type
average_size_and_price = data.groupby('BldgType')[['GrLivArea', 'SalePrice']].mean()

# Average price by overall quality
average_price_by_quality = data.groupby('OverallQual')['SalePrice'].mean().sort_values()
```

**Explanation:**
- Groups data by categorical features and calculates mean SalePrice
- Identifies price patterns by neighborhood, building type, and quality
- **Purpose**: Discover relationships between features and target variable
- **Key insight**: Quality and location significantly impact price

### Cell 16: Univariate Visualization

```python
# UNIVARIATE VISUALISATION
for col in numeric_cols:
    col_data = data[col].dropna()
    hist, edges = np.histogram(col_data, bins=20)

    kde = gaussian_kde(col_data)
    x_kde = np.linspace(col_data.min(), col_data.max(), 200)
    y_kde = kde(x_kde)
    y_kde = y_kde * len(col_data) * (edges[1] - edges[0])

    p = figure(width=600, height=400, title=f'Histogram & KDE of {col}',
               x_axis_label=col, y_axis_label='Frequency')

    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color='skyblue', line_color='white', alpha=0.7)

    p.line(x_kde, y_kde, line_width=2, line_color='navy', legend_label='KDE')

    show(p)
```

**Explanation:**
- Creates histogram (bar chart) and KDE (smooth curve) for each numeric column
- **Histogram**: Shows frequency distribution in bins
- **KDE**: Smooth probability density estimate
- **Purpose**: Visualize data distribution, identify skewness, outliers, normality
- **Why important**: Guides transformation decisions (e.g., log transform for skewed data)

### Cell 18: Correlation Heatmap

```python
# Correlation heat map
numeric_data = data.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr()
corr_df = corr_matrix.stack().reset_index()
corr_df.columns = ['Feature1', 'Feature2', 'Correlation']

mapper = LinearColorMapper(palette=Viridis256,
                           low=corr_df['Correlation'].min(),
                           high=corr_df['Correlation'].max())

features = list(corr_matrix.columns)
p1 = figure(width=800, height=600, title='Correlation Heatmap',
           x_range=features, y_range=list(reversed(features)),
           toolbar_location='above', tools='hover,pan,box_zoom,reset,save')

source = ColumnDataSource(corr_df)

p1.rect('Feature1', 'Feature2', 1, 1, source=source, line_color=None,
        fill_color=transform('Correlation', mapper))

color_bar = ColorBar(color_mapper=mapper, location=(0, 0))
p1.add_layout(color_bar, 'right')
```

**Explanation:**
- Calculates correlation matrix for all numeric features
- Creates heatmap visualization (color-coded correlation values)
- **Correlation range**: -1 (negative) to +1 (positive), 0 = no correlation
- **Purpose**: Identify multicollinearity, find features strongly related to target
- **Key insight**: Features like GarageCars and GarageArea are highly correlated

### Cell 20: Log Transformation

```python
# Check skewness and log-transform if needed
skew_val = data[target].skew()
print(f"Skewness of {target}: {skew_val:.2f}")
if skew_val > 0.75:
    data['SalePrice_log'] = np.log1p(data[target])
```

**Explanation:**
- Calculates skewness (measure of distribution asymmetry)
- **Skewness > 0.75**: Indicates right-skewed distribution
- **log1p**: log(1 + x) - numerically stable, handles zeros
- **Purpose**: Normalize distribution for better model performance
- **Why**: Many ML algorithms assume normal distribution
- **Output**: Skewness = 1.88 (highly skewed) → log transformation applied

---

## 4. Data Cleaning

### Cell 27: Missing Value Handling

```python
# Handle missing values
missing_pct = (data.isnull().sum() / len(data)) * 100
high_missing = missing_pct[missing_pct > 50].index.tolist()
print(f"Columns with >50% missing values: {high_missing}")

columns_to_drop = ['Id'] + high_missing
datan = data.drop(columns=columns_to_drop, errors='ignore').copy()

# For numerical columns: impute with median
numeric_cols_with_missing = datan.select_dtypes(include=[np.number]).columns[datan.select_dtypes(include=[np.number]).isnull().any()].tolist()
for col in numeric_cols_with_missing:
    datan.loc[:, col] = datan[col].fillna(datan[col].median())

# For categorical columns: impute with mode or 'None' for meaningful features
categorical_cols_with_missing = datan.select_dtypes(include=['object']).columns[datan.select_dtypes(include=['object']).isnull().any()].tolist()
for col in categorical_cols_with_missing:
    if col in ['GarageType', 'GarageFinish', 'GarageQual', 'GarageCond',
               'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
               'FireplaceQu', 'Fence', 'MiscFeature']:
        datan.loc[:, col] = datan[col].fillna('None')
    else:
        datan.loc[:, col] = datan[col].fillna(datan[col].mode()[0])
```

**Explanation:**
- **Step 1**: Identifies columns with >50% missing (drops them - insufficient information)
- **Step 2**: Drops 'Id' column (not a feature)
- **Step 3**: Numeric imputation - uses median (robust to outliers)
- **Step 4**: Categorical imputation - uses 'None' for meaningful absences (e.g., no garage), mode for others
- **Why median**: Less affected by outliers than mean
- **Why 'None'**: Missing garage = no garage (meaningful, not error)

### Cell 31: Outlier Capping (Winsorization)

```python
# Outlier Capping / Winsorization
from scipy.stats.mstats import winsorize

numeric_cols = datan.select_dtypes(include=[np.number]).columns

for col in numeric_cols:
    lower, upper = datan[col].quantile([0.01, 0.99])
    datan[col] = np.clip(datan[col], lower, upper)

print("Outliers capped at 1st-99th percentile for numeric columns.")
```

**Explanation:**
- **Winsorization**: Caps extreme values instead of removing them
- **Method**: Sets values below 1st percentile to 1st percentile, above 99th to 99th
- **Why cap instead of remove**: Preserves information, outliers may be legitimate luxury properties
- **Purpose**: Reduces impact of extreme values without losing data points

---

## 5. Feature Engineering

### Cell 34: Creating New Features

```python
# CREATE NEW FEATURES FROM EXISTING COLUMNS

# 1. Total Square Footage
datan['TotalSF'] = datan['TotalBsmtSF'] + datan['1stFlrSF'] + datan['2ndFlrSF']

# 2. Property Age (from year sold)
datan['PropertyAge'] = datan['YrSold'] - datan['YearBuilt']

# 3. Years Since Remodel
datan['RemodAge'] = datan['YrSold'] - datan['YearRemodAdd']

# 4. Binary features - Has Garage
datan['HasGarage'] = (datan['GarageArea'] > 0).astype(int)

# 5. Binary features - Has Basement
datan['HasBasement'] = (datan['TotalBsmtSF'] > 0).astype(int)

# 6. Binary features - Has Fireplace
datan['HasFireplace'] = (datan['Fireplaces'] > 0).astype(int)

# 7. Binary features - Has 2nd Floor
datan['Has2ndFloor'] = (datan['2ndFlrSF'] > 0).astype(int)

# 8. Quality Score (interaction feature)
datan['QualityScore'] = datan['OverallQual'] * datan['OverallCond']

# 9. Total Bathrooms
datan['TotalBath'] = datan['FullBath'] + 0.5 * datan['HalfBath'] + datan['BsmtFullBath'] + 0.5 * datan['BsmtHalfBath']

# 10. Total Porch Area
datan['TotalPorchSF'] = datan['OpenPorchSF'] + datan['EnclosedPorch'] + datan['3SsnPorch'] + datan['ScreenPorch']
```

**Explanation:**
- **TotalSF**: Combines all square footage → single size metric (most important feature)
- **PropertyAge**: Age at sale time (older = typically cheaper)
- **RemodAge**: Years since remodel (recent = more value)
- **Binary features**: Presence/absence often matters more than exact values
- **QualityScore**: Multiplicative interaction (both quality and condition matter)
- **TotalBath**: Weighted sum (full=1.0, half=0.5)
- **TotalPorchSF**: Aggregates all porch areas
- **Purpose**: Create more informative features that improve model performance

---

## 6. Feature Encoding

### Cell 37: One-Hot Encoding

```python
# One-hot encode categorical variables
categorical_cols = datan.select_dtypes(include=['object']).columns.tolist()

important_categoricals = ['Neighborhood', 'BldgType', 'HouseStyle', 'ExterQual', 'ExterCond',
                          'Foundation', 'HeatingQC', 'CentralAir', 'KitchenQual',
                          'GarageType', 'GarageFinish', 'PavedDrive', 'SaleCondition']

categorical_to_encode = [col for col in important_categoricals if col in categorical_cols]

datam = pd.get_dummies(datan, columns=categorical_to_encode, drop_first=True)
```

**Explanation:**
- **One-hot encoding**: Converts each category to binary column (0 or 1)
- **drop_first=True**: Removes one category per feature (prevents multicollinearity)
- **Why for important categoricals**: Preserves category independence, no artificial ordering
- **Example**: Neighborhood "NoRidge" becomes column `Neighborhood_NoRidge = 1` for that house
- **Result**: 76 features → 144 features (after encoding)

### Cell 40: Label Encoding

```python
# Using LabelEncoder to transform remaining categorical variables to numeric variables

from sklearn.preprocessing import LabelEncoder

# Separate features and target
X = datam.drop(columns=['SalePrice', 'SalePrice_log'], axis=1)
y = datam['SalePrice']

# Find remaining categorical columns (those not one-hot encoded)
cat_f = X.select_dtypes(include='object').columns
print(f"Remaining categorical columns to encode: {list(cat_f)}")

# Encode remaining categorical features
X_encoded = X.copy()
label_encoders = {}
for col in cat_f:
    le = LabelEncoder()
    X_encoded[col] = le.fit_transform(X_encoded[col])
    label_encoders[col] = le
```

**Explanation:**
- **Label encoding**: Assigns integer (0, 1, 2, ...) to each category
- **Why for remaining categoricals**: Less important features, reduces dimensionality
- **fit_transform**: Learns mapping and applies it
- **Stores encoders**: For applying same mapping to test data later
- **Limitation**: Creates artificial ordering (but acceptable for less important features)

---

## 7. Feature Selection

### Cell 43: Mutual Information

```python
from sklearn.feature_selection import SelectKBest, mutual_info_regression

selector = SelectKBest(score_func=mutual_info_regression, k='all')
selector.fit(X_encoded, y)

mi_scores = pd.DataFrame({
    'Feature': X_encoded.columns,
    'MI Score': selector.scores_
}).sort_values(by='MI Score', ascending=False)

print("Top 20 Features by Mutual Information Score:")
print(mi_scores.head(20))
```

**Explanation:**
- **Mutual Information**: Measures non-linear relationships between features and target
- **k='all'**: Scores all features (doesn't select yet)
- **Purpose**: Identify features with strong non-linear relationships
- **Why important**: Complements F-test (which only captures linear relationships)
- **Result**: TotalSF has highest MI score (0.68)

### Cell 45: F-Regression

```python
from sklearn.feature_selection import f_regression

f_selector = SelectKBest(score_func=f_regression, k='all')
f_selector.fit(X_encoded, y)

# Collect scores
f_scores = pd.DataFrame({
    'Feature': X_encoded.columns,
    'F_Score': f_selector.scores_,
    'p_value': f_selector.pvalues_
}).sort_values(by='F_Score', ascending=False)
```

**Explanation:**
- **F-test**: Statistical test for linear relationships
- **F_Score**: Higher = stronger linear relationship
- **p_value**: Lower = more statistically significant
- **Purpose**: Identify features with strong linear relationships
- **Why with MI**: Together they capture both linear and non-linear relationships

### Cell 47: Random Forest Feature Importance

```python
# Train Random Forest model to get feature importance
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_encoded, y)

importances = pd.Series(rf.feature_importances_, index=X_encoded.columns)
top_features = importances.sort_values(ascending=False).head(30)
```

**Explanation:**
- **Random Forest**: Trains model to get feature importance scores
- **Feature importance**: Measures how much each feature reduces prediction error
- **Purpose**: Model-aware feature selection (considers feature interactions)
- **Why useful**: Captures which features matter for actual predictions

### Cell 48-50: Combined Feature Selection

```python
# Combine F-test and Mutual Information top 30
top_30_f = f_scores.head(30)['Feature'].tolist()
top_30_mi = mi_scores.head(30)['Feature'].tolist()

# Get unique features from both methods
combined_features = list(set(top_30_f + top_30_mi))
print(f"Combined unique features: {len(combined_features)}")
```

**Explanation:**
- Combines top 30 features from F-test and Mutual Information
- **Purpose**: Get features selected by multiple methods (more reliable)
- **Result**: 35 unique features selected
- **Rationale**: Features selected by multiple methods are more trustworthy

### RFECV (Recursive Feature Elimination with CV)

```python
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestRegressor

rfecv = RFECV(
    estimator=RandomForestRegressor(n_estimators=50, random_state=42),
    step=1,
    cv=5,
    scoring='r2',
    n_jobs=-1
)
rfecv.fit(X_selected, y_train_log)

print(f"Optimal number of features: {rfecv.n_features_}")
print(f"Selected features: {rfecv.support_.sum()}")
```

**Explanation:**
- **RFECV**: Recursively removes features, uses cross-validation to find optimal number
- **step=1**: Remove one feature at a time
- **cv=5**: 5-fold cross-validation
- **scoring='r2'**: Optimize for R² score
- **Purpose**: Find optimal feature subset considering model performance
- **Result**: Selected 23 features with R² = 0.8965

### Lasso Feature Selection

```python
from sklearn.linear_model import LassoCV

lasso = LassoCV(cv=5, random_state=42, max_iter=2000)
lasso.fit(X_selected, y_train_log)

# Get non-zero coefficients (selected features)
selected_features_lasso = X_selected.columns[lasso.coef_ != 0].tolist()
print(f"Lasso selected {len(selected_features_lasso)} features")
```

**Explanation:**
- **Lasso**: L1 regularization sets some coefficients to exactly zero
- **LassoCV**: Automatically selects optimal regularization parameter using CV
- **Non-zero coefficients**: Features that matter (others set to zero)
- **Purpose**: Automatic feature selection with built-in regularization
- **Result**: Selected 23 features with R² = 0.8977

---

## 8. Dimensionality Reduction

### PCA (Principal Component Analysis)

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Standardize features before PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_final)

# Apply PCA
pca = PCA(n_components=0.95)  # Retain 95% variance
X_pca = pca.fit_transform(X_scaled)

print(f"Original features: {X_scaled.shape[1]}")
print(f"PCA components: {X_pca.shape[1]}")
print(f"Variance explained: {pca.explained_variance_ratio_.sum():.2%}")
```

**Explanation:**
- **StandardScaler**: Standardizes features (mean=0, std=1) - required before PCA
- **PCA**: Reduces dimensions while retaining variance
- **n_components=0.95**: Keep enough components to retain 95% variance
- **Purpose**: Handle multicollinearity, reduce dimensions, speed up training
- **Result**: 35 features → 20 components (95% variance retained)

---

## 9. Model Training

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_pca, y_log, test_size=0.2, random_state=42
)

print(f"Training samples: {X_train.shape[0]}")
print(f"Test samples: {X_test.shape[0]}")
```

**Explanation:**
- **train_test_split**: Randomly splits data into training (80%) and test (20%) sets
- **test_size=0.2**: 20% for testing
- **random_state=42**: Ensures reproducibility (same split every time)
- **Purpose**: Evaluate model on unseen data (prevents overfitting assessment)

### Gradient Boosting Model

```python
from sklearn.ensemble import GradientBoostingRegressor
import joblib

# Gradient Boosting Regressor (PCA)
gb = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    min_samples_split=10,
    subsample=0.8,
    random_state=42
)

gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)

# Save model
joblib.dump(gb, "models/model_gb_pca.pkl")
print("Gradient Boosting trained and saved as models/model_gb_pca.pkl")
```

**Explanation:**
- **GradientBoostingRegressor**: Ensemble of decision trees, each corrects previous errors
- **n_estimators=200**: Number of trees
- **learning_rate=0.05**: Shrinkage factor (prevents overfitting)
- **max_depth=5**: Limits tree depth (regularization)
- **subsample=0.8**: Uses 80% of samples per tree (stochastic boosting)
- **joblib.dump**: Saves trained model for later use
- **Result**: Best performing model (R² = 0.9043)

### LightGBM Model

```python
try:
    import lightgbm as lgb

    lgb_model = lgb.LGBMRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=5,
        random_state=42,
        n_jobs=-1
    )

    lgb_model.fit(X_train, y_train)
    y_pred_lgb = lgb_model.predict(X_test)

    joblib.dump(lgb_model, "models/model_lgb_pca.pkl")
    print("LightGBM trained and saved as models/model_lgb_pca.pkl")
except ImportError:
    print("LightGBM is not available")
```

**Explanation:**
- **LightGBM**: Fast gradient boosting implementation
- **try-except**: Handles case where LightGBM not installed
- **Similar parameters**: Fair comparison with Gradient Boosting
- **Result**: R² = 0.9001 (slightly lower but faster)

### Linear Regression Model

```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

joblib.dump(lr, "models/model_lr_pca.pkl")
print("Linear Regression trained and saved as models/model_lr_pca.pkl")
```

**Explanation:**
- **LinearRegression**: Simple linear model (baseline)
- **No hyperparameters**: Simple to use
- **Purpose**: Baseline comparison, interpretable
- **Result**: R² = 0.8942 (lower than tree-based models)

### SVR with GridSearchCV

```python
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

svr_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("svr", SVR())
])

svr_param_grid = {
    "svr__kernel": ["rbf"],
    "svr__C": [1.0, 10.0],
    "svr__epsilon": [0.05, 0.1],
    "svr__gamma": ["scale"]
}

svr_gs = GridSearchCV(svr_pipe, svr_param_grid, cv=3, scoring="neg_mean_squared_error", n_jobs=-1, verbose=1)
svr_gs.fit(X_train, y_train)

print(f"Best SVR params: {svr_gs.best_params_}")
svr_best = svr_gs.best_estimator_
y_pred_svr = svr_best.predict(X_test)

joblib.dump(svr_best, "models/model_svr_pca.pkl")
```

**Explanation:**
- **Pipeline**: Chains preprocessing (scaler) and model (SVR)
- **GridSearchCV**: Tests all combinations of hyperparameters
- **cv=3**: 3-fold cross-validation for each combination
- **scoring="neg_mean_squared_error"**: Optimize for MSE (negative because higher is better)
- **Purpose**: Find best hyperparameters automatically
- **Result**: Best params found, R² = 0.8801

---

## 10. Model Evaluation

### Model Comparison

```python
from sklearn.metrics import mean_squared_error, r2_score

preds = {}
preds['LinearRegression'] = lr_pred_log
preds['GradientBoosting'] = gb_pred_log
preds['TunedSVR'] = svr_pred_log
preds['LightGBM'] = lgb_pred_log

results = []
for name, y_pred in preds.items():
    if y_pred is None:
        results.append({'Model': name, 'RMSE_log': np.nan, 'R2_log': np.nan})
        continue
    y_true = np.ravel(y_test)
    y_pred_arr = np.ravel(y_pred)
    mse = mean_squared_error(y_true, y_pred_arr)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred_arr)
    results.append({'Model': name, 'RMSE_log': rmse, 'R2_log': r2})

df_results = pd.DataFrame(results).sort_values(by='RMSE_log')
print(df_results.to_string(index=False))
```

**Explanation:**
- **mean_squared_error**: Calculates MSE (average squared error)
- **np.sqrt(mse)**: Converts to RMSE (root mean squared error)
- **r2_score**: Calculates R² (variance explained)
- **Purpose**: Compare all models on same metrics
- **Result**: Gradient Boosting has lowest RMSE (0.1267) and highest R² (0.9043)

### Prediction Visualization

```python
y_test_original = np.expm1(y_test)
y_pred_original = np.expm1(gb_pred_log)

p2 = figure(width=700, height=600, title='Best Model Prediction Accuracy - GradientBoosting',
           x_axis_label='Actual Sale Price (log scale)', y_axis_label='Predicted Sale Price (log scale)')

source2 = ColumnDataSource({
    'actual': y_test,
    'predicted': gb_pred_log,
    'actual_orig': y_test_original,
    'predicted_orig': y_pred_original
})

p2.scatter('actual', 'predicted', source=source2, size=4, alpha=0.6, color='steelblue')

min_val = min(min(y_test), min(gb_pred_log))
max_val = max(max(y_test), max(gb_pred_log))
p2.line([min_val, max_val], [min_val, max_val], line_width=2, line_color='red',
        line_dash='dashed', legend_label='Perfect Prediction')
```

**Explanation:**
- **np.expm1**: Inverse log transform (converts back to original scale)
- **Scatter plot**: Actual vs Predicted (points closer to diagonal = better)
- **Red diagonal line**: Perfect prediction line (reference)
- **Purpose**: Visual assessment of prediction accuracy
- **Interpretation**: Points on diagonal = accurate predictions

---

## 11. Results Export

### Validation Results Export

```python
# Validation results for best model (GradientBoosting)
y_actual = y_test.flatten() if hasattr(y_test, 'flatten') else np.ravel(y_test)
predictions = gb_pred_log.flatten() if hasattr(gb_pred_log, 'flatten') else np.ravel(gb_pred_log)

errors = predictions - y_actual
percentage_error = (errors / y_actual) * 100

results_df = pd.DataFrame({
    'Actual_Price': y_actual,
    'Predicted_Price': predictions,
    'Error': errors,
    'Absolute_Error': np.abs(errors),
    'Percentage_Error': percentage_error,
    'Absolute_Percentage_Error': np.abs(percentage_error)
})

results_df.to_csv('house_price_validation_results.csv', index=False)
print(f"Validation results saved to 'house_price_validation_results.csv'")
print(f"Total validation samples: {len(results_df)}")
```

**Explanation:**
- **flatten/ravel**: Converts to 1D array (handles different array shapes)
- **Error calculation**: Difference between actual and predicted
- **Percentage error**: Error as percentage of actual value
- **Absolute percentage error**: Always positive (for averaging)
- **to_csv**: Saves results to CSV file for analysis
- **Purpose**: Detailed error analysis, export for reporting

### Error Distribution Analysis

```python
results_df = pd.read_csv('house_price_validation_results.csv')

ape_values = results_df['Absolute_Percentage_Error'].values
hist, edges = np.histogram(ape_values, bins=30)

mean_ape = results_df['Absolute_Percentage_Error'].mean()
p.line([mean_ape, mean_ape], [0, max(hist)],
       line_width=2, line_color='red', line_dash='dashed',
       legend_label=f'Mean: {mean_ape:.2f}%')

print(f"Mean Absolute Percentage Error: {results_df['Absolute_Percentage_Error'].mean():.2f}%")
print(f"Median Absolute Percentage Error: {results_df['Absolute_Percentage_Error'].median():.2f}%")
print(f"95th Percentile: {results_df['Absolute_Percentage_Error'].quantile(0.95):.2f}%")
```

**Explanation:**
- **Histogram**: Distribution of percentage errors
- **Mean APE**: Average absolute percentage error (0.76%)
- **Median APE**: Middle value (0.54%) - less affected by outliers
- **95th percentile**: 95% of predictions have error below this value (2.35%)
- **Purpose**: Understand error distribution, identify problematic predictions
- **Interpretation**: Very low errors indicate highly accurate model

---

## Key Code Patterns

### 1. Data Preprocessing Pattern

```python
# Standard pattern: Check → Handle → Verify
missing_pct = (data.isnull().sum() / len(data)) * 100  # Check
high_missing = missing_pct[missing_pct > 50].index.tolist()  # Identify
data = data.drop(columns=high_missing)  # Handle
print(f"Remaining missing: {data.isnull().sum().sum()}")  # Verify
```

### 2. Feature Engineering Pattern

```python
# Pattern: Combine related features
datan['TotalSF'] = datan['TotalBsmtSF'] + datan['1stFlrSF'] + datan['2ndFlrSF']

# Pattern: Create binary features
datan['HasGarage'] = (datan['GarageArea'] > 0).astype(int)

# Pattern: Create interaction features
datan['QualityScore'] = datan['OverallQual'] * datan['OverallCond']
```

### 3. Model Training Pattern

```python
# Standard pattern: Split → Train → Predict → Evaluate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = ModelClass(hyperparameters)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = r2_score(y_test, y_pred)
```

### 4. Model Saving Pattern

```python
# Save model for later use
import joblib
joblib.dump(model, "models/model_name.pkl")

# Load model later
model = joblib.load("models/model_name.pkl")
```

---

## Summary

This document covers all critical code sections in the notebook:

1. **Data Acquisition**: Kaggle API setup and data loading
2. **Data Audit**: Shape, types, missing values, duplicates
3. **EDA**: Statistics, visualizations, correlations
4. **Data Cleaning**: Missing value imputation, outlier handling
5. **Feature Engineering**: Creating new informative features
6. **Feature Encoding**: One-hot and label encoding
7. **Feature Selection**: Multiple methods (MI, F-test, RFECV, Lasso)
8. **Dimensionality Reduction**: PCA
9. **Model Training**: 4 different models
10. **Model Evaluation**: Metrics and visualizations
11. **Results Export**: Saving predictions and error analysis

Each code section is explained with:
- **What it does**: Simple description
- **Why it's important**: Purpose and impact
- **Key parameters**: Important settings
- **Results**: What to expect

---

*Prepared for: Advanced Apex Project - Phase 4 VIVA*
*Project: House Price Prediction using Machine Learning*
*Last Updated: Based on protected_apex_project_phase4_deliverable.ipynb*

