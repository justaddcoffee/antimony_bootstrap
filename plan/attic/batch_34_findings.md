# Batch 34 Paper Analysis - Alzheimer's ODE Mechanisms

## Summary Statistics
- Total papers analyzed: 86
- Papers with quantitative/mechanistic data (score >= 2): 19
- Papers with some quantitative mentions (score 1): 55
- Papers without quantitative data (score 0): 12

## Papers with Quantitative/Mechanistic Data

### PMC5849233 - Empirical derivation of the reference region for computing diagnostic sensitive 18fluorodeoxyglucose ratios in Alzheimer's disease based on the ADNI sample
- **Pathways**: amyloid_cascade, oxidative_stress, apoptosis, lipid_metabolism
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - rate_constant: k
                    =
                    1
  - concentration: 1mm; 2mm; 1.5mm
  - fold_change: 50-fold
- **Species**: ApoE
- **Compartments**: CSF

### PMC5913225 - Tau Internalization is Regulated by 6-O Sulfation on Heparan Sulfate Proteoglycans (HSPGs)
- **Pathways**: tau, synaptic, oxidative_stress, apoptosis, metal_ions
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - concentration: 0.9 nm; 3 nm; 11 nm
  - fold_change: 10-fold
  - ode_model: mathematical model
- **Species**: Tau
- **Compartments**: CSF, neuron, synapse, extracellular, intracellular
- **Extractable Reactions**:
  - Tau aggregation | MA or nucleated polymerization
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC5918692 - Common schizophrenia alleles are enriched in mutation-intolerant genes and in regions under strong background selection
- **Pathways**: tau, synaptic, oxidative_stress, lipid_metabolism, metal_ions
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - km: km = 0
  - fold_change: 1.23-fold; 2.01-fold; 0.90-fold
- **Species**: ApoE
- **Compartments**: neuron, synapse
- **Extractable Reactions**:
  - Tau aggregation | MA or nucleated polymerization
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC5920320 - Data-driven models of dominantly-inherited Alzheimer’s disease progression
- **Pathways**: amyloid_cascade, tau, synaptic, oxidative_stress, apoptosis, lipid_metabolism
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - fold_change: 10-fold
  - ode_model: differential equation; differential equation; differential equation
- **Species**: APP, gamma_secretase, Tau, pTau, ApoE
- **Compartments**: CSF, neuron
- **Extractable Reactions**:
  - APP cleavage by BACE1 | MM kinetics | BACE1-dependent
  - Tau aggregation | MA or nucleated polymerization
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC5934326 - Genome-wide association analyses identify 44 risk variants and refine the genetic architecture of major depression
- **Pathways**: neuroinflammation, synaptic, oxidative_stress, calcium, metal_ions, epigenetics
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - rate_constant: k=0.15
  - fold_change: 20.9 fold; 1.12-fold; 0.84-fold
- **Species**: glutamate
- **Compartments**: neuron, astrocyte, microglia, synapse
- **Extractable Reactions**:
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC5951394 - Integrative single-cell analysis of transcriptional and epigenetic states in the human adult brain
- **Pathways**: neuroinflammation, synaptic, oxidative_stress, mitochondria, epigenetics
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - rate_constant: k=10; k=10; k=50
  - concentration: 50 μm; 50 μm; 2 mm
  - fold_change: 0.25 fold; 2-fold; 2-fold
- **Species**: glutamate
- **Compartments**: neuron, astrocyte, microglia, mitochondria
- **Extractable Reactions**:
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC6080491 - A multi-omic atlas of the human frontal cortex for aging and Alzheimer’s disease research
- **Pathways**: amyloid_cascade, tau, synaptic, oxidative_stress, apoptosis, lipid_metabolism, epigenetics
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - rate_constant: k=100.
  - concentration: 5mm; 20 mm; 85 mm
- **Species**: Tau, ApoE
- **Compartments**: neuron
- **Extractable Reactions**:
  - Tau aggregation | MA or nucleated polymerization
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC6083837 - Detection of widespread horizontal pleiotropy in causal relationships inferred from Mendelian randomization between complex traits and diseases
- **Pathways**: oxidative_stress, lipid_metabolism
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - rate_constant: k = 1
  - concentration: 21. mm
- **Species**: ApoE
- **Compartments**: plasma

### PMC6085146 - Functional aspects of meningeal lymphatics in aging and Alzheimer’s disease
- **Pathways**: amyloid_cascade, neuroinflammation, synaptic, oxidative_stress, apoptosis, lipid_metabolism, bbb, metal_ions, mitochondria
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - concentration: 25 mm; 25 mm; 2mm
  - ode_model: mathematical model
- **Species**: AB42, gamma_secretase, CDK5
- **Compartments**: plasma, CSF, brain_ISF, neuron, astrocyte, microglia, mitochondria, extracellular, BBB
- **Extractable Reactions**:
  - Abeta aggregation (monomer -> oligomer -> fibril) | nucleation-dependent | concentration-dependent
  - Abeta clearance/degradation | MA | half-life dependent
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC6086934 - Molecular Architecture of the Mouse Nervous System
- **Pathways**: neuroinflammation, synaptic, oxidative_stress, bbb, cholinergic, metal_ions
- **Relevance Score**: 3/5
- **Quantitative Data Found**:
  - rate_constant: k = 150; k = 100; k = 100
  - concentration: 500μm; 100μm; 500 μm
  - fold_change: 1.2-fold
- **Species**: glutamate, GABA, acetylcholine
- **Compartments**: CSF, neuron, astrocyte, synapse, extracellular
- **Extractable Reactions**:
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC5839761 - Humanized TREM2 mice reveal microglia-intrinsic and -extrinsic effects of R47H polymorphism
- **Pathways**: amyloid_cascade, tau, neuroinflammation, synaptic, oxidative_stress, apoptosis, lipid_metabolism
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - concentration: 50 µm; 10 µm; 15 µm
  - kd: binding affinity
- **Species**: APP, gamma_secretase, Tau, TREM2, ApoE, TNFa
- **Compartments**: neuron, astrocyte, microglia, extracellular, intracellular
- **Extractable Reactions**:
  - APP cleavage by BACE1 | MM kinetics | BACE1-dependent
  - Tau aggregation | MA or nucleated polymerization
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - TREM2-mediated phagocytosis | MM kinetics
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC5847621 - Structural basis for the recognition of LDL-receptor family members by VSV glycoprotein
- **Pathways**: oxidative_stress, calcium, autophagy, lipid_metabolism
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - ic50: ic50; ic50
  - concentration: 20 µm; 1 µm; 1.5 µm
- **Compartments**: plasma, endosome, lysosome, extracellular, intracellular
- **Extractable Reactions**:
  - Protein clearance via autophagy | MA | capacity-limited

### PMC5870375 - Amyloid-beta modulates microglial responses by binding to the triggering receptor expressed on myeloid cells 2 (TREM2)
- **Pathways**: amyloid_cascade, tau, neuroinflammation, oxidative_stress, apoptosis, lipid_metabolism, insulin_signaling, metal_ions
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - concentration: 5 mm; 100 μm; 50 mm
  - ki: dissociation constant
  - kd: binding affinity; binding affinity; binding affinity
- **Species**: AB42, Tau, TREM2, ApoE
- **Compartments**: CSF, neuron, astrocyte, microglia, extracellular, intracellular
- **Extractable Reactions**:
  - Abeta aggregation (monomer -> oligomer -> fibril) | nucleation-dependent | concentration-dependent
  - Abeta clearance/degradation | MA | half-life dependent
  - Tau aggregation | MA or nucleated polymerization
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - TREM2-mediated phagocytosis | MM kinetics

### PMC5886064 - Progranulin functions as a cathepsin D chaperone to stimulate axonal outgrowth in vivo
- **Pathways**: neuroinflammation, oxidative_stress, autophagy, apoptosis, metal_ions
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - ic50: ic50
  - concentration: 500 µm; 100 µm; 25 µm
  - fold_change: 3-fold; 12-fold; 5-fold
- **Species**: TNFa
- **Compartments**: CSF, neuron, microglia, lysosome, extracellular
- **Extractable Reactions**:
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - Protein clearance via autophagy | MA | capacity-limited

### PMC5889092 - TREM2 is a receptor for β-amyloid which mediates microglial function
- **Pathways**: amyloid_cascade, tau, neuroinflammation, synaptic, oxidative_stress, autophagy, apoptosis, lipid_metabolism, insulin_signaling
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - concentration: 0.5 nm; 25 ng/ml; 2.2 mm
  - kd: kd = 12.7
  - fold_change: 3-fold; 2.5-fold
- **Species**: APP, gamma_secretase, Tau, GSK3B, TREM2, ApoE, TNFa
- **Compartments**: CSF, neuron, microglia, lysosome, extracellular, intracellular
- **Extractable Reactions**:
  - APP cleavage by BACE1 | MM kinetics | BACE1-dependent
  - Tau phosphorylation by kinase | MM kinetics | kinase-dependent
  - Tau aggregation | MA or nucleated polymerization
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - TREM2-mediated phagocytosis | MM kinetics
  - Neurotransmitter release/reuptake | MA | activity-dependent
  - Protein clearance via autophagy | MA | capacity-limited

### PMC5948105 - ApoE4 accelerates early seeding of amyloid pathology
- **Pathways**: amyloid_cascade, tau, neuroinflammation, synaptic, oxidative_stress, autophagy, apoptosis, lipid_metabolism, bbb
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - half_life: half-life of 1
  - concentration: 3.1 mm; 2.5 mm; 1.2 mm
  - fold_change: 3 fold
- **Species**: AB42, AB40, ApoE, IL1B, TNFa
- **Compartments**: CSF, brain_ISF, neuron, astrocyte, microglia, synapse, lysosome, extracellular, intracellular
- **Extractable Reactions**:
  - Abeta aggregation (monomer -> oligomer -> fibril) | nucleation-dependent | concentration-dependent
  - Abeta clearance/degradation | MA | half-life dependent
  - Tau aggregation | MA or nucleated polymerization
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - Neurotransmitter release/reuptake | MA | activity-dependent
  - Protein clearance via autophagy | MA | capacity-limited

### PMC6007078 - Slingshot: cell lineage and pseudotime inference for single-cell transcriptomics
- **Pathways**: synaptic, oxidative_stress
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - rate_constant: k=5; k=3; k=1
- **Species**: Tau
- **Compartments**: neuron
- **Extractable Reactions**:
  - Neurotransmitter release/reuptake | MA | activity-dependent

### PMC6040832 - Progranulin, lysosomal regulation and neurodegenerative disease
- **Pathways**: amyloid_cascade, neuroinflammation, synaptic, oxidative_stress, autophagy, apoptosis, insulin_signaling, epigenetics
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - half_life: half-life.
  - fold_change: 3.2-fold
- **Species**: Tau, BDNF
- **Compartments**: plasma, CSF, neuron, astrocyte, microglia, endosome, lysosome, extracellular, intracellular
- **Extractable Reactions**:
  - Cytokine production by activated microglia | MA or Hill | stimulus-dependent
  - Neurotransmitter release/reuptake | MA | activity-dependent
  - Protein clearance via autophagy | MA | capacity-limited

### PMC6041266 - An in vitro paradigm to assess potential anti-Aβ antibodies for Alzheimer’s disease
- **Pathways**: amyloid_cascade, tau, synaptic, oxidative_stress
- **Relevance Score**: 2/5
- **Quantitative Data Found**:
  - ic50: ic50; ic50; ic50
  - concentration: 0.2 nm; 300 nm; 1.1 ng/ml
  - kd: kd = 800
  - fold_change: 130-fold; 1000-fold; 4-fold
- **Species**: AB42, APP, Tau, pTau
- **Compartments**: neuron
- **Extractable Reactions**:
  - APP cleavage by BACE1 | MM kinetics | BACE1-dependent
  - Abeta aggregation (monomer -> oligomer -> fibril) | nucleation-dependent | concentration-dependent
  - Abeta clearance/degradation | MA | half-life dependent
  - Tau aggregation | MA or nucleated polymerization
  - Neurotransmitter release/reuptake | MA | activity-dependent

## Key Pathways Summary

| Pathway | Paper Count |
|---------|------------|
| oxidative_stress | 85 |
| synaptic | 67 |
| apoptosis | 60 |
| amyloid_cascade | 58 |
| neuroinflammation | 47 |
| tau | 43 |
| lipid_metabolism | 37 |
| autophagy | 26 |
| metal_ions | 25 |
| epigenetics | 19 |
| bbb | 13 |
| mitochondria | 10 |
| insulin_signaling | 10 |
| calcium | 6 |
| cholinergic | 2 |

## Species Registry

| Species | Paper Count | Suggested Elbert Name |
|---------|------------|----------------------|
| Tau | 46 | Tau_Neuron |
| ApoE | 35 | ApoE_BrainISF |
| APP | 24 | APP_Neuron |
| gamma_secretase | 18 | gSecretase_Neuron |
| AB42 | 15 | AB42_BrainISF |
| TREM2 | 15 | TREM2_Microglia |
| pTau | 14 | pTau_Neuron |
| glutamate | 14 | Glu_Synapse |
| TNFa | 9 | TNFa_BrainISF |
| AB40 | 9 | AB40_BrainISF |
| BDNF | 8 | BDNF_BrainISF |
| GABA | 6 | GABA_Synapse |
| IL1B | 6 | IL1B_BrainISF |
| GSK3B | 5 | GSK3B_Neuron |
| BACE1 | 4 | BACE1_Neuron |
| CDK5 | 2 | CDK5_Neuron |
| acetylcholine | 2 | ACh_Synapse |

## Compartments Registry

| Compartment | Paper Count |
|-------------|------------|
| neuron | 68 |
| astrocyte | 34 |
| microglia | 33 |
| CSF | 29 |
| extracellular | 29 |
| intracellular | 29 |
| plasma | 21 |
| lysosome | 16 |
| synapse | 11 |
| BBB | 11 |
| mitochondria | 10 |
| endosome | 9 |
| brain_ISF | 7 |

## Extractable Reactions Catalog

| Reaction | Rate Type | Source Papers | Pathway |
|----------|-----------|---------------|---------|
| ROS production and antioxidant defense | MA | PMC5913225, PMC6083837, PMC5870375, PMC5847621, PMC5920320 (+14 more) | oxidative_stress |
| Synaptic transmission and plasticity | MA | PMC5948105, PMC6041266, PMC5920320, PMC6085146, PMC5934326 (+9 more) | synaptic |
| ApoE-mediated lipid transport | MA | PMC5948105, PMC5920320, PMC5889092, PMC6085146, PMC5839761 (+6 more) | lipid_metabolism |
| APP processing by secretases | MM | PMC5948105, PMC6041266, PMC5920320, PMC6085146, PMC6040832 (+5 more) | amyloid_cascade |
| Abeta production and clearance | MA/MM | PMC5948105, PMC6041266, PMC5920320, PMC6085146, PMC6040832 (+5 more) | amyloid_cascade |
| Microglial activation and cytokine release | Hill/MA | PMC5948105, PMC6085146, PMC5934326, PMC5951394, PMC6086934 (+5 more) | neuroinflammation |
| Tau phosphorylation/dephosphorylation | MM | PMC5948105, PMC6041266, PMC5920320, PMC5839761, PMC5918692 (+4 more) | tau |
| Protein clearance via autophagy-lysosome | MA/MM | PMC5948105, PMC5847621, PMC5886064, PMC6040832, PMC5889092 | autophagy |
| Insulin/GSK3 signaling cascade | MM | PMC6040832, PMC5889092, PMC5870375 | insulin_signaling |
| Calcium influx/efflux and signaling | MA/Hill | PMC5934326, PMC5847621 | calcium |
| Mitochondrial bioenergetics | MA/MM | PMC5951394, PMC6085146 | mitochondria |

## Papers Without Quantitative Data

- **PMC5831169** - Aging and neurodegeneration are associated with increased mutations in single human neurons | Minimal quantitative data | Pathways: synaptic, oxidative_stress, apoptosis
- **PMC5831225** - Early long-term administration of the CSF1R inhibitor PLX3397 ablates microglia and reduces accumulation of intraneurona | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5837359** - Tau burden and the functional connectome in Alzheimer’s disease and progressive supranuclear palsy | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC5850938** - Cytoplasmic chromatin triggers inflammation in senescence and cancer | Minimal quantitative data | Pathways: tau, neuroinflammation, oxidative_stress
- **PMC5857215** - Structural tract alterations predict down-stream tau accumulation in amyloid positive older individuals | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC5858585** - An environment-dependent transcriptional network specifies human microglia identity | Minimal quantitative data | Pathways: neuroinflammation, synaptic, oxidative_stress
- **PMC5866736** - Evidence for brain glucose dysregulation in Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5881464** - ApoE facilitates the microglial response to amyloid plaque pathology | Minimal quantitative data | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC5886204** - Repetitive element transcripts are elevated in the brain of C9orf72 ALS/FTLD patients | Minimal quantitative data | Pathways: oxidative_stress, autophagy, apoptosis
- **PMC5894933** - Midlife cardiovascular fitness and dementia | Minimal quantitative data | Pathways: synaptic, oxidative_stress, lipid_metabolism
- **PMC5896171** - Extracellular Monomeric and Aggregated Tau Efficiently Enter Human Neurons through Overlapping but Distinct Pathways | Minimal quantitative data | Pathways: tau, neuroinflammation, oxidative_stress
- **PMC5904220** - Evidence of amyloid-β cerebral amyloid angiopathy transmission through neurosurgery | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC5907316** - Potent prion-like behaviors of pathogenic α-synuclein and evaluation of inactivation methods | Minimal quantitative data | Pathways: amyloid_cascade, synaptic, oxidative_stress
- **PMC5909703** - Neuroinflammation in Alzheimer's Disease | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5909931** - GGA1 regulates signal-dependent sorting of BACE1 to recycling endosomes, which moderates Aβ production | Minimal quantitative data | Pathways: amyloid_cascade, synaptic, oxidative_stress
- **PMC5917767** - Longitudinal tau PET in ageing and Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, synaptic, oxidative_stress
- **PMC5919412** - Stabilizing the Retromer Complex in a Human Stem Cell Model of Alzheimer’s Disease Reduces TAU Phosphorylation Independe | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5921896** - Association between midlife vascular risk factors and estimated brain amyloid deposition | Minimal quantitative data | Pathways: amyloid_cascade, oxidative_stress, apoptosis
- **PMC5927822** - Elevated TREM2 Gene Dosage Reprograms Microglia Responsivity and Ameliorates Pathological Phenotypes in Alzheimer’s Dise | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5928393** - Synaptic Tau Seeding Precedes Tau Pathology in Human Alzheimer's Disease Brain | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5928580** - TDP-43 pathology in anterior temporal pole cortex in aging and Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC5929130** - Directly Reprogrammed Human Neurons Retain Aging-Associated Transcriptomic Signatures and Reveal Age-Related Nucleocytop | Minimal quantitative data | Pathways: neuroinflammation, synaptic, oxidative_stress
- **PMC5935138** - Sense-encoded poly-GR dipeptide repeat proteins correlate to neurodegeneration and uniquely co-localize with TDP-43 in d | Minimal quantitative data | Pathways: oxidative_stress, apoptosis
- **PMC5948154** - Gain of toxic Apolipoprotein E4 effects in Human iPSC-Derived Neurons Is Ameliorated by a Small-Molecule Structure Corre | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5957089** - Human Hippocampal Neurogenesis Persists throughout Aging | Minimal quantitative data | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC5959890** - GWAS on family history of Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC5962917** - ABBY | Minimal quantitative data | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC5964045** - Flortaucipir tau PET imaging in semantic variant primary progressive aphasia | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5964634** - Preparation of organotypic brain slice cultures for the study of Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5966834** - Granulocyte Colony Stimulating Factor (G-CSF) Decreases Brain Amyloid Burden and Reverses Cognitive Impairment in Alzhei | Minimal quantitative data | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC5970994** - Cellular Milieu Imparts Distinct Pathological α-Synuclein Strains in α-Synucleinopathies | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5984804** - The Trem2 R47H variant confers loss-of-function-like phenotypes in Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC5985582** - Proteomics analysis identifies new markers associated with capillary cerebral amyloid angiopathy in Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5986066** - Re-evaluating Microglia Expression Profiles Using RiboTag and Cell Isolation Strategies | Minimal quantitative data | Pathways: neuroinflammation, oxidative_stress, lipid_metabolism
- **PMC5989565** - Assessment of the genetic architecture of Alzheimer’s Disease risk in rate of memory decline | Minimal quantitative data | Pathways: amyloid_cascade, tau, oxidative_stress
- **PMC5990464** - Atomic Structures of Segments from TDP-43 LCD and insight into Reversible and Pathogenic Aggregation | Minimal quantitative data | Pathways: amyloid_cascade, synaptic, oxidative_stress
- **PMC5992755** - Genetic variants associated with Alzheimer’s disease confer different cerebral cortex cell-type population structure | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC5995803** - Brain Cell Type Specific Gene Expression and Co-expression Network Architectures | Minimal quantitative data | Pathways: neuroinflammation, synaptic, oxidative_stress
- **PMC6003669** - Combining NGN2 Programming with Developmental Patterning Generates Human Excitatory Neurons with NMDAR-Mediated Synaptic | Minimal quantitative data | Pathways: neuroinflammation, synaptic, oxidative_stress
- **PMC6013502** - IBD risk loci are enriched in multigenic regulatory modules encompassing putative causative genes | Minimal quantitative data | Pathways: neuroinflammation, synaptic, oxidative_stress
- **PMC6015098** - Tau seeding activity begins in the transentorhinal/entorhinal regions and anticipates phospho-tau pathology in Alzheimer | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC6023731** - A combination of ontogeny and CNS environment establishes microglial identity. | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC6023751** - APOE4 causes widespread molecular and cellular alterations associated with Alzheimer’s disease phenotypes in human iPSC- | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC6027763** - Phosphorylation of different tau sites during progression of Alzheimer’s disease | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC6035389** - In Situ Structure of Neuronal C9ORF72 Poly-GA Aggregates Reveals Proteasome Recruitment | Minimal quantitative data | Pathways: amyloid_cascade, synaptic, oxidative_stress
- **PMC6039173** - Inert and seed-competent tau monomers suggest structural origins of aggregation | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC6043775** - Whole‐exome sequencing in 20,197 persons for rare variants in Alzheimer's disease | Minimal quantitative data | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC6051499** - Utilizing the Centiloid scale in cross-sectional and longitudinal PiB PET studies | Minimal quantitative data | Pathways: amyloid_cascade, tau, oxidative_stress
- **PMC6054740** - Poly-GR dipeptide repeat polymers correlate with neurodegeneration and Clinicopathological subtypes in C9ORF72-related b | Minimal quantitative data | Pathways: neuroinflammation, synaptic, oxidative_stress
- **PMC6069705** - RNA binding proteins co-localize with small tau inclusions in tauopathy | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC6075814** - Alzheimer’s Disease-Associated β-Amyloid Is Rapidly Seeded by Herpesviridae to Protect against Brain Infection | Minimal quantitative data | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC6080689** - Fibril structure of amyloid-ß(1-42) by cryo-electron microscopy | Minimal quantitative data | Pathways: amyloid_cascade, oxidative_stress, apoptosis
- **PMC6083872** - Stress granule assembly disrupts nucleocytoplasmic transport | Minimal quantitative data | Pathways: neuroinflammation, synaptic, oxidative_stress
- **PMC6090564** - Epigenetic regulation of brain region-specific microglia clearance activity | Minimal quantitative data | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC6091858** - Tau aggregation influences cognition and hippocampal atrophy in the absence of beta-amyloid: A clinico-imaging-pathologi | Minimal quantitative data | Pathways: amyloid_cascade, tau, synaptic
- **PMC5860371** - Comparison of Sociodemographic and Health-Related Characteristics of UK Biobank Participants With Those of the General P | No quantitative parameters found | Pathways: oxidative_stress
- **PMC5866992** - Lessons Learned from Alzheimer Disease: Clinical Trials with Negative Outcomes | No quantitative parameters found | Pathways: amyloid_cascade, neuroinflammation, synaptic
- **PMC5867896** - Genome-wide Analyses Identify KIF5A as a Novel ALS
Gene | No quantitative parameters found | Pathways: amyloid_cascade, synaptic, oxidative_stress
- **PMC5876097** - Effect of sleep on overnight CSF amyloid-β kinetics | No quantitative parameters found | Pathways: amyloid_cascade, oxidative_stress, apoptosis
- **PMC5896795** - Heritability enrichment of specifically expressed genes identifies disease-relevant tissues and cell types | No quantitative parameters found | Pathways: tau, neuroinflammation, synaptic
- **PMC5942893** - Transcriptome-wide association study of schizophrenia and chromatin activity yields mechanistic disease insights | No quantitative parameters found | Pathways: oxidative_stress, epigenetics
- **PMC5946692** - Updated TDP-43 in Alzheimer’s disease staging scheme | No quantitative parameters found | Pathways: amyloid_cascade, tau, synaptic
- **PMC5958625** - NIA-AA Research Framework: Toward a biological definition of Alzheimer’s disease | No quantitative parameters found | Pathways: amyloid_cascade, tau, synaptic
- **PMC5970949** - Non-Alzheimer’s dementia 1 | No quantitative parameters found | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC6029036** - TMEM106B haplotypes have distinct gene expression patterns in aged brain | No quantitative parameters found | Pathways: amyloid_cascade, tau, neuroinflammation
- **PMC6048952** - APOE4 Causes Widespread Molecular and Cellular Alterations Associated with Alzheimer’s Disease Phenotypes in Human iPSC- | No quantitative parameters found | Pathways: N/A
- **PMC6070131** - Astrocyte-derived Interleukin-33 promotes microglial synapse engulfment and neural circuit development | No quantitative parameters found | Pathways: neuroinflammation, synaptic, oxidative_stress
