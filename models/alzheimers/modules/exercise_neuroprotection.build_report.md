# exercise_neuroprotection Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/exercise_neuroprotection.yaml`
- Tier: 4 (exploratory)
- Compartments: `Neuron`, `Plasma`, `BrainISF`
- Reaction count: 10
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/exercise_neuroprotection.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This exploratory module provides exercise-driven neuroprotective forcing terms and intermediate signaling states for downstream AD modules.

Core represented biology:
- Peripheral `IRISIN` release into plasma and delivery to `BrainISF`
- Exercise-associated `lactate` increase in `BrainISF`
- Neuronal `PGC1alpha -> FNDC5` activation axis
- Exercise-associated `IL6_exercise` transient routing from plasma to neuron
- Anti-inflammatory conversion proxy (`AntiInflammatoryTone_BrainISF`)
- Exercise-enhanced `BDNF_exercise` upregulation in neuron

## Source-to-Model Mapping
- Parameter input JSON contains no module-specific constants (`parameter_count: 0`), so all parameters were instantiated as explicit exploratory placeholders with `estimated` or `assumed` confidence.
- `strategy_synaptic_neuronal.md` was used for compartment conventions and neuron-centric module style consistency; it does not define this exercise module directly.
- Elbert reference antimony files were reviewed for compartment naming/volume conventions and mass-action/custom kinetics style; no direct IRISIN/FNDC5/lactate exercise-neuroprotection block was found.
- Existing module style and schema requirements were followed from the provided YAML example and `ModuleSpec` schema.

## Assumptions
1. Muscle-origin exercise signals are represented as source reactions into `Plasma`/`BrainISF` due to fixed compartment scope.
2. `exercise_drive` is a dimensionless control parameter (default `1.0`) to scale exercise exposure in simulations.
3. `IL6_Resolution_to_AntiInflammatoryTone` is a lumped anti-inflammatory surrogate rather than explicit cytokine network modeling.
4. Parameter magnitudes are literature-informed placeholders and intended for later calibration/sensitivity analysis.

## Validation Status
- YAML structure follows `ModuleSpec` fields and supported `RateType` enums.
- Reaction count is within requested range (5-10): 10.
- Required key species were included: `IRISIN`, `BDNF_exercise`, `lactate`, `PGC1alpha`, `FNDC5`, `IL6_exercise`.
- Recommended follow-up checks:
  - `just validate-module models/alzheimers/modules/exercise_neuroprotection.yaml`
  - `just assemble`
  - perturbation tests by varying `exercise_drive` and `k_irisin_release`
