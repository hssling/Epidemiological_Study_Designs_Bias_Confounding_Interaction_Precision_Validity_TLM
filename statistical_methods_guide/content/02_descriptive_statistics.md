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
