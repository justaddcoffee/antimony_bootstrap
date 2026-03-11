# Batch 21 Findings: Alzheimer's Disease Paper Analysis

**Date**: 2026-02-24
**Papers analyzed**: 86 (PMC3257571 - PMC3392960, Secondary_Alzforum)
**Focus**: Quantitative biological mechanisms extractable as ODE equations in Antimony format

---

## 1. Papers with Quantitative/Mechanistic Data

### Tier 1: Directly Extractable Quantitative Mechanisms

| PMC ID | Title | Mechanistic Value |
|--------|-------|-------------------|
| PMC3257571 | VPS35 haploinsufficiency increases AD neuropathology | VPS35/retromer regulation of BACE1 activity and Abeta production rates |
| PMC3274732 | SorCS1 regulates AD amyloid-beta metabolism via SorL1 and retromer | SorCS1/SorL1/retromer-mediated APP trafficking and Abeta metabolism quantification |
| PMC3280222 | Large aggregates are major soluble Abeta species in AD brain | Abeta aggregation size distribution data; density gradient fractionation kinetics |
| PMC3281584 | The many substrates of presenilin/gamma-secretase | Gamma-secretase cleavage rates for APP and other substrates; sequential proteolysis kinetics |
| PMC3310198 | Amyloid beta from axons and dendrites reduces local spine number | Subcellular Abeta secretion rates; spine density as function of Abeta concentration |
| PMC3319647 | Water-soluble and triton-soluble Abeta levels increased in AD brain | Compartmental Abeta concentration measurements (water-soluble vs membrane-bound) |
| PMC3325361 | C3 and CR3 contribute to phagocytosis and clearance of fibrillar Abeta | Complement-mediated microglial Abeta clearance rates; C3/CR3/Mac-1 kinetics |
| PMC3325794 | Abeta/Fyn-induced synaptic impairments depend on tau levels | Tau-dependent Fyn kinase activation rates; dose-response for Abeta-tau-Fyn pathway |
| PMC3351137 | Lysosomal proteolysis inhibition disrupts axonal transport | Lysosomal degradation rates; autophagy flux kinetics; axonal transport velocities |
| PMC3352936 | Hyperphosphorylation and cleavage at D421 enhance tau secretion | Tau phosphorylation and secretion rates; cleavage-dependent secretion kinetics |
| PMC3364747 | Mechanism of gamma-secretase dysfunction in FAD | Abeta42/Abeta40 ratio modulation by presenilin mutations; gamma-secretase processivity |
| PMC3376850 | Beta- but not gamma-secretase proteolysis of APP causes synaptic deficits | BACE1 vs gamma-secretase contribution to synaptic dysfunction; APP processing rates |
| PMC3383996 | Direct observation of interconversion of normal and toxic alpha-synuclein | Single-molecule aggregation kinetics; oligomer-to-fibril conversion rates |
| PMC3392942 | Lysosomal calcium homeostasis defects in PSEN-deficient cells | Lysosomal calcium flux rates; presenilin-dependent endo-lysosomal function |

### Tier 2: Mechanistic Insights Supporting Model Structure

| PMC ID | Title | Mechanistic Value |
|--------|-------|-------------------|
| PMC3270029 | Trans-synaptic spread of tau pathology in vivo | Tau propagation rates between connected brain regions; seeding kinetics |
| PMC3292759 | Propagation of tau pathology in early AD model | EC-to-hippocampus tau spread rates; P301L tau aggregation kinetics |
| PMC3293176 | Exogenous seeding of cerebral beta-amyloid deposition | Abeta seeding kinetics in transgenic rats; prion-like templating rates |
| PMC3299300 | Factors affecting Abeta plasma levels as biomarkers | Plasma Abeta40/Abeta42 clearance and production rates; peripheral compartment dynamics |
| PMC3308018 | Synergistic interactions between Abeta, tau, and alpha-synuclein | Cross-seeding kinetics; synergistic acceleration rates for multi-protein aggregation |
| PMC3314063 | PrPc ablation does not ameliorate neural dysfunction in J20 mice | PrPc-Abeta binding kinetics (negative result constraining model) |
| PMC3321383 | Linking lipids to AD: cholesterol and beyond | Cholesterol-dependent APP processing rates; lipid raft dynamics |
| PMC3323924 | Memory impairment in AD mice requires cellular prion protein | PrPc-dependent Abeta oligomer signaling rates |
| PMC3338985 | Probing sporadic and familial AD using iPSCs | APP processing and Abeta secretion rates in patient-derived neurons |
| PMC3353745 | The amyloid state of proteins in human diseases | Amyloid nucleation and elongation rate constants |
| PMC3366469 | Passive immunization targeting phospho-tau reduces functional decline | Antibody-mediated tau clearance rates |
| PMC3375906 | Inhibitory interneuron deficit links altered network activity and cognitive dysfunction | GABAergic interneuron loss rates; network excitability as function of Abeta |
| PMC3383058 | Early AD pathology in PiB-negative case | Abeta deposition threshold for PET detection; early plaque formation kinetics |
| PMC3383085 | Astrocyte glypicans promote excitatory synapse formation | Synapse formation rates via GluA1 AMPA receptors; astrocyte-neuron signaling |

### Tier 3: Qualitative Mechanistic Descriptions (Limited Quantitative Data)

| PMC ID | Title | Relevance |
|--------|-------|-----------|
| PMC3266529 | NIA-AA guidelines for neuropathologic assessment of AD | ABC scoring framework for staging pathology |
| PMC3268003 | NIA-AA neuropathologic assessment practical approach | Staging criteria for model validation |
| PMC3281757 | Functional links between Abeta toxicity and endocytic trafficking | PICALM/endocytic pathway interactions with Abeta |
| PMC3312472 | Pathophysiological framework of hippocampal dysfunction | Regional vulnerability patterns for spatial modeling |
| PMC3319071 | Alzheimer mechanisms and therapeutic strategies | Comprehensive mechanism review |
| PMC3319390 | The many faces of tau | Tau signaling and cytoskeletal functions |
| PMC3348110 | Prion-like spread of protein aggregates | General spreading mechanism framework |
| PMC3372647 | RNA-binding proteins with prion-like domains | Prion-like domain mechanisms in neurodegeneration |

---

## 2. Key Pathways Identified

### A. Amyloid-Beta Production and Processing
- **APP sequential proteolysis**: alpha/beta/gamma-secretase cleavage cascade (PMC3281584, PMC3364747, PMC3376850)
- **VPS35/retromer regulation of BACE1**: Retromer trafficking controls BACE1 access to APP (PMC3257571, PMC3274732)
- **SorCS1/SorL1 trafficking**: Sortilin family regulation of APP endosomal sorting (PMC3274732)
- **Lipid/cholesterol modulation**: Cholesterol-dependent APP processing in lipid rafts (PMC3321383)
- **Presenilin/gamma-secretase processivity**: FAD mutations alter Abeta42/40 ratio (PMC3364747)

### B. Amyloid-Beta Aggregation and Clearance
- **Abeta aggregation cascade**: Monomer to oligomer to protofibril to fibril (PMC3280222, PMC3353745)
- **Prion-like seeding**: Template-dependent Abeta nucleation and propagation (PMC3293176)
- **Complement-mediated clearance**: C3/CR3/Mac-1 microglial phagocytosis of fibrillar Abeta (PMC3325361)
- **Lysosomal degradation**: Autophagy-mediated Abeta clearance, impaired by PSEN mutations (PMC3351137, PMC3392942)
- **Peripheral clearance**: Plasma Abeta dynamics and brain-to-blood transport (PMC3299300)

### C. Tau Pathology and Propagation
- **Tau phosphorylation cascade**: Hyperphosphorylation enhances secretion (PMC3352936)
- **Trans-synaptic tau spread**: EC-II to dentate gyrus to CA regions propagation (PMC3270029, PMC3292759)
- **Tau-Fyn kinase interaction**: Abeta-triggered Fyn activation requires tau (PMC3325794)
- **Immunotherapy-mediated clearance**: Antibody-dependent tau aggregate removal (PMC3366469)

### D. Neuroinflammation
- **Microglial activation**: TSPO-mediated detection and response (PMC3323305, PMC3375234)
- **Complement cascade**: C3-dependent phagocytosis signaling (PMC3325361)
- **Astrocyte-mediated synapse regulation**: Glypican-dependent synaptogenesis (PMC3383085)

### E. Synaptic Dysfunction and Neurodegeneration
- **Abeta-dependent spine loss**: Local Abeta secretion reduces spine density (PMC3310198)
- **PrPc-Abeta oligomer signaling**: Prion protein as receptor for toxic oligomers (PMC3323924, PMC3314063)
- **Inhibitory interneuron loss**: GABAergic deficit causes network hypersynchrony (PMC3375906)
- **Presynaptic protein reserve**: Cognitive reserve linked to synaptic protein levels (PMC3365257)

### F. Endo-Lysosomal Dysfunction
- **Lysosomal proteolysis failure**: Impaired degradation causes axonal dystrophy (PMC3351137)
- **Presenilin-dependent lysosomal calcium**: PSEN loss disrupts lysosomal Ca2+ (PMC3392942)
- **Autophagy flux impairment**: Autophagic vacuole accumulation in axons (PMC3351137)

---

## 3. Extractable Reactions and Rate Laws

### 3.1 APP Processing Module

```antimony
# BACE1 cleavage of APP (Mass Action)
# Source: PMC3376850, PMC3281584
J_bace1_cleavage: APP_Neuron -> sAPPbeta_BrainISF + CTFbeta_Neuron; k_bace1 * APP_Neuron * BACE1_Neuron * V_Neuron

# Alpha-secretase cleavage of APP
J_alpha_cleavage: APP_Neuron -> sAPPalpha_BrainISF + CTFalpha_Neuron; k_alpha * APP_Neuron * V_Neuron

# Gamma-secretase cleavage of CTFbeta (produces Abeta40 and Abeta42)
J_gamma_40: CTFbeta_Neuron -> AB40_BrainISF + AICD_Neuron; k_gamma40 * CTFbeta_Neuron * PSEN1_Neuron * V_Neuron
J_gamma_42: CTFbeta_Neuron -> AB42_BrainISF + AICD_Neuron; k_gamma42 * CTFbeta_Neuron * PSEN1_Neuron * V_Neuron

# VPS35/retromer regulation of BACE1 (PMC3257571)
J_vps35_bace1_recycling: BACE1_Endosome -> BACE1_Membrane; k_vps35_recycle * BACE1_Endosome * VPS35_Neuron
```

### 3.2 Abeta Aggregation Module

```antimony
# Abeta monomer to oligomer nucleation (PMC3280222, PMC3353745)
J_ab_nucleation: 2 AB42_BrainISF -> AB42_oligomer_BrainISF; k_nuc * AB42_BrainISF^2 * V_BrainISF

# Oligomer elongation to protofibril (PMC3280222)
J_ab_elongation: AB42_oligomer_BrainISF + AB42_BrainISF -> AB42_protofibril_BrainISF; k_elong * AB42_oligomer_BrainISF * AB42_BrainISF * V_BrainISF

# Protofibril to fibril/plaque (PMC3293176)
J_ab_fibrillization: AB42_protofibril_BrainISF -> AB42_plaque_BrainParenchyma; k_fib * AB42_protofibril_BrainISF * V_BrainISF

# Seeded aggregation prion-like (PMC3293176)
J_ab_seeded: AB42_BrainISF + AB42_plaque_BrainParenchyma -> 2 AB42_plaque_BrainParenchyma; k_seed * AB42_BrainISF * AB42_plaque_BrainParenchyma
```

### 3.3 Abeta Clearance Module

```antimony
# Complement-mediated microglial phagocytosis (PMC3325361)
J_microglia_clearance: AB42_plaque_BrainParenchyma -> ; Vmax_phag * AB42_plaque_BrainParenchyma / (Km_phag + AB42_plaque_BrainParenchyma) * C3_BrainISF * Microglia_active_Brain * V_BrainParenchyma

# Lysosomal degradation of Abeta (PMC3351137)
J_lysosomal_degrad: AB42_Lysosome -> ; k_lys_deg * AB42_Lysosome * V_Neuron

# Peripheral clearance via blood-brain barrier (PMC3299300)
J_ab_bbb_efflux: AB42_BrainISF -> AB42_Plasma; k_bbb_efflux * AB42_BrainISF
```

### 3.4 Tau Phosphorylation and Propagation Module

```antimony
# Tau phosphorylation triggered by Abeta (PMC3352936)
J_tau_phosph: Tau_Neuron -> pTau_Neuron; k_tau_phosph * Tau_Neuron * AB42_oligomer_BrainISF * V_Neuron

# Phospho-tau secretion enhanced by hyperphosphorylation (PMC3352936)
J_ptau_secretion: pTau_Neuron -> pTau_BrainISF; k_ptau_sec * pTau_Neuron * V_Neuron

# Tau cleavage at D421 enhances secretion (PMC3352936)
J_tau_cleavage: pTau_Neuron -> pTau_cleaved_Neuron; k_tau_cleave * pTau_Neuron * Caspase_Neuron * V_Neuron
J_cleaved_tau_sec: pTau_cleaved_Neuron -> pTau_cleaved_BrainISF; k_cleaved_sec * pTau_cleaved_Neuron * V_Neuron

# Trans-synaptic tau spread (PMC3270029, PMC3292759)
J_tau_spread_EC_to_DG: pTau_EC -> pTau_DG; k_tau_spread * pTau_EC * connectivity_EC_DG
J_tau_spread_DG_to_CA: pTau_DG -> pTau_CA; k_tau_spread * pTau_DG * connectivity_DG_CA

# Fyn kinase activation by Abeta-tau (PMC3325794)
J_fyn_activation: Fyn_inactive_Neuron -> Fyn_active_Neuron; k_fyn_act * Fyn_inactive_Neuron * AB42_oligomer_BrainISF * Tau_Neuron * V_Neuron
```

### 3.5 Abeta-Dependent Synaptic Dysfunction Module

```antimony
# Abeta-mediated spine loss (PMC3310198)
J_spine_loss: Spines_Neuron -> ; k_spine_loss * Spines_Neuron * AB42_oligomer_BrainISF * V_Neuron

# PrPc-Abeta oligomer binding (PMC3323924)
J_prpc_ab_binding: PrPc_Neuron + AB42_oligomer_BrainISF -> PrPc_AB_complex_Neuron; k_prpc_bind * PrPc_Neuron * AB42_oligomer_BrainISF * V_Neuron

# Interneuron loss from Abeta exposure (PMC3375906)
J_interneuron_loss: GABAergic_Interneuron -> ; k_intern_loss * GABAergic_Interneuron * AB42_oligomer_BrainISF * V_Brain
```

### 3.6 Neuroinflammation Module

```antimony
# Microglial activation by Abeta plaques (PMC3325361, PMC3375234)
J_microglia_activation: Microglia_resting_Brain -> Microglia_active_Brain; k_mg_act * Microglia_resting_Brain * AB42_plaque_BrainParenchyma * V_Brain

# Complement C3 production by activated microglia (PMC3325361)
J_c3_production: -> C3_BrainISF; k_c3_prod * Microglia_active_Brain * V_Brain

# C3 opsonization of Abeta plaques
J_c3_opsonization: C3_BrainISF + AB42_plaque_BrainParenchyma -> C3_AB_complex_BrainParenchyma; k_c3_ops * C3_BrainISF * AB42_plaque_BrainParenchyma * V_BrainParenchyma
```

### 3.7 Endo-Lysosomal Dysfunction Module

```antimony
# Autophagosome formation (PMC3351137)
J_autophagosome_form: -> Autophagosome_Neuron; k_auto_form * V_Neuron

# Autophagosome-lysosome fusion
J_auto_lys_fusion: Autophagosome_Neuron + Lysosome_Neuron -> Autolysosome_Neuron; k_fusion * Autophagosome_Neuron * Lysosome_Neuron * V_Neuron

# Lysosomal calcium leak PSEN-dependent (PMC3392942)
J_lys_ca_leak: Ca_Lysosome -> Ca_Cytosol; k_ca_leak * Ca_Lysosome * (1 - PSEN1_Neuron / PSEN1_normal) * V_Neuron

# Impaired lysosomal proteolysis causes AV accumulation (PMC3351137)
J_av_degradation: Autolysosome_Neuron -> ; k_av_degrad * Autolysosome_Neuron * Cathepsin_Neuron * V_Neuron
```

### 3.8 Alpha-Synuclein Cross-Seeding Module

```antimony
# Alpha-synuclein oligomerization (PMC3383996)
J_asyn_oligomer: 2 aSyn_Neuron -> aSyn_oligomer_Neuron; k_asyn_olig * aSyn_Neuron^2 * V_Neuron

# Oligomer conformational conversion key toxic step (PMC3383996)
J_asyn_conversion: aSyn_oligomer_Neuron -> aSyn_toxic_oligomer_Neuron; k_asyn_conv * aSyn_oligomer_Neuron * V_Neuron

# Cross-seeding with Abeta and tau (PMC3308018)
J_ab_asyn_cross_seed: AB42_oligomer_BrainISF + aSyn_Neuron -> aSyn_oligomer_Neuron; k_cross_seed_ab * AB42_oligomer_BrainISF * aSyn_Neuron * V_Neuron
J_tau_asyn_cross_seed: pTau_Neuron + aSyn_Neuron -> aSyn_oligomer_Neuron; k_cross_seed_tau * pTau_Neuron * aSyn_Neuron * V_Neuron
```

---

## 4. Species and Compartments

### Compartments

| Compartment | Description | Source Papers |
|-------------|-------------|---------------|
| Neuron | Neuronal cytoplasm (general) | PMC3310198, PMC3351137, PMC3352936 |
| BrainISF | Brain interstitial fluid | PMC3280222, PMC3319647, PMC3299300 |
| BrainParenchyma | Brain tissue/extracellular matrix | PMC3293176, PMC3325361 |
| Plasma | Blood plasma | PMC3299300 |
| Endosome | Endosomal compartment (within neuron) | PMC3257571, PMC3274732 |
| Lysosome | Lysosomal compartment (within neuron) | PMC3351137, PMC3392942 |
| EC | Entorhinal cortex (region-specific) | PMC3270029, PMC3292759 |
| DG | Dentate gyrus | PMC3270029, PMC3292759 |
| CA | CA1/CA3 hippocampal regions | PMC3270029, PMC3312472 |
| Brain | Whole brain (for diffuse processes) | PMC3325361, PMC3375234 |
| Membrane | Cell membrane/lipid rafts | PMC3321383 |

### Species

| Species | Compartment(s) | Description | Source |
|---------|-----------------|-------------|--------|
| APP | Neuron, Membrane | Amyloid precursor protein | PMC3281584, PMC3376850 |
| BACE1 | Neuron, Endosome, Membrane | Beta-secretase 1 | PMC3257571, PMC3376850 |
| PSEN1 | Neuron | Presenilin-1 / gamma-secretase | PMC3364747, PMC3392942 |
| VPS35 | Neuron | Retromer complex component | PMC3257571 |
| SorCS1 | Neuron | Sortilin family trafficking receptor | PMC3274732 |
| SorL1 | Neuron | SorLA/LR11 trafficking receptor | PMC3274732 |
| sAPPbeta | BrainISF | Soluble APP-beta fragment | PMC3281584 |
| sAPPalpha | BrainISF | Soluble APP-alpha fragment | PMC3281584 |
| CTFbeta | Neuron | C-terminal fragment beta | PMC3281584 |
| CTFalpha | Neuron | C-terminal fragment alpha | PMC3281584 |
| AICD | Neuron | APP intracellular domain | PMC3281584 |
| AB40 | BrainISF, Plasma | Amyloid-beta 40 | PMC3299300, PMC3364747 |
| AB42 | BrainISF, Plasma | Amyloid-beta 42 | PMC3280222, PMC3299300 |
| AB42_oligomer | BrainISF | Abeta42 soluble oligomers | PMC3280222, PMC3310198 |
| AB42_protofibril | BrainISF | Abeta42 protofibrils | PMC3280222 |
| AB42_plaque | BrainParenchyma | Fibrillar Abeta plaques | PMC3293176, PMC3325361 |
| Tau | Neuron | Unphosphorylated tau | PMC3319390, PMC3325794 |
| pTau | Neuron, BrainISF, EC, DG, CA | Hyperphosphorylated tau | PMC3352936, PMC3270029 |
| pTau_cleaved | Neuron, BrainISF | Caspase-cleaved phospho-tau | PMC3352936 |
| Fyn_inactive | Neuron | Inactive Fyn kinase | PMC3325794 |
| Fyn_active | Neuron | Active Fyn kinase | PMC3325794 |
| PrPc | Neuron | Cellular prion protein | PMC3323924, PMC3314063 |
| PrPc_AB_complex | Neuron | PrPc-Abeta oligomer complex | PMC3323924 |
| Spines | Neuron | Dendritic spines (synaptic density proxy) | PMC3310198, PMC3365257 |
| GABAergic_Interneuron | Brain | Inhibitory interneurons | PMC3375906 |
| Microglia_resting | Brain | Resting/surveilling microglia | PMC3325361, PMC3375234 |
| Microglia_active | Brain | Activated/phagocytic microglia | PMC3325361, PMC3375234 |
| C3 | BrainISF | Complement component C3 | PMC3325361 |
| C3_AB_complex | BrainParenchyma | C3-opsonized Abeta | PMC3325361 |
| Autophagosome | Neuron | Autophagic vacuoles | PMC3351137 |
| Lysosome_func | Neuron | Functional lysosomes | PMC3351137, PMC3392942 |
| Autolysosome | Neuron | Fused autophagosome-lysosome | PMC3351137 |
| Ca_Lysosome | Lysosome | Lysosomal calcium stores | PMC3392942 |
| Ca_Cytosol | Neuron | Cytosolic calcium | PMC3392942 |
| Cathepsin | Neuron | Lysosomal cathepsin proteases | PMC3351137 |
| Caspase | Neuron | Caspase (tau cleavage) | PMC3352936 |
| aSyn | Neuron | Alpha-synuclein monomer | PMC3383996, PMC3308018 |
| aSyn_oligomer | Neuron | Alpha-synuclein oligomers | PMC3383996 |
| aSyn_toxic_oligomer | Neuron | Compact proteinase-K-resistant oligomers | PMC3383996 |
| Cholesterol | Membrane | Membrane cholesterol | PMC3321383 |

---

## 5. Papers NOT Relevant to ODE Modeling

The following papers are primarily GWAS, bioinformatics tools, clinical criteria, neuroimaging methods, or unrelated to AD mechanisms, and do not contribute extractable ODE reactions:

- PMC3262952 (GWAS age-at-onset)
- PMC3267847 (CSF1R mutations, HDLS)
- PMC3268626 (Imaging genetics methods)
- PMC3270040 (Rare variant screening APP/PSEN)
- PMC3276165 (Genotype imputation methods)
- PMC3285143 (FTLD-TDP classification)
- PMC3285250 (TDP43 gain/loss of function review)
- PMC3286330 (C9ORF72 clinical features)
- PMC3286334 (FTD neuroimaging)
- PMC3296478 (Long-lived nuclear pore proteins)
- PMC3297825 (RNA-seq normalization)
- PMC3298368 (PLCG2 cold urticaria/immunodeficiency)
- PMC3299551 (Crohn disease loci)
- PMC3308021 (UDS neuropsychological calculator)
- PMC3309547 (Plasma biomarkers of depression)
- PMC3312024 (AD dementia diagnostic criteria)
- PMC3312027 (MCI diagnostic criteria)
- PMC3314964 (Bayesian cryo-EM methods)
- PMC3317783 (Plasma proteomics biomarkers)
- PMC3319279 (Dentate granule cells pattern separation)
- PMC3321732 (AD clinical trial placebo analysis)
- PMC3322258 (Depression in MCI neuroimaging)
- PMC3322381 (Bowtie 2 alignment tool)
- PMC3322422 (C9orf72 frequency study)
- PMC3322595 (phenix.refine crystallography)
- PMC3323305 (TSPO polymorphism PET)
- PMC3329969 (ADNI review paper)
- PMC3331862 (Clinical diagnosis accuracy)
- PMC3334321 (TopHat/Cufflinks RNA-seq)
- PMC3339565 (AD epidemiology review)
- PMC3343631 (Galectin-8 autophagy/bacteria)
- PMC3343696 (Phase transitions multi-valent proteins)
- PMC3343739 (AD Prevention Initiative trial design)
- PMC3345358 (Thy1-hAPP mouse behavioral phenotyping)
- PMC3346182 (IGV tool)
- PMC3354734 (Parkinson GWAS RIT2)
- PMC3356448 (Topological chromatin domains)
- PMC3365264 (AD GWAS additional loci)
- PMC3366726 (Voxelwise gene-wide association)
- PMC3368003 (Abeta volume loss requires phospho-tau qualitative)
- PMC3369937 (Brain eGWAS)
- PMC3371309 (Coronary risk and cerebral amyloid epidemiological)
- PMC3372647 (Prion-like domains review)
- PMC3383626 (Huntington ASO therapy)
- PMC3387980 (AD biomarker ordering)
- PMC3389460 (Longitudinal image analysis methods)
- PMC3392960 (APOE e4 network connectivity)

---

## 6. Summary and Priority Recommendations

### Highest-Priority Modules for Antimony Extraction

1. **APP Processing Module** (PMC3257571, PMC3274732, PMC3281584, PMC3364747, PMC3376850)
   - Most complete pathway with quantitative cleavage rate data
   - Directly maps to Elbert model APP processing reactions

2. **Abeta Aggregation Cascade** (PMC3280222, PMC3293176, PMC3353745)
   - Nucleation-elongation-fibrillization kinetics well characterized
   - Size-dependent toxicity data available

3. **Tau Phosphorylation and Trans-Synaptic Spread** (PMC3270029, PMC3292759, PMC3325794, PMC3352936)
   - Spatially resolved propagation data
   - Phosphorylation-secretion coupling quantified

4. **Microglial Complement Clearance** (PMC3325361, PMC3375234)
   - C3/CR3-dependent phagocytosis rates
   - Activation state dynamics

5. **Endo-Lysosomal/Autophagy Module** (PMC3351137, PMC3392942)
   - Presenilin-dependent lysosomal dysfunction
   - Connects to both Abeta and tau pathology

### Cross-Module Interactions to Capture
- Abeta oligomers trigger tau phosphorylation (via Fyn kinase, PMC3325794)
- Abeta-tau-aSyn cross-seeding (PMC3308018)
- Lysosomal dysfunction impairs Abeta/tau clearance (PMC3351137, PMC3392942)
- Microglial activation triggers complement cascade for plaque clearance (PMC3325361)
