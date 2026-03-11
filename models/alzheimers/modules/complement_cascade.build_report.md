# complement_cascade Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/complement_cascade.yaml`
- Tier: 2
- Compartment scope: `BrainISF`, `Synapse`
- Reaction count: 14
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/complement_cascade.json`
2. `plan/strategy_neuroinflammation.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This Tier-2 module implements classical complement activation and synapse pruning with explicit representation of requested key species:
- Core complement proteins: `C1Q`, `C3`, `C3a`, `C3b`, `C4`, `C5`, `C5a`, `MAC`
- Regulators: `CR1`, `CD59`, `CLU`
- Synaptic receptors/signaling: `C3AR1`, `C5AR1`

Implemented reaction groups:
- Basal production for C1Q/C3/C4/C5
- AB42 plaque-dependent classical pathway activation (`C1Q_AB` intermediate)
- C3 cleavage to `C3a` and `C3b` via convertase-like custom kinetics
- C3b regulation by CR1/clusterin control term
- C5 cleavage and terminal MAC formation with CD59/CLU inhibitory gating
- Complement-mediated synapse tagging and receptor-coupled elimination of tagged synapses

## Source-to-Model Mapping
- `complement_cascade.json` contains no extracted parameters (`parameter_count: 0`), so all kinetic constants were instantiated as explicit placeholders with confidence labels.
- `strategy_neuroinflammation.md` provided the required topology and motifs for:
  - AB42-triggered classical pathway initiation
  - C3 cleavage and C3b opsonization logic
  - complement-driven synapse elimination dynamics
- Elbert reference files were used for naming and compartmental modeling style consistency; no direct complement reaction block was found in the provided antimony text set.

## Assumptions
1. `AB42_plaque_BrainISF` is included as a shared coupling species for classical pathway initiation.
2. `C3AR1` and `C5AR1` are represented in `Synapse` and scale tagged synapse elimination flux.
3. `CR1`, `CD59`, and `CLU` are modeled as constitutive modulators (no separate synthesis/degradation reactions in this first pass).
4. Numeric values are Tier-2 calibration placeholders pending module-specific parameter extraction or fitting.

## Validation Status
- Ran schema validation command:
  - `uv run antimony-bootstrap validate-module models/alzheimers/modules/complement_cascade.yaml`
- Result: `Valid: complement_cascade (14 reactions, 25 parameters)`
