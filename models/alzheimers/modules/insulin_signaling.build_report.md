# insulin_signaling Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/insulin_signaling.yaml`
- Tier: 3
- Compartment scope: `Neuron`
- Reaction count: 22
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/insulin_signaling.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module implements the neuronal insulin-signaling cascade with explicit state transitions for:
- `INSULIN`, `IR`, `IRS1`, `PI3K`, `AKT`, `GSK3B`, `mTOR`, `FOXO`, `IDE`
- all represented as compartment-suffixed species in `Neuron`

Reaction groups included:
- Insulin supply/clearance and receptor activation (`Insulin_Input`, `Insulin_Clearance`, `IR_Activation_by_Insulin`, `IR_Deactivation`)
- IRS1 switching and feedback (`IRS1_Tyrosine_Phosphorylation_by_IR`, `IRS1_Serine_Phosphorylation_by_mTOR`, recovery reactions)
- PI3K/AKT activation/inactivation
- AKT control of `GSK3B`, `mTOR`, and `FOXO`
- IDE regulation and functional output (`IDE_Synthesis_by_AKT_FOXO`, `AB42_Degradation_by_IDE`)

## Source-to-Model Mapping
- `insulin_signaling.json` provided sparse but usable priors:
  - geometric concentration scale `340.9625290150061` (standardized to `nM`) mapped to key half-saturation constants (`K_INSULIN_IR`, `K_IRS1_PI3K`, `K_PI3K_AKT`, `K_FOXO_IDE`, `Km_ide_ab42`)
  - 12 h timescale mapped to first-order turnover defaults (`k_insulin_clear`, `k_ide_deg` as `ln2/12 h^-1`)
- `strategy_synaptic_neuronal.md` supplied neuronal compartment convention and `V_Neuron = 0.0005 L`.
- Elbert antimony references were inspected for insulin-specific blocks; no direct neuronal insulin cascade was present, but IDE clearance motifs informed `AB42_Degradation_by_IDE` form.

## Assumptions
1. Insulin and AB42 have local source terms in this module for standalone closure; integrated assembly can replace these with cross-module couplings.
2. Activity-state pairs (active/inactive) are used for `IR`, `PI3K`, `AKT`, `GSK3B`, `mTOR`, `FOXO` to keep mass-conserving toggles explicit.
3. `IRS1_pS` represents inhibitory serine phosphorylation (insulin-resistance feedback branch via `mTOR_active`).
4. IDE expression is represented as AKT-enhanced and FOXO-suppressed effective synthesis; this is a compact phenomenological approximation.

## Validation Status
- YAML fields and enums align with `ModuleSpec` schema (`RateType`: `MA`, `custom_conc_per_time`).
- Reaction count and requested pathway coverage are satisfied.
- Recommended follow-up checks:
  - `just validate-module models/alzheimers/modules/insulin_signaling.yaml`
  - `just assemble`
  - dynamic sanity sweep under insulin-low and insulin-resistant (`k_irs1_ps` high) scenarios
