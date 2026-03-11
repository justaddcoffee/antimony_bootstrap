# Build Report: `amyloid_aggregation`

## Summary
- Created `models/alzheimers/modules/amyloid_aggregation.yaml` as a complete Tier 1 `ModuleSpec`.
- Implemented **32 reactions** (within requested 20-40 range).
- Included requested compartments:
  - `BrainISF`
  - `BrainParenchyma`
- Included requested key species (with Elbert-style compartment suffixes):
  - `AB42_monomer_BrainISF`, `AB42_oligomer_BrainISF`, `AB42_protofibril_BrainISF`, `AB42_fibril_BrainISF`
  - `AB40_monomer_BrainISF`, `AB40_oligomer_BrainISF`, `AB40_protofibril_BrainISF`, `AB40_fibril_BrainISF`
  - `AB_plaque_BrainParenchyma`

## Inputs Used
- `data/parameters/module/amyloid_aggregation.json`
- `plan/strategy_amyloid_cascade.md`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_noSILK_1c_all_reactions.txt`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_noSILK_1c_parameters.txt`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_noSILK_1h_parameters.txt`
- `src/antimony_bootstrap/schema/module_spec.py`
- `models/alzheimers/modules/abeta_production.yaml`

## Kinetic Coverage
- Primary nucleation (AB42 and AB40): `custom_conc_per_time` with power-law monomer terms.
- Secondary nucleation (AB42 and AB40): `custom_conc_per_time` with monomer-power and fibril-catalysis terms (Knowles/Cohen structure).
- Elongation and maturation:
  - Oligomer to protofibril conversion
  - Monomer-driven fibril mass increase
  - Fragmentation and depolymerization
- Plaque dynamics:
  - Fibril to plaque deposition from AB42 and AB40
  - Cooperative protofibril plaque nucleation
  - Plaque clearance and low-rate resolubilization

## Parameter Sourcing Priority Applied
1. **Elbert reference model parameters** (highest priority):
   - `k_oligo1_AB42`, `k_oligo2_AB42`, `k_c_AB42`, `k_plus_AB42`, `k_off_AB42`
   - `k_oligo1_AB40`, `k_oligo2_AB40`, `k_c_AB40`, `k_plus_AB40`, `k_off_AB40`
   - `k_d1_Oligomer_*`, `k_d2_Oligomer_*`, `IDE_Kcat_ISF_AB*_Oligomer`
2. **Strategy/Literature-based values and forms**:
   - Knowles/Cohen nucleation-polymerization rate-law structure
   - Plaque deposition/clearance ranges
3. **Tier-1 assumed closures**:
   - Protofibril reversible rates
   - Cross-seeding terms
   - Lumped fibril/protofibril clearance and plaque shedding

## Notes on `data/parameters/module/amyloid_aggregation.json`
- The extracted JSON is highly noisy for mechanistic aggregation constants (many entries are generic assay metrics like EC50/Kd and mixed-context values).
- It was used as supporting context only; mechanistically specific Elbert and strategy constants were prioritized.

## Schema Compliance Notes
- File conforms to `ModuleSpec` shape:
  - top-level keys: `name`, `description`, `mechanism`, `notes`, `compartments`, `species`, `reactions`, `parameters`, `rules`, `evidence`
- All reactions include `rate_type`, `rate_parameters`, and for custom types a `rate_equation`.
- Parameters include `value`, `units`, `confidence`, and `source`.

## Caveats
- A fully mass-conserving fibril-number/fibril-mass pair (as in the full Elbert model) was simplified to a Tier-1 tractable species set.
- Some terms are assumptions added for numerical closure and bidirectional flow between aggregate states; these should be revisited during calibration.
