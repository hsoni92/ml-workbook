# Feature Engineering Question Paper 2

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

No, Loan_ID should not be included as a feature in the model. Loan_ID is a unique identifier for each loan record and has no predictive value for credit risk. Including it would:
1. Introduce data leakage - the model might memorize specific loan IDs rather than learning meaningful patterns
2. Add noise without providing any information about the borrower's creditworthiness
3. Potentially cause overfitting, especially if the model treats it as a meaningful feature
4. Violate the principle that features should have predictive power related to the target variable

Loan_ID should be kept only for tracking and joining purposes, but excluded from the feature set used for training the model.

### Q1.2 (3 marks)

Loan_Purpose contains 17 categories with no ordinal meaning.

(a) Should you use Ordinal Encoding? Why or why not?

(b) Suggest a more suitable encoding method and briefly describe how it works.

**Answer:**

(a) No, Ordinal Encoding should not be used. Ordinal encoding assigns numeric values (0, 1, 2, ...) to categories, which implies an inherent order or ranking. Since Loan_Purpose has no ordinal meaning, using ordinal encoding would introduce artificial relationships between categories. For example, if "Home Improvement" is encoded as 0 and "Debt Consolidation" as 1, the model might incorrectly interpret that "Debt Consolidation" is somehow "greater than" or "more important than" "Home Improvement", which is not true. This can mislead algorithms that are sensitive to numeric relationships.

(b) **One-Hot Encoding** (or dummy encoding) is a more suitable method. It works by:
- Creating a binary column for each unique category in Loan_Purpose
- For each loan record, setting the column corresponding to its Loan_Purpose category to 1, and all other columns to 0
- This results in 17 binary features (one for each category) where exactly one feature is 1 and the rest are 0
- This preserves the categorical nature without implying any order or hierarchy between categories

Alternatively, **Target Encoding** (mean encoding) could also be used, which replaces each category with the mean of the target variable (Default_Flag) for that category, providing a more compact representation while capturing the relationship between loan purpose and default risk.

### Q1.3 (3 marks)

Applicant_Income is extremely right-skewed.

(a) Name one transformation technique you can apply.

(b) Explain why this transformation helps the model.

**Answer:**

(a) **Log transformation** (logarithmic transformation) can be applied. Specifically, using natural log (ln) or log base 10. The formula would be: `log(Applicant_Income + 1)` or `log10(Applicant_Income + 1)`. The +1 is added to handle zero or negative values if present.

(b) This transformation helps the model in several ways:
1. **Reduces skewness**: Log transformation compresses large values more than small values, pulling in the long tail of the right-skewed distribution and making it more symmetric (closer to normal distribution)
2. **Improves model assumptions**: Many algorithms (like linear regression, logistic regression) assume features are normally distributed. Log transformation helps meet this assumption
3. **Reduces impact of outliers**: Extreme high-income values have less disproportionate influence on the model after transformation
4. **Better feature scaling**: The transformed values are on a more compact scale, which helps with algorithms sensitive to feature magnitudes (like gradient descent, KNN, SVM)
5. **Linearizes relationships**: In many cases, the relationship between log(income) and the target variable is more linear than the relationship between raw income and the target

### Q1.4 (2 marks)

Give one reason why feature scaling is important if using Logistic Regression or KNN for credit risk.

**Answer:**

**For Logistic Regression**: Feature scaling is important because logistic regression uses gradient descent optimization, and features on different scales cause the algorithm to converge slowly or get stuck in suboptimal solutions. Features with larger magnitudes dominate the gradient updates, making the optimization process inefficient and potentially leading to poor convergence.

**For KNN**: Feature scaling is critical because KNN calculates distances (typically Euclidean distance) between data points. If features are on different scales (e.g., Applicant_Income in thousands vs. a binary flag 0/1), the feature with larger magnitude will dominate the distance calculation. For example, a difference of 10,000 in income would completely overshadow a difference in any binary feature, making the distance metric meaningless and causing the algorithm to effectively ignore unscaled features.

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

1. **Bag of Words (BoW) / Count Vectorization**
   - **How it works**: Creates a vocabulary from all unique words in the corpus, then represents each review as a vector where each dimension corresponds to a word's count (or presence) in that review
   - **Why useful**: Simple and interpretable, captures word frequency which often correlates with sentiment (e.g., positive reviews may have more positive words). Preserves information about word importance through frequency counts

2. **TF-IDF (Term Frequency-Inverse Document Frequency)**
   - **How it works**: Similar to BoW but weights words by their importance. TF-IDF increases the weight of words that appear frequently in a document but rarely across the corpus, and decreases the weight of common words
   - **Why useful**: Reduces the impact of common words (like "the", "is", "was") that appear in all reviews and don't help distinguish between ratings. Emphasizes distinctive words that are more informative for predicting star ratings (e.g., "excellent", "terrible", "damaged")

3. **Word Embeddings (Word2Vec, GloVe, or pre-trained embeddings)**
   - **How it works**: Converts words into dense vector representations (typically 100-300 dimensions) that capture semantic meaning. Words with similar meanings have similar vectors. For a review, words are averaged or combined to create a document embedding
   - **Why useful**: Captures semantic relationships between words (e.g., "excellent" and "great" are close in embedding space), handles synonyms effectively, and provides a compact representation. Pre-trained embeddings leverage knowledge from large corpora, which is especially valuable for smaller datasets

### Q2.2 (4 marks)

Explain why dimensionality reduction is often necessary when working with text features. Name one suitable technique and describe how it works.

**Answer:**

**Why dimensionality reduction is necessary:**

1. **High dimensionality**: Text features (especially BoW or TF-IDF) can create thousands or tens of thousands of features (one for each unique word in the vocabulary), leading to the curse of dimensionality
2. **Sparsity**: Most documents contain only a small fraction of all possible words, resulting in sparse feature matrices (mostly zeros), which is computationally inefficient
3. **Overfitting risk**: With many features relative to samples, models are prone to overfitting and poor generalization
4. **Computational efficiency**: Reducing dimensions speeds up training and prediction, and reduces memory requirements
5. **Noise reduction**: Many words are not informative for prediction; dimensionality reduction helps focus on the most relevant features

**One suitable technique: Principal Component Analysis (PCA)**

**How PCA works:**
1. Standardizes the feature matrix (mean=0, std=1)
2. Computes the covariance matrix to understand relationships between features
3. Finds the principal components (eigenvectors) that capture the maximum variance in the data
4. Projects the original high-dimensional data onto a lower-dimensional space using the top k principal components (typically retaining 80-95% of variance)
5. Results in a reduced feature set that is a linear combination of original features, preserving most of the information while dramatically reducing dimensionality

Alternatively, **Truncated SVD (Singular Value Decomposition)** is also commonly used for text data as it works directly with sparse matrices without needing to compute the full covariance matrix, making it more memory-efficient for large vocabularies.

---

## Question 3 (10 marks)

**Dataset:** IoT sensor data from a smart building

| Timestamp | Room_ID | Temperature | Humidity | Motion_Flag |
|-----------|---------|-------------|----------|-------------|
| 2025-07-01 08:00 | R12 | 26.3 | 48 | 1 |
| 2025-07-01 08:05 | R12 | 26.8 | 47 | 1 |
| 2025-07-01 08:10 | R12 | 27.1 | 46 | 0 |
