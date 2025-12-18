# Feature Engineering Question Paper 3

## Question 1 (10 marks)

You are working on a credit-risk prediction model for a bank. The dataset contains the following columns:

- **Loan_ID** - Unique identifier for each loan
- **Applicant_Income** - Monthly income of the borrower
- **Loan_Purpose** - Category describing why the loan was taken (17 unique categories)
- **Default_Flag** - Target variable (1 = default, 0 = non-default)

Answer the following:

### Q1.1 (2 marks)

Should Loan_ID be included as a feature in the model? Explain your reasoning.

**Answer:**

No, Loan_ID should not be included as a feature in the model. Loan_ID is a unique identifier for each loan application and does not contain any meaningful information about the credit risk. Including it would:

1. **Cause overfitting**: Since each Loan_ID is unique, the model would memorize individual loan IDs rather than learning general patterns about credit risk.
2. **No predictive value**: The identifier is randomly assigned and has no relationship with the likelihood of default.
3. **Data leakage risk**: If used, it could lead to perfect memorization of training data but poor generalization to new loans.

Loan_ID should only be used for tracking and joining datasets, not as a feature for modeling.

### Q1.2 (3 marks)

Loan_Purpose contains 17 categories with no ordinal meaning.

(a) Should you use Ordinal Encoding? Why or why not?

(b) Suggest a more suitable encoding method and briefly describe how it works.

**Answer:**

**(a) Should you use Ordinal Encoding? Why or why not?**

No, Ordinal Encoding should not be used for Loan_Purpose. Ordinal encoding assigns numeric values (e.g., 0, 1, 2, ...) to categories, which implies an inherent order or ranking. Since Loan_Purpose has 17 categories with no ordinal meaning (e.g., "Home Improvement", "Debt Consolidation", "Business"), using ordinal encoding would:

- Create artificial relationships: The model might interpret "Business" (encoded as 2) as being "greater than" "Home Improvement" (encoded as 1), which is meaningless.
- Introduce bias: Algorithms like linear models would treat the encoded values as having magnitude relationships that don't exist in reality.

**(b) Suggest a more suitable encoding method and briefly describe how it works.**

**One-Hot Encoding** (or dummy encoding) is the most suitable method for nominal categorical variables like Loan_Purpose.

**How it works:**
- Each category is converted into a binary column (0 or 1).
- For 17 categories, this creates 17 binary features (or 16 if using one less to avoid multicollinearity).
- Each row has a value of 1 in the column corresponding to its category and 0 in all other columns.
- This treats each category as independent with no implied order or hierarchy.

**Alternative:** Target Encoding (or Mean Encoding) could also be used, where each category is replaced with the mean of the target variable (Default_Flag) for that category. This can be more compact and sometimes more informative, but requires careful handling to avoid overfitting.

### Q1.3 (3 marks)

Applicant_Income is extremely right-skewed.

(a) Name one transformation technique you can apply.

(b) Explain why this transformation helps the model.

**Answer:**

**(a) Name one transformation technique you can apply.**

**Log Transformation** (specifically, natural log: log(Applicant_Income) or log(1 + Applicant_Income) to handle zeros).

**Alternative transformations:** Square root transformation, Box-Cox transformation, or Yeo-Johnson transformation.

**(b) Explain why this transformation helps the model.**

Log transformation helps the model in several ways:

1. **Reduces skewness**: It compresses large values and expands small values, making the distribution more symmetric and closer to normal distribution. This is important because many machine learning algorithms (like linear regression, logistic regression) assume or work better with normally distributed features.

2. **Handles outliers**: Extreme high-income values are compressed, reducing their disproportionate influence on the model. This makes the model more robust to outliers.

3. **Improves model performance**: Algorithms like Logistic Regression and KNN perform better when features are on similar scales and have symmetric distributions. The transformed feature allows the model to learn more effectively.

4. **Better gradient behavior**: For gradient-based optimization algorithms, normalized distributions lead to more stable and faster convergence.

### Q1.4 (2 marks)

Give one reason why feature scaling is important if using Logistic Regression or KNN for credit risk.

**Answer:**

**For Logistic Regression:**
Feature scaling is important because Logistic Regression uses gradient descent optimization, and features with different scales cause the algorithm to converge slowly or get stuck in suboptimal solutions. Features with larger scales dominate the gradient updates, making smaller-scale features less influential in the learning process.

**For KNN (K-Nearest Neighbors):**
Feature scaling is critical because KNN relies on distance calculations (typically Euclidean distance) to find the nearest neighbors. If features are on different scales (e.g., Applicant_Income in thousands vs. a binary flag 0/1), the feature with larger magnitude will dominate the distance calculation. For example, a difference of 10,000 in income would completely overshadow a difference of 1 in a binary feature, even if the binary feature is more predictive. Scaling ensures all features contribute equally to the distance metric.

---

## Question 2 (10 marks)

**Dataset:** Product reviews from an e-commerce website

| Review_ID | Review_Text | Stars |
|-----------|-------------|-------|
| R101 | "Delivered quickly but packaging was damaged." | 3 |
| R102 | "Excellent quality! Worth every rupee." | 5 |
| R103 | "Product stopped working after two days." | 1 |
| R104 | "Good value for money but not very durable." | 4 |
| R105 | "Terrible experience, completely disappointed." | 1 |

**Goal:** Predict the Stars rating (1–5) from the review text.

### Q2.1 (6 marks)

List three feature engineering techniques to convert Review_Text into numeric representations for modelling. Explain why each technique is useful.

**Answer:**

**1. Bag of Words (BoW) / Count Vectorization**
- **How it works**: Creates a vocabulary from all unique words in the corpus, then represents each review as a vector where each dimension corresponds to the count (or presence) of a word in that review.
- **Why useful**:
  - Simple and interpretable: captures word frequency which often correlates with sentiment (e.g., "excellent", "terrible" appear more in positive/negative reviews).
  - Works well for sentiment analysis where specific words matter.
  - Fast to compute and works with many ML algorithms.

**2. TF-IDF (Term Frequency-Inverse Document Frequency)**
- **How it works**: Similar to BoW but weights words by their importance. Words that appear frequently in a document but rarely across the corpus get higher weights, while common words (like "the", "is") get lower weights.
- **Why useful**:
  - Reduces the influence of common words that don't carry much meaning (stop words).
  - Highlights distinctive words that are more informative for classification (e.g., "delivered", "packaging", "durable" in product reviews).
  - Often performs better than simple BoW for text classification tasks.

**3. Word Embeddings (Word2Vec, GloVe, or pre-trained embeddings)**
- **How it works**: Converts words into dense vector representations (typically 100-300 dimensions) where semantically similar words are close in vector space. For a review, words can be averaged or combined to create a document vector.
- **Why useful**:
  - Captures semantic relationships: words like "excellent" and "great" have similar vectors, allowing the model to understand synonyms and related concepts.
  - Dense representation is more efficient than sparse BoW/TF-IDF vectors.
  - Can capture context and meaning beyond just word presence, improving model understanding of review sentiment and content.

### Q2.2 (4 marks)

Explain why dimensionality reduction is often necessary when working with text features. Name one suitable technique and describe how it works.

**Answer:**

**Why dimensionality reduction is necessary:**

1. **High dimensionality**: Text features (especially BoW/TF-IDF) create very high-dimensional vectors. With a vocabulary of thousands or tens of thousands of words, each document becomes a sparse vector with thousands of dimensions. This leads to:
   - **Curse of dimensionality**: As dimensions increase, the data becomes sparse, and distance-based algorithms become less effective.
   - **Computational cost**: Training models on high-dimensional data is slow and memory-intensive.
   - **Overfitting risk**: Models may memorize noise rather than learn general patterns.

2. **Sparsity**: Most text vectors are sparse (mostly zeros), which is inefficient and can hurt model performance.

3. **Redundancy**: Many words are correlated or redundant, and dimensionality reduction can capture the most important information in fewer dimensions.

**One suitable technique: Principal Component Analysis (PCA)**

**How PCA works:**
1. PCA identifies the directions (principal components) in the high-dimensional space where the data varies the most.
2. It projects the original high-dimensional vectors onto a lower-dimensional space (e.g., reducing from 10,000 dimensions to 100-500 dimensions).
3. The principal components are linear combinations of the original features, ordered by the amount of variance they explain.
4. By keeping only the top-k principal components (that explain most of the variance), we retain the most important information while dramatically reducing dimensionality.

**Alternative techniques:** Latent Semantic Analysis (LSA), Non-negative Matrix Factorization (NMF), or t-SNE/UMAP for visualization (though these are less commonly used for feature reduction in modeling).

---

## Question 3 (10 marks)

**Dataset:** IoT sensor data from a smart building

| Timestamp | Room_ID | Temperature | Humidity | Motion_Flag |
|-----------|---------|-------------|----------|-------------|
| 2025-07-01 08:00 | R12 | 26.3 | 48 | 1 |
| 2025-07-01 08:05 | R12 | 26.8 | 47 | 1 |
| 2025-07-01 08:10 | R12 | 27.1 | 46 | 0 |
| 2025-07-01 08:15 | R12 | 27.4 | 45 | 0 |
| 2025-07-01 08:20 | R12 | 27.9 | 44 | 1 |

**Goal:** Predict Temperature at the next timestamp.

### Q3.1 (5 marks)

Suggest three time-derived features you can extract from Timestamp. For each, explain why it is useful for temperature prediction.

**Answer:**

**1. Hour of Day (0-23)**
- **Why useful**: Temperature in buildings follows daily patterns due to human activity, HVAC systems, and external weather. For example, temperatures typically rise during the day (8 AM - 4 PM) when people are active and HVAC systems are running, and may drop at night. The hour feature helps the model learn these cyclical patterns and predict temperature based on the time of day.

**2. Day of Week (Monday=0 to Sunday=6)**
- **Why useful**: Building occupancy and HVAC usage patterns differ between weekdays and weekends. Weekdays may have more consistent heating/cooling schedules, while weekends might have different patterns. This feature captures weekly cyclical behavior that affects temperature trends.

**3. Time Since Start of Day (in minutes) or Minutes Since Midnight**
- **Why useful**: This provides a continuous representation of time progression within a day, allowing the model to capture gradual temperature changes throughout the day. It's more granular than just hour and can help model smooth transitions between different periods (e.g., morning warming, afternoon peak, evening cooling).

**Alternative time-derived features:**
- **Month/Season**: Captures seasonal temperature patterns (summer vs. winter).
- **Is Weekend (binary)**: Simplifies weekday/weekend distinction.
- **Cyclical encoding (sin/cos)**: For hour and day of week, using sine and cosine transformations preserves the cyclical nature (e.g., 23:00 is close to 00:00) which can improve model performance.

### Q3.2 (5 marks)

**Note:** This question appears to be incomplete in the original document. Please provide the question text to receive an answer.
