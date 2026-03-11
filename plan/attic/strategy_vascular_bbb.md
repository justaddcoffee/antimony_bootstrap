# Strategy: Vascular and Blood-Brain Barrier Mechanisms for Alzheimer's ODE Models

## Overview

This document outlines the approach for extracting vascular and blood-brain barrier (BBB) mechanisms from Alzheimer's disease literature and encoding them as ODE-based Antimony modules. The BBB is central to Alzheimer's pathology: it regulates Abeta clearance from the brain, controls peripheral immune cell entry, and its breakdown accelerates disease progression.

All modules described below follow the antimony_bootstrap schema (ModuleSpec, ReactionSpec, ParameterSpec) and use the Elbert naming convention `{species}_{compartment}`.

---

## 1. Compartment Architecture

Vascular/BBB modules require a multi-compartment framework. The following compartments are needed beyond those already defined (BrainISF, CSF, Plasma):

| Compartment | Description | Estimated Volume |
|---|---|---|
| BrainISF | Brain interstitial fluid | 0.25 L |
| CSF | Cerebrospinal fluid | 0.14 L |
| Plasma | Blood plasma | 3.0 L |
| BrainParenchyma | Brain tissue (cells) | 1.0 L |
| PVS | Perivascular space (glymphatic) | 0.01-0.05 L |
| BrainEndothelium | Luminal + abluminal endothelial membranes | ~0.002 L (conceptual) |
| VascularWall | Cerebrovascular smooth muscle / basement membrane | ~0.01 L |

**Key principle**: Transport between BrainISF and Plasma always passes through the BBB (BrainEndothelium). Some models simplify by using direct ISF-to-Plasma rate constants (as in the existing abeta_production module); the vascular modules should provide the mechanistic detail behind those lumped rates.

---

## 2. BBB Permeability Changes

### Biology
BBB permeability increases with age and accelerates in AD. Tight junction proteins (claudin-5, occludin, ZO-1) are degraded by matrix metalloproteinases (MMP-2, MMP-9), reactive oxygen species, and inflammatory cytokines (TNF-alpha, IL-1beta).

### ODE Formulation

Model BBB permeability as a dynamic parameter `P_BBB` that modulates passive transport:

```
J_passive = P_BBB * SA_BBB * (C_Plasma - C_BrainISF)
```

Where:
- `P_BBB` = permeability coefficient (cm/s), dynamic variable
- `SA_BBB` = surface area of BBB (~150-200 cm^2/g brain, ~20 m^2 total)
- `C_Plasma`, `C_BrainISF` = concentrations in respective compartments

**Permeability degradation** can be modeled as:

```
dP_BBB/dt = k_BBB_baseline_repair - k_BBB_MMP_degrade * MMP9_BrainISF - k_BBB_ROS_degrade * ROS_BrainISF
```

### Rate Types
- Passive transport: **BDF** (bidirectional flow) or **custom_conc_per_time**
- Permeability dynamics: **custom_amt_per_time** (P_BBB is a unitless or cm/s parameter)

### Parameter Ranges

| Parameter | Value | Units | Source |
|---|---|---|---|
| P_BBB (baseline, small molecules) | 1e-7 to 1e-6 | cm/s | Pardridge 2005 (PMID:16081038) |
| P_BBB (albumin, intact BBB) | ~1e-9 | cm/s | Abbott 2010 (PMID:20816856) |
| P_BBB (albumin, AD BBB) | ~1e-7 | cm/s | Montagne 2017 (PMID:28106076) |
| SA_BBB | 100-200 | cm^2/g brain | Pardridge 2007 (PMID:17217990) |
| k_BBB_baseline_repair | ~0.01 | 1/hr | Estimated from TJ turnover (~days) |
| k_BBB_MMP_degrade | ~0.1 | 1/(nM*hr) | Bell 2012 (PMID:22406537) |

---

## 3. Abeta Transport Across BBB: LRP1 and RAGE

### Biology
- **LRP1 (Low-density lipoprotein receptor-related protein 1)**: Major efflux receptor. Transports Abeta from brain to blood. Expression decreases with age and AD. Located on abluminal (brain-facing) endothelial membrane.
- **RAGE (Receptor for Advanced Glycation End-products)**: Influx receptor. Transports Abeta from blood to brain. Expression increases in AD. Located on luminal (blood-facing) endothelial membrane.

### ODE Formulation

**LRP1-mediated efflux (brain to blood):**
```
J_LRP1 = Vmax_LRP1 * AB42_BrainISF / (Km_LRP1 + AB42_BrainISF) * fLRP1
```
Michaelis-Menten kinetics. `fLRP1` is a fractional activity term (0-1) that decreases with disease.

**RAGE-mediated influx (blood to brain):**
```
J_RAGE = Vmax_RAGE * AB42_Plasma / (Km_RAGE + AB42_Plasma) * fRAGE
```
`fRAGE` increases with disease (RAGE upregulation).

**Receptor dynamics (optional, adds detail):**
```
dLRP1_Endo/dt = k_LRP1_synth - k_LRP1_deg * LRP1_Endo - k_LRP1_ox_deg * ROS_BrainISF * LRP1_Endo
dRAGE_Endo/dt = k_RAGE_synth_basal + k_RAGE_upregulate * AB42_BrainISF - k_RAGE_deg * RAGE_Endo
```

### Rate Types
- LRP1 transport: **custom_conc_per_time** (Michaelis-Menten, multiply by V_BrainISF for amount)
- RAGE transport: **custom_conc_per_time** (Michaelis-Menten, multiply by V_Plasma for amount)
- Receptor dynamics: **custom_amt_per_time**

### Parameter Ranges

| Parameter | Value | Units | Confidence | Source |
|---|---|---|---|---|
| Vmax_LRP1 | 0.5-5.0 | nmol/hr | estimated | Deane 2004 (PMID:15313568), Elbert model |
| Km_LRP1 | 5-50 | nM | estimated | Deane 2004 (PMID:15313568) |
| Vmax_RAGE | 0.05-0.5 | nmol/hr | estimated | Deane 2003 (PMID:12805289) |
| Km_RAGE | 50-100 | nM | estimated | Deane 2003 (PMID:12805289) |
| k_LRP1_synth | 0.01 | nmol/hr | assumed | Estimated from protein turnover |
| k_LRP1_deg | 0.02 | 1/hr | assumed | Half-life ~35 hr |
| k_RAGE_synth_basal | 0.005 | nmol/hr | assumed | Lower basal than LRP1 |
| k_RAGE_upregulate | 0.001 | 1/(nM*hr) | assumed | AB42-dependent upregulation |

### Module Species

Following Elbert naming convention:
- `AB42_BrainISF`, `AB42_Plasma` (shared with abeta_production module)
- `LRP1_BrainEndothelium` (LRP1 receptor amount at endothelium)
- `RAGE_BrainEndothelium` (RAGE receptor amount at endothelium)

---

## 4. Cerebral Amyloid Angiopathy (CAA)

### Biology
Abeta (especially Abeta40) accumulates in cerebrovascular walls, particularly in smooth muscle cells and basement membranes. CAA impairs perivascular drainage, causes vessel wall weakening, and contributes to microhemorrhages. CAA is present in >80% of AD brains.

### ODE Formulation

**Abeta deposition in vascular wall:**
```
J_CAA_deposit = k_CAA_deposit * AB42_PVS * (1 - AB42_VascularWall / CAA_capacity)
```
Saturable deposition with carrying capacity.

**CAA-induced vascular damage:**
```
dVascularIntegrity/dt = k_repair_vasc - k_CAA_damage * AB42_VascularWall
```

**Impaired perivascular drainage due to CAA:**
```
k_PVS_drain_effective = k_PVS_drain_baseline * (1 - alpha_CAA * AB42_VascularWall / CAA_capacity)
```

### Rate Types
- Deposition: **custom_conc_per_time** (saturable kinetics)
- Vascular integrity: **custom_amt_per_time** (assignment rule for effective drainage)

### Parameter Ranges

| Parameter | Value | Units | Source |
|---|---|---|---|
| k_CAA_deposit | 0.001-0.01 | 1/hr | Estimated from pathology timecourse |
| CAA_capacity | 100-1000 | nmol | Assumed, tissue capacity |
| k_CAA_damage | 1e-4 | 1/(nmol*hr) | Assumed |
| k_PVS_drain_baseline | 0.05-0.2 | 1/hr | Iliff 2012 (PMID:22896675) |
| alpha_CAA | 0.5-0.9 | dimensionless | Weller 2009 (PMID:19714646) |

### Module Species
- `AB40_PVS` (Abeta40 in perivascular space, preferentially deposits)
- `AB42_PVS` (Abeta42 in perivascular space)
- `AB40_VascularWall`, `AB42_VascularWall` (deposited amyloid)
- `VascularIntegrity_VascularWall` (dimensionless, 0-1)

---

## 5. Neurovascular Coupling

### Biology
Neurovascular coupling links neuronal activity to local blood flow via astrocyte signaling, endothelial NO production, and pericyte contractility. In AD, neurovascular coupling is impaired, reducing cerebral blood flow and oxygen/glucose delivery.

### ODE Formulation

**Simplified CBF model:**
```
CBF = CBF_baseline * (1 + alpha_NVC * NeuronalActivity_BrainParenchyma) * PericyteFraction * NO_BrainEndothelium / (K_NO + NO_BrainEndothelium)
```

**Impact on transport**: CBF modulates delivery of oxygen/glucose and clearance of metabolites. Scale transport rate constants by CBF/CBF_baseline:

```
k_transport_effective = k_transport_baseline * (CBF / CBF_baseline)
```

### Rate Types
- Assignment rules for CBF and effective transport rates
- NVC itself is best represented as an **algebraic rule** rather than a reaction

### Parameter Ranges

| Parameter | Value | Units | Source |
|---|---|---|---|
| CBF_baseline | 50-60 | mL/100g/min | Iadecola 2004 (PMID:15500301) |
| alpha_NVC | 0.3-0.5 | dimensionless | Estimated |
| K_NO | 1-10 | nM | Estimated from NO physiology |
| CBF_AD_reduction | 20-30% | fraction | Iturria-Medina 2016 (PMID:27075150) |

### Notes
Neurovascular coupling is often approximated with algebraic rules rather than explicit reactions. This module may best be implemented as a set of RuleSpec entries that compute effective transport parameters used by other modules.

---

## 6. Pericyte Loss

### Biology
Pericytes wrap around capillaries and maintain BBB integrity. In AD, pericyte coverage decreases 25-50% (measured by PDGFRbeta). Loss correlates with BBB breakdown, capillary regression, and reduced CBF. Pericyte loss is driven by Abeta toxicity and PDGF signaling disruption.

### ODE Formulation

```
dPericyte_BrainEndothelium/dt = k_pericyte_recruit * PDGFB_BrainEndothelium / (K_PDGFB + PDGFB_BrainEndothelium) - k_pericyte_death_basal * Pericyte_BrainEndothelium - k_pericyte_AB_tox * AB42_BrainISF * Pericyte_BrainEndothelium
```

**Pericyte coverage modulates BBB integrity:**
```
BBB_integrity_factor = Pericyte_BrainEndothelium / Pericyte_baseline
P_BBB = P_BBB_baseline / BBB_integrity_factor
```

### Rate Types
- Pericyte dynamics: **custom_conc_per_time**
- BBB modulation: algebraic rule (RuleSpec)

### Parameter Ranges

| Parameter | Value | Units | Source |
|---|---|---|---|
| k_pericyte_recruit | 0.01 | 1/hr | Assumed (slow turnover, weeks-months) |
| K_PDGFB | 1-10 | nM | Estimated |
| k_pericyte_death_basal | 0.001 | 1/hr | Assumed (half-life ~months) |
| k_pericyte_AB_tox | 1e-4 | 1/(nM*hr) | Sagare 2013 (PMID:23602566) |
| Pericyte_baseline | 1.0 | dimensionless (normalized) | Reference state |

---

## 7. Tight Junction Degradation

### Biology
Tight junction (TJ) proteins (claudin-5, occludin, ZO-1) form the paracellular seal of the BBB. MMPs (especially MMP-2, MMP-9) cleave TJ proteins. Inflammatory cytokines (TNF-alpha, IL-1beta) downregulate TJ expression. Oxidative stress disrupts TJ assembly.

### ODE Formulation

```
dTJ_BrainEndothelium/dt = k_TJ_synth * Pericyte_BrainEndothelium - k_TJ_deg_basal * TJ_BrainEndothelium - k_TJ_MMP_deg * MMP9_BrainISF * TJ_BrainEndothelium - k_TJ_TNF_deg * TNFa_BrainISF * TJ_BrainEndothelium
```

**TJ level modulates paracellular permeability:**
```
P_paracellular = P_para_max * (1 - TJ_BrainEndothelium / TJ_baseline)^n_Hill
```

### Rate Types
- TJ dynamics: **custom_conc_per_time**
- Permeability rule: RuleSpec (algebraic)

### Parameter Ranges

| Parameter | Value | Units | Source |
|---|---|---|---|
| k_TJ_synth | 0.01-0.05 | 1/hr | Assumed (protein turnover ~12-24 hr) |
| k_TJ_deg_basal | 0.03 | 1/hr | Assumed (half-life ~24 hr) |
| k_TJ_MMP_deg | 0.01-0.1 | 1/(nM*hr) | Yang 2007 (PMID:17360908) |
| k_TJ_TNF_deg | 0.005-0.05 | 1/(nM*hr) | Aslam 2012 (PMID:22427375) |
| P_para_max | 1e-5 | cm/s | Estimated maximum paracellular P |
| n_Hill | 2-4 | dimensionless | Assumed, cooperativity |

---

## 8. Peripheral Immune Cell Infiltration

### Biology
In AD, BBB breakdown and endothelial activation allow peripheral immune cells (monocytes, T cells, neutrophils) to infiltrate the brain. Chemokines (MCP-1/CCL2, CXCL10) and adhesion molecules (ICAM-1, VCAM-1) mediate this process. Infiltrating monocytes can differentiate into macrophages that phagocytose Abeta or exacerbate inflammation.

### ODE Formulation

**Monocyte transmigration:**
```
J_monocyte_infiltration = k_infiltrate * Monocyte_Plasma * ICAM1_BrainEndothelium * P_BBB_factor
```

Where `P_BBB_factor` reflects BBB integrity (higher when BBB is disrupted).

**Infiltrated monocyte dynamics:**
```
dMacrophage_BrainISF/dt = J_monocyte_infiltration - k_macro_death * Macrophage_BrainISF
```

**Chemokine-driven recruitment:**
```
ICAM1_BrainEndothelium = ICAM1_basal * (1 + k_ICAM_TNF * TNFa_BrainISF + k_ICAM_AB * AB42_BrainISF)
```

### Rate Types
- Infiltration: **custom_amt_per_time** (flux between compartments)
- Macrophage dynamics: **MA** (first-order death)
- ICAM1 upregulation: RuleSpec

### Parameter Ranges

| Parameter | Value | Units | Source |
|---|---|---|---|
| k_infiltrate | 1e-6 to 1e-4 | 1/hr | Estimated from in vivo data |
| k_macro_death | 0.01-0.05 | 1/hr | Half-life 14-70 hr in tissue |
| k_ICAM_TNF | 0.1-1.0 | 1/nM | Grammas 2011 (PMID:21575724) |
| k_ICAM_AB | 0.01-0.1 | 1/nM | Estimated |
| ICAM1_basal | 1.0 | normalized | Reference state |
| Monocyte_Plasma (initial) | 300-600 | cells/uL -> normalized | Physiological range |

### Module Species
- `Monocyte_Plasma` (circulating monocytes)
- `Macrophage_BrainISF` (infiltrated monocytes/macrophages)
- `ICAM1_BrainEndothelium` (adhesion molecule)
- `TNFa_BrainISF` (shared with neuroinflammation module)

---

## 9. CSF/ISF Drainage and the Glymphatic System

### Biology
The glymphatic system drives CSF through perivascular spaces (PVS) into brain ISF via AQP4 channels on astrocyte endfeet, facilitating bulk clearance of solutes including Abeta. Drainage occurs preferentially during sleep. Impairment in AD is linked to AQP4 mislocalization, reactive astrogliosis, and CAA-mediated perivascular obstruction.

### ODE Formulation

**Glymphatic inflow (CSF to ISF via PVS):**
```
J_glymph_in = k_glymph_in * AB42_CSF * AQP4_activity * sleep_factor
```

**ISF to PVS bulk flow (clearance):**
```
J_ISF_PVS = k_ISF_PVS * AB42_BrainISF
```

**PVS to cervical lymph drainage:**
```
J_PVS_lymph = k_PVS_lymph * AB42_PVS * (1 - CAA_obstruction_factor)
```

**AQP4 activity (decreases with astrogliosis):**
```
AQP4_activity = AQP4_baseline * (1 - alpha_gliosis * ReactiveAstrocyte_BrainParenchyma / Astrocyte_total)
```

**Sleep modulation:**
```
sleep_factor = 1.0 + delta_sleep * sleep_state   // sleep_state: 0=awake, 1=sleep
```
(For steady-state models, use time-averaged value ~1.3 assuming 8hr sleep)

### Rate Types
- Glymphatic flows: **UDF** (unidirectional flow, no volume multiplication) for simple; **custom_conc_per_time** for modulated forms
- AQP4 and sleep: RuleSpec (algebraic)

### Parameter Ranges

| Parameter | Value | Units | Source |
|---|---|---|---|
| k_glymph_in | 0.01-0.05 | 1/hr | Iliff 2012 (PMID:22896675) |
| k_ISF_PVS | 0.02-0.1 | 1/hr | Iliff 2012, Mestre 2018 (PMID:30263252) |
| k_PVS_lymph | 0.05-0.2 | 1/hr | Ma 2017 (PMID:28925353) |
| AQP4_baseline | 1.0 | normalized | Reference |
| alpha_gliosis | 0.3-0.7 | dimensionless | Iliff 2014 (PMID:24695709) |
| delta_sleep | 0.6 | dimensionless | Xie 2013 (PMID:24136970): 60% increase during sleep |
| CAA_obstruction_factor | 0-0.9 | dimensionless | Depends on CAA load |

### Module Species
- `AB42_PVS`, `AB40_PVS` (perivascular space Abeta)
- `AQP4_BrainEndothelium` (aquaporin-4, functional amount)
- `ReactiveAstrocyte_BrainParenchyma` (shared with glia module)

---

## 10. Module Decomposition Plan

The vascular/BBB mechanisms should be split into the following antimony_bootstrap modules:

### Module 1: `bbb_transport` (Priority: HIGH)
Core BBB Abeta transport via LRP1 and RAGE.
- Compartments: BrainISF, Plasma, BrainEndothelium
- Key reactions: LRP1 efflux, RAGE influx, passive permeability
- Connects to: abeta_production (shares AB42_BrainISF, AB42_Plasma)

### Module 2: `bbb_integrity` (Priority: HIGH)
BBB structural components and their regulation.
- Species: TJ_BrainEndothelium, Pericyte_BrainEndothelium, P_BBB
- Key reactions: TJ synthesis/degradation, pericyte dynamics
- Connects to: bbb_transport (modulates permeability), neuroinflammation (receives MMP, TNFa)

### Module 3: `cerebral_amyloid_angiopathy` (Priority: MEDIUM)
CAA deposition and vascular damage.
- Compartments: PVS, VascularWall
- Key reactions: Abeta deposition, vascular integrity loss
- Connects to: glymphatic_drainage (impairs PVS flow), bbb_integrity (vascular damage)

### Module 4: `glymphatic_drainage` (Priority: MEDIUM)
CSF/ISF/PVS drainage and glymphatic clearance.
- Compartments: CSF, BrainISF, PVS
- Key reactions: glymphatic inflow, ISF-to-PVS flow, PVS-to-lymph drainage
- Connects to: abeta_production (alternative clearance path), CAA (obstruction), glia (AQP4)

### Module 5: `immune_infiltration` (Priority: LOW-MEDIUM)
Peripheral immune cell entry through disrupted BBB.
- Key reactions: monocyte transmigration, macrophage dynamics, ICAM1 regulation
- Connects to: bbb_integrity (BBB disruption enables entry), neuroinflammation (cytokine drivers)

### Module 6: `neurovascular_coupling` (Priority: LOW)
CBF regulation and its impact on transport.
- Primarily algebraic rules modulating transport rates
- Connects to: pericyte loss (reduced CBF), metabolic modules (O2/glucose delivery)

---

## 11. Integration with Existing Modules

### Shared Species (cross-module)
These species appear in multiple modules and must use consistent naming:

| Species | Defined In | Used By |
|---|---|---|
| AB42_BrainISF | abeta_production | bbb_transport, glymphatic_drainage, bbb_integrity |
| AB42_Plasma | abeta_production | bbb_transport |
| AB42_CSF | abeta_production | glymphatic_drainage |
| TNFa_BrainISF | neuroinflammation (TBD) | bbb_integrity, immune_infiltration |
| MMP9_BrainISF | neuroinflammation (TBD) | bbb_integrity |
| ROS_BrainISF | oxidative_stress (TBD) | bbb_integrity |

### Shared Compartments
Add to model.yaml `shared_compartments`:
- BrainEndothelium (volume: 0.002 L)
- PVS (volume: 0.02 L)
- VascularWall (volume: 0.01 L)
- BrainParenchyma (volume: 1.0 L)

### Parameter Consistency
When the same clearance pathway appears in both a simplified module (abeta_production's `k_AB42_ISF_CSF`) and a detailed module (glymphatic_drainage), the detailed module should reproduce the lumped rate at steady state. Validate by checking that total Abeta clearance rates match between simplified and detailed configurations.

---

## 12. Implementation Order

1. **bbb_transport** -- Highest impact. Replaces the lumped ISF-to-Plasma rates in abeta_production with mechanistic LRP1/RAGE transport. Start here.
2. **bbb_integrity** -- Enables disease-state BBB breakdown. Depends on having inflammation species as inputs.
3. **glymphatic_drainage** -- Important alternative clearance pathway. Can be built in parallel with bbb_transport.
4. **cerebral_amyloid_angiopathy** -- Requires PVS species from glymphatic module.
5. **immune_infiltration** -- Requires both BBB integrity and inflammation modules.
6. **neurovascular_coupling** -- Mostly algebraic rules; add last as a modulator.

---

## 13. Key Literature References

| PMID | Authors | Topic |
|---|---|---|
| 15313568 | Deane et al. 2004 | LRP1 mediates Abeta clearance across BBB |
| 12805289 | Deane et al. 2003 | RAGE mediates Abeta influx across BBB |
| 22896675 | Iliff et al. 2012 | Glymphatic pathway for brain waste clearance |
| 24136970 | Xie et al. 2013 | Sleep drives metabolite clearance via glymphatic |
| 28106076 | Montagne et al. 2017 | BBB breakdown in aging human brain |
| 22406537 | Bell et al. 2012 | Pericyte degeneration leads to BBB breakdown |
| 23602566 | Sagare et al. 2013 | Pericyte loss accelerates AD pathology |
| 16081038 | Pardridge 2005 | BBB permeability and drug delivery |
| 15500301 | Iadecola 2004 | Neurovascular regulation and AD |
| 27075150 | Iturria-Medina et al. 2016 | Vascular dysregulation as early AD event |
| 19714646 | Weller et al. 2009 | Perivascular drainage and CAA |
| 30263252 | Mestre et al. 2018 | AQP4 and glymphatic flow dynamics |
| 28925353 | Ma et al. 2017 | CSF outflow pathways |
| 24695709 | Iliff et al. 2014 | AQP4 mislocalization impairs glymphatic in AD |
| 17360908 | Yang et al. 2007 | MMP-9 degrades tight junctions |
| 22427375 | Aslam et al. 2012 | TNF-alpha disrupts BBB tight junctions |
| 21575724 | Grammas 2011 | Neurovascular inflammation in AD |
| 22120143 | Zlokovic 2011 | Neurovascular pathways to neurodegeneration (review) |
| 21068834 | Bell et al. 2010 | SRF/myocardin regulate Abeta clearance |

---

## 14. Modeling Decisions and Trade-offs

### Lumped vs. Mechanistic
- **Start lumped** for initial model: use effective rate constants for BBB transport (as in current abeta_production module)
- **Add mechanism** incrementally: replace lumped rates with LRP1/RAGE Michaelis-Menten when parameterization data is available
- **Never add complexity without data**: if a sub-mechanism cannot be parameterized, keep it lumped

### Units Convention
- Concentrations: nM (nanomolar) for soluble species
- Amounts: nmol for total species in compartment
- Volumes: L (liters)
- Rates: 1/hr for first-order; nmol/hr for zero-order; 1/(nM*hr) for second-order
- Time: hours (consistent with existing modules)

### Steady-State Validation
Each module should have a known steady-state that can be analytically verified:
- bbb_transport: at steady state, LRP1 efflux + degradation = production + RAGE influx
- glymphatic: at steady state, ISF-to-PVS outflow = glymphatic inflow + local production
- bbb_integrity: at steady state, TJ synthesis = TJ degradation (no inflammation)

### Sensitivity Analysis Priorities
Focus parameter sensitivity analysis on:
1. Vmax_LRP1 and Km_LRP1 (dominant Abeta clearance pathway)
2. k_glymph_in and AQP4_activity (glymphatic clearance, sleep-dependent)
3. k_TJ_MMP_deg (BBB breakdown rate)
4. k_CAA_deposit (CAA progression rate)
