# Build Report: `amyloid_transport`

## Summary
- Created `models/alzheimers/modules/amyloid_transport.yaml` as a complete ModuleSpec for Tier 1 amyloid vascular/BBB transport.
- Implemented **26 reactions** (within requested 20-30 range).
- Included required compartments:
  - `BrainISF`, `CSF`, `Plasma`, `BBB`
- Included required key species families in each compartment:
  - `AB40_*`, `AB42_*`, `LRP1_*`, `RAGE_*`, `P_gp_*`, `sLRP1_*`

## Inputs Used
- `data/parameters/module/amyloid_transport.json`
- `plan/strategy_vascular_bbb.md`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_1h_parameters.txt`
- `../Elbert_Esguerra_model_v2026b/antimony_models/Antimony_Elbert_Esguerra_1h_all_reactions.txt`
- `src/antimony_bootstrap/schema/module_spec.py`
- `models/alzheimers/modules/abeta_production.yaml`

## Parameter Sourcing Priority Applied
1. **Elbert reference model (highest priority)**:
   - `K_BBB_transport = 1e-1`
   - `Q_CSF = 0.024`
   - `Kdeg_AB40 = 7.002601312955259`
   - `Kdeg_AB42 = 10.236480516894925`
2. **Strategy/literature guidance**:
   - LRP1 and RAGE transporter kinetics framed as Michaelis-Menten.
   - BBB conceptual compartment volume (`V_BBB ~ 0.002 L`).
   - CSF bulk-flow structure and receptor turnover motifs.
3. **Estimated/assumed placeholders**:
   - Receptor scaling constants, passive exchange rates, transcytosis release rates.
   - Plasma sLRP1 scavenging constants.

## Mapping Notes
- Preserved Elbert naming style `{species}_{compartment}` and reused Elbert transport motifs:
  - BBB export terms (modeled via `LRP1Efflux_*`, `Passive_*`, and release steps)
  - CSF convective outflow approximations (`BulkFlow_*`)
  - Peripheral first-order plasma degradation (`PlasmaClearance_*`)
- Added explicit BBB transit pool (`AB40_BBB`, `AB42_BBB`) to separate receptor loading/unloading from net compartment transfer.
- Included receptor homeostasis closure (`LRP1Synthesis/Degradation`, `RAGESynthesis/Degradation`) to avoid static receptor assumptions at Tier 1.

## Rate Law Coverage
- `MA`: production/degradation sinks and receptor homeostasis.
- `UDF`: directional release and convective bulk-flow links.
- `BDF`: reversible passive BBB exchange terms.
- `custom_conc_per_time`: Michaelis-Menten receptor transport and second-order sLRP1 scavenging.

## Notes on `data/parameters/module/amyloid_transport.json`
- The module parameter extraction file contains several noisy/non-specific entries (including mixed-context values and inconsistent units).
- Only values judged mechanistically aligned were considered; Elbert transport/clearance values were prioritized per required sourcing policy.

## Caveats
- `Q_BrainISF` is taken from Elbert's commented alternate value (`0.0105`) rather than the active zero in that file to enable ISF transport in this Tier-1 module.
- Some parameters are placeholders and should be replaced by curated human BBB transport measurements when available.
