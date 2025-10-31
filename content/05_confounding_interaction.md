# Module 5: Confounding and Interaction

## Learning Objectives
- Define confounding and understand its impact on study results
- Identify confounders in epidemiological studies
- Learn methods to control for confounding
- Understand effect modification (interaction)
- Distinguish between confounding and interaction

## Confounding

### Definition
**Confounding** is a mixing of effects where the apparent association between exposure and outcome is distorted by the effect of a third variable (confounder).

### Characteristics of a Confounder
A variable is a confounder if it meets ALL THREE criteria:

1. **Associated with exposure**: Confounder must be related to the exposure of interest
2. **Independently associated with outcome**: Confounder must affect the outcome
3. **Not in the causal pathway**: Confounder should not be an intermediate variable

### Example: Smoking and Lung Cancer
```
Age → Smoking → Lung Cancer
     ↑
     └── Confounder: Age is associated with both smoking and lung cancer
```

- Older people are more likely to smoke (age associated with exposure)
- Older people are more likely to develop lung cancer (age associated with outcome)
- Age is not caused by smoking (not in causal pathway)

**Crude association**: Smoking appears strongly associated with lung cancer
**After controlling for age**: The association is weaker but still present

## Types of Confounding

### 1. Positive Confounding
- Confounder increases the apparent association
- Example: Age in smoking-lung cancer association

### 2. Negative Confounding
- Confounder decreases the apparent association
- Example: Socioeconomic status in some associations

### 3. Quantifying Confounding
- **Confounding bias**: Difference between crude and adjusted estimates
- **Percent change**: [(Crude RR - Adjusted RR) / Crude RR] × 100

## Methods to Control Confounding

### 1. Study Design Level

#### A. Randomization
- **How it works**: Balances confounders across groups
- **Best method**: In experimental studies
- **Limitations**: Not always possible (observational studies)

#### B. Restriction
- **Definition**: Limit study to participants with similar levels of confounder
- **Example**: Study only adults aged 40-60 to control for age
- **Advantages**: Simple, effective
- **Limitations**: Reduces generalizability, may not control multiple confounders

#### C. Matching
- **Definition**: Select controls similar to cases on confounding variables
- **Types**:
  - **Individual matching**: Each case matched to specific control(s)
  - **Frequency matching**: Controls selected to match case distribution
- **Example**: Match cases and controls by age and sex
- **Advantages**: Ensures balance on matched variables
- **Limitations**: Can only match on known confounders, matching on too many variables difficult

### 2. Analysis Level

#### A. Stratification
- **Definition**: Analyze data separately within strata of the confounder
- **Example**: Calculate association separately for different age groups
- **Mantel-Haenszel method**: Combines stratum-specific estimates
- **Advantages**: Simple, shows effect modification
- **Limitations**: Limited to few confounders

#### B. Statistical Adjustment
- **Multivariable regression**: Controls for multiple confounders simultaneously
- **Types**:
  - Linear regression (continuous outcomes)
  - Logistic regression (binary outcomes)
  - Cox regression (time-to-event outcomes)
- **Advantages**: Can control many confounders, handles continuous variables
- **Limitations**: Requires assumptions, can over-adjust

#### C. Standardization
- **Direct standardization**: Apply study rates to standard population
- **Indirect standardization**: Compare observed vs. expected rates
- **Purpose**: Compare rates across populations with different age structures

## Effect Modification (Interaction)

### Definition
**Effect modification** occurs when the association between exposure and outcome differs across levels of a third variable.

### Key Differences from Confounding

| Aspect | Confounding | Effect Modification |
|--------|-------------|-------------------|
| **Effect on association** | Distorts the association | Changes the association |
| **Control method** | Should be controlled | Should NOT be controlled |
| **Interpretation** | Single effect estimate | Separate estimates for subgroups |
| **Terminology** | Confounder | Effect modifier |

### Example: Exercise and Heart Disease
```
Exercise → Heart Disease
↑
Sex (Effect Modifier)
```

- In men: Exercise reduces heart disease risk by 30%
- In women: Exercise reduces heart disease risk by 50%
- Overall: Exercise reduces heart disease risk by 40%

### Types of Interaction

#### 1. Quantitative Interaction
- **Definition**: Direction of association same, but magnitude differs
- **Example**: Drug effect stronger in younger patients

#### 2. Qualitative Interaction
- **Definition**: Direction of association differs between subgroups
- **Example**: Treatment beneficial in men but harmful in women

### Testing for Interaction

#### 1. Stratified Analysis
- Calculate effect estimates in each stratum
- Compare estimates across strata
- Look for statistical significance of interaction term

#### 2. Statistical Tests
- **Interaction term** in regression models
- **Likelihood ratio test**: Compare models with/without interaction
- **Wald test**: Test significance of interaction coefficient

#### 3. Graphical Methods
- **Effect plots**: Show how association changes across levels of modifier
- **Interaction plots**: Lines that cross or diverge indicate interaction

## Confounding vs. Interaction: Decision Framework

### Is the third variable a confounder or effect modifier?

1. **Biological plausibility**: Does it make sense that the variable modifies the effect?
2. **Consistency**: Is the pattern seen in other studies?
3. **Statistical evidence**: Is there significant interaction?
4. **Clinical importance**: Does it change clinical decisions?

### Example: Age in a Drug Study
- **Confounding**: Age associated with both drug use and outcome
- **Effect modification**: Drug works differently in young vs. old patients

## Advanced Topics

### 1. Confounding by Indication
- **Definition**: Treatment appears harmful because sicker patients receive it
- **Example**: Drug appears to cause worse outcomes because given to severe cases
- **Control**: Instrumental variable analysis, propensity scores

### 2. Residual Confounding
- **Definition**: Confounding not fully controlled due to measurement error
- **Example**: Age categorized as 20-40, 41-60, but true effect varies within categories
- **Prevention**: Better measurement, more categories

### 3. Over-adjustment
- **Definition**: Controlling for variables in the causal pathway
- **Example**: Controlling for intermediate variables weakens true associations
- **Prevention**: Careful consideration of causal diagrams

### 4. Collider Bias
- **Definition**: Conditioning on a collider creates spurious associations
- **Example**: Studying factors associated with hospital admission creates associations between unrelated conditions

## Practical Applications

### 1. Causal Diagrams (DAGs)
- **Directed Acyclic Graphs**: Visual representation of causal relationships
- **Purpose**: Identify confounders, mediators, colliders
- **Use**: Guide analysis and control strategies

### 2. Propensity Scores
- **Definition**: Probability of exposure given covariates
- **Methods**: Logistic regression to estimate propensity
- **Uses**: Matching, stratification, weighting
- **Advantages**: Control many confounders simultaneously

### 3. Instrumental Variable Analysis
- **Definition**: Use instrumental variables to estimate causal effects
- **Requirements**: Instrument associated with exposure, affects outcome only through exposure
- **Example**: Physician preference as instrument for treatment choice

## Summary

Confounding and interaction are critical concepts in epidemiology. Confounding distorts associations and must be controlled, while effect modification reveals important heterogeneity in effects that should be explored. Understanding these concepts is essential for valid epidemiological research and appropriate interpretation of study results.
