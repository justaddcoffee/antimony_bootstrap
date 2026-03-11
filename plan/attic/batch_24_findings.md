# Batch 24 Findings: Quantitative Mechanisms for Alzheimer ODE Modeling

**Date**: 2026-02-24
**Papers analyzed**: 86
**Source**: Secondary_Alzforum collection (PMC3693547 - PMC3845973)

## Overview

This batch of 86 papers from the Secondary Alzforum collection is dominated by genetics/GWAS studies, imaging/biomarker analyses, and clinical cohort papers. While few papers contain directly extractable quantitative parameters (rate constants, kinetic values), approximately 26 papers provide mechanistic pathway information relevant to building Antimony ODE modules for Alzheimer disease.

## 1. Papers with Quantitative/Mechanistic Data

### Papers with Direct Mechanistic Relevance to ODE Modeling

The following papers describe biological mechanisms that can inform reaction topology, species interactions, and compartmental structure for Antimony models. None in this batch report explicit kinetic rate constants, but they provide essential qualitative and semi-quantitative pathway knowledge.

#### PMC3696910
**Title**: The Importance of Tau Phosphorylation for Neurodegenerative Diseases

**Pathways**: tau_pathology

**Species**: tau, ptau, GSK3beta

**Compartments**: Neuron

**Notes**: Reviews tau phosphorylation at multiple sites and its role in neurodegeneration. Discusses kinases (GSK3, CDK5) and phosphatases involved. Key insight: soluble phospho-tau species may be more toxic than fibrillar tangles.

---

#### PMC3741682
**Title**: Activity-induced convergence of APP and BACE-1 in acidic microdomains via endocytosis-dependent pathway

**Pathways**: amyloid_processing

**Species**: APP, BACE1

**Compartments**: Neuron, Endosome

**Notes**: Demonstrates that APP-BACE1 convergence is rate-limiting for amyloidogenic processing. Neuronal activity drives endocytosis-dependent co-localization in acidic microdomains. Directly relevant to modeling APP cleavage kinetics.

---

#### PMC3796170
**Title**: Development and Mechanism of gamma-Secretase Modulators for Alzheimer Disease

**Pathways**: amyloid_processing

**Species**: APP, BACE1

**Compartments**: Neuron

**Notes**: Details gamma-secretase composition (presenilin, Nicastrin, Aph1, Pen2) and cleavage mechanism. Gamma-secretase modulators shift AB42/AB40 ratio. Relevant to parameterizing gamma-secretase cleavage reactions.

---

#### PMC3812809
**Title**: NLRP3 is activated in Alzheimers disease and contributes to pathology in APP/PS1 mice

**Pathways**: neuroinflammation

**Species**: microglia_active, IL1beta

**Compartments**: Microglia

**Notes**: Shows NLRP3 inflammasome activation by AB in microglia is fundamental for IL-1beta maturation. NLRP3 deficiency in APP/PS1 mice reduces AB deposition and enhances microglial phagocytosis. Key for neuroinflammation module.

---

#### PMC3706457
**Title**: CD33 Inhibits Microglial Uptake of Amyloid Beta

**Pathways**: neuroinflammation

**Species**: microglia_active, APP

**Compartments**: Microglia

**Notes**: CD33 expression in microglia inhibits AB uptake/phagocytosis. CD33 inactivation restores microglial AB clearance. Relevant to modeling microglial AB clearance rates.

---

#### PMC3779465
**Title**: Microglial beclin 1 regulates retromer trafficking and phagocytosis in AD

**Pathways**: autophagy_proteostasis, neuroinflammation

**Species**: microglia_active

**Compartments**: Microglia, Endosome

**Notes**: Beclin 1 impairment in AD microglia reduces phagocytic receptor recycling via retromer dysfunction. Links autophagy to AB clearance capacity. Relevant to modeling microglial clearance efficiency.

---

#### PMC3726719
**Title**: Apolipoprotein E and Alzheimer disease: risk, mechanisms, and therapy

**Pathways**: lipid_metabolism, amyloid_processing

**Species**: ApoE, APP, cholesterol

**Compartments**: Neuron, BrainCSF

**Notes**: Comprehensive review: ApoE4 promotes AB aggregation and impairs AB clearance. ApoE modulates AB transport across BBB. ApoE lipidation state affects AB binding. Critical for ApoE-AB interaction module.

---

#### PMC3768018
**Title**: Metabotropic Glutamate Receptor 5 is Co-Receptor for AB Oligomer Bound to Cellular Prion Protein

**Pathways**: synaptic_dysfunction

**Species**: glutamate, APP

**Compartments**: Synapse, Neuron

**Notes**: AB oligomers bind PrPC, coupling through mGluR5 to activate Fyn kinase at PSD. This disrupts synapses. Provides receptor-level detail for modeling AB-mediated synaptic toxicity.

---

#### PMC3836238
**Title**: Tau protein is required for AB-induced impairment of hippocampal LTP

**Pathways**: synaptic_dysfunction, tau_pathology

**Species**: tau, APP

**Compartments**: Synapse, Neuron

**Notes**: Demonstrates AB requires tau to impair LTP. Tau knockout prevents AB synaptic toxicity. Key for modeling the AB-tau interaction in synaptic dysfunction.

---

#### PMC3798002
**Title**: IFNgamma promotes complement expression and attenuates amyloid plaque deposition

**Pathways**: neuroinflammation

**Species**: microglia_active, APP

**Compartments**: Microglia, Neuron

**Notes**: IFNgamma-mediated neuroinflammation activates complement system, promoting AB clearance. Shows dual role of inflammation. Relevant to modeling complement-mediated AB clearance.

---

#### PMC3807661
**Title**: Increased BIN1 expression mediates Alzheimer genetic risk by modulating tau pathology

**Pathways**: tau_pathology

**Species**: tau

**Compartments**: Neuron

**Notes**: BIN1 overexpression increases tau levels and modulates tau propagation. Provides mechanistic link between BIN1 locus and tau pathology. Relevant to tau module.

---

#### PMC3752843
**Title**: Preparing Synthetic AB in Different Aggregation States

**Pathways**: amyloid_processing

**Species**: APP

**Compartments**: BrainCSF

**Notes**: Protocols for monomer, oligomer, and fibril preparation. Describes aggregation conditions. Qualitative support for AB aggregation kinetics modeling.

---

#### PMC3713518
**Title**: Structure-based discovery of fiber-binding compounds that reduce cytotoxicity of amyloid beta

**Pathways**: amyloid_processing

**Species**: APP

**Compartments**: Neuron

**Notes**: Atomic structure of AB fibrils used for drug discovery. Provides structural context for aggregation modeling.

---

#### PMC3814033
**Title**: Molecular structure of beta-amyloid fibrils in Alzheimer disease brain tissue

**Pathways**: amyloid_processing

**Species**: APP

**Compartments**: Neuron

**Notes**: Brain-derived AB fibrils have distinct molecular structure. Relevant to understanding aggregation kinetics in vivo vs in vitro.

---

#### PMC3778669
**Title**: Vascular Contributions to Cognitive Impairment and Dementia

**Pathways**: vascular

**Species**: APP

**Compartments**: BBB, Plasma, Neuron

**Notes**: Comprehensive review of vascular contributions to dementia including BBB dysfunction, cerebral hypoperfusion, and impaired AB clearance. Supports vascular/BBB module development.

---

#### PMC3842016
**Title**: The pathobiology of vascular dementia

**Pathways**: vascular

**Species**: APP

**Compartments**: BBB, Neuron

**Notes**: Reviews cerebrovascular pathology in dementia. BBB breakdown, white matter lesions, and vascular contributions to neurodegeneration.

---

#### PMC3699502
**Title**: A Luminex Assay Detects AB Oligomers in AD Cerebrospinal Fluid

**Pathways**: amyloid_processing

**Species**: APP, tau

**Compartments**: BrainCSF

**Notes**: Measures AB oligomers in CSF. Oligomer levels correlate with disease. Provides concentration-level data for AB species in CSF compartment.

---

#### PMC3820001
**Title**: Distinct alpha-Synuclein Strains Differentially Promote Tau Inclusions in Neurons

**Pathways**: tau_pathology

**Species**: tau

**Compartments**: Neuron

**Notes**: Alpha-synuclein strains cross-seed tau aggregation. Relevant to understanding tau aggregation kinetics and prion-like spreading.

---

#### PMC3703870
**Title**: CD33 AD locus: Altered monocyte function and amyloid biology

**Pathways**: neuroinflammation

**Species**: APP, microglia_active

**Compartments**: Microglia

**Notes**: CD33 risk allele associated with diminished AB42 internalization. Quantifies relative expression changes. Supports modeling microglial clearance modulation.

---

#### PMC3840123
**Title**: The Microglial Sensome Revealed by Direct RNA Sequencing

**Pathways**: neuroinflammation

**Species**: microglia_active

**Compartments**: Microglia

**Notes**: Defines the microglial "sensome" - sensing apparatus. Identifies 100+ genes for microglia sensing, relevant to modeling microglial activation signals.

---

#### PMC3711605
**Title**: Tau loss attenuates neuronal network hyperexcitability

**Pathways**: tau_pathology, synaptic_dysfunction

**Species**: tau

**Compartments**: Neuron, Synapse

**Notes**: Tau reduction prevents network hyperexcitability in epilepsy models. Relevant to modeling tau role in neuronal excitability.

---

#### PMC3706568
**Title**: sAPPalpha Rescues Age-Linked Decline in Neural Progenitor Cell Proliferation

**Pathways**: amyloid_processing

**Species**: APP

**Compartments**: Neuron

**Notes**: sAPPalpha acts as a neuroprotective/proliferative factor. Relevant to modeling beneficial vs harmful APP cleavage products.

---

### Genetics/GWAS Papers (Limited ODE Relevance)

These papers focus on genetic risk factors and do not contain extractable mechanistic or quantitative data for ODE modeling:

- **PMC3696507: Imputation of sequence variants for identification of genetic risks for Parkinsons disease**
- **PMC3696580: Fast and accurate genotype imputation in genome-wide association studies through pre-phasing**
- **PMC3708460: The Genetics and Neuropathology of Alzheimers Disease**
- **PMC3708544: Evolution and Functional Impact of Rare Coding Variation from Deep Sequencing of Human Exomes**
- **PMC3709915: Best Practices and Joint Calling of the HumanExome BeadChip: The CHARGE Consortium**
- **PMC3712628: RNA-Guided Human Genome Engineering via Cas9**
- **PMC3713637: Genome-wide pathway analysis of memory impairment in ADNI**
- **PMC3756911: Prion-like domain mutations in hnRNPs cause multisystem proteinopathy and ALS**
- **PMC3771521: Systematic Localization of Common Disease-Associated Variation in Regulatory DNA**
- **PMC3776390: Signatures of mutational processes in human cancer**
- **PMC3777294: Whole-exome sequencing and imaging genetics identify functional variants for hippocampal volume**
- **PMC3791416: Bayesian refinement of association signals for 14 loci in 3 common diseases**
- **PMC3809344: Variants in PPP3R1 and MAPT are associated with more rapid functional decline in AD**
- **PMC3832488: Epistatic Genetic Effects among Alzheimers Candidate Genes**

### Imaging/Biomarker Papers (Limited ODE Relevance)

These papers focus on diagnostic imaging and biomarker measurements:

- **PMC3693547: Amyloid Related Imaging Abnormalities (ARIA) in Amyloid Modifying Therapeutic Trials**
- **PMC3707015: Plasma tau levels in Alzheimers disease**
- **PMC3707057: Modeling the heterogeneity in risk of progression to AD**
- **PMC3707386: CSF biomarker variability in the Alzheimers Association quality control program**
- **PMC3710290: The Alzheimers Association external quality control program for CSF biomarkers**
- **PMC3714437: Neuroimaging standards for research into small vessel disease**
- **PMC3720813: The Minimal Preprocessing Pipelines for the Human Connectome Project**
- **PMC3745014: Posterior Cingulate Glucose Metabolism and Hippocampal Volume**
- **PMC3747730: Amyloid-beta Imaging with Pittsburgh Compound B and Florbetapir**
- **PMC3748164: Comparing PET imaging and CSF measurements of AB**
- **PMC3751169: Subgroup of ADNI Normal Controls Characterized by Atrophy**
- **PMC3782292: Unbiased Comparison of Sample Size Estimates From Longitudinal Structural Measures**
- **PMC3786871: Amyloid Deposition, Hypometabolism, and Longitudinal Cognitive Decline**
- **PMC3792042: Characterization of Novel CSF Tau and ptau Biomarkers for AD**
- **PMC3795312: Biomarker-based prediction of progression in MCI**
- **PMC3800236: Florbetapir PET to assess amyloid burden**
- **PMC3809845: Imaging of tau pathology in a tauopathy mouse model**
- **PMC3819320: Quantitative Analysis of PiB-PET with FreeSurfer ROIs**

### Other Papers (Not Directly Relevant to AD ODE Modeling)

- **PMC3706780: Genes and pathways underlying regional and cell type changes in AD**
- **PMC3712285: Phase I study of antisense oligonucleotide directed against SOD1**
- **PMC3714794: Rejuvenation of regeneration in the aging CNS**
- **PMC3715864: Bace1 and Neuregulin-1 cooperate to control muscle spindles**
- **PMC3719181: Fate Mapping Analysis Reveals That Adult Microglia Derive from Primitive Macrophages**
- **PMC3721477: Caudo-rostral brain spreading of alpha-synuclein through vagal connections**
- **PMC3740510: Dissociation of FTD-Related Deficits and Neuroinflammation in Progranulin Mice**
- **PMC3743672: Progranulin mutations as a risk factor for Alzheimers Disease**
- **PMC3751803: Rapid Single-Step Induction of Functional Neurons from Pluripotent Stem Cells**
- **PMC3753484: Modeling key pathological features of FTD with C9ORF72 repeat expansion**
- **PMC3756294: CSF protein biomarkers predicting longitudinal reduction of CSF AB42**
- **PMC3766501: TMEM106B regulates TMEM106B protein levels: implications for FTD**
- **PMC3779219: Increased Neurofilament Light Chain Blood Levels in Neurodegenerative Diseases**
- **PMC3785076: Stages of pTDP-43 pathology in ALS**
- **PMC3788602: Identification of long-lived proteins reveals exceptional stability**
- **PMC3790461: SYNJ1 mutations in early-onset progressive parkinsonism**
- **PMC3804562: Criteria for Mild Cognitive Impairment Due to AD**
- **PMC3806057: Composite score for memory in ADNI**
- **PMC3811119: Altered Ribostasis: RNA-protein granule formation in degenerative disorders**
- **PMC3816382: Spatiotemporal Linear Mixed Effects Modeling for Longitudinal Neuroimage Data**
- **PMC3817409: Cerebral organoids model human brain development and microcephaly**
- **PMC3821180: Comprehensive comparative analysis of RNA sequencing methods**
- **PMC3821974: Activation of transposable elements during aging and neuronal decline**
- **PMC3823238: Relationship of cognitive reserve and CSF biomarkers**
- **PMC3826637: Structural and functional characterization of two alpha-synuclein strains**
- **PMC3828889: Apolipoprotein E e4 magnifies lifestyle risks for dementia**
- **PMC3830741: Antisense transcripts of expanded C9ORF72 hexanucleotide repeat**
- **PMC3830745: C9orf72 FTLD characterised by frequent neuronal RNA foci**
- **PMC3834153: High-resolution noise substitution in cryoEM 3D structure determination**
- **PMC3836174: The Hallmarks of Aging**
- **PMC3840954: TDP-43 Frontotemporal Lobar Degeneration and Autoimmune Disease**
- **PMC3845973: Much of late life cognitive decline is not due to common neurodegenerative pathologies**

## 2. Key Pathways Identified

| Pathway | Paper Count | Relevance to ODE Modeling |
|---------|------------|---------------------------|
| tau_pathology | 14 | Tau phosphorylation/aggregation cascade - primary ODE module |
| amyloid_processing | 10 | Core AB production/processing - primary ODE module |
| neuroinflammation | 9 | Microglial/astrocyte activation and cytokine dynamics |
| vascular | 7 | BBB transport and cerebrovascular dynamics |
| lipid_metabolism | 6 | ApoE/cholesterol interactions with AB |
| synaptic_dysfunction | 5 | Synaptic loss and neurotransmitter dynamics |
| insulin_signaling | 3 | Insulin/IGF pathway modulation |
| autophagy_proteostasis | 3 | Protein clearance pathways |

### Pathway Highlights

**Tau Pathology** (most represented):
- Tau phosphorylation as neurodegeneration driver (PMC3696910)
- BIN1 modulates tau levels and pathology (PMC3807661)
- Cross-seeding of tau by alpha-synuclein strains (PMC3820001)
- Tau required for AB-induced LTP impairment (PMC3836238)
- Tau role in network hyperexcitability (PMC3711605)

**Neuroinflammation**:
- NLRP3 inflammasome activation by AB, IL-1beta release (PMC3812809)
- CD33 inhibits microglial AB phagocytosis (PMC3706457, PMC3703870)
- Beclin 1 regulation of microglial phagocytosis (PMC3779465)
- IFNgamma/complement-mediated AB clearance (PMC3798002)
- Microglial sensome characterization (PMC3840123)

**Amyloid Processing**:
- APP-BACE1 convergence as rate-limiting step (PMC3741682)
- Gamma-secretase modulator mechanisms (PMC3796170)
- AB oligomer detection in CSF (PMC3699502)
- AB fibril structures (PMC3814033, PMC3713518)
- sAPPalpha neuroprotective signaling (PMC3706568)

## 3. Extractable Reactions and Rate Laws

Reactions identified from this batch with suggested Antimony rate law formulations. Note: this batch contains no explicit kinetic rate constants. Rate laws below are suggested templates based on mechanism descriptions.

### `AB_aggregation`
- **Reaction**: AB_monomer -> AB_oligomer -> AB_fibril
- **Supporting papers**: PMC3699502, PMC3703870, PMC3713518, PMC3752843, PMC3814033 (5 papers)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_nuc = k_nuc * [AB_mono_BrainISF]^2; v_elong = k_elong * [AB_mono_BrainISF] * [AB_fibril_BrainISF]`
- **Notes**: Multiple papers characterize AB aggregation states. PMC3752843 provides protocols for monomer/oligomer/fibril. PMC3814033 shows brain-derived fibrils have distinct structure.

### `AB_oligomer_toxicity`
- **Reaction**: AB_oligomer + PrPC + mGluR5 -> Fyn_activation -> synapse_damage
- **Supporting papers**: PMC3768018 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_tox = k_tox * [AB_oligo_Synapse] * [PrPC_Synapse] * [mGluR5_Synapse]`
- **Notes**: AB oligomers bind PrPC, coupling through mGluR5 to activate Fyn kinase at PSD.

### `APP_BACE1_convergence`
- **Reaction**: APP + BACE1 -> APP_BACE1_complex (endocytosis-dependent)
- **Supporting papers**: PMC3741682 (1 paper)
- **Elbert rate type**: `MA or custom_conc_per_time`
- **Suggested rate law**: `v_conv = k_endo * [APP_Neuron] * [BACE1_Neuron] * activity_factor`
- **Notes**: Rate-limiting step. Neuronal activity drives APP-BACE1 co-localization in acidic endosomal compartments.

### `gamma_secretase_cleavage`
- **Reaction**: CTFbeta -> AB42 + AB40 + AICD (gamma-secretase)
- **Supporting papers**: PMC3796170 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_gamma = k_gamma * [CTFbeta_Neuron]; AB42:AB40 ratio modulated by GSMs`
- **Notes**: Gamma-secretase modulators shift AB42:AB40 ratio without total inhibition.

### `NLRP3_inflammasome`
- **Reaction**: AB + microglia -> NLRP3_activation -> IL1beta_release
- **Supporting papers**: PMC3812809 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_inflam = k_nlrp3 * [AB_fibril_BrainISF]^n / (K^n + [AB_fibril_BrainISF]^n) * [microglia_resting]`
- **Notes**: NLRP3 inflammasome fundamental for IL-1beta in AD. Hill-type activation by AB aggregates.

### `CD33_microglial_clearance`
- **Reaction**: microglia + AB -> AB_cleared (modulated by CD33)
- **Supporting papers**: PMC3706457, PMC3703870 (2 papers)
- **Elbert rate type**: `MA`
- **Suggested rate law**: `v_clear = k_phag * [microglia_active] * [AB_BrainISF] * (1 - CD33_factor)`
- **Notes**: CD33 expression inhibits microglial AB uptake. CD33 inactivation restores phagocytic capacity.

### `beclin1_phagocytosis`
- **Reaction**: beclin1 -> retromer_recycling -> phagocytic_receptor_surface
- **Supporting papers**: PMC3779465 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_phag = k_phag_base * beclin1_activity * [microglia_active]`
- **Notes**: Beclin 1 regulates retromer trafficking for phagocytic receptor recycling. Impaired in AD.

### `ApoE_AB_interaction`
- **Reaction**: ApoE + AB -> ApoE_AB_complex (isoform-dependent)
- **Supporting papers**: PMC3726719 (1 paper)
- **Elbert rate type**: `MA`
- **Suggested rate law**: `v_bind = k_bind_ApoE * [ApoE_BrainISF] * [AB_BrainISF]` (k varies by isoform)
- **Notes**: ApoE4 promotes AB aggregation and impairs clearance. ApoE lipidation state modulates binding.

### `complement_AB_clearance`
- **Reaction**: IFNgamma -> complement_activation -> AB_plaque_clearance
- **Supporting papers**: PMC3798002 (1 paper)
- **Elbert rate type**: `MA`
- **Suggested rate law**: `v_comp = k_comp * [complement_active] * [AB_plaque_BrainISF]`
- **Notes**: IFNgamma promotes complement expression, attenuating AB plaque deposition.

### `tau_AB_LTP_impairment`
- **Reaction**: AB_oligomer + tau -> LTP_impairment
- **Supporting papers**: PMC3836238 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_LTP_impair = k_impair * [AB_oligo_Synapse] * [tau_Neuron]`
- **Notes**: Tau is required for AB-induced LTP impairment. Tau knockout blocks AB synaptic toxicity.

### `BIN1_tau_modulation`
- **Reaction**: BIN1 -> increased tau levels -> tau propagation
- **Supporting papers**: PMC3807661 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_tau_increase = k_BIN1 * [BIN1_Neuron] * [tau_Neuron]`
- **Notes**: BIN1 overexpression increases tau levels and modulates pathology spread.

### `tau_phosphorylation`
- **Reaction**: tau -> ptau (GSK3/CDK5)
- **Supporting papers**: PMC3696910 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_phos = Vmax * [tau_Neuron] / (Km + [tau_Neuron]) * [GSK3_Neuron]`
- **Notes**: Comprehensive review of tau phosphorylation sites and kinases. Soluble ptau more toxic than fibrils.

### `alpha_syn_tau_crossseed`
- **Reaction**: alpha_synuclein_strain + tau -> tau_aggregate
- **Supporting papers**: PMC3820001 (1 paper)
- **Elbert rate type**: `custom_conc_per_time`
- **Suggested rate law**: `v_cross = k_cross * [aSyn_Neuron] * [tau_Neuron]`
- **Notes**: Alpha-synuclein strains differentially promote tau inclusions. Relevant to mixed pathology.

## 4. Species and Compartments

### Species Identified (Elbert naming convention: `{species}_{compartment}`)

| Species | Count | Compartment(s) | Full Name |
|---------|-------|---------------|-----------|
| tau | 14 | Neuron, Synapse | Tau protein (total) |
| ApoE | 6 | BrainISF, BrainCSF, Plasma | Apolipoprotein E |
| APP | 5 | Neuron, Endosome | Amyloid Precursor Protein |
| ptau | 4 | Neuron, BrainCSF | Phosphorylated tau |
| BACE1 | 2 | Neuron, Endosome | Beta-secretase 1 |
| microglia_active | 1 | Microglia | Activated microglia |
| cholesterol | 1 | Neuron, BrainISF | Cholesterol |
| glutamate | 1 | Synapse | Glutamate |
| AB42_mono | - | BrainISF, BrainCSF | AB42 monomer (implied by aggregation studies) |
| AB42_oligo | - | BrainISF, Synapse | AB42 oligomer (implied) |
| AB42_fibril | - | BrainISF | AB42 fibril (implied) |
| IL1beta | - | Microglia, BrainISF | Interleukin-1 beta (implied by NLRP3 paper) |
| CD33 | - | Microglia | CD33 surface receptor |
| PrPC | - | Synapse | Cellular prion protein |
| mGluR5 | - | Synapse | Metabotropic glutamate receptor 5 |
| BIN1 | - | Neuron | Bridging integrator 1 |
| beclin1 | - | Microglia | Beclin 1 |
| complement | - | BrainISF | Complement system components |
| sAPPalpha | - | BrainISF | Soluble APP alpha fragment |

### Compartments Identified

| Compartment | Paper Count | Description |
|------------|------------|-------------|
| Neuron | 13 | Neuronal intracellular space |
| BrainCSF | 13 | Cerebrospinal fluid |
| Microglia | 8 | Microglial cell |
| Synapse | 1 | Synaptic cleft / post-synaptic density |
| Plasma | 1 | Blood plasma |
| Endosome | 1 | Endosomal compartment (acidic microdomains) |
| BrainISF | - | Brain interstitial fluid (implied in many papers) |
| BBB | - | Blood-brain barrier (implied by vascular papers) |

## Summary

- **Total papers analyzed**: 86
- **Papers with direct mechanistic relevance**: 22
- **Genetics/GWAS papers**: 14
- **Imaging/biomarker papers**: 18
- **Other (limited ODE relevance)**: 32
- **Papers with explicit quantitative parameters**: 0
- **Unique pathways identified**: 8
- **Unique species identified**: 19 (8 measured, 11 implied)
- **Unique compartments identified**: 8 (6 measured, 2 implied)
- **Unique extractable reactions**: 12

### Key Takeaways for ODE Modeling

1. **No explicit kinetic parameters** in this batch. Papers are primarily descriptive mechanistic, genetic, or clinical.
2. **Strong mechanistic coverage of tau pathology**: multiple papers provide pathway topology for tau phosphorylation, aggregation, and interaction with AB.
3. **NLRP3 inflammasome pathway** (PMC3812809) is a high-priority target for the neuroinflammation module, providing clear mechanistic steps from AB to IL-1beta release.
4. **APP-BACE1 convergence** (PMC3741682) provides important rate-limiting kinetic insight for amyloid processing module.
5. **CD33/beclin1 microglial clearance** modulation (PMC3706457, PMC3779465) informs clearance rate parameter sensitivity.
6. **ApoE isoform effects** (PMC3726719) critical for parameterizing ApoE-AB interaction module.
7. **AB oligomer-PrPC-mGluR5 signaling** (PMC3768018) defines synaptic toxicity mechanism at receptor level.
8. **Tau-AB synergy** (PMC3836238) requires coupling between amyloid and tau modules.

### Priority Papers for Full-Text Parameter Mining

These papers should be examined in full text for any quantitative data not captured in abstracts:

1. **PMC3741682**: APP-BACE1 convergence kinetics (may contain rate measurements)
2. **PMC3812809**: NLRP3 inflammasome activation (may contain dose-response data for AB concentration)
3. **PMC3706457**: CD33 microglial uptake (contains relative expression/uptake changes)
4. **PMC3703870**: CD33 locus functional dissection (contains t-statistics, expression fold-changes)
5. **PMC3779465**: Beclin 1 phagocytosis regulation (may contain phagocytic rate measurements)
6. **PMC3796170**: Gamma-secretase modulators (may contain IC50/EC50 values)
7. **PMC3699502**: AB oligomer Luminex assay (contains concentration measurements in CSF)
8. **PMC3726719**: ApoE and AD review (comprehensive, may cite parameter values)

