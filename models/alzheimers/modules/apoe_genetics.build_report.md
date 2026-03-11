# apoe_genetics Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/apoe_genetics.yaml`
- Tier: 4
- Compartments: `BrainISF`
- Reaction count: 10
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/apoe_genetics.json`
2. `plan/strategy_lipid_apoe.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module is implemented as a Tier 4 genotype-modifier layer centered on APOE isoform composition in `BrainISF`.

Key species included per request:
- `APOE2_BrainISF`
- `APOE3_BrainISF`
- `APOE4_BrainISF`
- `APOE_total_BrainISF`
- `APOE_lipidated_BrainISF`
- `LDLR_BrainISF`
- `LRP1_APOE_BrainISF`

Reaction groups implemented:
- Genotype-specific APOE isoform production (`APOE2/3/4`)
- APOE total formation + turnover
- APOE lipidation with isoform-weighted efficiency modifier
- APOE-lipoprotein receptor complex formation/unbinding
- LRP1-associated APOE complex clearance with AB-clearance-linked scaling

Cross-module modifier outputs are exposed as assignment rules:
- `mod_APOE_lipidation_eff`
- `mod_APOE_receptor_affinity`
- `mod_APOE_AB_clearance`

These are explicitly isoform-fraction weighted and can be consumed by other modules to scale clearance and transport terms.

## Source-to-Model Mapping
- `strategy_lipid_apoe.md` drove the core genotype scaling assumptions:
  - ApoE4 lower lipidation efficiency (~0.5x)
  - ApoE4 reduced receptor-linked handling (~0.5x)
  - ApoE4 reduced AB clearance (~0.5x)
  - ApoE2 protective upward scaling (~1.25-1.30x)
- `apoe_genetics.json` includes sparse extracted values (`IC50`, `KI`, and unspecified concentration values) without direct APOE production/lipidation kinetic constants suitable for direct ODE reaction mapping; therefore constants are strategy-anchored placeholders with confidence flagged `estimated`/`assumed`.
- Elbert reference files were scanned for direct APOE/ABCA1/ABCG1 reaction motifs and APOE-specific kinetic labels. No clean APOE reaction block was identified in the provided antimony files, so this module follows local schema conventions and strategy-driven structure.

## Parameterization Notes
- `sf_APOE4_AB_clearance = 0.50` encodes the required ~50% reduction in AB clearance under APOE4-dominant composition.
- Isoform fraction rules (`frac_APOE2/3/4`) use `eps_APOE_pool` for numerical safety.
- All custom rates are concentration-form equations (`amount / V_BrainISF`) to match `custom_conc_per_time` semantics.

## Schema and Naming Compliance
- YAML conforms to `ModuleSpec` in `src/antimony_bootstrap/schema/module_spec.py`.
- Species naming follows `{entity}_{compartment}`.
- Requested constraints satisfied:
  - Tier 4 metadata included
  - Compartment constrained to `BrainISF`
  - Reaction count in requested range (5-15)
  - Rate law types constrained to `MA` and `custom_conc_per_time`

## Assumptions
1. This module is a modifier-focused abstraction and does not attempt full APOE trafficking across cellular compartments.
2. `LDLR_BrainISF` is used as a lumped receptor pool participating in an effective `LRP1_APOE` complex term.
3. APOE isoform production rates are represented independently to allow genotype emulation by parameter edits.
4. `APOE_total_BrainISF` is retained as an explicit state for compatibility with downstream modules expecting a pooled APOE term.

## Validation Status
- Ran: `uv run antimony-bootstrap validate-module models/alzheimers/modules/apoe_genetics.yaml`
- Result: `Valid: apoe_genetics (10 reactions, 20 parameters)`
