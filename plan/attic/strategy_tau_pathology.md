# Strategy: Tau Pathology Mechanisms for Antimony ODE Models

**Date**: 2026-02-24

**Objective**: Extract tau pathology mechanisms from Alzheimer's literature and encode them as ODE-based Antimony modules compatible with the antimony_bootstrap schema (ModuleSpec YAML). This document covers five core sub-mechanisms, their rate law forms, parameter ranges, compartmental structure, and mapping to the Elbert naming conventions.

---

## 1. Compartmental Structure

Tau pathology spans intracellular neuronal compartments, the extracellular space, and CSF/plasma for biomarker transport. The following compartments are recommended, consistent with Elbert_Esguerra conventions:

| Compartment | Volume (L) | Notes |
|---|---|---|
| `Neuron` | 0.5 | Intracellular neuronal cytoplasm (aggregate across brain regions) |
| `BrainISF` | 0.25 | Brain interstitial fluid (shared with abeta_production module) |
| `CSF` | 0.14 | Cerebrospinal fluid (shared) |
| `Plasma` | 3.0 | Blood plasma (shared) |
| `Microtubule` | 0.1 | Virtual compartment representing microtubule-bound fraction |

For regional spreading models, subdivide `Neuron` into region-specific compartments:
- `Neuron_EC` (entorhinal cortex) -- Braak stage I-II
- `Neuron_Hippo` (hippocampus) -- Braak stage III-IV
- `Neuron_Cortex` (neocortex) -- Braak stage V-VI

Each regional compartment would have its own volume parameter (e.g., `V_Neuron_EC = 0.05 L`).

---

## 2. Tau Phosphorylation by Kinases (GSK3-beta, CDK5)

### Biological Summary

Tau hyperphosphorylation is a critical early event in tauopathy. GSK3-beta and CDK5/p25 are the primary kinases. Phosphatases (PP2A primarily) counterbalance phosphorylation. Hyperphosphorylated tau (p-tau) detaches from microtubules and is prone to aggregation.

### Species (Elbert naming convention)

- `Tau_Neuron` -- unphosphorylated tau monomer
- `pTau_Neuron` -- hyperphosphorylated tau monomer
- `GSK3b_Neuron` -- active GSK3-beta
- `GSK3b_inactive_Neuron` -- inactive (phosphorylated Ser9) GSK3-beta
- `CDK5_Neuron` -- CDK5/p25 active complex
- `PP2A_Neuron` -- protein phosphatase 2A

### Reactions and Rate Laws

#### 2.1 Tau phosphorylation by GSK3-beta
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[Tau_Neuron]`
- **Products**: `[pTau_Neuron]`
- **Rate law**: `Vmax_GSK3b * Tau_Neuron / (Km_GSK3b + Tau_Neuron) * (GSK3b_Neuron / GSK3b_total)`
- **Parameters**:
  - `Vmax_GSK3b`: 0.1-1.0 nM/hr (estimated from in vitro kinase assays; Hanger et al., 2009, PMID:19737999)
  - `Km_GSK3b`: 2-20 uM (Michaelis constant for tau substrate; Noble et al., 2005, PMID:16186107)
- **Rationale**: Michaelis-Menten captures saturation kinetics of enzymatic phosphorylation. The fraction of active GSK3b modulates the effective rate.

#### 2.2 Tau phosphorylation by CDK5/p25
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[Tau_Neuron]`
- **Products**: `[pTau_Neuron]`
- **Rate law**: `Vmax_CDK5 * Tau_Neuron / (Km_CDK5 + Tau_Neuron) * CDK5_Neuron`
- **Parameters**:
  - `Vmax_CDK5`: 0.05-0.5 nM/hr (Patrick et al., 1999, PMID:10517638)
  - `Km_CDK5`: 5-30 uM

#### 2.3 Tau dephosphorylation by PP2A
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[pTau_Neuron]`
- **Products**: `[Tau_Neuron]`
- **Rate law**: `Vmax_PP2A * pTau_Neuron / (Km_PP2A + pTau_Neuron) * PP2A_Neuron`
- **Parameters**:
  - `Vmax_PP2A`: 0.5-5.0 nM/hr (Liu et al., 2005, PMID:15668399)
  - `Km_PP2A`: 1-15 uM
- **Note**: PP2A activity is reduced ~50% in AD brain (Gong et al., 1993, PMID:8226771). Model this by reducing `PP2A_Neuron` or `Vmax_PP2A`.

#### 2.4 GSK3-beta activation/inactivation
- **Type**: `RMA` (reversible mass action)
- **Forward**: `GSK3b_inactive_Neuron -> GSK3b_Neuron` (activation via dephosphorylation at Ser9)
- **Reverse**: `GSK3b_Neuron -> GSK3b_inactive_Neuron` (inactivation via Akt/insulin signaling)
- **Parameters**:
  - `k_GSK3b_act`: 0.01-0.1 1/hr
  - `k_GSK3b_inact`: 0.05-0.5 1/hr (Akt-dependent; Cross et al., 1995, PMID:8524413)

### Recommended Module: `tau_phosphorylation`

This module encodes the phosphorylation/dephosphorylation cycle. It couples to the insulin signaling module via GSK3b activation state and to the aggregation module via pTau output.

---

## 3. Tau Aggregation (Monomers -> Oligomers -> PHF -> NFTs)

### Biological Summary

Hyperphosphorylated tau aggregates through a nucleation-elongation mechanism: monomers form soluble oligomers, which template into paired helical filaments (PHFs), and PHFs deposit as neurofibrillary tangles (NFTs). This follows nucleated polymerization kinetics similar to amyloid-beta aggregation but with distinct rate constants.

### Species

- `pTau_Neuron` -- hyperphosphorylated tau monomers (input from phosphorylation module)
- `TauOligo_Neuron` -- soluble tau oligomers (toxic, 2-50 mers)
- `PHF_Neuron` -- paired helical filaments
- `NFT_Neuron` -- neurofibrillary tangles (insoluble, essentially irreversible)

### Reactions and Rate Laws

#### 3.1 Oligomer nucleation
- **Type**: `custom_conc_per_time` (second-order nucleation)
- **Reactants**: `[pTau_Neuron]`
- **Products**: `[TauOligo_Neuron]`
- **Rate law**: `k_nuc_tau * pTau_Neuron^n_nuc`
- **Parameters**:
  - `k_nuc_tau`: 1e-6 to 1e-4 (concentration^(1-n))/hr (Congdon & Bhatt, 2018; adapted from ThT assay kinetics)
  - `n_nuc`: 2 (dimerization as minimal nucleus; Friedhoff et al., 1998, PMID:9836620)
- **Note**: The Hill-type exponent captures cooperative nucleation. In practice, n=2 is most common in tau literature.

#### 3.2 Oligomer elongation to PHF
- **Type**: `custom_conc_per_time`
- **Reactants**: `[TauOligo_Neuron, pTau_Neuron]`
- **Products**: `[PHF_Neuron]`
- **Rate law**: `k_elong_tau * TauOligo_Neuron * pTau_Neuron`
- **Parameters**:
  - `k_elong_tau`: 1e-4 to 1e-2 1/(nM*hr) (estimated from in vitro fibrillization; von Bergen et al., 2001, PMID:11524434)

#### 3.3 PHF maturation to NFT
- **Type**: `MA` (first-order, irreversible)
- **Reactants**: `[PHF_Neuron]`
- **Products**: `[NFT_Neuron]`
- **Rate law**: `k_NFT_mat * PHF_Neuron * V_Neuron`
- **Parameters**:
  - `k_NFT_mat`: 1e-4 to 1e-2 1/hr (slow maturation; estimated from post-mortem Braak staging timelines over 10-20 years)

#### 3.4 Oligomer disaggregation (reversible)
- **Type**: `MA`
- **Reactants**: `[TauOligo_Neuron]`
- **Products**: `[pTau_Neuron]`
- **Rate law**: `k_disagg_tau * TauOligo_Neuron * V_Neuron`
- **Parameters**:
  - `k_disagg_tau`: 0.001-0.01 1/hr (oligomers are metastable)

### Alternative: Smoluchowski Coagulation Simplified

For a more biophysical approach, use a simplified Smoluchowski model with two size classes:
- `rate_oligomerization = k_smol * pTau_Neuron^2` (bimolecular)
- `rate_elongation = k_smol_elong * TauOligo_Neuron * pTau_Neuron`

This is equivalent to the nucleation-elongation model above but explicitly roots in coagulation theory (Pallitto & Murphy, 2001, PMID:11292344).

### Recommended Module: `tau_aggregation`

---

## 4. Tau Spreading Between Brain Regions

### Biological Summary

Tau pathology spreads in a stereotypical pattern (Braak stages) via prion-like templated seeding. Tau seeds are released into the extracellular space, taken up by connected neurons, and template misfolding of endogenous tau. Key evidence: Braak staging, injection models (Clavaguera et al., 2009, PMID:19855036; de Calignon et al., 2012, PMID:22286176).

### Species (regional)

- `TauSeed_BrainISF` -- extracellular tau seeds (released oligomers)
- `pTau_Neuron_EC`, `pTau_Neuron_Hippo`, `pTau_Neuron_Cortex` -- regional p-tau
- `NFT_Neuron_EC`, `NFT_Neuron_Hippo`, `NFT_Neuron_Cortex` -- regional NFT burden

### Reactions and Rate Laws

#### 4.1 Tau seed release
- **Type**: `UDF` (unidirectional flow)
- **Reactants**: `[TauOligo_Neuron_EC]`
- **Products**: `[TauSeed_BrainISF]`
- **Rate law**: `k_tau_release * TauOligo_Neuron_EC`
- **Parameters**:
  - `k_tau_release`: 0.001-0.01 1/hr (Pooler et al., 2013, PMID:23463507)

#### 4.2 Tau seed uptake and templated seeding (EC -> Hippo)
- **Type**: `custom_conc_per_time`
- **Reactants**: `[TauSeed_BrainISF, Tau_Neuron_Hippo]`
- **Products**: `[pTau_Neuron_Hippo]`
- **Rate law**: `k_tau_seed * TauSeed_BrainISF * Tau_Neuron_Hippo * connectivity_EC_Hippo`
- **Parameters**:
  - `k_tau_seed`: 1e-5 to 1e-3 1/(nM*hr)
  - `connectivity_EC_Hippo`: 1.0 (dimensionless connectivity weight; from Allen Brain Atlas connectome data)

#### 4.3 Tau seed uptake and templated seeding (Hippo -> Cortex)
- Same form as 4.2 with `connectivity_Hippo_Cortex`: 0.5 (weaker connectivity)

#### 4.4 Tau seed clearance from ISF
- **Type**: `MA`
- **Reactants**: `[TauSeed_BrainISF]`
- **Products**: `[]`
- **Rate law**: `k_tau_seed_clear * TauSeed_BrainISF * V_BrainISF`
- **Parameters**:
  - `k_tau_seed_clear`: 0.05-0.2 1/hr (glymphatic clearance; Iliff et al., 2012, PMID:22896675)

### Network Diffusion Model Alternative

For a more abstract approach, use the Network Diffusion Model (Raj et al., 2012, PMID:22327886):
- `d(Tau_region_i)/dt = -beta * sum_j(L_ij * Tau_region_j)`
- Where `L_ij` is the graph Laplacian of structural connectivity
- `beta`: 0.01-0.1 1/yr (diffusion rate along white matter tracts)

This is harder to encode in standard Antimony reactions but can be implemented as assignment rules or custom rate expressions with explicit connectivity matrices.

### Recommended Module: `tau_spreading`

Start with a 3-region model (EC, Hippo, Cortex) using explicit seed release/uptake reactions. This is more mechanistic and fits the Antimony reaction framework naturally.

---

## 5. Microtubule Binding and Unbinding

### Biological Summary

Normal tau stabilizes microtubules. Hyperphosphorylation reduces tau-microtubule binding affinity by 3-10 fold, leading to microtubule destabilization, impaired axonal transport, and neurodegeneration.

### Species

- `Tau_Neuron` -- free unphosphorylated tau
- `pTau_Neuron` -- free phosphorylated tau
- `TauMT_Microtubule` -- tau bound to microtubules
- `pTauMT_Microtubule` -- p-tau weakly bound to microtubules
- `MT_stable_Neuron` -- stable microtubules
- `MT_unstable_Neuron` -- destabilized microtubules

### Reactions and Rate Laws

#### 5.1 Normal tau binding to microtubules
- **Type**: `RMA` (reversible mass action)
- **Forward**: `Tau_Neuron -> TauMT_Microtubule`
- **Reverse**: `TauMT_Microtubule -> Tau_Neuron`
- **Parameters**:
  - `k_tau_MT_on`: 0.1-1.0 1/(nM*hr) (Gustke et al., 1994, PMID:8075991)
  - `k_tau_MT_off`: 0.01-0.1 1/hr (Kd ~ 100 nM for normal tau; Butner & Bhatt, 2011, PMID:21451745)

#### 5.2 Phospho-tau binding to microtubules (weakened)
- **Type**: `RMA`
- **Forward**: `pTau_Neuron -> pTauMT_Microtubule`
- **Reverse**: `pTauMT_Microtubule -> pTau_Neuron`
- **Parameters**:
  - `k_pTau_MT_on`: 0.01-0.1 1/(nM*hr) (3-10x reduced vs normal tau)
  - `k_pTau_MT_off`: 0.1-1.0 1/hr (3-10x increased vs normal tau; Kd ~ 1 uM for p-tau)

#### 5.3 Microtubule destabilization
- **Type**: `custom_conc_per_time`
- **Reactants**: `[MT_stable_Neuron]`
- **Products**: `[MT_unstable_Neuron]`
- **Rate law**: `k_MT_destab * MT_stable_Neuron * (1 - TauMT_Microtubule / (TauMT_Microtubule + Kd_MT_stab))`
- **Parameters**:
  - `k_MT_destab`: 0.001-0.01 1/hr
  - `Kd_MT_stab`: half-maximal tau concentration for MT stabilization
- **Note**: When bound tau drops below a threshold, microtubule stability decreases. This is a Hill-like response.

#### 5.4 Microtubule restabilization
- **Type**: `MA`
- **Reactants**: `[MT_unstable_Neuron]`
- **Products**: `[MT_stable_Neuron]`
- **Rate law**: `k_MT_restab * MT_unstable_Neuron * V_Neuron`
- **Parameters**:
  - `k_MT_restab`: 0.005-0.05 1/hr

### Recommended Module: `tau_microtubule`

This module provides the functional readout of tau pathology on neuronal health. It couples to the phosphorylation module (pTau availability) and to a neurodegeneration module (MT instability -> impaired transport -> cell death).

---

## 6. Tau Clearance (Proteasome and Autophagy)

### Biological Summary

Tau is cleared by two primary pathways:
1. **Ubiquitin-proteasome system (UPS)**: Degrades soluble monomeric tau and some oligomeric tau. Impaired by tau aggregates.
2. **Autophagy-lysosomal pathway (ALP)**: Degrades larger aggregates (oligomers, PHFs) via macroautophagy. Key in aggregate clearance.

Both pathways become dysfunctional in AD, creating a vicious cycle where aggregates impair clearance, promoting further aggregation.

### Species

- `Tau_Neuron`, `pTau_Neuron` -- monomeric tau (UPS substrates)
- `TauOligo_Neuron`, `PHF_Neuron` -- aggregated tau (ALP substrates)
- `UPS_Neuron` -- proteasome capacity (abstract, dimensionless or nM equivalent)
- `ALP_Neuron` -- autophagy capacity

### Reactions and Rate Laws

#### 6.1 Proteasomal degradation of monomeric tau
- **Type**: `custom_conc_per_time` (Michaelis-Menten with competitive inhibition by aggregates)
- **Reactants**: `[Tau_Neuron]`
- **Products**: `[]`
- **Rate law**: `Vmax_UPS_tau * Tau_Neuron / (Km_UPS_tau * (1 + TauOligo_Neuron/Ki_UPS_oligo) + Tau_Neuron)`
- **Parameters**:
  - `Vmax_UPS_tau`: 0.1-1.0 nM/hr
  - `Km_UPS_tau`: 5-50 nM
  - `Ki_UPS_oligo`: 10-100 nM (inhibition constant; oligomers impair proteasome; Keck et al., 2003, PMID:12686575)

#### 6.2 Proteasomal degradation of phospho-tau
- Same form as 6.1 but with reduced Vmax (~50% of normal tau) since p-tau is a poorer UPS substrate (David et al., 2002, PMID:12027439)

#### 6.3 Autophagy degradation of tau oligomers
- **Type**: `custom_conc_per_time` (Michaelis-Menten)
- **Reactants**: `[TauOligo_Neuron]`
- **Products**: `[]`
- **Rate law**: `Vmax_ALP_oligo * TauOligo_Neuron / (Km_ALP_oligo + TauOligo_Neuron) * ALP_Neuron`
- **Parameters**:
  - `Vmax_ALP_oligo`: 0.01-0.1 nM/hr (slower than UPS; Rubinsztein et al., 2005, PMID:16186256)
  - `Km_ALP_oligo`: 10-100 nM

#### 6.4 Autophagy degradation of PHF
- **Type**: `custom_conc_per_time`
- **Reactants**: `[PHF_Neuron]`
- **Products**: `[]`
- **Rate law**: `Vmax_ALP_PHF * PHF_Neuron / (Km_ALP_PHF + PHF_Neuron) * ALP_Neuron`
- **Parameters**:
  - `Vmax_ALP_PHF`: 0.001-0.01 nM/hr (PHF clearance is very slow)
  - `Km_ALP_PHF`: 50-500 nM

#### 6.5 UPS impairment by aggregates (feedback)
- **Type**: `custom_conc_per_time`
- **Reactants**: `[UPS_Neuron]`
- **Products**: `[]` (degradation of capacity)
- **Rate law**: `k_UPS_impair * UPS_Neuron * TauOligo_Neuron / (Ki_UPS_impair + TauOligo_Neuron)`
- **Parameters**:
  - `k_UPS_impair`: 0.001-0.01 1/hr
  - `Ki_UPS_impair`: 50-200 nM

#### 6.6 ALP impairment (optional, age-dependent)
- Model as a slow linear decline: `ALP_Neuron' = -k_ALP_decline * ALP_Neuron`
- `k_ALP_decline`: 1e-5 to 1e-4 1/hr (decades-scale decline)

### Recommended Module: `tau_clearance`

---

## 7. Cross-Module Coupling Points

The five tau modules interconnect at these species:

```
tau_phosphorylation
  OUTPUT: pTau_Neuron ──────> tau_aggregation (INPUT)
  OUTPUT: pTau_Neuron ──────> tau_microtubule (INPUT)
  INPUT:  GSK3b_Neuron <───── insulin_signaling module (future)

tau_aggregation
  INPUT:  pTau_Neuron <────── tau_phosphorylation
  OUTPUT: TauOligo_Neuron ──> tau_spreading (INPUT)
  OUTPUT: TauOligo_Neuron ──> tau_clearance (INPUT)
  OUTPUT: PHF_Neuron ───────> tau_clearance (INPUT)
  OUTPUT: NFT_Neuron ───────> neurodegeneration module (future)

tau_spreading
  INPUT:  TauOligo_Neuron <── tau_aggregation (per region)
  OUTPUT: pTau_Neuron_region > tau_aggregation (per region, seed-templated)

tau_microtubule
  INPUT:  Tau_Neuron <──────── tau_phosphorylation
  INPUT:  pTau_Neuron <─────── tau_phosphorylation
  OUTPUT: MT_unstable_Neuron > neurodegeneration module (future)

tau_clearance
  INPUT:  Tau_Neuron <──────── tau_phosphorylation
  INPUT:  pTau_Neuron <─────── tau_phosphorylation
  INPUT:  TauOligo_Neuron <─── tau_aggregation
  INPUT:  PHF_Neuron <──────── tau_aggregation
  FEEDBACK: UPS impairment <── tau_aggregation (TauOligo)
```

### Shared Parameters Across Modules

These should be declared in `model.yaml` under `shared_parameters`:
- `k_tau_synth`: basal tau synthesis rate (0.01-0.1 nM/hr)
- `tau_total_init`: initial total tau concentration (~100-500 nM in neurons)

### Amyloid-Tau Crosstalk (Future)

AB42 oligomers promote tau phosphorylation via GSK3b activation. This creates the amyloid cascade -> tau pathway link:
- `k_AB42_GSK3b_act * AB42_BrainISF` added to GSK3b activation rate
- Encodes the "amyloid hypothesis" trigger for tauopathy

---

## 8. Implementation Priority

Recommended build order for incremental model construction:

| Priority | Module | Complexity | Dependencies |
|---|---|---|---|
| 1 | `tau_phosphorylation` | Medium | None (standalone kinase/phosphatase cycle) |
| 2 | `tau_aggregation` | Medium | `tau_phosphorylation` (pTau output) |
| 3 | `tau_clearance` | Medium | `tau_phosphorylation` + `tau_aggregation` |
| 4 | `tau_microtubule` | Low | `tau_phosphorylation` |
| 5 | `tau_spreading` | High | All above + regional compartments |

### Validation Strategy Per Module

1. **Unit test**: Each module in isolation with fixed inputs for upstream species
2. **Steady-state check**: Healthy baseline should reach stable steady state
3. **Perturbation test**: Increase GSK3b activity -> expect pTau increase -> aggregation increase
4. **Time-scale check**: NFT formation should occur over years, not hours

---

## 9. Key Literature References

| PMID | Authors | Year | Relevance |
|---|---|---|---|
| 19737999 | Hanger et al. | 2009 | Tau phosphorylation sites and kinase specificity |
| 16186107 | Noble et al. | 2005 | GSK3 as therapeutic target; kinase parameters |
| 10517638 | Patrick et al. | 1999 | CDK5/p25 in neurodegeneration |
| 15668399 | Liu et al. | 2005 | PP2A role in tau dephosphorylation |
| 9836620 | Friedhoff et al. | 1998 | Tau fibrillization kinetics in vitro |
| 11524434 | von Bergen et al. | 2001 | PHF assembly mechanism |
| 19855036 | Clavaguera et al. | 2009 | Prion-like tau spreading in vivo |
| 22286176 | de Calignon et al. | 2012 | Trans-synaptic tau spreading |
| 22327886 | Raj et al. | 2012 | Network diffusion model of tau spreading |
| 23463507 | Pooler et al. | 2013 | Activity-dependent tau release |
| 8075991 | Gustke et al. | 1994 | Tau-microtubule binding domains |
| 12686575 | Keck et al. | 2003 | Proteasome inhibition by tau aggregates |
| 16186256 | Rubinsztein et al. | 2005 | Autophagy in neurodegeneration |
| 22896675 | Iliff et al. | 2012 | Glymphatic clearance system |
| 8226771 | Gong et al. | 1993 | PP2A reduction in AD brain |

---

## 10. Parameter Summary Table

| Parameter | Range | Units | Module | Confidence |
|---|---|---|---|---|
| `Vmax_GSK3b` | 0.1-1.0 | nM/hr | phosphorylation | estimated |
| `Km_GSK3b` | 2-20 | uM | phosphorylation | estimated |
| `Vmax_CDK5` | 0.05-0.5 | nM/hr | phosphorylation | estimated |
| `Vmax_PP2A` | 0.5-5.0 | nM/hr | phosphorylation | estimated |
| `k_GSK3b_act` | 0.01-0.1 | 1/hr | phosphorylation | assumed |
| `k_GSK3b_inact` | 0.05-0.5 | 1/hr | phosphorylation | assumed |
| `k_nuc_tau` | 1e-6 to 1e-4 | conc^-1/hr | aggregation | estimated |
| `n_nuc` | 2 | dimensionless | aggregation | measured |
| `k_elong_tau` | 1e-4 to 1e-2 | 1/(nM*hr) | aggregation | estimated |
| `k_NFT_mat` | 1e-4 to 1e-2 | 1/hr | aggregation | assumed |
| `k_tau_release` | 0.001-0.01 | 1/hr | spreading | estimated |
| `k_tau_seed` | 1e-5 to 1e-3 | 1/(nM*hr) | spreading | assumed |
| `k_tau_MT_on` | 0.1-1.0 | 1/(nM*hr) | microtubule | estimated |
| `k_tau_MT_off` | 0.01-0.1 | 1/hr | microtubule | estimated |
| `Vmax_UPS_tau` | 0.1-1.0 | nM/hr | clearance | estimated |
| `Vmax_ALP_oligo` | 0.01-0.1 | nM/hr | clearance | estimated |
| `Ki_UPS_oligo` | 10-100 | nM | clearance | assumed |
