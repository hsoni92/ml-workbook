# House Price Prediction - Advanced Apex Project

## Problem Statement / Business Goal

This project aims to predict house sale prices using machine learning regression techniques. Accurate house price prediction helps real estate agents and buyers make informed decisions, enables financial institutions to assess property values for loans, assists homeowners in understanding their property's market value, and helps investors identify undervalued properties.

## Dataset Source

**Dataset:** House Prices - Advanced Regression Techniques
**Source:** Kaggle Competition
**URL:** https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
**Citation:** Kaggle Competition - House Prices: Advanced Regression Techniques

The dataset contains 1,460 training samples with 81 features including property characteristics (size, quality, location, age, etc.) and the target variable `SalePrice`. The data is based on actual housing sales in Ames, Iowa.

## Steps to Run the Notebooks

### Prerequisites

1. **Python Environment**: Ensure Python 3.7+ is installed
2. **Kaggle API**: You'll need a Kaggle account and API credentials

### Installation Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Kaggle API credentials (if not already configured):**
   - Create a Kaggle account at https://www.kaggle.com
   - Go to Account → API → Create New Token to download `kaggle.json`
   - Place `kaggle.json` in `~/.kaggle/` directory (or follow the notebook instructions)

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook --no-browser
   ```
   Or use JupyterLab:
   ```bash
   jupyter lab
   ```

4. **Open and run the notebooks:**
   - **Phase 2 Notebook:** `protected_apex_project_phase2_deliverable.ipynb` - Contains data preprocessing, EDA, and feature engineering
   - **Phase 4 Notebook:** `protected_apex_project_phase4_deliverable.ipynb` - Contains complete pipeline including:
     - Data audit and availability check
     - Exploratory Data Analysis (EDA) with univariate and bivariate visualizations
     - Data cleaning (missing value handling, outlier detection and Winsorization)
     - Feature engineering (10 new features created)
     - Feature selection using multiple methods (Mutual Information, F-test, Random Forest, RFECV, Lasso)
     - PCA dimensionality reduction (20 components for 95% variance retention)
     - Model training with 4 algorithms (Gradient Boosting, LightGBM, Linear Regression, Tuned SVR)
     - Model evaluation and comparison

   The notebooks will automatically download the dataset using the Kaggle API when executed.

5. **Run all cells:** Execute all cells sequentially (Cell → Run All) or run cells individually to follow the analysis step-by-step.

### Note

The notebooks are configured to automatically download the dataset from Kaggle using the API. Ensure your Kaggle credentials are properly set up before running the data download cells.
