# oxidative_stress Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/oxidative_stress.yaml`
- Tier: 2
- Compartments: `Neuron`, `Mitochondria`
- Reaction count: 24
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/oxidative_stress.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This Tier 2 module implements oxidative stress with two-compartment ROS handling and explicit antioxidant/damage pathways:
- ROS pools: `ROS_Mitochondria`, `ROS_Neuron`
- Antioxidant enzymes: `SOD2_Mitochondria`, `SOD1_Neuron`, `GPX_Neuron`, `CAT_Neuron`
- Glutathione cycle: `GSH_Neuron`, `GSSG_Neuron`
- Stress-response signaling: `NRF2_Neuron`, `KEAP1_Neuron`
- Damage biomarkers: `HNE4_Neuron` (4-HNE), `MDA_Neuron`, `OHdG8_Neuron` (8-OHdG)

Reaction groups included:
- ROS production/leakage (mitochondrial basal + autocatalytic + mitochondrial-to-neuronal transfer)
- SOD/CAT/GPX mediated ROS clearance
- GSH/GSSG cycling and NRF2-enhanced antioxidant replenishment
- NRF2-KEAP1 activation/degradation control loop
- Lipid peroxidation and DNA oxidation damage generation

## Source-to-Model Mapping
- Strategy document (`plan/strategy_synaptic_neuronal.md`) provided the oxidative stress mechanism blocks, expected kinetics, and nominal parameter scales (ROS leak, GSH cycle, NRF2 pathway, oxidative damage terms).
- Module parameter JSON (`data/parameters/module/oxidative_stress.json`) was screened for transferable values. Most extracted entries were heterogeneous/non-specific; `Hill_coefficient = 2.0` was directly incorporated for ROS amplification nonlinearity.
- Elbert reference antimony directory was checked for oxidative-stress-specific reaction templates and naming constraints. Core oxidative species/reactions were not directly present in the loaded Elbert reaction files, so this module follows project ModuleSpec conventions while staying compatible with Elbert-style compartment/species naming.
- Schema (`src/antimony_bootstrap/schema/module_spec.py`) constrained fields, enum values, and reaction encoding (`MA`, `custom_conc_per_time`) and was followed exactly.
- Existing example (`models/alzheimers/modules/abeta_production.yaml`) was used for YAML structure, confidence/source metadata style, and concise notes/evidence formatting.

## Assumptions
1. `Mitochondria` is used as compartment name (per request), with `V_Mitochondria` volume parameter analogous to the strategy's mitochondrial subcompartment.
2. 4-HNE and 8-OHdG are encoded as `HNE4_Neuron` and `OHdG8_Neuron` to keep Antimony-safe identifiers while preserving biological meaning.
3. Damage biomarkers are modeled as accumulating pools in this Tier 2 scope (no dedicated repair/export reactions beyond antioxidant buffering).
4. Parameter values are initialization defaults intended for downstream calibration; confidence is marked `estimated` or `assumed` accordingly.

## Validation Status
- YAML structure and field names match `ModuleSpec` schema expectations.
- Reaction count and rate law constraints satisfy the requested specification:
  - 24 reactions (within 15-25 target)
  - Includes ROS production, SOD dismutation, glutathione cycle, NRF2 pathway, lipid peroxidation, DNA oxidation
  - Uses only `MA` and `custom_conc_per_time`
- Recommended follow-up: run project-wide module validation and simulation sanity checks under baseline and high-ROS perturbation conditions.
