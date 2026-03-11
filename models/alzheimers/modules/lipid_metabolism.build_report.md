# lipid_metabolism Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/lipid_metabolism.yaml`
- Tier: 3
- Compartments: `Astrocyte`, `BrainISF`
- Reaction count: 28
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/lipid_metabolism.json`
2. `plan/strategy_lipid_apoe.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module implements astrocyte-centric lipid metabolism and ApoE lipoprotein dynamics with the requested key species represented as compartment-scoped entities:
- `CHOLESTEROL_Astrocyte`, `CHOLESTEROL_BrainISF`
- `24OHC_BrainISF`, `27OHC_BrainISF`
- `APOE_lipidated_BrainISF`, `HDL_brain_BrainISF`
- `ABCA1_Astrocyte`, `ABCG1_Astrocyte`
- `LXR_Astrocyte` + active state `LXR_active_Astrocyte`
- `SREBP2_Astrocyte`, `CYP46A1_Astrocyte`

Reaction groups included:
- Cholesterol synthesis, turnover, and Astrocyte/BrainISF exchange
- CYP46A1 synthesis/degradation and cholesterol-to-24OHC conversion
- 24OHC clearance and 27OHC ingress/clearance
- LXR activation/deactivation by oxysterols
- ABCA1 and ABCG1 basal + LXR-induced expression with turnover
- SREBP2 feedback activation by low cholesterol with turnover
- ApoE production/secretion/lipidation and HDL assembly/turnover

## Source-to-Model Mapping
- `strategy_lipid_apoe.md` provided the mechanistic template and parameter-scale guidance for:
  - cholesterol synthesis/efflux and CYP46A1-24OHC axis
  - 27OHC ingress and oxysterol-driven LXR activation
  - ABCA1/ABCG1 regulation and ApoE lipidation/HDL maturation
- `lipid_metabolism.json` contained one ApoE-related concentration estimate (`11.0668 nM`) and no direct named kinetic constants. This value was mapped to `Km_APOE_lipidation_chol` as a placeholder affinity scale (converted to mol amount scale used in this module).
- Elbert antimony reference files were searched for direct lipid/ApoE reaction blocks and parameter labels; no direct hits for `APOE/ABCA1/ABCG1/LXR/SREBP2/CYP46A1/24OHC/27OHC` were identified in sampled reaction/parameter files. Module therefore follows project schema and naming conventions while using strategy-driven structure.

## Parameterization Notes
- Most kinetic values are `estimated` or `assumed` placeholders due sparse extracted module parameter data.
- Rate equations use concentration forms (`amount / V_compartment`) for custom kinetics to align with `custom_conc_per_time` semantics.
- ApoE lipidation and HDL assembly are represented as saturable cholesterol-dependent steps modulated by transporter abundance.

## Schema and Naming Compliance
- YAML follows `ModuleSpec` fields in `src/antimony_bootstrap/schema/module_spec.py`.
- Species naming follows `{species}_{compartment}` and preserves requested key species roots.
- Requested reaction count range (20-30) is satisfied: 28 reactions.
- Only requested rate law types are used: `MA` and `custom_conc_per_time`.

## Assumptions
1. Module scope is restricted to `Astrocyte` and `BrainISF`, so neuron/plasma/BBB details are abstracted into ingress/clearance terms.
2. `LXR` is represented with inactive/active pools to enable explicit oxysterol-driven activation kinetics.
3. Single ApoE affinity datum from extraction is reused as a lipidation saturation placeholder due lack of direct transporter kinetic constants.
4. HDL-like particle dynamics are represented as a single `HDL_brain_BrainISF` pool.

## Validation Status
- Ran: `uv run antimony-bootstrap validate-module models/alzheimers/modules/lipid_metabolism.yaml`
- Result: valid module.
