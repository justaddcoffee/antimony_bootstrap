# Batch 17 Findings: Alzheimer's Paper Analysis for Antimony ODE Modeling

**Date**: 2026-02-24  
**Papers analyzed**: 86 (Secondary_Alzforum PMC2752218–PMC2867839)  
**Focus**: Extractable quantitative biological mechanisms for compartmental ODE models

---

## 1. Papers with Quantitative/Mechanistic Data

### Tier 1: High-value papers with directly extractable kinetic/mechanistic data

| PMC ID | Title | Key Quantitative Data |
|--------|-------|----------------------|
| PMC2787195 | Overexpression of LDLR in the Brain Markedly Inhibits Amyloid Deposition | LDLR-mediated Abeta clearance rates; apoE-Abeta binding; % reduction in Ab aggregation with LDLR overexpression |
| PMC2756291 | Characterizing the appearance and growth of amyloid plaques in APP/PS1 mice | Plaque growth rate ~0.7 um/week; concentration-dependent Ab aggregation kinetics in ISF; plaque appearance rates |
| PMC2755563 | Cystatin C-Cathepsin B Axis Regulates Amyloid Beta Levels | Cathepsin B-mediated Ab degradation rates; CysC inhibition constants; lysosomal Ab degradation kinetics |
| PMC2763626 | Synaptic activity reduces intraneuronal Ab, promotes APP transport to synapses | Activity-dependent APP trafficking rates; intraneuronal Ab reduction (%); neprilysin/IDE activity modulation |
| PMC2789838 | Amyloid-beta Dynamics are Regulated by Orexin and the Sleep-Wake Cycle | ISF Ab concentration dynamics; diurnal Ab fluctuation amplitudes; orexin-mediated Ab modulation |
| PMC2818651 | Distinct CSF amyloid beta peptide signatures (sporadic vs PSEN1) | Gamma-secretase cleavage specificity for Ab37/38/39/40/42; relative Ab isoform ratios in CSF |
| PMC2778845 | CD14 and TLR2/4 required for fibrillar Ab-stimulated microglial activation | fAb phagocytosis rates; TLR-dependent microglial activation thresholds; Ab clearance via phagocytosis |
| PMC2830092 | Cryo-EM Structure of Purified gamma-Secretase at 12A Resolution | gamma-secretase structural constraints on catalytic rate; substrate binding geometry |
| PMC2819840 | Hypothetical model of dynamic biomarkers of the AD pathological cascade | Biomarker trajectory model; temporal ordering of Ab, tau, synaptic, neurodegenerative cascades |
| PMC2776013 | Expression of SORL1 and a novel SORL1 splice variant in AD brain | SORL1-mediated APP trafficking to Golgi/endosomes; reduced SORL1 -> increased Ab production |
| PMC2812536 | Progranulin-deficient mice: exaggerated inflammation and neuropathology | Progranulin regulation of microglial activation; cytokine production rates; complement activation |
| PMC2838375 | Neuroprotective effects of BDNF in rodent and primate models of AD | BDNF-TrkB signaling rates; neuroprotective dose-response relationships |

### Tier 2: Papers with qualitative mechanistic insights (useful for model structure)

| PMC ID | Title | Mechanistic Insight |
|--------|-------|--------------------|
| PMC2782414 | Biochemical analysis of AD mouse model (J20) | Multiple Ab aggregation states: monomers, oligomers, protofibrils, fibrils in brain |
| PMC2813509 | Alzheimer's Disease and the beta-Amyloid Peptide | Review: Ab production/degradation balance; BBB efflux predicts amyloid burden |
| PMC2864360 | Structural and functional changes in tau mutant mice neurons | Tau pathology independent of NFT formation; soluble tau species cause dysfunction |
| PMC2759694 | Interaction of Reelin with APP promotes neurite outgrowth | Reelin-APP-LDLR pathway for Ab processing |
| PMC2760256 | Age-dependent impairment of synaptic function in htau mice | Tau accumulation kinetics; synaptic impairment progression |
| PMC2834890 | Immune activation in brain aging and neurodegeneration | Microglial activation states; neuroinflammatory feedback loops |
| PMC2823849 | Inflammation, Microglia and Alzheimer's Disease | Microglial phenotype switching; cytokine-mediated neuroinflammation |
| PMC2806678 | CSF tau and ptau181 increase with cortical amyloid deposition | Quantitative CSF tau/ptau as function of amyloid load |
| PMC2830375 | APOE Predicts Ab but not Tau AD Pathology | APOE genotype-specific Ab deposition rates |
| PMC2831066 | The AD-Associated Ab-Protein Is an Antimicrobial Peptide | Ab antimicrobial function; innate immune-Ab production link |
| PMC2855368 | Age-Dependent Cortical Neuronal Degeneration in Presenilin cKO | Presenilin loss -> neurodegeneration kinetics; age-dependent cortical volume loss |
| PMC2845852 | Tau isoform regulation is region and cell-specific in mouse brain | Region-specific tau isoform expression ratios |
| PMC2801051 | Axonal Transport Defects in Neurodegenerative Diseases | Axonal transport rates; deficits in APP/tau transport |
| PMC2799634 | Astrocytes: biology and pathology | Astrocyte roles in Ab clearance, glutamate buffering, BBB maintenance |
| PMC2867291 | Regulation of learning and memory by meningeal immunity (IL-4) | IL-4 mediated immune-cognitive coupling; meningeal T-cell cytokine production |

### Tier 3: Imaging/biomarker/clinical papers (parameter constraints only)

| PMC ID | Title | Constraint Type |
|--------|-------|----------------|
| PMC2752218 | Alzheimer's and Cognitive Reserve | PIB-PET amyloid quantification |
| PMC2759394 | CSF biomarkers and rate of cognitive decline | CSF biomarker decline rates |
| PMC2763631 | Decreased CSF Ab42 correlates with brain atrophy | CSF-brain Ab relationship |
| PMC2796577 | Cognitive decline and brain volume loss are signatures of cerebral Ab | Ab deposition-cognition relationship |
| PMC2804478 | Amyloid Imaging in Aging and Dementia | PIB kinetics in aging |
| PMC2828870 | Amyloid Imaging in MCI Subtypes | Ab deposition patterns |
| PMC2867838 | Update on Biomarker Core of ADNI | Longitudinal biomarker trajectories |
| PMC2867839 | ADNI: Annual Change in Biomarkers and Clinical Outcomes | Annual biomarker change rates |

---

## 2. Key Pathways Identified

### A. Amyloid-beta Production and Processing
- **APP processing by secretases**: gamma-secretase (presenilin-dependent) cleaves APP to generate Ab40/Ab42 isoforms; specificity modulated by PSEN1 mutations (PMC2818651, PMC2830092)
- **SORL1/SORLA trafficking**: SORL1 directs APP to Golgi/endosomes, reducing Ab production; decreased SORL1 -> increased Ab (PMC2776013)
- **Reelin-APP interaction**: Reelin promotes APP processing through LDLR pathway (PMC2759694)

### B. Amyloid-beta Clearance and Degradation
- **Enzymatic degradation**: Neprilysin, IDE, Cathepsin B degrade Ab; Cystatin C inhibits Cathepsin B (PMC2755563)
- **LDLR-mediated clearance**: LDLR overexpression dramatically reduces Ab aggregation and enhances clearance from brain extracellular space (PMC2787195)
- **Microglial phagocytosis**: CD14/TLR2/TLR4-dependent fibrillar Ab phagocytosis (PMC2778845)
- **BBB transport**: Net Ab efflux across BBB predicts cerebral amyloid burden (PMC2813509)

### C. Amyloid-beta Aggregation
- **Concentration-dependent aggregation**: ISF Ab concentration determines aggregation rate; monomer -> oligomer -> protofibril -> fibril -> plaque (PMC2756291, PMC2782414)
- **Plaque growth kinetics**: Linear growth rate ~0.7 um/week in APP/PS1 mice (PMC2756291)
- **Sleep-wake modulation**: Orexin and synaptic activity modulate ISF Ab levels, affecting aggregation (PMC2789838)

### D. Tau Pathology
- **Tau aggregation**: Independent of NFTs; soluble tau species cause synaptic dysfunction (PMC2864360)
- **Tau isoform regulation**: Region and cell-specific expression ratios (PMC2845852)
- **Age-dependent accumulation**: Progressive tau accumulation with synaptic impairment (PMC2760256)

### E. Neuroinflammation
- **Microglial activation**: TLR2/4/CD14-dependent activation by fibrillar Ab (PMC2778845)
- **Progranulin regulation**: Progranulin deficiency -> exaggerated inflammation (PMC2812536)
- **Cytokine cascades**: TNF, IL-1, IL-4, IL-6 production by activated microglia/macrophages (PMC2788152, PMC2867291)
- **Dual macrophage phenotypes**: Neurotoxic vs neuroprotective subsets (PMC2788152)

### F. Neuroprotection and Synaptic Function
- **BDNF-TrkB signaling**: Neuroprotective effects in AD models (PMC2838375)
- **Synaptic activity**: Reduces intraneuronal Ab, promotes APP transport to synapses (PMC2763626)
- **Nuclear pore deterioration**: Age-dependent loss of nuclear integrity (PMC2805151)

---

## 3. Extractable Reactions and Rate Laws

### Amyloid-beta Production

```
# APP cleavage by beta-secretase (BACE1)
# Rate type: MA (mass action)
R_BACE_cleavage: APP_Neuron => sAPPb_Neuron + CTFb_Neuron; k_BACE * APP_Neuron * V_Neuron
# Source: PMC2813509, PMC2818651

# CTFbeta cleavage by gamma-secretase producing Ab40 and Ab42
# Rate type: custom_conc_per_time (Michaelis-Menten)
R_gamma_Ab42: CTFb_Neuron => Ab42_Neuron; (Vmax_gamma42 * CTFb_Neuron / (Km_gamma + CTFb_Neuron)) * V_Neuron
R_gamma_Ab40: CTFb_Neuron => Ab40_Neuron; (Vmax_gamma40 * CTFb_Neuron / (Km_gamma + CTFb_Neuron)) * V_Neuron
# Source: PMC2818651 (Ab40:Ab42 ratio ~9:1 in normal, altered by PSEN1 mutations)
# PMC2830092 (gamma-secretase structure constrains kinetics)

# SORL1-mediated APP recycling (reduces Ab production)
# Rate type: MA
R_SORL1_recycle: APP_Endosome => APP_Golgi; k_SORL1 * APP_Endosome * SORL1_Endosome * V_Endosome
# Source: PMC2776013
```

### Amyloid-beta Degradation and Clearance

```
# Cathepsin B-mediated Ab degradation (inhibited by Cystatin C)
# Rate type: custom_conc_per_time (competitive inhibition)
R_CatB_degrade: Ab42_Lysosome => ; (kcat_CatB * CatB_Lysosome * Ab42_Lysosome / (Km_CatB * (1 + CysC_Lysosome/Ki_CysC) + Ab42_Lysosome)) * V_Lysosome
# Source: PMC2755563

# Neprilysin-mediated Ab degradation
# Rate type: custom_conc_per_time (Michaelis-Menten)
R_NEP_degrade: Ab42_BrainISF => ; (Vmax_NEP * Ab42_BrainISF / (Km_NEP + Ab42_BrainISF)) * V_BrainISF
# Source: PMC2763626, PMC2813509

# IDE-mediated Ab degradation
# Rate type: custom_conc_per_time (Michaelis-Menten)
R_IDE_degrade: Ab42_BrainISF => ; (Vmax_IDE * Ab42_BrainISF / (Km_IDE + Ab42_BrainISF)) * V_BrainISF
# Source: PMC2755563, PMC2813509

# LDLR-mediated Ab clearance (apoE-dependent)
# Rate type: MA
R_LDLR_clearance: Ab42_BrainISF => Ab42_degraded; k_LDLR * LDLR_Neuron * apoE_Ab42_BrainISF * V_BrainISF
# Source: PMC2787195

# Microglial phagocytic clearance of fibrillar Ab (TLR2/4 and CD14 dependent)
# Rate type: custom_conc_per_time (saturable)
R_phago_fAb: fAb_BrainISF => ; (k_phago * Microglia_active * fAb_BrainISF / (Km_phago + fAb_BrainISF)) * V_BrainISF
# Requires: CD14, TLR2, TLR4 expression on microglia
# Source: PMC2778845

# BBB-mediated Ab efflux (LRP1-dependent)
# Rate type: UDF (unidirectional flow)
R_BBB_efflux: Ab42_BrainISF => Ab42_Plasma; k_BBB_efflux * Ab42_BrainISF
# Source: PMC2813509
```

### Amyloid-beta Aggregation

```
# Concentration-dependent Ab aggregation: monomer -> oligomer
# Rate type: custom_conc_per_time (second-order nucleation)
R_Ab_oligomerize: 2 Ab42_BrainISF => Ab42_oligomer_BrainISF; k_nuc * Ab42_BrainISF^2 * V_BrainISF
# Source: PMC2756291 (concentration-dependent), PMC2782414 (multiple aggregation states)

# Oligomer -> protofibril elongation
# Rate type: MA
R_Ab_elongate: Ab42_oligomer_BrainISF + Ab42_BrainISF => Ab42_protofibril_BrainISF; k_elong * Ab42_oligomer_BrainISF * Ab42_BrainISF * V_BrainISF
# Source: PMC2756291

# Protofibril -> fibril/plaque deposition
# Rate type: MA
R_Ab_deposit: Ab42_protofibril_BrainISF => Ab42_plaque_Brain; k_deposit * Ab42_protofibril_BrainISF * V_BrainISF
# Source: PMC2756291 (plaque growth ~0.7 um/week)
```

### Amyloid-beta Dynamics (Sleep-Wake Modulation)

```
# Orexin-stimulated Ab release (synaptic activity dependent)
# Rate type: custom_conc_per_time
R_orexin_Ab: => Ab42_BrainISF; k_orexin * Orexin_BrainISF * SynapticActivity * V_BrainISF
# Source: PMC2789838

# Synaptic activity reduces intraneuronal Ab and promotes extracellular release
# Rate type: UDF
R_synapse_Ab_release: Ab42_Neuron => Ab42_BrainISF; k_syn_release * SynapticActivity * Ab42_Neuron
# Source: PMC2763626
```

### Tau Pathology

```
# Tau phosphorylation (multiple kinases)
# Rate type: custom_conc_per_time
R_tau_phospho: Tau_Neuron => pTau_Neuron; (k_GSK3 * GSK3_active + k_CDK5 * CDK5_active) * Tau_Neuron * V_Neuron
# Source: PMC2864360, PMC2760256

# Tau dephosphorylation (PP2A-mediated)
# Rate type: custom_conc_per_time
R_tau_dephospho: pTau_Neuron => Tau_Neuron; k_PP2A * PP2A_active * pTau_Neuron * V_Neuron
# Source: PMC2864360

# Soluble pTau aggregation (age-dependent, concentration-dependent)
# Rate type: custom_conc_per_time
R_tau_aggregate: 2 pTau_Neuron => pTau_aggregate_Neuron; k_tau_agg * pTau_Neuron^2 * V_Neuron
# Source: PMC2760256, PMC2864360 (NFT-independent toxicity)

# Tau release to CSF
# Rate type: UDF
R_tau_CSF: Tau_Neuron => Tau_CSF; k_tau_release * Tau_Neuron
# Source: PMC2806678, PMC2828879
```

### Neuroinflammation

```
# Microglial activation by fibrillar Ab (TLR2/4/CD14 dependent)
# Rate type: custom_conc_per_time (Hill-type)
R_microglia_activate: Microglia_resting => Microglia_active; k_act * fAb_BrainISF^n / (Kd_act^n + fAb_BrainISF^n) * Microglia_resting * V_BrainISF
# Source: PMC2778845

# Pro-inflammatory cytokine production by activated microglia
# Rate type: MA
R_TNF_prod: => TNF_BrainISF; k_TNF * Microglia_active * V_BrainISF
R_IL1_prod: => IL1_BrainISF; k_IL1 * Microglia_active * V_BrainISF
R_IL6_prod: => IL6_BrainISF; k_IL6 * Microglia_active * V_BrainISF
# Source: PMC2778845, PMC2812536, PMC2788152

# Anti-inflammatory IL-4 from meningeal T-cells
# Rate type: MA
R_IL4_prod: => IL4_BrainISF; k_IL4 * Tcell_meningeal * V_BrainISF
# Source: PMC2867291

# Progranulin-mediated inflammation regulation
# Rate type: custom_conc_per_time (inhibitory)
R_PGRN_antiinflam: Microglia_active => Microglia_resting; k_PGRN * PGRN_BrainISF * Microglia_active * V_BrainISF
# Source: PMC2812536
```

### Neuroprotection (BDNF)

```
# BDNF-TrkB signaling (neuroprotective)
# Rate type: custom_conc_per_time (saturable binding)
R_BDNF_signal: BDNF_BrainISF + TrkB_Neuron => BDNF_TrkB_Neuron; k_BDNF_bind * BDNF_BrainISF * TrkB_Neuron * V_BrainISF
# Source: PMC2838375

# BDNF-mediated synaptic maintenance
# Rate type: MA
R_BDNF_synapse: => Synapse_Neuron; k_syn_maint * BDNF_TrkB_Neuron * V_Neuron
# Source: PMC2838375
```

---

## 4. Species and Compartments

### Compartments

| Compartment | Description | Source Papers |
|-------------|-------------|---------------|
| Neuron | Neuronal intracellular space | PMC2763626, PMC2864360, PMC2855368 |
| BrainISF | Brain interstitial fluid (extracellular) | PMC2789838, PMC2787195, PMC2756291 |
| CSF | Cerebrospinal fluid | PMC2818651, PMC2806678, PMC2828879 |
| Plasma | Blood plasma | PMC2813509, PMC2830375 |
| Lysosome | Lysosomal compartment | PMC2755563 |
| Endosome | Endosomal compartment | PMC2776013 |
| Golgi | Golgi apparatus | PMC2776013 |
| Brain | Brain parenchyma (for deposited species) | PMC2756291 |
| Meninges | Meningeal immune compartment | PMC2867291 |

### Species

| Species | Compartment(s) | Description | Key Papers |
|---------|----------------|-------------|------------|
| APP | Neuron, Endosome, Golgi | Amyloid precursor protein | PMC2776013, PMC2763626 |
| sAPPb | Neuron, BrainISF | Soluble APP-beta fragment | PMC2813509 |
| CTFb | Neuron | C-terminal fragment beta | PMC2818651 |
| Ab40 | Neuron, BrainISF, CSF, Plasma | Amyloid-beta 40 | PMC2818651 |
| Ab42 | Neuron, BrainISF, CSF, Plasma | Amyloid-beta 42 | PMC2789838, PMC2818651 |
| Ab42_oligomer | BrainISF | Ab42 oligomers | PMC2782414, PMC2819840 |
| Ab42_protofibril | BrainISF | Ab42 protofibrils | PMC2782414 |
| fAb | BrainISF | Fibrillar amyloid-beta | PMC2778845, PMC2756291 |
| Ab42_plaque | Brain | Deposited amyloid plaques | PMC2756291 |
| apoE | BrainISF | Apolipoprotein E | PMC2787195, PMC2830375 |
| apoE_Ab42 | BrainISF | ApoE-Ab42 complex | PMC2787195 |
| LDLR | Neuron | LDL receptor | PMC2787195 |
| SORL1 | Endosome | Sortilin-related receptor | PMC2776013 |
| CatB | Lysosome | Cathepsin B | PMC2755563 |
| CysC | Lysosome | Cystatin C | PMC2755563 |
| NEP | BrainISF | Neprilysin | PMC2763626, PMC2813509 |
| IDE | BrainISF | Insulin-degrading enzyme | PMC2755563, PMC2813509 |
| Tau | Neuron, CSF | Total tau protein | PMC2864360, PMC2806678 |
| pTau | Neuron, CSF | Phosphorylated tau | PMC2864360, PMC2806678 |
| pTau_aggregate | Neuron | Aggregated phospho-tau | PMC2760256 |
| GSK3_active | Neuron | Active GSK3-beta kinase | PMC2864360 |
| CDK5_active | Neuron | Active CDK5 kinase | PMC2864360 |
| PP2A_active | Neuron | Active PP2A phosphatase | PMC2864360 |
| Microglia_resting | BrainISF | Resting microglia | PMC2778845, PMC2823849 |
| Microglia_active | BrainISF | Activated microglia | PMC2778845, PMC2812536 |
| TNF | BrainISF | Tumor necrosis factor alpha | PMC2788152, PMC2812536 |
| IL1 | BrainISF | Interleukin-1 beta | PMC2788152, PMC2812536 |
| IL4 | BrainISF | Interleukin-4 | PMC2867291 |
| IL6 | BrainISF | Interleukin-6 | PMC2788152 |
| BDNF | BrainISF | Brain-derived neurotrophic factor | PMC2838375 |
| TrkB | Neuron | BDNF receptor | PMC2838375 |
| BDNF_TrkB | Neuron | Activated BDNF-TrkB complex | PMC2838375 |
| PGRN | BrainISF | Progranulin | PMC2812536 |
| Orexin | BrainISF | Orexin/hypocretin | PMC2789838 |
| Synapse | Neuron | Synaptic density marker | PMC2838375, PMC2763626 |
| Tcell_meningeal | Meninges | Meningeal T-cells | PMC2867291 |

---

## 5. Summary and Prioritization

### Most Impactful Modules Extractable from This Batch

1. **Ab clearance module** (PMC2787195, PMC2755563, PMC2778845, PMC2813509): LDLR, Cathepsin B/CysC, neprilysin, IDE, microglial phagocytosis, BBB efflux - comprehensive clearance pathways with multiple rate laws
2. **Ab aggregation module** (PMC2756291, PMC2782414): Concentration-dependent nucleation -> oligomerization -> fibril -> plaque with measured growth kinetics
3. **Gamma-secretase/APP processing module** (PMC2818651, PMC2830092, PMC2776013): SORL1-dependent APP trafficking, gamma-secretase cleavage specificity for Ab isoforms
4. **Sleep-wake Ab dynamics module** (PMC2789838, PMC2763626): Orexin and synaptic activity modulation of ISF Ab levels
5. **Neuroinflammation module** (PMC2778845, PMC2812536, PMC2788152, PMC2867291): TLR/CD14-mediated microglial activation, cytokine cascades, progranulin regulation, IL-4 anti-inflammatory pathway
6. **Tau pathology module** (PMC2864360, PMC2760256, PMC2845852): Tau phosphorylation/aggregation kinetics, NFT-independent toxicity, isoform regulation
7. **BDNF neuroprotection module** (PMC2838375): BDNF-TrkB signaling for synaptic maintenance

### Papers with No Extractable Mechanistic Data (bioinformatics/methods/genetics only)

PMC2756411 (transcriptomics), PMC2756723 (stem cell methods), PMC2773131 (ML classification), PMC2787725 (GWAS Parkinson's), PMC2787842 (dementia diagnosis), PMC2796818 (edgeR software), PMC2803126 (MolProbity software), PMC2815665 (XDS software), PMC2815670 (PHENIX software), PMC2828108 (BWA software), PMC2828525 (GWAS FTLD), PMC2831613 (missing heritability), PMC2832824 (BEDTools software), PMC2845877 (GWAS CLU/PICALM), PMC2848547 (eQTL methods), PMC2850052 (genetic screening), PMC2852313 (Coot software), PMC2853717 (GWAS Parkinson's SNCA/MAPT), PMC2855889 (PolyPhen2 software), PMC2856322 (GBA mutations Parkinson's), PMC2858594 (Hi-C chromosome folding), PMC2862121 (behavioral phenotyping Parkinson's), PMC2864565 (TMM normalization RNA-seq), PMC2866090 (alpha-synuclein histopathology)
