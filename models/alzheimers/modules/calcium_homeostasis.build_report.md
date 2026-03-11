# calcium_homeostasis Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/calcium_homeostasis.yaml`
- Tier: 2
- Compartments: `Neuron`, `ER`, `Mitochondria`
- Reaction count: 22
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/calcium_homeostasis.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
This module implements calcium homeostasis / dysregulation dynamics centered on three intracellular compartments and the requested key molecular actors:
- Calcium pools: `Ca_cytosol_Neuron`, `Ca_ER_ER`, `Ca_mito_Mitochondria`
- ER channels/pumps: `IP3R`, `RyR`, `SERCA`
- Mito/plasma transporters: `MCU`, `PMCA`
- Buffer and phosphatase signaling: `CALBINDIN`, `CALCINEURIN`

Mechanistic groups:
- ER calcium channel gating (`IP3R_Opening/Closing`, `RyR_Opening/Closing`)
- ER release and refill (`ER_Ca_Release_via_IP3R`, `ER_Ca_Release_via_RyR`, `SERCA_Uptake`, `ER_Ca_Leak_to_Cytosol`)
- Mitochondrial uptake/release (`MCU_Uptake`, `Mito_Ca_Release_NCLX`)
- Plasma membrane extrusion (`PMCA_Extrusion`)
- Cytosolic buffering (`CALBINDIN_Ca_Binding`, `CALBINDIN_Ca_Unbinding`)
- Calcium-dependent effector activation (`CALCINEURIN_Activation_by_Ca`, `CALCINEURIN_Deactivation`)
- Homeostatic protein turnover for SERCA/MCU/PMCA

## Source-to-Model Mapping
- Strategy document (`calcium dysregulation` section) provided the core reaction template and nominal parameter scales for:
  - IP3R/RyR-mediated ER release
  - SERCA, MCU, PMCA Hill/Michaelis-style fluxes
  - NCLX-mediated mitochondrial efflux
  - calcineurin as downstream calcium effector
- Parameter JSON (`data/parameters/module/calcium_homeostasis.json`) contained two extracted `unspecified_parameter` records (generic calcium concentration/rate context and an NMDA-linked value) but no direct named kinetic constants for IP3R/RyR/SERCA/MCU/PMCA. These were treated as contextual evidence rather than one-to-one parameter assignments.
- Elbert reference antimony files were searched for explicit IP3R/RyR/SERCA/MCU/PMCA calcium-homeostasis reaction templates; no direct calcium-homeostasis block with these entities was identified. The module therefore follows antimony_bootstrap schema conventions and project naming patterns.

## Parameterization Notes
- Hill kinetics were used for channel/pump activation as requested:
  - `IP3R_Opening`, `RyR_Opening` (cooperative Ca-dependent opening)
  - `SERCA_Uptake`, `MCU_Uptake` (cooperative uptake)
  - `PMCA_Extrusion` (saturable Michaelis form)
  - `CALCINEURIN_Activation_by_Ca` (cooperative Ca-dependent activation)
- Strategy-scale constants were represented in `mol/L` and `mol/L/hr` with species in `mol`, consistent with existing modules.
- Transporter/channel abundances are dynamic via synthesis/turnover terms to support chronic AD-state perturbation studies.

## Assumptions
1. A basal cytosolic calcium ingress term (`Ca_Basal_Influx`) is included to maintain non-zero calcium in isolation.
2. IP3R and RyR are modeled with explicit open/closed pools to permit Hill-style gating without algebraic rules.
3. NCLX is represented as a first-order mitochondrial calcium release term (`k_nclx`) without explicit sodium coupling.
4. Generic calcium values from parameter JSON are not directly mapped because records are unnamed and not reaction-specific.

## Validation Status
- YAML structure is aligned to `ModuleSpec` fields and supported `RateType` enums.
- Reaction count satisfies requested range (15-25): 22.
- Required compartments and key species families are present.
- Recommended follow-up checks:
  - `just validate-module models/alzheimers/modules/calcium_homeostasis.yaml`
  - `just assemble`
  - dynamic perturbation checks under elevated ER leak / reduced SERCA conditions
