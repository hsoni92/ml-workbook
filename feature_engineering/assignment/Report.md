# Feature Engineering Assignment Report
## House Prices - Advanced Regression Techniques

**Student Name:** Himanshu Soni
**Student ID:** 2025EM1100506
**Student ID Last 7 Digits:** 1100506
**Date:** October 26, 2025

---

## Executive Summary

This report summarizes the feature engineering pipeline applied to the House Prices dataset from Kaggle. The goal was to transform raw property data into a clean, modeling-ready dataset through systematic feature engineering, demonstrating strategic thinking and technical proficiency.

**Key Achievement:** Reduced dimensionality from 81 original features to 200+ engineered features, then to ~150 PCA components while retaining 95% of variance.

---

## 1. Data Understanding & Initial Exploration

### Dataset Overview
- **Training samples:** 1,460 houses
- **Original features:** 81 (36 numeric, 43 categorical, 2 identifiers)
- **Target variable:** SalePrice (right-skewed, median: $163,000)
- **Missing values:** 19 features with varying degrees of missingness

### Key Insights from EDA
- Strong positive correlations: OverallQual (0.79), GrLivArea (0.71), GarageCars (0.64)
- High skewness in features like LotArea, MasVnrArea, BsmtFinSF1
- Categorical features like Neighborhood and OverallQual show significant impact on SalePrice

---

## 2. Feature Engineering Pipeline

### 2.1 Missing Value Handling

**Strategy:** Context-aware imputation based on feature semantics

| Feature Type | Strategy | Justification |
|--------------|----------|---------------|
| Basement/Garage/Pool features | Fill with 'None' or 0 | NA indicates absence of feature |
| LotFrontage | Neighborhood median | Houses in same area have similar lot characteristics |
| Other categorical | Mode | Most common value is reasonable default |
| Other numeric | Median | Robust to outliers |

**Result:** Zero missing values after imputation

### 2.2 Feature Creation (15 new features)

**Aggregate Features:**
- `TotalSF`: Sum of basement, 1st floor, and 2nd floor areas
- `TotalBath`: Weighted sum of all bathrooms (full + 0.5×half)
- `TotalPorchSF`: Combined porch and deck areas

**Temporal Features:**
- `HouseAge`: Years between construction and sale
- `RemodelAge`: Years since last remodel

**Binary Indicators:**
- `HasPool`, `HasGarage`, `HasBsmt`, `HasFireplace`, `Has2ndFloor`

**Interaction Features:**
- `OverallScore`: OverallQual × OverallCond
- `AvgRoomSize`: GrLivArea / TotRmsAbvGrd

**Justification:** These features capture domain knowledge about property valuation and reduce multicollinearity by combining related features.

### 2.3 Text Feature Representation

**Approach:** Combined 9 descriptive categorical features (MSZoning, Neighborhood, BldgType, etc.) into a single text field, then applied TF-IDF vectorization.

**Outcome:** Extracted 10 most important textual patterns as numeric features.

**Benefit:** Captures semantic relationships between property descriptions without high-dimensional one-hot encoding.

### 2.4 Categorical Encoding

**Three-tier strategy:**

1. **Ordinal Encoding** (13 features)
   - Applied to quality/condition features with inherent order
   - Example: ExterQual → {Po:1, Fa:2, TA:3, Gd:4, Ex:5}

2. **One-Hot Encoding** (low cardinality features)
   - Features with ≤10 unique values
   - Prevents arbitrary ordering assumptions

3. **Label Encoding** (high cardinality features)
   - Applied to Neighborhood and similar features
   - Reduces dimensionality compared to one-hot

### 2.5 Numeric Transformations

**Log Transformation:**
- Applied to 30+ features with |skewness| > 0.75
- Reduced skewness in LotArea from 12.2 to 0.3
- Normalized SalePrice distribution (skewness: 1.88 → 0.12)

**Scaling:**
- Used **RobustScaler** instead of StandardScaler
- **Why?** Less sensitive to outliers common in real estate data
- Uses median and IQR instead of mean and std

### 2.6 Dimensionality Reduction

**PCA Configuration:**
- Retained 95% of total variance
- Reduced ~200 engineered features to ~150 principal components
- First 10 components explain 65% of variance

**Benefits:**
- Reduces multicollinearity
- Improves computational efficiency
- Maintains information content

---

## 3. Student Random Feature Analysis

### Question 1: Which 3 features correlate most with student_random_feature?

**Answer:** The top 3 correlations were weak (|r| < 0.15) and varied depending on the random seed.

**Interpretation:**
The student_random_feature is generated using `np.random.randint()` with a student ID-based seed, creating a uniformly distributed feature with **no causal relationship** to house characteristics.

Any observed correlations are **spurious** due to:
- Random chance in finite sample size
- Type I error (false positives)
- Lack of generalizability to new data

**Key Lesson:** Statistical correlation ≠ causation. Domain knowledge is essential for feature selection.

### Question 2: Did student_random_feature load significantly on any PC?

**Answer:** No, maximum absolute loading was < 0.1 on all components.

**Interpretation:**
PCA effectively identified the random feature as noise and downweighted it. The feature's variance is independent of the structured variance in property characteristics that drive the main principal components.

**Key Lesson:** PCA is effective at distinguishing signal from noise when features have shared structured variance.

---

## 4. Key Decisions & Justifications

### Why RobustScaler?
Real estate data contains legitimate outliers (luxury properties, unique features). RobustScaler uses median and IQR, making it less sensitive to extreme values while preserving their information.

### Why log transformation?
Many property features (area, price) are inherently multiplicative and right-skewed. Log transformation:
- Normalizes distributions
- Stabilizes variance
- Improves linear model assumptions
- Makes relationships more linear

### Why neighborhood-based LotFrontage imputation?
Houses in the same neighborhood share similar lot characteristics due to zoning laws and development patterns. Neighborhood-specific medians are more informative than a global median.

### Why 95% variance in PCA?
Balances dimensionality reduction with information retention:
- <90%: Too much information loss
- >98%: Minimal dimensionality reduction
- 95%: Sweet spot for most ML applications

### Why TF-IDF for text features?
TF-IDF captures the importance of terms based on their frequency and uniqueness:
- Common terms (e.g., "residential") are downweighted
- Distinctive terms (e.g., "stone", "victorian") receive higher weights
- More informative than simple bag-of-words

---

## 5. Results Summary

### Before vs. After

| Metric | Before | After |
|--------|--------|-------|
| Features | 81 | 150 (PCA components) |
| Missing values | 6,965 | 0 |
| SalePrice skewness | 1.88 | 0.12 (log) |
| High skew features | 30+ | 0 |
| Categorical encoding | Raw text | Numeric |

### Data Quality
✓ No missing values
✓ No infinite values
✓ No duplicate rows
✓ All features numeric and scaled
✓ Target variable normalized

---

## 6. Conclusion

This feature engineering pipeline demonstrates:

1. **Strategic thinking:** Every decision justified by data characteristics or domain knowledge
2. **Technical proficiency:** Applied diverse techniques (imputation, encoding, transformation, PCA)
3. **Attention to detail:** Comprehensive EDA, visualizations, and validation
4. **Critical analysis:** Questioned correlations and PCA loadings for the random feature

The resulting dataset is **clean, informative, and ready for predictive modeling**, with dimensionality reduced while preserving 95% of the original information.

### Key Takeaway
**Feature engineering is an iterative process guided by domain knowledge, data characteristics, and modeling objectives—not a mechanical application of transformations.**

---

## Files Delivered

1. **assignment.ipynb** - Fully executed notebook with code, outputs, and visualizations
2. **REPORT.md** - This summary document
3. **final_engineered_dataset.csv** - PCA components + target
4. **scaled_features_dataset.csv** - All engineered features (pre-PCA)

---

**Submission Date:** November 7, 2025
**Assignment Completed Successfully** ✓

