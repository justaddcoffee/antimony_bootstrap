# synaptic_dysfunction Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/synaptic_dysfunction.yaml`
- Tier: 2
- Compartments: `Synapse`, `Neuron`
- Reaction count: 30
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/synaptic_dysfunction.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
The module implements synaptic dysfunction in two compartments with explicit coupling between:
- AB42 oligomer burden (`AB42o_Synapse`)
- BDNF-TrkB-CREB-ARC trophic signaling
- AMPAR/NMDAR receptor homeostasis and AMPAR endocytosis/recycling
- LTP/LTD state dynamics
- Structural synapse density (`SYNAPSE_density_Synapse`) loss and recovery

Requested key species were included directly:
- `SYNAPSE_density`, `PSD95`, `AMPAR`, `NMDAR`, `BDNF`, `TrkB`, `glutamate_syn`, `CREB`, `ARC`, `LTP`, `LTD`
(encoded with compartment suffixes per schema naming rules).

## Source-to-Model Mapping
- Strategy document provided the mechanistic template and nominal values for:
  - LTP/LTD rates (`k_ltp`, `k_ltd`, decay terms)
  - AMPAR trafficking rates (`k_ampar_endo`, `k_ampar_recycle`)
  - Synapse elimination/recovery scales (`k_synapse_elim`, `k_synapse_recover`)
  - Glutamate/NMDAR cooperative activation structure
- Parameter JSON had one transferable synaptic concentration-scale datum (geometric mean 4.384272591292935 nM), mapped to:
  - `K_AB42_synaptotoxic`
  - `K_AB42_PSD95`
  - `K_AB42_AMPAR_endo`
  - `K_AB42_NMDAR_int`
  - `K_AB42_calcineurin`
  - `K_AB42_LTD`
- Elbert reference antimony files were checked for direct synaptic receptor/plasticity templates. No direct PSD95/AMPAR/NMDAR/CREB/ARC synaptic block was found, so implementation follows project ModuleSpec conventions with Elbert-compatible naming and kinetics.

## Assumptions
1. This module owns a local `AB42o_Synapse` pool via input/clearance reactions for standalone completeness; in integrated assembly this can be bridged to amyloid modules.
2. Capacity terms (e.g., `LTP_capacity`, `SYNAPSE_capacity`) are included to bound state variables and prevent unphysical growth.
3. Concentration-scale units are represented as `nM` for half-saturation constants, while species are amount-based (`mol`) under ModuleSpec conventions.
4. Non-JSON parameters were initialized from strategy values or mechanistic scaling assumptions and marked `estimated`/`assumed`.

## Validation Status
- YAML is schema-aligned with `ModuleSpec` field names and supported `RateType` enums.
- Reaction count and kinetics match requested constraints:
  - 30 reactions (within requested 20-30)
  - Includes LTP/LTD, BDNF-TrkB signaling, AMPAR trafficking, synapse elimination, CREB activation
  - Uses only `MA` and `custom_conc_per_time`
- Recommended follow-up:
  - `just validate-module models/alzheimers/modules/synaptic_dysfunction.yaml`
  - `just assemble`
  - dynamic sanity checks under elevated `AB42o_Synapse`
