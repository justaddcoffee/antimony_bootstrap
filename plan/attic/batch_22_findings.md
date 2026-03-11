# Batch 22 Findings: Alzheimer's Disease Paper Analysis

**Batch**: 22 (86 papers from Secondary_Alzforum)
**PMC Range**: PMC3394933 – PMC3566780
**Date**: 2026-02-24

---

## 1. Papers with Quantitative/Mechanistic Data

### Tier 1: HIGH — Quantitative kinetic/clearance data directly modelable as ODEs

#### PMC3551275 — Paravascular (Glymphatic) Clearance of Amyloid-beta
**Title**: A Paravascular Pathway Facilitates CSF Flow Through the Brain Parenchyma and the Clearance of Interstitial Solutes, Including Amyloid β
**Key findings**:
- AQP4 knockout reduces interstitial solute clearance by ~70%
- AQP4 knockout reduces Aβ1-40 clearance by ~55%
- Clearance is bulk-flow dependent (not diffusion), as dextran-10 and mannitol clear at same rate
- 125I-Aβ1-40 clears faster than comparably sized dextran, suggesting receptor-mediated BBB efflux augments bulk flow
**Modelable**: YES — First-order clearance of Aβ from ISF via paravascular pathway, AQP4-modulated

#### PMC3493562 — ApoE Isoform-Dependent Aβ Oligomerization
**Title**: Apolipoprotein E, especially apolipoprotein E4, increases the oligomerization of amyloid β peptide
**Key findings**:
- Aβ oligomer levels in APOE4/4 AD brains are 2.7x higher than APOE3/3 brains (matched plaque burden)
- ApoE increases Aβ oligomers in isoform-dependent manner: E2 < E3 < E4
- ApoE4 slows Aβ clearance relative to E2 and E3 but has no effect on Aβ synthesis
- Half-life of Aβ in apoE knockout mice markedly decreased vs wild-type
**Modelable**: YES — ApoE-dependent modulation of Aβ oligomerization rate and Aβ clearance rate

#### PMC3433173 — ApoE Gene Dose Effect on Aβ Accumulation
**Title**: Reducing Human Apolipoprotein E Levels Attenuates Age-Dependent Aβ Accumulation
**Key findings**:
- Reducing apoE3 or apoE4 expression by 50% enables efficient Aβ clearance at 6 months
- At 12 months, one copy of apoE gene → significantly reduced Aβ levels vs two copies
- Gene dose-dependent effect on Aβ accumulation regardless of isoform
**Modelable**: YES — ApoE concentration-dependent Aβ accumulation (dose-response)

#### PMC3431439 — Aβ Oligomer → PrPC → Fyn → NMDA-R Signaling Cascade
**Title**: Alzheimer Amyloid-β Oligomer Bound to Post-Synaptic Prion Protein Activates Fyn to Impair Neurons
**Key findings**:
- Aβ oligomers bind PrPC at postsynaptic densities → activate Fyn kinase
- Fyn phosphorylates NR2B subunit of NMDA receptors
- Initial increase then loss of surface NMDA receptors
- Aβ-induced dendritic spine loss requires both PrPC and Fyn
**Modelable**: YES — Sequential signaling cascade: Aβ_oligo + PrPC → Fyn_active → pNR2B → NMDA-R internalization

#### PMC3528177 — Complement-Dependent Microglial Synaptic Pruning
**Title**: Microglia Sculpt Postnatal Neural Circuits in an Activity and Complement-Dependent Manner
**Key findings**:
- Microglia engulf presynaptic inputs via CR3/C3 phagocytic pathway
- Engulfment is neural activity-dependent
- Disrupting CR3/C3 signaling → sustained synaptic connectivity deficits
**Modelable**: YES — C3-tagged synapse elimination by microglia (relevant to AD complement activation)

### Tier 2: MEDIUM — Mechanistic pathways with some quantitative context

#### PMC3536811 — TREM2 and Inflammatory Response
**Title**: Attenuated Inflammatory Response in TREM2 Knock-Out Mice following Stroke
**Key findings**:
- TREM2 KO attenuates acute inflammatory cytokine response (TNF-α, IL-1β, IL-6)
- TREM2 expression greatly increases post-injury (qPCR)
- TREM2 involved in microglial phagocytosis of apoptotic debris
**Modelable**: Partially — TREM2-dependent microglial activation and cytokine production

#### PMC3463804 — Autophagy of Misfolded Proteins
**Title**: Autophagy and misfolded proteins in neurodegeneration
**Key findings**:
- Autophagy-lysosome pathway clears misfolded protein aggregates
- Impairment at different autophagy steps → different diseases
- Antioxidants can block autophagy (counterintuitive)
**Modelable**: Partially — Autophagy flux as clearance mechanism for aggregated proteins

#### PMC3501350 — Anti-ApoE Immunotherapy
**Title**: Anti-apoE immunotherapy inhibits amyloid accumulation
**Key findings**:
- Anti-ApoE antibody reduces amyloid deposition
- Enhances microglial response to Aβ plaques
**Modelable**: Partially — Therapeutic intervention modifying ApoE-Aβ interaction rates

#### PMC3528355 — APP Transmembrane Domain and Cholesterol Binding
**Title**: The Amyloid Precursor Protein has a Flexible Transmembrane Domain and Binds Cholesterol
**Key findings**:
- C99 (APP transmembrane fragment) binds cholesterol at a specific site
- Cholesterol binding promotes amyloidogenesis
- GXXXG motifs mediate both oligomerization and cholesterol binding
**Modelable**: Partially — Cholesterol-dependent γ-secretase cleavage rate modulation

#### PMC3440417 — Astrocyte Senescence in AD
**Title**: Astrocyte Senescence as a Component of Alzheimer's Disease
**Key findings**:
- p16INK4a-positive senescent astrocytes increase with age and in AD
- AD frontal cortex has significantly more senescent astrocytes
- Senescent astrocytes produce MMP-1 (senescence-associated secretory phenotype)
**Modelable**: Partially — Age-dependent astrocyte senescence rate affecting neuroinflammation

#### PMC3552866 — Intraneuronal Aβ42 and Neuron Loss
**Title**: Neuron loss in 5XFAD correlates with intraneuronal Aβ42 and Caspase-3 activation
**Key findings**:
- Intraneuronal Aβ42 accumulates in endosomes and lysosomes
- Caspase-3 activation correlates with neuron loss (stereology-confirmed at 9 months)
- Neuron loss in same regions as intraneuronal Aβ42 accumulation
**Modelable**: YES — Intraneuronal Aβ42 accumulation → caspase-3 activation → neuron death

#### PMC3428596 — Tau-Mediated Mitochondrial Dysfunction
**Title**: Tau promotes neurodegeneration via DRP1 mislocalization in vivo
**Key findings**:
- Tau stabilizes actin → inhibits DRP1 association with mitochondria
- Results in mitochondrial elongation and dysfunction
- Leads to cell cycle-mediated cell death
**Modelable**: Partially — Tau → actin stabilization → DRP1 mislocalization → mitochondrial dysfunction → death

#### PMC3395654 — LR11/SorLA-Mediated APP Trafficking
**Title**: GGA1-mediated endocytic traffic of LR11/SorLA alters APP distribution and Aβ production
**Key findings**:
- GGA1 facilitates LR11 endocytic trafficking
- LR11 modulates APP processing in nonamyloidogenic manner
- LR11 expression levels affect Aβ production
**Modelable**: Partially — LR11/SorLA as modulator of APP processing rate (α vs β pathway)

#### PMC3463004 — Tau Oligomer Propagation
**Title**: Alzheimer brain-derived tau oligomers propagate pathology from endogenous tau
**Key findings**:
- Brain-derived tau oligomers inhibit LTP
- Tau oligomers propagate abnormal conformation to endogenous murine tau
- Conformation and hydrophobicity critical for propagation
**Modelable**: Partially — Prion-like tau templating (seeded aggregation kinetics)

#### PMC3484250 — Neuropathologic Substrates of PD Dementia
**Title**: Neuropathologic substrates of Parkinson's disease dementia
**Relevance**: Limited AD relevance; primarily PD-focused with tau/synuclein overlap

#### PMC3472161 — Computational Disease Progression Score
**Title**: A Computational Neurodegenerative Disease Progression Score
**Relevance**: Methodological paper on biomarker trajectory modeling; useful for validation approaches

---

## 2. Key Pathways Identified

### A. Amyloid-beta Production and Processing
- **APP → C99 processing**: Cholesterol binding to C99 promotes γ-secretase cleavage (PMC3528355)
- **LR11/SorLA trafficking**: GGA1-mediated LR11 traffic diverts APP from amyloidogenic pathway (PMC3395654)
- **Presenilin 1 mutations**: FAD PS1 variants impair neurogenesis non-cell-autonomously (PMC3489017)

### B. Amyloid-beta Clearance
- **Glymphatic/paravascular clearance**: AQP4-dependent bulk ISF flow clears soluble Aβ; ~55% reduction in Aqp4-null mice (PMC3551275)
- **BBB receptor-mediated efflux**: Aβ1-40 clears faster than inert tracers, indicating receptor-mediated BBB transport augments bulk flow (PMC3551275)
- **ApoE-dependent clearance**: ApoE4 slows Aβ clearance vs E2/E3; reducing apoE levels paradoxically improves clearance (PMC3433173, PMC3493562)
- **Anti-ApoE immunotherapy**: Antibody-mediated reduction of ApoE-Aβ interaction enhances clearance (PMC3501350)

### C. Amyloid-beta Oligomerization and Toxicity
- **ApoE-dependent oligomerization**: E4 > E3 > E2 in promoting Aβ oligomer formation; 2.7x higher oligomers in E4/4 vs E3/3 brains (PMC3493562)
- **Aβ oligomer → PrPC → Fyn signaling**: Oligomers bind PrPC, activate Fyn, phosphorylate NR2B, cause NMDA-R loss and spine loss (PMC3431439)
- **Intraneuronal Aβ42 toxicity**: Endosomal/lysosomal Aβ42 accumulation triggers caspase-3 and neuron death (PMC3552866)

### D. Tau Pathology
- **Tau oligomer propagation**: Prion-like seeded conversion of endogenous tau by brain-derived oligomers (PMC3463004)
- **Tau → mitochondrial dysfunction**: Tau stabilizes actin → DRP1 mislocalization → mitochondrial elongation → cell death (PMC3428596)
- **p-Tau and entorhinal cortex**: P301L tau aggregation in EC-hippocampal network (PMC3454317)

### E. Neuroinflammation
- **TREM2-dependent microglial activation**: TREM2 KO attenuates TNF-α, IL-1β, IL-6 production (PMC3536811)
- **Complement-mediated synaptic pruning**: CR3/C3 pathway drives microglial engulfment of synapses (PMC3528177)
- **Microglial phagocytosis**: Dual role — beneficial debris clearance vs harmful synapse elimination (PMC3558702)
- **Astrocyte senescence**: Age-dependent SASP activation in AD brain (PMC3440417)
- **Innate immune gene activation**: Extensive inflammatory gene upregulation with aging (PMC3419089)

### F. Protein Quality Control
- **Autophagy-lysosome pathway**: Clearance mechanism for misfolded aggregates; impairment varies by disease (PMC3463804)

---

## 3. Extractable Reactions and Rate Laws

### Reaction 1: Paravascular Aβ Clearance (from PMC3551275)
```
# Glymphatic clearance of soluble Aβ from brain ISF
# First-order clearance modulated by AQP4 activity
compartment BrainISF;
compartment CSF;

species AB40_BrainISF in BrainISF;
species AB40_CSF in CSF;

# Bulk flow clearance (AQP4-dependent)
J_glymphatic_clearance: AB40_BrainISF -> AB40_CSF; k_glymph * AB40_BrainISF * AQP4_activity;

# AQP4 knockout reduces clearance by ~55% for Aβ, ~70% for general solutes
# k_glymph estimated from tracer clearance studies
# AQP4_activity = 1.0 (wild-type) or 0.45 (for Aβ in KO) / 0.30 (general solutes in KO)
```
**Rate type**: UDF (unidirectional flow between compartments)

### Reaction 2: ApoE-Dependent Aβ Oligomerization (from PMC3493562)
```
# ApoE promotes Aβ monomer → oligomer conversion
# Isoform-dependent: E4 > E3 > E2
compartment BrainISF;

species AB42_mono_BrainISF in BrainISF;
species AB42_oligo_BrainISF in BrainISF;
species ApoE_BrainISF in BrainISF;

# ApoE-catalyzed oligomerization
J_apoE_oligomerization: AB42_mono_BrainISF -> AB42_oligo_BrainISF; k_oligo_apoE * AB42_mono_BrainISF * ApoE_BrainISF;

# k_oligo_apoE varies by isoform:
# k_oligo_apoE4 > k_oligo_apoE3 > k_oligo_apoE2
# APOE4/4 brains have 2.7x more oligomers than APOE3/3
```
**Rate type**: MA (mass action, bimolecular)

### Reaction 3: ApoE-Modulated Aβ Clearance (from PMC3433173, PMC3493562)
```
# ApoE impairs Aβ clearance in dose-dependent manner
# Reducing apoE by 50% improves clearance
compartment BrainISF;

species AB_BrainISF in BrainISF;
species ApoE_BrainISF in BrainISF;

# Aβ clearance inhibited by ApoE (E4 > E3 > E2)
J_AB_clearance: AB_BrainISF -> ; k_clear_AB / (1 + K_inhib_apoE * ApoE_BrainISF) * AB_BrainISF;

# K_inhib_apoE represents apoE's inhibitory effect on clearance
# Isoform-dependent: K_inhib_apoE4 > K_inhib_apoE3 > K_inhib_apoE2
```
**Rate type**: custom_conc_per_time (Michaelis-Menten-like inhibition)

### Reaction 4: Aβ Oligomer → PrPC → Fyn Activation Cascade (from PMC3431439)
```
# Aβ oligomer binding to PrPC activates Fyn kinase
compartment Synapse;

species AB_oligo_Synapse in Synapse;
species PrPC_Synapse in Synapse;
species AB_PrPC_complex_Synapse in Synapse;
species Fyn_inactive_Synapse in Synapse;
species Fyn_active_Synapse in Synapse;
species NR2B_Synapse in Synapse;
species pNR2B_Synapse in Synapse;

# Binding
J_AB_PrPC_bind: AB_oligo_Synapse + PrPC_Synapse -> AB_PrPC_complex_Synapse; k_bind * AB_oligo_Synapse * PrPC_Synapse;

# Fyn activation
J_Fyn_activate: Fyn_inactive_Synapse -> Fyn_active_Synapse; k_fyn_act * AB_PrPC_complex_Synapse * Fyn_inactive_Synapse;

# NR2B phosphorylation
J_NR2B_phos: NR2B_Synapse -> pNR2B_Synapse; k_nr2b_phos * Fyn_active_Synapse * NR2B_Synapse;
```
**Rate type**: MA (mass action for each step)

### Reaction 5: Complement-Mediated Synaptic Elimination (from PMC3528177)
```
# C3-tagged synapses are engulfed by microglia via CR3
compartment Synapse;
compartment Microglia;

species Synapse_healthy in Synapse;
species C3_Synapse in Synapse;  # C3-tagged synapse
species Synapse_engulfed in Microglia;

# C3 tagging (activity-dependent)
J_C3_tag: Synapse_healthy -> C3_Synapse; k_c3_tag * Synapse_healthy * C3_concentration;

# Microglial engulfment via CR3
J_engulf: C3_Synapse -> Synapse_engulfed; k_engulf * C3_Synapse * CR3_Microglia;
```
**Rate type**: MA (mass action)

### Reaction 6: Intraneuronal Aβ42 → Caspase-3 → Neuron Death (from PMC3552866)
```
# Intraneuronal Aβ42 accumulation triggers apoptosis
compartment Neuron;

species AB42_intraneuronal in Neuron;
species Caspase3_inactive in Neuron;
species Caspase3_active in Neuron;
species Neuron_viable;
species Neuron_dead;

# Aβ42 accumulation triggers caspase-3 activation
J_casp3_act: Caspase3_inactive -> Caspase3_active; k_casp3 * AB42_intraneuronal * Caspase3_inactive;

# Caspase-3-mediated neuron death
J_neuron_death: Neuron_viable -> Neuron_dead; k_death * Caspase3_active * Neuron_viable;
```
**Rate type**: MA (mass action)

### Reaction 7: Tau Oligomer Seeded Propagation (from PMC3463004)
```
# Prion-like seeded conversion of native tau by tau oligomers
compartment BrainISF;

species Tau_native_BrainISF in BrainISF;
species Tau_oligo_BrainISF in BrainISF;

# Seeded conversion (nucleation-dependent)
J_tau_seed: Tau_native_BrainISF -> Tau_oligo_BrainISF; k_seed * Tau_oligo_BrainISF * Tau_native_BrainISF;
```
**Rate type**: MA (mass action, bimolecular — product-catalyzed)

### Reaction 8: Tau → DRP1 Mislocalization → Mitochondrial Dysfunction (from PMC3428596)
```
# Tau-mediated mitochondrial elongation and dysfunction
compartment Neuron;

species Tau_Neuron in Neuron;
species Actin_dynamic_Neuron in Neuron;
species Actin_stable_Neuron in Neuron;
species DRP1_mito_Neuron in Neuron;  # DRP1 on mitochondria
species DRP1_cyto_Neuron in Neuron;  # DRP1 displaced to cytoplasm
species Mito_healthy_Neuron in Neuron;
species Mito_elongated_Neuron in Neuron;

# Tau stabilizes actin
J_actin_stab: Actin_dynamic_Neuron -> Actin_stable_Neuron; k_actin_stab * Tau_Neuron * Actin_dynamic_Neuron;

# Stable actin displaces DRP1 from mitochondria
J_DRP1_displace: DRP1_mito_Neuron -> DRP1_cyto_Neuron; k_drp1_disp * Actin_stable_Neuron * DRP1_mito_Neuron;

# Reduced DRP1 on mitochondria → elongation
J_mito_elong: Mito_healthy_Neuron -> Mito_elongated_Neuron; k_elong * Mito_healthy_Neuron / (1 + DRP1_mito_Neuron / Km_drp1);
```
**Rate type**: Mixed MA and custom

### Reaction 9: TREM2-Dependent Cytokine Production (from PMC3536811)
```
# TREM2 modulates microglial inflammatory response
compartment Microglia;

species TREM2_Microglia in Microglia;
species TNFa_Microglia in Microglia;
species IL1b_Microglia in Microglia;
species IL6_Microglia in Microglia;

# TREM2-dependent cytokine production
J_TNFa_prod: -> TNFa_Microglia; k_tnf * TREM2_Microglia * stimulus;
J_IL1b_prod: -> IL1b_Microglia; k_il1b * TREM2_Microglia * stimulus;
J_IL6_prod: -> IL6_Microglia; k_il6 * TREM2_Microglia * stimulus;
```
**Rate type**: custom_conc_per_time

### Reaction 10: Autophagy-Mediated Aggregate Clearance (from PMC3463804)
```
# Autophagy clears misfolded protein aggregates
compartment Neuron;

species ProteinAgg_Neuron in Neuron;
species Autophagosome_Neuron in Neuron;

# Autophagic clearance (saturable)
J_autophagy: ProteinAgg_Neuron -> ; Vmax_autophagy * ProteinAgg_Neuron / (Km_autophagy + ProteinAgg_Neuron) * Autophagosome_Neuron;
```
**Rate type**: custom_conc_per_time (Michaelis-Menten)

---

## 4. Species and Compartments

### Compartments
| Compartment | Description | Source Papers |
|---|---|---|
| BrainISF | Brain interstitial fluid | PMC3551275, PMC3493562, PMC3433173 |
| CSF | Cerebrospinal fluid | PMC3551275 |
| Synapse | Synaptic cleft / postsynaptic density | PMC3431439, PMC3528177 |
| Neuron | Neuronal cytoplasm | PMC3552866, PMC3428596, PMC3463804 |
| Microglia | Microglial cell | PMC3536811, PMC3528177 |
| Endosome | Endosomal compartment | PMC3552866, PMC3395654 |
| Lysosome | Lysosomal compartment | PMC3552866, PMC3463804 |
| Membrane | Plasma membrane (for APP processing) | PMC3528355 |

### Species
| Species | Compartment(s) | Description | Source |
|---|---|---|---|
| AB40_BrainISF | BrainISF | Soluble Aβ1-40 in ISF | PMC3551275 |
| AB42_mono_BrainISF | BrainISF | Monomeric Aβ42 | PMC3493562 |
| AB42_oligo_BrainISF | BrainISF | Oligomeric Aβ42 | PMC3493562, PMC3431439 |
| AB42_intraneuronal | Neuron | Intraneuronal Aβ42 | PMC3552866 |
| ApoE_BrainISF | BrainISF | Apolipoprotein E (isoform-dependent) | PMC3433173, PMC3493562 |
| PrPC_Synapse | Synapse | Cellular prion protein | PMC3431439 |
| AB_PrPC_complex_Synapse | Synapse | Aβ oligomer-PrPC complex | PMC3431439 |
| Fyn_active_Synapse | Synapse | Active Fyn kinase | PMC3431439 |
| Fyn_inactive_Synapse | Synapse | Inactive Fyn kinase | PMC3431439 |
| NR2B_Synapse | Synapse | NMDA receptor NR2B subunit | PMC3431439 |
| pNR2B_Synapse | Synapse | Phospho-NR2B | PMC3431439 |
| Tau_native_BrainISF | BrainISF | Native tau protein | PMC3463004 |
| Tau_oligo_BrainISF | BrainISF | Tau oligomers | PMC3463004 |
| Tau_Neuron | Neuron | Intracellular tau | PMC3428596 |
| TREM2_Microglia | Microglia | TREM2 receptor | PMC3536811 |
| TNFa_Microglia | Microglia | TNF-alpha | PMC3536811 |
| IL1b_Microglia | Microglia | IL-1beta | PMC3536811 |
| IL6_Microglia | Microglia | IL-6 | PMC3536811 |
| C3_Synapse | Synapse | C3-tagged synapse | PMC3528177 |
| CR3_Microglia | Microglia | Complement receptor 3 | PMC3528177 |
| AQP4_Astrocyte | BrainISF | Aquaporin-4 (modulates bulk flow) | PMC3551275 |
| Caspase3_active | Neuron | Active caspase-3 | PMC3552866 |
| DRP1_mito_Neuron | Neuron | Mitochondrial DRP1 | PMC3428596 |
| Actin_stable_Neuron | Neuron | Stabilized actin (tau-bound) | PMC3428596 |
| LR11_Endosome | Endosome | LR11/SorLA receptor | PMC3395654 |
| Cholesterol_Membrane | Membrane | Membrane cholesterol | PMC3528355 |
| C99_Membrane | Membrane | APP C-terminal fragment | PMC3528355 |
| ProteinAgg_Neuron | Neuron | Misfolded protein aggregates | PMC3463804 |
| Autophagosome_Neuron | Neuron | Autophagosomes | PMC3463804 |
| Synapse_healthy | Synapse | Healthy synapse | PMC3528177 |
| Mito_healthy_Neuron | Neuron | Healthy mitochondria | PMC3428596 |
| Mito_elongated_Neuron | Neuron | Elongated/dysfunctional mitochondria | PMC3428596 |

---

## 5. Papers Without Quantitative Data (Mechanistic Only)

These papers describe AD-relevant pathways qualitatively but lack extractable rate constants or kinetic parameters:

| PMC ID | Title | Key Pathway |
|---|---|---|
| PMC3402380 | Stress Granule Proteins TIA-1/G3BP in Tauopathies | Stress granule formation |
| PMC3440417 | Astrocyte Senescence in AD | Cellular senescence |
| PMC3463004 | Tau Oligomer Propagation | Tau seeded aggregation |
| PMC3471388 | Vascular Risk Factors and AD | Vascular contributions |
| PMC3483034 | AD Neuropathological Subtypes | Disease heterogeneity |
| PMC3483256 | Exosomal α-Synuclein Transmission | Exosome-mediated spread |
| PMC3490201 | Neuroimaging in Atypical AD | Biomarker imaging |
| PMC3490232 | Neuropathology vs Cognition | Pathology-cognition correlation |
| PMC3515078 | Florbetapir PET in PS1 E280A | Amyloid imaging |
| PMC3528355 | APP TMD and Cholesterol | APP-cholesterol interaction |
| PMC3534053 | ApoE4 and GABAergic Interneurons | ApoE4 neurotoxicity |
| PMC3535537 | CR1 and Brain Amyloid with APOE | Complement-amyloid interaction |
| PMC3560290 | AD Neuropathology and Cognition Review | Review/correlation |

---

## 6. Summary of Modeling Priority

**Highest priority for Antimony module development** (quantitative, multi-paper support):

1. **Glymphatic Aβ clearance module** — PMC3551275 provides clearance rates and AQP4 dependence
2. **ApoE-Aβ interaction module** — PMC3493562 + PMC3433173 provide oligomerization rates and clearance modulation
3. **Aβ oligomer synaptic toxicity module** — PMC3431439 provides full signaling cascade
4. **Complement-mediated synapse loss module** — PMC3528177 provides CR3/C3 mechanism
5. **Intraneuronal Aβ42 toxicity module** — PMC3552866 provides caspase-3 link
6. **Tau propagation module** — PMC3463004 provides seeded conversion model
7. **TREM2-neuroinflammation module** — PMC3536811 provides cytokine regulation
