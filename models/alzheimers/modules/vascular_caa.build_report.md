# vascular_caa Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/vascular_caa.yaml`
- Tier: 3
- Compartments: `Perivascular`, `BrainParenchyma`
- Reaction count: 18
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/vascular_caa.json`
2. `plan/strategy_vascular_bbb.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This Tier 3 module implements cerebral amyloid angiopathy (CAA) progression with required key species:
- `AB40_perivascular`, `AB42_perivascular`
- `SMC`
- `COLLAGEN_IV`
- `PERIVASCULAR_drainage_rate`
- `CAA_severity`

Mechanistic blocks encoded:
- Brain parenchyma to perivascular AB40/AB42 transfer
- Perivascular drainage-dependent AB40/AB42 clearance
- Saturable perivascular deposition into `AB40_CAA_deposit` and `AB42_CAA_deposit`
- Smooth muscle cell (SMC) repair/loss under CAA burden
- Collagen-IV vessel-wall remodeling under CAA severity
- Dynamic drainage recovery vs CAA-driven impairment
- CAA severity integration and resolution
- Downstream microhemorrhage risk escalation and decay

## Source-to-Model Mapping
- `vascular_caa.json` contained one non-mechanistic infusion-duration value (`unspecified_parameter`, `21 h`) that does not map to CAA kinetics; it was not used directly.
- `strategy_vascular_bbb.md` supplied the CAA core structure and parameter ranges:
  - `k_CAA_deposit` in `0.001-0.01 1/hr`
  - `CAA_capacity` in `100-1000 nmol`
  - `k_PVS_drain_baseline` in `0.05-0.2 1/hr`
  - CAA-driven drainage impairment scaling (`alpha_CAA` concept)
- Elbert references informed style compatibility (flow and concentration-normalized transport/deposition patterns, compartment naming discipline, and first-order exchange motifs) rather than direct CAA reaction reuse.

## Parameterization Notes
- Most parameters are `estimated` or `assumed` placeholders for later calibration.
- Strategy-anchored values:
  - `k_CAA_deposit_AB40 = 0.008 1/hr`, `k_CAA_deposit_AB42 = 0.005 1/hr`
  - `k_AB40_pv_drain_base = 0.10 1/hr`, `k_AB42_pv_drain_base = 0.08 1/hr`
  - `CAA_capacity_AB40 = 4.0e-7 mol`, `CAA_capacity_AB42 = 2.0e-7 mol`
  - `alpha_COLLAGEN_CAA = 0.7`
- Added normalized reference constants (`SMC_ref`, `DRAIN_ref`, `CAA_ref`, `CAA_load_ref`, `COLLAGEN_ref`) to stabilize custom concentration-rate forms.

## Assumptions
1. `PERIVASCULAR_drainage_rate`, `CAA_severity`, and `MICROHEMORRHAGE_risk` are represented as normalized state variables (`arb`).
2. AB40 and AB42 perivascular pools are modeled explicitly; upstream APP processing is out-of-scope and represented as transfer from `BrainParenchyma` pools.
3. Vessel wall remodeling is represented by a single collagen-IV state, without explicit elastin/MMP substructure.
4. Microhemorrhage risk is a phenomenologic hazard state downstream of CAA severity, SMC depletion, and wall remodeling.

## Validation Status
- YAML structure and enum values follow `ModuleSpec` in `src/antimony_bootstrap/schema/module_spec.py`.
- Rate law constraint satisfied: only `MA` and `custom_conc_per_time` used.
- Reaction count constraint satisfied: 18 reactions (requested range 10-20).
