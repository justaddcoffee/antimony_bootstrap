# Strategy: Lipid Metabolism & ApoE Mechanisms for Antimony ODE Models

## 1. Overview

This document outlines strategies for encoding lipid metabolism and ApoE-related Alzheimer's disease mechanisms as ODE-based Antimony models. The lipid/ApoE axis is one of the strongest genetic risk pathways in AD, centered on the APOE gene (chromosome 19), cholesterol homeostasis in the brain, and the interplay between lipoproteins and amyloid-beta (Abeta) clearance.

---

## 2. ApoE Isoform Effects (E2/E3/E4)

### 2.1 Biological Background

- **ApoE2** (Cys112/Cys158): Protective, enhanced Abeta clearance, better lipid recycling
- **ApoE3** (Cys112/Arg158): Reference/neutral isoform
- **ApoE4** (Arg112/Arg158): Major genetic risk factor (~3x heterozygous, ~12x homozygous AD risk)

Key functional differences:
- ApoE4 has reduced lipidation efficiency (lower ABCA1 affinity)
- ApoE4 is preferentially degraded, leading to lower steady-state levels
- ApoE4 binds Abeta with different kinetics (lower affinity for Abeta clearance receptors)
- ApoE4 promotes Abeta aggregation and impairs glial-mediated clearance

### 2.2 ODE Representation of Genetic Variants

**Approach: Isoform-specific parameters, not separate species.**

The recommended approach is to use a single ApoE species but parameterize rate constants differently per genotype. This avoids combinatorial explosion while capturing the key biology.

```antimony
// Genotype-specific parameter sets (select one configuration)
// E3/E3 (reference)
k_ApoE_lipidation = 0.05;      // 1/hr
k_ApoE_Abeta_binding = 1.2e-3; // 1/(nM*hr)
k_ApoE_degradation = 0.02;     // 1/hr
k_ApoE_production = 0.5;       // nM/hr

// E4/E4 (risk)
// k_ApoE_lipidation = 0.025;    // ~50% reduced
// k_ApoE_Abeta_binding = 0.6e-3; // ~50% reduced
// k_ApoE_degradation = 0.04;    // ~2x faster degradation
// k_ApoE_production = 0.45;     // slightly reduced

// E2/E3 (protective)
// k_ApoE_lipidation = 0.065;    // ~30% enhanced
// k_ApoE_Abeta_binding = 1.5e-3; // ~25% enhanced
// k_ApoE_degradation = 0.015;   // slightly slower
```

**Alternative: Scaling factors**

For models that need to switch genotypes easily:

```antimony
// Genotype scaling factors (multiply reference E3/E3 rates)
isoform_lipidation_scale = 1.0;   // E3/E3=1.0, E4/E4=0.5, E2/E3=1.3
isoform_clearance_scale = 1.0;    // E3/E3=1.0, E4/E4=0.5, E2/E3=1.25
isoform_stability_scale = 1.0;    // E3/E3=1.0, E4/E4=0.5, E2/E3=1.15
```

This approach is compatible with the Elbert convention and allows genotype sweeps.

---

## 3. Brain Cholesterol Metabolism

### 3.1 Key Species

| Species | Compartment | Typical Concentration |
|---------|-------------|----------------------|
| Cholesterol_Neuron | Neuron | ~40 ug/mg protein |
| Cholesterol_Astrocyte | Astrocyte | ~30 ug/mg protein |
| Cholesterol_BrainISF | BrainISF | ~0.5-2 uM (free) |
| 24OHC_BrainISF | BrainISF | ~10-50 nM |
| 24OHC_Plasma | Plasma | ~30-80 ng/mL |
| 27OHC_Plasma | Plasma | ~100-200 ng/mL |
| 27OHC_BrainISF | BrainISF | ~1-5 nM |
| Desmosterol_Astrocyte | Astrocyte | variable |

### 3.2 Key Reactions

```
// Cholesterol synthesis (neurons - minimal in adult brain)
R_chol_synth_neuron: => Cholesterol_Neuron; k_chol_synth_neuron * HMGCoA_Neuron * Neuron

// Cholesterol synthesis (astrocytes - primary source in adult brain)
R_chol_synth_astro: => Cholesterol_Astrocyte; k_chol_synth_astro * HMGCoA_Astrocyte * Astrocyte

// Cholesterol efflux from astrocytes via ApoE lipoproteins
R_chol_efflux_astro: Cholesterol_Astrocyte => Cholesterol_BrainISF; k_chol_efflux * ApoE_lipidated_BrainISF * ABCA1_Astrocyte * Astrocyte

// Cholesterol uptake by neurons via LDL receptors
R_chol_uptake_neuron: Cholesterol_BrainISF => Cholesterol_Neuron; k_chol_uptake * LDLR_Neuron * ApoE_lipidated_BrainISF / (Km_LDLR + ApoE_lipidated_BrainISF) * Neuron

// CYP46A1 conversion (neuron-specific, major elimination pathway)
R_24OHC_formation: Cholesterol_Neuron => 24OHC_BrainISF; Vmax_CYP46A1 * Cholesterol_Neuron / (Km_CYP46A1 + Cholesterol_Neuron) * Neuron

// 24-OHC efflux across BBB (diffusion-driven)
R_24OHC_efflux: 24OHC_BrainISF => 24OHC_Plasma; k_24OHC_BBB * 24OHC_BrainISF * BBB

// 27-OHC influx from periphery
R_27OHC_influx: 27OHC_Plasma => 27OHC_BrainISF; k_27OHC_BBB * 27OHC_Plasma * BBB
```

### 3.3 Parameter Ranges

| Parameter | Value Range | Units | Source |
|-----------|-------------|-------|--------|
| k_chol_synth_astro | 0.01-0.1 | nmol/mg/hr | Pfrieger 2003 |
| Vmax_CYP46A1 | 0.5-5 | nmol/mg/hr | Lund et al. 2003 |
| Km_CYP46A1 | 10-50 | uM | Mast et al. 2003 |
| k_24OHC_BBB | 0.1-1.0 | 1/hr | Lutjohann et al. 1996 |
| k_27OHC_BBB | 0.01-0.05 | 1/hr | Heverin et al. 2005 |
| k_chol_efflux | 0.001-0.01 | 1/(nM*hr) | Karten et al. 2006 |

---

## 4. Lipid Raft Dynamics

### 4.1 Modeling Approach

Lipid rafts are cholesterol/sphingolipid-enriched membrane microdomains that concentrate APP processing machinery (BACE1, gamma-secretase). Model as a partitioning equilibrium:

```antimony
// Lipid raft cholesterol partitioning
R_raft_formation: Cholesterol_Neuron + Sphingomyelin_Neuron => CholSM_Raft_Neuron; k_raft_on * Cholesterol_Neuron * Sphingomyelin_Neuron * Neuron
R_raft_dissolution: CholSM_Raft_Neuron => Cholesterol_Neuron + Sphingomyelin_Neuron; k_raft_off * CholSM_Raft_Neuron * Neuron

// APP partitioning into rafts (determines amyloidogenic vs non-amyloidogenic)
fraction_APP_raft = CholSM_Raft_Neuron / (CholSM_Raft_Neuron + Kd_APP_raft)

// Amyloidogenic processing (raft-dependent)
R_APP_beta_cleavage: APP_Neuron => sAPPbeta_Neuron + CTFbeta_Neuron; k_BACE1 * APP_Neuron * fraction_APP_raft * BACE1_Neuron * Neuron

// Non-amyloidogenic processing (non-raft)
R_APP_alpha_cleavage: APP_Neuron => sAPPalpha_Neuron + CTFalpha_Neuron; k_ADAM10 * APP_Neuron * (1 - fraction_APP_raft) * ADAM10_Neuron * Neuron
```

### 4.2 Key Insight for ODE Models

Rather than explicitly modeling thousands of raft domains, use a **fractional partitioning** approach:
- fraction_APP_raft is a Hill-type function of raft cholesterol
- This captures the sigmoidal dependence of beta-secretase processing on cholesterol
- Consistent with experimental data showing statins reduce Abeta by ~25-40%

### 4.3 Parameters

| Parameter | Value Range | Units | Notes |
|-----------|-------------|-------|-------|
| k_raft_on | 0.01-0.1 | 1/(uM*hr) | Fast equilibrium |
| k_raft_off | 0.1-1.0 | 1/hr | |
| Kd_APP_raft | 5-20 | uM (cholesterol equiv) | Half-max raft partitioning |
| Baseline fraction_APP_raft | 0.3-0.5 | dimensionless | Ehehalt et al. 2003 |

---

## 5. ApoE-Abeta Interactions

### 5.1 Binding Kinetics

ApoE competes with Abeta for receptor-mediated clearance and directly modulates Abeta aggregation.

```antimony
// ApoE-Abeta complex formation (reversible)
R_ApoE_Abeta_bind: ApoE_lipidated_BrainISF + AB42_BrainISF -> ApoE_AB42_BrainISF; k_ApoE_AB_on * ApoE_lipidated_BrainISF * AB42_BrainISF * BrainISF
R_ApoE_Abeta_unbind: ApoE_AB42_BrainISF -> ApoE_lipidated_BrainISF + AB42_BrainISF; k_ApoE_AB_off * ApoE_AB42_BrainISF * BrainISF

// Receptor-mediated clearance of ApoE-Abeta complex (via LRP1)
R_ApoE_AB_clearance: ApoE_AB42_BrainISF => ; k_LRP1_clearance * LRP1_Neuron * ApoE_AB42_BrainISF / (Km_LRP1 + ApoE_AB42_BrainISF) * BrainISF

// ApoE effect on Abeta aggregation (seeding/nucleation)
R_AB_aggregation: 2 AB42_BrainISF => AB42_oligomer_BrainISF; k_aggregation * (1 + f_ApoE4_aggregation * ApoE_lipidated_BrainISF) * AB42_BrainISF^2 * BrainISF
// f_ApoE4_aggregation: 0 for E2, 0 for E3, 0.5-2.0 for E4
```

### 5.2 Isoform-Specific Binding Parameters

| Parameter | ApoE2 | ApoE3 | ApoE4 | Units | Source |
|-----------|-------|-------|-------|-------|--------|
| k_ApoE_AB_on | 2.0e-3 | 1.2e-3 | 0.6e-3 | 1/(nM*hr) | Tokuda et al. 2000 |
| k_ApoE_AB_off | 0.1 | 0.1 | 0.2 | 1/hr | |
| Kd_ApoE_AB | ~50 | ~80 | ~330 | nM | LaDu et al. 1994 |
| k_LRP1_clearance | 1.5 | 1.0 | 0.4 | 1/hr | Deane et al. 2008 |

---

## 6. Lipoprotein Particles in CSF

### 6.1 Biology

Brain lipoproteins are HDL-like particles (8-17 nm), primarily containing ApoE, ApoJ (clusterin), phospholipids, and cholesterol. They are distinct from plasma lipoproteins.

### 6.2 Species Definitions

```antimony
// Lipoprotein assembly states
ApoE_free_BrainISF = 0;        // unlipidated ApoE (rapidly lipidated)
ApoE_lipidated_BrainISF = 0;   // lipidated ApoE-HDL particle
ApoJ_BrainISF = 0;             // clusterin, also binds Abeta
ApoE_ApoJ_BrainISF = 0;        // mixed lipoprotein particle

// ApoE lipidation (ABCA1-dependent)
R_ApoE_lipidation: ApoE_free_BrainISF => ApoE_lipidated_BrainISF; k_lipidation * ABCA1_Astrocyte * ApoE_free_BrainISF * Astrocyte

// ApoE secretion from astrocytes
R_ApoE_secretion: => ApoE_free_BrainISF; k_ApoE_secrete * Astrocyte * (1 + LXR_activation_Astrocyte)

// ApoE degradation
R_ApoE_degrad: ApoE_lipidated_BrainISF => ; k_ApoE_deg * ApoE_lipidated_BrainISF * BrainISF
```

### 6.3 CSF Lipoprotein Parameters

| Parameter | Value Range | Units | Source |
|-----------|-------------|-------|--------|
| CSF ApoE concentration | 3-10 | ug/mL | Pitas et al. 1987 |
| CSF ApoJ concentration | 5-15 | ug/mL | Schrijvers et al. 2011 |
| ApoE half-life (brain) | 4-12 | hr | Riddell et al. 2008 |
| ApoE4 half-life (brain) | 2-6 | hr | ~50% shorter |
| k_ApoE_secrete | 0.1-0.5 | nM/hr | Per astrocyte compartment |

---

## 7. ABCA1/ABCG1 Transporters

### 7.1 Biological Roles

- **ABCA1**: Lipidates ApoE, rate-limiting step for HDL-like particle formation. Regulated by LXR.
- **ABCG1**: Adds cholesterol to partially lipidated particles. Works downstream of ABCA1.
- Both are transcriptionally regulated by LXR/RXR in response to oxysterols (24-OHC, 27-OHC).

### 7.2 ODE Formulation

```antimony
// ABCA1 transcriptional regulation by LXR (oxysterol-dependent)
LXR_activation_Astrocyte := (24OHC_Astrocyte + 27OHC_Astrocyte)^n_LXR / (Kd_LXR^n_LXR + (24OHC_Astrocyte + 27OHC_Astrocyte)^n_LXR)

// ABCA1 expression
R_ABCA1_synth: => ABCA1_Astrocyte; k_ABCA1_basal * (1 + fold_ABCA1_LXR * LXR_activation_Astrocyte) * Astrocyte
R_ABCA1_degrad: ABCA1_Astrocyte => ; k_ABCA1_deg * ABCA1_Astrocyte * Astrocyte

// ABCG1 expression (also LXR-regulated)
R_ABCG1_synth: => ABCG1_Astrocyte; k_ABCG1_basal * (1 + fold_ABCG1_LXR * LXR_activation_Astrocyte) * Astrocyte
R_ABCG1_degrad: ABCG1_Astrocyte => ; k_ABCG1_deg * ABCG1_Astrocyte * Astrocyte

// Cholesterol efflux via ABCA1 (to nascent ApoE particles)
R_chol_ABCA1: Cholesterol_Astrocyte => ApoE_lipidated_BrainISF; k_ABCA1_efflux * ABCA1_Astrocyte * Cholesterol_Astrocyte * ApoE_free_BrainISF / (Km_ABCA1 + Cholesterol_Astrocyte) * Astrocyte

// Cholesterol efflux via ABCG1 (to mature ApoE particles)
R_chol_ABCG1: Cholesterol_Astrocyte => ApoE_lipidated_BrainISF; k_ABCG1_efflux * ABCG1_Astrocyte * Cholesterol_Astrocyte * ApoE_lipidated_BrainISF / (Km_ABCG1 + Cholesterol_Astrocyte) * Astrocyte
```

### 7.3 Parameters

| Parameter | Value Range | Units | Source |
|-----------|-------------|-------|--------|
| k_ABCA1_basal | 0.01-0.05 | nM/hr | |
| fold_ABCA1_LXR | 3-10 | fold | Koldamova et al. 2003 |
| Kd_LXR | 1-10 | uM (oxysterol) | Janowski et al. 1999 |
| n_LXR | 1.5-2.5 | Hill coeff | |
| Km_ABCA1 | 5-20 | uM | |
| k_ABCA1_efflux | 0.001-0.01 | 1/(nM*hr) | Wahrle et al. 2004 |

### 7.4 Therapeutic Relevance

LXR agonists (e.g., GW3965, T0901317) increase ABCA1/ABCG1 expression, enhance ApoE lipidation, and improve Abeta clearance in mouse models.

---

## 8. ApoE4 Effects on Abeta Clearance

### 8.1 Mechanisms

ApoE4 impairs Abeta clearance through multiple pathways:

1. **Reduced lipidation** -- less efficient receptor binding -- slower clearance
2. **Lower steady-state ApoE levels** -- fewer clearance vehicles
3. **Competitive inhibition at LRP1** -- ApoE4 occupies receptors less productively
4. **Impaired glial phagocytosis** -- ApoE4 microglia clear less Abeta
5. **Enhanced Abeta aggregation** -- shifts monomer to oligomer equilibrium

### 8.2 Consolidated Clearance Model

```antimony
// 1. LRP1-mediated clearance (ApoE-dependent)
R_AB_LRP1: AB42_BrainISF => ; k_LRP1 * isoform_clearance_scale * LRP1_endothelial * ApoE_lipidated_BrainISF * AB42_BrainISF / (Km_LRP1_app + AB42_BrainISF) * BBB

// 2. Enzymatic degradation (NEP, IDE - partially ApoE-independent)
R_AB_NEP: AB42_BrainISF => ; k_NEP * NEP_BrainISF * AB42_BrainISF / (Km_NEP + AB42_BrainISF) * BrainISF

// 3. BBB transport (RAGE influx, LRP1 efflux)
R_AB_BBB_efflux: AB42_BrainISF => AB42_Plasma; k_BBB_efflux * isoform_clearance_scale * AB42_BrainISF * BBB
R_AB_BBB_influx: AB42_Plasma => AB42_BrainISF; k_RAGE * RAGE_endothelial * AB42_Plasma / (Km_RAGE + AB42_Plasma) * BBB

// 4. Microglial phagocytosis
R_AB_microglia: AB42_BrainISF => ; k_phago * Microglia_activated * isoform_clearance_scale * AB42_BrainISF / (Km_phago + AB42_BrainISF) * BrainISF
```

### 8.3 Clearance Rate Parameters by Genotype

| Pathway | E3/E3 half-clearance | E4/E4 half-clearance | Ratio | Source |
|---------|---------------------|---------------------|-------|--------|
| LRP1 at BBB | ~30 min | ~60 min | 2x slower | Deane et al. 2008 |
| Microglial | ~2 hr | ~4 hr | 2x slower | Lin et al. 2018 |
| Total ISF Abeta | ~1-2 hr | ~3-4 hr | 2-3x slower | Castellano et al. 2011 |

---

## 9. ApoE4 Effects on Tau Pathology

### 9.1 Mechanisms

Recent evidence (Shi et al. 2017, 2019) shows ApoE4 exacerbates tau pathology independently of Abeta:
- ApoE4 amplifies microglial neuroinflammatory response to tau
- ApoE4 impairs neuronal autophagy, reducing tau clearance
- ApoE4 increases tau phosphorylation via GSK3beta activation

### 9.2 ODE Representation

```antimony
// ApoE4-enhanced neuroinflammation amplifies tau phosphorylation
k_tau_phos_base = 0.01;  // 1/hr
f_ApoE_neuroinflam = 1.0;  // E3/E3=1.0, E4/E4=2.0-3.0

R_tau_phosphorylation: Tau_Neuron => pTau_Neuron; k_tau_phos_base * f_ApoE_neuroinflam * (GSK3b_active_Neuron + CDK5_active_Neuron) * Tau_Neuron * Neuron

// ApoE4-impaired tau autophagy
k_tau_autophagy_base = 0.05;  // 1/hr
f_ApoE_autophagy = 1.0;  // E3/E3=1.0, E4/E4=0.5

R_tau_autophagy: pTau_Neuron => ; k_tau_autophagy_base * f_ApoE_autophagy * Autophagy_Neuron * pTau_Neuron * Neuron

// ApoE-dependent microglial activation by tau
R_microglia_tau_activation: Microglia_resting => Microglia_activated; k_microglia_tau * pTau_BrainISF * f_ApoE_neuroinflam * Microglia_resting * BrainISF
```

---

## 10. Rate Law Forms Summary

### Recommended Rate Types (per Elbert convention)

| Mechanism | Rate Type | Form |
|-----------|-----------|------|
| ApoE secretion | MA (mass action) | k * compartment_vol |
| ApoE lipidation | custom_conc_per_time | k * ABCA1 * ApoE_free * compartment_vol |
| Cholesterol synthesis | MA | k * precursor * compartment_vol |
| Receptor-mediated clearance | custom_conc_per_time (MM) | Vmax * S / (Km + S) * compartment_vol |
| Binding reactions | RMA (reversible MA) | k_on * A * B - k_off * AB |
| BBB transport | UDF (unidirectional flow) | k * S (no volume multiplication) |
| Transcriptional regulation | custom_conc_per_time (Hill) | k_basal * (1 + fold * S^n/(Kd^n + S^n)) * vol |
| Aggregation | custom_amt_per_time | k * S^2 (second-order) |

---

## 11. Module Decomposition for antimony_bootstrap

Recommended module breakdown:

### Module 1: brain_cholesterol_metabolism.yaml
- Cholesterol synthesis (neuron, astrocyte)
- CYP46A1 (24-OHC formation)
- 24-OHC/27-OHC BBB transport
- HMG-CoA reductase

### Module 2: apoe_lipoprotein.yaml
- ApoE secretion (astrocytes)
- ApoE lipidation (ABCA1-dependent)
- ApoE-HDL particle formation
- ApoE degradation
- Isoform-specific parameters

### Module 3: abca1_abcg1_transport.yaml
- ABCA1/ABCG1 transcription (LXR-regulated)
- Cholesterol efflux from astrocytes
- Cholesterol efflux from microglia
- LXR activation by oxysterols

### Module 4: apoe_abeta_clearance.yaml
- ApoE-Abeta binding
- LRP1-mediated clearance
- Competitive receptor dynamics
- ApoE effect on Abeta aggregation

### Module 5: lipid_raft_app_processing.yaml
- Raft cholesterol partitioning
- APP raft localization
- BACE1/gamma-secretase raft dependence
- Alpha-secretase non-raft processing

### Module 6: apoe_tau_interaction.yaml
- ApoE-modulated neuroinflammation
- ApoE effect on tau phosphorylation
- ApoE effect on tau autophagy
- Microglial activation by tau (ApoE-dependent)

---

## 12. Key Literature References

1. **Holtzman et al. (2012)** - Apolipoprotein E and apolipoprotein E receptors - Cold Spring Harb Perspect Med
2. **Castellano et al. (2011)** - Human apoE isoforms differentially regulate brain Abeta clearance - Sci Transl Med
3. **Deane et al. (2008)** - apoE isoform-specific disruption of Abeta clearance - J Clin Invest
4. **Wahrle et al. (2004)** - ABCA1 required for normal CNS ApoE levels - J Biol Chem
5. **Shi et al. (2017)** - ApoE4 exacerbates tau neurodegeneration - Nature
6. **Koldamova et al. (2003)** - Oxysterols induce ABCA1 expression - J Biol Chem
7. **Pfrieger (2003)** - Cholesterol homeostasis in CNS neurons - Cell Mol Life Sci
8. **LaDu et al. (1994)** - Isoform-specific binding of ApoE to Abeta - J Biol Chem
9. **Lund et al. (2003)** - Cholesterol 24-hydroxylase knockout - J Biol Chem
10. **Lin et al. (2018)** - APOE4 molecular alterations in iPSC brain cells - Neuron

---

## 13. Implementation Notes

### Compartment Volumes (Elbert convention)
- Neuron: 0.5 L
- Astrocyte: 0.2 L
- Microglia: 0.05 L
- BrainISF: 0.28 L
- CSF: 0.14 L
- BBB: 0.001 L
- Plasma: 3.0 L

### Initial Conditions Strategy
1. Start from Elbert reference model values where available
2. Use published CSF biomarker values for ISF species
3. Run to steady state with E3/E3 parameters first
4. Then switch to E4/E4 parameters and observe trajectory

### Sensitivity Analysis Priorities
1. isoform_clearance_scale -- strongest effect on Abeta levels
2. k_ABCA1_efflux -- rate-limiting for ApoE lipidation
3. Kd_LXR -- determines oxysterol sensitivity
4. fraction_APP_raft baseline -- sets amyloidogenic/non-amyloidogenic balance
5. k_tau_phos_base * f_ApoE_neuroinflam -- tau pathology driver

---

*Generated 2026-02-24 for antimony_bootstrap lipid/ApoE module development*
