# neuroinflammation_microglia Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/neuroinflammation_microglia.yaml`
- Tier: 2
- Compartment scope: `Microglia`, `BrainISF`
- Reaction count: 43
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/neuroinflammation_microglia.json`
2. `plan/strategy_neuroinflammation.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module implements a two-compartment microglia-centered neuroinflammation network with required key species families:
- Microglial states: `MICROGLIA_resting`, `MICROGLIA_M1`, `MICROGLIA_M2`, `MICROGLIA_DAM`
- TREM2 axis: `TREM2`, `TREM2_active`, `SYK_inactive`, `SYK_active`, `CD33`
- Cytokines/trophic factors: `TNFA`, `IL1B`, `IL6`, `IL10`, `TGFB` (TGFbeta), `BDNF`
- Fractalkine axis: `CX3CL1`, `CX3CR1`
- Coupling sinks/inputs: `AB42_oligomer_BrainISF`, `AB_plaque_BrainISF`, `Debris_BrainISF`

Reaction groups included:
- Homeostasis and state occupancy: birth/turnover for resting/M1/M2/DAM
- State transitions: resting->M1, resting->M2, resting->DAM, DAM->M1, M1->M2, and resolution flows
- TREM2 signaling: activation/inactivation plus SYK activation/inactivation
- CD33 antagonism: suppressive routing from active TREM2 back to inactive TREM2
- Cytokine production and decay: TNFA/IL1B/IL6/IL10/TGFB/BDNF production + first-order degradation
- Fractalkine signaling: CX3CL1 and CX3CR1 turnover with CX3CL1/CX3CR1-driven M1->M2 conversion
- Phagocytosis/clearance: AB42 oligomer, plaque, and debris clearance with DAM/TREM2 weighting

## Source-to-Model Mapping
- Strategy document supplied the topology and rate-law motifs:
  - M0/M1/M2/DAM transitions
  - TREM2-dependent DAM behavior
  - cytokine positive/negative feedback loops
  - phagocytosis terms and anti-inflammatory resolution
- Module parameter JSON had sparse directly mappable numeric data (5 extracted entries):
  - `Hill_coefficient = 2` reused as `n_auto_TNFA`
  - TREM2-related concentration-scale entries used as guidance for nanomolar-scale midpoint constants
  - no directly reusable full kinetic set for all required reactions, so remaining constants are estimated/assumed placeholders
- Elbert reference was used for compatibility patterns (microglia state abstraction and clearance motifs), not for direct one-to-one neuroinflammation equations.

## Parameterization Notes
- All parameters are explicitly declared with `confidence` and `source` fields for traceability.
- Degradation constants for core cytokines follow the strategy's half-life table (converted to day^-1 values):
  - TNFA 33/day, IL1B 17/day, IL6 10/day, IL10 8/day, TGFB 5/day.
- Rate constants were selected to maintain Tier-2 dynamic responsiveness while avoiding stiff extreme values in baseline simulation.

## Schema and Naming Compliance
- YAML structure aligns with `ModuleSpec` fields in `src/antimony_bootstrap/schema/module_spec.py`.
- Species naming follows project convention `{species}_{compartment}`.
- Requested key species naming retained with compartment suffixes:
  - e.g., `MICROGLIA_M1_Microglia`, `TNFA_BrainISF`, `CX3CL1_BrainISF`.
- `TGFbeta` is represented as ASCII-safe `TGFB` in species/parameter naming.

## Assumptions
1. Tier-2 scope uses a lumped microglia compartment rather than DAM stage1/stage2 split.
2. AB42 oligomer/plaque are treated as external shared species for module coupling.
3. CD33 and CX3CR1 expression dynamics are included as local synthesis/degradation placeholders.
4. Several receptor and phagocytosis constants are calibration targets for later fitting.

## Validation Status
- Ran schema validation with `validate_module` CLI on the output YAML.
- Result: valid module with 43 reactions and 68 parameters.
