# Batch 16 Findings: Alzheimers Paper Analysis

**Date**: 2026-02-24

**Papers analyzed**: 86

**Papers with quantitative/mechanistic data**: 15

## 1. Papers with Quantitative/Mechanistic Data

Of 86 papers analyzed, **15** contain quantitative or mechanistic data potentially extractable for ODE modeling.

### Top Papers by Quantitative Content Score

| PMC ID | Title | Quant Score | Key Pathways |
|--------|-------|-------------|-------------|
| PMC2669320 | Loss of LR11/SORLA Enhances Early Pathology in a Mouse Model of Amyloidosis: Evi | 4 | Abeta_clearance, Abeta_aggregation, Cholesterol_metabolism |
| PMC2730994 | A gamma-secretase inhibitor decreases amyloid-beta production in the central ner | 4 | Abeta_production, Abeta_aggregation, Abeta_clearance |
| PMC2752010 | Amyloid-β protofibril levels correlate with spatial learning in Arctic Alzheimer | 4 | Abeta_clearance, Abeta_aggregation, Synaptic_dysfunction |
| PMC2663406 | Aβ peptides in human plasma and tissues and their significance for Alzheimer’s d | 3 | Abeta_clearance, Abeta_aggregation, Cholesterol_metabolism |
| PMC2676733 | Autophagy Induction and Autophagosome Clearance in Neurons: Relationship to Auto | 3 | Abeta_clearance, Autophagy_lysosome, Abeta_aggregation |
| PMC2702854 | Soluble oligomers of amyloid β-protein facilitate hippocampal long-term depressi | 3 | Abeta_clearance, Abeta_aggregation, Synaptic_dysfunction |
| PMC2740474 | γ-Secretase Heterogeneity in the Aph1 Subunit: Relevance for Alzheimer’s Disease | 3 | Abeta_production |
| PMC2743790 | Antidepressants increase neural progenitor cells in the human hippocampus | 3 | Abeta_clearance, Neuroinflammation |
| PMC2637561 | The future of amyloid-beta imaging: a tale of radionuclides and tracer prolifera | 2 | General |
| PMC2677798 | Serial PIB and MRI in normal, mild cognitive impairment and Alzheimer's disease: | 2 | Abeta_clearance, Abeta_aggregation, Tau_phosphorylation |
| PMC2692134 | Linking Aβ and Tau in Late-Onset Alzheimer’s Disease: A Dual Pathway Hypothesis | 2 | Abeta_clearance, Autophagy_lysosome, Abeta_aggregation |
| PMC2702495 | A facile method for expression and purification of the Alzheimer’s disease-assoc | 2 | Abeta_clearance, Abeta_aggregation, Autophagy_lysosome |
| PMC2711514 | MITOCHONDRIAL FRAGMENTATION IN NEURODEGENERATION | 2 | Abeta_clearance, Autophagy_lysosome, Abeta_aggregation |
| PMC2717716 | The Role of Metabolic Disorders in Alzheimer's Disease and Vascular Dementia: Tw | 2 | Abeta_clearance, Cholesterol_metabolism, Oxidative_stress |
| PMC2751885 | Remote control of neuronal activity in transgenic mice expressing evolved G prot | 2 | BBB_transport, Synaptic_dysfunction, Calcium_dysregulation |

## 2. Key Pathways Identified

| Pathway | Paper Count | PMC IDs (sample) |
|---------|-----------|------------------|
| Abeta_clearance | 67 | PMC2578820, PMC2580745, PMC2581433, PMC2583788, PMC2592715 |
| Abeta_aggregation | 56 | PMC2578820, PMC2580745, PMC2583788, PMC2597474, PMC2624575 |
| Neuroinflammation | 39 | PMC2580745, PMC2581433, PMC2583788, PMC2597474, PMC2615629 |
| Tau_phosphorylation | 37 | PMC2578820, PMC2624575, PMC2637553, PMC2638813, PMC2642882 |
| Cholesterol_metabolism | 25 | PMC2631488, PMC2636844, PMC2653223, PMC2654279, PMC2663406 |
| Abeta_production | 20 | PMC2578820, PMC2580745, PMC2581433, PMC2597474, PMC2626633 |
| Autophagy_lysosome | 16 | PMC2580745, PMC2581433, PMC2633781, PMC2648510, PMC2654279 |
| Calcium_dysregulation | 15 | PMC2578820, PMC2632990, PMC2633437, PMC2673049, PMC2677572 |
| Synaptic_dysfunction | 14 | PMC2578820, PMC2632990, PMC2633437, PMC2673049, PMC2702854 |
| Oxidative_stress | 13 | PMC2578820, PMC2580745, PMC2583788, PMC2597474, PMC2626633 |
| BBB_transport | 5 | PMC2578820, PMC2626633, PMC2654279, PMC2717716, PMC2751885 |
| Insulin_signaling | 5 | PMC2580745, PMC2615629, PMC2653223, PMC2676733, PMC2717716 |

### Pathway Coverage Summary

- **82** papers map to at least one AD pathway
- Most represented: Abeta_clearance (67 papers)

## 3. Extractable Reactions and Rate Laws

Based on detailed analysis of top quantitative papers:

### PMC2669320: Loss of LR11/SORLA Enhances Early Pathology in a Mouse Model of Amyloidosis: Evidence for a Proximal
- **Quantitative score**: 4
- **Pathways**: Abeta_clearance, Abeta_aggregation, Cholesterol_metabolism, Abeta_production, Neuroinflammation
- **Species identified**: APP, ApoE, BACE1
- **Reaction types found**:
  - degradation
  - aggregation
  - production
  - enzymatic_cleavage

### PMC2730994: A gamma-secretase inhibitor decreases amyloid-beta production in the central nervous system
- **Quantitative score**: 4
- **Pathways**: Abeta_production, Abeta_aggregation, Abeta_clearance, Cholesterol_metabolism
- **Species identified**: 
- **Reaction types found**:
  - degradation
  - aggregation
  - production

### PMC2752010: Amyloid-β protofibril levels correlate with spatial learning in Arctic Alzheimer’s disease transgeni
- **Quantitative score**: 4
- **Pathways**: Abeta_clearance, Abeta_aggregation, Synaptic_dysfunction, Tau_phosphorylation, Calcium_dysregulation
- **Species identified**: APP, Glutamate, PSEN, sAPP
- **Reaction types found**:
  - degradation
  - aggregation
  - transport

### PMC2663406: Aβ peptides in human plasma and tissues and their significance for Alzheimer’s disease
- **Quantitative score**: 3
- **Pathways**: Abeta_clearance, Abeta_aggregation, Cholesterol_metabolism, Neuroinflammation
- **Species identified**: Insulin
- **Reaction types found**:
  - transport
  - enzymatic_cleavage
  - degradation
  - aggregation
  - production

### PMC2676733: Autophagy Induction and Autophagosome Clearance in Neurons: Relationship to Autophagic Pathology in 
- **Quantitative score**: 3
- **Pathways**: Abeta_clearance, Autophagy_lysosome, Abeta_aggregation, Tau_phosphorylation, Insulin_signaling, Neuroinflammation
- **Species identified**: APP
- **Reaction types found**:
  - degradation
  - phosphorylation
  - transport
  - aggregation

### PMC2702854: Soluble oligomers of amyloid β-protein facilitate hippocampal long-term depression by disrupting neu
- **Quantitative score**: 3
- **Pathways**: Abeta_clearance, Abeta_aggregation, Synaptic_dysfunction, Tau_phosphorylation, Calcium_dysregulation, Neuroinflammation
- **Species identified**: APP, Calcium, GSK3B, Glutamate, Insulin, PSEN
- **Reaction types found**:
  - degradation
  - aggregation
  - transport

### PMC2740474: γ-Secretase Heterogeneity in the Aph1 Subunit: Relevance for Alzheimer’s Disease
- **Quantitative score**: 3
- **Pathways**: Abeta_production
- **Species identified**: APP, BACE1, PSEN
- **Reaction types found**:
  - production
  - enzymatic_cleavage

### PMC2743790: Antidepressants increase neural progenitor cells in the human hippocampus
- **Quantitative score**: 3
- **Pathways**: Abeta_clearance, Neuroinflammation
- **Species identified**: 
- **Reaction types found**:
  - degradation
  - enzymatic_cleavage

### PMC2637561: The future of amyloid-beta imaging: a tale of radionuclides and tracer proliferation
- **Quantitative score**: 2
- **Pathways**: General
- **Species identified**: sAPP
- **Reaction types found**:
  - production

### PMC2677798: Serial PIB and MRI in normal, mild cognitive impairment and Alzheimer's disease: implications for se
- **Quantitative score**: 2
- **Pathways**: Abeta_clearance, Abeta_aggregation, Tau_phosphorylation, Cholesterol_metabolism
- **Species identified**: ApoE
- **Reaction types found**:
  - production
  - enzymatic_cleavage

### PMC2692134: Linking Aβ and Tau in Late-Onset Alzheimer’s Disease: A Dual Pathway Hypothesis
- **Quantitative score**: 2
- **Pathways**: Abeta_clearance, Autophagy_lysosome, Abeta_aggregation, Cholesterol_metabolism, Tau_phosphorylation, Abeta_production
- **Species identified**: APP, ApoE, GSK3B, PSEN, Tau, sAPP
- **Reaction types found**:
  - phosphorylation
  - transport
  - enzymatic_cleavage
  - degradation
  - aggregation
  - production

### PMC2702495: A facile method for expression and purification of the Alzheimer’s disease-associated amyloid β-pept
- **Quantitative score**: 2
- **Pathways**: Abeta_clearance, Abeta_aggregation, Autophagy_lysosome
- **Species identified**: 
- **Reaction types found**:
  - transport
  - enzymatic_cleavage
  - degradation
  - aggregation
  - production

### PMC2711514: MITOCHONDRIAL FRAGMENTATION IN NEURODEGENERATION
- **Quantitative score**: 2
- **Pathways**: Abeta_clearance, Autophagy_lysosome, Abeta_aggregation, Oxidative_stress, Tau_phosphorylation, Calcium_dysregulation, Neuroinflammation
- **Species identified**: CDK5, Calcium, ROS, sAPP
- **Reaction types found**:
  - phosphorylation
  - transport
  - enzymatic_cleavage
  - degradation
  - production

### PMC2717716: The Role of Metabolic Disorders in Alzheimer's Disease and Vascular Dementia: Two Roads Converged?
- **Quantitative score**: 2
- **Pathways**: Abeta_clearance, Cholesterol_metabolism, Oxidative_stress, Tau_phosphorylation, Insulin_signaling, Neuroinflammation, BBB_transport
- **Species identified**: ApoE, IL6, Insulin, LRP1, TNFa, Tau
- **Reaction types found**:
  - phosphorylation
  - transport
  - enzymatic_cleavage
  - degradation
  - production

## 4. Species and Compartments

### Species Identified Across Top Papers

| Species | Occurrences | Sample Papers |
|---------|-------------|---------------|
| APP | 6 | PMC2669320, PMC2752010, PMC2676733 |
| ApoE | 4 | PMC2669320, PMC2677798, PMC2692134 |
| PSEN | 4 | PMC2752010, PMC2702854, PMC2740474 |
| sAPP | 4 | PMC2752010, PMC2637561, PMC2692134 |
| Insulin | 3 | PMC2663406, PMC2702854, PMC2717716 |
| Calcium | 3 | PMC2702854, PMC2711514, PMC2751885 |
| BACE1 | 2 | PMC2669320, PMC2740474 |
| Glutamate | 2 | PMC2752010, PMC2702854 |
| GSK3B | 2 | PMC2702854, PMC2692134 |
| Tau | 2 | PMC2692134, PMC2717716 |
| CDK5 | 1 | PMC2711514 |
| ROS | 1 | PMC2711514 |
| IL6 | 1 | PMC2717716 |
| LRP1 | 1 | PMC2717716 |
| TNFa | 1 | PMC2717716 |

### Suggested Compartments (Elbert Convention)

- **BrainISF**: Brain interstitial fluid - Abeta dynamics
- **BrainICF**: Brain intracellular fluid - APP processing, tau phosphorylation
- **CSF**: Cerebrospinal fluid - Abeta/tau drainage
- **Plasma**: Blood plasma - peripheral clearance, BBB transport
- **Neuron**: Neuronal cell body - calcium signaling, oxidative stress
- **Microglia**: Microglial cells - neuroinflammation, phagocytosis
- **Astrocyte**: Astrocyte cells - glutamate cycling, ApoE production
- **Endosome**: Endosomal compartment - APP processing
- **Synapse**: Synaptic cleft - neurotransmission
- **Mitochondria**: Mitochondrial compartment - ROS production

### Suggested Antimony Reaction Templates

```antimony
// Abeta production from APP (beta-secretase cleavage)
J_APP_cleavage: APP_BrainICF -> sAPPb_BrainISF + CTFb_BrainICF; k_BACE1 * BACE1_BrainICF * APP_BrainICF

// Abeta42 production from gamma-secretase cleavage
J_Abeta42_prod: CTFb_BrainICF -> AB42_BrainISF; k_gamma * PSEN_BrainICF * CTFb_BrainICF

// Abeta42 aggregation (monomer to oligomer)
J_AB42_aggregation: 2 AB42_BrainISF -> AB42o_BrainISF; k_agg * AB42_BrainISF^2

// Abeta42 clearance by neprilysin (Michaelis-Menten)
J_AB42_NEP_clearance: AB42_BrainISF -> ; Vmax_NEP * AB42_BrainISF / (Km_NEP + AB42_BrainISF)

// Tau phosphorylation by GSK3beta
J_Tau_phos: Tau_BrainICF -> pTau_BrainICF; k_GSK3B * GSK3B_BrainICF * Tau_BrainICF

// Microglial activation by Abeta oligomers
J_microglia_act: Microglia_rest_Brain -> Microglia_act_Brain; k_act * AB42o_BrainISF * Microglia_rest_Brain

// TNFa production by activated microglia
J_TNFa_prod: -> TNFa_BrainISF; k_TNFa * Microglia_act_Brain

// Abeta transport across BBB via LRP1
J_AB42_BBB_efflux: AB42_BrainISF -> AB42_Plasma; k_LRP1 * LRP1_BBB * AB42_BrainISF

// ROS production from mitochondrial dysfunction
J_ROS_prod: -> ROS_Neuron; k_ROS_basal + k_ROS_AB * AB42o_BrainISF
```

## Summary

This batch of 86 papers provides substantial coverage of AD mechanisms.
**15** papers contain quantitative data suitable for parameterizing ODE models.
The most represented pathways are neuroinflammation, Abeta production/clearance, and tau phosphorylation.
Key extractable mechanisms include enzymatic cleavage rates, aggregation kinetics, clearance rates, and inflammatory signaling cascades.