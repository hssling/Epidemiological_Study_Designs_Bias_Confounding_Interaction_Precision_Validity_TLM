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
