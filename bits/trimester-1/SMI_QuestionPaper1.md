# Statistical Modelling and Inferencing
## Practice Paper Set

**Total Marks:** 35

---

## General Instructions
- Attempt ALL questions
- Statistical tables and direct values will be provided within the question itself

---

## Question 1: Confidence Intervals and Sample Size Estimation [9 marks]

### Context
A mobile app company wants to estimate the proportion of users who would upgrade to a premium subscription. The company needs reliable survey results for their business planning.

### Part (a) [5 marks]
The company wants to estimate the true proportion of potential upgraders with 99% confidence and a margin of error of no more than 0.05. If no prior information is available about user preferences, what sample size should be used?

### Part (b) [4 marks]
After conducting the full survey, the company found that 156 out of 520 users indicated they would upgrade to premium. Construct a 99% confidence interval for the true proportion of users who would upgrade. Interpret this confidence interval in the context of the business decision the company needs to make.

---

## Question 2: Two-Way ANOVA [9 marks]

### Context
A pharmaceutical researcher is investigating the effects of two factors on patient recovery time (in days): Drug Type (Standard vs. New) and Dosage Level (Low vs. High). The researcher measures recovery times and obtains the following results:

### Mean Recovery Times (days)

| Drug Type | Low Dosage | High Dosage | Overall Mean |
|-----------|------------|-------------|--------------|
| Standard  | 14         | 10          | 12.0         |
| New       | 8          | 12          | 10.0         |
| **Overall Mean** | **11.0** | **11.0** | **11.0** |

### Two-Way ANOVA Results

| Source | SS | df | MS | F-stat | P-value |
|--------|-----|----|----|--------|---------|
| Drug Type | 16.0 | 1 | 16.0 | 3.56 | 0.082 |
| Dosage Level | 0.0 | 1 | 0.0 | 0.00 | 1.000 |
| Interaction (Drug × Dosage) | 64.0 | 1 | 64.0 | 14.22 | 0.003 |
| Error | 54.0 | 12 | 4.5 | | |
| Total | 134.0 | 15 | | | |

### Part (a) [4 marks]
Looking at the mean recovery times table, describe the pattern you observe. How do recovery times change with drug type and dosage level? Using α = 0.05, interpret the ANOVA results for the main effects (Drug Type and Dosage Level) and the interaction effect. Which effects are statistically significant?

### Part (b) [5 marks]
Explain what the significant interaction effect means in practical terms for this pharmaceutical study. The overall mean for Dosage Level is exactly the same (11.0 for both Low and High), yet we see very different recovery times within each drug type. Explain this paradox and discuss how the researcher should interpret these findings when making recommendations about drug prescription.

---

## Question 3: Multiple Regression and Time Series Forecasting [9 marks]

### Context
A retail analytics team wants to predict monthly revenue (in lakhs Rs.) based on marketing spend (in lakhs Rs.) and store footfall (in thousands). Using data from 18 months, the following regression model was fitted:

**Revenue = β₀ + β₁(Marketing) + β₂(Footfall) + ε**

### Regression Output

| Coefficient | Estimate | Std. Error | t-statistic | P-value |
|-------------|----------|------------|-------------|---------|
| Intercept (β₀) | 8.2 | 2.5 | 3.28 | 0.005 |
| Marketing (β₁) | 2.4 | 0.6 | 4.00 | 0.001 |
| Footfall (β₂) | 1.8 | 0.9 | 2.00 | 0.064 |

**Additional Information:**
- R² = 0.78
- Adjusted R² = 0.75
- Overall F-test p-value = 0.0002

### Part (a) [4 marks]
At α = 0.05 significance level, examine whether the overall regression model is significant. Then, analyze the individual t-tests for each predictor variable. Are both Marketing spend and Footfall significant predictors of Revenue? The manager suggests removing Footfall to simplify the model. Based on the statistical output, would you recommend this? Justify your answer.

### Part (b) [5 marks]
If the revenue data shows a clear upward trend with quarterly seasonal patterns, explain why Holt-Winters exponential smoothing would be more appropriate than simple exponential smoothing for forecasting future revenue. Describe what specific components Holt-Winters captures that simple exponential smoothing cannot. Also, explain one advantage and one disadvantage of using a 3-month moving average compared to exponential smoothing methods.

---

## Question 4: Maximum Likelihood Estimation and Logistic Regression [8 marks]

### Context
A technology company conducted a product trial where 30 users tested a new software feature, and 21 of them found it useful and continued using it.

### Part (a) [4 marks]
Using Maximum Likelihood Estimation (MLE), derive the estimate for the probability (p) that a user will find the feature useful. Show your complete derivation including:
1. The likelihood function
2. The log-likelihood function
3. The derivative and solution

Interpret what this estimate tells the company about the feature's potential success.

### Part (b) [4 marks]
The company also wants to predict whether a user will adopt the feature based on their age. Historical data shows the following pattern:

| Age (years) | 22 | 25 | 28 | 32 | 38 | 42 | 48 | 52 | 58 | 62 |
|-------------|----|----|----|----|----|----|----|----|----|----|
| Adopted     | 1  | 1  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 0  |

*(1 = adopted, 0 = did not adopt)*

After fitting a logistic regression model: **log(odds) = 3.2 − 0.08 × Age**

Calculate the probability that a 35-year-old user will adopt the feature using the logistic function. Then explain why logistic regression is more appropriate than linear regression for this problem, discussing at least two specific issues that would arise if ordinary linear regression were used instead.

---
---

# ANSWERS WITH DETAILED EXPLANATIONS

---

## Answer 1: Confidence Intervals and Sample Size Estimation

### Part (a) - Sample Size Calculation [5 marks]

**Given Information:**
- Confidence level: 99% (α = 0.01)
- Margin of error (E): 0.05
- No prior information available
- Critical value for 99% confidence: z₀.₀₀₅ = 2.576

**Solution:**

When no prior information is available, we use the most conservative estimate where p̂ = 0.5, which maximizes the variance p̂(1-p̂).

The formula for sample size is:

**n = (z²α/2 × p̂(1-p̂)) / E²**

Substituting values:
- n = (2.576² × 0.5 × 0.5) / 0.05²
- n = (6.635 × 0.25) / 0.0025
- n = 1.659 / 0.0025
- n = 663.6

**Answer: n = 664 users** (rounding up to ensure we meet the margin of error requirement)

**Explanation:**
- Using p̂ = 0.5 is the most conservative approach because it produces the maximum required sample size
- This ensures that regardless of the actual proportion, our margin of error won't exceed 0.05
- Rounding up is critical because we can't survey a fraction of a person, and rounding down would increase the margin of error beyond acceptable limits

---

### Part (b) - Confidence Interval Construction [4 marks]

**Given Information:**
- Sample size: n = 520
- Users who would upgrade: x = 156
- Confidence level: 99%
- Critical value: z₀.₀₀₅ = 2.576

**Solution:**

First, calculate the sample proportion:
- p̂ = 156/520 = 0.30 (or 30%)

Calculate the standard error:
- SE = √[p̂(1-p̂)/n] = √[0.30 × 0.70 / 520] = √[0.21/520] = √0.000404 = 0.0201

Calculate the margin of error:
- E = z × SE = 2.576 × 0.0201 = 0.0518

Construct the confidence interval:
- Lower limit = 0.30 - 0.0518 = 0.2482
- Upper limit = 0.30 + 0.0518 = 0.3518

**Answer: 99% CI = (0.248, 0.352) or (24.8%, 35.2%)**

**Business Interpretation:**
We are 99% confident that the true proportion of users who would upgrade to premium lies between 24.8% and 35.2%. This means:

1. **For Business Planning:** The company can expect between roughly 1 in 4 to 1 in 3 users to upgrade
2. **Conservative Planning:** Using the lower bound (24.8%), the company should plan for at least this conversion rate
3. **Revenue Forecasting:** With a user base, they can multiply by this range to estimate premium subscription revenue
4. **Decision Making:** This relatively narrow range (width ≈ 10%) provides good precision for business decisions, though the company might want to consider that even at the upper bound, about 2/3 of users won't upgrade
5. **99% Confidence Level:** The high confidence level means we're very certain about this range, which is appropriate for major business investment decisions

**Note:** The actual margin of error (0.0518) is very close to the target of 0.05 from part (a), validating our sample size calculation.

---

## Answer 2: Two-Way ANOVA

### Part (a) - ANOVA Interpretation [4 marks]

**Pattern in Mean Recovery Times:**

Looking at the table systematically:
- **Standard Drug:** Recovery time decreases from 14 days (low dosage) to 10 days (high dosage) - a 4-day improvement
- **New Drug:** Recovery time increases from 8 days (low dosage) to 12 days (high dosage) - a 4-day worsening
- **Overall means:** Drug Type means differ (12.0 vs 10.0), but Dosage Level means are identical (11.0 vs 11.0)

**Statistical Significance Analysis (α = 0.05):**

1. **Drug Type Main Effect:**
   - F-statistic: 3.56, P-value: 0.082
   - **NOT SIGNIFICANT** (p > 0.05)
   - Although the New drug has a lower overall mean (10.0 vs 12.0 days), this 2-day difference is not statistically significant

2. **Dosage Level Main Effect:**
   - F-statistic: 0.00, P-value: 1.000
   - **NOT SIGNIFICANT** (p > 0.05)
   - This makes sense as both dosage levels have identical overall means (11.0)

3. **Interaction Effect (Drug × Dosage):**
   - F-statistic: 14.22, P-value: 0.003
   - **HIGHLY SIGNIFICANT** (p < 0.05)
   - This is the critical finding - the effect of dosage depends on which drug is used

**Conclusion:**
Only the interaction effect is statistically significant. Neither main effect is significant on its own, but the strong interaction means we cannot interpret the factors independently.

---

### Part (b) - Interaction Effect Explanation [5 marks]

**Understanding the Significant Interaction:**

The significant interaction effect (p = 0.003) reveals a crucial finding: **the effect of dosage is completely opposite for the two drugs.**

**Practical Meaning:**

1. **For Standard Drug:**
   - Higher dosage is BENEFICIAL: 14 days → 10 days (4-day improvement)
   - Following traditional pharmaceutical logic: more drug = faster recovery

2. **For New Drug:**
   - Higher dosage is HARMFUL: 8 days → 12 days (4-day worsening)
   - Counterintuitive: more drug = slower recovery
   - Suggests possible toxicity or adverse effects at high doses

**Explaining the Paradox:**

The overall mean for dosage levels is the same (11.0) despite dramatic differences within each drug type. This is Simpson's Paradox in action:

- **Low Dosage overall:** (14 + 8) / 2 = 11.0
- **High Dosage overall:** (10 + 12) / 2 = 11.0

The averaging **masks** the opposite effects because:
- Standard drug's improvement (14→10) exactly cancels out
- New drug's worsening (8→12) when averaged together

This demonstrates why looking only at main effects would be dangerously misleading!

**Recommendations for the Researcher:**

1. **DO NOT prescribe based on main effects alone**
   - Simply saying "use high dosage" or "use low dosage" would be wrong

2. **Drug-Specific Dosage Protocols:**
   - **Standard Drug:** Prescribe HIGH dosage (10 days recovery - best overall outcome)
   - **New Drug:** Prescribe LOW dosage (8 days recovery - actually the fastest!)

3. **Further Investigation Needed:**
   - Why does the new drug show adverse effects at high doses?
   - Is there a therapeutic window or toxicity threshold?
   - Should intermediate dosages be tested?

4. **Best Practice:**
   - The optimal treatment is **New Drug at Low Dosage** (8 days)
   - If New drug is unavailable, use **Standard Drug at High Dosage** (10 days)
   - AVOID: New Drug at High Dosage (12 days - worst outcome)

**Key Learning:** Significant interactions mean we must consider factor combinations, not factors in isolation. Ignoring the interaction could lead to prescribing high-dose New drug, which is actually the worst treatment option!

---

## Answer 3: Multiple Regression and Time Series Forecasting

### Part (a) - Regression Model Assessment [4 marks]

**1. Overall Model Significance:**

**Hypotheses:**
- H₀: β₁ = β₂ = 0 (model has no predictive value)
- H₁: At least one βᵢ ≠ 0 (model is useful)

**Test:** F-test with p-value = 0.0002

**Conclusion:** Since p-value (0.0002) < α (0.05), we **REJECT H₀**. The overall regression model is **statistically significant**. This means the model as a whole provides valuable information for predicting revenue.

**Additional Support:**
- R² = 0.78 indicates that 78% of variation in revenue is explained by the model
- Adjusted R² = 0.75 confirms the model isn't overfitting (close to R²)

---

**2. Individual Predictor Analysis (α = 0.05):**

**Marketing (β₁):**
- Estimate: 2.4 (for every lakh Rs. increase in marketing, revenue increases by 2.4 lakhs)
- t-statistic: 4.00
- P-value: 0.001
- **SIGNIFICANT** (p < 0.05)
- Conclusion: Marketing spend is a strong, statistically significant predictor

**Footfall (β₂):**
- Estimate: 1.8 (for every thousand increase in footfall, revenue increases by 1.8 lakhs)
- t-statistic: 2.00
- P-value: 0.064
- **NOT SIGNIFICANT** (p > 0.05, though close)
- Conclusion: Footfall is marginally non-significant at the 0.05 level

---

**3. Should Footfall be Removed?**

**Recommendation: NO, DO NOT remove Footfall**

**Justification:**

1. **Marginal Significance:**
   - P-value of 0.064 is very close to 0.05 threshold
   - This is borderline; slight changes in data could make it significant
   - At α = 0.10, it would be significant

2. **Practical Significance:**
   - Coefficient of 1.8 is substantial in business terms
   - Effect size matters beyond just statistical significance
   - Footfall has strong theoretical justification (more customers → more sales)

3. **Overall Model Performance:**
   - R² = 0.78 shows strong predictive power
   - Model uses both controllable (marketing) and environmental (footfall) factors
   - Removing footfall would decrease model explanatory power

4. **Multicollinearity Consideration:**
   - Standard error for Footfall (0.9) is large, suggesting possible collinearity with Marketing
   - Marketing and Footfall might be correlated (more marketing → more footfall)
   - This inflates standard errors and can make significant predictors appear non-significant

5. **Business Context:**
   - Footfall provides information about factors beyond the company's control
   - Useful for forecasting and understanding revenue drivers holistically
   - Simplicity isn't always better if it sacrifices predictive accuracy

**Alternative Suggestion:**
Instead of removing Footfall, the team should:
- Check for multicollinearity (VIF values)
- Consider interaction terms (Marketing × Footfall)
- Collect more data to increase power
- Keep both predictors for comprehensive revenue modeling

---

### Part (b) - Time Series Methods [5 marks]

**Why Holt-Winters over Simple Exponential Smoothing:**

**Simple Exponential Smoothing Limitations:**
- Only captures the **level** (current value) of the series
- Formula: Ŷₜ₊₁ = α·Yₜ + (1-α)·Ŷₜ
- Assumes data is relatively flat with no systematic trend or seasonality
- Would fail to capture the "clear upward trend and quarterly seasonal patterns"

**Holt-Winters Exponential Smoothing Advantages:**

Holt-Winters (Triple Exponential Smoothing) captures **three components:**

1. **Level (ℓₜ):** The baseline value at time t
   - Updated: ℓₜ = α(Yₜ/sₜ₋ₛ) + (1-α)(ℓₜ₋₁ + bₜ₋₁)

2. **Trend (bₜ):** The rate of change (upward/downward direction)
   - Updated: bₜ = β(ℓₜ - ℓₜ₋₁) + (1-β)bₜ₋₁
   - Captures the systematic increase in revenue over time
   - Simple exponential smoothing **cannot** model this

3. **Seasonality (sₜ):** Repeating quarterly patterns
   - Updated: sₜ = γ(Yₜ/ℓₜ) + (1-γ)sₜ₋ₛ
   - Captures Q1, Q2, Q3, Q4 differences (e.g., holiday shopping in Q4)
   - Simple exponential smoothing **completely ignores** this

**Forecast Formula:**
- Ŷₜ₊ₕ = (ℓₜ + h·bₜ) × sₜ₊ₕ₋ₛ
- Incorporates trend projection and seasonal adjustment

**Why This Matters for Revenue:**
- Revenue typically has **growth trends** (business expansion, inflation)
- Revenue has **seasonal patterns** (festivals, year-end, seasonal products)
- Ignoring these would lead to systematic forecast errors

---

**3-Month Moving Average vs. Exponential Smoothing:**

**3-Month Moving Average:**
- Formula: MAₜ = (Yₜ + Yₜ₋₁ + Yₜ₋₂) / 3

**One Advantage of Moving Average:**

**Equal Weighting & Simplicity**
- Treats all three months equally (each gets weight = 1/3)
- Easier to understand and explain to non-technical stakeholders
- No parameters to tune (unlike α, β, γ in exponential smoothing)
- More transparent: "average of last 3 months"
- Less prone to parameter selection bias

**One Disadvantage of Moving Average:**

**Insensitivity to Recent Changes**
- All observations in the window receive equal weight
- A sudden spike 3 months ago affects the forecast just as much as last month's value
- Less responsive to recent trends or shifts in the data
- **Lag effect:** Moving averages are inherently backward-looking and slow to adapt
- **Wastes information:** Completely ignores data older than 3 months
- In exponential smoothing, recent observations get exponentially higher weights (α for most recent, α(1-α) for second-most recent, etc.), making it more adaptive

**Example:** If revenue suddenly increased last month due to a successful campaign, exponential smoothing would adjust forecasts more aggressively, while the 3-month MA would dilute this signal across three months.

**Optimal Use Case for Each:**
- **Moving Average:** When you want smooth, stable forecasts and equal treatment of recent history
- **Exponential Smoothing:** When you want adaptive forecasts that respond quickly to recent changes
- **Holt-Winters:** When you have trend and seasonality that must be modeled explicitly

---

## Answer 4: Maximum Likelihood Estimation and Logistic Regression

### Part (a) - MLE Derivation [4 marks]

**Given Information:**
- n = 30 users tested the feature
- x = 21 users found it useful
- We need to estimate p (probability a user finds it useful)

**Complete MLE Derivation:**

**Step 1: Likelihood Function**

Assuming each user's response is independent and follows a Bernoulli distribution with probability p, the likelihood function for observing x = 21 successes out of n = 30 trials follows a binomial distribution:

**L(p) = C(n,x) × pˣ × (1-p)ⁿ⁻ˣ**

Where C(n,x) = n!/(x!(n-x)!) is the binomial coefficient

Substituting values:
- L(p) = C(30,21) × p²¹ × (1-p)⁹

**Step 2: Log-Likelihood Function**

Taking the natural logarithm to simplify differentiation:

**ℓ(p) = ln(L(p)) = ln(C(30,21)) + 21·ln(p) + 9·ln(1-p)**

Note: The constant term ln(C(30,21)) doesn't affect optimization, so we can focus on:

**ℓ(p) = 21·ln(p) + 9·ln(1-p)**

**Step 3: Derivative and Solution**

To find the maximum, take the derivative with respect to p and set it equal to zero:

**dℓ/dp = 21/p - 9/(1-p) = 0**

Solving for p:
- 21/p = 9/(1-p)
- 21(1-p) = 9p
- 21 - 21p = 9p
- 21 = 30p
- **p̂ = 21/30 = 0.70**

**Verification (Second Derivative Test):**
- d²ℓ/dp² = -21/p² - 9/(1-p)²
- At p = 0.70: d²ℓ/dp² = -21/0.49 - 9/0.09 = -42.86 - 100 = -142.86 < 0
- Negative second derivative confirms this is a maximum ✓

**Answer: p̂_MLE = 0.70 or 70%**

**Interpretation for the Company:**

1. **User Acceptance:** The MLE estimate indicates that 70% of users find the feature useful - a strong acceptance rate

2. **Feature Success:** This is a positive signal for the feature's potential success:
   - More than 2/3 of users find value in it
   - Well above the 50% threshold that might indicate mixed reception

3. **Business Decision:** With 70% user approval:
   - **Recommended action:** Proceed with feature development and rollout
   - Strong enough to justify investment in full production
   - May want to understand why 30% didn't find it useful to improve further

4. **Statistical Note:** The MLE is unbiased and efficient, giving us the "best" estimate given the data. With 30 users, we have reasonable confidence, though a larger sample would provide more precision.

5. **Risk Assessment:** Even accounting for sampling variability, the true proportion is likely well above 50%, making this a viable feature for broad release.

---

### Part (b) - Logistic Regression Application [4 marks]

**Part 1: Probability Calculation for 35-year-old**

**Given Model:** log(odds) = 3.2 - 0.08 × Age

**For Age = 35:**
- log(odds) = 3.2 - 0.08 × 35
- log(odds) = 3.2 - 2.8
- log(odds) = 0.4

**Converting to Probability using Logistic Function:**

The logistic function is: **P(Adopt) = e^(log(odds)) / (1 + e^(log(odds)))**

Or equivalently: **P(Adopt) = 1 / (1 + e^(-log(odds)))**

Substituting:
- P(Adopt) = e^0.4 / (1 + e^0.4)
- e^0.4 ≈ 1.4918
- P(Adopt) = 1.4918 / (1 + 1.4918)
- P(Adopt) = 1.4918 / 2.4918
- **P(Adopt) = 0.599 or approximately 59.9%**

**Interpretation:** A 35-year-old user has about a 60% probability of adopting the feature - slightly better than a coin flip, but the model shows age is near the threshold where adoption becomes less likely.

---

**Part 2: Why Logistic Regression is More Appropriate**

**Issue 1: Predicted Values Must be Probabilities (0 to 1)**

**Problem with Linear Regression:**
- Linear regression: Ŷ = β₀ + β₁×Age
- Can produce predictions **outside [0,1] range**
- Example with our data:
  - For Age = 20: might predict Ŷ = 1.3 (impossible - probability > 100%)
  - For Age = 70: might predict Ŷ = -0.4 (impossible - negative probability)

**Logistic Regression Solution:**
- Uses logistic function: P = 1/(1 + e^(-(β₀ + β₁×Age)))
- **Automatically constrains** output between 0 and 1
- Always produces valid probabilities regardless of input values
- The S-shaped curve asymptotically approaches 0 and 1

---

**Issue 2: Violation of Assumptions**

**A. Non-constant Variance (Heteroscedasticity):**
- Linear regression assumes constant variance of errors (homoscedasticity)
- For binary outcomes:
  - Variance = p(1-p)
  - Maximized at p = 0.5
  - Approaches 0 as p approaches 0 or 1
- Variance inherently depends on the predicted value
- Violates OLS assumptions → **inefficient estimates and invalid standard errors**

**B. Non-normal Residuals:**
- Linear regression assumes normally distributed errors
- With binary outcomes (0 or 1), residuals are **fundamentally non-normal**
- For any prediction p̂:
  - When Y = 1: residual = 1 - p̂
  - When Y = 0: residual = 0 - p̂
  - Only two possible residual values per predicted probability
- Creates bimodal residual distribution, not normal
- Invalidates t-tests, confidence intervals, and hypothesis tests

---

**Issue 3: Inappropriate Error Structure (Bonus Explanation)**

**Linear Regression:**
- Assumes additive, normally distributed errors: Y = Xβ + ε, where ε ~ N(0, σ²)
- Doesn't match the **binomial error structure** of adoption/non-adoption

**Logistic Regression:**
- Uses **binomial likelihood** and maximum likelihood estimation
- Properly models the binary nature of the outcome
- Appropriate link function (logit) for the data generating process

---

**Practical Demonstration with the Given Data:**

Looking at the data pattern:
- Ages 22-32: All adopted (Y = 1)
- Ages 38-62: None adopted (Y = 0)
- Sharp transition around age 35

**Linear Regression would:**
- Draw a straight line through the data
- Produce problematic predictions like P = 1.2 for age 20 or P = -0.3 for age 70
- Fail to capture the sharp S-shaped transition
- Underestimate adoption probability for young users
- Overestimate adoption probability for old users

**Logistic Regression:**
- Produces smooth S-curve matching the underlying binary process
- Probabilities gracefully transition from near 1 (young) to near 0 (old)
- Model coefficient (-0.08) correctly indicates negative relationship
- All predictions are valid probabilities

---

**Summary:**

Logistic regression is appropriate because:
1. ✅ Constrains predictions to valid probability range [0,1]
2. ✅ Accounts for heteroscedastic variance inherent in binary data
3. ✅ Uses appropriate binomial likelihood, not normal distribution assumption
4. ✅ Provides interpretable odds ratios (e^(-0.08) ≈ 0.923 = 7.7% decrease in odds per year)

Using linear regression for binary outcomes is statistically inappropriate and can lead to nonsensical predictions and invalid inference.

---

# END OF ANSWERS