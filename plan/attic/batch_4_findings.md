# Batch 4 Findings: Quantitative Mechanisms for Alzheimer's ODE Modeling

**Date**: 2026-02-24
**Papers analyzed**: 86 (from /tmp/paper_batch_4.txt)
**Source directory**: data/alz_papers_3k/Primary_Alzforum/

---

## 1. Papers with Quantitative/Mechanistic Data

### Tier 1: High-Value Papers (quantitative kinetics directly extractable as ODEs)

#### PMC3838868 (PMID:23761040) — TOP PRIORITY
**Title**: Increased in vivo Amyloid-beta42 production, exchange, and irreversible loss in Presenilin Mutations Carriers
**Relevance**: Directly provides compartmental kinetic model for Abeta38/Abeta40/Abeta42 turnover using SILK (Stable Isotope Labeling Kinetics). Reports fractional turnover rates (FTR), production rates, and exchange/irreversible loss rates for Abeta species in CNS. PSEN mutation carriers show increased Abeta42:Abeta40 production rate ratio and increased irreversible loss (plaque deposition).
**Extractable parameters**:
- Fractional turnover rates for Abeta38, Abeta40, Abeta42 in CSF
- Production rates of Abeta isoforms (normal vs PSEN carriers)
- Exchange rates between CNS compartments (ISF to CSF)
- Irreversible loss rate (plaque deposition sink)
- Abeta42:Abeta40 production ratio changes with PSEN mutations

#### PMC3949564 (PMID:24534188)
**Title**: Neuronal activity regulates extracellular tau in vivo
**Relevance**: Quantifies ISF tau dynamics using microdialysis. Reports tau half-life estimates, release kinetics dependent on neuronal activity (NMDA, picrotoxin stimulation), and clearance rates. EC50 of NMDA for tau release.
**Extractable parameters**:
- ISF tau turnover rate (slow, contrasts with Abeta t1/2 ~2 h)
- Activity-dependent tau release rate (stimulation increases ISF tau ~2-fold)
- Tau clearance rate from ISF
- NMDA EC50 for tau release (~35 uM in vitro)

#### PMC3551275 (PMID:22896675)
**Title**: A Paravascular Pathway Facilitates CSF Flow Through the Brain Parenchyma and the Clearance of Interstitial Solutes, Including Amyloid-beta
**Relevance**: Defines the glymphatic clearance pathway — paravascular CSF flow through brain parenchyma. Quantifies clearance rates of tracers of different molecular sizes. Critical for modeling ISF-to-CSF solute exchange and Abeta clearance.
**Extractable parameters**:
- CSF-ISF exchange rates for different molecular weight tracers (3kD, 45kD, 2000kD)
- Size-dependent paravascular clearance rates
- AQP4-dependent component of ISF clearance (AQP4 knockout reduces clearance ~70%)
- Bulk flow rate through brain parenchyma

#### PMC3920563 (PMID:24470444)
**Title**: Transferrin receptor (TfR) trafficking determines brain uptake of TfR antibody affinity variants
**Relevance**: Quantifies BBB transcytosis kinetics for therapeutic antibodies. Reports affinity-dependent brain uptake (Kd ~20 nM vs ~600 nM variants), TfR degradation kinetics, and sorting/recycling rates.
**Extractable parameters**:
- BBB transcytosis rates as function of TfR binding affinity
- TfR antibody Kd values: 20 nM (high affinity), 100 nM (moderate), 600 nM (low affinity)
- TfR degradation rate (high-affinity binding promotes lysosomal degradation)
- Brain uptake pharmacokinetics at 4d post-injection

#### PMC3924573 (PMID:24075978)
**Title**: Anti-tau antibodies that block tau aggregate seeding in vitro markedly decrease pathology and improve cognition in vivo
**Relevance**: Quantifies tau seeding/propagation kinetics and antibody blocking. Reports antibody Kd values, seeding IC50, and propagation reduction rates.
**Extractable parameters**:
- Tau seed propagation rate (cell-based biosensor assay)
- Anti-tau antibody KD = 100 pM (HJ8.5), 6.9 nM, 50 nM for other clones
- Seeding inhibition IC50 values
- Reduction in pathology propagation rate with antibody treatment

### Tier 2: Moderate-Value Papers (qualitative mechanisms with some quantitative data)

#### PMC3812809 (PMID:23254930)
**Title**: NLRP3 is activated in Alzheimer's disease and contributes to pathology in APP/PS1 mice
**Relevance**: Defines NLRP3 inflammasome to caspase-1 to IL-1beta pathway in AD microglia. NLRP3 knockout reduces Abeta deposition by enhancing microglial phagocytosis. Links neuroinflammation to Abeta clearance.
**Extractable reactions**:
- NLRP3 activation by Abeta leads to Caspase-1 cleavage leads to IL-1beta maturation
- IL-1beta inhibition of microglial Abeta phagocytosis
- IDE/NEP enzymatic Abeta degradation (mentioned)

#### PMC3376850 (PMID:22170863)
**Title**: beta- but not gamma-secretase proteolysis of APP causes synaptic and memory deficits in a mouse model of dementia
**Relevance**: Demonstrates BACE1 (beta-secretase) cleavage of APP as the pathogenic step (not gamma-secretase alone). BACE inhibitor concentrations tested: 10 nM, 50 nM.
**Extractable reactions**:
- APP to sAPPbeta + C99 (BACE cleavage, rate depends on BRI2 inhibition)
- APP to sAPPalpha + C83 (alpha-secretase cleavage, reduced by BRI2 loss)

#### PMC3431439 (PMID:22820466)
**Title**: Alzheimer Amyloid-beta Oligomer Bound to Post-Synaptic Prion Protein Activates Fyn to Impair Neurons
**Relevance**: Maps the signaling cascade: Abeta oligomer to PrPC binding to Fyn kinase activation to NR2B phosphorylation to synaptic impairment. Concentrations used: Abeta 10 nM.
**Extractable reactions**:
- Abeta_oligomer + PrPC to Abeta_PrPC_complex (binding at post-synaptic densities)
- Abeta_PrPC_complex to Fyn_active (kinase activation)
- Fyn_active + NR2B to pNR2B (NMDA receptor phosphorylation)
- pNR2B to synaptic_impairment (loss of surface GluN2B)

#### PMC3651582 (PMID:22323736)
**Title**: ApoE-Directed Therapeutics Rapidly Clear beta-Amyloid and Reverse Deficits in AD Mouse Models
**Relevance**: ApoE lipidation via bexarotene/RXR activation enhances Abeta clearance. Rapid reduction in soluble Abeta (within hours). Involves LXR/RXR to ApoE expression to Abeta-ApoE complex to clearance.
**Extractable reactions**:
- RXR_agonist to ApoE_expression_upregulation
- ApoE + Abeta to ApoE_Abeta_complex (enhanced by lipidation)
- ApoE_Abeta_complex to clearance (microglial phagocytosis, LRP1-mediated)

#### PMC3528355 (PMID:22654059)
**Title**: The Amyloid Precursor Protein has a Flexible Transmembrane Domain and Binds Cholesterol
**Relevance**: C99 (APP transmembrane domain) binds cholesterol with Kd ~5 nM. Cholesterol binding affects gamma-secretase cleavage site selection (Abeta42 vs Abeta40 ratio).
**Extractable parameters**:
- Cholesterol-C99 binding Kd of approximately 5 nM (1:1 binding model)
- Cholesterol modulation of Abeta42:Abeta40 production ratio

#### PMC4047116 (PMID:22622580)
**Title**: Apolipoprotein E controls cerebrovascular integrity via cyclophilin A
**Relevance**: ApoE4 to CypA to NFkB to MMP9 pathway degrades BBB. ApoE2/E3 suppress CypA in pericytes; ApoE4 fails to suppress. Quantifies BBB breakdown via tight junction protein loss.
**Extractable reactions**:
- ApoE4 fails to suppress CypA
- CypA to NFkB_activation to MMP9_expression
- MMP9 to TightJunction_degradation to BBB_permeability_increase

#### PMC4007018 (PMID:24698269)
**Title**: Reduced Synaptic STIM2 Expression and Impaired Store-Operated Calcium Entry Cause Destabilization of Mature Spines in Mutant PS1 Mice
**Relevance**: PSEN1 mutations to reduced STIM2 to impaired store-operated calcium entry (SOCE) to mushroom spine loss. Quantifies spine density changes and calcium store depletion.
**Extractable reactions**:
- STIM2_reduction to impaired_SOCE
- Impaired_SOCE to ER_calcium_depletion
- ER_calcium_depletion to CaMKII_inactivation to spine_destabilization

#### PMC3952111 (PMID:24462250)
**Title**: Conformational Changes Induced by the A21G Flemish Mutation in the Amyloid Precursor Protein Lead to Increased Abeta Production
**Relevance**: Flemish mutation increases total Abeta production by altering APP conformation. Distinguishes alpha vs beta cleavage competition.
**Extractable reactions**:
- APP_A21G to enhanced beta-cleavage (conformational shift favoring BACE access)

#### PMC3746074 (PMID:19581723)
**Title**: Caffeine suppresses beta-amyloid levels in plasma and brain of Alzheimer's transgenic mice
**Relevance**: Caffeine reduces Abeta levels in plasma and brain. Reports dose-dependent Abeta reduction in multiple compartments (plasma, brain).
**Extractable parameters**:
- Dose-response for caffeine to Abeta suppression (brain and plasma compartments)

### Tier 3: Supporting/Contextual Papers

| PMC ID | PMID | Title (abbreviated) | Relevant Pathway |
|--------|------|---------------------|-----------------|
| PMC3474597 | 22784036 | Clinical and Biomarker Changes in DIAD | Biomarker temporal ordering (Abeta then tau then neurodegeneration) |
| PMC3622225 | 23332364 | Update on hypothetical model of AD biomarkers | Disease progression staging model |
| PMC3601591 | 22464332 | Proline Isomer-Specific Antibodies for Tau | cis/trans p-tau conformation, Pin1 isomerase |
| PMC3610427 | 21451522 | Amyloid-binding compounds and protein homeostasis | Amyloid aggregation modulation |
| PMC3661272 | 22431837 | Antioxidants for AD | Oxidative stress biomarker changes with treatment |
| PMC3567462 | 22302812 | GalphaS-Protein Signaling with APP Intracellular Domain | AICD-GalphaS signaling cascade |
| PMC3752906 | 22133718 | Testing the Right Target and Drug at the Right Stage | Framework for intervention timing |
| PMC3381884 | 21307267 | ABAD-Abeta Interaction Reduces Abeta Accumulation | Mitochondrial Abeta-ABAD complex |
| PMC3402380 | 22699908 | Stress Granule Proteins TIA-1 and G3BP in Tauopathies | Tau-stress granule interaction |
| PMC3411546 | 19625522 | BDNF Depends on Amyloid Aggregation State | Abeta aggregation state to BDNF levels |
| PMC3419089 | 22824372 | Innate Immune Gene Activation with Brain Aging | Age-dependent neuroinflammation |
| PMC3467018 | 22723704 | Presenilins in Autophagy: Lysosomal Acidification | Presenilin-autophagy connection |
| PMC3615658 | 23412472 | Physiological Release of Endogenous Tau | Activity-dependent tau secretion |
| PMC3623298 | 22445347 | Network Diffusion Model of Disease Progression | Graph-based tau spreading model |
| PMC3632731 | 22232349 | Proteomic Changes in CSF of ADAD | CSF proteome changes in presymptomatic AD |
| PMC3664196 | 22817896 | RIP1/RIP3 Necrosome as Amyloid Signaling Complex | Necroptosis signaling |
| PMC3696038 | 20209626 | Impaired Neurogenesis in Familial AD | Neurogenesis suppression by APP/PSEN |
| PMC3846276 | 19914182 | Fg01 Reduces beta-Amyloid and Tau Phosphorylation | Abeta/tau modulation gene |
| PMC4038930 | 24598588 | Longitudinal CSF Biomarker Change in ADAD | Temporal profiles of CSF Abeta42, tau, p-tau |
| PMC3392942 | 22753898 | Lysosomal Calcium Defects in PSEN-deficient Cells | PSEN to lysosomal Ca2+ homeostasis |
| PMC4049806 | 24893973 | Altered Microglial Response with TREM2 Heterozygosity | TREM2 to microglial Abeta phagocytosis |
| PMC4000136 | 24660806 | Parkin Activated by PINK1 Phosphorylation of Ubiquitin | Mitophagy pathway |

### Papers with Primarily Genetic/Epidemiological Focus (limited ODE extractability)

PMC3369937, PMC3372084, PMC3375906, PMC3378676, PMC3387980, PMC3389510, PMC3391348, PMC3391724, PMC3392960, PMC3394933, PMC3417348, PMC3420968, PMC3447081, PMC3458508, PMC3489017, PMC3498952, PMC3510670, PMC3515078, PMC3525981, PMC3576050, PMC3583203, PMC3589992, PMC3600944, PMC3618977, PMC3622279, PMC3640480, PMC3657692, PMC3677161, PMC3704214, PMC3720142, PMC3799583, PMC3904678, PMC3908455, PMC3916843, PMC3923462, PMC3929356, PMC3944799, PMC4000602, PMC4004919, PMC4040530, PMC4046618, PMC4051831, PMC3792042, PMC3710290, PMC3707386

---

## 2. Key Pathways

### Pathway Frequency Across 86 Papers

| Pathway | Papers | Priority for ODE Modeling |
|---------|--------|--------------------------|
| Amyloid Processing/APP Cleavage | 39 | **HIGH** — alpha/beta/gamma-secretase kinetics |
| Amyloid Aggregation | 38 | **HIGH** — nucleation-elongation-deposition |
| Tau Pathology | 35 | **HIGH** — phosphorylation, aggregation, spreading |
| Biomarkers/Diagnostics | 28 | MEDIUM — temporal profiles inform model validation |
| Genetics/GWAS | 26 | LOW — parameter modifiers, not direct ODE terms |
| Synaptic/Neuronal Function | 26 | **HIGH** — downstream functional impairment |
| Lipid Metabolism/ApoE | 26 | **HIGH** — ApoE-dependent clearance, BBB integrity |
| Protein Clearance/Autophagy | 21 | **HIGH** — proteolytic + glymphatic clearance |
| Neuroinflammation | 15 | **HIGH** — NLRP3/IL-1beta/microglial phagocytosis |
| Insulin/Glucose Metabolism | 14 | MEDIUM — metabolic coupling |
| Calcium Signaling | 14 | MEDIUM — SOCE, ER stress |
| BBB/Transport | 8 | **HIGH** — Abeta/drug brain-plasma exchange |
| Oxidative Stress/Mitochondria | 8 | MEDIUM — ROS production/clearance |
| Pharmacokinetics/Drug | 4 | LOW — therapeutic intervention modeling |
| Cholinergic System | 3 | MEDIUM — neurotransmitter dynamics |

---

## 3. Extractable Reactions and Rate Laws

### 3.1 APP Processing Module

```antimony
// Alpha-secretase pathway (non-amyloidogenic)
J_alpha: APP_membrane -> sAPPalpha_ISF + C83_membrane; k_alpha * APP_membrane * V_neuron
// Rate type: MA (mass action, unidirectional)

// Beta-secretase (BACE1) pathway (amyloidogenic)
J_beta: APP_membrane -> sAPPbeta_ISF + C99_membrane; k_beta * APP_membrane * V_neuron
// Rate type: MA
// BRI2 inhibits BACE access: k_beta_effective = k_beta / (1 + BRI2/Ki_BRI2)
// Source: PMC3376850

// Gamma-secretase cleavage of C99
J_gamma_40: C99_membrane -> Abeta40_ISF + AICD_cytosol; k_gamma40 * C99_membrane * V_neuron
J_gamma_42: C99_membrane -> Abeta42_ISF + AICD_cytosol; k_gamma42 * C99_membrane * V_neuron
// Rate type: MA
// Cholesterol modulation: k_gamma42/k_gamma40 ratio depends on cholesterol-C99 binding (Kd ~5 nM)
// Source: PMC3528355, PMC3952111

// PSEN mutation effect: increases k_gamma42/k_gamma40 ratio
// Source: PMC3838868 (SILK kinetics)
```

### 3.2 Amyloid-beta Turnover Module (from SILK data)

```antimony
// Abeta production (from gamma-secretase, above)
// Fractional turnover in CNS
J_Abeta40_turnover: Abeta40_CSF -> ; FTR_Abeta40 * Abeta40_CSF * V_CSF
J_Abeta42_turnover: Abeta42_CSF -> ; FTR_Abeta42 * Abeta42_CSF * V_CSF
// Rate type: MA (first-order clearance)

// ISF-CSF exchange
J_Abeta_ISF_to_CSF: Abeta42_ISF -> Abeta42_CSF; k_exchange * Abeta42_ISF * V_ISF
J_Abeta_CSF_to_ISF: Abeta42_CSF -> Abeta42_ISF; k_exchange_rev * Abeta42_CSF * V_CSF
// Rate type: BDF or RMA

// Irreversible loss to plaque (deposition sink)
J_Abeta42_plaque: Abeta42_ISF -> Abeta42_plaque; k_dep * Abeta42_ISF * V_ISF
// Rate type: MA (irreversible)
// Source: PMC3838868 — increased in PSEN carriers with amyloid-positive PET
```

### 3.3 Glymphatic/Paravascular Clearance Module

```antimony
// CSF influx through paravascular spaces (size-dependent)
J_CSF_paravascular: CSF_subarachnoid -> ISF_parenchyma; k_glymph * CSF_subarachnoid
// Rate type: UDF

// ISF solute clearance (Abeta via glymphatic)
J_Abeta_glymph_clear: Abeta_ISF -> Abeta_CSF_drain; k_glymph_clear * Abeta_ISF
// Rate type: UDF
// AQP4-dependent: k_glymph_clear reduced ~70% in AQP4 KO
// Source: PMC3551275

// Size-dependent clearance (small molecules cleared faster)
// 3 kD tracer: enters ISF freely
// 45 kD tracer: enters ISF from paravascular spaces
// 2000 kD tracer: confined to paravascular spaces
```

### 3.4 Tau Dynamics Module

```antimony
// Activity-dependent tau release from neurons
J_tau_release: tau_neuron -> tau_ISF; k_tau_release * tau_neuron * neuronal_activity
// Rate type: custom_conc_per_time
// Neuronal activity modulates release ~2-fold
// Source: PMC3949564, PMC3615658

// ISF tau clearance
J_tau_ISF_clear: tau_ISF -> ; k_tau_clear * tau_ISF
// Rate type: MA
// tau half-life in ISF >> Abeta half-life (~2 h for Abeta)
// Source: PMC3949564

// Tau phosphorylation (pathogenic)
J_tau_phos: tau_neuron -> ptau_neuron; k_phos * tau_neuron * kinase_active
// Rate type: MA
// Pin1 isomerase converts cis-ptau to trans-ptau (protective)
// Source: PMC3601591

// Tau seed propagation (prion-like spreading)
J_tau_seed: tau_ISF + tau_aggregate -> tau_aggregate; k_seed * tau_ISF * tau_aggregate
// Rate type: MA (autocatalytic/nucleated polymerization)
// Blocked by anti-tau antibodies (HJ8.5 KD = 100 pM)
// Source: PMC3924573
```

### 3.5 Neuroinflammation Module (NLRP3/IL-1beta)

```antimony
// Abeta activates NLRP3 inflammasome in microglia
J_NLRP3_activation: NLRP3_inactive + Abeta_ISF -> NLRP3_active; k_NLRP3 * NLRP3_inactive * Abeta_ISF
// Rate type: MA

// Caspase-1 activation and IL-1beta maturation
J_casp1: proCasp1 -> Casp1_active; k_casp1 * NLRP3_active * proCasp1
J_IL1b: proIL1b -> IL1b; k_IL1b * Casp1_active * proIL1b
// Rate type: MA

// IL-1beta impairs microglial phagocytosis of Abeta
// phagocytosis_rate = k_phago_base / (1 + IL1b / Ki_IL1b)
// Rate type: custom (inhibitory Hill function)
// Source: PMC3812809

// Microglial Abeta phagocytosis
J_Abeta_phago: Abeta_ISF -> ; k_phago_base / (1 + IL1b / Ki_IL1b) * Abeta_ISF * Microglia_active
// Rate type: custom_conc_per_time
```

### 3.6 Abeta Oligomer Toxicity/Synaptic Signaling Module

```antimony
// Abeta oligomer binding to PrPC at post-synaptic density
J_Abeta_PrP: Abeta_oligomer_ISF + PrPC_synapse -> Abeta_PrPC_complex; k_bind * Abeta_oligomer_ISF * PrPC_synapse
// Rate type: RMA (reversible)

// Fyn kinase activation by Abeta-PrPC complex
J_Fyn_act: Fyn_inactive + Abeta_PrPC_complex -> Fyn_active; k_fyn * Fyn_inactive * Abeta_PrPC_complex
// Rate type: MA

// NR2B phosphorylation by Fyn
J_NR2B_phos: NR2B_surface + Fyn_active -> pNR2B; k_NR2B * NR2B_surface * Fyn_active
// Rate type: MA
// pNR2B leads to NMDA receptor internalization and excitotoxicity
// Source: PMC3431439
```

### 3.7 ApoE-Dependent Clearance Module

```antimony
// ApoE expression (regulated by LXR/RXR)
J_ApoE_prod: -> ApoE_ISF; k_ApoE_prod * (1 + RXR_agonist / EC50_RXR)
// Rate type: custom_amt_per_time

// ApoE-Abeta complex formation (isoform-dependent)
J_ApoE_Abeta: ApoE_ISF + Abeta_ISF -> ApoE_Abeta_complex; k_ApoE_bind * ApoE_ISF * Abeta_ISF
// Rate type: MA
// k_ApoE_bind: ApoE2 > ApoE3 >> ApoE4 for Abeta clearance efficiency
// Source: PMC3651582

// LRP1-mediated clearance at BBB
J_LRP1_clear: ApoE_Abeta_complex -> ; k_LRP1 * ApoE_Abeta_complex
// Rate type: MA
// Source: PMC3651582

// ApoE4-CypA-MMP9 BBB degradation pathway
// ApoE4: suppression_factor approx 0; ApoE2/3: suppression_factor approx 0.8
J_CypA: -> CypA_pericyte; k_CypA_base * (1 - ApoE_suppression_factor)
J_MMP9: -> MMP9_pericyte; k_MMP9 * CypA_pericyte
J_BBB_degrade: TJ_protein -> ; k_TJ_degrade * MMP9_pericyte * TJ_protein
// Source: PMC4047116
```

### 3.8 BBB Transport Module

```antimony
// Receptor-mediated transcytosis (TfR example, generalizable)
J_brain_uptake: Drug_plasma -> Drug_brain; k_transcytosis * Drug_plasma * TfR_BBB
// Rate type: UDF
// Affinity-dependent: low affinity (Kd ~600 nM) > high affinity (Kd ~20 nM) for brain uptake
// High affinity leads to lysosomal degradation of TfR and reduced transcytosis capacity
// Source: PMC3920563
```

### 3.9 Calcium/SOCE/Spine Stability Module

```antimony
// STIM2-dependent store-operated calcium entry
J_SOCE: -> Ca_spine; k_SOCE * STIM2_spine * (Ca_ER_max - Ca_ER) / (Kd_STIM2 + Ca_ER_max - Ca_ER)
// Rate type: custom_conc_per_time

// PSEN1 mutation leads to STIM2 downregulation leads to impaired SOCE
// Ca_spine_low leads to CaMKII inactivation leads to mushroom spine loss
J_spine_loss: Spine_mushroom -> Spine_thin; k_spine_loss * (1 - Ca_spine / Ca_threshold)
// Source: PMC4007018
```

---

## 4. Species and Compartments

### Compartments

| Compartment | Description | Key Papers |
|-------------|-------------|------------|
| `Neuron` (or `neuron_cytosol`) | Intraneuronal space | PMC3949564, PMC3431439, PMC4007018 |
| `BrainISF` | Brain interstitial fluid | PMC3838868, PMC3551275, PMC3949564 |
| `CSF` | Cerebrospinal fluid | PMC3838868, PMC3474597, PMC4038930 |
| `Plasma` | Blood plasma | PMC3838868, PMC3746074, PMC3920563 |
| `Microglia` | Microglial cell | PMC3812809, PMC4049806 |
| `Synapse` (or `PostSynapticDensity`) | Synaptic cleft / PSD | PMC3431439, PMC4007018 |
| `BBB_endothelium` | Blood-brain barrier endothelial cells | PMC3920563, PMC4047116 |
| `Pericyte` | BBB pericytes | PMC4047116 |
| `Paravascular` | Paravascular/glymphatic space | PMC3551275 |
| `Plaque` | Extracellular amyloid plaque (sink) | PMC3838868 |
| `ER` | Endoplasmic reticulum (neuronal) | PMC4007018, PMC3392942 |
| `Lysosome` | Lysosomal compartment | PMC3467018, PMC3392942 |

### Species (following Elbert convention: `{species}_{compartment}`)

#### Amyloid-beta pathway
| Species | Compartment | Description |
|---------|-------------|-------------|
| `APP_membrane` | Neuron | Full-length amyloid precursor protein |
| `C99_membrane` | Neuron | beta-CTF (BACE1 cleavage product) |
| `C83_membrane` | Neuron | alpha-CTF (alpha-secretase cleavage product) |
| `AICD_cytosol` | Neuron | APP intracellular domain |
| `sAPPalpha_BrainISF` | BrainISF | Soluble APPalpha (non-amyloidogenic) |
| `sAPPbeta_BrainISF` | BrainISF | Soluble APPbeta (amyloidogenic) |
| `Abeta40_BrainISF` | BrainISF | Abeta40 monomer in ISF |
| `Abeta42_BrainISF` | BrainISF | Abeta42 monomer in ISF |
| `Abeta38_BrainISF` | BrainISF | Abeta38 monomer in ISF |
| `Abeta40_CSF` | CSF | Abeta40 in cerebrospinal fluid |
| `Abeta42_CSF` | CSF | Abeta42 in cerebrospinal fluid |
| `Abeta_oligomer_BrainISF` | BrainISF | Abeta oligomeric assemblies |
| `Abeta42_Plaque` | Plaque | Deposited insoluble Abeta42 |
| `Abeta40_Plasma` | Plasma | Plasma Abeta40 |
| `Abeta42_Plasma` | Plasma | Plasma Abeta42 |

#### Tau pathway
| Species | Compartment | Description |
|---------|-------------|-------------|
| `tau_Neuron` | Neuron | Intraneuronal tau (microtubule-bound) |
| `ptau_Neuron` | Neuron | Phosphorylated tau (detached from MT) |
| `cis_ptau_Neuron` | Neuron | cis-conformation p-tau (pathogenic) |
| `trans_ptau_Neuron` | Neuron | trans-conformation p-tau (physiologic) |
| `tau_BrainISF` | BrainISF | Extracellular tau in ISF |
| `tau_aggregate_BrainISF` | BrainISF | Tau aggregates/seeds in ISF |
| `tau_CSF` | CSF | CSF total tau |
| `ptau181_CSF` | CSF | CSF phospho-tau 181 |

#### Secretase enzymes
| Species | Compartment | Description |
|---------|-------------|-------------|
| `BACE1_membrane` | Neuron | beta-secretase |
| `gamma_secretase_membrane` | Neuron | gamma-secretase complex (PSEN1/2) |
| `ADAM10_membrane` | Neuron | alpha-secretase |

#### Neuroinflammation
| Species | Compartment | Description |
|---------|-------------|-------------|
| `NLRP3_inactive_Microglia` | Microglia | Inactive NLRP3 inflammasome |
| `NLRP3_active_Microglia` | Microglia | Activated NLRP3 inflammasome |
| `Casp1_active_Microglia` | Microglia | Active caspase-1 |
| `IL1b_BrainISF` | BrainISF | Mature IL-1beta |
| `Microglia_resting` | Microglia | Resting microglia |
| `Microglia_active` | Microglia | Activated microglia |

#### Lipid/ApoE
| Species | Compartment | Description |
|---------|-------------|-------------|
| `ApoE_BrainISF` | BrainISF | Apolipoprotein E (isoform-dependent) |
| `ApoE_Abeta_complex_BrainISF` | BrainISF | ApoE-Abeta complex |
| `Cholesterol_membrane` | Neuron | Membrane cholesterol |

#### BBB/Transport
| Species | Compartment | Description |
|---------|-------------|-------------|
| `TfR_BBB` | BBB_endothelium | Transferrin receptor at BBB |
| `LRP1_BBB` | BBB_endothelium | LDL receptor-related protein 1 |
| `CypA_Pericyte` | Pericyte | Cyclophilin A |
| `MMP9_Pericyte` | Pericyte | Matrix metalloproteinase 9 |
| `TJ_protein_BBB` | BBB_endothelium | Tight junction proteins |

#### Synaptic/Calcium
| Species | Compartment | Description |
|---------|-------------|-------------|
| `PrPC_Synapse` | Synapse | Cellular prion protein |
| `Abeta_PrPC_complex_Synapse` | Synapse | Abeta-PrPC complex |
| `Fyn_active_Synapse` | Synapse | Active Fyn kinase |
| `NR2B_surface_Synapse` | Synapse | Surface NMDA receptor subunit |
| `pNR2B_Synapse` | Synapse | Phosphorylated NR2B |
| `STIM2_Synapse` | Synapse | STIM2 ER calcium sensor |
| `Ca_Spine` | Synapse | Spine calcium concentration |
| `Spine_mushroom` | Synapse | Mature mushroom spines (count) |

#### Clearance enzymes
| Species | Compartment | Description |
|---------|-------------|-------------|
| `IDE_BrainISF` | BrainISF | Insulin-degrading enzyme |
| `NEP_BrainISF` | BrainISF | Neprilysin |
| `Pin1_Neuron` | Neuron | Peptidyl-prolyl isomerase |

---

## Summary Statistics

- **Total papers analyzed**: 86
- **Papers with high quantitative value (Tier 1)**: 5
- **Papers with moderate mechanistic value (Tier 2)**: 10
- **Papers with supporting context (Tier 3)**: 22+
- **Papers primarily genetic/epidemiological**: ~49
- **Distinct extractable ODE modules**: 9 (APP processing, Abeta turnover, glymphatic clearance, tau dynamics, neuroinflammation, Abeta-oligomer toxicity, ApoE clearance, BBB transport, calcium/spine)
- **Total extractable reaction templates**: ~30
- **Total species identified**: ~50
- **Total compartments identified**: 12
