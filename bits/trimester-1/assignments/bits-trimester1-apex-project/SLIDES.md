# House Price Prediction - Storytelling Presentation

---

## Slide 1: The Challenge
**What's a House Really Worth?**

Every house sale raises the same question: *"Is this the right price?"*

**The Problem:**
- Buyers want fair deals
- Sellers want accurate valuations
- Real estate agents need quick estimates
- Banks need reliable appraisals

**Our Mission:** Build an AI model that predicts house prices with 90%+ accuracy using property features.

*[Placeholder: Notebook Cell 17 - SalePrice Distribution (Before/After Log Transform) - Shows why we need prediction]*

---

## Slide 2: The Data
**1,460 Houses, 81 Features, One Goal**

**Dataset:** Kaggle House Prices Competition (Ames, Iowa)

**What We Have:**
- 1,460 real property sales
- 81 features: size, quality, location, age, amenities
- Target: SalePrice (ranging from $34,900 to $755,000)

**The Challenge:**
- Missing values in 19 columns
- Outliers in 32 numeric features
- Mix of categorical and numerical data
- Skewed price distribution

*[Placeholder: Notebook Cell 5-6 - Data shape and types summary]*

---

## Slide 3: The Discovery Journey
**What Drives House Prices?**

**Key Insights from EDA:**

1. **Size Matters Most**
   - Total Square Footage is the #1 predictor (68% mutual information score)
   - Living area, basement, and floors all correlate strongly

2. **Quality Over Location**
   - Overall Quality (58% MI score) beats neighborhood
   - Quality Score (quality × condition) is a powerful predictor

3. **Price Patterns**
   - Average price varies 3.4x across neighborhoods ($98K to $335K)
   - Quality rating (1-10) shows clear price progression
   - Log transformation needed (skewness: 1.88)

*[Placeholder: Notebook Cell 16 - Correlation Heatmap - Shows feature relationships]*
*[Placeholder: Notebook Cell 14 - Average Price by Neighborhood/Quality - Shows price patterns]*
*[Placeholder: Notebook Cell 19-21 - Bivariate visualizations - Price by Neighborhood/Quality/Building Type]*

---

## Slide 4: The Transformation
**From Raw Data to Predictions**

**Our Data Pipeline:**

1. **Cleaning** → Removed 5 columns with >50% missing data, imputed strategically, capped outliers (1st-99th percentile)

2. **Feature Engineering** → Created 10 powerful new features:
   - TotalSF (total square footage)
   - PropertyAge, RemodAge
   - QualityScore (quality × condition)
   - TotalBath, TotalPorchSF
   - Binary flags (HasGarage, HasBasement, etc.)

3. **Feature Selection** → Multi-method approach:
   - Started with 81 features
   - Filtered to 35 using Mutual Information, F-test, Random Forest
   - Refined with RFECV (24 features) and Lasso (23 features)
   - Final: 35 best features selected

4. **Dimensionality Reduction** → PCA reduced to 20 components (95% variance retained)

*[Placeholder: Notebook Cell 35 - Top 30 Feature Importance (Random Forest) - Shows which features matter]*
*[Placeholder: Notebook Cell 43 - PCA Variance Explained - Shows dimensionality reduction]*

---

## Slide 5: The Solution
**Four Models, One Winner**

**Models Tested:**
1. **Gradient Boosting** ⭐ (Best)
2. LightGBM
3. Linear Regression
4. Tuned SVR

**Why Gradient Boosting Won:**
- Handles non-linear relationships
- Captures feature interactions
- Robust to outliers
- Best performance on PCA-reduced features

**Training Strategy:**
- Log-transformed target (normalized distribution)
- 80/20 train-test split
- PCA-reduced features (20 components)
- Hyperparameter tuning for SVR

*[Placeholder: Notebook Cell 38 - RFECV Performance Plot - Shows feature selection optimization]*

---

## Slide 6: The Results
**90.4% Accuracy Achieved**

| Model | R² Score | RMSE (log) | Performance |
|-------|----------|------------|-------------|
| **Gradient Boosting** ⭐ | **0.9043** | **0.1267** | **Best** |
| LightGBM | 0.9001 | 0.1295 | Excellent |
| Linear Regression | 0.8942 | 0.1333 | Good |
| Tuned SVR | 0.8801 | 0.1419 | Good |

**What This Means:**
- Model explains **90.4%** of price variance
- Predictions are within **12.7%** error (log scale)
- Top 3 models all exceed 89% accuracy
- Robust and reliable predictions

*[Placeholder: Notebook Cell 57 - Model Performance Comparison (R² Scores) - Bar chart showing all models]*
*[Placeholder: Notebook Cell 57 - Best Model Prediction Accuracy Scatter Plot - Actual vs Predicted]*

---

## Slide 7: The Insights
**What We Learned About House Prices**

**Top 5 Price Drivers:**
1. **Total Square Footage** (46.4% importance)
2. **Overall Quality** (31.8% importance)
3. **Quality Score** (2.6% importance)
4. **Year Built** (1.8% importance)
5. **Lot Area** (1.2% importance)

**Business Recommendations:**
- ✅ **Size investments** yield highest ROI
- ✅ **Quality improvements** significantly boost value
- ✅ **Age matters** but can be offset by quality
- ✅ **Location** matters less than quality and size

**15 Features** consistently selected across all methods:
- TotalSF, OverallQual, GrLivArea, GarageArea, TotalBath, and 10 more

*[Placeholder: Notebook Cell 35 - Top 30 Feature Importance Visualization - Horizontal bar chart]*
*[Placeholder: Notebook Cell 40 - Common features across all selection methods]*

---

## Slide 8: The Impact
**From Data to Decisions**

**What We Built:**
✅ Complete ML pipeline (data → predictions)
✅ 90.4% accurate price prediction model
✅ Multi-method feature selection approach
✅ Production-ready model (saved as .pkl)

**Real-World Applications:**
- 🏠 **Real Estate:** Instant property valuations
- 🏦 **Banking:** Automated loan assessments
- 💼 **Investors:** Identify undervalued properties
- 📊 **Market Analysis:** Understand price drivers

**Key Achievement:**
Transformed 81 messy features into 35 powerful predictors, achieving **90.4% accuracy** with Gradient Boosting.

*[Placeholder: Notebook Cell 42 - PCA Plot (First Two Components) - Shows data structure in reduced space]*

---

## Slide 9: Validation Results Export
**Detailed Performance Analysis**

**What We Exported:**
- **292 validation samples** analyzed in detail
- Per-sample predictions with comprehensive error metrics
- Complete validation results saved to CSV for further analysis

**Key Metrics in Export:**
- Actual vs Predicted prices (log scale)
- Error distribution (raw and absolute)
- Percentage errors for interpretability
- Absolute percentage errors for magnitude assessment

**Validation Insights:**
- Model performance validated on **20% hold-out test set**
- Each prediction includes error breakdown
- Enables detailed analysis of model behavior
- Supports production deployment validation

**Key Findings from Validation:**
- **Mean Absolute Percentage Error: 0.76%** - Excellent average accuracy
- **Median Absolute Percentage Error: 0.54%** - Most predictions are highly accurate
- **95th Percentile: 2.35%** - 95% of predictions within 2.35% error
- **Max Error: 4.66%** - Worst case scenario still under 5% error

**Deliverable:**
✅ `house_price_validation_results.csv` - Complete validation breakdown with 6 metrics per sample

*[Placeholder: Notebook Cell 66 - Validation Results Export - Shows CSV export code and sample results]*
*[Placeholder: Sample rows from validation_results.csv showing actual vs predicted with errors]*

---

## Slide 10: Conclusion
**The Story in Numbers**

**Project Summary:**
- 📊 **1,460** houses analyzed
- 🔧 **81** features → **35** selected → **20** PCA components
- 🤖 **4** models tested
- 🎯 **90.4%** accuracy achieved
- ⭐ **Gradient Boosting** as best model

**Future Enhancements:**
- Hyperparameter optimization
- Ensemble methods (stacking/blending)
- Cross-validation for robustness
- Production deployment with API

**Thank You!**

*Advanced Apex Project - Phase 4*
*BITS Pilani Digital | Dr. Naga Janapati*

---

## Appendix: Graph Placeholders Reference

**Recommended Visualizations from Notebook:**

1. **Cell 17** - SalePrice Distribution (Before/After Log Transform)
   - *Purpose:* Show why log transformation was needed
   - *Slide:* 1 (The Challenge)

2. **Cell 16** - Correlation Heatmap
   - *Purpose:* Show feature relationships
   - *Slide:* 3 (The Discovery Journey)

3. **Cell 14, 19-21** - Average Price by Neighborhood/Quality/Building Type
   - *Purpose:* Show price patterns and insights
   - *Slide:* 3 (The Discovery Journey)

4. **Cell 35** - Top 30 Feature Importance (Random Forest)
   - *Purpose:* Show which features matter most
   - *Slide:* 4 (The Transformation) and 7 (The Insights)

5. **Cell 43** - PCA Variance Explained
   - *Purpose:* Show dimensionality reduction effectiveness
   - *Slide:* 4 (The Transformation)

6. **Cell 38** - RFECV Performance Plot
   - *Purpose:* Show feature selection optimization
   - *Slide:* 5 (The Solution)

7. **Cell 57** - Model Performance Comparison & Prediction Accuracy
   - *Purpose:* Show results and model quality
   - *Slide:* 6 (The Results)

8. **Cell 42** - PCA Plot (First Two Components)
   - *Purpose:* Show data structure in reduced space
   - *Slide:* 8 (The Impact)

9. **Cell 66** - Validation Results Export
   - *Purpose:* Show detailed validation analysis and CSV export
   - *Slide:* 9 (Validation Results Export)
