# Module 1: Introduction to Statistical Methods

## Learning Objectives
- Define statistics and its role in research
- Understand the difference between descriptive and inferential statistics
- Identify types of data and measurement scales
- Understand the research process and study designs
- Recognize ethical considerations in statistical analysis

## What is Statistics?

Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data. It provides methods for making inferences about populations from samples and for quantifying uncertainty.

**Key terms:**
- **Population**: Complete set of individuals or objects of interest
- **Sample**: Subset of the population used for study
- **Parameter**: Numerical characteristic of a population
- **Statistic**: Numerical characteristic of a sample
- **Variable**: Characteristic that varies among individuals

## Branches of Statistics

### 1. Descriptive Statistics
- Organize and summarize data
- Describe main features of a dataset
- Include measures of central tendency, dispersion, and distribution

### 2. Inferential Statistics
- Make inferences about populations from samples
- Test hypotheses and draw conclusions
- Include estimation, hypothesis testing, and prediction

## Types of Data

### By Nature
- **Quantitative**: Numerical measurements
  - **Discrete**: Countable values (e.g., number of children)
  - **Continuous**: Measurable values (e.g., height, weight)

- **Qualitative**: Categorical measurements
  - **Nominal**: Categories without order (e.g., gender, blood type)
  - **Ordinal**: Categories with order (e.g., education level, pain scale)

### By Measurement Scale
- **Nominal**: Categories, no quantitative meaning
- **Ordinal**: Ordered categories, unequal intervals
- **Interval**: Equal intervals, no true zero
- **Ratio**: Equal intervals, true zero point

## The Research Process

### 1. Problem Identification
- Define research question
- Review existing literature
- Formulate hypotheses

### 2. Study Design
- Choose appropriate design
- Determine sample size
- Select measurement methods

### 3. Data Collection
- Implement data collection procedures
- Ensure data quality
- Maintain ethical standards

### 4. Data Analysis
- Clean and prepare data
- Apply statistical methods
- Interpret results

### 5. Reporting Results
- Present findings clearly
- Draw appropriate conclusions
- Suggest future research

## Study Designs in Research

### Experimental Designs
- **Randomized Controlled Trials (RCTs)**: Gold standard for establishing causality
- **Quasi-experimental**: Intervention without randomization
- **Field Experiments**: Natural setting interventions

### Observational Designs
- **Cohort Studies**: Follow groups over time
- **Case-Control Studies**: Compare cases and controls
- **Cross-Sectional Studies**: Snapshot at single point
- **Ecological Studies**: Population-level data

## Ethical Considerations

### Key Principles
- **Respect for persons**: Informed consent, voluntary participation
- **Beneficence**: Maximize benefits, minimize harms
- **Justice**: Fair distribution of benefits and burdens
- **Confidentiality**: Protect participant privacy

### Statistical Ethics
- **Data integrity**: Accurate data collection and analysis
- **Transparency**: Clear reporting of methods and results
- **Objectivity**: Avoid bias in analysis and interpretation
- **Reproducibility**: Enable verification of results

## Software Tools for Statistics

### Statistical Software
- **R**: Free, powerful statistical programming language
- **Python**: General programming with statistical libraries
- **SPSS**: User-friendly interface for statistical analysis
- **SAS**: Enterprise statistical software
- **Stata**: Comprehensive statistical package

### Data Visualization
- **Tableau**: Interactive data visualization
- **Power BI**: Business intelligence and analytics
- **ggplot2 (R)**: Advanced plotting capabilities
- **matplotlib (Python)**: Flexible plotting library

## Summary

Statistical methods provide the tools for extracting meaningful insights from data. Understanding the fundamentals of statistics is essential for conducting valid research and making evidence-based decisions in health sciences and beyond.

## Key Takeaways
- Statistics involves collecting, analyzing, and interpreting data
- Descriptive statistics summarize data, inferential statistics make predictions
- Data types determine appropriate statistical methods
- Research follows systematic process from question to conclusion
- Ethical considerations are crucial in statistical practice

## Practice Questions

1. What is the difference between a population and a sample?
2. Give examples of nominal, ordinal, interval, and ratio data.
3. Why are ethical considerations important in statistical analysis?
4. Name three statistical software packages and their main uses.

## Further Reading
- Kirkwood BR, Sterne JAC. Essential Medical Statistics. 2nd ed. Oxford: Blackwell Science; 2003
- Bland M. An Introduction to Medical Statistics. 3rd ed. Oxford: Oxford University Press; 2000
- Daniel WW. Biostatistics: A Foundation for Analysis in the Health Sciences. 7th ed. New York: Wiley; 1999
# Module 2: Descriptive Statistics

## Learning Objectives
- Understand measures of central tendency
- Calculate and interpret measures of dispersion
- Describe data distributions
- Create and interpret data visualizations
- Understand sampling distributions

## Measures of Central Tendency

### Mean (Arithmetic Average)
**Formula**: $\bar{x} = \frac{\sum x_i}{n}$

**Example**: Test scores: 85, 90, 78, 92, 88
Mean = (85 + 90 + 78 + 92 + 88) / 5 = 86.6

**Advantages**:
- Uses all data points
- Mathematically useful
- Foundation for many statistical tests

**Disadvantages**:
- Affected by extreme values (outliers)
- Not appropriate for ordinal data

### Median (Middle Value)
**Calculation**:
- Sort data in ascending order
- For odd n: Middle value
- For even n: Average of two middle values

**Example**: Ages: 23, 25, 28, 30, 35
Median = 28

**Advantages**:
- Not affected by outliers
- Appropriate for ordinal data
- Easy to understand

### Mode (Most Frequent Value)
**Definition**: Value that appears most frequently

**Example**: Blood types: A, B, AB, A, O, A
Mode = A

**Uses**:
- Categorical data
- Identifying most common category
- Bimodal/multimodal distributions

## Measures of Dispersion

### Range
**Formula**: Range = Maximum - Minimum

**Example**: Heights: 160, 165, 170, 175, 180 cm
Range = 180 - 160 = 20 cm

**Limitations**:
- Only uses extreme values
- Affected by outliers
- No information about data distribution

### Variance
**Population Variance**: $\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$

**Sample Variance**: $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$

**Interpretation**: Average squared deviation from mean

### Standard Deviation
**Formula**: $s = \sqrt{s^2}$

**Example**: Data: 10, 12, 14, 16, 18
Mean = 14, Variance = 8, SD = √8 ≈ 2.83

**Coefficient of Variation**: CV = (s/mean) × 100%

## Data Distributions

### Normal Distribution
- Bell-shaped, symmetric
- Mean = Median = Mode
- 68% within 1 SD, 95% within 2 SD, 99.7% within 3 SD
- Many statistical tests assume normality

### Skewness
- **Positive skew**: Tail extends to right
- **Negative skew**: Tail extends to left
- **Symmetric**: No skew

### Kurtosis
- **Mesokurtic**: Normal peakedness
- **Leptokurtic**: More peaked than normal
- **Platykurtic**: Less peaked than normal

## Data Visualization

### Histograms
- Show frequency distribution
- Bar chart for continuous data
- Height represents frequency

### Box Plots (Box-and-Whisker Plots)
- Show median, quartiles, outliers
- Box: IQR (Q3-Q1)
- Whiskers: 1.5 × IQR
- Points: Outliers

### Scatter Plots
- Show relationship between two variables
- X-axis: Independent variable
- Y-axis: Dependent variable
- Pattern indicates correlation

### Bar Charts and Pie Charts
- Categorical data
- Bar charts: Compare categories
- Pie charts: Show proportions

## Sampling Distributions

### Central Limit Theorem
- Sample means follow normal distribution
- Regardless of population distribution
- For sufficiently large samples (n ≥ 30)

### Standard Error
**Formula**: $SE = \frac{s}{\sqrt{n}}$

**Interpretation**: Standard deviation of sampling distribution

**Uses**:
- Confidence interval calculation
- Hypothesis testing
- Sample size determination

## Summary

Descriptive statistics provide the foundation for understanding data. Measures of central tendency describe typical values, while measures of dispersion describe variability. Data visualization helps identify patterns and outliers, and sampling distributions form the basis for inferential statistics.

## Key Takeaways
- Mean, median, and mode describe central tendency
- Range, variance, and standard deviation measure dispersion
- Normal distribution is fundamental to many statistical methods
- Data visualization aids in understanding and communication
- Sampling distributions enable inference about populations

## Practice Questions

1. Calculate mean, median, and mode for: 12, 15, 18, 15, 20, 22, 15
2. What is the difference between variance and standard deviation?
3. How does skewness affect data interpretation?
4. When should you use a histogram vs. a bar chart?

## Further Reading
- Moore DS, McCabe GP, Craig BA. Introduction to the Practice of Statistics. 8th ed. New York: W.H. Freeman; 2014
- Agresti A, Franklin C. Statistics: The Art and Science of Learning from Data. 4th ed. Pearson; 2018
- Devore JL. Probability and Statistics for Engineering and the Sciences. 9th ed. Cengage Learning; 2015
# Module 3: Probability Theory

## Learning Objectives
- Understand basic probability concepts
- Calculate probabilities using different rules
- Work with common probability distributions
- Understand conditional probability and independence
- Apply Bayes' theorem

## Basic Probability Concepts

### Probability
**Definition**: Measure of likelihood that an event will occur

**Range**: 0 ≤ P(A) ≤ 1
- P(A) = 0: Impossible event
- P(A) = 1: Certain event

### Sample Space
**Definition**: All possible outcomes of an experiment

**Examples**:
- Coin flip: {Heads, Tails}
- Die roll: {1, 2, 3, 4, 5, 6}

### Events
- **Simple event**: Single outcome
- **Compound event**: Combination of outcomes
- **Mutually exclusive**: Cannot occur together
- **Independent**: Occurrence doesn't affect other events

## Probability Rules

### Addition Rule
**For mutually exclusive events**: P(A ∪ B) = P(A) + P(B)

**For non-mutually exclusive events**: P(A ∪ B) = P(A) + P(B) - P(A ∩ B)

### Multiplication Rule
**For independent events**: P(A ∩ B) = P(A) × P(B)

**For dependent events**: P(A ∩ B) = P(A) × P(B|A)

### Complement Rule
P(A') = 1 - P(A)

### Conditional Probability
**Formula**: P(A|B) = P(A ∩ B) / P(B)

**Example**: Probability of having disease given positive test

## Bayes' Theorem

### Formula
P(A|B) = [P(B|A) × P(A)] / P(B)

### Extended Form
P(A|B) = [P(B|A) × P(A)] / [P(B|A) × P(A) + P(B|A') × P(A')]

### Applications
- Medical diagnosis
- Spam filtering
- Risk assessment
- Quality control

## Common Probability Distributions

### Discrete Distributions

#### Binomial Distribution
- Fixed number of trials (n)
- Each trial: success/failure
- Constant probability of success (p)
- Independent trials

**Mean**: μ = n × p
**Variance**: σ² = n × p × (1-p)

**Example**: Number of heads in 10 coin flips

#### Poisson Distribution
- Counts rare events
- Events occur randomly over time/space
- Constant average rate (λ)

**Mean = Variance = λ**

**Example**: Number of accidents per day

### Continuous Distributions

#### Normal Distribution
- Bell-shaped, symmetric
- Defined by mean (μ) and standard deviation (σ)
- 68-95-99.7 rule

**Standard Normal**: μ = 0, σ = 1
**Z-score**: z = (x - μ) / σ

#### t-Distribution
- Similar to normal but with heavier tails
- Used for small samples
- Degrees of freedom = n - 1

#### Chi-Square Distribution
- Sum of squared standard normal variables
- Used for goodness of fit and independence tests
- Degrees of freedom vary

## Expected Value and Variance

### Expected Value (Mean)
**Discrete**: E[X] = Σ x × P(x)

**Continuous**: E[X] = ∫ x × f(x) dx

### Variance
Var(X) = E[X²] - (E[X])²

### Properties
- E[aX + b] = aE[X] + b
- Var(aX + b) = a²Var(X)
- Var(X + Y) = Var(X) + Var(Y) (if independent)

## Summary

Probability theory provides the foundation for statistical inference. Understanding probability rules, distributions, and concepts like conditional probability and Bayes' theorem is essential for advanced statistical analysis and decision-making under uncertainty.

## Key Takeaways
- Probability measures likelihood of events
- Addition and multiplication rules combine probabilities
- Conditional probability depends on additional information
- Bayes' theorem updates probabilities with new evidence
- Different distributions model different types of data

## Practice Questions

1. If P(A) = 0.3 and P(B) = 0.4, what is P(A ∪ B) if A and B are mutually exclusive?
2. A test has 95% sensitivity and 90% specificity. If disease prevalence is 10%, what is the probability that a positive test indicates disease?
3. What is the difference between binomial and Poisson distributions?
4. Calculate the expected value of rolling a fair die.

## Further Reading
- Ross SM. Introduction to Probability Models. 12th ed. Academic Press; 2019
- Blitzstein JK, Hwang J. Introduction to Probability. 2nd ed. Chapman & Hall/CRC; 2019
- Pitman J. Probability. Springer; 1993
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
# Module 5: Parametric Statistical Tests

## Learning Objectives
- Understand assumptions of parametric tests
- Perform and interpret t-tests
- Conduct ANOVA and post-hoc tests
- Calculate and interpret correlation coefficients
- Understand linear regression

## Assumptions of Parametric Tests

### Normality
- Data follows normal distribution
- Check with histograms, Q-Q plots, Shapiro-Wilk test
- Central Limit Theorem helps with large samples

### Homoscedasticity (Equal Variances)
- Variances equal across groups
- Test with Levene's test or Bartlett's test
- Important for t-tests and ANOVA

### Independence
- Observations independent of each other
- Violated in repeated measures designs
- Important for all parametric tests

### Linearity
- Relationship between variables is linear
- Check with scatter plots
- Important for correlation and regression

## t-Tests

### One-Sample t-Test
**Purpose**: Test if sample mean differs from known population mean

**Formula**: t = (x̄ - μ₀) / (s / √n)

**Example**: Test if average height differs from national average

### Independent Samples t-Test
**Purpose**: Compare means of two independent groups

**Formula**: t = (x̄₁ - x̄₂) / √[(s₁²/n₁) + (s₂²/n₂)]

**Assumptions**:
- Independent observations
- Normal distribution in each group
- Equal variances (or use Welch's correction)

### Paired t-Test
**Purpose**: Compare means of two related groups

**Formula**: t = (x̄_d) / (s_d / √n)

Where x̄_d is mean of differences

**Uses**:
- Before-after studies
- Matched pairs
- Repeated measures

## Analysis of Variance (ANOVA)

### One-Way ANOVA
**Purpose**: Compare means of three or more groups

**Logic**: Partition total variation into between-group and within-group

**F-statistic**: F = MS_between / MS_within

**Post-hoc tests**:
- Tukey's HSD: Compare all pairs
- Bonferroni: Control family-wise error
- Dunnett's: Compare to control group

### Two-Way ANOVA
**Purpose**: Examine effects of two factors and their interaction

**Model**: Y = μ + A + B + AB + ε

**Main effects**: Effect of each factor alone
**Interaction**: Combined effect of factors

### Repeated Measures ANOVA
**Purpose**: Compare means across multiple time points or conditions

**Advantages**:
- Controls for individual differences
- Requires fewer subjects
- More powerful than independent groups

## Correlation Analysis

### Pearson Correlation
**Purpose**: Measure strength and direction of linear relationship

**Formula**: r = Σ[(x_i - x̄)(y_i - ȳ)] / √[Σ(x_i - x̄)² Σ(y_i - ȳ)²]

**Interpretation**:
- +1: Perfect positive correlation
- 0: No linear relationship
- -1: Perfect negative correlation

**Hypothesis testing**: t = r √[(n-2)/(1-r²)]

### Correlation vs. Causation
- Correlation does not imply causation
- Third variable may explain relationship
- Experimental design needed for causality

## Linear Regression

### Simple Linear Regression
**Model**: Y = β₀ + β₁X + ε

**Parameters**:
- β₀: Intercept (Y when X=0)
- β₁: Slope (change in Y per unit X)
- ε: Error term

**Estimation**: Least squares method

### Multiple Linear Regression
**Model**: Y = β₀ + β₁X₁ + β₂X₂ + ... + βₖXₖ + ε

**Assumptions**:
- Linearity
- Independence
- Homoscedasticity
- Normality of residuals

### Model Evaluation
- **R²**: Proportion of variance explained
- **Adjusted R²**: Penalizes for additional variables
- **F-test**: Overall model significance
- **t-tests**: Individual coefficient significance

### Regression Diagnostics
- **Residual plots**: Check assumptions
- **Influential points**: Cook's distance
- **Multicollinearity**: VIF > 10
- **Outliers**: Standardized residuals > 3

## Summary

Parametric tests provide powerful tools for comparing groups and examining relationships when assumptions are met. Understanding test assumptions, proper interpretation, and appropriate use of post-hoc tests is essential for valid statistical analysis.

## Key Takeaways
- Parametric tests require normality and equal variances
- t-tests compare means between groups
- ANOVA extends t-tests to multiple groups
- Correlation measures linear relationships
- Regression predicts outcomes from predictors

## Practice Questions

1. What are the main assumptions of parametric tests?
2. When should you use a paired t-test vs. independent samples t-test?
3. Explain the difference between one-way and two-way ANOVA.
4. How do you interpret an R² value in regression?

## Further Reading
- Kutner MH, Nachtsheim CJ, Neter J, Li W. Applied Linear Statistical Models. 5th ed. McGraw-Hill/Irwin; 2005
- Montgomery DC, Peck EA, Vining GG. Introduction to Linear Regression Analysis. 5th ed. Wiley; 2012
- Draper NR, Smith H. Applied Regression Analysis. 3rd ed. Wiley; 1998
# Module 6: Non-Parametric Statistical Tests

## Learning Objectives
- Understand when to use non-parametric tests
- Perform and interpret chi-square tests
- Apply Mann-Whitney and Kruskal-Wallis tests
- Use Spearman's correlation
- Understand non-parametric alternatives

## When to Use Non-Parametric Tests

### Advantages
- **No normality assumption**: Work with any distribution
- **Ordinal data**: Appropriate for ranked data
- **Robust**: Less affected by outliers
- **Small samples**: Often more powerful with small n

### Disadvantages
- **Less powerful**: May miss real effects with normal data
- **Less precise**: Often only test for differences, not magnitude
- **Ordinal results**: May lose information from continuous data

### Decision Criteria
- Data not normally distributed
- Ordinal or nominal data
- Small sample sizes
- Presence of outliers

## Chi-Square Tests

### Chi-Square Goodness of Fit
**Purpose**: Test if observed frequencies match expected distribution

**Formula**: χ² = Σ [(O_i - E_i)² / E_i]

**Example**: Test if die is fair
- Expected: Each face 1/6 = 16.67
- Observed: 20, 15, 18, 16, 17, 14

### Chi-Square Test of Independence
**Purpose**: Test if two categorical variables are independent

**Contingency table**:
```
         Variable B
Variable A | B1 | B2 | Total
-----------|----|----|------
A1        |    |    |
A2        |    |    |
-----------|----|----|------
Total     |    |    |
```

**Formula**: Same as goodness of fit, but for all cells

**Expected frequency**: E_ij = (Row total × Column total) / Grand total

### Fisher's Exact Test
**Purpose**: Alternative to chi-square for small samples

**Uses**: 2×2 tables with small expected frequencies (<5)

## Mann-Whitney U Test

### Purpose
- Compare two independent groups
- Alternative to independent samples t-test
- Works with ordinal or continuous data

### Logic
- Rank all observations combined
- Compare sum of ranks between groups
- Test if groups come from same distribution

### Formula
U = n₁n₂ + n₁(n₁+1)/2 - R₁

Where R₁ is sum of ranks in group 1

### Effect Size
r = |z| / √(n₁ + n₂)

## Kruskal-Wallis Test

### Purpose
- Compare three or more independent groups
- Extension of Mann-Whitney test
- Alternative to one-way ANOVA

### Logic
- Rank all observations
- Compare mean ranks between groups
- Chi-square approximation for large samples

### Post-hoc Tests
- Dunn's test for pairwise comparisons
- Bonferroni correction for multiple tests

## Wilcoxon Signed-Rank Test

### Purpose
- Compare two related samples
- Alternative to paired t-test
- Works with ordinal data

### Procedure
1. Calculate differences between pairs
2. Rank absolute differences
3. Assign signs based on direction
4. Test if positive and negative ranks balanced

## Spearman's Rank Correlation

### Purpose
- Measure monotonic relationship between variables
- Alternative to Pearson correlation
- Works with ordinal data

### Calculation
1. Rank both variables
2. Calculate Pearson correlation on ranks

**Formula**: r_s = 1 - (6Σd_i²) / (n(n²-1))

## Summary

Non-parametric tests provide robust alternatives when parametric assumptions are not met. They work with ordinal data and non-normal distributions, making them valuable tools for real-world data analysis.

## Key Takeaways
- Non-parametric tests don't require normality assumptions
- Chi-square tests analyze categorical data
- Mann-Whitney and Kruskal-Wallis compare groups using ranks
- Wilcoxon signed-rank test compares paired data
- Spearman's correlation measures monotonic relationships

## Practice Questions

1. When should you choose non-parametric over parametric tests?
2. How does the Mann-Whitney U test work?
3. What is the difference between chi-square goodness of fit and test of independence?
4. How do you interpret Spearman's correlation coefficient?

## Further Reading
- Siegel S, Castellan NJ. Nonparametric Statistics for the Behavioral Sciences. 2nd ed. McGraw-Hill; 1988
- Conover WJ. Practical Nonparametric Statistics. 3rd ed. Wiley; 1999
- Hollander M, Wolfe DA, Chicken E. Nonparametric Statistical Methods. 3rd ed. Wiley; 2013
