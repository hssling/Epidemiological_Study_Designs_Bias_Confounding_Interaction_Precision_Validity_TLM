# Exercise Set 2: Bias, Confounding, and Study Validity

## Exercise 2.1: Bias Scenarios

Identify the type of bias in each scenario and suggest how to minimize it:

1. A study of the relationship between coffee consumption and heart disease finds that coffee drinkers are more likely to accurately report their coffee intake than non-drinkers.

2. In a case-control study of breast cancer, cases are recruited from a specialized cancer hospital while controls come from the general population.

3. Participants in a weight loss intervention study who drop out tend to have poorer outcomes than those who complete the study.

4. Blood pressure measurements are taken by different nurses, with some nurses consistently recording higher readings than others.

5. A study of occupational exposure to chemicals uses employment records from 20 years ago, but some workers' exposure histories are incomplete.

## Exercise 2.2: Confounding Control

For each scenario, identify potential confounders and suggest control methods:

1. **Scenario**: A study finds that people who eat more fruits have lower rates of heart disease.
   - Potential confounders: Age, socioeconomic status, exercise habits
   - Control methods: Stratification by age, multivariate regression, matching

2. **Scenario**: Coffee drinkers have higher rates of pancreatic cancer.
   - Potential confounders: Smoking, alcohol consumption, diet
   - Control methods: Adjust for smoking in analysis, restrict to non-smokers

3. **Scenario**: People with higher education levels have better health outcomes.
   - Potential confounders: Income, occupation, access to healthcare
   - Control methods: Propensity score matching, instrumental variables

## Exercise 2.3: Effect Modification vs. Confounding

Determine whether each scenario represents confounding or effect modification:

1. The association between smoking and lung cancer is stronger in older adults than younger adults.

2. Age is associated with both physical activity levels and arthritis prevalence.

3. The effect of aspirin on heart attack prevention differs between men and women.

4. Socioeconomic status affects both access to healthy food and obesity rates.

5. The relationship between alcohol consumption and liver disease varies by genetic factors.

## Exercise 2.4: Study Validity Assessment

Evaluate the validity threats in this hypothetical study:

**Study**: Cross-sectional survey of 1,000 adults examining the relationship between smartphone use and sleep quality.

**Potential validity threats**:
- **Internal validity**: Reverse causation, confounding by age/technology adoption
- **External validity**: Limited to surveyed population, self-selection bias
- **Construct validity**: How well does self-reported sleep quality measure actual sleep?

**Improvement strategies**:
- Use objective sleep measures (actigraphy)
- Control for age, income, education
- Consider longitudinal design

## Exercise 2.5: Critical Appraisal Practice

Appraise this study summary:

**Study**: RCT comparing low-dose aspirin vs. placebo for prevention of cardiovascular events in 10,000 healthy adults aged 50-75, followed for 5 years.

**Key findings**: 12% reduction in cardiovascular events (RR = 0.88, 95% CI: 0.82-0.94)

**Appraisal questions**:
1. **Randomization**: Was allocation concealment adequate?
2. **Blinding**: Were participants and investigators blinded?
3. **Follow-up**: What was the dropout rate? Was it differential?
4. **Analysis**: Was intention-to-treat analysis used?
5. **Generalizability**: Can results apply to other populations?
6. **Clinical significance**: Is the 12% reduction meaningful?

## Exercise 2.6: Sample Size and Power

Calculate or estimate sample size considerations:

1. **Scenario**: Cohort study of rare exposure (5% prevalence) and common outcome
   - Required sample size: Large cohort needed
   - Power considerations: Need long follow-up for sufficient events

2. **Scenario**: Case-control study of rare outcome (10 cases per 100,000 per year)
   - Sample size: 500 cases + 500 controls often sufficient
   - Matching: Consider frequency matching on age/sex

3. **Scenario**: RCT with expected effect size of 20% reduction
   - Sample size formula: n = (Zα + Zβ)² × (p1(1-p1) + p2(1-p2)) / (p1-p2)²
   - Power: 80%, alpha: 0.05, baseline risk: 10%

## Answers and Explanations

### Exercise 2.1 Answers:
1. **Recall bias** - Differential reporting; use objective measures or blinded interviewers
2. **Berkson's bias** - Hospital controls not representative; use population-based controls
3. **Attrition bias** - Differential loss to follow-up; use intention-to-treat analysis
4. **Observer bias** - Inconsistent measurements; standardize protocols and training
5. **Misclassification bias** - Incomplete records; validate historical data, use multiple sources

### Exercise 2.2 Answers:
1. **Confounders**: Age (older people eat more fruits, have lower heart disease), SES (affects fruit consumption and healthcare access), exercise (correlated with fruit eating and heart health)
   - **Control**: Stratify by age groups, adjust for SES and exercise in regression

2. **Confounders**: Smoking (coffee drinkers more likely to smoke), alcohol (correlated with coffee), diet quality
   - **Control**: Restrict to never-smokers, adjust for alcohol and diet

3. **Confounders**: Income (education leads to higher income), occupation (education affects job type), healthcare access
   - **Control**: Use education as proxy for SES, instrumental variable analysis

### Exercise 2.3 Answers:
1. **Effect modification** - Age modifies the effect of smoking on lung cancer
2. **Confounding** - Age affects both physical activity and arthritis risk
3. **Effect modification** - Sex modifies aspirin's effect on heart attacks
4. **Confounding** - SES affects both food access and obesity
5. **Effect modification** - Genetics modify alcohol's effect on liver disease

### Exercise 2.4 Answers:
**Internal validity threats**:
- Reverse causation (poor sleepers may use smartphones more)
- Confounding (younger people use smartphones more and sleep differently)
- Information bias (self-reported sleep may be inaccurate)

**External validity threats**:
- Selection bias (only smartphone owners participated)
- Limited generalizability (specific population, time period)

**Improvements**:
- Objective measures (sleep trackers, medical records)
- Longitudinal design to establish temporality
- Representative sampling, high response rates

### Exercise 2.5 Answers:
**Strengths**:
- Large sample size, long follow-up
- Clear randomization and blinding
- Intention-to-treat analysis
- Precise effect estimate

**Limitations**:
- Healthy participant bias
- Adherence issues
- Generalizability to other age groups
- Cost-effectiveness not addressed

**Overall**: High-quality RCT with important clinical implications

### Exercise 2.6 Answers:
1. **Cohort study**: Need 10,000+ participants for sufficient power with rare exposure
2. **Case-control**: 500 cases provide good power for most associations
3. **RCT**: Approximately 1,000 participants per group (2,000 total) for 80% power
