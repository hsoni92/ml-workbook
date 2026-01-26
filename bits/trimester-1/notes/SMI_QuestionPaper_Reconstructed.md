# Statistics – Question Paper (Reconstructed)

**Time:** 3 Hours
**Maximum Marks:** 70

---

## Question 1: One-Way ANOVA (15 Marks)

A researcher wants to study whether the mean performance scores differ among three different teaching methods (Method A, Method B, Method C). The following summary statistics are obtained:

| Source of Variation | Sum of Squares | Degrees of Freedom |
|---------------------|----------------|--------------------|
| Between Groups      | SSB = 240      | 2                  |
| Within Groups       | SSW = 360      | 27                 |
| Total               | SST = 600      | 29                 |

**(a)** State the null hypothesis (H₀) and alternative hypothesis (H₁) for the one-way ANOVA test. **(3 marks)**

**Answer:**
- **H₀ (Null Hypothesis):** μₐ = μᵦ = μᴄ (The mean performance scores are equal across all three teaching methods)
- **H₁ (Alternative Hypothesis):** At least one group mean differs from the others (Not all means are equal)

**Concept:** One-way ANOVA tests whether there are statistically significant differences between the means of three or more independent groups. The null hypothesis assumes all population means are equal, while the alternative suggests at least one differs.

**(b)** Compute the Mean Square Between (MSB) and Mean Square Within (MSW). **(4 marks)**

**Answer:**
- **MSB (Mean Square Between)** = SSB / df_between = 240 / 2 = **120**
- **MSW (Mean Square Within)** = SSW / df_within = 360 / 27 = **13.33**

**Concept:** Mean squares are variance estimates. MSB measures the variance between group means (due to treatment effect + random error), while MSW measures the variance within groups (due to random error only). These values form the basis for the F-statistic calculation.

**(c)** Calculate the F-statistic. **(3 marks)**

**Answer:**
- **F-statistic** = MSB / MSW = 120 / 13.33 = **9.00**

**Concept:** The F-statistic is a ratio comparing between-group variability to within-group variability. A larger F-value suggests that the differences between groups are more significant relative to the variation within groups. If treatment effects exist, MSB will be larger than MSW, resulting in F > 1.

**(d)** Given that the critical F-value at α = 0.05 is F₍₂,₂₇₎ = 3.35, decide whether the null hypothesis should be rejected. Clearly justify your answer. **(3 marks)**

**Answer:**
- **Decision:** Reject the null hypothesis (H₀)
- **Justification:** Since the calculated F-statistic (9.00) > critical F-value (3.35), we have sufficient evidence to reject H₀ at the 5% significance level.
- **Conclusion:** There is statistically significant evidence that the mean performance scores differ among at least two of the three teaching methods.

**Concept:** We compare the calculated F-statistic with the critical value from the F-distribution table. If F_calculated > F_critical, the observed differences are too large to be attributed to random chance alone, leading us to reject the null hypothesis.

**(e)** Is one-way ANOVA an appropriate method for this problem? Briefly explain why or why not. Also, what should be the next step if the null hypothesis is rejected? **(2 marks)**

**Answer:**
- **Appropriateness:** Yes, one-way ANOVA is appropriate because:
  - We have one independent variable (teaching method) with three categories
  - We're comparing means across three independent groups
  - The dependent variable (performance score) is continuous

- **Next Step:** Conduct **post-hoc tests** (e.g., Tukey's HSD, Bonferroni, or Scheffé test) to determine which specific pairs of teaching methods differ significantly from each other.

**Concept:** ANOVA tells us that at least one group differs, but not which specific groups differ. Post-hoc tests perform pairwise comparisons while controlling for Type I error inflation due to multiple comparisons.

---

## Question 2: Simple Linear Regression (15 Marks)

The relationship between hours studied (X) and exam score (Y) is to be modeled using simple linear regression. The following summary values are given:

- Mean of X, x̄ = 10
- Mean of Y, ȳ = 65
- ∑(X − x̄)(Y − ȳ) = 420
- ∑(X − x̄)² = 140

**(a)** Derive the regression equation of Y on X. **(8 marks)**

**Answer:**

**Step 1:** Calculate the slope (b₁)
- Formula: b₁ = ∑(X − x̄)(Y − ȳ) / ∑(X − x̄)²
- b₁ = 420 / 140 = **3.0**

**Step 2:** Calculate the intercept (b₀)
- Formula: b₀ = ȳ − b₁x̄
- b₀ = 65 − 3.0(10) = 65 − 30 = **35**

**Step 3:** Write the regression equation
- **Ŷ = 35 + 3.0X**

Where:
- Ŷ = predicted exam score
- X = hours studied
- 35 = intercept (expected score with 0 hours studied)
- 3.0 = slope (change in score per additional hour studied)

**Concept:** Simple linear regression models the linear relationship between a predictor variable (X) and response variable (Y). The slope represents the rate of change, and the intercept represents the baseline value of Y when X = 0.

**(b)** Interpret the slope coefficient obtained in the context of this problem. **(3 marks)**

**Answer:**
The slope coefficient b₁ = 3.0 means that **for every additional hour of study, the exam score is expected to increase by 3 points**, on average, holding all other factors constant.

**Interpretation Details:**
- The positive slope indicates a positive relationship between study hours and exam performance
- The magnitude (3.0) quantifies this relationship
- This is the average effect; individual variations may exist

**Concept:** The slope in regression represents the marginal effect—the expected change in the dependent variable (Y) for a one-unit increase in the independent variable (X). It's the core interpretive parameter in regression analysis.

**(c)** What assumptions are made while fitting a simple linear regression model? **(4 marks)**

**Answer:**

The key assumptions (LINE) for simple linear regression are:

1. **Linearity:** The relationship between X and Y is linear
   - The true relationship can be adequately represented by a straight line

2. **Independence:** Observations are independent of each other
   - No autocorrelation or clustering in the data

3. **Normality:** Residuals (errors) are normally distributed
   - For hypothesis testing and confidence intervals, errors should follow N(0, σ²)

4. **Equal Variance (Homoscedasticity):** The variance of residuals is constant across all levels of X
   - Spread of residuals doesn't change systematically with X

**Additional Assumption:**
5. **No measurement error in X:** The independent variable is measured without error

**Concept:** Violating these assumptions can lead to biased estimates, incorrect standard errors, invalid hypothesis tests, and unreliable predictions. Diagnostic plots (residual plots, Q-Q plots) are used to check these assumptions.

---

## Question 3: Dependent (Paired) t-Test (15 Marks)

A psychologist measures the reaction time of 10 subjects before and after a training program. The differences (Before − After) have:

- Mean difference = 2.5
- Standard deviation of differences = 1.8

**(a)** State the null and alternative hypotheses for a dependent t-test. **(4 marks)**

**Answer:**
- **H₀ (Null Hypothesis):** μ_d = 0
  - The mean difference in reaction times (Before − After) is zero
  - The training program has no effect on reaction time

- **H₁ (Alternative Hypothesis):** μ_d ≠ 0 (two-tailed) or μ_d > 0 (one-tailed)
  - The mean difference is not zero
  - The training program affects reaction time
  - Since we expect improvement (positive difference), a one-tailed test (μ_d > 0) may be appropriate

Where μ_d represents the population mean of paired differences.

**Concept:** In a paired t-test, we test whether the average of the paired differences differs significantly from zero. This accounts for the correlation between before and after measurements on the same subjects.

**(b)** Calculate the t-statistic. **(5 marks)**

**Answer:**

**Formula:** t = (d̄ − μ₀) / (s_d / √n)

Where:
- d̄ = mean difference = 2.5
- μ₀ = hypothesized mean difference = 0
- s_d = standard deviation of differences = 1.8
- n = number of pairs = 10

**Calculation:**

**Step 1:** Calculate the standard error (SE)
- SE = s_d / √n = 1.8 / √10 = 1.8 / 3.162 = 0.569

**Step 2:** Calculate the t-statistic
- t = (2.5 − 0) / 0.569 = 2.5 / 0.569 = **4.39**

**Concept:** The t-statistic measures how many standard errors the sample mean difference is away from the hypothesized population mean (typically 0). A larger absolute t-value indicates stronger evidence against the null hypothesis.

**(c)** At α = 0.05 and 9 degrees of freedom, the critical t-value is 2.262. Test the hypothesis and draw a conclusion. **(4 marks)**

**Answer:**

**Decision Rule:** For a two-tailed test, reject H₀ if |t_calculated| > t_critical

**Comparison:**
- Calculated t-statistic = 4.39
- Critical t-value = 2.262
- Since |4.39| > 2.262, we **reject the null hypothesis**

**Conclusion:**
At the 5% significance level, there is **statistically significant evidence** that the training program affects reaction time. The mean difference of 2.5 units is significantly different from zero, suggesting the training program was effective in changing reaction times.

**Practical Interpretation:** The subjects showed a significant improvement (reduction) in reaction time after the training program.

**Concept:** We compare the calculated t-statistic with the critical value from the t-distribution table. If the calculated value exceeds the critical value, the observed difference is unlikely to have occurred by chance alone, leading us to reject the null hypothesis.

**(d)** Why is a paired t-test more appropriate here than an independent samples t-test? **(2 marks)**

**Answer:**

A paired t-test is more appropriate because:

1. **Same Subjects Measured Twice:** The data consists of repeated measurements on the same 10 subjects (before and after training), creating natural pairs.

2. **Controls for Individual Differences:** By using the same subjects, we eliminate between-subject variability. Each subject serves as their own control, making the test more powerful and sensitive to detect the treatment effect.

3. **Dependent/Correlated Observations:** The before and after measurements are not independent—they're correlated because they come from the same individuals.

**Concept:** Paired t-tests have higher statistical power than independent t-tests in repeated measures designs because they account for the correlation within pairs, reducing the error variance. An independent t-test would incorrectly treat the measurements as coming from different individuals, ignoring this valuable information and potentially missing real effects.

---

## Question 4: Factor Analysis – KMO and Bartlett's Test (15 Marks)

A researcher intends to perform factor analysis on a dataset containing multiple variables. The following results are obtained:

- Kaiser–Meyer–Olkin (KMO) Measure = 0.81
- Bartlett's Test of Sphericity:
  - χ² = 420.6
  - p-value < 0.001

**(a)** What does the KMO statistic measure? Interpret the given KMO value. **(5 marks)**

**Answer:**

**What KMO Measures:**
The Kaiser-Meyer-Olkin (KMO) statistic measures **sampling adequacy** for factor analysis. Specifically, it:
- Assesses how much variance in variables is common variance (suitable for grouping into factors)
- Compares the magnitude of observed correlation coefficients to partial correlation coefficients
- Ranges from 0 to 1

**Formula Concept:** KMO = (Sum of squared correlations) / (Sum of squared correlations + Sum of squared partial correlations)

**Interpretation of KMO = 0.81:**
- **Rating:** "Meritorious" or "Good"
- **Meaning:** The data is well-suited for factor analysis
- The variables share enough common variance to justify data reduction through factor analysis

**KMO Interpretation Guidelines:**
- 0.90+ = Marvelous
- 0.80-0.89 = Meritorious
- 0.70-0.79 = Middling
- 0.60-0.69 = Mediocre
- 0.50-0.59 = Miserable
- Below 0.50 = Unacceptable

**Concept:** KMO helps determine whether the correlation patterns in the data are compact enough to yield reliable and distinct factors. High KMO values indicate that factor analysis will likely produce meaningful results.

**(b)** State the null hypothesis of Bartlett's Test of Sphericity. **(4 marks)**

**Answer:**

**H₀ (Null Hypothesis):** The correlation matrix is an identity matrix.

**Detailed Explanation:**
- **Identity Matrix:** A matrix with 1s on the diagonal and 0s elsewhere
- **Implication:** All variables are uncorrelated with each other (correlation = 0)
- **In other words:** The variables are orthogonal and share no common variance

**Alternative Hypothesis (H₁):** The correlation matrix is NOT an identity matrix (i.e., at least some correlations exist among variables)

**Why This Matters:**
If the null hypothesis is true (variables are uncorrelated), factor analysis is inappropriate because there's no underlying structure to extract. We want to **reject** this null hypothesis to justify performing factor analysis.

**Concept:** Bartlett's Test assesses whether the observed correlation matrix differs significantly from an identity matrix. It uses chi-square distribution to test this hypothesis. Significant results (p < 0.05) indicate sufficient correlations exist for factor analysis.

**(c)** Based on the Bartlett's test result, comment on the suitability of the data for factor analysis. **(4 marks)**

**Answer:**

**Test Results:**
- χ² = 420.6
- p-value < 0.001 (highly significant)

**Decision:** **Reject the null hypothesis** at α = 0.05 (and even at α = 0.001)

**Interpretation:**
The extremely low p-value (< 0.001) provides very strong evidence that the correlation matrix is NOT an identity matrix. This means:
- Significant correlations exist among the variables
- The variables share common variance
- There is underlying structure in the data

**Conclusion on Suitability:**
The data is **highly suitable for factor analysis**. The significant Bartlett's test result confirms that:
1. Variables are sufficiently intercorrelated
2. Data reduction through factor analysis is justified
3. Meaningful factors can likely be extracted from the data

**Combined with KMO:** Both tests (KMO = 0.81 and significant Bartlett's test) strongly support proceeding with factor analysis.

**Concept:** Bartlett's test is a prerequisite check for factor analysis. A significant result (rejecting H₀) is desirable as it confirms the presence of correlations needed for factor extraction. A non-significant result would suggest factor analysis is inappropriate.

**(d)** What conclusions can be drawn when KMO is low but Bartlett's test is significant? **(2 marks)**

**Answer:**

When **KMO is low** (< 0.5 or 0.6) but **Bartlett's test is significant**, it indicates a **conflicting situation:**

**Interpretation:**

1. **Bartlett's test (significant)** suggests:
   - Correlations exist among variables (good for factor analysis)
   - Variables are not independent

2. **Low KMO** suggests:
   - The pattern of correlations is diffuse or scattered
   - Partial correlations are too high relative to simple correlations
   - Sampling adequacy is poor
   - Individual variables may not group well into coherent factors

**Conclusions:**
- **Proceed with caution:** While correlations exist, they may not form clear factor structures
- **Possible issues:** Some variables might be measuring unique constructs or have weak loadings
- **Recommendation:**
  - Review individual KMO values for each variable (MSA)
  - Consider removing variables with very low individual KMO
  - Factor analysis may produce unclear or unreliable factors

**Concept:** KMO and Bartlett's test assess different aspects. Bartlett's tests for presence of correlations, while KMO tests for quality/pattern of correlations. Both should ideally support factor analysis, but KMO is often considered more important for practical factor analysis success.

---

**End of Question Paper**