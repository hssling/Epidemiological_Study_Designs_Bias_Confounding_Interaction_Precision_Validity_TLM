# Confounding and Interaction Diagrams

## 1. Confounding Illustration

### ASCII Art: Confounding Triangle

```
EXPOSURE (E) ──────────────► OUTCOME (O)
     ^                             ^
     |                             |
     |                             |
     └───────── CONFOUNDER (C) ───┘

Legend:
E = Exposure (e.g., Smoking)
O = Outcome (e.g., Lung Cancer)
C = Confounder (e.g., Age)

Path: E ← C → O (Confounding path)
     E → O (Direct path - if exists)
```

### Detailed Confounding Diagram

```
[Age] ──────────────► [Smoking] ──────────────► [Lung Cancer]
   ↑                        ↑                        ↑
   │                        │                        │
   │                        │                        │
   └────────────────────────┴────────────────────────┘
                BACKDOOR PATH (Confounding)
```

**Explanation:**
- Age affects both smoking behavior and lung cancer risk
- Crude association: Smoking appears strongly associated with lung cancer
- After controlling for age: Association weakens but remains significant
- Age is a confounder because it affects both exposure and outcome

## 2. Effect Modification (Interaction)

### ASCII Art: Interaction Diagram

```
EXPOSURE (E) ──────────────► OUTCOME (O)
     │                             │
     │                             │
     v                             v
MODIFIER (M)                  MODIFIER (M)

For M = Young:    E ── Strong ──► O
For M = Old:      E ── Weak ────► O

Legend:
E = Exposure
O = Outcome
M = Effect Modifier (e.g., Age)
```

### Stratified Interaction Plot

```
Effect Size by Age Group
═══════════════════════════

High Exposure    ████████████████  RR = 3.0
Low Exposure     ███████           RR = 1.5
                 └─────────────────┘
                 Young Age

High Exposure    ████████████████  RR = 2.0
Low Exposure     ███████████       RR = 1.3
                 └─────────────────┘
                 Old Age

Key: █ = Effect Size
     Interaction present (different slopes)
```

## 3. Bias Types Classification

### ASCII Art: Bias Classification Tree

```
BIAS
├── Selection Bias
│   ├── Sampling Bias
│   ├── Berkson's Bias
│   ├── Healthy Worker Effect
│   ├── Self-Selection Bias
│   └── Loss to Follow-up Bias
│
├── Information Bias
│   ├── Recall Bias
│   ├── Observer Bias
│   ├── Interviewer Bias
│   └── Misclassification Bias
│       ├── Non-differential
│       └── Differential
│
└── Confounding Bias
    ├── Positive Confounding
    └── Negative Confounding
```

### Bias Impact Diagram

```
BIAS DIRECTION
═══════════════

Non-Differential Misclassification
         ↓
    Biases toward null
    (Underestimates association)

Differential Misclassification
         ↓
    Can bias in either direction
    (Over/underestimates association)

Selection Bias
         ↓
    Usually biases toward null
    (Underestimates association)

Confounding
         ↓
    Can bias in either direction
    depending on confounder-outcome association
```

## 4. Directed Acyclic Graph (DAG) Examples

### Simple Confounding DAG

```
A ──► X ──► Y
│         ▲
└─────────┘
    Confounder A
```

**Legend:**
- X = Exposure
- Y = Outcome
- A = Confounder
- Arrows show causal relationships

### Collider Bias DAG

```
X ──► C ◄── Y
      │
      ▼
   Selection
   on C
```

**Explanation:**
- X and Y are independent
- C is a collider (common effect)
- Conditioning on C creates spurious association between X and Y

### Mediation DAG

```
X ──► M ──► Y
│         ▲
└─────────┘
   Direct effect
```

**Legend:**
- X = Exposure
- M = Mediator
- Y = Outcome
- Total effect = Direct + Indirect (through M)

## 5. Study Design Comparison Matrix

### Visual Matrix

```
STUDY DESIGNS COMPARISON
══════════════════════════

Features →     RCT    Cohort    Case-Control    Cross-Sectional
              ──────  ────────  ─────────────  ────────────────

Temporality    ✓✓✓      ✓✓✓         ✓✓              ✗
Causality      ✓✓✓      ✓✓          ✓               ✗
Cost          $$$$     $$$        $$              $
Time          $$$$     $$$        $$              $
Rare Outcome   ✓        ✗          ✓✓✓            ✓
Rare Exposure  ✓        ✓✓✓        ✗              ✓
Confounding    ✓✓✓      ✓✓          ✓              ✗
Generalizable  ✓        ✓           ✓              ✓✓

Legend:
✓✓✓ Excellent    ✓✓ Good    ✓ Fair    ✗ Poor
$ Low $$$$ High
```

## 6. Bradford Hill Criteria Wheel

### ASCII Art: Hill Criteria

```
                   STRENGTH
                ↗          ↖
         CONSISTENCY      SPECIFICITY
        ↗        ↑        ↖
   PLAUSIBILITY ←─┼─→ TEMPORALITY
        ↘        ↓        ↗
         COHERENCE     BIOLOGICAL
                ↘          ↖
                 GRADIENT
                     ↕
                EXPERIMENT
                     ↕
                  ANALOGY
```

### Criteria Explanation Wheel

```
STRENGTH: Large effect size
CONSISTENCY: Replicated findings
SPECIFICITY: Exposure causes specific outcome
TEMPORALITY: Exposure precedes outcome
BIOLOGICAL GRADIENT: Dose-response relationship
PLAUSIBILITY: Biologically credible
COHERENCE: Fits existing knowledge
EXPERIMENT: Experimental evidence
ANALOGY: Similar to known relationships
```

## 7. PICO Framework Diagram

### ASCII Art: PICO Structure

```
PICO FRAMEWORK
═══════════════

┌─────────────────────────────────────┐
│ P = POPULATION                      │
│ Who is the study about?             │
│ - Age, sex, condition, setting      │
└─────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ I = INTERVENTION/EXPOSURE          │
│ What is being studied?              │
│ - Treatment, exposure, risk factor  │
└─────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ C = COMPARISON                     │
│ What is the alternative?            │
│ - Placebo, standard treatment, none │
└─────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ O = OUTCOME                        │
│ What is the result?                 │
│ - Clinical, surrogate, patient-centered │
└─────────────────────────────────────┘
```

## 8. Critical Appraisal Framework

### CASP Framework Diagram

```
CRITICAL APPRAISAL (CASP)
══════════════════════════

┌─────────────────────────────────────┐
│ 1. Are the results valid?           │
│    - Study design appropriate?      │
│    - Bias minimized?                │
│    - Confounding controlled?        │
└─────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 2. What are the results?            │
│    - Main findings?                 │
│    - Precision measures?            │
│    - Clinical significance?         │
└─────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 3. Will the results help locally?   │
│    - Applicability to my setting?   │
│    - Patient population similar?    │
│    - Intervention feasible?         │
└─────────────────────────────────────┘
```

## 9. Sample Size Calculation Visual

### Power Curve Diagram

```
STATISTICAL POWER CURVE
════════════════════════

Power (%)
100 │                                      *
    │                                   *  *
    │                                *     *
    │                             *        *
    │                          *           *
    │                       *              *
    │                    *                 *
    │                 *                    *
    │              *                       *
    │           *                          *
    │        *                             *
    │     *                                *
 50 │  *                                   *
    │*                                     *
    └──────────────────────────────────────
     Small Effect          Medium Effect         Large Effect

     Effect Size

Legend: * = 80% Power line
        Different sample sizes shown
```

## Implementation Notes

### Creating Visual Diagrams:
1. **Use drawing tools**: PowerPoint, Google Slides, Draw.io
2. **Color coding**: Different colors for different concepts
3. **Arrows**: Show direction of relationships
4. **Labels**: Clear, concise text
5. **Legends**: Explain symbols and colors

### Teaching Applications:
- **Flowcharts**: Guide study design selection
- **DAGs**: Explain causal relationships
- **Matrices**: Compare study designs
- **Wheels**: Show criteria relationships
- **Plots**: Demonstrate statistical concepts

### Digital Tools for Creation:
- **Mermaid**: For flowcharts and diagrams
- **Graphviz**: For complex graphs
- **TikZ**: LaTeX diagrams
- **D3.js**: Interactive web visualizations
- **Tableau**: Data visualization

These visualization assets provide clear, memorable representations of complex epidemiological concepts, making them easier to understand and teach.
