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
3. **Exploratory Data Analysis** → Visualizations, correlations
4. **Data Cleaning** → Handle missing values, outliers, duplicates
5. **Feature Engineering** → Create 10 new features (TotalSF, PropertyAge, QualityScore, etc.)
6. **Feature Selection** → Selected 35 best features from 81
7. **Modeling** → Built 4 regression models
8. **Evaluation** → RMSE, MAE, R² metrics

---

## Slide 5: Key Findings - Data Insights
**What We Discovered**

- **Missing Values:** Handled strategically (dropped >50% missing, imputed others)
- **Top Price Drivers:**
  - Overall Quality (37.8% importance)
  - Total Square Footage (33.8% importance)
  - Quality Score (4.9% importance)
- **Insight:** Quality and size together account for ~72% of price variation

---

## Slide 6: Model Performance
**Results Comparison**

| Model | R² Score | RMSE | MAE |
|-------|----------|------|-----|
| Simple Linear Regression | 0.7466 | $39,010 | - |
| Multiple Linear Regression | 0.9012 | $24,363 | - |
| **Gradient Boosting** ⭐ | **0.9106** | **$23,172** | **$15,310** |
| LightGBM | 0.9102 | $23,229 | - |

**Best Model: Gradient Boosting Regressor**
- 91.06% variance explained
- Average error: ~$15,310 (8.5% of average price)

---

## Slide 7: Business Value & Insights
**Key Takeaways**

✅ **Model Accuracy:** 91% accurate predictions
✅ **Average Error:** ~$15,000 per house
✅ **Top Predictors:** Quality and size are most important
✅ **Actionable Insight:** Focus on quality improvements for maximum ROI

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
- Multiple models evaluated and compared
- Strong predictive performance (91% accuracy)
- Clear business insights delivered

**Future Improvements:**
- Hyperparameter optimization
- Cross-validation for robustness
- Ensemble methods
- Production deployment

**Thank You!**

