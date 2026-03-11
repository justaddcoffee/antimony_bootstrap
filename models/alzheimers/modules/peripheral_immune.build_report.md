# peripheral_immune Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/peripheral_immune.yaml`
- Tier: 4
- Compartment scope: `Plasma`, `BrainISF`
- Reaction count: 19
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/peripheral_immune.json`
2. `plan/strategy_neuroinflammation.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This Tier-4 module implements a peripheral immune layer with bidirectional Plasma-BrainISF coupling and immunotherapy effects.

Required key species are included (compartment-resolved):
- `MONOCYTE_Plasma`
- `MACROPHAGE_BrainISF`
- `T_CELL_Plasma`
- `T_CELL_BrainISF`
- `TNFA_Plasma`
- `IL6_Plasma`
- `CRP_Plasma` (CRP)
- `anti_AB_antibody_Plasma` (plus `anti_AB_antibody_BrainISF` transport pool)

Additional coupling species:
- `AB42_BrainISF`
- `AB42_anti_AB_complex_BrainISF`

Reaction groups implemented:
- Monocyte production/clearance and cytokine-amplified infiltration to BrainISF macrophages
- T-cell production/clearance, TNFA-gated entry to BrainISF, and egress back to plasma
- Peripheral cytokine module (TNFA, IL6) with first-order clearance
- IL6 -> CRP Hill-type acute-phase response
- Anti-AB immunotherapy source, plasma clearance, brain entry, AB42 binding, and macrophage-modulated complex clearance

## Source-to-Model Mapping
- `plan/strategy_neuroinflammation.md` supplied core motifs used in this module:
  - cytokine-amplified immune recruitment/entry
  - TNFA/IL6 production + first-order decay
  - Hill-type nonlinear inflammatory response term structure
- `peripheral_immune.json` contained sparse directly relevant values; mapped as:
  - `IC50` geometric mean `72.2115` -> `IC50_anti_inflam`
  - `EC50` geometric mean `461.5417` -> `EC50_anti_ab_bind`
  - `Hill_coefficient` geometric mean `4.0` -> `n_crp_il6`
  - `unspecified_parameter` geometric mean `60.0658 nM` -> `K_IL6_CRP`
- Elbert antimony references were used for naming and structure compatibility:
  - Plasma/BrainISF compartment naming patterns
  - anti-body transport and AB42-antibody interaction style

## Parameterization Notes
- Because extracted peripheral_immune parameters are sparse and partially indirect, most kinetic constants are explicit Tier-4 placeholders marked `assumed` or `estimated`.
- Concentration-form custom equations use `(species / V_compartment)` to match `custom_conc_per_time` semantics.
- Cytokine clearance constants follow strategy-consistent fast-turnover scales (`TNFA`) and intermediate turnover (`IL6`).

## Schema and Naming Compliance
- YAML structure follows `ModuleSpec` in `src/antimony_bootstrap/schema/module_spec.py`.
- Species naming follows `{entity}_{compartment}`.
- Constraint checks satisfied:
  - Requested compartments (`Plasma`, `BrainISF`) only
  - Reaction count in requested range (10-20)
  - Rate laws restricted to `MA` and `custom_conc_per_time`

## Assumptions
1. Monocyte infiltration and macrophage differentiation are represented as a single conversion flux (`MONOCYTE_Plasma -> MACROPHAGE_BrainISF`).
2. `AB42_BrainISF` is treated as a shared coupling species provided by amyloid modules.
3. Anti-AB therapy is represented by a continuous source term (`AntiAB_Antibody_Dose_Input`) rather than event-based dosing.
4. EC50/IC50 values extracted from generic records are reused as practical scaling constants, not definitive mechanism-specific affinities.

## Validation Status
- Ran:
  - `uv run antimony-bootstrap validate-module models/alzheimers/modules/peripheral_immune.yaml`
- Result:
  - `Valid: peripheral_immune (19 reactions, 30 parameters)`
