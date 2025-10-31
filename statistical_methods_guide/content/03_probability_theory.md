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
