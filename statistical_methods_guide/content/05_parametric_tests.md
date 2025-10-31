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
