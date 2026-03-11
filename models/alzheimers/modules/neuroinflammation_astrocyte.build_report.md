# neuroinflammation_astrocyte Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/neuroinflammation_astrocyte.yaml`
- Tier: 2
- Compartment scope: `Astrocyte`, `BrainISF`
- Reaction count: 30
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/neuroinflammation_astrocyte.json`
2. `plan/strategy_neuroinflammation.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module implements a two-compartment astrocyte-focused neuroinflammation network with required key species:
- Astrocyte states: `ASTROCYTE_resting_Astrocyte`, `ASTROCYTE_A1_Astrocyte`, `ASTROCYTE_A2_Astrocyte`
- Astrocyte effectors: `GFAP_Astrocyte`, `S100B_Astrocyte`, `AQP4_Astrocyte`, `EAAT2_Astrocyte`
- Neurotransmitter and secreted signal: `glutamate_BrainISF`, `S100B_BrainISF`
- Coupling species for composition: `TNFA_BrainISF`, `IL1B_BrainISF`, `C1Q_BrainISF`, `IL10_BrainISF`, `TGFB_BrainISF`, `AB42_BrainISF`

Reaction groups included:
- Astrocyte state occupancy and turnover (resting/A1/A2 birth-turnover-resolution)
- Cytokine-driven polarization (`TNFA + IL1B + C1Q` for A1, `IL10 + TGFB` for A2)
- GFAP baseline synthesis, A1 upregulation, and degradation
- EAAT2 homeostasis and A1/A2 modulation
- Glutamate release (A1), saturable EAAT2-mediated uptake, and bulk clearance
- S100B synthesis/secretion/degradation with feedback-driven A1 polarization
- AQP4 maintenance under A1/A2 influence
- AQP4-dependent glymphatic AB42 clearance
- S100B-AB42 binding/unbinding and complex clearance closure

## Source-to-Model Mapping
- `strategy_neuroinflammation.md` supplied:
  - A0/A1/A2 conceptual astrocyte state transitions
  - combinatorial pro-inflammatory activation motif (TNFA/IL1B/C1Q)
  - glutamate uptake as a saturable process affected by astrocyte state
- `neuroinflammation_astrocyte.json` supplied sparse directly reusable parameter values:
  - `Ki` geometric mean used for `Ki_S100B_feedback`
  - `Kd` geometric mean used indirectly through `k_off_S100B_AB42 = Kd * k_on_S100B_AB42`
- Elbert reference supplied compatibility-scale guidance:
  - `Q_glymph` value used as the scale for `k_glymph_AB42`

## Parameterization Notes
- Parameters were declared with explicit `confidence` and `source`.
- Most kinetic values are estimated or assumed placeholders because the module-specific extraction file contained only affinity-type values (`Ki`, `Kd`) and not a full kinetic set.
- Glymphatic clearance rate scale is aligned to Elbert `Q_glymph` order of magnitude and modulated by normalized `AQP4_Astrocyte`.

## Schema and Naming Compliance
- YAML structure follows `ModuleSpec` in `src/antimony_bootstrap/schema/module_spec.py`.
- Species naming follows project convention `{species}_{compartment}`.
- Requested key species names are preserved with compartment suffixes.
- Only requested rate law types are used: `MA` and `custom_conc_per_time`.

## Assumptions
1. Astrocyte dynamics are represented as lumped state populations in a single `Astrocyte` compartment.
2. Cytokines (`TNFA`, `IL1B`, `C1Q`, `IL10`, `TGFB`) and `AB42_BrainISF` are shared interface species for module composition.
3. S100B signaling is represented as both phenotype feedback and AB42-binding sink modulation.
4. AQP4 influence is represented as a multiplicative gain on AB42 glymphatic clearance.

## Validation Status
- Ran `uv run antimony-bootstrap validate-module models/alzheimers/modules/neuroinflammation_astrocyte.yaml`.
- Result: valid module.
