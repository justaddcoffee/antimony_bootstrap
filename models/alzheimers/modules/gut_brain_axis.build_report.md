# gut_brain_axis Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/gut_brain_axis.yaml`
- Tier: 4 (exploratory)
- Compartment scope: `Gut`, `Plasma`, `BrainISF`
- Reaction count: 10
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/gut_brain_axis.json`
2. `plan/strategy_neuroinflammation.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This Tier-4 exploratory module encodes a mechanistic gut-to-brain inflammatory axis with required key species:
- `SCFA_Gut`
- `LPS_Gut` and `LPS_Plasma`
- `TMAO_Plasma`
- `gut_permeability_Gut`
- `vagal_tone_Gut`

Brain coupling output species:
- `TNFA_BrainISF`

Reaction groups implemented:
- SCFA production and clearance in gut
- LPS production in gut and permeability-dependent translocation to plasma
- Plasma LPS and TMAO turnover with LPS-gated TMAO generation
- Dynamic gut barrier remodeling (LPS injury vs SCFA repair)
- Dynamic vagal tone remodeling (SCFA support vs inflammatory suppression)
- Brain TNFA drive from plasma LPS/TMAO signals with vagal protective damping

## Source-to-Model Mapping
- `gut_brain_axis.json` was minimal (`parameter_count: 0`), so no direct numeric parameter import was possible.
- `strategy_neuroinflammation.md` provided reusable ODE motifs used here:
  - saturating signal-response forms (`x/(K+x)`)
  - first-order turnover/clearance terms
  - anti-inflammatory suppression factor structure
- Elbert reference set was used for compatibility with naming and module structure conventions rather than direct gut-brain equations.

## Parameterization Notes
- Parameters are intentionally exploratory placeholders and mostly marked `assumed`.
- Midpoint constants (`K_*`) were set to keep concentration-response terms numerically active around initial state magnitudes.
- Brain TNFA turnover uses a fast clearance scale (`k_tnfa_brain_clear = 30/day`) aligned with neuroinflammation strategy turnover guidance.

## Schema and Naming Compliance
- YAML structure matches `ModuleSpec` in `src/antimony_bootstrap/schema/module_spec.py`.
- Species naming follows `{entity}_{compartment}`.
- Requested compartment set and key species are present.
- Reaction count is within requested range (5-10).
- Rate law usage is restricted to `MA` and `custom_conc_per_time`.

## Assumptions
1. Gut dysbiosis pressure is represented by basal LPS source and dynamic barrier/vagal state equations.
2. TMAO is represented as a lumped plasma pool with LPS-gated production to encode dysbiosis linkage.
3. `TNFA_BrainISF` is used as the neuroinflammatory readout coupling species for composition with other modules.
4. Tier-4 values are placeholders intended for later calibration/sensitivity analysis.

## Validation Status
- Ran:
  - `uv run antimony-bootstrap validate-module models/alzheimers/modules/gut_brain_axis.yaml`
- Result:
  - `Valid: gut_brain_axis (10 reactions, 23 parameters)`
