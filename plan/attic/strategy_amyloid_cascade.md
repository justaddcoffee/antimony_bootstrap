# Strategy: Amyloid Cascade Mechanisms for Antimony ODE Models

**Date**: 2026-02-24

**Objective**: Extract amyloid cascade mechanisms from Alzheimer's literature and encode them as ODE-based Antimony modules compatible with the antimony_bootstrap schema (ModuleSpec YAML). This document covers APP processing, Abeta aggregation kinetics, plaque dynamics, clearance pathways, compartmental structure, rate law forms, and parameter ranges from published literature and the Elbert_Esguerra reference model.

---

## 1. Compartmental Structure

The amyloid cascade spans intracellular processing, extracellular aggregation, and multi-compartment transport. The following compartments are recommended, consistent with Elbert_Esguerra naming conventions:

| Compartment | Volume (L) | Notes |
|---|---|---|
| `Neuron` | 0.5 | Intracellular neuronal cytoplasm; site of APP processing |
| `Endosome` | 0.01 | Endosomal/lysosomal compartment; beta-secretase active at acidic pH |
| `BrainISF` | 0.25 | Brain interstitial fluid; primary site of Abeta monomer release and aggregation |
| `BrainParenchyma` | 1.0 | Brain parenchyma tissue; site of insoluble plaque deposition |
| `Perisynaptic` | 0.05 | Perisynaptic cleft; high local Abeta concentration relevant for oligomer toxicity |
| `CSF` | 0.14 | Cerebrospinal fluid; biomarker sampling compartment |
| `Plasma` | 3.0 | Blood plasma; peripheral clearance and biomarker |

**Rationale**: The Endosome compartment is critical because BACE1 activity is pH-dependent and concentrated in the endosomal pathway. BrainParenchyma separates soluble ISF species from insoluble plaque deposits. Perisynaptic is optional but important for modeling oligomer-mediated synaptic toxicity at high local concentrations.

For the initial module, a minimal 3-compartment model (BrainISF, CSF, Plasma) is sufficient, matching the existing `abeta_production.yaml`. Full modules should progressively add Neuron, Endosome, and BrainParenchyma.

---

## 2. APP Processing (Alpha, Beta, Gamma Secretase)

### 2.1 Biological Summary

Amyloid Precursor Protein (APP) is a type I transmembrane protein processed through two competing pathways:

- **Non-amyloidogenic pathway**: alpha-secretase (ADAM10/ADAM17) cleaves APP within the Abeta domain, producing soluble APPalpha (sAPPalpha) and C83 (alpha-CTF). Gamma-secretase subsequently cleaves C83 to produce p3 peptide (non-toxic).
- **Amyloidogenic pathway**: beta-secretase (BACE1) cleaves APP at the N-terminus of the Abeta domain, producing soluble APPbeta (sAPPbeta) and C99 (beta-CTF). Gamma-secretase cleaves C99 to produce Abeta peptides of varying lengths (Abeta38, Abeta40, Abeta42).

The ratio of alpha vs. beta cleavage determines how much Abeta is produced. In AD, the balance shifts toward beta-secretase processing.

### 2.2 Species (Elbert naming convention)

- `APP_Neuron` -- full-length APP at neuronal membrane
- `sAPPa_BrainISF` -- soluble APPalpha (non-amyloidogenic product)
- `sAPPb_BrainISF` -- soluble APPbeta
- `C83_Neuron` -- alpha-CTF (alpha-secretase C-terminal fragment)
- `C99_Neuron` -- beta-CTF (beta-secretase C-terminal fragment)
- `AB40_BrainISF` -- Abeta40 monomer released into ISF
- `AB42_BrainISF` -- Abeta42 monomer released into ISF
- `AB38_BrainISF` -- Abeta38 monomer (optional, minor species)
- `p3_BrainISF` -- p3 fragment (non-toxic, often omitted)
- `BACE1_Endosome` -- beta-secretase enzyme
- `ADAM10_Neuron` -- alpha-secretase enzyme

### 2.3 Reactions and Rate Laws

#### 2.3.1 APP synthesis
- **Type**: `MA` (zero-order production)
- **Reactants**: `[]` (source)
- **Products**: `[APP_Neuron]`
- **Rate law**: `k_APP_synth * V_Neuron`
- **Parameters**:
  - `k_APP_synth`: 0.5-5.0 nM/hr (Bhatt et al., 2022; Elbert model uses ~2 nM/hr)
- **Rationale**: Constant transcription/translation of APP, assumed to be at steady state in normal conditions.

#### 2.3.2 Alpha-secretase cleavage of APP
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[APP_Neuron]`
- **Products**: `[sAPPa_BrainISF, C83_Neuron]`
- **Rate law**: `Vmax_alpha * APP_Neuron / (Km_alpha + APP_Neuron)`
- **Parameters**:
  - `Vmax_alpha`: 5-50 nM/hr (Skovronsky et al., 2000, PMID:10642507; Bhatt et al., 2022)
  - `Km_alpha`: 10-100 nM (estimated from cell-based assays; Bhatt et al.)
- **Rationale**: Michaelis-Menten kinetics capture enzyme saturation. Alpha-secretase competes with beta-secretase for APP substrate.

#### 2.3.3 Beta-secretase (BACE1) cleavage of APP
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[APP_Neuron]`
- **Products**: `[sAPPb_BrainISF, C99_Neuron]`
- **Rate law**: `Vmax_beta * APP_Neuron / (Km_beta + APP_Neuron) * (BACE1_Endosome / BACE1_total)`
- **Parameters**:
  - `Vmax_beta`: 1-10 nM/hr (Lin et al., 2000, PMID:10816430; typical ~3 nM/hr)
  - `Km_beta`: 20-200 nM (measured Km for BACE1 on APP substrate in vitro: ~1-5 uM; effective in vivo lower due to membrane concentration; Bhatt et al.)
  - `BACE1_total`: reference normalization constant
- **Rationale**: BACE1 is rate-limiting for Abeta production. Michaelis-Menten appropriate because BACE1 is a classical aspartyl protease with well-characterized kinetics.

#### 2.3.4 Gamma-secretase cleavage of C99 to Abeta
- **Type**: `custom_conc_per_time` (Michaelis-Menten with branching)
- **Reactants**: `[C99_Neuron]`
- **Products**: `[AB42_BrainISF]` (one reaction per Abeta species)
- **Rate law (for Abeta42)**: `Vmax_gamma * C99_Neuron / (Km_gamma + C99_Neuron) * f_AB42`
- **Rate law (for Abeta40)**: `Vmax_gamma * C99_Neuron / (Km_gamma + C99_Neuron) * f_AB40`
- **Parameters**:
  - `Vmax_gamma`: 5-20 nM/hr (De Strooper et al., 2010, PMID:20139999)
  - `Km_gamma`: 50-500 nM
  - `f_AB42`: 0.05-0.15 (fraction going to Abeta42; ~10% of total Abeta; Bhatt et al.)
  - `f_AB40`: 0.80-0.90 (fraction going to Abeta40; ~85-90%)
  - `f_AB38`: 0.02-0.05 (fraction going to Abeta38; optional)
- **Rationale**: Gamma-secretase is an intramembrane protease complex (presenilin-1/2, nicastrin, APH-1, PEN-2). The branching fraction determines Abeta42/40 ratio, which is pathologically elevated in familial AD (PS1/PS2 mutations shift f_AB42 upward).

#### 2.3.5 Gamma-secretase cleavage of C83 to p3
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[C83_Neuron]`
- **Products**: `[p3_BrainISF]`
- **Rate law**: `Vmax_gamma_C83 * C83_Neuron / (Km_gamma_C83 + C83_Neuron)`
- **Parameters**: Similar to C99 cleavage; often simplified by assuming same Vmax_gamma and Km_gamma.
- **Note**: Often omitted in simplified models since p3 is considered non-pathogenic.

#### 2.3.6 APP degradation
- **Type**: `MA` (first-order)
- **Reactants**: `[APP_Neuron]`
- **Products**: `[]`
- **Rate law**: `k_APP_deg * APP_Neuron * V_Neuron`
- **Parameters**:
  - `k_APP_deg`: 0.1-0.5 /hr (APP half-life ~2-8 hours in neurons; Bhatt et al.)

### 2.4 Simplified Alternative (Mass-Action Lumped)

For the simplest module (matching current `abeta_production.yaml` style), the entire APP processing cascade can be lumped into a single zero-order Abeta production term:

```
AB42_production: -> AB42_BrainISF; k_AB42_prod * V_BrainISF
```

where `k_AB42_prod` = 3-10 pM/hr (Elbert: ~5e-12 mol/hr in 0.25 L = 20 pM/hr)

This is appropriate when APP processing details are not the focus of the module. The full Michaelis-Menten cascade should be used when modeling secretase inhibitor pharmacology.

---

## 3. Abeta Monomer/Oligomer/Fibril Kinetics

### 3.1 Biological Summary

Once released into the ISF, Abeta monomers undergo concentration-dependent aggregation:

1. **Nucleation**: Monomers form small oligomers (dimers, trimers, up to ~12-mers). This is the rate-limiting step governed by nucleated polymerization kinetics.
2. **Oligomer formation**: Small oligomers are the most neurotoxic species. They include Abeta*56 (~56 kDa, dodecamers), ADDLs (Abeta-derived diffusible ligands), and protofibrils.
3. **Fibril elongation**: Oligomers and monomers add to growing fibrils. Elongation is faster than nucleation.
4. **Secondary nucleation**: Existing fibril surfaces catalyze new oligomer formation from monomers (Knowles/Cohen mechanism). This creates positive feedback.
5. **Fibril fragmentation**: Fibrils break, generating new growth-competent ends.

### 3.2 Species

- `AB42_BrainISF` -- Abeta42 monomer (soluble)
- `AB40_BrainISF` -- Abeta40 monomer (soluble)
- `oAB42_BrainISF` -- Abeta42 oligomers (soluble, toxic)
- `fAB42_BrainISF` -- Abeta42 fibrils (soluble protofibrils)
- `AB42_BrainParenchyma` -- insoluble Abeta42 (plaque-associated)

Optional additional species:
- `oAB40_BrainISF` -- Abeta40 oligomers (less toxic)
- `AB42_dimer_BrainISF` -- Abeta42 dimers (specific toxic species)

### 3.3 Rate Law Approaches

There are two major frameworks for modeling Abeta aggregation:

#### 3.3.1 Approach A: Smoluchowski-Type Coagulation (Detailed)

Used in detailed models (e.g., Craft et al., 2002, PMID:12105649; Pallitto & Murphy, 2001, PMID:11165098). Models each oligomer size class (i=1 to N) with bimolecular association:

```
dM_i/dt = 0.5 * sum_{j=1}^{i-1} k_{j,i-j} * M_j * M_{i-j} - M_i * sum_{j=1}^{N} k_{i,j} * M_j
```

**Pros**: Mechanistically accurate, captures size distribution.
**Cons**: Requires tracking many species (50-100+), computationally expensive, many unknown rate constants.
**Verdict**: Not recommended for antimony_bootstrap. Too many species for practical ODE models.

#### 3.3.2 Approach B: Lumped 3-Species Model (Recommended)

Aggregate into three pools: Monomer (M), Oligomer (O), Fibril (F). This is the approach used in the Elbert_Esguerra model and most QSP frameworks.

**Nucleation (monomer to oligomer)**:
- **Type**: `custom_conc_per_time` or `MA`
- **Rate law**: `k_nuc * AB42_BrainISF^n_nuc` (nucleation order n_nuc = 2)
- **Parameters**:
  - `k_nuc`: 1e-4 to 1e-2 /nM/hr (strongly concentration-dependent; Knowles et al., 2009, PMID:19700509; Cohen et al., 2013, PMID:24270810)
  - `n_nuc`: 2 (dimerization as rate-limiting step; simplified from theoretical n=2-4)

**Oligomer to fibril (elongation/conversion)**:
- **Type**: `MA` (first or second order)
- **Rate law**: `k_elong * oAB42_BrainISF * V_BrainISF` (first-order conversion) or `k_elong * oAB42_BrainISF * fAB42_BrainISF * V_BrainISF` (template-dependent)
- **Parameters**:
  - `k_elong`: 0.01-1.0 /hr (first-order) or 1e-3-1e-1 /nM/hr (second-order)
  - Literature: Hellstrand et al., 2010 (PMID:19953381) report elongation rate constants of ~1e4 /M/s for Abeta42

**Secondary nucleation (fibril-catalyzed oligomer formation)**:
- **Type**: `custom_conc_per_time`
- **Rate law**: `k_2 * AB42_BrainISF^n2 * fAB42_BrainISF`
- **Parameters**:
  - `k_2`: 1e-6 to 1e-3 /nM^n2/hr (Cohen et al., 2013)
  - `n2`: 2 (reaction order for monomer in secondary nucleation)
- **Rationale**: Secondary nucleation is the dominant mechanism for oligomer generation in the presence of fibrils. This is the key insight from the Knowles group (Cambridge) and is critical for capturing the autocatalytic nature of Abeta aggregation.

**Fibril fragmentation** (optional):
- **Type**: `MA`
- **Rate law**: `k_frag * fAB42_BrainISF * V_BrainISF`
- **Parameters**: `k_frag`: 1e-6 to 1e-4 /hr

#### 3.3.3 Approach C: Nucleated Polymerization (Knowles/Cohen Framework)

The analytically tractable framework from Cohen et al. (2012, PMID:22406560) uses integrated rate laws for total fibril mass M(t) and fibril number P(t):

```
dM/dt = 2 * k_elong * m(t) * P(t)
dP/dt = k_nuc * m(t)^nc + k_2 * m(t)^n2 * M(t) + k_frag * M(t)
dm/dt = -dM/dt   (mass conservation)
```

where m(t) = monomer concentration, M(t) = fibril mass, P(t) = fibril number.

This maps cleanly to the antimony_bootstrap framework:
- `AB42_BrainISF` = m(t)
- `fAB42_BrainISF` = M(t)
- `P_fib_BrainISF` = P(t) (fibril number, auxiliary variable)
- Oligomers can be approximated as proportional to dP/dt

**Parameters from Cohen et al., 2013 (PMID:24270810), Abeta42 at pH 7.4, 37C**:
- `k_nuc` (primary nucleation): ~3e-4 /M/s (nc=2)
- `k_elong` (elongation): ~3e6 /M/s
- `k_2` (secondary nucleation): ~1e4 /M^(n2+1)/s (n2=2)
- `k_frag`: negligible for Abeta42 under quiescent conditions

**Recommended conversion to model units** (nM, hr):
- `k_nuc`: ~1.1e-6 /nM/hr
- `k_elong`: ~1.1e4 /nM/hr
- `k_2`: ~3.6e1 /nM^2/hr

### 3.4 Recommended Implementation

For antimony_bootstrap, use **Approach B (Lumped 3-Species)** with secondary nucleation from Approach C:

```yaml
reactions:
  - name: AB42_nucleation
    reactants: [AB42_BrainISF]
    products: [oAB42_BrainISF]
    rate_type: custom_conc_per_time
    rate_parameters: [k_nuc, AB42_BrainISF]
    notes: "Primary nucleation: k_nuc * AB42^2 (second-order in monomer)"

  - name: AB42_secondary_nucleation
    reactants: [AB42_BrainISF]
    products: [oAB42_BrainISF]
    rate_type: custom_conc_per_time
    rate_parameters: [k_2, AB42_BrainISF, fAB42_BrainISF]
    notes: "Secondary nucleation: k_2 * AB42^2 * fAB42 (fibril-catalyzed)"

  - name: AB42_elongation
    reactants: [oAB42_BrainISF]
    products: [fAB42_BrainISF]
    rate_type: MA
    rate_parameters: [k_elong]
    notes: "Oligomer-to-fibril conversion/elongation"

  - name: AB42_monomer_to_fibril
    reactants: [AB42_BrainISF]
    products: [fAB42_BrainISF]
    rate_type: custom_conc_per_time
    rate_parameters: [k_elong_m, AB42_BrainISF, fAB42_BrainISF]
    notes: "Direct monomer addition to fibril ends: k_elong_m * AB42 * fAB42"
```

---

## 4. Plaque Formation and Clearance

### 4.1 Biological Summary

Insoluble amyloid plaques form when fibrils deposit in brain parenchyma. Plaque formation is essentially irreversible under normal conditions. Clearance mechanisms include:

1. **Microglial phagocytosis**: Microglia surround and internalize plaque material. Efficiency depends on microglial activation state and ApoE genotype.
2. **Enzymatic degradation**: Neprilysin (NEP), insulin-degrading enzyme (IDE), matrix metalloproteinases (MMPs) degrade soluble Abeta. These enzymes are less effective against insoluble plaques.
3. **Perivascular drainage**: Soluble Abeta drains along perivascular channels (Weller pathway). Impaired in cerebral amyloid angiopathy (CAA).
4. **BBB efflux**: LRP1-mediated transport of soluble Abeta across BBB into plasma. RAGE mediates influx from plasma to brain.
5. **Anti-Abeta antibody-mediated clearance**: Relevant for immunotherapy modeling (lecanemab, aducanumab, donanemab).

### 4.2 Species

- `Plaque_BrainParenchyma` -- insoluble amyloid plaque (measured in Centiloid or SUVr units for PET; in model, use mol or arbitrary units)
- `NEP_BrainISF` -- neprilysin enzyme
- `IDE_BrainISF` -- insulin-degrading enzyme
- `LRP1_BBB` -- LRP1 receptor at BBB (optional)
- `RAGE_BBB` -- RAGE receptor at BBB (optional)

### 4.3 Reactions and Rate Laws

#### 4.3.1 Plaque deposition (fibril to plaque)
- **Type**: `UDF` (unidirectional flow)
- **Reactants**: `[fAB42_BrainISF]`
- **Products**: `[Plaque_BrainParenchyma]`
- **Rate law**: `k_dep * fAB42_BrainISF`
- **Parameters**:
  - `k_dep`: 0.001-0.05 /hr (estimated; Elbert model calibrated to PET amyloid trajectory over decades)
- **Rationale**: Deposition is essentially first-order in soluble fibril concentration. No volume multiplication (UDF) because this is a transfer between compartments.

#### 4.3.2 Neprilysin degradation of Abeta monomer
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[AB42_BrainISF]`
- **Products**: `[]` (sink)
- **Rate law**: `Vmax_NEP * AB42_BrainISF / (Km_NEP + AB42_BrainISF)`
- **Parameters**:
  - `Vmax_NEP`: 1-10 nM/hr (Iwata et al., 2001, PMID:11689568; Farris et al., 2003, PMID:14502290)
  - `Km_NEP`: 5-50 uM (Leissring et al., 2003, PMID:14573789; note: Km is much higher than physiological Abeta concentrations ~1-10 nM, so the reaction is essentially first-order in vivo)
- **Simplification**: Since [AB42] << Km, can approximate as first-order: `k_deg_NEP * AB42_BrainISF` where `k_deg_NEP = Vmax_NEP / Km_NEP` ~ 0.01-0.1 /hr

#### 4.3.3 IDE degradation of Abeta
- **Type**: `custom_conc_per_time` (Michaelis-Menten) or `MA` (simplified)
- **Parameters**:
  - `Vmax_IDE`: 0.5-5 nM/hr
  - `Km_IDE`: 1-10 uM (Qiu et al., 1998, PMID:9813085)
- **Note**: IDE also degrades insulin, creating a competition relevant for metabolic syndrome/AD comorbidity models.

#### 4.3.4 Abeta degradation (lumped first-order)
For simplified models, lump all enzymatic degradation into a single first-order term:
- **Type**: `MA`
- **Rate law**: `k_AB42_deg * AB42_BrainISF * V_BrainISF`
- **Parameters**:
  - `k_AB42_deg`: 0.05-0.15 /hr (Abeta42 half-life in ISF ~4-14 hours; Bateman et al., 2006, PMID:17035524; Patterson et al., 2015, PMID:25568215)
  - Elbert model: ~0.069 /hr (t1/2 ~ 10 hr)

#### 4.3.5 BBB efflux (LRP1-mediated)
- **Type**: `UDF`
- **Reactants**: `[AB42_BrainISF]`
- **Products**: `[AB42_Plasma]`
- **Rate law**: `k_LRP1 * AB42_BrainISF`
- **Parameters**:
  - `k_LRP1`: 0.01-0.1 /hr (Deane et al., 2004, PMID:15337763; Shibata et al., 2000, PMID:10806142)

#### 4.3.6 BBB influx (RAGE-mediated)
- **Type**: `UDF`
- **Reactants**: `[AB42_Plasma]`
- **Products**: `[AB42_BrainISF]`
- **Rate law**: `k_RAGE * AB42_Plasma`
- **Parameters**:
  - `k_RAGE`: 0.001-0.01 /hr (Deane et al., 2003, PMID:12805289)
- **Note**: RAGE influx is normally minor relative to LRP1 efflux, but RAGE is upregulated in AD.

#### 4.3.7 ISF to CSF bulk flow
- **Type**: `UDF`
- **Reactants**: `[AB42_BrainISF]`
- **Products**: `[AB42_CSF]`
- **Rate law**: `k_ISF_CSF * AB42_BrainISF`
- **Parameters**:
  - `k_ISF_CSF`: 0.02-0.05 /hr (Elbert: 0.035 /hr; consistent with CSF turnover ~4x/day)

#### 4.3.8 CSF to plasma absorption
- **Type**: `UDF`
- **Reactants**: `[AB42_CSF]`
- **Products**: `[AB42_Plasma]`
- **Rate law**: `k_CSF_Plasma * AB42_CSF`
- **Parameters**:
  - `k_CSF_Plasma`: 0.015-0.04 /hr (Elbert: 0.025 /hr)

#### 4.3.9 Plasma clearance
- **Type**: `MA`
- **Reactants**: `[AB42_Plasma]`
- **Products**: `[]`
- **Rate law**: `k_AB42_deg_Plasma * AB42_Plasma * V_Plasma`
- **Parameters**:
  - `k_AB42_deg_Plasma`: 0.1-0.3 /hr (Abeta42 plasma half-life ~2-5 hours; Ghiso et al., 2004; Elbert: 0.14 /hr)

#### 4.3.10 Microglial phagocytosis of plaque
- **Type**: `custom_conc_per_time` (Michaelis-Menten or Hill)
- **Reactants**: `[Plaque_BrainParenchyma]`
- **Products**: `[]` (sink) or `[AB42_BrainISF]` (resolubilization)
- **Rate law**: `Vmax_phago * Plaque_BrainParenchyma / (Km_phago + Plaque_BrainParenchyma) * Microglia_active`
- **Parameters**:
  - `Vmax_phago`: 0.001-0.01 /hr (very slow; plaque accumulation takes decades)
  - `Km_phago`: model-dependent
- **Note**: This reaction connects to the neuroinflammation module (microglial activation state). For the amyloid-only module, use a simplified first-order plaque clearance: `k_plaque_clear * Plaque_BrainParenchyma`.
  - `k_plaque_clear`: 1e-5 to 1e-3 /hr (effectively negligible without anti-Abeta antibody)

---

## 5. Parameter Summary Table

| Parameter | Value | Range | Units | Source | Confidence |
|---|---|---|---|---|---|
| `k_APP_synth` | 2.0 | 0.5-5.0 | nM/hr | Elbert model | estimated |
| `Vmax_alpha` | 20 | 5-50 | nM/hr | Skovronsky 2000 | estimated |
| `Km_alpha` | 50 | 10-100 | nM | Cell-based assays | estimated |
| `Vmax_beta` | 3.0 | 1-10 | nM/hr | Lin 2000 | estimated |
| `Km_beta` | 100 | 20-200 | nM | BACE1 kinetics | estimated |
| `Vmax_gamma` | 10 | 5-20 | nM/hr | De Strooper 2010 | estimated |
| `Km_gamma` | 200 | 50-500 | nM | Cell-free assays | estimated |
| `f_AB42` | 0.10 | 0.05-0.15 | dimensionless | Abeta42/total ratio | measured |
| `f_AB40` | 0.85 | 0.80-0.90 | dimensionless | Abeta40/total ratio | measured |
| `k_APP_deg` | 0.2 | 0.1-0.5 | /hr | APP t1/2 ~3-7 hr | estimated |
| `k_nuc` | 1e-6 | 1e-8 to 1e-4 | /nM/hr | Cohen 2013 | measured |
| `k_elong` | 1e4 | 1e2 to 1e5 | /nM/hr | Hellstrand 2010 | measured |
| `k_2` | 36 | 1-100 | /nM^2/hr | Cohen 2013 | measured |
| `k_dep` | 0.01 | 0.001-0.05 | /hr | Elbert (PET fit) | estimated |
| `k_AB42_deg` | 0.069 | 0.05-0.15 | /hr | Bateman 2006 | measured |
| `k_LRP1` | 0.05 | 0.01-0.1 | /hr | Deane 2004 | estimated |
| `k_RAGE` | 0.005 | 0.001-0.01 | /hr | Deane 2003 | estimated |
| `k_ISF_CSF` | 0.035 | 0.02-0.05 | /hr | Elbert model | estimated |
| `k_CSF_Plasma` | 0.025 | 0.015-0.04 | /hr | Elbert model | estimated |
| `k_AB42_deg_Plasma` | 0.14 | 0.1-0.3 | /hr | Ghiso 2004 | estimated |
| `k_plaque_clear` | 1e-4 | 1e-5 to 1e-3 | /hr | Negligible naturally | assumed |

---

## 6. Recommended Module Decomposition

The amyloid cascade should be split into 3-4 modules for antimony_bootstrap:

### Module 1: `app_processing` (NEW)
- APP synthesis, alpha/beta/gamma cleavage
- Species: APP_Neuron, sAPPa, sAPPb, C83, C99
- Products feed into Module 2
- Rate laws: Michaelis-Menten for secretase reactions, MA for synthesis/degradation

### Module 2: `abeta_production` (EXISTING -- extend)
- Abeta monomer production (from C99 cleavage or lumped), transport across compartments, degradation
- Species: AB42_BrainISF, AB42_CSF, AB42_Plasma, AB40_BrainISF, AB40_CSF, AB40_Plasma
- Rate laws: UDF for transport, MA for degradation

### Module 3: `abeta_aggregation` (NEW)
- Monomer to oligomer to fibril kinetics
- Species: AB42_BrainISF (shared), oAB42_BrainISF, fAB42_BrainISF
- Rate laws: Custom (nucleation with power law), MA (elongation)
- Secondary nucleation as key feedback loop

### Module 4: `plaque_dynamics` (NEW)
- Fibril deposition to insoluble plaque, plaque clearance
- Species: fAB42_BrainISF (shared), Plaque_BrainParenchyma
- Connections to neuroinflammation module (microglial clearance)
- Rate laws: UDF (deposition), custom (clearance depends on microglia)

---

## 7. Key Literature References

1. **Selkoe & Hardy (2016)** PMID:27025652 -- "The amyloid hypothesis of Alzheimer's disease at 25 years." Comprehensive review of the amyloid cascade.

2. **Cohen et al. (2013)** PMID:24270810 -- "Proliferation of amyloid-beta42 aggregates occurs through a secondary nucleation mechanism." Quantitative kinetic parameters for Abeta42 aggregation.

3. **Knowles et al. (2009)** PMID:19700509 -- "An analytical solution to the kinetics of breakable filament assembly." Mathematical framework for nucleated polymerization.

4. **Bateman et al. (2006)** PMID:17035524 -- "Human amyloid-beta synthesis and clearance rates as measured in cerebrospinal fluid in vivo." Direct measurement of Abeta production and clearance rates in humans (~7.6%/hr production, ~8.3%/hr clearance).

5. **Mawuenyega et al. (2010)** PMID:21147930 -- "Decreased clearance of CNS beta-amyloid in Alzheimer's disease." Showed ~30% reduction in Abeta42 clearance rate in AD vs. controls (clearance rate 5.3 vs. 7.6 %/hr).

6. **Bhatt et al. (2022)** -- Elbert group QSP model documentation. Primary source for parameter values and naming conventions.

7. **Deane et al. (2004)** PMID:15337763 -- "LRP/amyloid beta-peptide interaction mediates differential brain efflux of Abeta isoforms." LRP1-mediated BBB transport rates.

8. **Iwata et al. (2001)** PMID:11689568 -- "Metabolic regulation of brain Abeta by neprilysin." Neprilysin as major Abeta-degrading enzyme.

9. **Hellstrand et al. (2010)** PMID:19953381 -- "Amyloid beta-protein aggregation produces highly reproducible kinetic data and occurs by a two-phase process." Elongation rate constants for Abeta42.

10. **Patterson et al. (2015)** PMID:25568215 -- "Age and amyloid effects on human CNS amyloid-beta kinetics." SILK study: Abeta42 half-life ~9.4 hours in ISF.

---

## 8. Mapping to Elbert_Esguerra Rate Types

| Biological Process | Rate Type | Rationale |
|---|---|---|
| APP synthesis | `MA` (zero-order) | Constant production rate |
| Alpha/beta/gamma cleavage | `custom_conc_per_time` | Michaelis-Menten enzyme kinetics |
| Abeta degradation (lumped) | `MA` (first-order) | [Abeta] << Km, linear regime |
| ISF-to-CSF transport | `UDF` | Bulk flow, no volume multiplication |
| CSF-to-Plasma transport | `UDF` | Bulk flow |
| BBB efflux (LRP1) | `UDF` | Transporter-mediated, first-order |
| BBB influx (RAGE) | `UDF` | Transporter-mediated, first-order |
| Nucleation | `custom_conc_per_time` | Power-law kinetics (n=2) |
| Secondary nucleation | `custom_conc_per_time` | Monomer^2 * fibril catalysis |
| Elongation | `MA` or `custom_conc_per_time` | Bimolecular (monomer + fibril) |
| Plaque deposition | `UDF` | First-order transfer |
| Plaque clearance | `custom_conc_per_time` | Depends on microglial state |
| Plasma clearance | `MA` | First-order degradation |

---

## 9. Implementation Priority

1. **Extend `abeta_production.yaml`** to include AB40 species alongside AB42, and add Abeta40/42 ratio tracking.
2. **Build `abeta_aggregation.yaml`** with the 3-species lumped model (monomer, oligomer, fibril) and secondary nucleation.
3. **Build `plaque_dynamics.yaml`** for fibril-to-plaque deposition and basic clearance.
4. **Build `app_processing.yaml`** with full secretase cascade (needed for BACE inhibitor or gamma-secretase modulator pharmacology).
5. **Validate** each module independently, then compose and validate the full amyloid cascade.

The secondary nucleation mechanism (Section 3.3.3) is the single most important kinetic feature to get right, as it creates the positive feedback loop that explains the decades-long prodromal phase followed by rapid amyloid accumulation.
