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
|-----------|----------|-------------|---------|-------------|
| 2025-07-01 08:00 | R12 | 26.3 | 48 | 1 |
| 2025-07-01 08:05 | R12 | 26.8 | 47 | 1 |
| 2025-07-01 08:10 | R12 | 27.1 | 46 | 0 |
| 2025-07-01 08:15 | R12 | 27.4 | 45 | 0 |
| 2025-07-01 08:20 | R12 | 27.9 | 44 | 1 |

**Goal:** Predict Temperature at the next timestamp.

### Q3.1 (5 marks)

Suggest three time-derived features you can extract from Timestamp.
For each, explain why it is useful for temperature prediction.

**Answer:**

1. **Hour of Day**
   - **How it works**: Extract the hour component from the timestamp (e.g., 08:00 → 8, 14:30 → 14)
   - **Why useful**: Temperature follows daily cycles - typically lowest in early morning (4-6 AM) and highest in afternoon (2-4 PM). The hour of day captures these diurnal patterns, allowing the model to learn that temperature at 2 PM is generally higher than at 6 AM, even with similar other conditions. This is crucial for time series prediction as it encodes the natural daily temperature cycle.

2. **Day of Week**
   - **How it works**: Extract the day of week (Monday=0, Tuesday=1, ..., Sunday=6) or as categorical features
   - **Why useful**: Building occupancy patterns vary by day of week (weekdays vs weekends), which affects HVAC usage and internal temperature. Weekdays may have more consistent heating/cooling schedules, while weekends might have different patterns. This helps the model distinguish between weekday and weekend temperature behaviors, especially in commercial buildings where occupancy-driven temperature changes differ significantly.

3. **Time of Day Category (or Minute of Hour)**
   - **How it works**: Categorize time into periods (e.g., Morning: 6-12, Afternoon: 12-18, Evening: 18-22, Night: 22-6) or extract minute component
   - **Why useful**: Captures broader temporal patterns beyond just hour. Morning periods often show rising temperatures as the day warms up, while evening periods may show cooling trends. Alternatively, minute of hour can capture sub-hourly patterns and help model temperature changes within the same hour, which is useful for short-interval predictions (5-minute intervals in this dataset). This granularity helps capture rapid temperature fluctuations that occur within hourly cycles.

### Q3.2 (5 marks)

Humidity and Motion_Flag may carry more information than appears.
Propose two feature engineering strategies to make these features more predictive and
explain how they help.

**Answer:**

**Strategy 1: Lag Features and Rolling Statistics**

- **For Humidity**: Create lag features (Humidity at t-1, t-2, etc.) and rolling statistics (mean, std, min, max over a window like last 3-5 timestamps)
  - **Why helpful**: Temperature and humidity are correlated through thermodynamics (higher humidity can affect perceived temperature and actual heat transfer). Lag features capture the temporal relationship - if humidity was decreasing over the past few readings, temperature might be rising (as seen in the data: humidity drops from 48→44 while temperature rises 26.3→27.9). Rolling statistics smooth out noise and reveal trends that single-point values miss.

- **For Motion_Flag**: Create lag features (Motion_Flag at t-1, t-2) and rolling sum/count (number of motion events in last N timestamps)
  - **Why helpful**: Motion indicates occupancy, which affects temperature through body heat and HVAC usage. A room that had motion recently (lag=1) might still be warming up from occupancy. A room with frequent recent motion (rolling sum) suggests sustained occupancy and higher temperature. The pattern in the data shows motion at 08:00 and 08:05, then none, then motion again at 08:20 - this sequence pattern is more informative than just the current binary flag.

**Strategy 2: Rate of Change and Interaction Features**

- **For Humidity**: Create rate of change features (ΔHumidity = Humidity_t - Humidity_t-1) and interaction with temperature
  - **Why helpful**: The rate of change in humidity (humidity_delta) can indicate environmental dynamics - rapid humidity drops might correlate with temperature increases (as air warms, it can hold more moisture, reducing relative humidity). An interaction feature like Temperature × Humidity captures the combined effect, as the relationship between humidity and temperature is not linear but depends on both values together (psychrometric relationships).

- **For Motion_Flag**: Create "time since last motion" and "motion duration" features, and interaction with hour of day
  - **Why helpful**: "Time since last motion" (e.g., minutes since Motion_Flag was last 1) captures cooling/heating decay after occupancy ends. "Motion duration" (consecutive timestamps with motion=1) indicates sustained occupancy vs brief presence. An interaction feature like Motion_Flag × Hour_of_Day is valuable because motion at 8 AM (morning arrival) has different temperature implications than motion at 2 PM (midday activity) - morning motion might trigger heating startup, while afternoon motion might occur in an already warm room.

## Question 4 (10 marks)

Answer the following:

### Q4.1 (5 marks)

Explain what feature engineering involves when working with audio (.wav) files.

**Answer:**

Feature engineering for audio (.wav) files involves converting raw audio waveforms (time-domain signals) into meaningful numerical representations that capture relevant acoustic properties. This typically includes:

1. **Time-Domain Features**:
   - **Amplitude statistics**: Mean, variance, zero-crossing rate (ZCR) - captures energy and signal characteristics
   - **Temporal patterns**: Short-time energy, autocorrelation - identifies rhythm, tempo, and periodic patterns

2. **Frequency-Domain Features**:
   - **Spectral features**: Using Fast Fourier Transform (FFT) to convert time-domain to frequency-domain
   - **Spectral centroid**: Brightness of sound (higher = brighter)
   - **Spectral rolloff**: Frequency below which 85% of energy is contained
   - **Spectral bandwidth**: Spread of frequencies around the centroid
   - **Spectral contrast**: Difference between peaks and valleys in spectrum

3. **Mel-Frequency Cepstral Coefficients (MFCCs)**:
   - Most common audio feature representation
   - Converts audio to frequency domain, applies mel-scale filterbank (mimics human auditory perception), then applies DCT to get cepstral coefficients
   - Typically extracts 13-40 MFCC coefficients per time frame
   - Captures timbre, tone quality, and phonetic content - widely used in speech recognition and music classification

4. **Spectrograms**:
   - 2D representation showing frequency content over time
   - Created using Short-Time Fourier Transform (STFT) with windowing
   - Can be used directly as image-like features or further processed

5. **Chroma Features**:
   - Represents the 12 pitch classes (C, C#, D, ..., B) in music
   - Useful for music-related tasks like genre classification

6. **Temporal Segmentation**:
   - Dividing audio into frames/windows (typically 20-40ms) with overlap
   - Features are extracted per frame, then aggregated (mean, std, max, etc.) to create fixed-length feature vectors

The goal is to extract features that are invariant to irrelevant variations (like volume, background noise) while capturing discriminative information (like phonemes in speech, instruments in music, or events in environmental sounds).

### Q4.2 (5 marks)

Is it possible to train a model directly on raw audio waveforms without explicit feature
extraction?
Explain when this is possible and when it is not.

**Answer:**

Yes, it is possible to train models directly on raw audio waveforms, but it depends on several factors:

**When it IS possible:**

1. **Deep Learning with Sufficient Data**:
   - Modern deep learning architectures (1D CNNs, WaveNet, Wav2Vec, SincNet) can learn features automatically from raw waveforms
   - These models use convolutional layers that act as learnable feature extractors, discovering relevant patterns (like MFCCs, spectral features) automatically during training
   - Requires large datasets (thousands to millions of samples) for the model to learn meaningful representations

2. **Sufficient Computational Resources**:
   - Raw audio has high dimensionality (e.g., 16kHz audio = 16,000 samples per second)
   - Training on raw waveforms requires significant computational power (GPUs) and memory
   - Deep learning models with appropriate architectures can handle this complexity

3. **End-to-End Learning Objectives**:
   - When the task benefits from learning task-specific features rather than generic audio features
   - For example, speech recognition models like Wav2Vec2 learn features optimized for speech tasks directly from raw audio

**When it is NOT possible or NOT advisable:**

1. **Small Datasets**:
   - Traditional machine learning models (SVM, Random Forest, Logistic Regression) cannot effectively learn from raw waveforms
   - These models require explicit feature extraction (MFCCs, spectral features) to reduce dimensionality and provide meaningful input
   - With limited data, hand-crafted features are more reliable than learning from scratch

2. **Limited Computational Resources**:
   - Raw audio processing is computationally expensive
   - Feature extraction (MFCCs, spectrograms) provides a compact, informative representation that reduces computational burden
   - Pre-extracted features can be used with simpler, faster models

3. **Need for Interpretability**:
   - Hand-crafted features (like MFCCs, spectral centroid) have clear physical/auditory meaning
   - Raw waveform features learned by deep networks are often black-box and harder to interpret
   - When domain knowledge and interpretability matter, explicit feature engineering is preferred

4. **Real-Time or Low-Latency Applications**:
   - Feature extraction can be optimized and cached
   - Processing raw waveforms end-to-end may introduce latency
   - Pre-computed features enable faster inference

5. **Domain-Specific Knowledge**:
   - When domain experts know which features matter (e.g., formants for speech, tempo for music), explicit feature engineering leverages this knowledge
   - Raw waveform learning might miss important domain-specific patterns without sufficient data

**Summary**: Raw waveform learning is feasible with deep learning and large datasets, but explicit feature extraction remains valuable for traditional ML, small datasets, interpretability needs, and computational efficiency.
