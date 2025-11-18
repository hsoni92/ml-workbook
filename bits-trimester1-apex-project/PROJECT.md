# Advanced Apex Project - 1

**Instructor:** Dr. Naga Janapati
**Position:** Associate Professor, BITS Pilani Digital
**Credits:** 2

## Overview

An Apex project is a project with higher order skills as outcomes by integrating the learning from multiple courses, typically in the same trimester.

## Learning Objectives

By the end of the Advanced Apex Project, students should be able to:

- Integrate data preprocessing, feature engineering, modelling and visualization into a coherent pipeline.
- Handle end-to-end data challenges.
- Communicate insights through dashboards and introductory storytelling with visuals.

## Phases & Student Deliverables

### Phase 1: Proposal & Data Acquisition (Weeks 2-3)

**Overview:** Teams formed. Supervisor assigned. Problem statement given.

**Deliverables:**

1. **1–2-page Proposal (PDF/Word):**
   - Project Title, Problem statement & business goal (Ex. House Price prediction, customer segmentation or Demand forecasting, etc.)
   - Data Sources: Ex. Kaggle, UCI ML, GitHub, etc.
   - Tools: Python, Pandas, Matplotlib/Seaborn, Tableau/PBI, etc.
   - Work flow: High-level flow of the project (e.g., Data acquisition → Preprocessing → Feature Engineering → Modelling → Visualization).

2. **Data Extraction:**
   - From Kaggle, UCI ML, GitHub, etc. (Use Kaggle API or direct download; optional use of publicly enabled AWS S3 buckets for extra practice).
   - A short notebook or script showing how the dataset is pulled (API call / download) and saved reproducibly.

3. **Schema/Data dictionary:**
   - Data Model Excel sheet: Feature – Data type – Description – PK (Yes/No)
   - *Note: Students should prepare this document by checking the metadata file provided with the dataset (if available). If no metadata is provided, they need to do a quick Python-based inspection of the extracted dataset.*

---

### Phase 2: Preprocessing & Feature Engineering (Weeks 4-7)

**NOTE:** Students should perform only the tasks that are relevant to their dataset and model. They are not expected to do every single step listed below.

**Deliverables:**

1. **Data Audit & Data Availability Check:**
   - Check shape, data types, missing values, quality flags (e.g., negative ages), etc. (df.shape, df.dtypes, df.isnull().sum(), etc)
   - Check if the task relevant columns are available. (Eg. Loan Approval Application: Annual Income, Employee?, etc)

2. **Exploratory Data Analysis (EDA):**
   - Summary statistics: .describe(), .quantile(), .value_counts(), Correlations (df.corr()), slicing/dicing, roll-up, etc.
   - Visualizations:
     - Univariate: histograms/KDE (numeric), bar/count plots (categorical).
     - Bivariate: scatter plots, boxplots, crosstabs.
     - Multivariate: correlation heatmap, pair plots.

3. **Data Cleaning:**
   - Drop irrelevant columns (e.g., Cust_Name).
   - Drop the columns with too many missing values.
   - Impute missing values: (mean/median/mode/forward fill/backward fill; justify, e.g., "Median for skewed 'salary'", etc).
   - Remove duplicates.
   - Handle outliers: (IQR/z-score; cap/remove).
   - Convert types: e.g., strings to datetime, etc.

4. **Feature Engineering:**
   - Data scaling/normalization (MinMax, Z-score), categorical encoding (One-Hot, Label, Target, etc.).
   - Feature extraction from raw data/existing features.
     - Ex. Extracting "Days Since Purchase"/"Purchase_Recency" from purchase_date and current_date, ratios like CPM (Cost Per Mile) from some other existing features, etc.
   - Feature subset selection:
     - Select task-relevant features using filter methods (e.g., correlation analysis, multicollinearity check)
   - Dimensionality Reduction (optional):
     - PCA, SVD, DWT, etc.
   - *NOTE: Depending on Model to be constructed, engineer at least a minimum set of task-relevant features.*

5. **Documentation:**
   - Jupyter Notebook, document each step inline (code + outputs + explanations).
   - Place observations/insights close to the relevant code/output.
   - At the end, include a final summary/conclusion (often a markdown cell summarizing all key findings).

---

### Phase 3: Modeling & Inferencing (Weeks 8-9)

**Deliverables:**

1. **Model Construction:**
   - Build at least one appropriate basic model based on the problem type, such as:
     - Regression Models: Simple Linear Regression, Multiple Linear Regression.
     - Clustering Models: e.g., K-Means, Hierarchical Clustering.
     - Time Series Models (Univariate): Forecasting using engineered features like Moving Average, Exponential Moving Average, etc.
       - (Students should explore which feature/method forecasts the next month/day value most effectively.)

2. **Evaluation Metrics:**
   - Compute relevant evaluation metrics, such as:
     - Regression → RMSE, MAE, R²
     - Clustering → Silhouette Score, Davies–Bouldin Index
     - Time Series → RMSE, MAPE

3. **Presentation:**
   - Notebook should clearly show:
     - Data input
     - Model construction steps
     - Metric computation & output

---

### Phase 4: Visualization & Storytelling (Week 10)

**Option A: Tableau / Power BI (preferred, if comfortable)**

- **Interactive Dashboard (1–2 dashboards):**
  - Show results from EDA and/or model outcomes.
  - Include 1–2 key metrics (KPIs) (e.g., Median Price, RMSE) if available.
  - Include 1–2 dimensions (filters) (e.g., City, Bedrooms) for simple interactivity.

- **5-Slide Story Deck (PDF/PPT):**
  - Title & project context.
  - Visual highlights (EDA or model results).
  - Key metric(s) / dimension(s) if available.
  - 1–2 key observations (what the charts show).
  - Simple conclusion or "next steps."

**Option B: Matplotlib / Seaborn (Notebook-based)**

- **Notebook with 3–5 clear plots (serves as a static dashboard):**
  - Plots from EDA and/or model outcomes.
  - If filters are not possible, show segmented plots (e.g., price by bedrooms).
  - Include 1–2 key metrics in text cells (if available).

- **5-Slide Story Deck (same as Option A).**

---

### Phase 5: Documentation & Submission (Week 10)

**Deliverables:**

1. **Final code (Jupyter Notebooks):**
   - All their analysis (Cleaning, EDA, Feature Engineering, modelling, visualization) in one or more well-structured notebooks.

2. **README:**
   - Short guide for reviewing the project. Include:
     - Problem statement / business goal (1–2 sentences)
     - Dataset source(s) and clear citation (URL or name, e.g., Kaggle/UCI)
     - Steps to run the notebooks (e.g., pip install -r requirements.txt → open notebook → run all cells)

3. **Source Links:**
   - Explicit reference to original datasets: Kaggle URL, UCI ML link, or GitHub repo link
   - Include small note if sample data is provided due to privacy

4. **Dashboard Output:**
   - Matplotlib/Seaborn path: screenshots of 3–5 key plots OR indicate in the notebook that plots are present
   - Tableau/Power BI path: workbook file (.twbx / .pbix) OR exported screenshots / shareable link
   - Include brief captions or text explaining what the visuals show

5. **requirements.txt:**
   - Python version, key libraries, versions, and dependencies required to run the notebook
   - Example: pandas==2.1.0, numpy==1.25.0, matplotlib==3.8.0, etc.

---

### Phase 6: Presentation & Evaluation (Weeks 11-12)

**Deliverables:**

- Each team will deliver a final presentation summarizing their overall project, supported by a PowerPoint deck, Jupyter Notebook(s), and other relevant artifacts (e.g., dashboard, data dictionary).
- During the presentation, teams should demonstrate their workflow, key findings, and recommendations.
- Every student is expected to have a clear understanding of all phases of the project (proposal, preprocessing, feature engineering, modeling, visualization, and storytelling), not just the part they individually worked on.

---

## Important Notes

*Please note that the timelines provided are indicative. While we will make every effort to adhere to them, any changes, if required, will only involve advancing certain activities to an earlier date.*
