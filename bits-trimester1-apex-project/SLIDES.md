# House Price Prediction - Presentation Deck

## Slide 1: Title Slide
**House Price Prediction using Machine Learning**

Advanced Apex Project - Phase 4
BITS Pilani Digital
Dr. Naga Janapati

---

## Slide 2: Problem Statement
**Business Goal**

Predict house sale prices to help:
- Real estate agents and buyers make informed decisions
- Financial institutions assess property values for loans
- Homeowners understand their property's market value
- Investors identify undervalued properties

**Challenge:** Build an accurate regression model using property features

---

## Slide 3: Dataset Overview
**Kaggle: House Prices - Advanced Regression Techniques**

- **Source:** Kaggle Competition
- **Training Samples:** 1,460 houses
- **Features:** 81 property characteristics
- **Target:** SalePrice (house sale price)
- **Location:** Ames, Iowa housing data

**Features Include:**
- Property size, quality ratings, location
- Age, building type, amenities
- Garage, basement, exterior features

---

## Slide 4: Methodology
**End-to-End ML Pipeline**

1. **Data Acquisition** → Download via Kaggle API
2. **Data Audit** → Shape, types, missing values analysis
3. **Exploratory Data Analysis** → Univariate & bivariate visualizations, correlations
4. **Data Cleaning** → Handle missing values, outlier Winsorization (1st-99th percentile), duplicates
5. **Feature Engineering** → Create 10 new features (TotalSF, PropertyAge, QualityScore, TotalBath, etc.)
6. **Feature Selection** → Multi-method approach:
   - Mutual Information, F-test, Random Forest importance
   - RFECV (24 features), Lasso regularization (23 features)
   - Final: 35 selected features
7. **Dimensionality Reduction** → PCA (20 components, 95% variance retained)
8. **Modeling** → Built 4 regression models on log-transformed target
9. **Evaluation** → RMSE, R² metrics on log scale

---

## Slide 5: Key Findings - Data Insights
**What We Discovered**

- **Missing Values:** Handled strategically (dropped >50% missing: Alley, MasVnrType, PoolQC, Fence, MiscFeature)
- **Outliers:** Winsorized at 1st-99th percentile to cap extreme values
- **Top Price Drivers (by Mutual Information):**
  - TotalSF (67.99% MI score)
  - OverallQual (57.53% MI score)
  - GrLivArea (47.76% MI score)
  - QualityScore (44.64% MI score)
- **Feature Selection:** 35 features selected from 81 using multiple methods
- **Dimensionality Reduction:** PCA reduced to 20 components (95% variance retained)

---

## Slide 6: Model Performance
**Results Comparison (Log-Transformed Target)**

| Model | R² Score | RMSE (log scale) |
|-------|----------|------------------|
| **Gradient Boosting** ⭐ | **0.9043** | **0.1267** |
| LightGBM | 0.9001 | 0.1295 |
| Linear Regression | 0.8942 | 0.1333 |
| Tuned SVR | 0.8801 | 0.1419 |

**Best Model: Gradient Boosting Regressor**
- 90.43% variance explained
- Trained on PCA-reduced features (20 components)
- Log-transformed target for better distribution

---

## Slide 7: Business Value & Insights
**Key Takeaways**

✅ **Model Accuracy:** 90.4% variance explained (R² = 0.9043)
✅ **Robust Pipeline:** Multi-method feature selection + PCA dimensionality reduction
✅ **Top Predictors:** Total Square Footage and Overall Quality are most important
✅ **Actionable Insight:** Focus on size and quality improvements for maximum ROI

**Applications:**
- Automated price estimates
- Faster property valuations
- Better investment decisions
- Data-driven pricing strategies

---

## Slide 8: Conclusion & Next Steps
**Project Summary**

**Achievements:**
- Complete ML pipeline from data to predictions
- Multiple models evaluated and compared (4 algorithms)
- Strong predictive performance (90.4% R² score)
- Comprehensive feature selection and PCA dimensionality reduction
- Clear business insights delivered

**Future Improvements:**
- Hyperparameter optimization
- Cross-validation for robustness
- Ensemble methods
- Production deployment

**Thank You!**

