# Build Report: `amyloid_production`

## Summary
- Created `models/alzheimers/modules/amyloid_production.yaml` as a complete `ModuleSpec` for the Alzheimer's amyloid production module.
- Implemented **21 reactions** (within requested 15-25 range).
- Included required species set with Elbert-style compartment suffixes:
  - `APP_Neuron`, `BACE1_Neuron`, `GAMMA_SECRETASE_Neuron`
  - `sAPPalpha_BrainISF`, `sAPPbeta_BrainISF`
  - `C83_Neuron`, `C99_Neuron`, `CTFalpha_Neuron`, `CTFbeta_Neuron`
  - `AB40_BrainISF`, `AB42_BrainISF`, `AICD_Neuron`

## Inputs Used
- `data/parameters/module/amyloid_production.json`
- `plan/strategy_amyloid_cascade.md`
- `../Elbert_Esguerra_model_v2026b/antimony_models/1a.txt`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_1a_all_reactions.txt`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_elbert_Esguerra_1a_parameters.txt`
- `src/antimony_bootstrap/schema/module_spec.py`
- `models/alzheimers/modules/abeta_production.yaml`

## Parameter Sourcing Priority Applied
1. **Elbert reference model**: Used for primary APP/CTF/gamma-cleavage kinetics and constants (`k_APP`, `Vm_*`, `Km_*`, `k_gammasec_*`, `IDE_Kcat_ISF_*`).
2. **Extracted strategy/literature context**: Used for module structure and compartment mapping rationale.
3. **Steady-state estimates**: Used where Elbert does not provide direct values (enzyme synthesis/degradation placeholders, alias interconversion, some degradation sinks).

## Mapping Notes
- Elbert reactions implemented in `BrainISF` and `EndoLysNeuron` were condensed into a module with requested compartments `Neuron` and `BrainISF`.
- Saturable cleavage rate-law forms were preserved (custom `custom_conc_per_time`) and mapped to `*_Neuron` species.
- Added explicit enzyme states (`BACE1_Neuron`, `GAMMA_SECRETASE_Neuron`) as requested key species; they scale beta/gamma cleavage fluxes via normalization parameters.

## Schema Compliance Notes
- Used exact `ModuleSpec` top-level keys: `name`, `description`, `mechanism`, `notes`, `compartments`, `species`, `reactions`, `parameters`, `evidence`.
- Every reaction includes:
  - `name`, `reactants`, `products`, `rate_type`, `rate_parameters`
  - `rate_equation` for all `custom_conc_per_time` reactions
  - non-empty `evidence` and `rate_law_evidence` lists with `supports`
- Every parameter includes:
  - `name`, `value`, `units`, `confidence`, `source`, `evidence`
- Every species has `initial_amount` and `units`.

## Caveats
- `CTFalpha`/`C83` and `CTFbeta`/`C99` are represented as linked aliases to satisfy required species inventory while maintaining mechanistic continuity.
- Several degradation/synthesis placeholders are steady-state assumptions and should be replaced if curated measurements become available.
