# bbb_integrity Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/bbb_integrity.yaml`
- Tier: 3
- Compartments: `BBB`, `BrainISF`, `Plasma`
- Reaction count: 24
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/bbb_integrity.json`
2. `plan/strategy_vascular_bbb.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This Tier 3 module implements BBB structural failure dynamics with the required key species:
- `TJ_CLAUDIN5_BBB`, `TJ_OCCLUDIN_BBB`, `TJ_ZO1_BBB`
- `PERICYTE_BBB`
- `MMP2_BrainISF`, `MMP9_BrainISF`
- `PDGFRB_BBB`, `PDGFRB_active_BBB`
- `VEGF_Plasma`, `VEGF_BrainISF`
- `BBB_permeability_BBB`

Mechanistic blocks encoded:
- Tight-junction synthesis + basal degradation for claudin-5, occludin, ZO-1
- MMP2/MMP9-driven junction degradation terms
- PDGFRB-dependent pericyte maintenance with basal and MMP9-induced pericyte loss
- VEGF production/clearance and permeability-coupled VEGF transport from plasma to brain ISF
- Dynamic permeability drift/increase (MMP + VEGF) opposed by TJ/pericyte-mediated repair

## Source-to-Model Mapping
- `bbb_integrity.json` contained no module-specific parameter values (`parameter_count: 0`), so no direct quantitative transfer was possible.
- `strategy_vascular_bbb.md` supplied the dominant biology and target rate-law style:
  - Tight-junction turnover and MMP degradation
  - Pericyte loss and PDGFRB maintenance axis
  - VEGF and permeability coupling
  - Dynamic BBB permeability variable with repair/degradation balance
- Elbert references were used for compatibility conventions (BBB compartment naming, concentration-based transport/degradation expression patterns) rather than direct reaction reuse.

## Parameterization Notes
- Parameters are initialized as `estimated` or `assumed` placeholders for calibration.
- Values are anchored to strategy ranges where present:
  - TJ basal degradation near `0.03 1/hr`
  - MMP-dependent permeability increase scale near `0.1 1/(nM*hr)`
  - Pericyte basal loss near `0.001 1/hr`
- Additional normalization constants (`Pericyte_ref`, `TJ_total_ref`, `BBBperm_ref`) were added to stabilize custom concentration-rate terms and keep equations dimensionally interpretable.

## Assumptions
1. `BBB_permeability_BBB` is represented as a normalized state variable (`arb`) where baseline is `1.0`.
2. PDGFRB signaling is represented with a minimal active/inactive receptor cycle; explicit PDGFB ligand dynamics are collapsed.
3. VEGF signaling stress is represented through VEGF-driven MMP9 upregulation and direct permeability gain.
4. MMP2 and MMP9 are local BBB-impacting pools in `BrainISF`; upstream inflammatory drivers are not explicitly modeled in this module.

## Validation Status
- YAML structure and enum values follow `ModuleSpec` in `src/antimony_bootstrap/schema/module_spec.py`.
- Rate law constraint satisfied: only `MA` and `custom_conc_per_time` used.
- Reaction count constraint satisfied: 24 reactions (requested range 15-25).
