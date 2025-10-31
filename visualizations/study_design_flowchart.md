# Study Design Selection Flowchart

## ASCII Art Flowchart

```
START: Research Question
        |
        v
   Can experiment?
   ethically/feasible?
        |
        +------------------+ No
        |                  |
       Yes                 v
        |          OBSERVATIONAL STUDIES
        |                  |
        v                  v
   EXPERIMENTAL       Outcome frequency?
   (RCT)              (Rare/Common)
        |                  |
        |              Rare|Common
        |                  |
        |              v   v
        |        CASE-CONTROL   |
        |              |        |
        |              |   CROSS-SECTIONAL
        |              |        |
        |              v        |
        |        Exposure?       |
        |        frequency       |
        |        (Rare/Common)   |
        |              |        |
        |          Rare|Common   |
        |              |        |
        |              v        |
        |            COHORT     |
        |              |        |
        |              |        |
        +--------------+--------+
                       |
                       v
                 END: Chosen Design
```

## Detailed Flowchart Description

### Step 1: Research Question
- Begin with a clear, focused research question
- Consider PICO format (Population, Intervention/Exposure, Comparison, Outcome)

### Step 2: Ethical Feasibility
**Can you ethically and practically manipulate the exposure?**
- **YES → Experimental Study (RCT)**
  - Gold standard for establishing causality
  - Requires ethical approval, equipoise
  - Best for interventions, treatments, prevention strategies

- **NO → Observational Study**
  - Cannot manipulate exposure
  - Natural exposures, retrospective designs
  - Proceed to outcome frequency assessment

### Step 3: Outcome Frequency (for Observational Studies)
**How common is the outcome of interest?**

#### Rare Outcome
- **→ Case-Control Study**
  - Efficient for rare diseases
  - Starts with outcome, looks backward
  - Good for studying multiple exposures
  - Examples: Cancer, congenital malformations

#### Common Outcome
- **→ Assess Exposure Frequency**
  - How common is the exposure?

  **Rare Exposure → Cohort Study**
  - Follow exposed and unexposed forward
  - Can establish temporality
  - Good for studying multiple outcomes
  - Examples: Occupational exposures, rare drugs

  **Common Exposure → Cross-Sectional Study**
  - Snapshot of population at one time
  - Quick and inexpensive
  - Cannot establish causality
  - Good for prevalence studies

## Alternative Decision Framework

### By Research Objective

```
What is your primary objective?

CAUSALITY PROOF          RISK FACTOR IDENTIFICATION     PREVALENCE ESTIMATION
     |                              |                              |
     v                              v                              v
   EXPERIMENTAL                   COHORT                        CROSS-SECTIONAL
   (RCT)                        STUDY                           STUDY

HYPOTHESIS TESTING     MULTIPLE EXPOSURE STUDY     QUICK ASSESSMENT
     |                              |                              |
     v                              v                              v
  CASE-CONTROL                   CASE-CONTROL                 CROSS-SECTIONAL
   STUDY                          STUDY                          STUDY
```

### By Resource Availability

```
High Resources + Ethics OK     Moderate Resources          Limited Resources
     |                              |                              |
     v                              v                              v
   RCT/COHORT                     CASE-CONTROL                 CROSS-SECTIONAL
                                  STUDY                          STUDY

Long Timeline                   Medium Timeline               Short Timeline
     |                              |                              |
     v                              v                              v
   COHORT/CASE-CONTROL            CASE-CONTROL                 CROSS-SECTIONAL
   (prospective)                   STUDY                          STUDY
```

## Study Design Comparison Matrix

| Design | Temporality | Causality | Cost | Time | Rare Outcome | Rare Exposure |
|--------|-------------|-----------|------|------|--------------|---------------|
| RCT    | ✓✓✓        | ✓✓✓      | $$$  | $$$  | ✓            | ✓             |
| Cohort | ✓✓✓        | ✓✓       | $$$  | $$$  | ✗            | ✓✓✓           |
| Case-Control | ✓✓     | ✓        | $$   | $$   | ✓✓✓          | ✗             |
| Cross-Sectional | ✗   | ✗       | $    | $    | ✓            | ✓             |

**Legend:**
- ✓✓✓ = Excellent
- ✓✓ = Good
- ✓ = Fair
- ✗ = Poor/Limited
- $ = Low cost/time
- $$$ = High cost/time

## Implementation Tips

### For Flowchart Use:
1. **Start with PICO question** - Ensure question is clear
2. **Consider ethics first** - Can you experiment?
3. **Assess frequency** - Rare outcomes → case-control
4. **Check resources** - Match design to available resources
5. **Validate choice** - Does design answer your question?

### Common Mistakes:
- Choosing RCT when observational design suffices
- Using cross-sectional when temporality matters
- Ignoring resource constraints
- Not considering outcome/exposure frequency

### Validation Questions:
- Does this design establish temporality?
- Can it provide incidence rates?
- Is it feasible with available resources?
- Will results be generalizable?

This flowchart provides a systematic approach to study design selection, ensuring the chosen design matches the research question, resources, and objectives.
