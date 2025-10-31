# Module 4: Inferential Statistics

## Learning Objectives
- Understand sampling and sampling distributions
- Calculate and interpret confidence intervals
- Perform hypothesis testing
- Understand Type I and Type II errors
- Interpret p-values and statistical significance

## Sampling Theory

### Populations and Samples
- **Population**: Complete set of interest
- **Sample**: Subset used for inference
- **Sampling frame**: List of population elements
- **Sampling methods**: Random, stratified, cluster, systematic

### Sampling Distributions
- **Sampling distribution**: Distribution of a statistic over many samples
- **Standard error**: Standard deviation of sampling distribution
- **Central Limit Theorem**: Sample means approach normal distribution

## Confidence Intervals

### Concept
- Range of values likely to contain true population parameter
- Based on sample data and desired confidence level

### Formula for Mean (σ known)
CI = $\bar{x} \pm z \times \frac{\sigma}{\sqrt{n}}$

### Formula for Mean (σ unknown)
CI = $\bar{x} \pm t \times \frac{s}{\sqrt{n}}$

### Formula for Proportion
CI = $p \pm z \sqrt{\frac{p(1-p)}{n}}$

### Interpretation
- 95% CI: 95% confidence that interval contains true parameter
- Wider intervals: More uncertainty
- Factors affecting width: Sample size, variability, confidence level

## Hypothesis Testing

### Steps in Hypothesis Testing
1. **State hypotheses**
   - H₀: Null hypothesis (no effect/difference)
   - H₁: Alternative hypothesis (effect/difference exists)

2. **Choose significance level (α)**
   - Common values: 0.05, 0.01, 0.10

3. **Select test statistic**

4. **Determine critical value or p-value**

5. **Make decision**
   - Reject H₀ if p < α
   - Fail to reject H₀ if p ≥ α

### Types of Errors
- **Type I Error (α)**: Reject true H₀ (false positive)
- **Type II Error (β)**: Fail to reject false H₀ (false negative)
- **Power (1-β)**: Probability of correctly rejecting false H₀

### Power Analysis
**Factors affecting power**:
- Sample size (primary factor)
- Effect size
- Significance level (α)
- Variability

**Sample size formula**: n = [(zα + zβ)/δ]² × σ²

## Common Statistical Tests

### Parametric Tests (Normal data, equal variances)

#### One-sample t-test
- Compare sample mean to known value
- H₀: μ = μ₀

#### Two-sample t-test
- Compare means of two groups
- Independent samples or paired

#### One-way ANOVA
- Compare means of three or more groups
- Tests if at least one group differs

#### Pearson Correlation
- Measure linear relationship between variables
- Range: -1 to +1

### Non-parametric Tests (No normality assumption)

#### Chi-square test
- Test independence of categorical variables
- Goodness of fit

#### Mann-Whitney U test
- Compare two independent groups
- Alternative to t-test

#### Kruskal-Wallis test
- Compare three or more independent groups
- Alternative to ANOVA

#### Spearman correlation
- Measure monotonic relationship
- Alternative to Pearson correlation

## p-Values and Significance

### p-Value Definition
- Probability of observing data as extreme as sample data, assuming H₀ true
- Smaller p-values: Stronger evidence against H₀

### Significance Levels
- **p < 0.05**: Statistically significant
- **p < 0.01**: Highly significant
- **p < 0.001**: Very highly significant

### Misconceptions
- p-value ≠ probability that H₀ is true
- p-value ≠ importance of result
- Statistical significance ≠ clinical significance

## Effect Size

### Importance
- Magnitude of relationship or difference
- Independent of sample size
- More meaningful than p-values

### Common Measures
- **Cohen's d**: Standardized mean difference
- **Odds ratio**: For categorical outcomes
- **Relative risk**: For incidence data
- **R²**: Proportion of variance explained

## Summary

Inferential statistics allow us to make conclusions about populations from sample data. Confidence intervals provide estimates with uncertainty, while hypothesis testing helps determine if observed effects are real. Understanding Type I/II errors, power, and effect sizes is crucial for proper interpretation of statistical results.

## Key Takeaways
- Sampling distributions enable inference about populations
- Confidence intervals estimate parameters with uncertainty
- Hypothesis testing evaluates evidence against null hypothesis
- Type I/II errors represent different kinds of mistakes
- Effect size measures practical importance of results

## Practice Questions

1. What is the difference between a confidence interval and a hypothesis test?
2. Explain Type I and Type II errors with examples.
3. How does sample size affect statistical power?
4. Why is effect size important in addition to p-values?

## Further Reading
- Cohen J. Statistical Power Analysis for the Behavioral Sciences. 2nd ed. Lawrence Erlbaum Associates; 1988
- Cumming G. Understanding the New Statistics: Effect Sizes, Confidence Intervals, and Meta-Analysis. Routledge; 2012
- Kirk RE. Experimental Design: Procedures for the Behavioral Sciences. 4th ed. Sage Publications; 2012
