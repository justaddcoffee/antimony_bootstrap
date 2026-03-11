# Batch 0 Paper Analysis Findings

**Date**: 2026-02-24
**Total papers analyzed**: 86
**Tier 1 (kinetic models / rich quantitative data, score >= 10)**: 81
**Tier 2 (some kinetic parameters, score 3-9)**: 4
**Tier 3 (qualitative / limited quantitative, score < 3)**: 1

## 1. Papers Containing Quantitative/Mechanistic Data

### Tier 1: High-Value Papers (kinetic models or rich parameter data)

#### PMC10527432
**Title**: Development of an α-synuclein positron emission tomography tracer for imaging synucleinopathies
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, protein_clearance
**Kinetic score**: 53
**Contains mathematical model references**: ODE_model
- Kd_values: KD: 10.97 nM, KD: 109.2 nM, KD: 120.5 nM
- ODE_model: ode, ode, ode, ode, ode
- binding_affinity: binding affinity, binding affinity, binding affinity, binding affinity, binding affinity
- half_life: half-life of F0
- pharmacokinetic: pharmacokinetic, pharmacokinetic
**Key species**: APP, dopamine, ide, presenilin, rage, sting

#### PMC10166855
**Title**: Tau activation of microglial cGAS–IFN reduces MEF2C-mediated cognitive resilience
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 38
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- half_life: half-life of 1
- kinetic_param: kinetic parameter, kinetic parameter
- pharmacokinetic: Pharmacokinetic, pharmacokinetic, pharmacokinetic, pharmacokinetic
**Key species**: Apoe, CGAS, Cgas, GABA, IFN, Ifn, STING, Sting, cGAS, cgas

#### PMC10916992
**Title**: APOE Christchurch‐mimetic therapeutic antibody reduces APOE‐mediated toxicity and tau phosphorylation
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 33
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- binding_affinity: binding affinity, binding affinity, binding affinity, binding affinity, binding affinity
- kinetic_param: Kinetic parameter
**Key species**: APOE, APOE2, APOE3, APOE4, APP, ApoE, ApoE2, ApoE3, ApoE4, Apoe

#### PMC10644954
**Title**: Human Microglial State Dynamics in Alzheimer’s Disease Progression
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, calcium, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 31
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: koff, koff, koff
**Key species**: APOE, IFN, IL1, TNF, TREM2, ide, rage, sting

#### PMC10202812
**Title**: Resilience to autosomal dominant Alzheimer’s disease in a Reelin-COLBOS heterozygous man
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 27
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- binding_affinity: Binding affinity, binding affinity
- kinetic_param: kinetic constant
**Key species**: APOE, APOE3, APOE4, APP, GSK3, ide, presenilin, rage, sting

#### PMC10371027
**Title**: Lysosomal dysfunction in Down syndrome and Alzheimer mouse models is caused by v-ATPase inhibition by Tyr682-phosphorylated APP βCTF
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 27
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- binding_affinity: binding affinity, binding affinity
- pharmacokinetic: pharmacokinetic
**Key species**: APOE4, APP, BACE, BACE1, ide, rage, sting

#### PMC10418207
**Title**: Alzheimer’s disease linked Aβ42 exerts product feedback inhibition on γ-secretase impairing downstream cell signaling
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, protein_clearance
**Kinetic score**: 26
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- degradation_rate: degradation rate
**Key species**: APP, BACE, BACE1, NGF, ide, nicastrin, presenilin, rage, sting

#### PMC10548173
**Title**: Microglia‐synapse engulfment via PtdSer‐TREM2 ameliorates neuronal hyperactivity in Alzheimer's disease models
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, protein_clearance, insulin_signaling
**Kinetic score**: 26
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: kon
**Key species**: APP, TGF, TREM2, Trem2, glutamate, ide, ngF, rage, sting

#### PMC10689245
**Title**: The APOE-R136S mutation protects against APOE4-driven Tau pathology, neurodegeneration and neuroinflammation
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 26
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- binding_affinity: binding affinity, binding affinity
**Key species**: APOE, APOE2, APOE3, APOE4, Apoe, BDNF, GABA, ide, rage, sting

#### PMC1274341
**Title**: Focal glial activation coincides with increased BACE1 activation and precedes amyloid plaque deposition in APP[V717I] transgenic mice
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, protein_clearance
**Kinetic score**: 26
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: kon, kon, kon
**Key species**: APP, BACE, BACE1, IFN, IL-1, IL-6, Il-1, Il-6, TGF, TNF

#### PMC10412454
**Title**: cGAS–STING drives ageing-related inflammation and neurodegeneration
**Pathways**: amyloid, neuroinflammation, synaptic, oxidative_stress, protein_clearance
**Kinetic score**: 25
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- pharmacokinetic: Pharmacokinetic
**Key species**: CGAS, Cgas, IFN, IL-6, STING, Sting, TNF, Tnf, cGAS, ide

#### PMC10957154
**Title**: Increased palmitoylation improves estrogen receptor alpha–dependent hippocampal synaptic deficits in a mouse model of synucleinopathy
**Pathways**: neuroinflammation, synaptic, oxidative_stress, protein_clearance
**Kinetic score**: 25
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- pharmacokinetic: pharmacokinetic
**Key species**: dopamine, ide, rage, sting

#### PMC10287562
**Title**: Tau-targeting antisense oligonucleotide MAPTRx in mild Alzheimer’s disease: a phase 1b, randomized, placebo-controlled trial
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 24
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- pharmacokinetic: pharmacokinetic, pharmacokinetic, pharmacokinetic
**Key species**: APOE4, APP, ide, ngf, sting

#### PMC10517010
**Title**: Acetylation discriminates disease-specific tau deposition
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, protein_clearance
**Kinetic score**: 22
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- binding_affinity: binding affinity
**Key species**: ide, rage, sting

#### PMC10518633
**Title**: Human astrocytes and microglia show augmented ingestion of synapses in Alzheimer’s disease via MFG-E8
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 22
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APOE4, BDNF, TGF, ide, rage, sting

#### PMC10564391
**Title**: Genetic Variants of Phospholipase C-γ2 Alter the Phenotype and Function of Microglia and Confer Differential Risk for Alzheimer’s Disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, calcium, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 22
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: kon, kon
**Key species**: APOE4, APP, Apoe, GABA, IFN, IL-1, TNF, TREM2, glutamate, ide

#### PMC10569712
**Title**: Whole human-brain mapping of single cortical neurons for profiling morphological diversity and stereotypy
**Pathways**: amyloid, neuroinflammation, oxidative_stress
**Kinetic score**: 22
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: kon
- production_rate: production rate
**Key species**: ide, rage, sting

#### PMC10148063
**Title**: Mechanism of STMN2 cryptic splice/polyadenylation and its correction for TDP-43 proteinopathies
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, protein_clearance
**Kinetic score**: 21
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: BDNF, TNF, ide, rage, sting

#### PMC10464935
**Title**: Single-nucleus multi-region transcriptomic analysis of brain vasculature in Alzheimer’s Disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 21
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: koff, koff
**Key species**: APOE, APOE3, APOE4, ApoE, ApoE4, IL-1, IL6, TGF, apoe, ide

#### PMC10467038
**Title**: The neuronal pentraxin Nptx2 regulates complement activity and restrains microglia-mediated synapse loss in neurodegeneration
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 21
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- binding_affinity: binding affinity, binding affinity
**Key species**: ApoE, glutamate, ide, rage, sting

#### PMC10476347
**Title**: Large-scale proximity extension assay reveals CSF midkine and DOPA decarboxylase as supportive diagnostic biomarkers for Parkinson’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, protein_clearance
**Kinetic score**: 21
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, IL-1, IL-6, IL1, IL6, TGF, dopamine, ide, rage, sting

#### PMC10557526
**Title**: Large-scale differentiation of iPSC-derived motor neurons from ALS and control subjects
**Pathways**: neuroinflammation, calcium, oxidative_stress, lipid_metabolism
**Kinetic score**: 21
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, BDNF, IL-6, TNF, ide, ngF, rage, sting

#### PMC10701763
**Title**: Unconventional secretion of misfolded proteins promotes adaptation to proteasome dysfunction in mammalian cells
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress, protein_clearance
**Kinetic score**: 21
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: IL1, ide, sting

#### PMC10192217
**Title**: The in-tissue molecular architecture of β-amyloid pathology in the mammalian brain
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, protein_clearance
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, App, glutamate, ide, presenilin, rage, sting

#### PMC10227043
**Title**: Multi-omic approach characterises the neuroprotective role of retromer in regulating lysosomal health
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, BACE2, ide, rage, sting

#### PMC10244178
**Title**: Early alterations in the MCH system link aberrant neuronal activity and sleep disturbances in a mouse model of Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, insulin_signaling
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: App, Bdnf, GABA, ide, ngF, rage, sting

#### PMC10274680
**Title**: Early Alzheimer’s disease pathology in human cortex is associated with a transient phase of distinct cell states
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: kon
**Key species**: APOE, APP, BACE, BACE2, BDNF, CDK5, IL-1, IL1, TGF, TNF

#### PMC10511632
**Title**: VE-cadherin in arachnoid and pia mater cells serves as a suitable landmark for in vivo imaging of CNS immune surveillance and inflammation
**Pathways**: amyloid, neuroinflammation, vascular, oxidative_stress
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
- kon_koff: kon
**Key species**: ide, nGF, rage, sting

#### PMC10516951
**Title**: Altered ubiquitin signaling induces Alzheimer’s disease-like hallmarks in a three-dimensional human neural cell culture model
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APOE3, APOE4, APP, ApoE, ApoE3, ApoE4, apoE3, apoE4, ide

#### PMC10619638
**Title**: Identification of a protective microglial state mediated by miR-155 and interferon-γ signaling in a mouse model of Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APP, ApoE, ApoE4, Apoe, IFN, IL-6, Ifn, TGF, TREM2

#### PMC10690472
**Title**: APP substrate ectodomain defines amyloid‐β peptide length by restraining γ‐secretase processivity and facilitating product release
**Pathways**: amyloid, neuroinflammation, oxidative_stress
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, BACE, ide, nicastrin, presenilin, rage, sting

#### PMC1288039
**Title**: Functional Amyloid Formation within Mammalian Tissue
**Pathways**: amyloid, neuroinflammation, oxidative_stress
**Kinetic score**: 20
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, rage, sting

#### PMC10447236
**Title**: TDP-43 forms amyloid filaments with a distinct fold in type A FTLD-TDP
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress
**Kinetic score**: 19
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: gaba, ide, ngF, sting

#### PMC10630957
**Title**: Taurine deficiency as a driver of aging
**Pathways**: neuroinflammation, synaptic, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 19
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: IL1, TNF, glutamate, ide, ngf, sting

#### PMC10764278
**Title**: Disease-specific tau filaments assemble via polymorphic intermediates
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress
**Kinetic score**: 19
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, rage, sting

#### PMC10330525
**Title**: Abundant Aβ fibrils in ultracentrifugal supernatants of aqueous extracts from Alzheimer’s disease brains
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, calcium, oxidative_stress
**Kinetic score**: 18
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, TREM2, ide, rage, sting

#### PMC10427416
**Title**: Clinical effects of Lewy body pathology in cognitively impaired individuals
**Pathways**: amyloid, tau, neuroinflammation, vascular, oxidative_stress
**Kinetic score**: 18
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, sting

#### PMC10427420
**Title**: Cognitive effects of Lewy body pathology in clinically unimpaired individuals
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism
**Kinetic score**: 18
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, dopamine, sting

#### PMC10115173
**Title**: Phospho-tau with subthreshold tau-PET predicts increased tau accumulation rates in amyloid-positive individuals
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 17
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APP, ide, rage, sting

#### PMC10154225
**Title**: CSF tau phosphorylation occupancies at T217 and T205 represent improved biomarkers of amyloid and tau pathology in Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism
**Kinetic score**: 17
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, ide, ngf, sting

#### PMC10258627
**Title**: Microglia-mediated T cell Infiltration Drives Neurodegeneration in Tauopathy
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, calcium, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 17
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APOE3, APOE4, APP, ApoE, ApoE3, ApoE4, IFN, IL-1, Il1

#### PMC10284271
**Title**: An in vivo neuroimmune organoid model to study human microglia phenotypes
**Pathways**: amyloid, tau, neuroinflammation, vascular, oxidative_stress, insulin_signaling
**Kinetic score**: 17
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: IL-6, IL1, IL6, TGF, TNF, ide, rage, sting

#### PMC10449561
**Title**: Sleep deprivation exacerbates microglial reactivity and Aβ deposition in a TREM2-dependent manner in mice
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, protein_clearance, insulin_signaling
**Kinetic score**: 17
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, Cd33, IL-1, IL-6, Il6, TGF, TNF, TREM2, ide, presenilin

#### PMC10468133
**Title**: Human cerebrospinal fluid contains diverse lipoprotein subspecies enriched in proteins implicated in central nervous system health
**Pathways**: amyloid, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 17
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, ide, ngf, rage, sting

#### PMC10499811
**Title**: CSF proteome profiling reveals biomarkers to discriminate dementia with Lewy bodies from Alzheimer´s disease
**Pathways**: amyloid, tau, neuroinflammation, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 17
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APOE4, dopamine, ide, rage, sting

#### PMC10027402
**Title**: Divergent transcriptional regulation of astrocyte reactivity across disorders
**Pathways**: amyloid, neuroinflammation, synaptic, calcium, oxidative_stress, lipid_metabolism
**Kinetic score**: 16
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: Apoe4, ide, rage, sting

#### PMC10150695
**Title**: Palmitoylation of the Parkinson’s disease-associated protein synaptotagmin-11 links its turnover to α-synuclein homeostasis†
**Pathways**: tau, neuroinflammation, synaptic, calcium, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 16
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: dopamine, ide, sting

#### PMC10427428
**Title**: Cerebrospinal fluid proteomics define the natural history of autosomal dominant Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, calcium, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 16
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APP, TREM2, glutamate, ide, il6, presenilin, rage, sting

#### PMC10031303
**Title**: Granulin loss of function in human mature brain organoids implicates astrocytes in TDP-43 pathology
**Pathways**: tau, neuroinflammation, synaptic, vascular, oxidative_stress, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, sting

#### PMC10042173
**Title**: Increasing participant diversity in AD research: Plans for digital screening, blood testing, and a community‐engaged approach in the Alzheimer's Disease Neuroimaging Initiative 4
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, ApoE, ide, rage, sting

#### PMC10079561
**Title**: Virus exposure and neurodegenerative disease risk across national biobanks
**Pathways**: neuroinflammation, vascular, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, rage, sting

#### PMC10087054
**Title**: Prediction of Longitudinal Cognitive Decline in Preclinical Alzheimer Disease Using Plasma Biomarkers
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE4, ide, ngf, rage, sting

#### PMC10087669
**Title**: The Alzheimer's Association appropriate use recommendations for blood biomarkers in Alzheimer's disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, ide, rage, sting

#### PMC10154209
**Title**: Biomarker modeling of Alzheimer’s disease using PET-based Braak staging
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, Presenilin, ide, ngf, rage, sting

#### PMC10233457
**Title**: Neuroinflammation After COVID-19 With Persistent Depressive and Cognitive Symptoms
**Pathways**: neuroinflammation, synaptic, vascular, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, sting

#### PMC10243600
**Title**: A genome-wide association study with 1,126,563 individuals identifies new risk loci for Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ODE, ode, ode
**Key species**: APOE, APOE2, CD33, ide, il6, sting

#### PMC10353939
**Title**: Astrocyte reactivity influences amyloid-β effects on tau pathology in preclinical Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, TREM2, ide, sting

#### PMC10425864
**Title**: Increased Medial Temporal Tau Positron Emission Tomography Uptake in the Absence of Amyloid-β Positivity
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, rage, sting

#### PMC10427417
**Title**: CSF MTBR-tau243 is a specific biomarker of tau tangle pathology in Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, ide, rage, sting

#### PMC10431934
**Title**: The chronic neuropsychiatric sequelae of COVID-19: The need for a prospective study of viral impact on brain functioning
**Pathways**: neuroinflammation, synaptic, vascular, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: glutamate, ide, sting

#### PMC10433790
**Title**: Association between CSF biomarkers of Alzheimer’s disease and neuropsychiatric symptoms: Mayo Clinic Study of Aging
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, ide, rage, sting

#### PMC10567546
**Title**: Rare variant associations with plasma protein levels in the UK Biobank
**Pathways**: amyloid, neuroinflammation, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: IL-1, IL-6, TNF, gaba, ide, rage, sting

#### PMC10567551
**Title**: Plasma proteomic associations with genetics and health in the UK Biobank
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: IL-1, IL-6, TNF, app, ide, rage, sting

#### PMC10567571
**Title**: Large-scale plasma proteomics comparisons through genetics and disease associations
**Pathways**: amyloid, neuroinflammation, vascular, oxidative_stress, lipid_metabolism, insulin_signaling
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: IFN, IL-1, IL-6, IL1, TNF, ide, il1, rage, sting

#### PMC10570139
**Title**: DOPA decarboxylase is an emerging biomarker for Parkinsonian disorders including preclinical Lewy body disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: Dopamine, dopamine, ide, sting

#### PMC10570140
**Title**: The VCAM1–ApoE pathway directs microglial chemotaxis and alleviates Alzheimer’s disease pathology
**Pathways**: amyloid, tau, neuroinflammation, vascular, calcium, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APOE4, APP, ApoE, ApoE4, Apoe, CD33, Il1, LRP1, TREM2

#### PMC10572106
**Title**: Single Cell DNA Methylation and 3D Genome Architecture in the Human Brain
**Pathways**: neuroinflammation, synaptic, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, rage, sting

#### PMC10590452
**Title**: Soluble TREM2 ameliorates tau phosphorylation and cognitive deficits through activating transgelin-2 in Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode
**Key species**: GSK3, NLRP3, TREM2, ide, sting

#### PMC10601493
**Title**: Single-cell atlas reveals correlates of high cognitive function, dementia, and resilience to Alzheimer’s disease pathology
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: Apoe, BDNF, IL1, apoe, ide, rage, sting

#### PMC10627170
**Title**: Assessment of heterogeneity among participants in the Parkinson’s Progression Markers Initiative cohort using α-synuclein seed amplification: a cross-sectional study
**Pathways**: amyloid, tau, neuroinflammation, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: dopamine, ide, rage, sting

#### PMC10665113
**Title**: Proteomics analysis of plasma from middle-aged adults identifies protein markers of dementia risk in later life
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, GABA, TREM2, glutamate, ide, rage, sting

#### PMC10680783
**Title**: Gut microbiome composition may be an indicator of preclinical Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, glutamate, ide, rage, sting

#### PMC10681293
**Title**: Alzheimer risk-increasing TREM2 variant causes aberrant cortical synapse density and promotes network hyperexcitability in mouse models
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, App, TNF, TREM2, Trem2, ide, rage, sting

#### PMC10697236
**Title**: Neuronal DNA double-strand breaks lead to genome structural variations and 3D genome disruption in neurodegeneration
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, App, CDK5, Cdk5, ide, rage, sting

#### PMC10782612
**Title**: Epigenomic dissection of Alzheimer’s disease pinpoints causal variants and reveals epigenome erosion
**Pathways**: amyloid, tau, neuroinflammation, synaptic, vascular, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, GSK3, TREM2, ide, rage, sting

#### PMC10803068
**Title**: Proteomics of brain, CSF, and plasma identifies molecular signatures for distinguishing sporadic and genetic Alzheimer’s disease
**Pathways**: amyloid, tau, neuroinflammation, vascular, calcium, oxidative_stress, lipid_metabolism, protein_clearance, insulin_signaling
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, APOE4, APP, IDE, IL-1, IL-6, IL1, TGF, TNF, TREM2

#### PMC10914599
**Title**: Long non-coding RNA SNHG8 drives stress granule formation in tauopathies
**Pathways**: amyloid, tau, neuroinflammation, synaptic, oxidative_stress, lipid_metabolism, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APOE, BDNF, ide, rage, sting

#### PMC11156248
**Title**: Expectations and clinical meaningfulness of randomized controlled trials
**Pathways**: amyloid, tau, vascular, calcium, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, ngf

#### PMC1181540
**Title**: Aging and Gene Expression in the Primate Brain
**Pathways**: amyloid, neuroinflammation, oxidative_stress, insulin_signaling
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, rage, sting

#### PMC1216331
**Title**: Impaired Cross-Modal Inhibition in Alzheimer Disease
**Pathways**: neuroinflammation, synaptic, vascular, oxidative_stress
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: ide, sting

#### PMC1283364
**Title**: Persistent Amyloidosis following Suppression of Aβ Production in a Transgenic Model of Alzheimer Disease
**Pathways**: amyloid, tau, neuroinflammation, synaptic, calcium, oxidative_stress, protein_clearance
**Kinetic score**: 15
**Contains mathematical model references**: ODE_model
- ODE_model: ode, ode, ode, ode, ode
**Key species**: APP, BACE1, TGF, ide, neprilysin, ngF, presenilin, rage, sting

### Tier 2: Moderate-Value Papers (some extractable parameters)

- **PMC10193187** (score=9): Genetic Associations Between Modifiable Risk Factors and Alzheimer Disease
  - Pathways: amyloid, tau, neuroinflammation, synaptic
  - ODE_model: ode, ode, ode

- **PMC10720501** (score=6): The role of cerebrospinal fluid and other biomarker modalities in the Alzheimer’s disease diagnostic
  - Pathways: amyloid, tau, neuroinflammation, vascular
  - ODE_model: ode, ode

- **PMC10228637** (score=3): Multiple Cerebral Hemorrhages in a Patient Receiving Lecanemab and
Treated with t-PA for Stroke
  - Pathways: amyloid, vascular, lipid_metabolism
  - ODE_model: ode

- **PMC10569699** (score=3): Diversity of primate brain cells unraveled
  - Pathways: neuroinflammation
  - ODE_model: ode

### Tier 3: Qualitative Papers (limited direct parameter extraction)

- **PMC10331726**: Sex and gender considerations in dementia: a call for global research
  - Pathways: tau, neuroinflammation, synaptic

## 2. Key Biological Pathways Identified

| Pathway | Paper Count | % of Batch |
|---------|-----------|-----------|
| neuroinflammation | 84 | 97% |
| oxidative_stress | 84 | 97% |
| amyloid | 74 | 86% |
| tau | 66 | 76% |
| synaptic | 58 | 67% |
| lipid_metabolism | 48 | 55% |
| protein_clearance | 45 | 52% |
| vascular | 43 | 50% |
| calcium | 20 | 23% |
| insulin_signaling | 14 | 16% |

## 3. Specific Reactions/Rate Laws Extractable with Parameters

### Amyloid-beta production (APP processing)
- **Description**: APP cleavage by beta/gamma-secretase producing Abeta40/42
- **Rate law type**: Michaelis-Menten or mass action
- **Key parameters needed**: Km for BACE1, kcat for gamma-secretase, Abeta42/40 ratio
- **Source papers**: PMC10527432, PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10418207, PMC10548173, PMC10689245, PMC1274341

### Amyloid-beta aggregation
- **Description**: Monomer -> oligomer -> fibril -> plaque cascade
- **Rate law type**: Nucleation-dependent polymerization or simplified mass action
- **Key parameters needed**: aggregation rate constants, critical concentration, elongation rate
- **Source papers**: PMC10527432, PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10418207, PMC10548173, PMC10689245, PMC1274341

### Amyloid-beta clearance
- **Description**: Enzymatic degradation (NEP, IDE) and transport (LRP1, RAGE, BBB)
- **Rate law type**: Michaelis-Menten (enzymatic) or first-order (transport)
- **Key parameters needed**: Km/Vmax for NEP, Km/Vmax for IDE, BBB transport rates, CSF clearance rate
- **Source papers**: PMC10527432, PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10418207, PMC10548173, PMC10689245, PMC1274341

### Tau phosphorylation/dephosphorylation
- **Description**: Kinase (GSK3b, CDK5) and phosphatase (PP2A) activity on tau
- **Rate law type**: Michaelis-Menten
- **Key parameters needed**: Km/Vmax for GSK3b, Km/Vmax for PP2A, phospho-tau half-life
- **Source papers**: PMC10527432, PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10418207, PMC10548173, PMC10689245, PMC1274341

### Neuroinflammatory cytokine signaling
- **Description**: Microglial activation, cytokine production/clearance
- **Rate law type**: Mass action or Hill function
- **Key parameters needed**: cytokine production rates, cytokine half-lives, microglial activation threshold
- **Source papers**: PMC10527432, PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10418207, PMC10548173, PMC10689245, PMC1274341

### Synaptic transmission/plasticity
- **Description**: Neurotransmitter release, receptor binding, LTP/LTD
- **Rate law type**: Mass action or custom
- **Key parameters needed**: glutamate release rate, receptor binding Kd, synaptic vesicle recycling rate
- **Source papers**: PMC10527432, PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10418207, PMC10548173, PMC10689245, PMC1274341

### ApoE-mediated lipid transport
- **Description**: ApoE isoform effects on Abeta clearance and lipid metabolism
- **Rate law type**: First-order or Michaelis-Menten
- **Key parameters needed**: ApoE-Abeta binding Kd by isoform, ApoE-LRP1 Kd, lipid transport rates
- **Source papers**: PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10689245, PMC10287562, PMC10518633, PMC10564391, PMC10464935

### Protein clearance (autophagy/proteasome/lysosome)
- **Description**: Degradation of misfolded proteins via autophagy, UPS, lysosomes
- **Rate law type**: First-order or Michaelis-Menten
- **Key parameters needed**: autophagy flux rate, proteasome degradation rate, lysosomal pH
- **Source papers**: PMC10527432, PMC10166855, PMC10916992, PMC10644954, PMC10202812, PMC10371027, PMC10418207, PMC10548173, PMC10689245, PMC1274341

## 4. Species and Compartments Mentioned

### Key Species (Antimony naming convention: species_compartment)

**Amyloid pathway**: APP, App, BACE, BACE1, BACE2, Presenilin, app, nicastrin, presenilin

**Tau pathway**: CDK5, Cdk5, GSK3

**Neuroinflammation**: CGAS, Cgas, IFN, IL-1, IL-6, Ifn, Il-1, Il-6, NLRP3, STING, Sting, TGF, TNF, Tgf, Tnf, cGAS, cgas, sting

**Receptors/transporters**: APOE, APOE2, APOE3, APOE4, ApoE, ApoE2, ApoE3, ApoE4, Apoe, Apoe4, CD33, Cd33, LRP1, TREM2, Trem2, apoE, apoE3, apoE4, apoe, rage

**Neurotransmitters**: Dopamine, GABA, dopamine, gaba, glutamate

**Neurotrophins**: BDNF, Bdnf, NGF, nGF, ngF, ngf

**Enzymes**: IDE, ide, neprilysin

### Compartments

- Astrocyte
- BLOOD
- Blood
- CSF
- Cerebral
- Cerebrospinal
- Cortex
- Csf
- Entorhinal
- Extracellular
- Glia
- Glial
- Hippocampus
- Intracellular
- Lysosome
- Microglia
- Neuron
- Neuronal
- Perivascular
- Plasma
- Serum
- Synapse
- astrocyte
- blood
- brain parenchyma
- cerebral
- cerebrospinal
- cortex
- csf
- endosome
- entorhinal
- extracellular
- glia
- glial
- hippocampus
- intracellular
- lysosome
- microglia
- neuron
- neuronal
- perivascular
- plasma
- serum
- synapse

## 5. Summary and Recommendations

### Overall Statistics
- 86 papers in batch 0
- 81 high-value papers with kinetic/model data
- 4 moderate-value papers with some quantitative parameters
- 1 qualitative papers (useful for mechanism identification, not parameter extraction)

### Priority Papers for Deep Parameter Extraction

These papers should be read in full to extract specific parameter values:

1. **PMC10527432** (score=53): Development of an α-synuclein positron emission tomography tracer for imaging synucleinopa
   - Contains: Kd_values, ODE_model, binding_affinity, half_life, pharmacokinetic
2. **PMC10166855** (score=38): Tau activation of microglial cGAS–IFN reduces MEF2C-mediated cognitive resilience
   - Contains: ODE_model, half_life, kinetic_param, pharmacokinetic
3. **PMC10916992** (score=33): APOE Christchurch‐mimetic therapeutic antibody reduces APOE‐mediated toxicity and tau phos
   - Contains: ODE_model, binding_affinity, kinetic_param
4. **PMC10644954** (score=31): Human Microglial State Dynamics in Alzheimer’s Disease Progression
   - Contains: ODE_model, kon_koff
5. **PMC10202812** (score=27): Resilience to autosomal dominant Alzheimer’s disease in a Reelin-COLBOS heterozygous man
   - Contains: ODE_model, binding_affinity, kinetic_param
6. **PMC10371027** (score=27): Lysosomal dysfunction in Down syndrome and Alzheimer mouse models is caused by v-ATPase in
   - Contains: ODE_model, binding_affinity, pharmacokinetic
7. **PMC10418207** (score=26): Alzheimer’s disease linked Aβ42 exerts product feedback inhibition on γ-secretase impairin
   - Contains: ODE_model, degradation_rate
8. **PMC10548173** (score=26): Microglia‐synapse engulfment via PtdSer‐TREM2 ameliorates neuronal hyperactivity in Alzhei
   - Contains: ODE_model, kon_koff
9. **PMC10689245** (score=26): The APOE-R136S mutation protects against APOE4-driven Tau pathology, neurodegeneration and
   - Contains: ODE_model, binding_affinity
10. **PMC1274341** (score=26): Focal glial activation coincides with increased BACE1 activation and precedes amyloid plaq
   - Contains: ODE_model, kon_koff
11. **PMC10412454** (score=25): cGAS–STING drives ageing-related inflammation and neurodegeneration
   - Contains: ODE_model, pharmacokinetic
12. **PMC10957154** (score=25): Increased palmitoylation improves estrogen receptor alpha–dependent hippocampal synaptic d
   - Contains: ODE_model, pharmacokinetic
13. **PMC10287562** (score=24): Tau-targeting antisense oligonucleotide MAPTRx in mild Alzheimer’s disease: a phase 1b, ra
   - Contains: ODE_model, pharmacokinetic
14. **PMC10517010** (score=22): Acetylation discriminates disease-specific tau deposition
   - Contains: ODE_model, binding_affinity
15. **PMC10518633** (score=22): Human astrocytes and microglia show augmented ingestion of synapses in Alzheimer’s disease
   - Contains: ODE_model

### Top Pathways by Coverage

- **neuroinflammation**: 84 papers
- **oxidative_stress**: 84 papers
- **amyloid**: 74 papers
- **tau**: 66 papers
- **synaptic**: 58 papers

### Next Steps

1. Deep-read Tier 1 papers to extract exact parameter values with units
2. Cross-reference with Elbert_Esguerra reference model parameters
3. Build module YAMLs for each reaction category using extracted parameters
4. Prioritize amyloid and tau pathways (most coverage in this batch)
5. For Tier 3 papers, use pathway assignments to inform mechanism graph construction