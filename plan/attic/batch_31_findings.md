# Batch 31 Paper Analysis: Alzheimer's ODE Modeling Extraction

## Summary Statistics
- Total papers analyzed: 86
- Papers with quantitative/mechanistic data: 14
- Papers with extractable rate laws: 8

---

## Papers with Quantitative/Mechanistic Data

### PMC5016232 - Imaging and cerebrospinal fluid biomarkers in early preclinical Alzheimer disease
- **PMID**: 27398953
- **Key Finding**: Robust negative correlation (r=-0.879) between CSF Abeta42 and PiB binding in early preclinical AD. CSF Abeta42 levels decrease as brain amyloid deposition increases, quantifying the sink effect of plaque sequestration.
- **Pathway**: Amyloid processing / Abeta clearance and deposition
- **Extractable Reactions**:
  - AB42_CSF depletion proportional to plaque burden -> linear/first-order relationship
  - AB42_BrainISF -> AB42_Plaque (sequestration): rate correlates with PiB SUVR
  - Correlation parameter: r = -0.879 (CSF Abeta42 vs cortical PiB binding in converters)
- **Compartments**: CSF, BrainParenchyma
- **Confidence**: measured
- **Notes**: Provides quantitative relationship between soluble and deposited Abeta but not kinetic rate constants per se. Useful for constraining transfer rates in ISF-CSF Abeta model.

### PMC5085902 - Loss of Endothelial Nitric Oxide Synthase Promotes p25 Generation and Tau Phosphorylation
- **PMID**: 27601478
- **Key Finding**: eNOS knockout increases p25/p35 ratio and Cdk5 activity, leading to increased tau phosphorylation in APP/PS1 mice. Quantitative ratios of p25/p35 measured across genotypes.
- **Pathway**: Tau phosphorylation / Nitric oxide signaling
- **Extractable Reactions**:
  - p35_BrainParenchyma -> p25_BrainParenchyma (calpain-mediated cleavage, enhanced by loss of NO): UDF
  - Cdk5_p25 + Tau_BrainParenchyma -> pTau_BrainParenchyma (phosphorylation by Cdk5-p25 complex): MA or MM kinetics
  - eNOS -> NO_BrainParenchyma (production): MA
  - NO inhibition of p35->p25 conversion (inhibitory modulation)
- **Compartments**: BrainParenchyma, Endothelium
- **Confidence**: measured (mouse model, n=4-14 per group, P<0.05 to P<0.001)
- **Notes**: Significant because it links vascular dysfunction to tau pathology mechanistically. Cdk5 activity increase was significant (P<0.001). No absolute rate constants provided, but fold-changes available.

### PMC5094372 - Complement and Microglia Mediate Early Synapse Loss in Alzheimer Mouse Models
- **PMID**: 27033548
- **Key Finding**: C1q-C3-CR3 complement cascade mediates early synapse elimination by microglia in AD. Soluble Abeta oligomers activate complement-dependent synaptic pruning. C1q increased before plaque deposition.
- **Pathway**: Neuroinflammation / Complement-mediated synapse loss
- **Extractable Reactions**:
  - AB42o_BrainISF + Synapse_BrainParenchyma -> C1q_Synapse (C1q tagging of synapses by soluble Abeta oligomers): MA
  - C1q_Synapse -> C3b_Synapse (complement cascade activation): MA
  - Microglia_BrainParenchyma + C3b_Synapse -> SynapseEliminated (CR3-dependent phagocytosis): MM or MA
  - Inhibition of C1q/C3/CR3 reduces synapse loss (potential drug targets)
- **Compartments**: BrainISF, BrainParenchyma
- **Confidence**: measured (mouse models, multiple quantitative readouts)
- **Notes**: Critical pathway linking Abeta to synapse loss. Quantitative measures of synapse loss with/without complement inhibition are provided. No kinetic constants but mechanistic pathway is well-defined.

### PMC5119496 - Generation and deposition of Abeta43 by the virtually inactive presenilin-1 L435F mutant
- **PMID**: 26988102
- **Key Finding**: PS1 L435F mutant generates primarily Abeta43 instead of Abeta40/42. Abeta43 is highly amyloidogenic and deposits in plaques. Demonstrates gamma-secretase processivity determines Abeta species ratios.
- **Pathway**: Amyloid processing / Gamma-secretase processivity
- **Extractable Reactions**:
  - APP_CTF -> AB43_BrainISF (gamma-secretase cleavage, impaired processivity): MM kinetics
  - AB43_BrainISF -> AB43_Plaque (aggregation/deposition, faster than AB42): MA or nucleation-dependent
  - Gamma-secretase processivity: AB49->AB46->AB43 (truncated) vs AB49->AB46->AB43->AB40 (normal)
- **Compartments**: BrainParenchyma, BrainISF
- **Confidence**: measured (cell-based and patient brain tissue)
- **Notes**: Important for modeling the gamma-secretase product line. Adds AB43 as a species to track alongside AB40 and AB42.

### PMC5137165 - Soluble Amyloid-beta Aggregates from Human Alzheimer's Disease Brains
- **PMID**: 27917876
- **Key Finding**: Novel extraction method for soluble Abeta aggregates. Clusters of 10-20nm ovoid structures with 2-3 amino-terminal binding sites. Purified >6000 fold. Demonstrates distinct structural features of native soluble aggregates.
- **Pathway**: Amyloid aggregation
- **Extractable Reactions**:
  - AB42_BrainISF -> AB42o_BrainISF (oligomerization): nucleation-dependent polymerization
  - Physical characterization: ~10-20nm diameter clusters
  - Less than 40% loss during extraction suggests stability of oligomeric species
- **Compartments**: BrainISF, BrainParenchyma
- **Confidence**: measured (human brain tissue)
- **Notes**: Structural characterization rather than kinetic data. Useful for defining oligomer species in the model but does not provide rate constants directly.

### PMC5310835 - ApoE2, ApoE3 and ApoE4 Differentially Stimulate APP Transcription and Abeta Secretion
- **PMID**: 28111074
- **Key Finding**: ApoE isoforms stimulate neuronal Abeta production with potency ApoE4>ApoE3>ApoE2 via DLK->MKK7->ERK1/2->cFos->AP-1 pathway that enhances APP transcription. Novel signal transduction cascade.
- **Pathway**: Amyloid processing / ApoE signaling / APP transcription regulation
- **Extractable Reactions**:
  - ApoE4_BrainISF + ApoEReceptor_Neuron -> DLK_active (receptor activation): MA
  - DLK_active -> MKK7_active -> ERK12_active (MAP kinase cascade): MA cascade
  - ERK12_active + cFos -> pcFos (phosphorylation): MM
  - pcFos -> AP1_active -> APP_mRNA (transcriptional upregulation): Hill function
  - APP_mRNA -> APP_Neuron (translation): MA
  - APP_Neuron -> AB_BrainISF (secretase processing): MM
  - Potency rank: ApoE4 > ApoE3 > ApoE2 (quantitative differences in Abeta production)
- **Compartments**: BrainISF, Neuron (intracellular)
- **Confidence**: measured (human ES-derived neurons, mouse in vivo)
- **Notes**: Highly relevant for modeling ApoE4 risk mechanism. Provides a complete signaling cascade from ApoE to Abeta production. Quantitative fold-changes between ApoE isoforms available.

### PMC5233555 - Structural Variation in Amyloid-beta Fibrils from Alzheimer's Disease Clinical Subtypes
- **PMID**: 28052060
- **Key Finding**: Abeta fibril structures vary between AD clinical subtypes (typical AD vs rapidly progressive AD vs posterior cortical atrophy). Structural polymorphism of fibrils is disease-subtype specific.
- **Pathway**: Amyloid aggregation / Fibril polymorphism
- **Extractable Reactions**:
  - AB42_BrainISF -> AB42_fibril_typeA or AB42_fibril_typeB (polymorphic fibril formation)
  - Different fibril structures may have different seeding/propagation rates
- **Compartments**: BrainParenchyma
- **Confidence**: measured (human brain, ssNMR/EM)
- **Notes**: Suggests that different fibril polymorphs should be considered as distinct species in models. No kinetic data provided.

### PMC5237256 - The release and trans-synaptic transmission of Tau via exosomes
- **PMID**: 28086931
- **Key Finding**: Tau is released trans-synaptically via exosomes. Provides mechanism for prion-like tau spreading between connected brain regions.
- **Pathway**: Tau propagation / Exosomal transport
- **Extractable Reactions**:
  - Tau_Neuron -> Tau_Exosome (exosome packaging): MA
  - Tau_Exosome -> Tau_Synapse (trans-synaptic release): UDF
  - Tau_Synapse -> Tau_Neuron2 (uptake by connected neuron): MA
  - This represents a spreading/propagation mechanism
- **Compartments**: Neuron (presynaptic), Synapse, Neuron (postsynaptic)
- **Confidence**: measured (cell culture systems)
- **Notes**: Key for spatial propagation models. Rate of exosome-mediated tau transfer could be parameterized from this data.

### PMC5263237 - Coupled Proliferation and Apoptosis Maintain the Rapid Turnover of Microglia in the Adult Brain
- **PMID**: 28076784
- **Key Finding**: Microglia have rapid turnover in adult brain with coupled proliferation and apoptosis maintaining steady-state population. Important for modeling microglial dynamics in neuroinflammation.
- **Pathway**: Neuroinflammation / Microglial population dynamics
- **Extractable Reactions**:
  - Microglia_BrainParenchyma -> 2*Microglia_BrainParenchyma (proliferation): MA with rate k_prolif
  - Microglia_BrainParenchyma -> (apoptosis): MA with rate k_apoptosis
  - At steady state: k_prolif = k_apoptosis
  - Turnover rate quantifiable from the study
- **Compartments**: BrainParenchyma
- **Confidence**: measured (mouse brain, in vivo imaging)
- **Notes**: Critical for parameterizing microglial population dynamics in neuroinflammation module.

### PMC5298942 - Locus coeruleus volume and cell population changes during Alzheimer's disease progression
- **PMID**: 27513978
- **Key Finding**: Stereological quantification of locus coeruleus (LC) neuronal loss during AD progression. LC volume and cell counts decrease with Braak stage. Quantitative cell counts provided.
- **Pathway**: Neurodegeneration / Noradrenergic system decline
- **Extractable Reactions**:
  - LC_Neuron -> LC_NeuronDead (neurodegeneration): first-order with rate dependent on Braak stage
  - NE_production rate decreases proportionally with LC neuron loss
  - NE_Brain modulates neuroinflammation and Abeta clearance
- **Compartments**: LocusCoeruleus, BrainParenchyma
- **Confidence**: measured (human postmortem, stereological counts)
- **Notes**: Provides quantitative data on neuronal loss trajectory. Important for modeling noradrenergic contributions to AD.

### PMC5218895 - The DIAN-TU Next Generation Alzheimer's prevention trial: adaptive design and disease progression model
- **PMID**: 27583651
- **Key Finding**: Disease progression model for autosomal dominant AD with quantitative biomarker trajectories. Models CSF biomarker changes, brain volume loss, and cognitive decline as function of estimated years to symptom onset.
- **Pathway**: Disease progression modeling (multi-pathway)
- **Extractable Reactions**:
  - Provides temporal ordering and quantitative trajectories for:
    - CSF AB42 decline (earliest, ~25 years before onset)
    - Amyloid PET increase (~15-20 years before)
    - CSF tau increase (~15 years before)
    - Brain volume decrease (~10 years before)
    - Cognitive decline (~5 years before)
  - Sigmoid/logistic progression curves for each biomarker
- **Compartments**: CSF, BrainParenchyma, Plasma
- **Confidence**: measured (DIAN cohort, longitudinal)
- **Notes**: Excellent source for calibrating overall disease progression dynamics. Provides temporal framework for when different pathological processes become dominant.

### PMC5173282 - Autophagy flux in CA1 neurons of Alzheimer hippocampus
- **PMID**: 27813694
- **Key Finding**: Comprehensive evaluation of autophagy in CA1 neurons across AD stages. Autophagosome formation and lysosomal biogenesis are upregulated but flux is impeded due to lysosomal substrate clearance failure.
- **Pathway**: Autophagy-lysosomal pathway
- **Extractable Reactions**:
  - Autophagosome_formation: upregulated in early AD (gene expression quantified)
  - Autophagosome + Lysosome -> Autolysosome (fusion, not impaired): MA
  - Autolysosome -> degradation_products (substrate clearance, impaired in AD): MM with reduced Vmax
  - Lysosome_biogenesis: upregulated (TFE3-dependent)
  - Net effect: accumulation of undigested material in lysosomes
- **Compartments**: Neuron (intracellular: cytoplasm, lysosomes)
- **Confidence**: measured (human postmortem hippocampus, microarray + protein)
- **Notes**: Provides gene expression fold-changes for autophagy components across AD stages. Could parameterize autophagy module.

### PMC5389415 - Atomic Resolution Structure of Monomorphic Abeta42 Amyloid Fibrils
- **PMID**: 27355699
- **Key Finding**: Atomic resolution structure (PDB: 5KK3) of Abeta42 fibrils. Dimer of Abeta42 molecules, four beta-strands, S-shaped fold, parallel in-register. Salt bridge caps hydrophobic cores. M35-L17/Q15 interface contacts.
- **Pathway**: Amyloid aggregation / Fibril structure
- **Extractable Reactions**:
  - 2*AB42_monomer -> AB42_dimer (dimerization at fibril interface): kon/koff
  - AB42_dimer + AB42_fibril -> AB42_fibril_extended (elongation): MA
  - Structural details inform binding surface for secondary nucleation modeling
- **Compartments**: BrainISF, BrainParenchyma
- **Confidence**: measured (solid-state NMR, >500 distance constraints)
- **Notes**: Structure is critical reference for modeling Abeta aggregation kinetics. Does not provide rate constants directly, but structural parameters could inform binding models.

### PMC5389999 - Hyperphosphorylated tau causes reduced hippocampal CA1 excitability by relocating the axon initial segment
- **PMID**: 28091722
- **Key Finding**: Hyperphosphorylated tau relocates the axon initial segment (AIS), depolarizing action potential threshold and reducing neuronal firing. Rescued by tau suppression and microtubule stabilization.
- **Pathway**: Tau phosphorylation / Neuronal excitability / Synaptic dysfunction
- **Extractable Reactions**:
  - pTau_Neuron -> AIS_relocation (microtubule-dependent): threshold function
  - AIS_relocation -> reduced_excitability (AP threshold shift): linear relationship
  - Microtubule_stabilizer -> prevents AIS_relocation (pharmacological rescue)
  - Tau_phosphorylation level determines degree of AIS displacement
- **Compartments**: Neuron (axon initial segment, soma)
- **Confidence**: measured (mouse models, electrophysiology)
- **Notes**: Provides functional link from pTau to neuronal dysfunction. Quantitative electrophysiology data available. Important for synaptic dysfunction module.

---

## Key Pathways Summary

| Pathway | Paper Count | Key PMCIDs |
|---------|------------|------------|
| Amyloid processing / Abeta production | 4 | PMC5119496, PMC5310835, PMC5016232, PMC5137165 |
| Amyloid aggregation / Fibril structure | 3 | PMC5233555, PMC5389415, PMC5137165 |
| Tau phosphorylation / Tau pathology | 3 | PMC5085902, PMC5389999, PMC5237256 |
| Neuroinflammation / Complement / Microglia | 3 | PMC5094372, PMC5263237, PMC5298942 |
| Autophagy-lysosomal pathway | 1 | PMC5173282 |
| ApoE signaling | 1 | PMC5310835 |
| Disease progression modeling | 1 | PMC5218895 |
| Tau propagation | 1 | PMC5237256 |
| Synaptic dysfunction | 2 | PMC5094372, PMC5389999 |

---

## Extractable Reactions Catalog

### Amyloid Processing Module
1. **ApoE-driven APP transcription**: ApoE + ApoEReceptor -> DLK -> MKK7 -> ERK1/2 -> cFos -> AP-1 -> APP_mRNA (PMC5310835, MA/MM cascade)
2. **Gamma-secretase processivity**: APP_CTF -> AB49 -> AB46 -> AB43/AB42/AB40 (PMC5119496, MM kinetics)
3. **Abeta CSF-brain equilibrium**: AB42_BrainISF <-> AB42_CSF with plaque-dependent sink (PMC5016232, first-order)

### Amyloid Aggregation Module
4. **Abeta oligomerization**: AB42_BrainISF -> AB42o_BrainISF (PMC5137165, nucleation-dependent)
5. **Abeta fibrillization**: AB42_dimer -> AB42_fibril (PMC5389415, elongation kinetics)
6. **Abeta43 deposition**: AB43_BrainISF -> AB43_Plaque (PMC5119496, faster than AB42)

### Tau Phosphorylation Module
7. **Cdk5-p25 tau phosphorylation**: p35 -> p25 (calpain) then Cdk5-p25 + Tau -> pTau (PMC5085902, MA/MM)
8. **eNOS/NO modulation**: eNOS -> NO -> inhibits p35->p25 (PMC5085902, inhibitory MA)
9. **pTau-induced AIS relocation**: pTau -> AIS_relocation -> reduced excitability (PMC5389999, threshold)

### Tau Propagation Module
10. **Exosomal tau spreading**: Tau_Neuron -> Tau_Exosome -> Tau_Synapse -> Tau_Neuron2 (PMC5237256, UDF)

### Neuroinflammation Module
11. **Complement-mediated synapse loss**: AB42o -> C1q_tagging -> C3b -> CR3-dependent phagocytosis (PMC5094372, MA cascade)
12. **Microglial population dynamics**: proliferation/apoptosis balance (PMC5263237, coupled MA)

### Autophagy-Lysosomal Module
13. **Autophagosome formation**: upregulated in AD (PMC5173282, first-order)
14. **Lysosomal clearance**: impaired substrate degradation (PMC5173282, MM with reduced Vmax)

### Neurodegeneration Module
15. **LC neuron loss**: LC_Neuron -> death, rate increases with Braak stage (PMC5298942, first-order)

---

## Species and Compartments

### Species Identified
| Species | Description | Source Papers |
|---------|-------------|---------------|
| AB40_BrainISF | Amyloid-beta 40 in brain ISF | PMC5119496 |
| AB42_BrainISF | Amyloid-beta 42 in brain ISF | PMC5016232, PMC5137165 |
| AB43_BrainISF | Amyloid-beta 43 in brain ISF | PMC5119496 |
| AB42o_BrainISF | Abeta42 oligomers in brain ISF | PMC5094372, PMC5137165 |
| AB42_CSF | Amyloid-beta 42 in CSF | PMC5016232 |
| AB42_Plaque | Deposited Abeta42 (plaques) | PMC5016232, PMC5119496 |
| AB43_Plaque | Deposited Abeta43 (plaques) | PMC5119496 |
| AB42_fibril | Abeta42 fibrils | PMC5389415 |
| APP_Neuron | Amyloid precursor protein | PMC5310835 |
| APP_mRNA | APP transcript | PMC5310835 |
| APP_CTF | APP C-terminal fragment | PMC5119496 |
| ApoE4_BrainISF | Apolipoprotein E4 | PMC5310835 |
| ApoE3_BrainISF | Apolipoprotein E3 | PMC5310835 |
| ApoE2_BrainISF | Apolipoprotein E2 | PMC5310835 |
| ApoEReceptor_Neuron | ApoE receptor on neurons | PMC5310835 |
| DLK_active | Active dual leucine zipper kinase | PMC5310835 |
| MKK7_active | Active MKK7 | PMC5310835 |
| ERK12_active | Active ERK1/2 | PMC5310835 |
| cFos_Neuron | cFos transcription factor | PMC5310835 |
| pcFos_Neuron | Phosphorylated cFos | PMC5310835 |
| Tau_BrainParenchyma | Unphosphorylated tau | PMC5085902, PMC5389999 |
| pTau_BrainParenchyma | Phosphorylated tau | PMC5085902, PMC5389999 |
| p35_BrainParenchyma | p35 (Cdk5 activator) | PMC5085902 |
| p25_BrainParenchyma | p25 (truncated Cdk5 activator) | PMC5085902 |
| Cdk5_BrainParenchyma | Cyclin-dependent kinase 5 | PMC5085902 |
| eNOS_Endothelium | Endothelial nitric oxide synthase | PMC5085902 |
| NO_BrainParenchyma | Nitric oxide | PMC5085902 |
| Tau_Exosome | Tau in exosomes | PMC5237256 |
| C1q_BrainParenchyma | Complement C1q | PMC5094372 |
| C3b_Synapse | Complement C3b at synapse | PMC5094372 |
| CR3_Microglia | Complement receptor 3 | PMC5094372 |
| Microglia_BrainParenchyma | Microglia | PMC5094372, PMC5263237 |
| Synapse_BrainParenchyma | Synapses | PMC5094372, PMC5389999 |
| Autophagosome_Neuron | Autophagosomes | PMC5173282 |
| Lysosome_Neuron | Lysosomes | PMC5173282 |
| Autolysosome_Neuron | Autolysosomes | PMC5173282 |
| LC_Neuron | Locus coeruleus neurons | PMC5298942 |
| NE_Brain | Norepinephrine in brain | PMC5298942 |

### Compartments Identified
| Compartment | Description | Source Papers |
|-------------|-------------|---------------|
| BrainISF | Brain interstitial fluid | PMC5016232, PMC5137165, PMC5310835, PMC5094372 |
| BrainParenchyma | Brain tissue / parenchyma | PMC5085902, PMC5094372, PMC5263237, PMC5298942 |
| CSF | Cerebrospinal fluid | PMC5016232 |
| Neuron | Neuronal intracellular | PMC5310835, PMC5173282, PMC5237256, PMC5389999 |
| Endothelium | Vascular endothelium | PMC5085902 |
| Synapse | Synaptic space | PMC5094372, PMC5237256 |
| LocusCoeruleus | Locus coeruleus | PMC5298942 |
| Lysosome | Lysosomal lumen | PMC5173282 |

---

## Papers Without Quantitative Data

| PMC ID | Title | Reason |
|--------|-------|--------|
| PMC5014597 | ALS mutations disrupt phase separation mediated by alpha-helical structure in TDP-43 | ALS/TDP-43 structural study; no AD-relevant kinetics |
| PMC5018207 | Analysis of protein-coding genetic variation in 60,706 humans | Population genetics reference; no mechanistic AD data |
| PMC5021368 | Self-Organizing 3D Human Neural Tissue Derived from iPSCs Recapitulate AD Phenotypes | Qualitative organoid model; no kinetic parameters |
| PMC5034296 | Solid-State NMR Structure of a Pathogenic Fibril of Full-Length Human alpha-Synuclein | Alpha-synuclein (PD) structure; not directly AD-relevant |
| PMC5036102 | Evaluation of a Genetic Risk Score to Improve Risk Prediction for AD | Genetic epidemiology; no molecular mechanisms |
| PMC5038589 | Neuronal subtypes and diversity revealed by single-nucleus RNA sequencing | Transcriptomics method; no mechanistic data |
| PMC5040069 | Increased 4R-tau induces pathological changes in a human-tau mouse model | Qualitative tau pathology description; no rate constants |
| PMC5047041 | Serum neurofilament light chain protein is a measure of disease intensity in FTD | FTD biomarker study; serum NfL concentrations but no ODE-modelable mechanisms |
| PMC5048391 | Alpha-synuclein RT-QuIC in the CSF of patients with synucleinopathies | Diagnostic assay for synucleinopathies; not AD kinetics |
| PMC5049617 | Identification of key amino acids responsible for distinct aggregation properties of MAP2 and tau | Structural biology of tau vs MAP2; qualitative aggregation differences |
| PMC5058336 | Human whole genome genotype and transcriptome data for AD and other neurodegenerative diseases | Dataset description; no mechanistic data |
| PMC5073117 | Risk factor SORL1: from genetic association to functional validation in AD | Review of SORLA/SORL1; qualitative pathway description |
| PMC5074873 | What we know about TMEM106B in neurodegeneration | Review of TMEM106B; no quantitative kinetics |
| PMC5075285 | Genetic Adaptation and Neandertal Admixture Shaped the Immune System | Evolutionary immunology; not AD-specific |
| PMC5076566 | Toxic PR poly-dipeptides encoded by C9orf72 repeat expansion target LC domain polymers | C9orf72/ALS mechanism; not directly AD-relevant |
| PMC5079111 | C9orf72 dipeptide repeats impair membrane-less organelles | C9orf72/ALS-FTD; not directly AD modeling relevant |
| PMC5083142 | Gene Expression Elucidates Functional Impact of Polygenic Risk for Schizophrenia | Schizophrenia study; not AD-relevant |
| PMC5088659 | Integrative network analysis of nineteen brain regions in AD | Transcriptomics network analysis; qualitative pathway identification |
| PMC5089525 | Plasma tau in Alzheimer disease | Biomarker study; weak correlations (no strong quantitative mechanism) |
| PMC5097044 | ApoE4 causes age-dependent disruption of slow gamma oscillations | Electrophysiology/network oscillations; no molecular rate constants |
| PMC5098187 | Serum neurofilament light protein predicts clinical outcome in TBI | TBI biomarker; not AD-specific kinetics |
| PMC5101156 | Efficient derivation of microglia-like cells from human pluripotent stem cells | Cell differentiation protocol; no AD kinetic data |
| PMC5102064 | A mesoscale connectome of the mouse brain | Neuroanatomy atlas; no AD mechanisms |
| PMC5110027 | Unique pathological tau conformers from AD brains transmit tau pathology | Tau propagation in WT mice; qualitative demonstration (brief report) |
| PMC5111366 | Poly(GR) in C9ORF72-Related ALS/FTD Compromises Mitochondrial Function | C9orf72/ALS; mitochondrial dysfunction mechanism |
| PMC5112157 | Disorders of lysosomal acidification and v-ATPase | Review of v-ATPase; qualitative pathway description |
| PMC5112579 | A step-by-step workflow for low-level analysis of single-cell RNA-seq | Bioinformatics methods; no AD data |
| PMC5112585 | Senescent intimal foam cells are deleterious at all stages of atherosclerosis | Atherosclerosis; not AD-relevant |
| PMC5119954 | Genetic Drivers of Epigenetic and Transcriptional Variation in Human Immune Cells | Immunogenomics; not AD-specific |
| PMC5120370 | sTREM2 cerebrospinal fluid levels as potential biomarker for microglia activity | Biomarker study; sTREM2 levels but no kinetic modeling data |
| PMC5120541 | C9orf72 is required for proper macrophage and microglial function in mice | C9orf72 loss-of-function; qualitative immune phenotype |
| PMC5123296 | variancePartition: interpreting drivers of variation in gene expression | Statistical methods tool; no AD mechanisms |
| PMC5123850 | Protein-RNA networks regulated by normal and ALS-associated mutant HNRNPA2B1 | ALS RNA-binding protein networks; not AD-relevant |
| PMC5127391 | Functional recovery in new mouse models of ALS/FTLD after clearance of TDP-43 | TDP-43 proteinopathy; ALS/FTLD model, not AD kinetics |
| PMC5138863 | C9ORF72 poly(GA) aggregates sequester HR23 and nucleocytoplasmic transport proteins | C9orf72 poly-GA toxicity; ALS/FTD mechanism |
| PMC5149108 | Phase separation by low complexity domains promotes stress granule assembly | Stress granule biology; no AD-specific quantitative data |
| PMC5157836 | Next-generation genotype imputation service and methods | Computational genetics tool; no AD data |
| PMC5172605 | Ageing, neurodegeneration and brain rejuvenation | Review article on aging; qualitative overview |
| PMC5173322 | Neurodegenerative disease mutations in TREM2 reveal functional surface | TREM2 structural biology; qualitative functional characterization |
| PMC5177487 | Incidence and Impact of Subclinical Epileptiform Activity in AD | Clinical electrophysiology; no molecular kinetics |
| PMC5182069 | RNA splicing is a primary link between genetic variation and disease | Genomics review; not AD-specific |
| PMC5210310 | Inflammatory pre-conditioning restricts seeded induction of alpha-synuclein pathology | Alpha-synuclein/PD; not directly AD-relevant |
| PMC5210579 | Expansion of the Gene Ontology knowledgebase and resources | Bioinformatics resource; not AD data |
| PMC5210595 | PANTHER version 11: expanded annotation data | Bioinformatics tool; no AD data |
| PMC5210637 | The STRING database in 2017 | Bioinformatics tool; no AD data |
| PMC5221728 | Oligodendrocyte heterogeneity in the mouse CNS | Cell type characterization; no AD kinetics |
| PMC5224821 | Genomics implicates adaptive and innate immunity in AD and PD | GWAS/genomics; qualitative pathway identification |
| PMC5237381 | Longitudinal Beta-Amyloid Deposition and Hippocampal Volume in Preclinical AD | Imaging biomarker study; longitudinal rates but no molecular kinetics |
| PMC5237382 | Evaluation of Tau Imaging in Staging AD | PET imaging staging; no molecular kinetics |
| PMC5241818 | Massively parallel digital transcriptional profiling of single cells | scRNA-seq technology (Drop-seq); no AD data |
| PMC5243141 | Astrocyte scar formation aids CNS axon regeneration | Spinal cord injury; not AD-relevant |
| PMC5263238 | Major Shifts in Glial Regional Identity Are a Transcriptional Hallmark of Human Brain Aging | Aging transcriptomics; qualitative glial changes |
| PMC5269514 | A Multi-Network Approach Identifies Protein-specific Co-expression in AD | Proteomics network analysis; qualitative |
| PMC5299056 | AD-associated TREM2 variants exhibit decreased or increased ligand-dependent activation | TREM2 variant functional study; identifies HDL/LDL as ligands but no kinetics |
| PMC5313473 | Measurement of Longitudinal Beta-Amyloid Change with Florbetapir PET | PET imaging methodology; reference region optimization |
| PMC5319193 | Pathologic correlations of AV-1451 imaging in non-Alzheimer tauopathies | Tau PET validation; non-AD tauopathies |
| PMC5325702 | Interaction of tau with RNA-Binding Protein TIA1 Regulates tau Pathophysiology | Tau-TIA1 interaction and stress granules; qualitative mechanism |
| PMC5325836 | Mixed pathologies including CTE in retired football players | Clinical neuropathology; no molecular kinetics |
| PMC5335603 | Astrocyte pathology in human neural stem cell model of FTD | FTD astrocyte study; qualitative pathology description |
| PMC5338864 | Genetic Risk, Adherence to a Healthy Lifestyle, and Coronary Disease | Cardiovascular epidemiology; not AD-relevant |
| PMC5339672 | Soluble TREM2 induces inflammatory responses and enhances microglial survival | sTREM2 function; qualitative (brief report) |
| PMC5340039 | Cell-specific deletion of C1qa identifies microglia as dominant source of C1q | C1q source identification; supports PMC5094372 but no new kinetics |
| PMC5344738 | Defining imaging biomarker cut-points for brain aging and AD | Imaging biomarker thresholds; no molecular kinetics |
| PMC5345650 | The Synucleinopathies: Twenty Years On | Historical review of synucleinopathies; no quantitative data |
| PMC5349617 | Network degeneration and dysfunction in presymptomatic C9ORF72 expansion carriers | Brain imaging in presymptomatic C9orf72; not AD-specific |
| PMC5358512 | TAM receptors regulate multiple features of microglial physiology | Microglial receptor biology; qualitative |
| PMC5360460 | Plasma phospholipids identify antecedent memory impairment | Lipidomic biomarker discovery; no mechanistic kinetics |
| PMC5364369 | Phase Separation of C9orf72 Dipeptide Repeats Perturbs Stress Granule Dynamics | C9orf72 DPR/stress granules; ALS/FTD not AD-specific |
| PMC5366078 | ApoE, ApoE receptors, and the Synapse in Alzheimer's Disease | Review of ApoE at synapse; qualitative overview |
| PMC5382945 | Relationships between flortaucipir PET tau binding and amyloid burden | Tau PET imaging correlations; no molecular kinetics |
| PMC5388176 | A reference panel of 64,976 haplotypes for genotype imputation | Genetics reference panel; no AD data |
| PMC5390006 | Roles of tau protein in health and disease | Comprehensive tau review; qualitative overview |
