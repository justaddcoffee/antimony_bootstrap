# Batch 18 Paper Analysis: Quantitative Mechanisms for Alzheimer's ODE Modeling

**Date:** 2026-02-24
**Papers analyzed:** 86 (from Secondary_Alzforum collection, PMC2867843-PMC3000457)
**Purpose:** Identify extractable quantitative biological mechanisms for Antimony ODE models

---

## 1. Papers with Quantitative/Mechanistic Data

### Tier 1: Strong Quantitative Data (directly extractable kinetics/parameters)

#### PMC2987723 - Abeta dimers rapidly form stable synaptotoxic protofibrils
- **Key finding:** Abeta dimer aggregation kinetics measured experimentally
- **Quantitative data:**
  - Apparent rate constant for (AbetaS26C)2 protofibril formation: **k = 0.085 +/- 0.03 h^-1** (single exponential fit, R2 = 0.96)
  - Aggregation threshold: no ThT binding at dimer concentrations <= 2.5 uM; aggregation at >= 1.25 uM for dimers vs >= 5 uM for monomers
  - Protofibril dimensions: width ~5.8 nm, length grows from 59 nm (day 1) to 139 nm (day 3) to 284 nm (day 30)
  - ~40% material remains soluble after centrifugation at 16,000g
- **Extractable reactions:** Abeta monomer -> dimer -> protofibril -> fibril aggregation cascade
- **Relevance:** Core amyloid aggregation module

#### PMC2947312 - Modulation of gamma-Secretase Reduces beta-Amyloid Deposition
- **Key finding:** Gamma-secretase modulator (GSM) IC50 values and in vivo Abeta reduction
- **Quantitative data:**
  - Initial hit IC50 for Abeta42 inhibition: 15 uM
  - Optimized Series A GSM IC50s: low nanomolar range (~29 nM for Compound 4)
  - No NICD inhibition at concentrations >=1000-fold above Abeta42 IC50 (30 uM)
  - In vivo chronic dosing (29 weeks): DEA-extractable Abeta reduced to 24% of control (Abeta38, Abeta40, Abeta42 all reduced)
  - SDS-extractable: reduced to 41-52% of control
  - FA-extractable: reduced to 45-55% of control
  - PK: Tmax = 3 h (oral), bioavailability F = 49%
- **Extractable reactions:** APP -> C99 -> Abeta (gamma-secretase cleavage), with modulator effects on Abeta38/40/42 ratio
- **Relevance:** APP processing / secretase module, therapeutic intervention modeling

#### PMC2879048 - The beta-Secretase Enzyme BACE in Health and Alzheimer's Disease
- **Key finding:** BACE1 cleavage efficiency and regulation
- **Quantitative data:**
  - BACE cleaves APPswe ~10-100 fold more efficiently than wild-type APP
  - BACE1 knockout mice are viable (baseline for BACE inhibition modeling)
- **Extractable reactions:** APP -> sAPPbeta + C99 (BACE1 cleavage), regulation by trafficking/expression
- **Relevance:** APP processing module, BACE1 kinetics

#### PMC2879045 - The secretases: enzymes with therapeutic potential in Alzheimer disease
- **Key finding:** Comprehensive review of alpha-, beta-, gamma-secretase pathways
- **Quantitative data:**
  - PKC, MAPK, tyrosine kinase, and calcium pathways regulate alpha-secretase activity
  - BACE1 knockout abolishes Abeta production in vivo
  - Series A GSMs are 1000-10,000x more potent than tarenflurbil/sulindac sulfide
- **Extractable reactions:** Complete APP processing cascade: alpha-secretase (non-amyloidogenic) vs beta-secretase (amyloidogenic) pathway
- **Relevance:** Core APP processing module

#### PMC2902368 - BACE1 deficiency causes altered neuronal activity and neurodegeneration
- **Key finding:** BACE1 knockout effects on neuronal activity and NaV1.1 processing
- **Quantitative data:** Qualitative but important for BACE1 substrate considerations
- **Extractable reactions:** BACE1 -> NaV1.1 cleavage (off-target effects of BACE inhibition)
- **Relevance:** BACE1 inhibition side-effect modeling

### Tier 2: Mechanistic Pathway Data (qualitative mechanisms with some parameters)

#### PMC2906098 - Role of presenilins in neuronal calcium homeostasis
- **Key finding:** Presenilin mutations cause ER calcium dysregulation
- **Quantitative data:**
  - Intracellular Ca2+ concentrations: resting ~100 nM, ER store ~140-500 uM
  - FAD mutations cause supranormal Ca2+ release via InsP3 receptors
  - Ryanodine receptor (RyR) and store-operated calcium entry (SOC) affected
- **Extractable reactions:**
  - ER_Ca2+ -> Cytosol_Ca2+ (InsP3R-mediated release, enhanced by PS1 mutations)
  - Extracellular_Ca2+ -> Cytosol_Ca2+ (SOC entry, reduced by ER overfilling)
  - Cytosol_Ca2+ -> ER_Ca2+ (SERCA pump)
- **Relevance:** Calcium homeostasis module

#### PMC2898196 - Gain-of-function enhancement of InsP3 receptor modal gating by PS mutants
- **Key finding:** FAD presenilin mutations enhance InsP3R channel open probability
- **Quantitative data:**
  - InsP3 concentrations tested: 100 nM, 1 uM, 10 uM
  - Modal gating analysis shows increased high-activity mode probability
- **Extractable reactions:** InsP3 + InsP3R -> Ca2+ release (enhanced by PS1 mutations)
- **Relevance:** Calcium signaling module, InsP3R kinetics

#### PMC2944253 - NMDA-mediated Ca2+ influx drives aberrant ryanodine receptor activation
- **Key finding:** NMDA receptor -> RyR calcium signaling cascade is aberrant in young AD mice
- **Quantitative data:**
  - Caffeine-evoked Ca2+ release: measurable differences between WT and 3xTg-AD
  - NMDA-evoked responses show aberrant RyR recruitment
- **Extractable reactions:**
  - Glutamate + NMDAR -> Ca2+ influx
  - Ca2+ + RyR -> ER_Ca2+ release (CICR, calcium-induced calcium release)
  - Aberrant CICR in AD context
- **Relevance:** Synaptic calcium / excitotoxicity module

#### PMC2884172 - Synchronous Hyperactivity and Intercellular Calcium Waves in Astrocytes
- **Key finding:** Astrocytes near amyloid plaques show calcium hyperactivity
- **Quantitative data:**
  - Resting Ca2+ in astrocytes: 81 nM (control) vs 149 nM (near plaques)
  - Calcium wave propagation distances: ~100 um from plaques
- **Extractable reactions:**
  - Abeta_plaque -> Astrocyte_Ca2+ elevation
  - Astrocyte_Ca2+ -> intercellular calcium wave propagation
- **Relevance:** Neuroinflammation / astrocyte activation module

#### PMC2908393 - Apolipoprotein E and its receptors in AD: pathways, pathogenesis, therapy
- **Key finding:** Comprehensive ApoE pathway review
- **Quantitative data:**
  - ApoE4 carriers: AD incidence rate 8.3x higher
  - ApoE affects Abeta clearance, aggregation, and tau phosphorylation
- **Extractable reactions:**
  - ApoE + Abeta -> ApoE-Abeta complex (clearance pathway)
  - ApoE + LRP1/LDLR -> receptor-mediated endocytosis
  - ApoE4 impairs Abeta clearance vs ApoE2/E3
- **Relevance:** ApoE / lipid metabolism module

#### PMC2997622 - Deletion of CD14 attenuates AD pathology
- **Key finding:** CD14 (TLR co-receptor) deletion reduces neuroinflammation and plaque burden
- **Quantitative data:**
  - CD14 knockout reduces plaque deposition
  - M1 vs M2 microglial phenotype shift
  - TLR2/TLR4 signaling modulation
- **Extractable reactions:**
  - fAbeta + CD14/TLR4 -> NF-kB activation -> proinflammatory cytokines
  - Microglia_M0 -> Microglia_M1 (classical activation via TLR)
  - Microglia_M0 -> Microglia_M2 (alternative activation)
- **Relevance:** Neuroinflammation / microglial activation module

#### PMC2873093 - Mechanisms Underlying Inflammation in Neurodegeneration
- **Key finding:** Comprehensive review of neuroinflammatory pathways
- **Quantitative data:** Qualitative but detailed pathway descriptions
- **Extractable reactions:**
  - TLR -> MyD88/TRIF -> IkB kinase -> NF-kB -> cytokine production
  - IFN-gamma -> M1 activation; IL-4/IL-13 -> M2 activation
  - SOCS proteins, ATF3, Nurr1 as negative feedback regulators
  - Scavenger receptor-mediated Abeta uptake by microglia
- **Relevance:** Neuroinflammation module (multiple reaction pathways)

#### PMC2988475 - ApoE4 Causes Age- and Tau-Dependent Impairment of GABAergic Interneurons
- **Key finding:** ApoE4 causes GABAergic interneuron loss in age/tau-dependent manner
- **Quantitative data:**
  - Picrotoxin subthreshold dose: 1 mg/kg for GABAA blockade
  - Age-dependent progression of interneuron loss
- **Extractable reactions:**
  - ApoE4 + Tau -> GABAergic interneuron dysfunction
  - GABA + GABAA_receptor -> inhibitory signaling
- **Relevance:** Synaptic dysfunction / GABAergic module

#### PMC2891148 - Tau-Focused Immunotherapy for AD and Related Tauopathies
- **Key finding:** Active and passive tau immunotherapy approaches
- **Quantitative data:**
  - Tau aggregation starts at 2-3 months in JNPL3 mice
  - Moribund paralysis by ~12 months
  - Vaccination at 2 months shows therapeutic effect
- **Extractable reactions:**
  - Tau_monomer -> Tau_aggregate (age-dependent)
  - Anti-tau_antibody + Tau_aggregate -> clearance
- **Relevance:** Tau aggregation / immunotherapy module

#### PMC2972675 - Effects of synaptic modulation on beta-amyloid, synaptophysin and memory
- **Key finding:** Synaptic activity modulates Abeta accumulation and synapse loss
- **Quantitative data:** Qualitative relationship between synaptic activity and Abeta
- **Extractable reactions:**
  - Synaptic_activity -> Abeta_production (activity-dependent)
  - Abeta_accumulation -> Synapse_loss
- **Relevance:** Synaptic activity / Abeta feedback module

### Tier 3: Contextual/Supportive Data (useful background, limited kinetics)

| PMC ID | Title (abbreviated) | Relevance |
|--------|---------------------|-----------|
| PMC2913164 | Biomarkers in translational research of AD | CSF Abeta42, t-tau, p-tau as biomarker compartment values |
| PMC2886514 | Thiophene derivatives for imaging protein aggregates | Aggregate binding probes, no kinetic data |
| PMC2964735 | Anti-PrPC antibody for AD cognitive deficits | PrPC-Abeta interaction pathway |
| PMC2966423 | Mouse BBB transcriptome | BBB transport gene expression |
| PMC3000457 | Aptamer-based proteomic technology | Assay methodology |
| PMC2945234 | Chronic traumatic encephalopathy | Tau pathology progression |
| PMC2919638 | CLU, CR1, PICALM associations | Genetic risk factors |
| PMC2919230 | Single-molecule ELISA | Detection methodology |
| PMC2902719 | Retrograde axonal transport | Transport dysfunction mechanisms |
| PMC2900152 | TREM2/DAP12 activation of PI3K | TREM2 signaling pathway |
| PMC2989531 | GWAS loci for AD | Genetic associations |
| PMC2965820 | Endosomal dysfunction in hippocampal CA1 | Early endosome pathway |
| PMC2962809 | Prion protein and Abeta synaptic toxicity | PrPC as Abeta receptor |
| PMC2951281 | TDP-43 proteinopathy in CTE | TDP-43 pathology |
| PMC2944799 | Selective disruption of cerebral neocortex | Regional vulnerability |
| PMC2873177 | PCDH11X and late-onset AD | Genetic association |
| PMC2902689 | Brain tissue loss, CSF biomarkers, ApoE | Biomarker trajectories |
| PMC2902004 | Progranulin mutation AD-like phenotype | PGRN pathway |

### Papers with No Extractable Mechanistic Data (clinical, imaging, epidemiological, genetic)

PMC2867843, PMC2868595, PMC2869317, PMC2872874, PMC2886669, PMC2886712, PMC2886795, PMC2886799, PMC2891865, PMC2892479, PMC2893399, PMC2894993, PMC2897173, PMC2898526, PMC2900429, PMC2901533, PMC2902683, PMC2902875, PMC2903199, PMC2909476, PMC2910889, PMC2912147, PMC2917798, PMC2920531, PMC2922887, PMC2927112, PMC2927852, PMC2928998, PMC2929320, PMC2929880, PMC2930111, PMC2935401, PMC2938201, PMC2938772, PMC2941039, PMC2947486, PMC2951115, PMC2951116, PMC2952586, PMC2956420, PMC2956757, PMC2963067, PMC2964442, PMC2965392, PMC2965417, PMC2965425, PMC2978421, PMC2981572, PMC2990962, PMC2992822, PMC2997634, PMC3000441

---

## 2. Key Pathways Identified

### A. APP Processing / Secretase Cascade
**Papers:** PMC2947312, PMC2879048, PMC2879045, PMC2902368
- **Non-amyloidogenic:** APP -> sAPPalpha + C83 (alpha-secretase) -> p3 + AICD (gamma-secretase)
- **Amyloidogenic:** APP -> sAPPbeta + C99 (BACE1) -> Abeta38/40/42 + AICD (gamma-secretase)
- BACE1 cleaves APPswe 10-100x more efficiently than WT
- Gamma-secretase modulators shift Abeta42->Abeta38 ratio without affecting Notch

### B. Abeta Aggregation Cascade
**Papers:** PMC2987723, PMC2972675
- Abeta monomer -> SDS-stable dimer -> protofibril -> fibril
- Rate constant for dimer->protofibril: k = 0.085 h^-1
- Concentration-dependent nucleation threshold (~1.25 uM for dimers)
- Protofibrils are synaptotoxic; fibrils deposit as plaques

### C. Calcium Homeostasis / ER Signaling
**Papers:** PMC2906098, PMC2898196, PMC2944253, PMC2884172
- ER Ca2+ store -> cytosolic Ca2+ via InsP3R (enhanced by PS1 FAD mutations)
- ER Ca2+ store -> cytosolic Ca2+ via RyR (CICR, aberrant in AD)
- Cytosolic Ca2+ -> ER via SERCA pump
- Extracellular Ca2+ -> cytosolic via SOC (store-operated channels)
- NMDAR -> Ca2+ influx -> aberrant RyR activation in AD
- Astrocytic calcium waves near plaques (resting Ca2+ elevated from 81->149 nM)

### D. Neuroinflammation / Microglial Activation
**Papers:** PMC2997622, PMC2873093
- fAbeta + TLR4/CD14 -> NF-kB -> proinflammatory cytokines (TNF-alpha, IL-1beta, IL-6)
- M1 activation (classical, proinflammatory): IFN-gamma pathway
- M2 activation (alternative, anti-inflammatory): IL-4/IL-13 pathway
- Negative feedback: SOCS, ATF3, Nurr1
- Scavenger receptor-mediated Abeta phagocytosis

### E. ApoE / Lipid Metabolism
**Papers:** PMC2908393, PMC2988475
- ApoE-mediated Abeta clearance via LRP1/LDLR
- ApoE4 impairs clearance relative to ApoE2/E3
- ApoE4 + tau -> GABAergic interneuron loss (age-dependent)
- AD risk: ~8.3x increased incidence with ApoE4

### F. Tau Pathology
**Papers:** PMC2891148, PMC2988475, PMC2945234
- Tau monomer -> phospho-tau -> tau aggregates -> NFTs
- Age-dependent aggregation kinetics
- Tau immunotherapy clearance pathway

---

## 3. Extractable Reactions and Rate Laws

### APP Processing Module

```antimony
// BACE1 cleavage (amyloidogenic pathway)
// Rate type: custom_conc_per_time (Michaelis-Menten)
J_BACE1: APP_Neuron => sAPPbeta_BrainISF + C99_Neuron; Vmax_BACE1 * APP_Neuron / (Km_BACE1 + APP_Neuron)

// Alpha-secretase cleavage (non-amyloidogenic, competing)
J_alpha: APP_Neuron => sAPPalpha_BrainISF + C83_Neuron; Vmax_alpha * APP_Neuron / (Km_alpha + APP_Neuron)

// Gamma-secretase cleavage of C99
J_gamma42: C99_Neuron => Abeta42_BrainISF + AICD_Neuron; k_gamma42 * C99_Neuron
J_gamma40: C99_Neuron => Abeta40_BrainISF + AICD_Neuron; k_gamma40 * C99_Neuron
J_gamma38: C99_Neuron => Abeta38_BrainISF + AICD_Neuron; k_gamma38 * C99_Neuron

// GSM effect (shifts ratio): k_gamma42 is reduced, k_gamma38 increased
// IC50_GSM_Abeta42 = 29 nM (Compound 4, PMC2947312)
```

### Abeta Aggregation Module

```antimony
// Monomer to dimer (reversible mass action)
J_dimerize: 2 Abeta42_BrainISF => Abeta42dimer_BrainISF; k_dimer_on * Abeta42_BrainISF^2 - k_dimer_off * Abeta42dimer_BrainISF

// Dimer to protofibril (nucleation-dependent, single exponential)
// k = 0.085 h^-1 = 2.36e-5 s^-1 (PMC2987723)
// Concentration threshold ~1.25 uM for dimers
J_protofibril: Abeta42dimer_BrainISF => Abeta42protofibril_BrainISF; k_protofibril * Abeta42dimer_BrainISF

// Protofibril to fibril/plaque (slow conversion)
J_fibril: Abeta42protofibril_BrainISF => Abeta42fibril_BrainParenchyma; k_fibril * Abeta42protofibril_BrainISF

// Parameter values:
// k_protofibril = 0.085 h^-1 (PMC2987723, measured)
// Protofibril growth: 59 nm/day initially, slowing over time
```

### Calcium Homeostasis Module

```antimony
// InsP3R-mediated ER calcium release
// Enhanced by PS1 FAD mutations (gain-of-function, PMC2898196)
J_InsP3R: Ca_ER => Ca_Cytosol; k_InsP3R * InsP3_Cytosol * Ca_ER / (K_InsP3 + InsP3_Cytosol)

// RyR-mediated ER calcium release (CICR)
J_RyR: Ca_ER => Ca_Cytosol; k_RyR * Ca_Cytosol^n_Hill / (K_RyR^n_Hill + Ca_Cytosol^n_Hill) * Ca_ER

// SERCA pump (ER refilling)
J_SERCA: Ca_Cytosol => Ca_ER; Vmax_SERCA * Ca_Cytosol^2 / (Km_SERCA^2 + Ca_Cytosol^2)

// Store-operated calcium entry
J_SOC: Ca_Extracellular => Ca_Cytosol; k_SOC * (K_SOC / (K_SOC + Ca_ER))

// NMDAR-mediated calcium influx (PMC2944253)
J_NMDAR: Ca_Extracellular => Ca_Cytosol; k_NMDAR * Glutamate_Synapse * V_membrane_factor

// Astrocyte calcium elevation near plaques (PMC2884172)
// Resting [Ca2+]: 81 nM (control) -> 149 nM (near plaques)
J_astro_Ca: Ca_ER_Astrocyte => Ca_Cytosol_Astrocyte; k_astro_plaque * Abeta42fibril_BrainParenchyma
```

### Neuroinflammation Module

```antimony
// TLR4/CD14 activation by fibrillar Abeta (PMC2997622)
J_TLR4: fAbeta_BrainISF + TLR4_Microglia => TLR4_active_Microglia; k_TLR4 * fAbeta_BrainISF * TLR4_Microglia

// NF-kB activation
J_NFkB: TLR4_active_Microglia => NFkB_active_Microglia; k_NFkB * TLR4_active_Microglia

// Proinflammatory cytokine production (M1)
J_TNFa: NFkB_active_Microglia => TNFalpha_BrainISF; k_TNFa * NFkB_active_Microglia
J_IL1b: NFkB_active_Microglia => IL1beta_BrainISF; k_IL1b * NFkB_active_Microglia
J_IL6: NFkB_active_Microglia => IL6_BrainISF; k_IL6 * NFkB_active_Microglia

// M1/M2 polarization (PMC2873093)
J_M1: Microglia_M0 => Microglia_M1; k_M1 * IFNgamma_BrainISF * Microglia_M0
J_M2: Microglia_M0 => Microglia_M2; k_M2 * IL4_BrainISF * Microglia_M0

// Negative feedback (SOCS pathway)
J_SOCS: NFkB_active_Microglia => SOCS_Microglia; k_SOCS * NFkB_active_Microglia
// SOCS inhibits further NF-kB signaling

// Scavenger receptor Abeta phagocytosis
J_phago: Abeta42_BrainISF => Abeta42_Microglia; k_phago * Abeta42_BrainISF * Microglia_M2
```

### ApoE / Abeta Clearance Module

```antimony
// ApoE-mediated Abeta clearance (PMC2908393)
J_ApoE_bind: ApoE_BrainISF + Abeta42_BrainISF => ApoE_Abeta42_BrainISF; k_ApoE_bind * ApoE_BrainISF * Abeta42_BrainISF

// LRP1 receptor-mediated endocytosis
J_LRP1: ApoE_Abeta42_BrainISF => ApoE_Abeta42_degraded; k_LRP1 * ApoE_Abeta42_BrainISF * LRP1_Neuron

// ApoE4 impairment factor (reduced clearance)
// ApoE4 risk: ~8.3x increased AD incidence
// Model as reduced k_ApoE_bind or k_LRP1 for E4 isoform
```

### Tau Aggregation Module

```antimony
// Tau phosphorylation
J_tau_phos: Tau_Neuron => pTau_Neuron; k_tau_phos * Tau_Neuron * Kinase_active

// pTau aggregation (age-dependent, PMC2891148)
// Aggregation starts ~2-3 months in JNPL3 mice
J_tau_agg: pTau_Neuron => TauAgg_Neuron; k_tau_agg * pTau_Neuron^2

// NFT formation
J_NFT: TauAgg_Neuron => NFT_Neuron; k_NFT * TauAgg_Neuron

// Tau immunotherapy clearance
J_tau_clear: TauAgg_Neuron + AntiTau_Ab => TauAgg_cleared; k_immuno * TauAgg_Neuron * AntiTau_Ab
```

---

## 4. Species and Compartments

### Compartments

| Compartment | Description | Source Papers |
|-------------|-------------|---------------|
| Neuron | Intraneuronal (cytoplasm) | PMC2906098, PMC2944253, PMC2988475 |
| ER_Neuron | Endoplasmic reticulum | PMC2906098, PMC2898196 |
| Synapse | Synaptic cleft | PMC2944253, PMC2972675 |
| BrainISF | Brain interstitial fluid | PMC2987723, PMC2908393 |
| BrainParenchyma | Brain parenchyma (plaque deposition) | PMC2947312, PMC2997622 |
| Microglia | Microglial cell | PMC2997622, PMC2873093 |
| Astrocyte | Astrocyte cell | PMC2884172 |
| CSF | Cerebrospinal fluid | PMC2913164, PMC2902689 |
| Plasma | Blood plasma | PMC2947312 |

### Species

| Species | Compartment | Description | Source |
|---------|-------------|-------------|--------|
| APP | Neuron | Amyloid precursor protein | PMC2879048, PMC2879045 |
| C99 | Neuron | Beta-CTF (BACE1 product) | PMC2947312, PMC2879048 |
| C83 | Neuron | Alpha-CTF | PMC2879045 |
| sAPPalpha | BrainISF | Soluble APP-alpha | PMC2879045 |
| sAPPbeta | BrainISF | Soluble APP-beta | PMC2879048 |
| AICD | Neuron | APP intracellular domain | PMC2947312 |
| Abeta38 | BrainISF | Amyloid-beta 38 | PMC2947312 |
| Abeta40 | BrainISF | Amyloid-beta 40 | PMC2947312, PMC2987723 |
| Abeta42 | BrainISF | Amyloid-beta 42 | PMC2947312, PMC2987723 |
| Abeta42dimer | BrainISF | Abeta42 SDS-stable dimer | PMC2987723 |
| Abeta42protofibril | BrainISF | Abeta42 protofibril | PMC2987723 |
| Abeta42fibril | BrainParenchyma | Fibrillar Abeta (plaques) | PMC2987723, PMC2997622 |
| Tau | Neuron | Unphosphorylated tau | PMC2891148, PMC2988475 |
| pTau | Neuron | Phosphorylated tau | PMC2891148 |
| TauAgg | Neuron | Aggregated tau | PMC2891148 |
| NFT | Neuron | Neurofibrillary tangle | PMC2891148 |
| Ca | Cytosol, ER, Extracellular | Calcium ions | PMC2906098, PMC2898196 |
| InsP3 | Cytosol | Inositol trisphosphate | PMC2898196 |
| Glutamate | Synapse | Glutamate neurotransmitter | PMC2944253 |
| ApoE | BrainISF | Apolipoprotein E (E2/E3/E4) | PMC2908393 |
| ApoE_Abeta42 | BrainISF | ApoE-Abeta complex | PMC2908393 |
| LRP1 | Neuron | LDL receptor-related protein 1 | PMC2908393 |
| TLR4 | Microglia | Toll-like receptor 4 | PMC2997622 |
| CD14 | Microglia | TLR co-receptor | PMC2997622 |
| NFkB | Microglia | NF-kappa B transcription factor | PMC2873093 |
| TNFalpha | BrainISF | Tumor necrosis factor alpha | PMC2873093 |
| IL1beta | BrainISF | Interleukin 1-beta | PMC2873093 |
| IL6 | BrainISF | Interleukin 6 | PMC2873093 |
| SOCS | Microglia | Suppressor of cytokine signaling | PMC2873093 |
| Microglia_M0 | Microglia | Resting microglia | PMC2997622 |
| Microglia_M1 | Microglia | Classically activated microglia | PMC2873093 |
| Microglia_M2 | Microglia | Alternatively activated microglia | PMC2873093 |
| GABA | Synapse | Gamma-aminobutyric acid | PMC2988475 |
| BACE1 | Neuron | Beta-secretase 1 enzyme | PMC2879048, PMC2902368 |
| Synaptophysin | Synapse | Synaptic vesicle marker | PMC2972675 |

---

## Summary Statistics

- **Total papers in batch:** 86
- **Papers with quantitative/mechanistic data (Tier 1):** 5
- **Papers with mechanistic pathway data (Tier 2):** 10
- **Papers with contextual data (Tier 3):** 18
- **Papers with no extractable ODE data:** 53

### Most Valuable Parameter Extracted
- **Abeta dimer to protofibril rate constant: k = 0.085 +/- 0.03 h^-1** (PMC2987723)
  - Confidence: measured (in vitro, synthetic cross-linked dimers)
  - Note: Uses AbetaS26C disulfide dimers as proxy for natural SDS-stable dimers

### Priority Modules for Implementation
1. **APP Processing** - Well-characterized BACE1/gamma-secretase cascade with IC50 data
2. **Abeta Aggregation** - Direct rate constant measurement available
3. **Calcium Homeostasis** - Multiple papers with complementary pathway data
4. **Neuroinflammation** - TLR4/NF-kB/M1-M2 pathway well described
5. **ApoE Clearance** - Key risk modifier pathway
6. **Tau Aggregation** - Age-dependent kinetics from animal models
