# autophagy Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/autophagy.yaml`
- Tier: 3
- Compartments: `Neuron`
- Reaction count: 25
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/autophagy.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module implements neuronal autophagy dynamics centered on the requested species set:
- Initiation/signaling: `AMPK`, `mTOR`, `ULK1`, `TFEB`
- Core autophagy machinery: `BECLIN1`, `LC3I`, `LC3II`, `P62`
- Vesicle and lysosomal states: `AUTOPHAGOSOME`, `LYSOSOME`, `AUTOLYSOSOME`, `LAMP1`

Mechanistic groups:
- Initiation control via AMPK-mTOR-ULK1 (`AMPK_Activation_by_Stress`, `mTOR_Inhibition_by_AMPK`, `ULK1_Activation_by_AMPK_and_mTOR_Relief`)
- Nucleation and membrane progression (`BECLIN1_Activation_by_ULK1`, `Autophagosome_Nucleation`, `LC3_Lipidation_LC3I_to_LC3II`)
- Cargo recognition and flux (`Cargo_Recognition_P62_to_Autophagosome`, `P62_Autolysosomal_Degradation`)
- Lysosome biogenesis/fusion/degradation (`Lysosome_Biogenesis_by_TFEB_LAMP1`, `Autophagosome_Lysosome_Fusion`, `Autolysosome_Resolution`)

## Source-to-Model Mapping
- `autophagy.json` provided 3 sparse priors and no reaction-specific named constants:
  - `Hill_coefficient = 4.0` mapped directly to cooperative AMPK/mTOR gating (`Hill_coefficient`).
  - concentration geometric mean `87.02718086557644` mapped to half-saturation terms (`K_*`) used across ULK1/TFEB/lipidation/fusion controls (`K_autophagy_switch`, `K_ampk_mtor`, `K_ampk_ulk1`, `K_mtor_ulk1`, etc.).
  - clearance timescale-like value `5477.225575051666 h` mapped as `k_lysosome_turnover = ln(2)/5477.225575051666 = 0.00012654888458104032 1/hr`.
- Strategy document was used for tiering/compartment context (`Neuron`, `V_Neuron = 0.0005 L`) and for consistency with the synaptic-neuronal module style.
- Elbert antimony references were scanned for direct autophagy species/reaction templates (`BECLIN1`, `LC3`, `ULK1`, `TFEB`, `LAMP1`, `lysosome`, `autophagy`); no explicit autophagy block was identified. Construction therefore follows antimony_bootstrap schema and existing module conventions.

## Parameterization Notes
- `MA` kinetics were used for first-order turnover and simple consumption/transfer steps.
- `custom_conc_per_time` kinetics were used where concentration-based regulation is central:
  - cooperative AMPK/mTOR gating (`AMPK_Activation_by_Stress`, `mTOR_Inhibition_by_AMPK`)
  - ULK1/TFEB activation by AMPK and mTOR relief
  - BECLIN1-dependent LC3 lipidation
  - TFEB-controlled LAMP1/lysosome/p62 synthesis
  - LAMP1-modulated autophagosome-lysosome fusion
- Most parameters are estimated placeholders intended for calibration because the autophagy input JSON is sparse and mostly generic.

## Assumptions
1. Requested key species are represented as effective active pools (single-state species) in `Neuron`.
2. `AUTOPHAGOSOME`, `LYSOSOME`, and `AUTOLYSOSOME` are effective pool variables rather than explicit vesicle-size distributions.
3. `Cargo_Recognition_P62_to_Autophagosome` and `P62_Autolysosomal_Degradation` use p62 flux as a proxy for aggregate cargo handling.
4. The module is internally closed with basal synthesis/turnover terms; integrated whole-model assembly may replace selected source terms with cross-module couplings.

## Validation Status
- YAML fields and enums align with `ModuleSpec` schema (`RateType`: `MA`, `custom_conc_per_time`).
- Reaction count satisfies the requested range (15-25): 25.
- Required compartment and key species set are present.
- Recommended follow-up checks:
  - `just validate-module models/alzheimers/modules/autophagy.yaml`
  - `just assemble`
  - perturbation tests: increase `mTOR_Neuron` (expect reduced `ULK1_Neuron`, `AUTOPHAGOSOME_Neuron`) and increase `AMPK_Neuron` (expect increased `TFEB_Neuron`, `LYSOSOME_Neuron`, autolysosomal flux)
