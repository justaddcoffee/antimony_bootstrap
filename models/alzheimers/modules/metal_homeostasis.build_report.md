# metal_homeostasis Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/metal_homeostasis.yaml`
- Tier: 3
- Compartments: `Neuron`, `BrainISF`
- Reaction count: 15
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/metal_homeostasis.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This Tier 3 module implements a compact metal dysregulation mechanism centered on copper, zinc, and iron handling with explicit AD-relevant coupling to AB42:
- Metal pools: `Cu_free`, `Zn_free`, `Fe2`, `Fe3` in neuron/ISF contexts
- Buffering/sequestration: `MT3`, `Cu_bound`, `Zn_bound`, `FERRITIN`, `TRANSFERRIN`
- Amyloid interactions: `APP_Cu`, `AB42_Cu`, `AB42_Zn`
- Oxidative/ferroptotic bridge: `Fe2_Fenton_Oxidation` generates `LipidROS_Neuron`, consumed by `Ferroptosis_Progression`

Reaction groups included:
- Metal import/export across `BrainISF <-> Neuron` for Cu and Zn
- Transferrin-modulated Fe3 uptake and ferritin-mediated Fe3 sequestration
- Fe3/Fe2 redox cycling with Fenton-like lipid ROS production
- Metallothionein (MT3) binding/release buffering for Cu and Zn
- APP-copper and AB42-metal complexation pathways

## Source-to-Model Mapping
- `plan/strategy_synaptic_neuronal.md` contributed the mechanistic requirements linking metal dysregulation to oxidative stress (Fenton chemistry; AB42-metal ROS amplification).
- `plan/strategy_module_decomposition.md` provided module scope constraints (Tier 3, 10-15 reactions, Neuron/BrainISF compartments).
- `data/parameters/module/metal_homeostasis.json` contained only a non-specific `unspecified_parameter` record and no reaction-mapped kinetic constants; therefore direct one-to-one parameter transfer was not possible.
- `../Elbert_Esguerra_model_v2026b/antimony_models/` was searched for ferritin/transferrin/copper/zinc/ferroptosis reaction templates; no direct metal-homeostasis reaction block was found, so this module was authored de novo using repository conventions.
- `src/antimony_bootstrap/schema/module_spec.py` constrained all field names and enum values; only supported `RateType` values were used.
- `models/alzheimers/modules/abeta_production.yaml` informed formatting, naming, and parameter metadata style.

## Assumptions
1. `AB42_BrainISF` is declared locally as a placeholder shared species for metal complexation; assembly-stage ownership should be reconciled with amyloid modules.
2. `Cu_bound_Neuron` and `Zn_bound_Neuron` are lumped MT3-bound pools rather than explicit multi-state MT3 species.
3. Ferritin and transferrin effects are represented as modulators in custom concentration-rate equations rather than explicit receptor/complex trafficking chains.
4. Ferroptosis is represented by a lipid ROS burden sink (`Ferroptosis_Progression`) to provide a coupling hook into neuronal death modules.
5. Parameter values are initialization defaults (`estimated`/`assumed`) intended for downstream calibration.

## Validation Status
- YAML structure and field names follow `ModuleSpec` schema.
- Requested reaction count constraint met: 15 reactions.
- Requested kinetics constraint met: only `MA` and `custom_conc_per_time` used.
- Expected biology covered: metal transport, MT3 buffering, AB42-metal complexation, Fe redox/Fenton chemistry, ferroptosis link.
