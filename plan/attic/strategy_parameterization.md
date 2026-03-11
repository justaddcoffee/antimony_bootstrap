# Parameterization Strategy for Alzheimer's Disease ODE Model

## Overview

This document covers strategies for parameterizing compartmental ODE models of Alzheimer's disease (AD), with specific focus on the antimony_bootstrap workflow and the Elbert/Esguerra reference model. The goal is to assign biologically justified kinetic parameter values to every reaction in the model, with documented sources, units, and confidence levels.

---

## 1. Extracting Kinetic Parameters from Literature

### Types of Parameters Commonly Needed

| Parameter Type | Symbol | Typical Context |
|---|---|---|
| Production rate | k_prod | Constitutive synthesis of Abeta, tau, cytokines |
| Degradation rate | k_deg | Enzymatic clearance (neprilysin, IDE), autophagy |
| Michaelis constant | Km | Enzyme-substrate (BACE1 cleaving APP, gamma-secretase) |
| Inhibition constant | Ki, IC50 | Drug effects, feedback inhibition |
| Half-life | t1/2 | Species turnover (convert to k_deg = ln(2)/t1/2) |
| Binding/dissociation | kon, koff, Kd | Antibody-Abeta binding, receptor-ligand |
| Transport rate | k_trans | ISF-to-CSF clearance, BBB transport, glymphatic flow |
| Aggregation rate | k_agg | Abeta monomer-to-oligomer-to-fibril nucleation/elongation |
| Hill coefficient | n | Cooperative binding, threshold responses |

### Extraction Workflow

1. **Identify the reaction** -- What biological process does this parameter govern?
2. **Search PubMed** with structured queries:
   - `"amyloid beta" AND "rate constant" AND "kinetic"`
   - `"tau phosphorylation" AND "Km" OR "kcat"`
   - `"neprilysin" AND "half-life" AND "amyloid"`
3. **Check review/meta-analysis papers first** -- These aggregate multiple measurements:
   - Bhatt et al. (2021) -- Systems pharmacology models of AD
   - Kyrtsos & Bhatt (2015) -- Abeta transport kinetics
   - Pallitto & Murphy (2001) -- Abeta aggregation kinetics
4. **Extract from figures if needed** -- Use WebPlotDigitizer for time-course data, then fit first-order kinetics to estimate rate constants
5. **Record PMID, table/figure number, exact conditions** (temperature, pH, concentration range, cell type)

### Key Reference Papers for AD Parameters

| Process | Key References |
|---|---|
| APP processing / Abeta production | Bhatt et al. 2021 (PMID: 34225390), Bhatt & Bhatt 2024 |
| Abeta clearance mechanisms | Elbert et al. 2022 (Elbert_Esguerra model), Tarasoff-Conway 2015 |
| Abeta aggregation kinetics | Pallitto & Murphy 2001, Cohen et al. 2013, Meisl et al. 2014 |
| Tau kinetics | Yamada 2017, Sato et al. 2018 (SILK studies) |
| Neuroinflammation | Bhatt et al. 2021, Heneka et al. 2015 |
| BBB transport | Storck et al. 2016, Roberts et al. 2014, Deane et al. 2009 |
| Glymphatic clearance | Iliff et al. 2012, Nedergaard 2013 |

### The Elbert/Esguerra Model as Primary Source

The reference model (`../Elbert_Esguerra_model_v2026b/`) is the single best source:
- Already has ~800 reactions fully parameterized
- Parameters are curated from literature with clinical relevance
- Naming conventions (species_Compartment) match our target
- **Strategy**: Extract parameters directly from the Elbert model first, then supplement with literature for any mechanisms not covered

---

## 2. Unit Conversions Across Experimental Systems

### The Core Challenge

Published parameters come in wildly different unit systems:
- **In vitro**: nM, uM, min^-1, sec^-1
- **In vivo rodent**: ng/mL, pg/mg tissue, hr^-1
- **Clinical/CSF**: pg/mL, ng/L, day^-1
- **PET imaging**: SUVr (dimensionless), Centiloid

### Standard Unit System for the Model

Adopt a consistent internal unit system (following Elbert convention):

| Quantity | Model Unit | Notes |
|---|---|---|
| Concentration | nmol/L (nM) | For species in fluid compartments |
| Amount | nmol | For species in tissue compartments |
| Volume | L | Compartment volumes |
| Time | hour (hr) | All rate constants in hr^-1 |
| Mass | nmol preferred | Convert from ng using MW |

### Common Conversions

```
# Concentration
1 pg/mL Abeta42 ~ 0.222 pM  (MW Abeta42 ~ 4514 Da)
1 ng/mL Abeta42 ~ 0.222 nM

# Time
k (min^-1) -> k * 60 = k (hr^-1)
k (sec^-1) -> k * 3600 = k (hr^-1)
k (day^-1) -> k / 24 = k (hr^-1)
t1/2 (hours) -> k_deg = ln(2) / t1/2  (hr^-1)

# Enzyme kinetics
Vmax (nmol/min/mg protein) -> need to scale by:
  - mg protein in compartment
  - convert min to hr
  - compartment volume (to get concentration rate)

# Binding
Kd (nM) = koff / kon
kon typically 10^4 -- 10^6 M^-1 s^-1 for protein-protein
```

### Compartment Volume Estimates (Human Brain)

| Compartment | Volume (L) | Source |
|---|---|---|
| Brain ISF | ~0.2 -- 0.3 | Elbert model, Bhatt 2021 |
| Brain parenchyma | ~1.0 -- 1.4 | Estimated total brain ~1.4 L |
| CSF (total) | ~0.14 | Standard physiology |
| Plasma | ~3.0 | Standard physiology |
| Perivasculature | ~0.01 -- 0.05 | Estimated |

### Tips

- Always document the conversion chain in the parameter's `source` field
- If a paper reports a range, use the geometric mean (not arithmetic) for rate constants
- When combining in vitro Km with in vivo Vmax, verify the assay conditions (pH 7.4, 37C)

---

## 3. Mouse vs. Human Parameter Translation

### Why This Matters

Many AD kinetic parameters come from transgenic mouse models (APP/PS1, 5xFAD, 3xTg, Tg2576). These need careful translation to human physiology.

### Allometric Scaling Principles

For pharmacokinetic parameters, allometric scaling relates body weight to clearance:

```
CL_human = CL_mouse * (BW_human / BW_mouse)^0.75
t1/2_human = t1/2_mouse * (BW_human / BW_mouse)^0.25
```

Typical values:
- Mouse BW: 0.025 kg
- Human BW: 70 kg
- Scaling factor for clearance: (70/0.025)^0.75 ~ 640
- Scaling factor for half-life: (70/0.025)^0.25 ~ 7.6

### Brain-Specific Scaling

Brain scaling does NOT follow simple allometry well. Use:

| Parameter | Mouse | Human | Ratio |
|---|---|---|---|
| Brain weight | ~0.4 g | ~1400 g | 3500x |
| Brain ISF turnover | ~4.5 hr | ~6-8 hr | 1.3-1.8x |
| CSF production rate | ~0.35 uL/min | ~350 uL/min | 1000x |
| Abeta half-life in ISF | ~1-2 hr | ~6-8 hr | 3-6x |

### Translation Heuristics

1. **Enzyme intrinsic rates (kcat, Km)**: Generally conserved across species for orthologous enzymes. Use mouse values directly but verify protein sequence homology.

2. **Clearance rates**: Scale allometrically. Abeta CSF clearance in humans is ~3-6x slower than mouse (Bateman et al. 2006 SILK data gives human Abeta42 t1/2 ~ 8-9 hr).

3. **Transport rates (BBB)**: Scale by BBB surface area and permeability. Human BBB SA is ~12-18 m^2 vs mouse ~1-2 cm^2. Use human PET/CSF data when available.

4. **Production rates**: Use human SILK data (Bateman lab) -- Abeta fractional production rate ~7.6%/hr, tau ~2.7%/hr.

5. **Aggregation kinetics**: Use in vitro values directly (these are intrinsic chemical properties), but adjust for in vivo chaperone effects (typically 10-100x slower in vivo).

### Preferred Hierarchy for Parameter Sources

1. **Human clinical data** (SILK, PET, CSF biomarkers) -- highest confidence
2. **Human in vitro** (iPSC neurons, human enzyme assays)
3. **Primate in vivo** (NHP studies)
4. **Mouse in vivo** with allometric scaling
5. **Mouse in vitro** / cell line data
6. **Computational estimation** (lowest confidence)

---

## 4. Estimating Parameters from Qualitative Data

### When You Only Have Directional Information

Many literature sources say "X increases Y" or "knockout of Z reduces clearance by ~50%" without providing rate constants. Strategies:

### Approach 1: Steady-State Constraint

If you know the steady-state concentration of a species:
```
At steady state: d[X]/dt = 0
k_prod = k_deg * [X]_ss

If [Abeta42]_ss ~ 10 nM in ISF and t1/2 ~ 8 hr:
k_deg = ln(2)/8 = 0.0866 hr^-1
k_prod = 0.0866 * 10 = 0.866 nM/hr
```

### Approach 2: Fold-Change Constraints

If a paper reports "30% reduction in Abeta upon drug treatment":
```
[Abeta]_treated / [Abeta]_baseline = 0.7
For simple production/degradation:
k_prod_new / k_deg = 0.7 * k_prod_old / k_deg
-> k_prod_new = 0.7 * k_prod_old
```

### Approach 3: Time-Course Fitting

If a paper shows a time-course figure (even without extracted data):
1. Digitize the curve (WebPlotDigitizer)
2. Fit to the ODE model's analytical solution
3. Extract apparent rate constants

### Approach 4: Order-of-Magnitude Estimation

Use biological priors:

| Process | Typical Rate Range |
|---|---|
| Protein synthesis | 0.01 -- 1 nM/hr |
| Protein degradation (t1/2) | 1 -- 100 hr |
| Enzyme catalysis (kcat) | 0.1 -- 1000 s^-1 |
| Receptor binding (kon) | 10^4 -- 10^7 M^-1 s^-1 |
| Diffusion-limited (kon) | ~10^9 M^-1 s^-1 |
| Transport across BBB | 10^-4 -- 10^-2 hr^-1 |

### Approach 5: Borrow from Analogous Systems

If no data exists for a specific AD reaction:
1. Find the same reaction type in another disease model
2. Find a homologous protein with known kinetics
3. Use the Elbert model's value for a similar reaction class

### Approach 6: Parameter Identifiability Analysis

Before spending effort estimating a parameter:
1. Check if the model output is sensitive to it (see Section 5)
2. If not sensitive, use a reasonable estimate and flag as "assumed"
3. Focus estimation effort on sensitive parameters

---

## 5. Parameter Sensitivity Analysis Approaches

### Local Sensitivity Analysis

Vary one parameter at a time by +/-10% and measure output change:

```python
import tellurium as te
import numpy as np

def local_sensitivity(model, param_name, output_species, perturbation=0.1):
    \"\"\"One-at-a-time sensitivity.\"\"\"
    r = te.loada(model)

    # Baseline
    r.simulate(0, 1000, 100)  # Run to steady state
    baseline = r[output_species]

    # Perturbed
    r.reset()
    original = getattr(r, param_name)
    setattr(r, param_name, original * (1 + perturbation))
    r.simulate(0, 1000, 100)
    perturbed = r[output_species]

    # Normalized sensitivity coefficient
    S = ((perturbed - baseline) / baseline) / perturbation
    return S
```

### Global Sensitivity Analysis (Morris Method)

Better for nonlinear models with parameter interactions:

```python
from SALib.sample import morris as morris_sample
from SALib.analyze import morris as morris_analyze

problem = {
    'num_vars': N_params,
    'names': param_names,
    'bounds': [[lo, hi] for lo, hi in param_bounds]
}

param_values = morris_sample.sample(problem, N=1000)
# Run model for each sample, collect outputs
# Analyze with morris_analyze.analyze()
```

### Sobol Sensitivity Analysis

For variance decomposition (which parameters explain output variance):
- First-order indices (Si): direct effect of parameter i
- Total-order indices (STi): including interactions
- Use SALib library with Saltelli sampling

### Practical Workflow for AD Models

1. **Screen with local sensitivity** -- fast, identifies obviously insensitive parameters
2. **Rank parameters** by |S| -- top 20% are "critical"
3. **Run Morris method** on critical parameters -- assess nonlinearity and interactions
4. **Sobol analysis** on the top 10 most sensitive parameters -- quantify variance contributions
5. **Focus parameterization effort** on high-sensitivity parameters

### Key Outputs of Interest for AD

| Output | Clinical Relevance |
|---|---|
| [Abeta42]_CSF | CSF biomarker (A- vs A+) |
| [pTau181]_CSF | CSF biomarker |
| [Abeta_plaque]_Brain | Amyloid PET (Centiloid) |
| [NFT]_Brain | Tau PET (SUVr) |
| [Neuron_count] | Neurodegeneration / atrophy |
| [MMSE_proxy] | Cognitive score approximation |

---

## 6. Assigning Confidence Levels

### Three-Tier Confidence System

Following the antimony_bootstrap schema (ParameterSpec.confidence):

#### **measured** -- Direct experimental measurement
- Value comes from a specific experiment with error bars
- Conditions match the model context (human, relevant tissue, physiological conditions)
- Has a PMID and specific table/figure reference
- Example: "Abeta42 fractional turnover rate = 7.6%/hr from SILK study (Bateman et al. 2006, PMID: 16418406)"

#### **estimated** -- Derived or scaled from data
- Calculated from related measurements (e.g., t1/2 to k_deg)
- Allometrically scaled from mouse data
- Fit to a time-course or dose-response
- Extracted from a published computational model
- Steady-state constrained
- Example: "k_deg_Abeta_ISF = 0.087 hr^-1, estimated from human SILK t1/2 = 8 hr"

#### **assumed** -- No direct data available
- Order-of-magnitude estimate based on biological priors
- Borrowed from analogous reaction/protein
- Placeholder value to be refined later
- Set to make model produce reasonable steady states
- Example: "k_transport_perivasc = 0.01 hr^-1, assumed based on typical perivascular drainage rates"

### Confidence Assignment Checklist

```
[ ] Is the value from a human study?                    -> +measured
[ ] Is it from in vitro with human enzyme/cells?        -> +measured (if direct) or +estimated
[ ] Is it from mouse, allometrically scaled?            -> estimated
[ ] Is it calculated from a different measured quantity? -> estimated
[ ] Is it from another computational model?             -> estimated
[ ] Is it an order-of-magnitude guess?                  -> assumed
[ ] Is it tuned to match a known steady state?          -> estimated (if target is measured)
                                                           -> assumed (if target is also estimated)
```

### Documentation Requirements by Confidence Level

| Level | Required Fields |
|---|---|
| measured | PMID, specific table/figure, experimental conditions, error range |
| estimated | PMID of source data, derivation method, assumptions made |
| assumed | Rationale, range of plausible values, sensitivity ranking |

---

## 7. Common Parameter Ranges for AD Reactions

### Abeta Production & Processing

| Parameter | Value | Units | Source | Confidence |
|---|---|---|---|---|
| APP production rate | 0.1 -- 1.0 | nM/hr | Bhatt 2021 | estimated |
| BACE1 kcat | 0.2 -- 2.0 | s^-1 | Bhatt 2021, Turner 2001 | measured |
| BACE1 Km for APP | 1 -- 10 | uM | Various in vitro | measured |
| gamma-secretase kcat | 0.01 -- 0.1 | s^-1 | Bhatt 2021 | measured |
| gamma-secretase Km | 0.1 -- 1.0 | uM | Bhatt 2021 | measured |
| Abeta42/Abeta40 ratio | 0.05 -- 0.15 | dimensionless | Clinical data | measured |
| Abeta fractional production | 7.6 +/- 1.0 | %/hr | Bateman 2006 SILK | measured |

### Abeta Degradation & Clearance

| Parameter | Value | Units | Source | Confidence |
|---|---|---|---|---|
| Neprilysin Km for Abeta | 2 -- 20 | uM | Iwata 2001, Shirotani 2001 | measured |
| Neprilysin kcat for Abeta | 0.5 -- 5 | s^-1 | Various | measured |
| IDE Km for Abeta | 0.1 -- 2 | uM | Various | measured |
| Abeta ISF half-life (human) | 6 -- 10 | hr | Bateman 2006 SILK | measured |
| Abeta ISF-to-CSF clearance | 0.05 -- 0.2 | hr^-1 | Elbert model, estimated | estimated |
| Abeta BBB efflux (LRP1) | 0.01 -- 0.1 | hr^-1 | Deane 2009 | estimated |
| Abeta glymphatic clearance | 0.005 -- 0.05 | hr^-1 | Iliff 2012 | estimated |
| Abeta CSF half-life | 4 -- 8 | hr | Bateman 2006 | measured |

### Abeta Aggregation

| Parameter | Value | Units | Source | Confidence |
|---|---|---|---|---|
| Nucleation rate (kn) | 10^-4 -- 10^-2 | M^-1 hr^-1 | Cohen 2013, Meisl 2014 | measured (in vitro) |
| Elongation rate (k+) | 10^4 -- 10^6 | M^-1 hr^-1 | Cohen 2013 | measured (in vitro) |
| Secondary nucleation (k2) | 10^1 -- 10^4 | M^-2 hr^-1 | Meisl 2014 | measured (in vitro) |
| Oligomer-to-fibril conversion | 0.01 -- 1 | hr^-1 | Estimated | assumed |
| In vivo correction factor | 0.01 -- 0.1 | dimensionless | Chaperone effects | assumed |

### Tau Kinetics

| Parameter | Value | Units | Source | Confidence |
|---|---|---|---|---|
| Tau fractional production | 2.7 +/- 0.4 | %/hr | Sato 2018 SILK | measured |
| Tau ISF half-life | 20 -- 30 | hr | Sato 2018 SILK | measured |
| Tau phosphorylation rate | 0.01 -- 0.1 | hr^-1 | Estimated from models | estimated |
| pTau dephosphorylation | 0.005 -- 0.05 | hr^-1 | Estimated | estimated |
| Tau aggregation (seeded) | 0.001 -- 0.01 | hr^-1 | Estimated from tauopathy | assumed |
| Tau spread rate (connectome) | 0.0001 -- 0.001 | hr^-1 | Estimated from PET staging | assumed |

### Neuroinflammation

| Parameter | Value | Units | Source | Confidence |
|---|---|---|---|---|
| Microglia activation rate | 0.01 -- 0.5 | hr^-1 | Various models | estimated |
| Microglia deactivation | 0.001 -- 0.05 | hr^-1 | Various models | estimated |
| TNFa production (activated) | 0.1 -- 10 | pM/hr | Cell culture | estimated |
| TNFa half-life | 0.3 -- 1 | hr | Bhatt 2021 | measured |
| IL-1b production | 0.1 -- 5 | pM/hr | Cell culture | estimated |
| IL-6 half-life | 1 -- 6 | hr | PK data | measured |
| Complement activation rate | 0.01 -- 0.1 | hr^-1 | Estimated | assumed |

### Synaptic / Neuronal Dynamics

| Parameter | Value | Units | Source | Confidence |
|---|---|---|---|---|
| Neuronal death rate (baseline) | 10^-6 -- 10^-5 | hr^-1 | Very slow in normal aging | estimated |
| Neuronal death rate (AD) | 10^-4 -- 10^-3 | hr^-1 | Accelerated ~10-100x | estimated |
| Synapse turnover | 0.001 -- 0.01 | hr^-1 | Bhatt 2021 | estimated |
| LTP threshold shift | varies | -- | Functional, not kinetic | assumed |

### Transport & Binding

| Parameter | Value | Units | Source | Confidence |
|---|---|---|---|---|
| Typical protein kon | 10^4 -- 10^6 | M^-1 s^-1 | General biochemistry | measured |
| Typical protein koff | 10^-4 -- 10^-1 | s^-1 | General biochemistry | measured |
| RAGE-Abeta Kd | 50 -- 200 | nM | Deane 2003 | measured |
| LRP1-Abeta Kd | 1 -- 20 | nM | Deane 2004 | measured |
| ApoE-Abeta Kd | 10 -- 100 | nM | Varies by isoform | measured |

---

## Practical Parameterization Workflow

### Step-by-Step for Each Module

1. **List all parameters** needed for the module's reactions
2. **Check Elbert model first** -- extract matching parameters with proper units
3. **Search literature** for any remaining parameters, using PubMed structured queries
4. **Apply unit conversions** to the model's standard system (nM, hr, L)
5. **Scale mouse-to-human** if needed, using allometric or SILK-based corrections
6. **Estimate missing parameters** using steady-state constraints and fold-change data
7. **Assign confidence levels** (measured/estimated/assumed)
8. **Run sensitivity analysis** -- if an "assumed" parameter is highly sensitive, prioritize finding better data
9. **Document everything** -- PMID, derivation, assumptions in the ParameterSpec source field
10. **Validate** -- simulate and check that steady-state concentrations are physiologically reasonable

### Physiological Steady-State Sanity Checks

| Species | Expected Steady State | Source |
|---|---|---|
| Abeta42 in ISF | 5 -- 15 nM | CSF data, corrected for ISF |
| Abeta42 in CSF | 0.5 -- 2 nM (~500 -- 1000 pg/mL) | Clinical cutoff ~600 pg/mL |
| Abeta42 in plasma | 0.02 -- 0.1 nM | Plasma assays |
| Total tau in CSF | 0.5 -- 2 nM (~200 -- 400 pg/mL) | Clinical reference |
| pTau181 in CSF | 0.05 -- 0.2 nM (~20 -- 40 pg/mL) | Clinical reference |
| TNFa in brain | 1 -- 50 pM | Cell culture + tissue data |

---

## Summary of Key Principles

1. **Elbert model first** -- It is the most complete parameterized AD model available
2. **Human data preferred** -- SILK studies are gold standard for turnover rates
3. **Document the chain** -- Every derived value should trace back to a primary measurement
4. **Use confidence tiers** -- Be honest about what is measured vs assumed
5. **Sensitivity-driven prioritization** -- Spend effort on parameters that matter
6. **Steady-state validation** -- Final check that parameters produce physiological concentrations
7. **Iterate** -- Parameterization is not one-pass; expect to revise as modules are assembled
