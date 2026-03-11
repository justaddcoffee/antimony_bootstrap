# Batch 8 Paper Analysis: Quantitative Mechanisms for Alzheimer ODE Modeling

**Date:** 2026-02-24
**Papers analyzed:** 86 (PMC5310835 through PMC5711511)
**Source:** Primary_Alzforum collection

---

## 1. Papers with Quantitative/Mechanistic Data

### Tier 1: Strong quantitative data (score >= 3)

| PMC ID | Title | Quant Score | Key Quantitative Terms |
|--------|-------|-------------|----------------------|
| PMC5310835 | ApoE2, ApoE3 and ApoE4 Differentially Stimulate APP Transcription and Abeta Secretion | 6 | rate constant, half-life, degradation rate, first-order, kon, dose-response |
| PMC5378956 | Inhibition of delta-secretase improves cognitive functions in mouse models of AD | 6 | rate constant, half-life, pharmacokinetic, first-order, second-order, IC50 |
| PMC5523817 | Diverse requirements for microglial survival, specification, and function | 3 | half-life, Km, dose-response |
| PMC5567785 | Amyloid beta concentrations and stable isotope labeling kinetics of human plasma | 3 | half-life, production rate, turnover rate |
| PMC5644271 | Design of Bayesian adaptive phase 2 trial for BAN2401 | 3 | pharmacokinetic, first-order, dose-response |

### Tier 2: Moderate quantitative data (score = 2)

| PMC ID | Title | Key Data |
|--------|-------|----------|
| PMC5512541 | Neuronal heparan sulfates promote amyloid pathology by modulating brain Abeta clearance | half-life, clearance rate; Abeta ISF half-life 1-2 hours (mouse), ~8 hours (human CSF) |
| PMC5540680 | The Lifespan and Turnover of Microglia in the Human Brain | mathematical model, turnover rate; microglia turnover median 28%/year (0.08%/day), average lifespan 4.2 years |
| PMC5500003 | RNA stores tau reversibly in complex coacervates | Kd, dissociation constant; tau-tRNA Kd = 735+/-217 nM (4R2N), 372+/-9 nM (K18) |
| PMC5656389 | Gamma frequency entrainment attenuates amyloid load and modifies microglia | Km, clearance rate; 40 Hz stimulation reduces Abeta1-40 and Abeta1-42 levels |
| PMC5653973 | C9ORF72 dipeptide repeat proteins associate with U2 snRNP | Kd, kon |
| PMC5388136 | Genome-scale networks link neurodegenerative disease genes to alpha-synuclein | Km, first-order kinetics |
| PMC5469297 | 2014 Update of the AD Neuroimaging Initiative | half-life, pharmacokinetic (review) |

### Tier 3: Qualitative mechanism data useful for model structure

| PMC ID | Title | Relevant Pathways |
|--------|-------|-------------------|
| PMC5404890 | Neurotoxic reactive astrocytes are induced by activated microglia | Neuroinflammation: IL-1alpha + TNFalpha + C1q --> A1 astrocyte induction |
| PMC5634784 | Clearance of beta-amyloid facilitated by apoE and circulating HDL | ApoE + HDL synergize for Abeta transport across cerebral vessels |
| PMC5573224 | TREM2 maintains microglial metabolic fitness in AD | TREM2 signaling --> mTOR --> metabolic fitness for phagocytosis |
| PMC5663386 | TREM2 deficiency attenuates neuroinflammation in tauopathy | TREM2 modulates microglial activation and tau pathology |
| PMC5644120 | TREM2 deficiency exacerbates tau pathology via dysregulated kinase signaling | TREM2 --> GSK3beta/CDK5 regulation --> tau phosphorylation |
| PMC5384262 | FAD presenilin 1 mutants promote gamma-secretase cleavage of STIM1 | PS1 mutations --> STIM1 cleavage --> impaired SOCE/calcium signaling |
| PMC5650912 | AD macrophages shuttle Abeta from neurons to vessels (CAA) | Macrophage phagocytosis of Abeta, impaired BBB export in AD |
| PMC5522360 | Brain perivascular macrophages initiate neurovascular dysfunction | Abeta --> CD36 --> Nox2/NADPH oxidase --> ROS --> neurovascular dysfunction |
| PMC5681558 | CSF outflow predominantly through lymphatic vessels, reduced in aged mice | Lymphatic CSF drainage pathway, reduced with aging |
| PMC5552202 | Cryo-EM structures of Tau filaments from AD brain | PHF and SF tau structural data |
| PMC5510615 | Pathological alpha-synuclein transmission via LAG3 binding | LAG3 receptor-mediated alpha-synuclein uptake (Kd reported) |
| PMC5339672 | Soluble TREM2 induces inflammatory responses and enhances microglial survival | sTREM2 promotes survival + inflammation in microglia |

---

## 2. Key Pathways

### Pathway frequency across all 86 papers (papers with >= 2 keyword hits):

| Pathway | Paper Count | Top PMC IDs |
|---------|------------|-------------|
| **Abeta dynamics** (aggregation, clearance, oligomers, fibrils) | 42 | PMC5355803, PMC5512541, PMC5656389, PMC5650912, PMC5634784 |
| **Immune clearance** (phagocytosis, LRP1, RAGE, neprilysin, transport) | 38 | PMC5540680, PMC5650912, PMC5656389, PMC5519492, PMC5681558 |
| **Neuroinflammation** (microglia, astrocytes, cytokines, TREM2) | 27 | PMC5663386, PMC5404890, PMC5644120, PMC5573224, PMC5528863 |
| **Synaptic** (LTP/LTD, glutamate, NMDA, cholinergic) | 20 | PMC5469297, PMC5341123, PMC5384262, PMC5589746, PMC5656389 |
| **Tau pathology** (phosphorylation, tangles, spreading) | 18 | PMC5552202, PMC5363269, PMC5589746, PMC5500003, PMC5710183 |
| **Amyloid processing** (APP, secretases, BACE, presenilin) | 17 | PMC5310835, PMC5378956, PMC5384262, PMC5505565, PMC5623859 |
| **Lipid metabolism** (ApoE, cholesterol, HDL) | 16 | PMC5310835, PMC5634784, PMC5341123, PMC5646357, PMC5360460 |
| **Vascular/BBB** (cerebrovascular, pericytes, perivascular, glymphatic) | 14 | PMC5522360, PMC5634784, PMC5528863, PMC5681558, PMC5550770 |
| **Autophagy/proteostasis** (lysosome, proteasome, endosome) | 8 | PMC5336134, PMC5383508, PMC5558861, PMC5578869 |
| **Oxidative stress** (ROS, mitochondria) | 6 | PMC5336134, PMC5522360, PMC5573225, PMC5506489 |
| **Insulin signaling** (IGF, AKT, GSK3, PI3K) | 5 | PMC5573224, PMC5339672, PMC5341123 |
| **Calcium signaling** | 4 | PMC5384262, PMC5388136 |

---

## 3. Extractable Reactions and Rate Laws

### 3.1 Abeta Production and Processing (APP pathway)

**Source: PMC5310835 (ApoE-stimulated APP transcription)**

```antimony
// ApoE-receptor binding activates DLK-MKK7-ERK1/2 cascade
// ApoE4 > ApoE3 > ApoE2 potency for stimulating Abeta secretion
J_ApoE_bind: ApoE_BrainISF + ApoER_Neuron -> ApoE_ApoER_Neuron; k_bind_ApoE * ApoE_BrainISF * ApoER_Neuron;
J_DLK_induction: ApoE_ApoER_Neuron -> ApoE_ApoER_Neuron + DLK_Neuron; k_DLK_induction * ApoE_ApoER_Neuron;
J_MKK7_phos: DLK_Neuron + MKK7_Neuron -> DLK_Neuron + pMKK7_Neuron; k_MKK7_phos * DLK_Neuron * MKK7_Neuron;
J_ERK_phos: pMKK7_Neuron + ERK12_Neuron -> pMKK7_Neuron + pERK12_Neuron; k_ERK_phos * pMKK7_Neuron * ERK12_Neuron;
J_cFos_phos: pERK12_Neuron + cFos_Neuron -> pERK12_Neuron + pcFos_Neuron; k_cFos_phos * pERK12_Neuron * cFos_Neuron;
J_APP_transcription: pcFos_Neuron -> pcFos_Neuron + APP_mRNA_Neuron; k_APP_transcription * pcFos_Neuron;
J_APP_translation: APP_mRNA_Neuron -> APP_Neuron; k_APP_translation * APP_mRNA_Neuron;
J_beta_cleavage: APP_Neuron -> Abeta40_BrainISF + sAPPbeta_BrainISF; k_beta_cleavage * BACE1_Neuron * APP_Neuron;
J_gamma_cleavage: APP_Neuron -> Abeta42_BrainISF + sAPPbeta_BrainISF; k_gamma_cleavage * gamma_sec_Neuron * APP_Neuron;
```

Quantitative data:
- ApoE stimulates 2-3 fold more Abeta40/42 secretion vs. control
- ERK1/2 phosphorylation: 2-5 fold increase with ApoE
- MKK7 phosphorylation: ~4-5 fold with ApoE3

**Source: PMC5378956 (delta-secretase/AEP inhibition)**

```antimony
// Delta-secretase cleaves both APP and tau
J_AEP_APP: AEP_Lysosome + APP_Neuron -> AEP_Lysosome + APP_N585_Neuron + APP_C585_Neuron; k_AEP_APP * AEP_Lysosome * APP_Neuron;
J_AEP_tau: AEP_Lysosome + tau_Neuron -> AEP_Lysosome + tau_N368_Neuron + tau_C368_Neuron; k_AEP_tau * AEP_Lysosome * tau_Neuron;
J_inh_bind: Compound11 + AEP_Lysosome -> Compound11_AEP_Lysosome; k_inh_on * Compound11 * AEP_Lysosome;
J_inh_unbind: Compound11_AEP_Lysosome -> Compound11 + AEP_Lysosome; k_inh_off * Compound11_AEP_Lysosome;
```

Quantitative data:
- IC50 for Compound 11 vs delta-secretase: ~700 nM
- IC50 for Compound 38: ~370 nM
- IC50 for BB1: ~130 nM (most potent)
- Selectivity: >= 80-fold over caspases (Compound 11)

### 3.2 Abeta Clearance and Dynamics

**Source: PMC5567785 (Abeta SILK kinetics)**

```antimony
// Abeta isoform turnover in plasma and CNS
// Half-life of Abeta in plasma: ~3 hours; in CNS: ~9 hours
J_prod_Ab40: -> Abeta40_Plasma; k_prod_Abeta40;
J_prod_Ab42: -> Abeta42_Plasma; k_prod_Abeta42;
J_clear_Ab40: Abeta40_Plasma -> ; k_clear_Abeta40 * Abeta40_Plasma; // t1/2 ~ 3 hr, k = 0.231/hr
J_clear_Ab42: Abeta42_Plasma -> ; k_clear_Abeta42 * Abeta42_Plasma; // t1/2 ~ 3 hr
J_clear_Ab42_CSF: Abeta42_CSF -> ; k_clear_Abeta42_CSF * Abeta42_CSF; // t1/2 ~ 9 hr, k = 0.077/hr
```

Quantitative data:
- Plasma Abeta half-life: ~3 hours (k_clear = 0.231/hr)
- CNS Abeta half-life: ~9 hours (k_clear = 0.077/hr)
- Abeta38 has faster turnover than Abeta40 and Abeta42
- Abeta42 turnover faster relative to Abeta40 in amyloid-positive individuals

**Source: PMC5512541 (Neuronal HS modulates Abeta clearance)**

```antimony
// Heparan sulfate promotes Abeta aggregation and reduces clearance
J_clear_ISF: Abeta_BrainISF -> ; k_clear_ISF * Abeta_BrainISF; // t1/2 1-2 hr mouse
J_HS_bind: Abeta_BrainISF + HS_Neuron -> Abeta_HS_BrainISF; k_HS_bind * Abeta_BrainISF * HS_Neuron;
J_HS_agg: Abeta_HS_BrainISF -> Abeta_aggregate_BrainParenchyma; k_HS_agg * Abeta_HS_BrainISF;
```

**Source: PMC5634784 (ApoE/HDL-mediated Abeta clearance at BBB)**

```antimony
// ApoE and HDL facilitate Abeta transport across cerebral vessels
J_ApoE_bind_Ab: Abeta_BrainISF + ApoE_BrainISF -> Abeta_ApoE_BrainISF; k_ApoE_bind * Abeta_BrainISF * ApoE_BrainISF;
J_transport_ApoE: Abeta_ApoE_BrainISF -> Abeta_BrainVessel; k_transport_ApoE * Abeta_ApoE_BrainISF;
J_HDL_bind_Ab: Abeta_BrainISF + HDL_BrainVessel -> Abeta_HDL_BrainVessel; k_HDL_bind * Abeta_BrainISF * HDL_BrainVessel;
J_transport_HDL: Abeta_HDL_BrainVessel -> Abeta_Plasma; k_transport_HDL * Abeta_HDL_BrainVessel;
```

### 3.3 Tau Dynamics

**Source: PMC5500003 (Tau-RNA phase separation)**

```antimony
// Tau-tRNA binding and phase separation
J_tau_tRNA_bind: tau_Neuron + tRNA_Neuron -> tau_tRNA_Neuron; k_on_tau_tRNA * tau_Neuron * tRNA_Neuron;
J_tau_tRNA_unbind: tau_tRNA_Neuron -> tau_Neuron + tRNA_Neuron; k_off_tau_tRNA * tau_tRNA_Neuron;
// Kd = k_off/k_on = 735 nM (4R2N); 372 nM (K18)
```

Quantitative data:
- Tau-tRNA Kd = 735+/-217 nM (full-length 4R2N)
- Tau-tRNA Kd = 372+/-9 nM (K18 domain)
- Random RNA Kd = 832+/-94 nM (Hill coefficient 2.6)

**Source: PMC5644120 (TREM2 regulates tau phosphorylation kinases)**

```antimony
// TREM2 deficiency leads to dysregulated GSK3beta and CDK5
J_tau_phos_GSK3: GSK3beta_active_Neuron + tau_Neuron -> GSK3beta_active_Neuron + pTau_Neuron; k_tau_phos_GSK3 * GSK3beta_active_Neuron * tau_Neuron;
J_tau_phos_CDK5: CDK5_active_Neuron + tau_Neuron -> CDK5_active_Neuron + pTau_Neuron; k_tau_phos_CDK5 * CDK5_active_Neuron * tau_Neuron;
J_tau_dephos: pTau_Neuron -> tau_Neuron; k_tau_dephos * pTau_Neuron;
```

**Source: PMC5552202 (Tau filament structures)**

```antimony
// Tau aggregation pathway
J_tau_oligomerize: 2 pTau_Neuron -> pTau_oligomer_Neuron; k_tau_oligomerize * pTau_Neuron * pTau_Neuron;
J_PHF_elongation: pTau_oligomer_Neuron + pTau_Neuron -> PHF_Neuron; k_PHF_elongation * pTau_oligomer_Neuron * pTau_Neuron;
```

### 3.4 Neuroinflammation Cascade

**Source: PMC5404890 (Microglia-induced A1 reactive astrocytes)**

```antimony
// Activated microglia secrete cytokines that induce A1 astrocytes
J_IL1a_secrete: Microglia_act_BrainP -> Microglia_act_BrainP + IL1alpha_BrainISF; k_IL1a * Microglia_act_BrainP;
J_TNFa_secrete: Microglia_act_BrainP -> Microglia_act_BrainP + TNFalpha_BrainISF; k_TNFa * Microglia_act_BrainP;
J_C1q_secrete: Microglia_act_BrainP -> Microglia_act_BrainP + C1q_BrainISF; k_C1q * Microglia_act_BrainP;
J_A1_induction: Astrocyte_rest_BrainP -> Astrocyte_A1_BrainP; k_A1_ind * IL1alpha_BrainISF * TNFalpha_BrainISF * C1q_BrainISF * Astrocyte_rest_BrainP;
J_A1_neurotox: Astrocyte_A1_BrainP -> ; k_A1_neurotox * Astrocyte_A1_BrainP; // neuron/oligo death
```

**Source: PMC5540680 (Microglia turnover)**

```antimony
// Microglia population dynamics
// Turnover rate: 28% per year; Average lifespan: 4.2 years
J_microglia_birth: -> Microglia_BrainParenchyma; k_microglia_prod; // zero-order
J_microglia_death: Microglia_BrainParenchyma -> ; k_microglia_death * Microglia_BrainParenchyma; // k=4.52e-4/day
```

Quantitative data:
- Microglial turnover: median 28% per year
- Microglial lifespan: average 4.2 years
- Daily turnover rate: 0.08% per day

### 3.5 TREM2 Signaling Network

**Source: PMC5339672, PMC5573224, PMC5623839, PMC5623859**

```antimony
// TREM2 shedding, mTOR activation, and microglial metabolic fitness
J_TREM2_shed: TREM2_Microglia -> sTREM2_BrainISF + TREM2stub_Microglia; k_TREM2_shed * TREM2_Microglia;
J_TREM2_activate: TREM2_Microglia + TREM2_ligand_BrainISF -> TREM2_active_Microglia; k_TREM2_act * TREM2_Microglia * TREM2_ligand_BrainISF;
J_mTOR_activate: TREM2_active_Microglia -> TREM2_active_Microglia + mTOR_active_Microglia; k_mTOR_act * TREM2_active_Microglia;
J_phago_boost: mTOR_active_Microglia -> Microglia_phagocytic_BrainP; k_metab_boost * mTOR_active_Microglia;
```

### 3.6 Vascular/BBB Transport

**Source: PMC5522360 (Perivascular macrophages and neurovascular dysfunction)**

```antimony
// Abeta activates CD36 on perivascular macrophages --> ROS production
J_CD36_bind: Abeta_BrainISF + CD36_PVM -> Abeta_CD36_PVM; k_CD36_bind * Abeta_BrainISF * CD36_PVM;
J_Nox2_activate: Abeta_CD36_PVM -> Nox2_active_PVM; k_Nox2_act * Abeta_CD36_PVM;
J_ROS_produce: Nox2_active_PVM -> ROS_BrainParenchyma; k_ROS_prod * Nox2_active_PVM;
```

**Source: PMC5681558 (CSF lymphatic drainage)**

```antimony
// CSF outflow via lymphatic vessels (reduced with aging)
J_lymph_drain: CSF_Subarachnoid -> CSF_Lymphatic; k_lymph_drain * CSF_Subarachnoid;
J_venous_drain: CSF_Subarachnoid -> CSF_Venous; k_venous_drain * CSF_Subarachnoid;
```

**Source: PMC5650912 (Macrophage Abeta shuttle to vessels)**

```antimony
// Macrophages phagocytose Abeta but get stuck at BBB --> CAA
J_phago_Ab: Macrophage_BrainP + Abeta_BrainISF -> Macrophage_Abeta_BrainP; k_phago * Macrophage_BrainP * Abeta_BrainISF;
J_BBB_export: Macrophage_Abeta_BrainP -> Macrophage_Blood + Abeta_BrainVessel; k_BBB_export * Macrophage_Abeta_BrainP;
J_mac_apoptosis: Macrophage_Abeta_BrainP -> ; k_apoptosis * Macrophage_Abeta_BrainP;
```

---

## 4. Species and Compartments

### 4.1 Species Inventory (Elbert naming convention: Species_Compartment)

#### Amyloid Pathway Species
| Species | Compartments | Source Papers |
|---------|-------------|---------------|
| APP | Neuron, BrainISF | PMC5310835, PMC5378956, PMC5384262 |
| APP_mRNA | Neuron | PMC5310835 |
| Abeta40 | BrainISF, CSF, Plasma | PMC5310835, PMC5567785, PMC5512541 |
| Abeta42 | BrainISF, CSF, Plasma | PMC5310835, PMC5567785, PMC5512541 |
| Abeta38 | Plasma | PMC5567785 |
| Abeta_oligomer | BrainISF | PMC5355803, PMC5367518, PMC5650912 |
| Abeta_fibril | BrainISF | PMC5552202, PMC5656389 |
| Abeta_plaque | BrainParenchyma | PMC5656389, PMC5512541, PMC5663717 |
| sAPPbeta | BrainISF | PMC5310835 |
| sAPPalpha | BrainISF | PMC5310835 |
| CTF | Neuron | PMC5310835, PMC5384262 |
| AICD | Neuron | PMC5384262 |

#### ApoE/Lipid Species
| Species | Compartments | Source Papers |
|---------|-------------|---------------|
| ApoE2/3/4 | BrainISF, Astrocyte | PMC5310835 |
| ApoER (ApoE receptor) | Neuron | PMC5310835 |
| HDL | Plasma, BrainVessel | PMC5634784 |
| Cholesterol | Astrocyte, BrainISF | PMC5523817, PMC5341123 |

#### Tau Species
| Species | Compartments | Source Papers |
|---------|-------------|---------------|
| tau | Neuron | PMC5500003, PMC5378956, PMC5644120 |
| pTau | Neuron | PMC5644120, PMC5552202, PMC5589746 |
| tau_tRNA | Neuron | PMC5500003 |
| tau_oligomer | Neuron | PMC5500003 |
| PHF | Neuron | PMC5552202 |
| SF | Neuron | PMC5552202 |
| tau_N368 | Neuron | PMC5378956 (AEP-cleaved fragment) |

#### Enzyme/Receptor Species
| Species | Compartments | Source Papers |
|---------|-------------|---------------|
| BACE1 | Neuron, Endosome | PMC5310835, PMC5378956 |
| gamma_secretase | Neuron | PMC5384262, PMC5310835 |
| AEP (delta-secretase) | Lysosome | PMC5378956 |
| PS1 (presenilin 1) | Neuron | PMC5384262 |
| TREM2 | Microglia | PMC5573224, PMC5663386, PMC5644120 |
| sTREM2 | BrainISF, CSF | PMC5339672, PMC5623839, PMC5623859, PMC5385711 |
| CD36 | PVM | PMC5522360 |
| CSF1R | Microglia | PMC5523817 |
| LAG3 | Neuron | PMC5510615 |
| LRP1 | BrainVessel | PMC5634784 |

#### Signaling Species
| Species | Compartments | Source Papers |
|---------|-------------|---------------|
| DLK | Neuron | PMC5310835 |
| pMKK7 | Neuron | PMC5310835 |
| pERK12 | Neuron | PMC5310835 |
| pcFos | Neuron | PMC5310835 |
| GSK3beta | Neuron | PMC5644120 |
| CDK5 | Neuron | PMC5644120 |
| mTOR | Microglia | PMC5573224 |
| Nox2 | PVM | PMC5522360 |
| STIM1 | Neuron (ER) | PMC5384262 |

#### Immune/Inflammatory Species
| Species | Compartments | Source Papers |
|---------|-------------|---------------|
| Microglia_resting | BrainParenchyma | PMC5540680, PMC5523817 |
| Microglia_activated | BrainParenchyma | PMC5404890, PMC5656389 |
| Astrocyte_resting | BrainParenchyma | PMC5404890 |
| Astrocyte_A1 | BrainParenchyma | PMC5404890 |
| Macrophage | Blood, BrainParenchyma | PMC5650912 |
| IL1alpha | BrainISF | PMC5404890 |
| TNFalpha | BrainISF | PMC5404890 |
| C1q | BrainISF | PMC5404890 |
| CSF1 | BrainISF | PMC5523817 |
| TGFbeta2 | BrainISF | PMC5523817 |
| ROS | BrainParenchyma | PMC5522360 |

### 4.2 Compartments

| Compartment | Description | Source Papers |
|-------------|-------------|---------------|
| Neuron | Neuronal cytoplasm/membrane | PMC5310835, PMC5384262, PMC5378956 |
| Neuron_ER | Neuronal endoplasmic reticulum | PMC5384262 |
| Endosome | Endosomal compartment | PMC5378956 |
| Lysosome | Lysosomal compartment | PMC5378956, PMC5558861 |
| BrainISF | Brain interstitial fluid | PMC5512541, PMC5567785 |
| BrainParenchyma | Brain tissue (cells + ECM) | PMC5404890, PMC5656389, PMC5663386 |
| CSF | Cerebrospinal fluid | PMC5567785, PMC5681558, PMC5385711 |
| Plasma | Blood plasma | PMC5567785, PMC5634784 |
| BrainVessel | Cerebral vasculature (endothelium) | PMC5634784, PMC5650912, PMC5522360 |
| PVM | Perivascular macrophage space | PMC5522360 |
| Astrocyte | Astrocyte cytoplasm | PMC5310835, PMC5404890, PMC5523817 |
| Microglia | Microglial cytoplasm | PMC5573224, PMC5540680, PMC5523817 |
| Lymphatic | Lymphatic drainage pathway | PMC5681558 |
| Subarachnoid | Subarachnoid space | PMC5681558 |

---

## 5. Summary of Key Quantitative Parameters

| Parameter | Value | Units | Source |
|-----------|-------|-------|--------|
| Abeta plasma half-life | ~3 | hours | PMC5567785 |
| Abeta CNS half-life | ~9 | hours | PMC5567785 |
| Abeta ISF half-life (mouse) | 1-2 | hours | PMC5512541 |
| Abeta CSF half-life (human) | ~8 | hours | PMC5512541 |
| Microglia turnover rate | 28 | % per year | PMC5540680 |
| Microglia average lifespan | 4.2 | years | PMC5540680 |
| Microglia daily turnover | 0.08 | % per day | PMC5540680 |
| Tau-tRNA Kd (4R2N) | 735+/-217 | nM | PMC5500003 |
| Tau-tRNA Kd (K18) | 372+/-9 | nM | PMC5500003 |
| Tau-random RNA Kd | 832+/-94 | nM | PMC5500003 |
| AEP IC50 (Compound 11) | ~700 | nM | PMC5378956 |
| AEP IC50 (Compound 38) | ~370 | nM | PMC5378956 |
| AEP IC50 (BB1) | ~130 | nM | PMC5378956 |
| ApoE-induced ERK1/2 activation | 2-5 | fold | PMC5310835 |
| ApoE-induced MKK7 activation | 4-5 | fold | PMC5310835 |
| ApoE-induced Abeta secretion | 2-3 | fold | PMC5310835 |
| ApoE-induced DLK induction | 2-4 | fold | PMC5310835 |

---

## 6. Priority Modules for Antimony Model Construction

Based on this batch, the following modules have the strongest quantitative support:

1. **Abeta_turnover_kinetics** -- Plasma and CNS Abeta production/clearance with SILK-derived half-lives (PMC5567785, PMC5512541)
2. **ApoE_APP_signaling** -- ApoE isoform-dependent APP transcription via DLK/ERK cascade (PMC5310835)
3. **Microglia_population_dynamics** -- Turnover, survival factors, activation states (PMC5540680, PMC5523817)
4. **Neuroinflammation_A1_astrocytes** -- Microglia-astrocyte cytokine cascade (PMC5404890)
5. **Tau_phase_separation** -- Tau-RNA LLPS with measured Kd values (PMC5500003)
6. **TREM2_signaling** -- TREM2 shedding, mTOR activation, kinase regulation (PMC5573224, PMC5644120, PMC5339672)
7. **BBB_Abeta_transport** -- ApoE/HDL-mediated cerebrovascular clearance (PMC5634784, PMC5650912)
8. **Perivascular_ROS** -- CD36/Nox2 neurovascular dysfunction pathway (PMC5522360)
9. **AEP_dual_cleavage** -- Delta-secretase cleaving APP and tau with IC50 data (PMC5378956)
10. **CSF_lymphatic_drainage** -- Age-dependent lymphatic outflow (PMC5681558)

---

## 7. Papers Without Modeling Utility

60 of 86 papers scored 0 on quantitative mechanism keywords. These are primarily epidemiological, clinical trial, imaging, genetic screening, or structural biology studies without extractable rate parameters. However, several (PMC5404890, PMC5634784, PMC5339672, PMC5522360, PMC5681558, PMC5644120, PMC5663386) still provide valuable qualitative pathway topology for model structure and are listed in Tier 3 above.