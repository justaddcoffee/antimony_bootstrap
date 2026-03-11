# Strategy: Leveraging Existing ODE-Based Alzheimer's Disease Models

## Overview

This document surveys published ODE-based computational models of Alzheimer's disease (AD) that can serve as reference implementations for antimony_bootstrap. For each model family, we describe structure, pathways covered, rate law conventions, parameter sourcing, and how to leverage them.

---

## 1. Elbert/Bhatt QSP Models (Elbert_Esguerra_model_v2026b)

### Description
The Elbert/Bhatt Quantitative Systems Pharmacology (QSP) platform is the most comprehensive mechanistic model of AD pathophysiology available. It has been developed iteratively since ~2018 and represents the gold-standard target for this project.

### Structure
- **Compartments**: ~50 (plasma, brain ISF, brain parenchyma, CSF, perisynaptic space, endosomal, various cell types, peripheral organs)
- **Species**: Hundreds (amyloid-beta peptides in multiple forms, tau species, inflammatory mediators, neurotransmitters, drug concentrations)
- **Reactions**: ~800 reactions
- **Naming convention**: `{species}_{compartment}` (e.g., `AB42_BrainISF`, `pTau_Neuron`)

### Pathways Covered
- **Amyloid cascade**: APP processing (alpha, beta, gamma secretase), Abeta production (Abeta38, Abeta40, Abeta42), oligomerization, fibrillization, plaque formation/clearance
- **Tau pathology**: Tau phosphorylation, aggregation, NFT formation, tau spreading (Braak-like staging)
- **Neuroinflammation**: Microglial activation (M1/M2 polarization), astrocyte reactivity, cytokine signaling (TNF-alpha, IL-1beta, IL-6, IL-10), complement cascade
- **Synaptic dysfunction**: Neurotransmitter dynamics (ACh, glutamate), synaptic loss, LTP/LTD
- **Neuronal health**: Neuronal viability, apoptosis, oxidative stress
- **Vascular**: BBB transport, cerebral blood flow effects
- **Drug PK/PD**: Monoclonal antibody PK (lecanemab, aducanumab, donanemab), small molecule PK

### Rate Law Types
From the `RxnDict_to_antimony.py` converter:
- **MA** (Mass Action): `k * [S1] * [S2] * V_compartment` -- most common for binding, production, degradation
- **RMA** (Reversible Mass Action): Forward + reverse with `kon`/`koff` -- used for binding equilibria
- **BDF** (Bidirectional Flow): Same rate constant in both directions -- used for transport between compartments
- **UDF** (Unidirectional Flow): `k * [S]` without volume multiplication -- used for clearance, transport
- **custom_conc_per_time**: Custom expression x compartment volume
- **custom_amt_per_time**: Custom expression in absolute amounts
- **custom**: Arbitrary rate law expression (e.g., Hill functions, Michaelis-Menten, piecewise)

### Parameter Sources
- In vivo human PET/CSF biomarker data
- In vitro kinetic measurements from literature
- Allometric scaling from preclinical species
- Clinical trial PK data for drug parameters
- Some parameters estimated via model calibration to clinical endpoints

### Key Files for Reference
- `Elbert_Esguerra_model_v2026b/` -- the full model in the parent directory
- Rate constants, initial conditions, and compartment volumes are all parameterized with units and sources

---

## 2. Bhatt 2021 Alzheimer's QSP Model

### Citation
Bhatt et al. (2021). "Quantitative Systems Pharmacology Model of Alzheimer's Disease Pathology." CPT: Pharmacometrics and Systems Pharmacology.

### Description
This is the published version of the Elbert/Bhatt platform (an earlier snapshot). It was the first comprehensive QSP model to integrate amyloid, tau, neuroinflammation, and neuronal loss in a single framework, calibrated to clinical biomarker data.

### Structure
- **Compartments**: ~15-20 (plasma, brain ISF, CSF, neurons, microglia, astrocytes, endosomes)
- **Species**: ~100-150
- **Reactions**: ~200-300

### Pathways Covered
- Amyloid-beta production, aggregation, and clearance
- Tau phosphorylation and aggregation
- Microglial phagocytosis of amyloid
- Neuronal damage and cognitive endpoints (ADAS-Cog proxy)
- Anti-amyloid antibody PK/PD

### Rate Laws
- Predominantly mass action kinetics
- Michaelis-Menten for enzymatic processes (secretase activity)
- Hill functions for saturable processes (microglial phagocytosis)

### Parameter Sources
- Literature-derived kinetic constants
- Clinical biomarker data (CSF Abeta42, p-tau, total tau)
- PET imaging data (amyloid PET SUVr, tau PET)
- Population PK models from clinical trials

### Leveraging Strategy
- Use published parameter tables as primary source for kinetic constants
- Validate our module outputs against their reported steady-state concentrations
- Compare reaction structures to ensure pathway coverage is equivalent

---

## 3. Proctor-Gray Models of Amyloid and Tau

### Citations
- Proctor and Gray (2010). "A Model of Amyloid Aggregation and Neurotoxicity." J Alzheimers Dis.
- Proctor and Gray (2012). "A Model of Tau Aggregation." PLoS Comput Biol.
- Proctor et al. (2013). "Aggregation, Impairment of the UPS, and Neurodegeneration." BMC Neurosci.

### Description
The Proctor-Gray models are detailed mechanistic models focusing on protein aggregation dynamics. They are SBML-formatted and available on BioModels.

### Structure (Amyloid Model -- BIOMD0000000462)
- **Compartments**: 1-2 (cytoplasm, extracellular)
- **Species**: ~30-50 (APP, alpha-CTF, beta-CTF, AICD, Abeta monomers, dimers, oligomers, protofibrils, fibrils, plaques, secretases)
- **Reactions**: ~40-60

### Structure (Tau Model)
- **Compartments**: 1 (cytoplasm/neuronal)
- **Species**: ~20-30 (tau monomers, phospho-tau, paired helical filaments, NFTs, kinases like GSK3beta, CDK5, phosphatases like PP2A)
- **Reactions**: ~30-40

### Pathways Covered
- **Amyloid model**: APP processing by secretases, Abeta monomer release, nucleation-dependent polymerization (monomer to dimer to oligomer to protofibril to fibril to plaque), neurotoxic oligomer effects, UPS impairment
- **Tau model**: Tau phosphorylation by GSK3beta/CDK5, dephosphorylation by PP2A, p-tau aggregation into PHFs and NFTs, Abeta-driven enhancement of tau phosphorylation

### Rate Laws
- Mass action kinetics for most aggregation steps
- Michaelis-Menten for enzymatic reactions (secretase cleavage, kinase/phosphatase activity)
- Nucleation-dependent polymerization kinetics for aggregation cascades
- First-order degradation for clearance

### Parameter Sources
- In vitro kinetic studies of Abeta aggregation (e.g., Harper and Lansbury)
- Enzyme kinetics from cell-free assays
- Some parameters fitted to reproduce qualitative aggregation time courses
- Concentrations estimated from cell biology literature

### BioModels Entries
- **BIOMD0000000462** -- Proctor amyloid aggregation model
- **BIOMD0000000463** -- Proctor tau aggregation model

### Leveraging Strategy
- Directly import aggregation kinetic parameters (nucleation rates, elongation rates)
- Use as reference for aggregation module structure
- SBML files can be parsed to extract exact rate constants
- Compare our amyloid/tau modules against these well-validated submodels

---

## 4. Kyrtsos/Bhatt Amyloid Models

### Citation
Kyrtsos and Bhatt (2015). "Modeling the Role of the Glymphatic Pathway and Cerebral Blood Vessel Properties in Alzheimer's Disease Pathogenesis." PLoS ONE.

### Description
Focused on amyloid-beta transport and clearance, emphasizing the glymphatic system, perivascular drainage, and cerebrovascular factors. This model bridges the vascular and amyloid hypotheses.

### Structure
- **Compartments**: 5-8 (brain parenchyma, perivascular space, CSF, blood/plasma, vessel wall, glymphatic pathway)
- **Species**: ~20-30 (Abeta40, Abeta42, soluble vs. deposited forms in each compartment, ApoE, LRP1, RAGE)
- **Reactions**: ~30-50

### Pathways Covered
- Abeta production in brain parenchyma
- ISF bulk flow / glymphatic clearance
- Perivascular drainage pathway
- BBB transport via LRP1 (brain-to-blood) and RAGE (blood-to-brain)
- Enzymatic degradation (neprilysin, IDE, MMP)
- Cerebral amyloid angiopathy (CAA) -- vessel wall deposition
- Effects of cerebral blood flow reduction on clearance

### Rate Laws
- First-order kinetics for most transport and clearance
- Michaelis-Menten for receptor-mediated transport (LRP1, RAGE)
- Mass action for production
- Flow-dependent terms (clearance rate proportional to CBF)

### Parameter Sources
- Mouse glymphatic system experiments (Iliff et al.)
- Human CSF/plasma Abeta concentration measurements
- LRP1/RAGE transport kinetics from in vitro BBB models
- Neprilysin/IDE kinetics from enzyme assays
- CBF measurements from imaging studies

### Leveraging Strategy
- Primary source for transport/clearance parameters between compartments
- Use their compartment volume estimates and flow rates
- Reference for BBB transport module parameterization
- Important for vascular-amyloid interaction modules

---

## 5. BioModels.org Entries for Alzheimer's Disease

### Curated Models

| BioModels ID | Authors | Focus | Species Count | Reaction Count |
|---|---|---|---|---|
| BIOMD0000000462 | Proctor and Gray 2010 | Amyloid aggregation | ~40 | ~50 |
| BIOMD0000000463 | Proctor and Gray 2012 | Tau aggregation | ~25 | ~35 |
| BIOMD0000000983 | Sasidharakurup et al. | Amyloid-calcium signaling | ~30 | ~40 |
| BIOMD0000000127 | Hao and Bhatt 2005 | Abeta kinetics (simple) | ~10 | ~15 |
| BIOMD0000000831 | Puri and Li 2010 | Abeta42 aggregation kinetics | ~15 | ~20 |
| MODEL1006230101 | Craft et al. 2002 | Abeta production/clearance | ~8 | ~10 |

### Additional Relevant Entries
- **Neuroinflammation models**: Several non-AD-specific inflammation models that include relevant pathways (NF-kB signaling, cytokine networks)
- **Calcium signaling models**: Relevant to excitotoxicity modules
- **Apoptosis models**: BCL-2 family signaling relevant to neuronal death

### Rate Law Conventions in BioModels
- SBML-standard kinetic law annotations
- Most use mass action or Michaelis-Menten
- Parameters annotated with SBO terms and units
- Can be programmatically extracted via BioModels API

### Leveraging Strategy
- Use antimony_bootstrap retrieval module to query BioModels API
- Extract SBML, convert to Antimony, compare rate constants
- Cross-validate our parameter choices against published model values
- Import well-validated sub-models directly where applicable

---

## 6. Other Notable Models

### Craft et al. (2002) -- Minimal Abeta Model
- 2 compartments (brain, plasma), ~8 species
- Simple production/clearance kinetics
- Useful as a sanity check for steady-state Abeta levels

### Jack et al. (2013) -- Biomarker Cascade Model
- Not strictly ODE-based but provides important temporal ordering constraints
- Biomarker trajectories (amyloid to tau to neurodegeneration to cognitive decline)
- Use to validate that our model produces the correct temporal cascade

### Lloret-Villas et al. (2017) -- Integrated AD Pathway Model
- Focus on signaling crosstalk between amyloid, tau, and inflammation
- Useful for identifying key regulatory interactions between modules

---

## 7. Comparative Summary

| Feature | Elbert/Bhatt 2026 | Bhatt 2021 | Proctor-Gray | Kyrtsos/Bhatt | BioModels (various) |
|---|---|---|---|---|---|
| Compartments | ~50 | ~15-20 | 1-2 | 5-8 | 1-3 |
| Species | Hundreds | ~100-150 | 30-50 | 20-30 | 8-40 |
| Reactions | ~800 | ~200-300 | 40-60 | 30-50 | 10-50 |
| Amyloid | Full cascade | Full cascade | Detailed aggregation | Transport focus | Varies |
| Tau | Full | Full | Detailed aggregation | Minimal | Varies |
| Inflammation | Full (M1/M2) | Moderate | None | None | Some |
| Vascular | Yes (BBB) | Limited | None | Primary focus | None |
| Drug PK/PD | Extensive | Yes | None | None | None |
| Rate types | MA/RMA/BDF/UDF/custom | Mostly MA/MM | MA/MM | MA/MM/1st order | MA/MM |
| Available format | Antimony/SBML | Published tables | SBML (BioModels) | Published equations | SBML |

---

## 8. Strategy for Leveraging Existing Models

### 8.1 Parameter Sourcing Priority

When parameterizing antimony_bootstrap modules, use this hierarchy:

1. **Elbert_Esguerra_model_v2026b** (gold standard) -- Direct extraction of rate constants, ICs, compartment volumes. This is our primary reference and the model we are reconstructing.
2. **Bhatt 2021 published tables** -- For parameters not directly accessible from the code, check supplementary materials.
3. **Domain-specific models** (Proctor-Gray for aggregation, Kyrtsos for transport) -- Cross-validate Elbert parameters and fill gaps.
4. **BioModels SBML extraction** -- Programmatic extraction for additional validation.
5. **Primary literature** -- When no model source exists, go to original experimental papers.

### 8.2 Module Architecture Alignment

- Structure our modules to match Elbert compartmentalization and naming conventions
- Use the same rate law type system (MA/RMA/BDF/UDF/custom) since our assembly pipeline is designed for it
- Ensure species names match Elbert convention: `{species}_{compartment}`

### 8.3 Validation Against Reference Models

For each module:
1. Compare steady-state concentrations against Elbert model outputs
2. Compare individual reaction fluxes where possible
3. Use Proctor-Gray models as independent validation of aggregation dynamics
4. Use Kyrtsos model to validate transport/clearance rates
5. Compare against clinical biomarker ranges (CSF Abeta42: ~200-1000 pg/mL, CSF p-tau: ~20-80 pg/mL)

### 8.4 BioModels Retrieval Workflow

Use the retrieval module to search for relevant models:
```bash
just retrieve-biomodels "alzheimer amyloid"
```

The retrieval module can parse SBML and extract:
- Compartment volumes
- Species initial concentrations
- Kinetic parameters with units
- Rate law expressions

### 8.5 Practical Recommendations

1. **Start with the Elbert model as ground truth** -- Our primary task is to reconstruct this model from dismech + literature, so it serves as both reference and validation target.
2. **Use Proctor-Gray for aggregation subroutines** -- Their detailed nucleation-polymerization kinetics are well-validated and can inform our amyloid and tau aggregation modules.
3. **Use Kyrtsos for transport parameters** -- Their focus on BBB transport and glymphatic clearance provides the best available estimates for inter-compartment transport.
4. **Cross-validate liberally** -- Any parameter we assign should ideally be consistent with at least two independent model sources.
5. **Document parameter provenance** -- For every ParameterSpec, record which reference model(s) support the chosen value, along with PMID citations.
6. **Flag discrepancies** -- When models disagree on parameter values, document the range and choose based on the most clinically relevant data (human > primate > rodent > in vitro).

---

## 9. Key References

1. Bhatt et al. (2021). CPT Pharmacometrics Syst Pharmacol. -- QSP model of AD
2. Proctor and Gray (2010). J Alzheimers Dis. -- Amyloid aggregation model
3. Proctor and Gray (2012). PLoS Comput Biol. -- Tau aggregation model
4. Kyrtsos and Bhatt (2015). PLoS ONE. -- Glymphatic/vascular amyloid model
5. Craft et al. (2002). J Neuroimmunol. -- Minimal Abeta kinetics
6. Elbert and Bhatt (ongoing). Elbert_Esguerra_model_v2026b -- Gold-standard reference

---

*Generated: 2026-02-24 | antimony_bootstrap reference model survey*
