# Build Report: `amyloid_clearance`

## Summary
- Created `models/alzheimers/modules/amyloid_clearance.yaml` as a complete Tier 1 `ModuleSpec`.
- Implemented **20 reactions** (within requested 15-25 range).
- Constrained compartments to:
  - `BrainISF`
  - `Microglia`
  - `Perivascular`
- Included required key species (compartment-resolved):
  - `AB42_BrainISF`, `AB40_BrainISF`
  - `IDE_BrainISF`, `NEP_BrainISF`, `MMP9_BrainISF`
  - `LRP1_Perivascular`
  - `microglia_phagocytic_Microglia`

## Inputs Used
- `data/parameters/module/amyloid_clearance.json`
- `plan/strategy_amyloid_cascade.md`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_3a_all_reactions.txt`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_3a_parameters.txt`
- `src/antimony_bootstrap/schema/module_spec.py`
- `models/alzheimers/modules/abeta_production.yaml`

## Implemented Mechanistic Blocks
1. **Enzymatic soluble Abeta degradation (IDE/NEP/MMP9)**:
   - AB42 and AB40 each have Michaelis-Menten reactions using `custom_conc_per_time`.
   - Enzyme activity scales with enzyme species amount relative to reference amount.
2. **Microglial clearance**:
   - Resting/phagocytic microglia state transition with Hill activation by AB42 burden.
   - Uptake reactions for AB42 and AB40 into microglia.
   - Intracellular lysosomal degradation sinks for internalized pools.
3. **ISF and perivascular flow clearance**:
   - ISF bulk transfer to perivascular compartment (AB42, AB40).
   - Perivascular drainage sink (AB42, AB40).
   - Additional lumped ISF bulk-clearance sink (AB42, AB40).
4. **LRP1-mediated perivascular efflux**:
   - Saturable export of AB42 and AB40 from perivascular compartment via LRP1.

## Rate Law Coverage
- `custom_conc_per_time`:
  - All enzyme-mediated degradation reactions (IDE, NEP, MMP9).
  - Microglia activation Hill term.
  - Microglial phagocytic uptake.
  - LRP1-mediated efflux.
- `MA`:
  - Microglia deactivation and lysosomal degradation.
  - ISF bulk flow and perivascular drainage terms.
  - Lumped ISF baseline clearance.

## Parameter Sourcing Notes
1. **Strategy-driven mechanistic form/range**:
   - IDE/NEP Michaelis-Menten forms and baseline ranges.
   - Perivascular drainage and bulk-flow structure.
   - LRP1 clearance pathway inclusion.
2. **Elbert-driven motifs**:
   - IDE-linked degradation constants and microglia-dependent clearance families.
   - First-order clearance-style reactions used as Tier-1 abstractions.
3. **Parameter extraction file (`amyloid_clearance.json`) usage**:
   - `degradation_rate` geometric mean (0.0261 1/hr) used as baseline `k_ISF_bulk_clear_AB42`.
   - `Hill_coefficient` (4.0) used in microglial activation Hill term.
   - `Km` signal informed submicromolar-to-micromolar activation/clearance scaling.

## Assumptions and Simplifications
- `MMP9` kinetics were included as requested but parameterized conservatively due sparse direct values in the provided extraction file.
- Microglial uptake is represented as transfer to intracellular pools followed by first-order lysosomal degradation (instead of explicit endosome/lysosome subcompartments).
- Perivascular route is modeled as a dedicated compartment to separate ISF outflow from downstream clearance.
- Units for microglia state species are modeled as `a.u.` and used as scaling states.

## Schema Compliance
- Top-level fields follow `ModuleSpec` (`name`, `description`, `mechanism`, `compartments`, `species`, `reactions`, `parameters`, `rules`, `evidence`, `notes`).
- Custom reactions include explicit `rate_equation` and declared `rate_parameters`.
- Parameter entries include `value`, `units`, `confidence`, and `source`.
