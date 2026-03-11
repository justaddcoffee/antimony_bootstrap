# apoptosis Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/apoptosis.yaml`
- Tier: 2
- Compartments: `Neuron`
- Reaction count: 20
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/apoptosis.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module implements intrinsic neuronal apoptosis centered on the requested key species set:
- Core apoptosis signaling: `BAX`, `BCL2`, `CYTO_C`, `APAF1`, `CASP9`, `CASP3`
- BH3 modulators: `BID`, `BAD`
- Execution/viability readouts: `PARP`, `PARP_CLEAVED`, `NEURON_count`
- Parallel mitochondrial death effector: `AIF`

Mechanistic groups:
- BH3/BCL2 control of BAX activation (`BAX_Activation_by_BID_BAD`, `BAX_Inhibition_by_BCL2`)
- Mitochondrial permeabilization outputs (`CYTO_C_Release`, `AIF_Release`)
- Apoptosome and caspase cascade (`Apoptosome_Formation`, `CASP9_Activation`, `CASP3_Activation`)
- Execution phase (`PARP_Cleavage_by_CASP3`)
- Neuronal population decline (`Neuronal_Loss_via_CASP3`, `Neuronal_Loss_via_AIF`)

## Source-to-Model Mapping
- Strategy document (`neuronal_death` section) provided reaction topology targets and nominal timescale constants (`k_apopto`, `k_casp9`, `k_casp3`, `k_apoptosis`) used to initialize caspase and neuron-loss parameter scales.
- Parameter JSON (`data/parameters/module/apoptosis.json`) contained one generic cell-death concentration record (geometric mean 1378.7157 uM). It was mapped to `K_apoptosis_trigger` after unit conversion to `1.3787157053417275e-3 mol/L`.
- Elbert antimony reference set was scanned for direct intrinsic apoptosis species/reactions (`CASP*`, `BAX`, `BCL2`, `APAF1`, `PARP`, `AIF`); no explicit block was identified. The module therefore uses project schema conventions and strategy-driven construction.

## Parameterization Notes
- Mass-action kinetics were used for binding, turnover, and population-loss reactions.
- `custom_conc_per_time` was used where concentration-based modulation is biologically important:
  - `CYTO_C_Release` (BAX/BCL2 stress ratio)
  - `AIF_Release` (BAX-saturable release)
  - `CASP3_Activation` (CASP9 flux with AIF-dependent gain)
- `K_apoptosis_trigger` is the only directly data-derived constant from the apoptosis JSON input; all other constants are estimated/assumed and intended for calibration.

## Assumptions
1. `NEURON_count` is a normalized viability state variable (dimensionless-like `cell_equivalent`) represented as a species in `Neuron` for ODE coupling.
2. `APAF1` is modeled as a recyclable scaffold via apoptosome assembly/disassembly rather than synthesis/degradation in this module.
3. Mitochondrial pools are not explicitly represented; `CYTO_C` and `AIF` release terms are effective fluxes driven by BAX/BCL2 balance.
4. Parallel neuron-loss channels (CASP3- and AIF-mediated) are included to capture caspase-dependent and caspase-independent apoptosis contributions.

## Validation Status
- YAML structure follows `ModuleSpec` schema fields and supported `RateType` enum values.
- Reaction count is within the requested range (10-20): 20.
- Recommended follow-up checks:
  - `just validate-module models/alzheimers/modules/apoptosis.yaml`
  - `just assemble`
  - perturbation tests: increase `BAX` or decrease `BCL2` and verify monotonic increase in `CASP3` and decline in `NEURON_count`
