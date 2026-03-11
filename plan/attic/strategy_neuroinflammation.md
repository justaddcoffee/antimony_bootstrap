# Strategy: Neuroinflammation Mechanisms for Alzheimer's Antimony Models

## 1. Overview

Neuroinflammation is a central driver of Alzheimer's disease (AD) pathology, encompassing microglial activation, astrocyte reactivity, cytokine signaling, complement activation, and their downstream effects on amyloid-beta clearance and synaptic integrity. This document outlines strategies for translating these mechanisms into ODE-based Antimony models compatible with the antimony_bootstrap framework.

### Modeling Philosophy

- Each mechanism becomes a **ModuleSpec** YAML with compartments, species, reactions, and parameters.
- Species follow Elbert naming: {species}_{compartment} (e.g., TNFa_BrainISF, Microglia_DAM_Brain).
- Rate laws use the established type system (MA, RMA, UDF, custom_conc_per_time, etc.).
- Parameters require literature citations with confidence levels (measured/estimated/assumed).
- Modules compose via shared species at assembly time.

---

## 2. Microglial Activation States

### 2.1 Biological Background

Microglia exist in multiple functional states relevant to AD:

- **Homeostatic (M0)**: Surveillance state, expressing P2RY12, TMEM119, CX3CR1. Low cytokine output, baseline phagocytosis.
- **Disease-Associated Microglia (DAM)**: Identified by Keren-Shaul et al. (2017, Cell 169:1276). Upregulate TREM2, APOE, LPL, CST7. Enhanced phagocytosis of plaques. Two-stage activation: DAM Stage 1 (TREM2-independent) then DAM Stage 2 (TREM2-dependent).
- **Inflammatory/Activated (M1-like)**: Produce TNFa, IL-1b, IL-6, ROS. Neurotoxic phenotype driven by NF-kB signaling. Triggered by oligomers, TLR4/CD14 engagement.
- **Anti-inflammatory (M2-like)**: Produce IL-10, TGFb, Arg1. Tissue repair, debris clearance. Note: the M1/M2 dichotomy is an oversimplification; in practice, use a continuum or multi-state model.

### 2.2 ODE Model Structure

Model microglia as cell populations transitioning between discrete states. This is analogous to compartmental epidemiological models.

    Species:
      Microglia_M0_Brain            # Homeostatic microglia (cells)
      Microglia_DAM1_Brain          # DAM Stage 1 (cells)
      Microglia_DAM2_Brain          # DAM Stage 2 (cells)
      Microglia_Inflammatory_Brain  # Pro-inflammatory (cells)

### 2.3 State Transition Rate Laws

**Transition: M0 -> DAM1** (triggered by plaques, TREM2-independent)

    rate_type: custom_conc_per_time
    rate_equation: k_M0_DAM1 * Microglia_M0_Brain * AB42_plaque_Brain / (Km_AB_DAM1 + AB42_plaque_Brain)

This uses a saturating (Michaelis-Menten-like) form because DAM activation saturates at high plaque load.

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_M0_DAM1 | 0.01 | 0.001-0.1 | 1/day | Keren-Shaul 2017, estimated from scRNA-seq kinetics |
| Km_AB_DAM1 | 50 | 10-200 | nM (equiv) | Estimated |

**Transition: DAM1 -> DAM2** (TREM2-dependent)

    rate_type: custom_conc_per_time
    rate_equation: k_DAM1_DAM2 * Microglia_DAM1_Brain * TREM2_active_Brain / (Km_TREM2 + TREM2_active_Brain)

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_DAM1_DAM2 | 0.005 | 0.001-0.05 | 1/day | Estimated from Nugent 2020 |
| Km_TREM2 | 10 | 1-50 | nM | Estimated |

**Transition: M0 -> Inflammatory** (triggered by oligomers + cytokines)

    rate_type: custom_conc_per_time
    rate_equation: k_M0_Inf * Microglia_M0_Brain * (AB42_olig_BrainISF / (Km_AB_inf + AB42_olig_BrainISF)) * (1 + amp_TNF * TNFa_BrainISF / (Km_TNF_act + TNFa_BrainISF))

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_M0_Inf | 0.02 | 0.005-0.1 | 1/day | Estimated |
| Km_AB_inf | 10 | 1-100 | nM | Estimated |
| amp_TNF | 2.0 | 1-5 | dimensionless | Estimated |
| Km_TNF_act | 0.1 | 0.01-1 | nM | Heneka 2015 (PMID: 25656850) |

**Reversion: Inflammatory -> M0** (resolution)

    rate_type: custom_conc_per_time
    rate_equation: k_Inf_M0 * Microglia_Inflammatory_Brain * IL10_BrainISF / (Km_IL10_res + IL10_BrainISF)

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_Inf_M0 | 0.005 | 0.001-0.05 | 1/day | Estimated |
| Km_IL10_res | 0.05 | 0.01-0.5 | nM | Estimated |

### 2.4 Microglial Proliferation and Death

    # Proliferation (CSF1R-dependent)
    rate_type: MA
    rate_equation: k_prolif * Microglia_total_Brain * (1 - Microglia_total_Brain / K_max_microglia)

    # Death/Apoptosis
    rate_type: MA
    rate_equation: k_death_microglia * Microglia_Inflammatory_Brain

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_prolif | 0.001 | 1/day | Askew 2017 (PMID: 28187747), ~0.5-2% renewal/year in human |
| K_max_microglia | 1.0 | relative | Normalized carrying capacity |
| k_death_microglia | 0.003 | 1/day | Estimated, ~1% turnover/day in disease |

---

## 3. Astrocyte Reactivity

### 3.1 Biological Background

Reactive astrocytes in AD fall into two broad categories (Liddelow et al., 2017, Nature 541:481):

- **A1 (neurotoxic)**: Induced by microglial TNFa + IL-1a + C1q. Lose normal functions (synaptogenesis support, phagocytosis). Upregulate complement C3.
- **A2 (neuroprotective)**: Induced by ischemia/injury signals. Upregulate neurotrophic factors (BDNF, GDNF).
- **Homeostatic (A0)**: Normal astrocyte functions -- glutamate uptake, BBB maintenance, metabolic support.

### 3.2 ODE Model Structure

    Species:
      Astrocyte_A0_Brain        # Homeostatic
      Astrocyte_A1_Brain        # Neurotoxic reactive
      Astrocyte_A2_Brain        # Neuroprotective reactive

### 3.3 State Transitions

**A0 -> A1** (driven by microglial signals: TNFa + IL-1b + C1q)

    rate_type: custom_conc_per_time
    rate_equation: k_A0_A1 * Astrocyte_A0_Brain * TNFa_BrainISF * IL1b_BrainISF * C1q_BrainISF / ((Km_TNF_A1 + TNFa_BrainISF) * (Km_IL1b_A1 + IL1b_BrainISF) * (Km_C1q_A1 + C1q_BrainISF))

This triple-saturation form captures the requirement for combinatorial signaling (all three signals needed for full A1 polarization).

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_A0_A1 | 0.015 | 0.005-0.05 | 1/day | Estimated from Liddelow 2017 |
| Km_TNF_A1 | 0.1 | 0.01-1 | nM | Estimated |
| Km_IL1b_A1 | 0.05 | 0.01-0.5 | nM | Estimated |
| Km_C1q_A1 | 5 | 1-50 | nM | Estimated |

**A1 astrocytes produce C3** (complement amplification loop)

    rate_type: custom_conc_per_time
    rate_equation: k_A1_C3 * Astrocyte_A1_Brain

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_A1_C3 | 0.5 | nM/day/cell_equiv | Lian 2015, estimated |

### 3.4 Astrocyte Functional Outputs

Astrocyte state affects glutamate clearance and synaptic support:

    # Glutamate uptake (reduced in A1 state)
    rate_type: custom_conc_per_time
    rate_equation: (Vmax_glu_uptake * Astrocyte_A0_Brain + 0.3 * Vmax_glu_uptake * Astrocyte_A1_Brain) * Glutamate_BrainISF / (Km_glu + Glutamate_BrainISF)

---

## 4. Cytokine Networks

### 4.1 Core Cytokine Species

    Species:
      TNFa_BrainISF       # Tumor necrosis factor alpha (nM)
      IL1b_BrainISF       # Interleukin-1 beta (nM)
      IL6_BrainISF        # Interleukin-6 (nM)
      IL10_BrainISF       # Interleukin-10 (nM)
      TGFb_BrainISF       # Transforming growth factor beta (nM)

### 4.2 Cytokine Production

**TNFa production by inflammatory microglia**

    rate_type: custom_conc_per_time
    rate_equation: k_prod_TNFa * Microglia_Inflammatory_Brain * (1 + amp_AB_TNF * AB42_olig_BrainISF / (Km_AB_TNF + AB42_olig_BrainISF))

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_prod_TNFa | 0.5 | 0.1-5 | nM/day/cell_equiv | Heneka 2015; Vom Berg 2012 (PMID: 22509247) |
| amp_AB_TNF | 3.0 | 1-10 | dimensionless | Estimated |
| Km_AB_TNF | 5 | 1-50 | nM | Estimated |

**IL-1b production** (NLRP3 inflammasome-dependent)

    rate_type: custom_conc_per_time
    rate_equation: k_prod_IL1b * Microglia_Inflammatory_Brain * NLRP3_active_Brain / (Km_NLRP3 + NLRP3_active_Brain)

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_prod_IL1b | 0.3 | 0.05-3 | nM/day/cell_equiv | Halle 2008 (PMID: 18830242) |
| Km_NLRP3 | 0.5 | 0.1-5 | nM | Estimated |

**IL-6 production** (by both microglia and astrocytes)

    rate_type: custom_conc_per_time
    rate_equation: k_prod_IL6_mic * Microglia_Inflammatory_Brain + k_prod_IL6_ast * Astrocyte_A1_Brain

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_prod_IL6_mic | 0.2 | nM/day/cell_equiv | Estimated |
| k_prod_IL6_ast | 0.1 | nM/day/cell_equiv | Estimated |

**IL-10 production** (anti-inflammatory feedback)

    rate_type: custom_conc_per_time
    rate_equation: k_prod_IL10 * Microglia_DAM2_Brain + k_prod_IL10_TGF * TGFb_BrainISF / (Km_TGF_IL10 + TGFb_BrainISF)

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_prod_IL10 | 0.1 | nM/day/cell_equiv | Estimated |
| k_prod_IL10_TGF | 0.05 | nM/day | Estimated |

**TGFb production** (by multiple cell types, critical for homeostasis)

    rate_type: custom_conc_per_time
    rate_equation: k_prod_TGFb_baseline + k_prod_TGFb_A2 * Astrocyte_A2_Brain

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_prod_TGFb_baseline | 0.01 | nM/day | Tesseur 2006 (PMID: 16434498) |
| k_prod_TGFb_A2 | 0.05 | nM/day/cell_equiv | Estimated |

### 4.3 Cytokine Degradation

All cytokines have first-order degradation:

    rate_type: MA
    rate_equation: k_deg_{cytokine} * {cytokine}_BrainISF

| Cytokine | k_deg (1/day) | Half-life | Source |
|----------|---------------|-----------|--------|
| TNFa | 33 | ~30 min | Bhatt 2013 (PMID: 23583617) |
| IL-1b | 17 | ~1 hr | Estimated from in vivo clearance |
| IL-6 | 10 | ~1.5 hr | Estimated |
| IL-10 | 8 | ~2 hr | Estimated |
| TGFb | 5 | ~3 hr | Estimated |

### 4.4 Key Feedback Loops

1. **Positive feedback**: TNFa -> NF-kB -> more TNFa (autocrine amplification). Model with Hill function: k_auto_TNF * TNFa^n / (Km_auto^n + TNFa^n), n=2.
2. **Negative feedback**: IL-10 suppresses TNFa and IL-1b production. Model as inhibition term: 1 / (1 + IL10_BrainISF / Ki_IL10).
3. **Cross-regulation**: TGFb promotes M0 reversion, IL-6 promotes inflammatory state via STAT3.

---

## 5. Complement Cascade

### 5.1 Key Species

    Species:
      C1q_BrainISF         # Complement C1q (nM)
      C3_BrainISF          # Complement C3 (nM)
      C3a_BrainISF         # Anaphylatoxin C3a (nM)
      C3b_BrainISF         # Opsonin C3b (nM)
      iC3b_BrainISF        # Inactivated C3b (nM)
      C3b_AB_plaque_Brain  # C3b opsonized on plaques

### 5.2 Complement Activation

**C1q binding to plaques** (classical pathway initiation)

    rate_type: RMA
    rate_equation_fwd: k_C1q_bind * C1q_BrainISF * AB42_plaque_Brain
    rate_equation_rev: k_C1q_unbind * C1q_AB_plaque_Brain

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_C1q_bind | 0.01 | 1/(nM*day) | Rogers 1992 (PMID: 1373228); Webster 2000 |
| k_C1q_unbind | 0.5 | 1/day | Estimated |

**C3 cleavage** (activated by C1q-bound complexes)

    rate_type: custom_conc_per_time
    rate_equation: k_C3_cleave * C3_BrainISF * C1q_AB_plaque_Brain / (Km_C3_cleave + C3_BrainISF)

Produces both C3a (anaphylatoxin, pro-inflammatory) and C3b (opsonin).

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_C3_cleave | 0.1 | 1/day | Estimated from Fonseca 2004 (PMID: 15329385) |
| Km_C3_cleave | 100 | nM | Estimated |

**C3b opsonization of plaques**

    rate_type: MA
    rate_equation: k_C3b_opsonize * C3b_BrainISF * AB42_plaque_Brain

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_C3b_opsonize | 0.005 | 1/(nM*day) | Estimated |

**C3b inactivation to iC3b** (by Factor H and Factor I)

    rate_type: MA
    rate_equation: k_iC3b * C3b_BrainISF

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_iC3b | 5 | 1/day | Estimated from serum half-life |

### 5.3 Complement-Driven Synapse Elimination

C1q and C3 tag synapses for elimination (eat-me signals):

    rate_type: custom_conc_per_time
    rate_equation: k_complement_tag * C1q_BrainISF * C3b_BrainISF * Synapses_Brain / ((Km_C1q_syn + C1q_BrainISF) * (Km_C3b_syn + C3b_BrainISF))

This is the Stevens/Bhatt complement-mediated synapse loss pathway (Hong 2016, Science 352:712).

---

## 6. TREM2 Signaling

### 6.1 Biological Background

TREM2 (Triggering Receptor Expressed on Myeloid cells 2) is a key AD risk gene. It:
- Binds lipids, APOE, oligomers on damaged neurons
- Signals through DAP12/TYROBP -> SYK -> PI3K -> mTOR
- Required for DAM Stage 2 transition
- Promotes phagocytosis and metabolic fitness
- Cleaved by ADAM10/17 to produce soluble TREM2 (sTREM2, a biomarker)

### 6.2 TREM2 Model

    Species:
      TREM2_surface_Microglia    # Membrane-bound TREM2 (relative units)
      sTREM2_BrainISF            # Soluble TREM2 (nM, CSF biomarker)
      TREM2_active_Brain         # Ligand-engaged TREM2 signaling complex

**TREM2 activation by ligands** (oligomers, APOE on damaged neurons)

    rate_type: custom_conc_per_time
    rate_equation: k_TREM2_act * TREM2_surface_Microglia * (AB42_olig_BrainISF + APOE_lipid_BrainISF) / (Km_TREM2_lig + AB42_olig_BrainISF + APOE_lipid_BrainISF)

| Parameter | Value | Range | Units | Source |
|-----------|-------|-------|-------|--------|
| k_TREM2_act | 0.1 | 0.01-1 | 1/day | Estimated from Zhao 2018 (PMID: 30049709) |
| Km_TREM2_lig | 20 | 5-100 | nM | Estimated |

**TREM2 shedding** (ADAM10/17 cleavage, produces sTREM2)

    rate_type: MA
    rate_equation: k_TREM2_shed * TREM2_surface_Microglia

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_TREM2_shed | 0.5 | 1/day | Estimated, sTREM2 half-life ~4 hr in CSF |

**sTREM2 clearance**

    rate_type: MA
    rate_equation: k_deg_sTREM2 * sTREM2_BrainISF

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_deg_sTREM2 | 4 | 1/day | Estimated, CSF sTREM2 half-life ~4 hr |

### 6.3 TREM2 Downstream Effects

TREM2 signaling modulates:
1. **DAM transition**: DAM1 -> DAM2 (see Section 2.3)
2. **Phagocytic capacity**: multiplicative factor on phagocytosis rate
3. **Microglial survival**: anti-apoptotic via mTOR/Bcl2
4. **Metabolic fitness**: mitochondrial function, lipid metabolism

---

## 7. Phagocytosis of Amyloid-Beta

### 7.1 Mechanisms

Multiple clearance routes:
- **Microglial phagocytosis**: Receptor-mediated (TREM2, CD36, SR-A, CR3) uptake
- **Astrocyte phagocytosis**: Lower capacity than microglia, via MEGF10/MERTK
- **Enzymatic degradation**: Neprilysin, IDE (modeled elsewhere in amyloid module)

### 7.2 Microglial Phagocytosis Rate Law

    rate_type: custom_conc_per_time
    rate_equation: Vmax_phago * f_phago_state * AB42_plaque_Brain * (1 + amp_C3b * C3b_AB_plaque_Brain / (Km_C3b_phago + C3b_AB_plaque_Brain)) / (Km_phago + AB42_plaque_Brain)

Where f_phago_state is a function of microglial state:

    # Assignment rule for phagocytic capacity
    f_phago_state = phi_M0 * Microglia_M0_Brain + phi_DAM2 * Microglia_DAM2_Brain + phi_Inf * Microglia_Inflammatory_Brain

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| Vmax_phago | 1.0 | nM/day | Estimated, calibrated to clearance rates |
| Km_phago | 100 | nM | Estimated |
| phi_M0 | 0.3 | dimensionless | Baseline phagocytosis |
| phi_DAM2 | 1.0 | dimensionless | DAM2 = maximal phagocytosis |
| phi_Inf | 0.1 | dimensionless | Inflammatory microglia have reduced phagocytosis |
| amp_C3b | 2.0 | dimensionless | C3b opsonization enhances uptake |
| Km_C3b_phago | 10 | nM | Estimated |

### 7.3 Important Consideration: Phagocytosis Saturation

At high plaque loads, phagocytosis saturates and can become overwhelmed. The Michaelis-Menten form naturally captures this. Additionally, inflammatory microglia shift from phagocytic to cytokine-secreting mode (captured by low phi_Inf).

---

## 8. Synaptic Pruning and Loss

### 8.1 Mechanisms of Synapse Loss

1. **Complement-mediated**: C1q/C3 tag -> microglial engulfment (Section 5.3)
2. **Cytokine-mediated**: TNFa disrupts LTP, IL-1b impairs synaptic plasticity
3. **Oligomer-mediated**: Direct synaptotoxicity (modeled in amyloid module)
4. **Astrocyte dysfunction**: A1 astrocytes fail to support synapses, secrete toxic factors

### 8.2 Synapse Model

    Species:
      Synapses_Brain              # Total synaptic density (relative, healthy=1.0)
      Synapses_tagged_Brain       # Complement-tagged synapses

**Complement tagging** (see Section 5.3)

**Microglial engulfment of tagged synapses**

    rate_type: custom_conc_per_time
    rate_equation: k_syn_engulf * Synapses_tagged_Brain * (Microglia_DAM2_Brain + f_inf_engulf * Microglia_Inflammatory_Brain)

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_syn_engulf | 0.01 | 1/day/cell_equiv | Hong 2016 (PMID: 27338780) |
| f_inf_engulf | 0.5 | dimensionless | Inflammatory microglia also prune, less selectively |

**Cytokine-mediated synapse weakening**

    rate_type: custom_conc_per_time
    rate_equation: k_syn_TNF * Synapses_Brain * TNFa_BrainISF / (Km_TNF_syn + TNFa_BrainISF) + k_syn_IL1b * Synapses_Brain * IL1b_BrainISF / (Km_IL1b_syn + IL1b_BrainISF)

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_syn_TNF | 0.005 | 1/day | Estimated, Bhatt 2013 |
| Km_TNF_syn | 0.5 | nM | Estimated |
| k_syn_IL1b | 0.003 | 1/day | Estimated |
| Km_IL1b_syn | 0.2 | nM | Estimated |

**Synapse repair/formation** (neuroplasticity, BDNF-dependent)

    rate_type: custom_conc_per_time
    rate_equation: k_syn_repair * (1 - Synapses_Brain) * Astrocyte_A0_Brain / (Astrocyte_A0_Brain + Astrocyte_A1_Brain + Astrocyte_A2_Brain)

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| k_syn_repair | 0.002 | 1/day | Estimated, slow repair in adult brain |

---

## 9. Module Decomposition Plan

### Proposed Modules

| Module | Key Species | Interfaces |
|--------|-------------|------------|
| neuroinflam_microglia.yaml | Microglia states (M0, DAM1, DAM2, Inflammatory) | AB42 species, cytokines, TREM2 |
| neuroinflam_astrocyte.yaml | Astrocyte states (A0, A1, A2) | Cytokines, C1q, C3, Glutamate |
| neuroinflam_cytokines.yaml | TNFa, IL-1b, IL-6, IL-10, TGFb | Microglia states, astrocyte states |
| neuroinflam_complement.yaml | C1q, C3, C3a, C3b, iC3b | AB42 plaques, synapses, microglia |
| neuroinflam_trem2.yaml | TREM2 surface, sTREM2, TREM2 active | Microglia DAM, AB42, APOE |
| neuroinflam_phagocytosis.yaml | Phagocytosis fluxes | Microglia states, AB42, C3b |
| neuroinflam_synaptic.yaml | Synapses, tagged synapses | Complement, cytokines, astrocytes |

### Shared Compartments

- Brain (volume ~1400 mL, or normalized)
- BrainISF (interstitial fluid, ~280 mL, or ~20% of brain volume)

### Interface Species (shared across modules)

These species appear in multiple modules and serve as coupling points:
- AB42_olig_BrainISF, AB42_plaque_Brain (from amyloid module)
- TNFa_BrainISF, IL1b_BrainISF, IL10_BrainISF, TGFb_BrainISF
- C1q_BrainISF, C3b_BrainISF
- Microglia_M0_Brain, Microglia_DAM2_Brain, Microglia_Inflammatory_Brain
- Synapses_Brain

---

## 10. Parameter Confidence and Calibration Strategy

### Confidence Levels

| Level | Description | Pct of Parameters |
|-------|-------------|-------------------|
| **measured** | Direct experimental measurement from literature | ~10% |
| **estimated** | Derived from related measurements or constrained by data | ~40% |
| **assumed** | Order-of-magnitude guess, needs calibration | ~50% |

### Key Literature Sources

1. **Heneka et al. (2015)** PMID: 25656850 -- Neuroinflammation in AD review
2. **Keren-Shaul et al. (2017)** PMID: 28602351 -- DAM identification
3. **Liddelow et al. (2017)** PMID: 28099414 -- A1/A2 astrocyte classification
4. **Hong et al. (2016)** PMID: 27338780 -- Complement-mediated synapse pruning
5. **Halle et al. (2008)** PMID: 18830242 -- NLRP3 inflammasome and amyloid
6. **Vom Berg et al. (2012)** PMID: 22509247 -- TNFa signaling in AD
7. **Rogers et al. (1992)** PMID: 1373228 -- Complement activation by amyloid
8. **Fonseca et al. (2004)** PMID: 15329385 -- C1q and neurodegeneration
9. **Zhao et al. (2018)** PMID: 30049709 -- TREM2 biology
10. **Tesseur et al. (2006)** PMID: 16434498 -- TGFb in AD
11. **Askew et al. (2017)** PMID: 28187747 -- Microglial turnover
12. **Elbert and Bhatt (Elbert_Esguerra model)** -- Reference Antimony model for naming and structure

### Calibration Approach

1. **Steady-state constraints**: Healthy-state cytokine concentrations should match CSF measurements (TNFa ~1-5 pg/mL, IL-6 ~2-10 pg/mL).
2. **Time-course data**: Microglial activation kinetics from mouse models (e.g., 5xFAD, APP/PS1). DAM emergence at ~6 months in mice corresponds to approximately years 50-60 in human.
3. **Sensitivity analysis**: Identify most influential parameters, prioritize for literature search.
4. **Biomarker validation**: sTREM2 CSF levels, complement protein levels, cytokine ratios.

---

## 11. Implementation Notes

### Rate Law Selection Guide

| Mechanism | Recommended Rate Type | Rationale |
|-----------|----------------------|-----------|
| Cell state transitions | custom_conc_per_time with saturation | Transitions saturate; depend on signal concentration |
| Cytokine production | custom_conc_per_time | Multi-signal integration, Hill functions for cooperativity |
| Cytokine degradation | MA | First-order clearance |
| Receptor binding | RMA | Reversible binding kinetics |
| Phagocytosis | custom_conc_per_time with MM | Saturating, state-dependent |
| Complement cleavage | custom_conc_per_time with MM | Enzyme kinetics |

### Numerical Considerations

- **Stiff system**: Cytokine half-lives (minutes) vs. cell transitions (days) create stiffness. Use te.simulate() with appropriate solver (CVODE handles this well).
- **Initial conditions**: Start from healthy steady state, perturb with amyloid input.
- **Units**: Keep concentrations in nM, time in days, volumes in mL for consistency with Elbert model.

### Potential Simplifications

If the full model is too complex for initial implementation:
1. Collapse DAM1/DAM2 into single DAM state
2. Use a single "inflammatory cytokine" species instead of individual cytokines
3. Omit NLRP3 intermediate, directly link amyloid to IL-1b production
4. Use A0/A1 only (drop A2)
5. Represent complement as single "complement activation" variable

---

## 12. Next Steps

1. **Build neuroinflam_microglia.yaml** first -- it is the central hub
2. **Build neuroinflam_cytokines.yaml** -- needed by microglia and astrocyte modules
3. **Build neuroinflam_complement.yaml** -- needed for phagocytosis and synapse modules
4. **Build remaining modules** in dependency order
5. **Validate each module individually** with just validate-modules
6. **Assemble with amyloid module** and run just qc
7. **Calibrate** against Elbert model outputs and literature time courses
