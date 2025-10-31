# Study Design Quick Reference Guide

## Observational Study Designs

### Cohort Studies
**Definition**: Follow groups of people forward in time to see who develops the outcome

**Types**:
- **Prospective**: Exposure assessed before outcome occurs
- **Retrospective**: Use existing records to reconstruct cohorts

**Advantages**:
- Can establish temporality
- Multiple outcomes possible
- Incidence rates calculable

**Disadvantages**:
- Expensive and time-consuming
- Not suitable for rare outcomes
- Loss to follow-up

**Measures**: Relative Risk (RR), Attributable Risk (AR)

**Example**: Framingham Heart Study

### Case-Control Studies
**Definition**: Compare people with disease (cases) to people without disease (controls)

**Types**:
- Population-based
- Hospital-based
- Nested case-control

**Advantages**:
- Efficient for rare outcomes
- Quick and inexpensive
- Multiple exposures possible

**Disadvantages**:
- Cannot calculate incidence
- Prone to recall bias
- Selection bias possible

**Measures**: Odds Ratio (OR)

**Example**: Oral contraceptives and thrombosis

### Cross-Sectional Studies
**Definition**: Measure exposure and outcome at the same point in time

**Advantages**:
- Quick and inexpensive
- Good for prevalence
- Multiple variables

**Disadvantages**:
- Cannot establish causality
- Prevalence-incidence bias
- Survival bias

**Measures**: Prevalence Ratio (PR)

**Example**: National Health Survey

## Experimental Study Designs

### Randomized Controlled Trials (RCTs)
**Definition**: Participants randomly assigned to intervention or control groups

**Key Features**:
- Randomization
- Control group
- Blinding
- Intention-to-treat analysis

**Advantages**:
- Gold standard for causality
- Minimizes confounding
- High internal validity

**Disadvantages**:
- Expensive
- Ethical constraints
- May not be generalizable

**Example**: Drug trials

### Non-Randomized Trials
**Definition**: Participants assigned without randomization

**Methods**: Alternate allocation, physician choice

**Advantages**: Easier to implement

**Disadvantages**: Selection bias possible

### Cluster Randomized Trials
**Definition**: Groups (clusters) are randomized

**Examples**: Schools, clinics, communities

**Advantages**: Practical for community interventions

**Disadvantages**: Requires larger sample size

## Choosing a Study Design

### Decision Framework

| Scenario | Preferred Design |
|----------|------------------|
| Rare outcome, common exposure | Cohort study |
| Rare outcome, rare exposure | Case-control study |
| Common outcome, common exposure | Cross-sectional study |
| Experimental question | RCT (if feasible) |
| Quick assessment needed | Cross-sectional study |
| Multiple outcomes | Cohort study |
| Multiple exposures | Case-control study |

### Factors to Consider
1. **Research question**: What are you trying to answer?
2. **Frequency**: How common are exposure and outcome?
3. **Resources**: Time, money, personnel available
4. **Ethics**: Is experimentation possible?
5. **Feasibility**: Can the study be conducted?

## Bias and Validity

### Types of Bias
- **Selection bias**: Systematic differences in participant selection
- **Information bias**: Errors in measuring exposure or outcome
- **Confounding**: Mixing of effects from third variables

### Controlling Bias
- **Randomization**: Balances known and unknown factors
- **Matching**: Ensures comparability
- **Blinding**: Prevents observer bias
- **Standardization**: Consistent data collection

### Validity Types
- **Internal validity**: Study measures what it intends
- **External validity**: Results apply to other populations

## Measures of Association

### For Cohort Studies
- **Relative Risk (RR)** = Incidence_exposed / Incidence_unexposed
- **Attributable Risk (AR)** = Incidence_exposed - Incidence_unexposed
- **Attributable Fraction (AF)** = (RR-1)/RR × 100%

### For Case-Control Studies
- **Odds Ratio (OR)** = (Cases_exposed × Controls_unexposed) / (Cases_unexposed × Controls_exposed)
- When disease is rare: OR ≈ RR

### For Cross-Sectional Studies
- **Prevalence Ratio (PR)** = Prevalence_exposed / Prevalence_unexposed

## Critical Appraisal Checklist

### For Any Study
1. **Research question**: Clear and focused?
2. **Study population**: Defined and appropriate?
3. **Sample size**: Adequate power?
4. **Data collection**: Valid and reliable?
5. **Analysis**: Appropriate methods?
6. **Conclusions**: Supported by data?

### Study-Specific Questions
- **Cohort**: Complete follow-up? Exposure before outcome?
- **Case-control**: Appropriate controls? Recall bias addressed?
- **Cross-sectional**: Response rate? Temporality considered?
- **RCT**: Adequate randomization? Blinding maintained?

## Common Pitfalls

1. **Ecological fallacy**: Group-level associations ≠ individual-level
2. **Reverse causation**: Outcome causes exposure (in cross-sectional studies)
3. **Confounding**: Third variable explains association
4. **Selection bias**: Non-representative sample
5. **Information bias**: Measurement errors

## Key Terms

- **Incidence**: New cases in a time period
- **Prevalence**: Existing cases at a point in time
- **Cohort**: Group followed over time
- **Case**: Person with the outcome
- **Control**: Person without the outcome
- **Exposure**: Risk factor of interest
- **Outcome**: Health event of interest
- **Confounder**: Variable associated with both exposure and outcome

## Study Design Flowchart

```
Start with research question
        ↓
Is experimentation ethical/feasible?
        ↓
Yes → Experimental design (RCT)
        ↓
No → Observational design
        ↓
What is frequency of outcome?
        ↓
Rare → Case-control study
        ↓
Common → What is frequency of exposure?
        ↓
Rare → Cohort study
        ↓
Common → Cross-sectional study
```

## References
- Rothman KJ. Epidemiology: An Introduction. 2nd ed. Oxford University Press; 2012.
- Hennekens CH, Buring JE. Epidemiology in Medicine. Lippincott Williams & Wilkins; 1987.
