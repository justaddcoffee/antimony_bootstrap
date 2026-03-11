# Batch 14 Findings: Alzheimer's Disease Paper Analysis for Antimony Modeling

**Date**: 2026-02-24
**Batch**: 14 (86 papers from Primary_Alzforum collection)
**PMC Range**: PMC8934148 – PMC9708566
**Purpose**: Identify quantitative biological mechanisms extractable as ODE equations in Antimony format

---

## 1. Papers with Quantitative/Mechanistic Data

### Tier 1: Strong Quantitative/Kinetic Data (High Priority for Antimony Extraction)

| PMC ID | Title | Key Quantitative Data | Score |
|--------|-------|----------------------|-------|
| PMC9354770 | Discovery and engineering of an anti-TREM2 antibody to promote amyloid plaque clearance by microglia in 5XFAD mice | EC50 values (117.1, 206.7, 405.2 nM); TREM2 binding kinetics; oAbeta-induced phagocytosis dose-response; antibody PK parameters | 29 |
| PMC9254231 | A linked organ-on-chip model of the human NVU reveals metabolic coupling of endothelial and neuronal cells | Michaelis-Menten kinetics (Vmax, Km); metabolic flux rates across BBB; ODE-based transport modeling; glucose/lactate exchange rates | 25 |
| PMC9133466 | Abeta oligomer concentration in mouse and human brain and its drug-induced reduction ex vivo | Dose-dependent Abeta oligomer concentrations; time-dependent reduction curves; size distribution data; quantitative sFIDA measurements | 22 |
| PMC8988215 | PAC1 receptor-mediated clearance of tau in postsynaptic compartments | Tau clearance rates (rate ~0.25); proteasomal degradation kinetics; PAC1-dependent tau turnover in synaptic compartments | 19 |
| PMC9554345 | Reversal of synapse loss by targeting mGluR5 to prevent synaptic tagging by C1Q | Ki = 0.6 nM (BMS-984923); IC50 = 1.14 nM; C1Q-mediated synaptic elimination rates; dose-occupancy PET data | 17 |

### Tier 2: Mechanistic Pathway Data (Moderate Priority)

| PMC ID | Title | Key Mechanistic Insight | Score |
|--------|-------|------------------------|-------|
| PMC9299535 | Targeted BACE-1 inhibition in microglia enhances amyloid clearance | BACE-1 deletion increases microglial phagocytosis; Abeta clearance enhancement; DAM gene signature upregulation | 18 |
| PMC9108550 | Cholesterol determines cytosolic entry and seeded aggregation of tau | Cholesterol-dependent tau membrane crossing; NPC1-mediated regulation; nucleation kinetics of tau seeding | 17 |
| PMC9199162 | Microglial Abeta clearance is driven by PIEZO1 channels | Mechanosensitive Abeta uptake; PIEZO1-dependent phagocytic flux; calcium-mediated signaling in clearance | 17 |
| PMC9581485 | Numb regulates Tau levels and prevents neurodegeneration | Numb-dependent tau proteasomal degradation; steady-state tau level regulation; age-dependent neurodegeneration kinetics | 17 |
| PMC8934148 | Astrocyte-derived IL-3 reprograms microglia and limits AD | IL-3/IL-3Ra signaling axis; microglia reprogramming kinetics; Abeta and tau clearance enhancement | 17 |
| PMC9194753 | Safety and Efficacy of Semorinemab in prodromal-mild AD | Anti-tau antibody PK; CSF tau steady-state measurements; treatment effect on tau biomarkers | 17 |
| PMC9259669 | Periarteriolar spaces modulate CSF transport into brain | CSF flow rates (1.5-2 um/s); perivascular transport modeling; age-dependent clearance changes | 16 |
| PMC9581941 | Assessment of Cholesterol Homeostasis in the Living Human Brain | CYP46A1-mediated cholesterol turnover rates; brain cholesterol metabolism quantification via PET | 15 |
| PMC9156411 | PSEN1 variants determine Abeta profiles and pathogenicity | Abeta42/Abeta40 ratio kinetics; gamma-secretase cleavage efficiency; mutation-dependent production rates | 14 |
| PMC9625082 | TREM2 Drives Microglia Response to Abeta via SYK-dependent and -independent Paths | TREM2-SYK-PI3K-AKT-GSK3beta signaling cascade; DAM transition kinetics; Abeta plaque encasement rates | 15 |
| PMC9205595 | BACE-1 inhibition facilitates homeostatic to DAM-1 transition | Microglial state transition rates; BACE-1-dependent gene regulation kinetics; phagocytic capacity changes | 15 |
| PMC9018606 | DOPEGAL-tau modification by MAO-A norepinephrine metabolite | MAO-A enzymatic rate for NE to DOPEGAL conversion; DOPEGAL-tau K353 binding kinetics; tau aggregation propagation rate | 14 |

### Tier 3: Supporting Mechanistic Context (Lower Priority but Useful)

| PMC ID | Title | Relevant Context |
|--------|-------|-----------------|
| PMC9188195 | Novel App knock-in mouse model metabolic dysregulation | APP processing rates; microglial metabolic changes |
| PMC9394447 | Alpha-synuclein modulates P-bodies and mRNA stability | Protein turnover kinetics; mRNA degradation rates |
| PMC9054012 | Axonal transport modulated by local Ca2+ efflux, disrupted by PSEN1 | Ca2+ flux rates; endosome transport velocities |
| PMC9481908 | Human tau mutations induce cholesterol dyshomeostasis | Cholesterol flux alterations; tau mutation effects |
| PMC9285116 | Absence of microglia promotes diverse pathologies | Microglia-dependent Abeta/tau clearance baseline rates |
| PMC9345574 | R47H-TREM2 induces disease-enhancing microglial states via AKT | AKT hyperactivation kinetics; microglial state transitions |
| PMC9122331 | Protein lifetimes in aged brains reveal proteostatic adaptation | Protein half-life measurements; age-dependent turnover changes |
| PMC9531302 | Tau trapping at dynamic hot spots near plasma membrane | Tau membrane binding kinetics; trapping rate constants |
| PMC9559604 | Chronic TREM2 activation exacerbates tau seeding and spreading | TREM2 agonism effects on tau seeding rate; neuritic dystrophy |
| PMC9577883 | Donanemab treatment exploratory plasma biomarkers | p-tau217 clearance kinetics; GFAP dynamics; NfL changes |
| PMC9258953 | Ablating single master site abolishes tau hyperphosphorylation | Tau phosphorylation cascade kinetics; site-specific rates |

---

## 2. Key Pathways Identified

### A. Amyloid-Beta (Abeta) Processing and Clearance
- **APP Processing**: APP -> (BACE-1/gamma-secretase) -> Abeta40, Abeta42 [PMC9156411, PMC9299535, PMC9205595]
- **Abeta Aggregation**: Abeta_monomer -> Abeta_oligomer -> Abeta_fibril -> Abeta_plaque [PMC9133466, PMC9108550]
- **Microglial Abeta Clearance**: TREM2/PIEZO1/BACE1-dependent phagocytosis [PMC9354770, PMC9199162, PMC9299535, PMC9625082]
- **Perivascular Clearance**: ISF Abeta -> periarteriolar drainage -> CSF [PMC9259669]
- **IL-3-mediated Clearance**: Astrocyte IL-3 -> Microglia reprogramming -> Enhanced Abeta clearance [PMC8934148]

### B. Tau Pathology and Clearance
- **Tau Phosphorylation**: Tau -> p-Tau (GSK3beta, CDK5 dependent) [PMC9258953, PMC9625082]
- **Tau Aggregation/Seeding**: Monomeric tau -> seeded aggregation (cholesterol-dependent entry) [PMC9108550, PMC9549419]
- **Tau Clearance - Postsynaptic**: PAC1 receptor -> proteasomal tau degradation [PMC8988215]
- **Tau Clearance - Numb-dependent**: Numb -> tau trafficking to proteasome [PMC9581485]
- **DOPEGAL-Tau Modification**: NE -> (MAO-A) -> DOPEGAL + Tau-K353 -> aggregation [PMC9018606]
- **Tau Propagation**: Trans-synaptic tau transfer; prion-like spreading [PMC9559604, PMC9018606]

### C. Microglial State Transitions
- **Homeostatic -> DAM-1 -> DAM-2**: TREM2/SYK-dependent transition [PMC9625082, PMC9205595, PMC9345574]
- **BACE-1 Regulation**: BACE-1 inhibition accelerates homeostatic -> DAM-1 [PMC9205595]
- **IL-3 Reprogramming**: IL-3Ra activation -> transcriptional/morphological/functional changes [PMC8934148]
- **AKT Hyperactivation**: R47H-TREM2 -> enhanced AKT -> disease-enhancing states [PMC9345574]

### D. Cholesterol Homeostasis
- **Brain Cholesterol Synthesis**: De novo synthesis in astrocytes/oligodendrocytes [PMC9581941]
- **Cholesterol Elimination**: Neuronal cholesterol -> (CYP46A1) -> 24S-hydroxycholesterol -> efflux [PMC9581941]
- **Cholesterol-Tau Interaction**: Membrane cholesterol modulates tau cytosolic entry [PMC9108550, PMC9481908]

### E. Neurovascular Unit / BBB Transport
- **Metabolic Coupling**: Endothelial glucose uptake -> lactate shuttle -> neuronal metabolism [PMC9254231]
- **CSF/ISF Dynamics**: CSF periarteriolar influx; waste metabolite drainage [PMC9259669]
- **BBB Drug Transport**: P-gp efflux; receptor-mediated transcytosis [PMC9254231, PMC9354770]

### F. Synaptic Loss / Complement Pathway
- **Complement Tagging**: mGluR5 activation -> C1Q synaptic tagging -> microglial pruning [PMC9554345]
- **Synapse Elimination**: C1Q/C3-tagged synapses -> microglial phagocytosis [PMC9554345]

### G. Calcium Dysregulation
- **Endosomal Ca2+ Flux**: Local Ca2+ efflux modulates organelle transport [PMC9054012]
- **PSEN1-dependent Dysfunction**: PSEN1 mutations disrupt lysosomal Ca2+ [PMC9054012]

---

## 3. Extractable Reactions and Rate Laws

### Reaction Set A: Abeta Production and Processing
```
# APP cleavage by BACE-1 and gamma-secretase
# Rate type: Michaelis-Menten (MA or custom)
APP_BrainISF -> sAPPbeta_BrainISF + CTFbeta_BrainISF; BACE1_BrainISF * Vmax_BACE1 * APP_BrainISF / (Km_BACE1 + APP_BrainISF)
CTFbeta_BrainISF -> Abeta40_BrainISF; k_gamma40 * CTFbeta_BrainISF
CTFbeta_BrainISF -> Abeta42_BrainISF; k_gamma42 * CTFbeta_BrainISF

# PSEN1 mutation effects on Abeta42/40 ratio [PMC9156411]
# Different PSEN1 variants shift k_gamma42/k_gamma40 ratio
# Abeta42/40 ratio correlates with age at onset
```

### Reaction Set B: Abeta Aggregation Cascade
```
# Monomer -> Oligomer -> Fibril -> Plaque [PMC9133466, PMC9108550]
# Rate type: MA or custom nucleation-dependent
2 Abeta42_BrainISF -> Abeta42_oligo_BrainISF; k_nucleation * Abeta42_BrainISF^2
Abeta42_oligo_BrainISF + Abeta42_BrainISF -> Abeta42_oligo_BrainISF; k_elongation * Abeta42_oligo_BrainISF * Abeta42_BrainISF
Abeta42_oligo_BrainISF -> Abeta42_fibril_BrainISF; k_fibril * Abeta42_oligo_BrainISF
Abeta42_fibril_BrainISF -> Abeta42_plaque_BrainParenchyma; k_deposit * Abeta42_fibril_BrainISF
```

### Reaction Set C: Microglial Abeta Clearance
```
# TREM2-dependent phagocytic clearance [PMC9354770, PMC9625082]
# Rate type: Michaelis-Menten or Hill function
Abeta42_plaque_BrainParenchyma -> ; Vmax_phago * TREM2_active_Microglia * Abeta42_plaque_BrainParenchyma / (Km_phago + Abeta42_plaque_BrainParenchyma)

# PIEZO1-dependent mechanosensitive clearance [PMC9199162]
Abeta42_plaque_BrainParenchyma -> ; k_PIEZO1 * PIEZO1_Microglia * Abeta42_plaque_BrainParenchyma

# IL-3-enhanced microglial clearance [PMC8934148]
# IL-3 from astrocytes upregulates microglial phagocytic capacity
-> IL3_BrainISF; k_prod_IL3 * Astrocyte_BrainParenchyma
IL3_BrainISF -> ; k_deg_IL3 * IL3_BrainISF
# IL-3 enhances TREM2-dependent clearance (modifier on phagocytosis rate)
```

### Reaction Set D: Tau Phosphorylation and Aggregation
```
# Tau phosphorylation [PMC9258953, PMC9625082]
# Rate type: MA with enzyme modification
Tau_Neuron -> pTau_Neuron; (k_GSK3b * GSK3b_active_Neuron + k_CDK5 * CDK5_active_Neuron) * Tau_Neuron
pTau_Neuron -> Tau_Neuron; k_PP2A * PP2A_Neuron * pTau_Neuron

# DOPEGAL-mediated tau modification [PMC9018606]
NE_LC -> DOPEGAL_LC; k_MAOA * NE_LC
DOPEGAL_LC + Tau_LC -> DOPEGAL_Tau_LC; k_DOPEGAL_bind * DOPEGAL_LC * Tau_LC
DOPEGAL_Tau_LC -> AggTau_LC; k_DOPEGAL_agg * DOPEGAL_Tau_LC

# Cholesterol-dependent tau seeding [PMC9108550]
# Extracellular tau seed entry rate modulated by membrane cholesterol
TauSeed_BrainISF -> TauSeed_Neuron; k_entry * TauSeed_BrainISF * Cholesterol_membrane_Neuron
TauSeed_Neuron + Tau_Neuron -> AggTau_Neuron; k_seed * TauSeed_Neuron * Tau_Neuron
```

### Reaction Set E: Tau Clearance
```
# PAC1 receptor-mediated postsynaptic tau clearance [PMC8988215]
# Rate type: MA
pTau_Postsynaptic -> ; k_PAC1_clear * PAC1_Postsynaptic * pTau_Postsynaptic

# Numb-dependent proteasomal degradation [PMC9581485]
Tau_Neuron -> ; k_Numb_deg * Numb_Neuron * Tau_Neuron / (Km_Numb + Tau_Neuron)

# Tau propagation (trans-synaptic) [PMC9018606, PMC9559604]
AggTau_Neuron_Region1 -> AggTau_BrainISF; k_release * AggTau_Neuron_Region1
AggTau_BrainISF -> AggTau_Neuron_Region2; k_uptake * AggTau_BrainISF
```

### Reaction Set F: Microglial State Transitions
```
# Homeostatic -> DAM-1 -> DAM-2 transitions [PMC9625082, PMC9205595]
# Rate type: MA or Hill function
Microglia_Homeostatic -> Microglia_DAM1; k_DAM1_trans * TREM2_signal * Microglia_Homeostatic
Microglia_DAM1 -> Microglia_DAM2; k_DAM2_trans * SYK_active * Microglia_DAM1

# BACE-1 effect on transition [PMC9205595]
# BACE-1 inhibition increases k_DAM1_trans
# k_DAM1_trans = k_DAM1_base / (1 + BACE1_Microglia / Ki_BACE1_DAM)

# AKT hyperactivation in R47H-TREM2 [PMC9345574]
TREM2_R47H -> AKT_hyperactive; k_AKT_R47H * TREM2_R47H
```

### Reaction Set G: Cholesterol Homeostasis
```
# Brain cholesterol turnover [PMC9581941]
# Rate type: MA or Michaelis-Menten
-> Cholesterol_Neuron; k_synth_chol * HMGCoA_reductase_Astrocyte  # astrocyte synthesis + transfer
Cholesterol_Neuron -> OHC24S_Neuron; Vmax_CYP46A1 * Cholesterol_Neuron / (Km_CYP46A1 + Cholesterol_Neuron)
OHC24S_Neuron -> OHC24S_BrainISF; k_efflux_24OHC * OHC24S_Neuron  # crosses BBB
OHC24S_BrainISF -> OHC24S_Plasma; k_BBB_24OHC * OHC24S_BrainISF
```

### Reaction Set H: Complement-Mediated Synapse Elimination
```
# mGluR5/C1Q synapse tagging [PMC9554345]
# Rate type: MA
Synapse_healthy -> Synapse_C1Q_tagged; k_C1Q_tag * C1Q_BrainISF * Abeta_oligo_BrainISF * mGluR5_active
Synapse_C1Q_tagged -> ; k_prune * Microglia_DAM2 * Synapse_C1Q_tagged  # microglial phagocytosis
# mGluR5 SAM inhibits tagging: k_C1Q_tag reduced by factor (1 - SAM_occupancy)
```

### Reaction Set I: Neurovascular Unit Transport
```
# BBB glucose transport [PMC9254231]
# Rate type: Michaelis-Menten
Glucose_Plasma -> Glucose_BrainISF; Vmax_GLUT1 * Glucose_Plasma / (Km_GLUT1 + Glucose_Plasma)

# Astrocyte-neuron lactate shuttle [PMC9254231]
Glucose_BrainISF -> Lactate_Astrocyte; k_glycolysis * Glucose_BrainISF
Lactate_Astrocyte -> Lactate_BrainISF; k_MCT1 * Lactate_Astrocyte
Lactate_BrainISF -> Lactate_Neuron; k_MCT2 * Lactate_BrainISF

# CSF periarteriolar transport [PMC9259669]
# Rate type: UDF (flow rate ~1.5-2 um/s)
Solute_CSF -> Solute_BrainISF; k_PVS_influx * Solute_CSF
Solute_BrainISF -> Solute_CSF; k_PVS_efflux * Solute_BrainISF
```

---

## 4. Species and Compartments

### Compartments
| Compartment | Description | Source Papers |
|-------------|-------------|---------------|
| BrainISF | Brain interstitial fluid | PMC9259669, PMC9254231, PMC9133466 |
| BrainParenchyma | Brain parenchymal tissue | PMC9354770, PMC9199162 |
| Neuron | Neuronal cytoplasm | PMC9581485, PMC9108550, PMC9258953 |
| Postsynaptic | Postsynaptic density/compartment | PMC8988215 |
| Presynaptic | Presynaptic terminal | PMC8988215 |
| Microglia | Microglial cytoplasm | PMC9625082, PMC9205595, PMC9345574 |
| Astrocyte | Astrocyte cytoplasm | PMC8934148, PMC9254231 |
| LC (Locus Coeruleus) | Noradrenergic nucleus | PMC9018606 |
| CSF | Cerebrospinal fluid | PMC9259669, PMC9499867 |
| Plasma | Blood plasma | PMC8938295, PMC9577883 |
| BBB_Endothelium | Blood-brain barrier endothelial cells | PMC9254231 |
| Lysosome | Lysosomal lumen | PMC9174056, PMC9067636 |
| Endosome | Endosomal compartment | PMC9054012 |
| Membrane | Neuronal plasma membrane | PMC9531302, PMC9108550 |

### Species
| Species | Compartment(s) | Description | Source |
|---------|----------------|-------------|--------|
| APP | Neuron, BrainISF | Amyloid precursor protein | PMC9156411, PMC9188195 |
| BACE1 | Neuron, Microglia | Beta-secretase 1 | PMC9299535, PMC9205595 |
| Abeta40 | BrainISF, CSF, Plasma | Amyloid-beta 1-40 | PMC9156411, PMC9133466 |
| Abeta42 | BrainISF, CSF, Plasma | Amyloid-beta 1-42 | PMC9156411, PMC9133466 |
| Abeta42_oligo | BrainISF | Abeta42 oligomers | PMC9133466, PMC8938295 |
| Abeta42_fibril | BrainISF | Abeta42 fibrils | PMC9133466 |
| Abeta42_plaque | BrainParenchyma | Abeta plaques | PMC9354770, PMC9199162 |
| Tau | Neuron, Postsynaptic | Microtubule-associated protein tau | PMC9581485, PMC8988215 |
| pTau | Neuron, Postsynaptic, CSF, Plasma | Phosphorylated tau | PMC9258953, PMC9499867 |
| pTau217 | CSF, Plasma | Phospho-tau 217 | PMC9499867, PMC9577883 |
| pTau231 | CSF, Plasma | Phospho-tau 231 | PMC9499867 |
| AggTau | Neuron, BrainISF | Aggregated tau seeds | PMC9108550, PMC9559604 |
| TREM2 | Microglia | Triggering receptor expressed on myeloid cells 2 | PMC9354770, PMC9625082 |
| TREM2_R47H | Microglia | AD-risk TREM2 variant | PMC9345574 |
| SYK | Microglia | Spleen tyrosine kinase | PMC9625082, PMC9617784 |
| DAP12 | Microglia | DNAX-activating protein of 12 kDa | PMC9625082 |
| IL3 | BrainISF | Interleukin-3 | PMC8934148 |
| IL3Ra | Microglia | IL-3 receptor alpha | PMC8934148 |
| PIEZO1 | Microglia | Mechanosensitive ion channel | PMC9199162 |
| PAC1 | Postsynaptic | Pituitary adenylate cyclase-activating polypeptide receptor | PMC8988215 |
| Numb | Neuron | Trafficking adaptor protein | PMC9581485 |
| GSK3b | Neuron | Glycogen synthase kinase 3 beta | PMC9625082, PMC9258953 |
| AKT | Microglia, Neuron | Protein kinase B | PMC9345574 |
| PP2A | Neuron | Protein phosphatase 2A | PMC9258953 |
| NE | LC | Norepinephrine | PMC9018606 |
| DOPEGAL | LC | 3,4-dihydroxyphenylglycolaldehyde | PMC9018606 |
| MAO_A | LC | Monoamine oxidase A | PMC9018606 |
| mGluR5 | Postsynaptic | Metabotropic glutamate receptor 5 | PMC9554345 |
| C1Q | BrainISF | Complement component 1q | PMC9554345 |
| Cholesterol | Neuron, Membrane | Neuronal cholesterol | PMC9108550, PMC9581941 |
| CYP46A1 | Neuron | Cholesterol 24-hydroxylase | PMC9581941 |
| OHC24S | Neuron, BrainISF, Plasma | 24S-hydroxycholesterol | PMC9581941 |
| Glucose | Plasma, BrainISF, Astrocyte, Neuron | Glucose | PMC9254231 |
| Lactate | Astrocyte, BrainISF, Neuron | Lactate | PMC9254231 |
| NfL | CSF, Plasma | Neurofilament light chain | PMC9577883 |
| GFAP | CSF, Plasma | Glial fibrillary acidic protein | PMC9577883 |
| Microglia_Homeostatic | BrainParenchyma | Homeostatic microglia | PMC9625082, PMC9205595 |
| Microglia_DAM1 | BrainParenchyma | Stage 1 disease-associated microglia | PMC9205595 |
| Microglia_DAM2 | BrainParenchyma | Stage 2 disease-associated microglia | PMC9625082 |
| Synapse_healthy | Neuron | Functional synapse | PMC9554345 |
| Synapse_C1Q_tagged | Neuron | C1Q-tagged synapse (pruning target) | PMC9554345 |
| PSEN1 | Neuron | Presenilin 1 (gamma-secretase catalytic subunit) | PMC9156411 |
| NPC1 | Neuron | Niemann-Pick C1 cholesterol transporter | PMC9108550 |
| aSynuclein | Neuron | Alpha-synuclein | PMC9394447, PMC9481630 |

---

## 5. Summary Statistics

- **Total papers analyzed**: 86
- **Papers with quantitative/mechanistic data (Tier 1)**: 5
- **Papers with mechanistic pathway data (Tier 2)**: 12
- **Papers with supporting context (Tier 3)**: 11
- **Papers primarily clinical/epidemiological/methodological**: 58
- **Unique pathways identified**: 9 major pathway categories
- **Extractable reaction sets**: 9 (approximately 35+ individual reactions)
- **Unique species identified**: 40+
- **Unique compartments identified**: 14

## 6. Priority Recommendations for Module Building

1. **Microglial Abeta Clearance Module** (TREM2/PIEZO1/IL-3 pathway) — richest quantitative data from PMC9354770, PMC9199162, PMC8934148, PMC9625082
2. **Tau Phosphorylation and Clearance Module** (PAC1/Numb/proteasome) — mechanistic detail from PMC8988215, PMC9581485, PMC9258953
3. **DOPEGAL-Tau Module** (LC-specific vulnerability) — novel mechanism from PMC9018606
4. **Cholesterol-Tau Interaction Module** — membrane cholesterol regulation of tau seeding from PMC9108550, PMC9581941
5. **Microglial State Transition Module** (Homeostatic/DAM-1/DAM-2) — from PMC9625082, PMC9205595, PMC9345574
6. **Complement-Mediated Synapse Loss Module** — C1Q/mGluR5 from PMC9554345
7. **NVU Metabolic Transport Module** — BBB transport kinetics from PMC9254231, PMC9259669
8. **Abeta Aggregation Cascade Module** — oligomer kinetics from PMC9133466
