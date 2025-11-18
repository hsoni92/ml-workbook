# Refactor Notebook for Kaggle House Prices Dataset

## Current State

The notebook currently:

- Downloads India housing prices dataset via Kaggle API
- Has 250k rows with 23 columns including location (State, City), property features (BHK, Size_in_SqFt), and target (Price_in_Lakhs)
- Performs data audit, EDA, cleaning, feature engineering, and feature selection
- Uses amenities column for one-hot encoding
- Applies LabelEncoder to categorical features
- Trains RandomForest and evaluates feature importance

## Main Steps

### 1. Data Download

- Change download command from `kaggle datasets download` to `kaggle competitions download -c house-prices-advanced-regression-techniques`
- Update unzip to extract train.csv and test.csv
- Load train.csv as primary dataset (1460 rows, 81 columns)

### 2. Column Mapping

Map analysis steps to new column schema:

- **Target**: Price_in_Lakhs → SalePrice
- **Size**: Size_in_SqFt → GrLivArea (or create total area feature)
- **Bedrooms**: BHK → BedroomAbvGr
- **Location**: State/City → Neighborhood (single column)
- **Property Type**: Property_Type → BldgType, HouseStyle
- **Year Built**: Year_Built → YearBuilt (already exists)
- **Age**: Age_of_Property → calculate from YearBuilt
- **Quality**: No direct equivalent → use OverallQual, OverallCond
- **Garage**: Parking_Space → GarageArea, GarageCars
- **Basement**: No equivalent → use TotalBsmtSF, BsmtQual

### 3. Data Audit

Keep same checks, adapt for new columns:

- Shape analysis (expect ~1460 rows, 81 columns)
- Data types check
- Missing values analysis (Kaggle dataset has many missing values unlike current)
- Negative value checks for numeric columns
- Duplicate rows check

### 4. Exploratory Data Analysis (EDA)

Adapt visualizations:

- Summary statistics for numeric features
- Categorical value counts (Neighborhood, HouseStyle, etc.)
- Average prices by: Neighborhood, OverallQual, BldgType
- Univariate histograms for: SalePrice, GrLivArea, YearBuilt, OverallQual
- Correlation heatmap
- Bivariate plots: Neighborhood vs SalePrice, OverallQual vs SalePrice, BldgType vs SalePrice

### 5. Data Cleaning

- **Handle missing values** (critical for Kaggle dataset):
  - Drop high-missing columns (>50%)
  - Impute numerical: median/mean
  - Impute categorical: mode or 'None' for applicable features
- Drop irrelevant columns: Id (like current ID column)
- Remove duplicates
- Outlier detection using IQR method on numeric columns

### 6. Feature Engineering

Replace amenities parsing with relevant feature creation:

- **Total area features**: TotalSF = TotalBsmtSF + 1stFlrSF + 2ndFlrSF
- **Age features**: PropertyAge = YrSold - YearBuilt, RemodAge = YrSold - YearRemodAdd
- **Binary features**: HasGarage, HasBasement, HasFireplace
- **Quality interaction**: QualityScore = OverallQual * OverallCond
- One-hot encode categorical features (instead of single Amenities column)

### 7. Encoding & Feature Selection

- Apply LabelEncoder to remaining categorical features
- Run Mutual Information Regression analysis
- Run F-regression feature scoring
- Train RandomForest for feature importance
- Keep top features based on importance scores

### 8. Model Construction

Build at least one appropriate basic regression model:

- **Simple Linear Regression**: Use single most important feature (e.g., GrLivArea or OverallQual) to predict SalePrice
- **Multiple Linear Regression**: Use top selected features from feature selection phase
- Document model construction steps clearly in notebook
- Show data input (train/test split or cross-validation setup)
- Show model construction steps (feature selection, model fitting)

### 9. Model Evaluation

Compute relevant regression evaluation metrics:

- **RMSE** (Root Mean Squared Error): Primary metric for house price prediction
- **MAE** (Mean Absolute Error): Interpretable in dollars
- **R²** (Coefficient of Determination): Measure of model fit
- Display metrics clearly with interpretation
- Show model interpretation (coefficients, feature importance)

### 10. Visualization & Storytelling

**Option A: Tableau / Power BI (preferred, if comfortable)**

- **Interactive Dashboard (1–2 dashboards):**
  - Show results from EDA (e.g., price distribution by neighborhood, quality vs price)
  - Include key metrics (KPIs): Median SalePrice, Model RMSE, R² score
  - Include dimensions (filters): Neighborhood, OverallQual, BldgType, YearBuilt range
  - Show model predictions vs actual prices if possible

- **5-Slide Story Deck (PDF/PPT):**
  - Title & project context (House Price Prediction using Kaggle dataset)
  - Visual highlights (EDA or model results)
  - Key metric(s) / dimension(s) (RMSE, R², top features)
  - 1–2 key observations (what the charts show - e.g., "Neighborhood significantly impacts price", "OverallQual is strongest predictor")
  - Simple conclusion or "next steps" (model improvements, additional features)

**Option B: Matplotlib / Seaborn (Notebook-based)**

- **Notebook with 3–5 clear plots (serves as a static dashboard):**
  - Plots from EDA: SalePrice distribution, correlation heatmap, price by neighborhood/quality
  - Model results: Predicted vs Actual scatter plot, residual plots, feature importance
  - Segmented plots (e.g., price by bedrooms, price by quality levels)
  - Include 1–2 key metrics in text cells (RMSE, R², MAE)

- **5-Slide Story Deck (same as Option A)**

## Files Modified

- `apex_project_common.ipynb`: All cells will be updated with new column references and logic

## Key Considerations

- Kaggle dataset has significant missing values (current has none) - must handle carefully
- Many more features (81 vs 23) - may need more selective feature engineering
- Different scale (SalePrice in dollars vs lakhs) - may need different visualizations
- No multi-category amenities column - different approach for categorical encoding
