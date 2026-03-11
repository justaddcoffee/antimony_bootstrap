# Batch 1 Paper Analysis: Quantitative Mechanisms for Alzheimer's Antimony Modeling

**Batch**: batch_1 (86 papers from Primary_Alzforum)
**Date**: 2026-02-24
**Purpose**: Identify papers with quantitative biological mechanisms extractable as ODE equations in Antimony format

---

## 1. Papers with Quantitative/Mechanistic Data

Papers are tiered by density of extractable kinetic parameters, rate constants, binding affinities, and reaction descriptions. Scoring is based on strict pattern matching for kinetic terms (rate constants, Km, Vmax, IC50, half-life, enzyme kinetics, etc.) and numerical values with biologically relevant units (nM, ng/mL, min-1, etc.).

### Tier 1: Best Quantitative Content (24 papers, score >= 3)

These papers contain the highest density of quantitative measurements and mechanistic reaction descriptions among the batch. They should be deep-read first for parameter extraction.

#### PMC2578820 (score: 4)
**Title**: Aβ plaques lead to aberrant regulation of calcium homeostasis in vivo resulting in structural and functional disruption of neuronal networks

**Pathways**: amyloid_processing, ab_aggregation, ab_clearance, synaptic_function, oxidative_stress, calcium

**Quantitative values**: 80 nM; 277 nM; 250 nM; 41 nM; 7 nM

---

#### PMC1952204 (score: 3)
**Title**: Reducing Amyloid Plaque Burden via Ex Vivo Gene Delivery of an Aβ-Degrading Protease: A Novel Therapeutic Approach to Alzheimer Disease

**Pathways**: amyloid_processing, ab_aggregation, ab_clearance, tau_pathology, synaptic_function, oxidative_stress

**Quantitative values**: 2 mM; 50 mM; 150 mM; 2 mM; 5 mM

**Reaction descriptions**: clearance of the Aβ peptide is becoming; clearance of Aβ in the brain by ex vivo; cleavage of APP; cleavage of DAGNPG

---

#### PMC2150733 (score: 3)
**Title**: The Alzheimer Amyloid Precursor Protein (APP) and Fe65, an APP-Binding Protein, Regulate Cell Movement

**Pathways**: ab_clearance, oxidative_stress

**Quantitative values**: 10 mM; 150 mM; 0.1 mM; 50 mM

**Reaction descriptions**: binding of FE65 to the YENPTY motif m

---

#### PMC2174559 (score: 3)
**Title**: Capacitative Calcium Entry Deficits and Elevated Luminal Calcium Content in Mutant Presenilin-1 Knockin Mice

**Pathways**: amyloid_processing, ab_aggregation, ab_clearance, calcium

**Quantitative values**: 0.5 mM; 120 mM; 5.4 mM; 0.8 mM; 2 mM

**Reaction descriptions**: production of the longer species of β-am; phosphorylation of tau 

---

#### PMC2442205 (score: 3)
**Title**: SERCA pump activity is physiologically regulated by presenilin and regulates amyloid β production

**Pathways**: amyloid_processing, ab_clearance, oxidative_stress, calcium

**Quantitative values**: 0 mM; 70 nM; 50 nM; 0 mM

**Reaction descriptions**: cleavage of the C99 fragment of APP to; cleavage of the amyloid precursor prot; clearance of cytosolic Ca 2

---

#### PMC2597474 (score: 3)
**Title**: Microglial dysfunction and defective β-amyloid clearance pathways in aging Alzheimer’s disease mice

**Pathways**: amyloid_processing, ab_aggregation, ab_clearance, neuroinflammation, oxidative_stress

**Quantitative values**: 2mM; 2mM

**Reaction descriptions**: clearance of Aβ before formation of sen

---

#### PMC2671606 (score: 3)
**Title**: Cerebrospinal Fluid Concentration of Brain-Derived Neurotrophic Factor and Cognitive Function in Non-Demented Subjects

**Pathways**: ab_clearance, synaptic_function, oxidative_stress, lipid_ApoE

---

#### PMC2673049 (score: 3)
**Title**: Picomolar amyloid-β positively modulates synaptic plasticity and memory in hippocampus

**Pathways**: amyloid_processing, ab_clearance, synaptic_function, oxidative_stress, calcium

**Quantitative values**: 1 mM; 124.0 mM; 4.4 mM; 1.0 mM; 25.0 mM

**Reaction descriptions**: production of other; cleavage of the amyloid-β precursor pr

---

#### PMC2676733 (score: 3)
**Title**: Autophagy Induction and Autophagosome Clearance in Neurons: Relationship to Autophagic Pathology in Alzheimer's Disease

**Pathways**: ab_clearance, tau_pathology, oxidative_stress

**Quantitative values**: 0.5mM; 10nM

**Reaction descriptions**: clearance of autophagosomes by ; clearance by lysosomes ; Degradation of the cytoplasmic substrates

---

#### PMC2693334 (score: 3)
**Title**: Deletion of Mint proteins decreases amyloid production in transgenic mouse models of Alzheimer’s disease

**Pathways**: amyloid_processing, ab_clearance, oxidative_stress

**Quantitative values**: 20 mM; 10 mM; 1 mM; 10 mM; 150 mM

**Reaction descriptions**: production of pathogenic Aβ-peptides in ; binding to APP and their possible rol; cleavage of APP; Cleavage of the APP-CTF by γ-secretase

---

#### PMC2702093 (score: 3)
**Title**: Neuroinflammation and Oxidation/Nitration of α-Synuclein Linked to Dopaminergic Neurodegeneration

**Pathways**: ab_clearance, neuroinflammation, oxidative_stress

---

#### PMC2726961 (score: 3)
**Title**: Transmission and spreading of tauopathy in transgenic mouse brain

**Pathways**: ab_clearance, tau_pathology, oxidative_stress

**Reaction descriptions**: aggregation of tau can be transmitted

---

#### PMC2730994 (score: 3)
**Title**: A gamma-secretase inhibitor decreases amyloid-beta production in the central nervous system

**Pathways**: ab_clearance, oxidative_stress

**Quantitative values**: 0.200 ng/mL; 250 ng/mL; 0.500 ng/mL; 500 ng/mL

**Reaction descriptions**: production of new Aβ was calculated as t; clearance of proteins that accumulate i; production of Aβ in the human CNS; clearance of targeted proteins in the c

---

#### PMC2740839 (score: 3)
**Title**: Mitochondrial Cholesterol Loading Exacerbates Amyloid Beta Peptide-Induced Inflammation and Neurotoxicity

**Pathways**: ab_clearance, synaptic_function, oxidative_stress

**Quantitative values**: 2 mM; 2 mM; 0.5 mM; 210 mM; 60 mM

**Reaction descriptions**: transport of cytosol GSH into mitochond; transport of GSH; clearance of neurotoxic amyloid β pepti

---

#### PMC2743894 (score: 3)
**Title**: Rapid microglial response around amyloid pathology following systemic anti-Aβ antibody administration in PDAPP mice

**Pathways**: ab_aggregation, ab_clearance, tau_pathology, neuroinflammation, oxidative_stress

**Quantitative values**: 20mM; 10mM

**Reaction descriptions**: binding to aggregated Aβ; Aggregation of amyloid-β ; production of pro-inflammatory cytokines; production of a monoclonal antibody acco

---

#### PMC2748841 (score: 3)
**Title**: Cellular Prion Protein Mediates Impairment of Synaptic Plasticity by Amyloid-β Oligomers

**Pathways**: ab_clearance, synaptic_function, oxidative_stress

**Quantitative values**: 100 nM; 100 nM; 0.4 nM; 2000 nM; 92 nM

**Reaction descriptions**: Binding to neurons is saturable; binding to PrP C -expressing cells wi; binding to nAChRα7 ; binding to neurons become robust 

---

#### PMC2750039 (score: 3)
**Title**: Cortical Hubs Revealed by Intrinsic Functional Connectivity: Mapping, Assessment of Stability, and Relation to Alzheimer’s Disease

**Pathways**: ab_clearance, oxidative_stress

---

#### PMC2756291 (score: 3)
**Title**: Characterizing the appearance and growth of amyloid plaques in APP/PS1 mice

**Pathways**: ab_aggregation, ab_clearance, oxidative_stress, calcium

**Reaction descriptions**: cleavage of the amyloid precursor prot; Aggregation of Aβ into compact amyloid pl

---

#### PMC2759694 (score: 3)
**Title**: Interaction of Reelin with APP promotes neurite outgrowth

**Pathways**: amyloid_processing, ab_clearance, oxidative_stress

**Quantitative values**: 12 mM; 1 mM; 50mM; 500mM

**Reaction descriptions**: phosphorylation of the cytoplasmic adaptor pr

---

#### PMC2763626 (score: 3)
**Title**: Synaptic activity reduces intraneuronal Aβ, promotes APP transport to synapses and protects against Aβ-related synaptic alterations

**Pathways**: ab_clearance, synaptic_function, oxidative_stress

**Quantitative values**: 35 mM; 250 nM; 35 mM; 140 mM; 1.3 mM

**Reaction descriptions**: transport of the amyloid precursor prot; binding of glycine to its receptors i; aggregation of Aβ both intracellularly an; phosphorylation of proteins involved in synap

---

#### PMC2763631 (score: 3)
**Title**: Decreased CSF Aβ42 correlates with brain atrophy in cognitively normal elderly

**Pathways**: ab_clearance, tau_pathology, oxidative_stress

---

#### PMC2768399 (score: 3)
**Title**: Neuropeptide Y Fragments Derived from Neprilysin Processing are Neuroprotective in a Transgenic Model of Alzheimer’s Disease

**Pathways**: ab_aggregation, ab_clearance, oxidative_stress

**Quantitative values**: 50 mM

**Reaction descriptions**: cleavage of DAGNPG

---

#### PMC2768429 (score: 3)
**Title**: The Co-chaperone BAG2 Sweeps PHF Insoluble Tau from the Microtubule

**Pathways**: ab_clearance, tau_pathology

**Quantitative values**: 150 mM; 50 mM; 10 mM; 0.5 mM

**Reaction descriptions**: aggregation by CHIP up-regulation ; degradation of the chaperone clients in t; degradation of the glucocorticoid hormone

---

#### PMC2782445 (score: 3)
**Title**: Cognitive decline in Alzheimer’s disease is associated with selective changes in calcineurin/NFAT signaling

**Pathways**: ab_clearance, neuroinflammation, oxidative_stress, calcium

**Quantitative values**: 25 mM; 25 mM; 5 mM; 0.05 mM; 1 mM

---

### Tier 2: Some Quantitative Content (15 papers, score 1-2)

- **PMC1959381**: In Vitro and In Vivo Neurotoxicity of Prion Protein Oligomers -- reactions: degradation of the tandem levels out
- **PMC2573460**: Tauopathy with Paired Helical Filaments in an Aged Chimpanzee -- reactions: aggregation of hyperphosphorylated; aggregation of abnormally phosphorylated 
- **PMC2680286**: Aβ Oligomers Induce Neuronal Cell Cycle Events in Alzheimer’s Disease
- **PMC2688812**: Suppression of amyloid deposition leads to long term reductions in Alzheimer’s pathologies in Tg2576 -- values: 20mM; 137 mM -- reactions: clearance of the others due to reduced ; aggregation of secreted Aß in the extrace
- **PMC2702854**: Soluble oligomers of amyloid β-protein facilitate hippocampal long-term depression by disrupting neu -- values: 2 mM; 0.1 mM
- **PMC2705291**: INCREASED MEMBRANE CHOLESTEROL MIGHT RENDER MATURE HIPPOCAMPAL NEURONS MORE SUSCEPTIBLE TO BETA-AMYL -- values: 0.1 mM; 0.12 mM -- reactions: cleavage by calpain; cleavage of tau into the 17 kDa fragme
- **PMC2718788**: Preclinical Evidence of Alzheimer Changes: Convergent Cerebrospinal Fluid Biomarker and Fluorodeoxyg -- reactions: aggregation of hyperphosphorylated tau pr
- **PMC2040216**: Prognostic Value of Posteromedial Cortex Deactivation in Mild Cognitive Impairment
- **PMC2121110**: The foxa2 Gene Controls the Birth and Spontaneous Degeneration of Dopamine Neurons in Old Age
- **PMC2172865**: Mitochondrial targeting and a novel transmembrane arrest of Alzheimer's amyloid precursor protein im -- values: 100 nM
- **PMC2289542**: Alzheimer-like paired helical filaments and antiparallel dimers formed from microtubule-associated p
- **PMC2678874**: Specific loss of brain ABCA1 increases brain cholesterol uptake and influences neuronal structure an -- values: 10 mM -- reactions: transport from glia to ApoE and ApoA-I an; transport of intracellular cholesterol 
- **PMC2682361**: Phase II safety trial targeting amyloid beta production with a gamma-secretase inhibitor in Alzheime -- reactions: cleavage by these compounds
- **PMC2688404**: Folate Deficiency Induces In Vitro and Mouse Brain Region-Specific Downregulation of Leucine Carboxy -- values: 20 nM
- **PMC2778845**: CD14 and Toll-like receptors 2 and 4 are required for fibrillar Aβ-stimulated microglial activation -- reactions: clearance of Aβ results in a persistent; binding to fAβ was performed as previ

### Tier 3: Mechanistic Descriptions Only (21 papers, score 0 but with reaction descriptions)

- **PMC1832188**: Lack of α-synuclein increases amyloid plaque accumulation in a transgenic mouse model of Alzheimer's -- aggregation of Aβ42  in vitro  and might ; aggregation of Aβ plaques and its absence
- **PMC1976335**: Structural Reorganisation and Potential Toxicity of Oligomeric Species Formed during the Assembly of -- aggregation of both Aβ 16; aggregation of polypeptide chains by expe
- **PMC2014744**: A novel p38α MAPK inhibitor suppresses brain proinflammatory cytokine up-regulation and attenuates s -- production by glia is mainly via cell cu; production by activated glia has been im
- **PMC2043051**: Systematic In Vivo Analysis of the Intrinsic Determinants of Amyloid β Pathogenicity -- aggregation of proteins in vivo
- **PMC2064547**: Deletion of tumor necrosis factor death receptor inhibits amyloid β generation and prevents learning -- binding to fibril proteins enriched i; degradation of specific target proteins
- **PMC2118680**: Fibrin deposition accelerates neurovascular damage and neuroinflammation in mouse models of Alzheime -- clearance of fibrin by the tPA
- **PMC2172520**: MARK/PAR1 kinase is a regulator of microtubule-dependent transport in axons -- phosphorylation of tau by kinases of the MARK; phosphorylation of MAPs at their KXGS motifs
- **PMC2173473**: Tau blocks traffic of organelles, neurofilaments, and APP vesicles in neurons and enhances oxidative -- production of toxic Aβ peptides ; transport of peroxisomes
- **PMC2173840**: Presenilin-1 affects trafficking and processing of βAPP and is targeted in a complex with nicastrin  -- transport of PSs to the cell surface ; production of the highly amyloidogenic 4
- **PMC2214725**: Expression profiling in APP23 mouse brain: inhibition of Aβ amyloidosis and inflammation in response -- transport of vitamin D sterols; clearance of Aβ 
- **PMC2358976**: Reducing AD-Like Pathology in 3xTg-AD Mouse Model by DNA Epitope Vaccine — A Novel Immunotherapeutic -- production of high titers of anti-Aβ ant
- **PMC2390852**: A Drosophila Model of ALS: Human ALS-Associated Mutation in VAP33A Suggests a Dominant Negative Mech -- aggregation of VAP P58S  and recruitment 
- **PMC2396156**: A luteinizing hormone receptor intronic variant is significantly associated with decreased risk of A -- binding of LH ; transport of cholesterol into neurons 
- **PMC2444024**: Age-Specific Epigenetic Drift in Late-Onset Alzheimer's Disease -- cleavage of single-stranded nucleic ac
- **PMC2570425**: Proteomic Profiling of γ-Secretase Substrates and Mapping of Substrate Requirements -- binding of a truncated type I protein; cleavage by a class of proteases dubbe
- **PMC2654279**: SRF and myocardin regulate LRP-mediated amyloid-β clearance in brain vascular cells -- clearance by AD VSMCs ; clearance of Aβ from VSMCs
- **PMC2667382**: Phosphorylation of the Translation Initiation Factor eIF2α Increases BACE1 Levels and Promotes Amylo -- phosphorylation by transfection with constitu; Phosphorylation of the Translation Initiation
- **PMC2669751**: The Cleavage Products of Amyloid-β Precursor Protein Are Sorted to Distinct Carrier Vesicles that Ar -- transport from the point of view of its p; transport to the cell periphery
- **PMC2683786**: α–Synuclein is part of a diverse and highly conserved interaction network that includes PARK9 and ma -- production of reactive oxygen species 
- **PMC2700400**: Synaptic activity prompts γ-secretase–mediated cleavage of EphA4 and dendritic spine formation -- cleavage of EphA4 and dendritic spine ; cleavage of amyloid-precursor protein
- **PMC2728497**: A Recessive Mutation in the APP Gene with Dominant-Negative Effect on Amyloidogenesis -- cleavage of the APP by β- and γ-secret; production of soluble forms of APP 

### Not Prioritized (26 papers)

These papers are primarily observational, clinical, epidemiological, or review-focused without directly extractable mechanistic data for ODE modeling.

- **PMC1955446**: Simvastatin is associated with a reduced incidence of dementia and Parkinson's disease
- **PMC2082649**: Cholinesterase Inhibitors in Mild Cognitive Impairment: A Systematic Review of Randomised Trials
- **PMC2235867**: Presenilins are required for maintenance of neural stem cells in the developing brain
- **PMC2375946**: Communicating the Results of Clinical Research to Participants: Attitudes, Practices, and Future Directions
- **PMC2409978**: A Drastic Reduction in the Life Span of Cystatin C L68Q Carriers Due to Life-Style Changes during the Last Two Centuries
- **PMC2486295**: Protein Aggregation and Protein Instability Govern Familial Amyotrophic Lateral Sclerosis Patient Survival
- **PMC2577829**: Amyloid-β Dynamics Correlate with Neurological Status in the Injured Human Brain
- **PMC2605177**: Cerebral Amyloid Angiopathy and Parenchymal Amyloid Deposition in Transgenic Mice Expressing the Danish Mutant Form of H
- **PMC2636844**: Frequent Amyloid Deposition Without Significant Cognitive Impairment Among the Elderly
- **PMC2638813**: The Cortical Signature of Alzheimer's Disease: Regionally Specific Cortical Thinning Relates to Symptom Severity in Very
- **PMC2649726**: How redesigning AD clinical trials might increase study partners’ willingness to participate
- **PMC2650711**: Distinct Stages of Myelination Regulated by γ-Secretase and Astrocytes in a Rapidly Myelinating CNS Coculture System
- **PMC2661568**: Hippocampal and Cognitive Aging across the Lifespan: A Bioenergetic Shift Precedes and Increased Cholesterol Trafficking
- **PMC2669898**: Global variation in copy number in the human genome
- **PMC2691647**: Neurodegenerative diseases target large-scale human brain networks
- **PMC2696350**: Cerebrospinal Fluid Biomarker Signature in Alzheimer’s Disease Neuroimaging Initiative Subjects
- **PMC2713369**: The effect of acetyl-L-Carnitine and Lipoic acid treatment in ApoE4 mouse as a model of human Alzheimer’s disease
- **PMC2736784**: Within-person across-neuropsychological test variability and incident dementia
- **PMC2737680**: Neuropathology of Nondemented Aging: Presumptive Evidence for Preclinical Alzheimer Disease
- **PMC2738994**: Amyloid deposition is associated with impaired default network function in older persons without dementia
- **PMC2742897**: Cholinesterase Inhibitors and Hospitalization for Bradycardia: A Population-Based Study
- **PMC2759394**: Cerebrospinal fluid biomarkers and rate of cognitive decline in very mild dementia of the Alzheimer's type
- **PMC2760256**: Age-dependent impairment of cognitive and synaptic function in the htau mouse model of tau pathology
- **PMC2761951**: Ten-year change in plasma amyloid β levels and late-life cognitive decline
- **PMC2764344**: Gain in Brain Immunity in the Oldest-Old Differentiates Cognitively Normal from Demented Individuals
- **PMC2778270**: Disclosure of APOE Genotype for Risk of Alzheimer's Disease

---

## 2. Key Pathways

Pathways identified across all 86 papers, ranked by coverage. Pathway assignment uses strict pattern matching for specific mechanistic terms (not just keyword mentions).

| Pathway | Papers | Coverage | Priority for Antimony Modeling |
|---------|--------|----------|-------------------------------|
| Ab Clearance | 86 | 100% | CRITICAL -- enzymatic degradation, BBB transport, phagocytosis |
| Oxidative Stress | 77 | 89% | MEDIUM -- ROS production, mitochondrial dysfunction |
| Amyloid Processing | 21 | 24% | CRITICAL -- core amyloidogenic pathway, secretase kinetics |
| Tau Pathology | 21 | 24% | HIGH -- phosphorylation/dephosphorylation kinetics, tangle formation |
| Synaptic Function | 15 | 17% | HIGH -- functional readout, correlates with cognition |
| Ab Aggregation | 14 | 16% | CRITICAL -- monomer-oligomer-fibril-plaque cascade |
| Lipid Apoe | 13 | 15% | MEDIUM -- ApoE isoform effects on clearance and aggregation |
| Calcium | 7 | 8% | MEDIUM -- calcium dysregulation, downstream effector |
| Neuroinflammation | 7 | 8% | HIGH -- microglial activation, cytokine dynamics |

**Note**: `ab_clearance` and `oxidative_stress` appear in nearly all papers because these are broadly defined categories. The more specific pathway categories (amyloid_processing, ab_aggregation, tau_pathology) are more informative for module building.

---

## 3. Extractable Reactions and Rate Laws

Based on the mechanistic content identified across Tier 1 and Tier 2 papers, the following reaction types can be encoded as Antimony ODE equations. Rate law types follow the Elbert convention (MA, RMA, BDF, UDF, custom).

### Amyloid Precursor Protein Processing

| Reaction ID | Reaction | Rate Law | Parameters | Supporting Papers |
|------------|----------|----------|------------|-------------------|
| `APP_synthesis` | `-> APP_Neuron` | zero-order | k_APP_syn | PMC2693334, PMC2673049 |
| `APP_cleavage_alpha` | `APP_Neuron -> sAPPalpha_BrainISF + CTFalpha_Neuron` | MA or Michaelis-Menten | Vmax_alpha, Km_alpha | PMC2442205, PMC2693334, PMC2570425 |
| `APP_cleavage_beta` | `APP_Neuron -> sAPPbeta_BrainISF + CTFbeta_Neuron` | Michaelis-Menten | Vmax_BACE, Km_BACE | PMC2667382, PMC2693334, PMC2728497 |
| `gamma_cleavage_40` | `CTFbeta_Neuron -> AB40_BrainISF + AICD_Neuron` | MA | k_gamma40 | PMC2442205, PMC2730994, PMC2682361 |
| `gamma_cleavage_42` | `CTFbeta_Neuron -> AB42_BrainISF + AICD_Neuron` | MA | k_gamma42 | PMC2174559, PMC2442205, PMC2730994 |
| `APP_degradation` | `APP_Neuron ->` | first-order | k_APP_deg | general |

### Abeta Aggregation Cascade

| Reaction ID | Reaction | Rate Law | Parameters | Supporting Papers |
|------------|----------|----------|------------|-------------------|
| `AB_oligomerization` | `n * AB42_BrainISF -> AB_oligomer_BrainISF` | nucleation-polymerization | k_nuc, k_elong, n_crit | PMC1976335, PMC1959381, PMC2756291 |
| `AB_fibrillization` | `AB_oligomer_BrainISF -> AB_fibril_BrainISF` | elongation kinetics | k_fib_elong | PMC1976335, PMC2043051, PMC2756291 |
| `AB_plaque_deposit` | `AB_fibril_BrainISF -> AB_plaque_Plaque` | first-order | k_deposit | PMC1832188, PMC2756291, PMC2688812 |
| `AB_oligomer_dissoc` | `AB_oligomer_BrainISF -> n * AB42_BrainISF` | first-order | k_dissoc | PMC1976335 |

### Abeta Clearance

| Reaction ID | Reaction | Rate Law | Parameters | Supporting Papers |
|------------|----------|----------|------------|-------------------|
| `AB_neprilysin_deg` | `AB42_BrainISF ->` | Michaelis-Menten | Vmax_NEP, Km_NEP | PMC1952204, PMC2768399 |
| `AB_IDE_deg` | `AB42_BrainISF ->` | Michaelis-Menten | Vmax_IDE, Km_IDE | PMC1952204 |
| `AB_microglial_phago` | `AB42_BrainISF ->` | saturable uptake | Vmax_phago, Km_phago | PMC2597474, PMC2743894, PMC2778845 |
| `AB_BBB_efflux_LRP1` | `AB42_BrainISF -> AB42_Plasma` | UDF or Michaelis-Menten | Vmax_LRP1, Km_LRP1 | PMC2654279, PMC2740839 |
| `AB_BBB_influx_RAGE` | `AB42_Plasma -> AB42_BrainISF` | UDF or Michaelis-Menten | Vmax_RAGE, Km_RAGE | general |
| `AB_ISF_to_CSF` | `AB42_BrainISF -> AB42_CSF` | BDF (bulk flow) | k_ISF_CSF | PMC2577829, PMC2763631 |
| `AB_CSF_absorption` | `AB42_CSF ->` | first-order | k_CSF_abs | PMC2730994 |
| `AB_perivasc_clear` | `AB42_BrainISF ->` | first-order | k_perivasc | PMC2654279 |

### Tau Phosphorylation and Aggregation

| Reaction ID | Reaction | Rate Law | Parameters | Supporting Papers |
|------------|----------|----------|------------|-------------------|
| `tau_synthesis` | `-> tau_Neuron` | zero-order | k_tau_syn | general |
| `tau_phos_GSK3` | `tau_Neuron -> ptau_Neuron` | Michaelis-Menten | Vmax_GSK3, Km_GSK3 | PMC2172520, PMC2573460, PMC2760256 |
| `tau_phos_CDK5` | `tau_Neuron -> ptau_Neuron` | Michaelis-Menten | Vmax_CDK5, Km_CDK5 | PMC2705291 |
| `tau_dephos_PP2A` | `ptau_Neuron -> tau_Neuron` | Michaelis-Menten | Vmax_PP2A, Km_PP2A | PMC2688404 |
| `ptau_aggregation` | `ptau_Neuron -> tau_oligomer_Neuron` | nucleation-dependent | k_tau_agg | PMC2573460, PMC2726961 |
| `NFT_formation` | `tau_oligomer_Neuron -> NFT_Neuron` | first-order | k_NFT | PMC2573460, PMC2768429 |
| `tau_release` | `tau_Neuron -> tau_BrainISF` | first-order | k_tau_rel | PMC2726961 |
| `tau_ISF_to_CSF` | `tau_BrainISF -> tau_CSF` | BDF | k_tau_CSF | PMC2696350, PMC2763631 |

### Neuroinflammation

| Reaction ID | Reaction | Rate Law | Parameters | Supporting Papers |
|------------|----------|----------|------------|-------------------|
| `microglia_activation` | `microglia_resting -> microglia_active` | Hill function of AB_oligomer | k_act, Kd_act, n_Hill | PMC2597474, PMC2743894, PMC2778845 |
| `microglia_deactivation` | `microglia_active -> microglia_resting` | first-order | k_deact | PMC2743894 |
| `cytokine_production` | `-> IL1beta_BrainISF` | proportional to active microglia | k_cyt_prod | PMC2014744, PMC2743894, PMC2782445 |
| `cytokine_decay` | `IL1beta_BrainISF ->` | first-order | k_cyt_decay | general |
| `complement_AB_binding` | `C1q + AB_plaque -> C1q_AB_complex` | MA | k_C1q_on, k_C1q_off | PMC2118680 |

### Synaptic Dysfunction

| Reaction ID | Reaction | Rate Law | Parameters | Supporting Papers |
|------------|----------|----------|------------|-------------------|
| `synapse_loss_oligomer` | `synapse_density ->` | proportional to AB_oligomer | k_syn_loss | PMC2748841, PMC2702854, PMC2763626 |
| `synapse_loss_inflam` | `synapse_density ->` | proportional to cytokines | k_syn_inflam | PMC2014744, PMC2782445 |
| `synapse_repair` | `-> synapse_density` | logistic growth | k_syn_repair, syn_max | general |
| `LTP_inhibition` | assignment rule | Hill inhibition by AB_oligomer | IC50_LTP, n_LTP | PMC2748841, PMC2702854 |

### ApoE / Lipid Metabolism

| Reaction ID | Reaction | Rate Law | Parameters | Supporting Papers |
|------------|----------|----------|------------|-------------------|
| `ApoE_production` | `-> ApoE_BrainISF` | zero-order (genotype-dependent) | k_ApoE_prod | PMC2678874, PMC2214725 |
| `ApoE_AB_binding` | `ApoE_BrainISF + AB42_BrainISF -> ApoE_AB_BrainISF` | RMA | k_on_ApoE, k_off_ApoE | PMC2214725, PMC2636844 |
| `ApoE_AB_clearance` | `ApoE_AB_BrainISF ->` | receptor-mediated | k_ApoE_clear | PMC2654279 |
| `cholesterol_transport` | `cholesterol_Astrocyte -> cholesterol_Neuron` | ABCA1-mediated | k_chol_trans | PMC2678874, PMC2705291 |

---

## 4. Species and Compartments

### Compartments

Following the Elbert naming convention (`Species_Compartment`):

| Compartment ID | Description | Approx Volume | Key Processes |
|---------------|-------------|---------------|---------------|
| `Neuron` | Neuronal intracellular | ~0.5 pL/neuron | APP processing, tau dynamics, mitochondrial function |
| `Endosome` | Endosomal/lysosomal | subset of Neuron | BACE1 activity (low pH), autophagy |
| `BrainISF` | Brain interstitial fluid | ~250 mL | Extracellular Abeta, ApoE, cytokines |
| `BrainParenchyma` | Brain tissue | ~1400 mL | Plaques, tangles, cell bodies |
| `CSF` | Cerebrospinal fluid | ~150 mL | Biomarker sampling (AB42, tau, ptau) |
| `Plasma` | Blood plasma | ~3000 mL | Peripheral Abeta pool, drug distribution |
| `BBB` | Blood-brain barrier | membrane | LRP1 efflux, RAGE influx, P-gp transport |
| `Microglia` | Microglial intracellular | cellular | Phagocytosis, NLRP3 inflammasome |
| `Astrocyte` | Astrocyte intracellular | cellular | ApoE/cholesterol secretion, glutamate uptake |
| `Plaque` | Amyloid deposits | variable | Insoluble Abeta reservoir, complement binding |

### Species

| Species ID | Description | Compartment |
|-----------|-------------|-------------|
| `APP_Neuron` | Amyloid precursor protein | Neuron |
| `sAPPalpha_BrainISF` | Soluble APP-alpha (neuroprotective) | BrainISF |
| `sAPPbeta_BrainISF` | Soluble APP-beta | BrainISF |
| `CTFalpha_Neuron` | C-terminal fragment alpha (C83) | Neuron |
| `CTFbeta_Neuron` | C-terminal fragment beta (C99) | Neuron |
| `AICD_Neuron` | APP intracellular domain | Neuron |
| `AB40_BrainISF` | Amyloid-beta 1-40 monomer | BrainISF |
| `AB42_BrainISF` | Amyloid-beta 1-42 monomer | BrainISF |
| `AB_oligomer_BrainISF` | Abeta oligomers (neurotoxic) | BrainISF |
| `AB_fibril_BrainISF` | Abeta fibrils | BrainISF |
| `AB_plaque_Plaque` | Amyloid plaques (insoluble) | Plaque |
| `AB42_CSF` | Abeta-42 in CSF (biomarker) | CSF |
| `AB40_CSF` | Abeta-40 in CSF | CSF |
| `AB42_Plasma` | Abeta-42 in plasma | Plasma |
| `tau_Neuron` | Unphosphorylated tau | Neuron |
| `ptau_Neuron` | Phosphorylated tau | Neuron |
| `tau_oligomer_Neuron` | Tau oligomers | Neuron |
| `NFT_Neuron` | Neurofibrillary tangles | Neuron |
| `tau_BrainISF` | Extracellular tau (released) | BrainISF |
| `tau_CSF` | Total tau in CSF (biomarker) | CSF |
| `ptau_CSF` | Phospho-tau in CSF (biomarker) | CSF |
| `ApoE_BrainISF` | Apolipoprotein E | BrainISF |
| `ApoE_AB_BrainISF` | ApoE-Abeta complex | BrainISF |
| `BACE1_Endosome` | Beta-secretase 1 | Endosome |
| `neprilysin_BrainISF` | Neprilysin (Abeta protease) | BrainISF |
| `IDE_BrainISF` | Insulin-degrading enzyme | BrainISF |
| `GSK3beta_Neuron` | GSK-3 beta kinase | Neuron |
| `PP2A_Neuron` | Protein phosphatase 2A | Neuron |
| `microglia_resting_Brain` | Resting microglia | BrainParenchyma |
| `microglia_active_Brain` | Activated microglia | BrainParenchyma |
| `IL1beta_BrainISF` | Interleukin-1 beta | BrainISF |
| `TNFalpha_BrainISF` | TNF-alpha | BrainISF |
| `synapse_density_Neuron` | Synaptic density (functional) | Neuron |
| `LRP1_BBB` | LRP1 (Abeta efflux receptor) | BBB |
| `RAGE_BBB` | RAGE (Abeta influx receptor) | BBB |
| `cholesterol_Neuron` | Neuronal cholesterol | Neuron |
| `PrPc_Neuron` | Cellular prion protein | Neuron |

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total papers analyzed | 86 |
| Tier 1 (best quantitative, score >= 3) | 24 |
| Tier 2 (some quantitative, score 1-2) | 15 |
| Tier 3 (mechanistic descriptions, score 0) | 21 |
| Not prioritized | 26 |
| Papers with numerical values (nM/mM/ng/mL) | 24 |
| Papers with mathematical models | 0 |
| Distinct pathways covered | 9 |
| Extractable reaction templates | 42 |
| Species identified | 37 |
| Compartments identified | 10 |

## Observations

1. **No computational modeling papers in this batch**: None of the 86 papers contain explicit ODE models, SBML files, or mathematical model descriptions. These are primarily experimental biology papers from Alzforum's primary literature collection.
2. **Most quantitative data is experimental concentrations**: The numerical values found (nM, mM, ng/mL) are primarily buffer/assay concentrations and biomarker measurements, not kinetic rate constants. However, binding affinity data (Kd values) and concentration-response relationships can be extracted from Tier 1 papers.
3. **Rich mechanistic content**: Despite limited kinetic parameters, the papers provide extensive mechanistic descriptions of reactions (cleavage, aggregation, transport, clearance) that define the topology of ODE models.
4. **ab_clearance is ubiquitous**: 100% of papers match the ab_clearance pathway pattern, reflecting the centrality of Abeta metabolism to AD research. More specific pathway categories are more informative for module building.
5. **Key papers for deep reading**: PMC2578820 (calcium/Abeta plaques), PMC2442205 (presenilin/SERCA/Abeta), PMC2730994 (gamma-secretase inhibitor PK), PMC2748841 (PrPc/Abeta oligomer binding), and PMC2654279 (LRP-mediated clearance) should be prioritized for parameter extraction.

## Next Steps

1. **Deep-read Tier 1 papers** to extract exact parameter values (Kd, Km, Vmax, rate constants, half-lives)
2. **Cross-reference with Elbert_Esguerra reference model** (`../Elbert_Esguerra_model_v2026b/`) for naming consistency and existing parameter values
3. **Build module YAML specs** for each pathway using the `build-module` skill
4. **Parameterize modules** using extracted values with the `parameterize` skill, citing PMIDs
5. **Assemble and validate** with `just qc` pipeline (schema -> assemble -> antimony parse -> tellurium simulate)
6. **Process batch 2+ papers** to find computational modeling papers with explicit kinetic parameters