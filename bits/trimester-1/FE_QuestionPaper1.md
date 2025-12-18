# Feature Engineering Sample Questions

## Section 1: Brief Answers (One Line)

Answer the following questions briefly (in one line).

**Q1.** Define Feature Engineering in the context of improving model accuracy.

**Answer:** Feature Engineering is the process of creating, transforming, or selecting features from raw data to improve model performance and accuracy.

**Explanation:** Feature engineering involves techniques like creating new features from existing ones, transforming features (scaling, normalization), handling missing values, encoding categorical variables, and extracting domain-specific features. The goal is to provide the model with the most informative and relevant features that help it learn patterns more effectively.

---

**Q2.** True or False: Filter methods for feature selection rely on the specific machine learning algorithm (e.g., Random Forest) to select the best features.

**Answer:** False

**Explanation:** Filter methods are algorithm-agnostic and use statistical measures (like correlation, mutual information, chi-square) to rank features independently of any specific ML algorithm. Wrapper methods, on the other hand, use the ML algorithm itself to evaluate feature subsets.

---

**Q3.** A "Rolling Mean" is a feature extraction technique primarily used for what type of data?

**Answer:** Time-series data

**Explanation:** Rolling Mean (also called Moving Average) calculates the mean of values within a sliding window over time. It's used to smooth out short-term fluctuations and highlight longer-term trends in time-series data, making it easier to identify patterns and reduce noise.

---

**Q4.** In image processing, what specific structural information does Edge Detection capture?

**Answer:** Boundaries and transitions between different regions or objects in an image.

**Explanation:** Edge detection identifies points where image brightness changes sharply, which typically correspond to object boundaries, contours, and structural features. This captures geometric and shape information rather than just color/intensity values, making it useful for object recognition and structural analysis.

---

**Q5.** Why is One-Hot Encoding generally not recommended for a "Zip Code" column with 30,000 unique values?

**Answer:** It creates 30,000 new binary columns, leading to high dimensionality, sparsity, and increased computational cost without meaningful ordinal relationships.

**Explanation:** One-Hot Encoding creates one binary column per unique value. With 30,000 zip codes, this results in 30,000 sparse columns (mostly zeros), causing the curse of dimensionality, memory issues, and overfitting. Better alternatives include target encoding, frequency encoding, or treating zip codes as categorical with dimensionality reduction.

---

**Q6.** What is the purpose of a Logarithmic Transformation on a highly skewed "Income" feature?

**Answer:** To reduce skewness and make the distribution more normal, improving model performance and handling outliers better.

**Explanation:** Logarithmic transformation compresses large values and expands small ones, reducing right-skewness in income distributions. This helps models that assume normality (like linear regression), reduces the impact of outliers, and can improve the relationship between features and target variables.

---

**Q7.** Name one automated tool mentioned in the syllabus for Time-Series feature extraction.

**Answer:** tsfresh (Time Series Feature Extraction from Scalable Hypothesis tests)

**Explanation:** tsfresh is a Python library that automatically extracts a large number of time-series features (statistical, temporal, frequency-domain features) from time-series data. It can identify relevant features and help with feature selection for time-series analysis.

---

**Q8.** True or False: PCA (Principal Component Analysis) preserves the original meaning of the features (e.g., "Age", "Salary").

**Answer:** False

**Explanation:** PCA creates new principal components that are linear combinations of original features. These components don't preserve the original feature meanings (e.g., "Age", "Salary") but instead represent directions of maximum variance in the data. The components are abstract mathematical constructs without direct interpretability.

---

**Q9.** In text analysis, what does TF-IDF penalize to highlight important words?

**Answer:** Common words that appear frequently across many documents.

**Explanation:** TF-IDF (Term Frequency-Inverse Document Frequency) penalizes words that appear in many documents (high document frequency) by using the inverse document frequency component. This reduces the weight of common words (like "the", "is", "and") and increases the weight of words that are distinctive to specific documents, making them more informative for classification.

---

**Q10.** Give one example of a domain-specific feature you might calculate for a financial trading dataset (e.g., stock prices).

**Answer:** Moving Average Convergence Divergence (MACD) or Relative Strength Index (RSI) or Bollinger Bands.

**Explanation:** Domain-specific features capture expert knowledge. For financial data, examples include:
- **MACD**: Measures momentum and trend changes
- **RSI**: Indicates overbought/oversold conditions
- **Bollinger Bands**: Shows volatility and potential price reversals
- **Price momentum**: Rate of change over time periods
- **Volume-weighted average price (VWAP)**: Price adjusted for trading volume

---

## Section 2: Scenario-Based Questions (With Justification)

Answer the following questions based on the provided scenarios. Justify your choice of technique.

**Q11.** You are predicting house prices. The "Lot Area" feature mostly ranges from 500 to 5,000 sq ft, but contains three valid but extreme outliers (mansions) with 500,000 sq ft.

- Identify the most appropriate feature scaling technique for this specific distribution.
- Justify why it is a better choice compared to the other techniques.

**Answer:** **Robust Scaling** (using median and IQR) is the most appropriate technique.

**Explanation:**
- **Robust Scaling** uses median and Interquartile Range (IQR) instead of mean and standard deviation, making it resistant to outliers. The three extreme outliers (500,000 sq ft) won't significantly affect the median or IQR, so the scaling will properly normalize the majority of data (500-5,000 sq ft range) without being distorted.

- **Why not Min-Max Scaling?** Min-Max scaling uses min and max values, so the extreme outliers (500,000) would compress all other values into a very narrow range, losing information.

- **Why not Standardization (Z-score)?** Standardization uses mean and standard deviation, which are highly sensitive to outliers. The three extreme values would inflate the standard deviation, making most values appear close to the mean and reducing variance in the scaled feature.

- **Why not Log Transformation?** While log transformation could help with skewness, it doesn't scale the data to a specific range, which might be needed for certain algorithms. Robust scaling provides both outlier resistance and proper scaling.

---

**Q12.** You have a dataset with only 200 patients (rows) but 50,000 gene features (columns). You need to select the top 50 relevant genes.

- Which class of feature selection method (Filter or Wrapper) is practically feasible here?
- Justify your answer.

**Answer:** **Filter methods** are practically feasible here.

**Explanation:**
- **Filter methods** are computationally efficient and don't require training the model multiple times. They use statistical measures (correlation, mutual information, chi-square, variance threshold) to rank features independently. With 50,000 features and only 200 samples, filter methods can quickly evaluate and rank all features without the computational overhead of model training.

- **Wrapper methods** are not feasible because:
  - They require training the model multiple times for different feature subsets
  - With 50,000 features, the search space is enormous (2^50,000 possible subsets)
  - With only 200 samples, training models repeatedly would be computationally expensive and time-consuming
  - The small sample size (200) relative to features (50,000) makes wrapper methods prone to overfitting

- **Hybrid approach:** Start with filter methods to reduce from 50,000 to a smaller subset (e.g., 500-1000), then potentially use wrapper methods on the reduced set if needed.

---

**Q13.** You are training a model to distinguish between photos of wheels and photos of bricks. The model using raw pixel colors is failing because the object colors vary.

- Recommend a specific feature descriptor/extraction technique.
- Justify your choice.

**Answer:** **HOG (Histogram of Oriented Gradients)** or **SIFT (Scale-Invariant Feature Transform)** or **Edge Detection features** (like Canny edge detector).

**Explanation:**
- **HOG (Histogram of Oriented Gradients)** is recommended because:
  - It captures shape and structure information rather than color
  - It's invariant to color variations, focusing on gradient directions and edge orientations
  - Wheels have circular/curved edges, while bricks have rectangular/straight edges - HOG can capture these structural differences
  - It's computationally efficient and widely used for object recognition

- **Alternative: SIFT** - Also captures structural features and is scale-invariant, but computationally more expensive.

- **Why not raw pixels?** Raw pixel colors vary with lighting, material, and object color, making it difficult to learn shape-based patterns. Structural features like edges, gradients, and textures are more robust to color variations and better capture the geometric differences between wheels (circular) and bricks (rectangular).

---

**Q14.** You have a dataset containing only the "Closing Price" of a stock for the last 365 days. You cannot use the "Date" column directly in a regression model.

- Propose a specific temporal feature engineering technique that utilizes past data (e.g., previous days' prices) to create a predictive feature for tomorrow's price.
- Explain the logic of your chosen feature.

**Answer:** **Lag Features** (e.g., previous day's closing price, moving averages) or **Momentum Features** (e.g., price change over N days).

**Explanation:**
- **Lag Features:** Create features using previous days' prices:
  - `lag_1`: Yesterday's closing price
  - `lag_7`: Closing price 7 days ago
  - `lag_30`: Closing price 30 days ago

  **Logic:** Stock prices often exhibit temporal dependencies. Yesterday's price is often a strong predictor of today's price. Multiple lag features capture short-term and long-term trends.

- **Moving Average Features:**
  - `MA_7`: 7-day moving average
  - `MA_30`: 30-day moving average
  - `MA_ratio`: Ratio of current price to moving average

  **Logic:** Moving averages smooth out noise and capture trends. When current price is above/below the moving average, it indicates momentum or potential reversals.

- **Momentum/Change Features:**
  - `price_change_1d`: Change from yesterday
  - `price_change_7d`: Change over last 7 days
  - `momentum`: Rate of change

  **Logic:** These capture the direction and speed of price movements, which are predictive of future price movements.

- **Why these work:** Financial time-series data exhibits autocorrelation - past prices influence future prices. These features explicitly encode temporal relationships that the model can learn from.

---

## Section 3: Detailed Answers

Answer the following questions in detail, addressing all parts.

**Q15.** You have a dataset of 28x28 pixel images of handwritten digits (0-9). You want to build a classifier (e.g., SVM).

1. The raw data has 784 features (pixels) per image. Would applying PCA (Principal Component Analysis) be useful before training the SVM?
2. Suggest a technique to capture the structure or edges of the digits. Why is this better than raw pixels?
3. Why would "Min-Max Scaling" the pixel values (0-255) be useful, whereas "Standardization" might be less intuitive for image pixel intensity?

**Answer:**

**1. PCA Application:**
Yes, applying PCA would be useful before training the SVM.

**Explanation:**
- **Dimensionality Reduction:** 784 features is high-dimensional, and many pixels (especially in corners/background) may not be informative. PCA can reduce dimensionality while preserving most variance (e.g., reduce to 50-200 principal components).
- **Computational Efficiency:** SVMs can be slow with high-dimensional data. Reducing dimensions speeds up training and prediction.
- **Noise Reduction:** PCA captures the most important patterns and can filter out noise in pixel values.
- **Curse of Dimensionality:** With limited training samples relative to 784 features, reducing dimensions can help prevent overfitting.
- **Note:** However, PCA may lose some spatial information, so it's a trade-off between dimensionality reduction and information preservation.

**2. Technique to Capture Structure/Edges:**
**HOG (Histogram of Oriented Gradients)** or **Edge Detection** (like Sobel, Canny) or **Gabor Filters**.

**Explanation:**
- **HOG:** Captures local gradient orientations, which are excellent for digit recognition as digits have distinct edge patterns (curves, lines, intersections).
- **Edge Detection:** Identifies boundaries and contours of digits, capturing shape information.
- **Why better than raw pixels:**
  - **Invariance:** Edge/structural features are more robust to variations in stroke thickness, writing style, and slight translations
  - **Relevant Information:** Focuses on shape and structure (what makes a "3" different from "8") rather than exact pixel intensities
  - **Dimensionality:** Can be more compact than 784 raw pixels while preserving discriminative information
  - **Generalization:** Structural features generalize better across different handwriting styles and image conditions

**3. Min-Max Scaling vs Standardization for Pixel Values:**
**Min-Max Scaling** is more intuitive and useful for image pixel intensity.

**Explanation:**
- **Min-Max Scaling (0-255 → 0-1):**
  - **Preserves relative relationships:** Maintains the proportional differences between pixel intensities
  - **Natural range:** Pixel values naturally range from 0-255, so scaling to 0-1 is intuitive and preserves the meaning of "dark" (0) and "bright" (255)
  - **Algorithm compatibility:** Many image processing algorithms and neural networks expect pixel values in [0,1] range
  - **Interpretability:** Scaled values directly correspond to brightness levels

- **Standardization (Z-score normalization):**
  - **Less intuitive:** Produces values that can be negative or greater than 1, which doesn't align with the natural interpretation of pixel intensity
  - **Assumes normal distribution:** Standardization assumes data is normally distributed, but pixel intensities in images are often not normally distributed
  - **Loses natural bounds:** Pixel values are naturally bounded [0,255], but standardization removes this constraint
  - **Can create artifacts:** Negative standardized values don't have a meaningful interpretation for pixel intensity

---

**Q16.** You are building a spam detector using a dataset of 50,000 emails.

- **(a)** Which would be more useful - TF-IDF or Boolean Bag-of-Words?
- **(b)** Why would using One-Hot Encoding for every unique word in the dataset be a bad idea?

**Answer:**

**(a) TF-IDF would be more useful than Boolean Bag-of-Words.**

**Explanation:**
- **TF-IDF advantages:**
  - **Term Frequency component:** Captures how important a word is within a document (spam emails may repeat certain words like "free", "click", "urgent")
  - **Inverse Document Frequency component:** Penalizes common words (like "the", "is", "and") that appear in both spam and non-spam emails, while highlighting distinctive words
  - **Discriminative power:** Words that appear frequently in spam but rarely in legitimate emails get higher weights, making classification easier
  - **Gradient information:** Provides continuous values (0 to positive numbers) rather than binary, giving more nuanced information to the model

- **Boolean Bag-of-Words limitations:**
  - **Binary representation:** Only indicates presence/absence of words, losing frequency information
  - **No discrimination:** Treats all words equally, whether they're common stop words or distinctive spam indicators
  - **Less informative:** Doesn't capture the importance or relevance of words within documents

- **Example:** If "free" appears 10 times in a spam email and once in a legitimate email, TF-IDF will give it a higher weight in the spam email, while Boolean BoW treats both the same (just "present").

**(b) One-Hot Encoding for every unique word would be a bad idea because:**

**Explanation:**
- **Extreme dimensionality:** With 50,000 emails, there could be tens of thousands of unique words, creating tens of thousands of binary columns. This leads to:
  - **Memory issues:** Massive sparse matrices that consume excessive memory
  - **Computational cost:** Training becomes extremely slow or infeasible
  - **Curse of dimensionality:** With so many features, the model needs exponentially more data to learn effectively

- **Sparsity problem:** Each email contains only a small subset of all possible words, resulting in extremely sparse vectors (mostly zeros). This is inefficient and makes learning difficult.

- **No frequency information:** One-Hot Encoding only captures presence/absence, losing important frequency information that TF-IDF or regular BoW provide.

- **No word relationships:** One-Hot Encoding treats each word independently with no semantic or contextual relationships.

- **Better alternatives:**
  - **TF-IDF:** Captures frequency and importance
  - **Word embeddings:** Captures semantic relationships
  - **Bag-of-Words with frequency:** Simpler but still informative
  - **Feature selection:** Reduce vocabulary size before encoding
