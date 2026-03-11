# tau_aggregation Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/tau_aggregation.yaml`
- Tier: 1
- Compartment scope: `Neuron`
- Reaction count: 14
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/tau_aggregation.json`
2. `plan/strategy_tau_pathology.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
The module encodes a compact neuronal tau-aggregation cascade with required key species:
- `PTAU_monomer_Neuron`
- `PTAU_oligomer_Neuron`
- `PTAU_PHF_Neuron`
- `NFT_Neuron`
- `TAU_seeds_Neuron`

Additional coupling species:
- `PTAU_MULTI_Neuron` as upstream input from the phosphorylation module.

Reaction groups:
- 1 upstream feed reaction from multisite p-tau to aggregation-competent monomer
- 3 aggregation growth reactions (primary nucleation, seeded nucleation, elongation)
- 1 PHF to NFT maturation reaction
- 2 reversibility/fragmentation reactions (oligomer disaggregation, PHF fragmentation)
- 5 seed and spreading reactions (oligomer/PHF release, NFT amplification, seeded NFT deposition, external seed import)
- 2 clearance reactions (seeds, NFTs)

## Source-to-Model Mapping
- Strategy document supplied the core mechanism template and rate-law forms:
  - nucleation-elongation aggregation
  - PHF maturation to NFT
  - seeded templating / prion-like propagation
- Parameter JSON supplied one directly useful quantitative signal:
  - elongation second-order rate evidence (`~2e5 M^-1 s^-1`) mapped to `k_elong_tau = 7.2e8 L/mol/hr`
- Remaining JSON entries were mostly PET tracer affinity/inhibition values (Ki/Kd/IC50); these were treated as qualitative context rather than direct kinetic constants for ODE state transitions.
- Elbert reference files were used for compatibility conventions (reaction naming style and concentration-based custom rate terms) rather than direct tau reaction reuse.

## Parameterization Notes
- `k_nuc_tau`, `n_nuc_tau`, `k_nft_mat`, `k_disagg_tau`, and clearance constants were chosen within strategy-provided ranges and converted to consistent units.
- Seeded conversion terms were represented with both mass-action-like (`k_seed_tau`) and saturable (`k_seeded_nft`, `K_seed_tau`) forms to stabilize dynamics at high seed burden.
- `k_seed_influx` was included as a tier-1 boundary condition to represent connectivity-driven spread without introducing extra compartments.

## Assumptions
1. Tier-1 scope is single-compartment (`Neuron`) while still capturing spreading effects via explicit seed inflow/amplification terms.
2. `PTAU_MULTI_Neuron` is an upstream input pool supplied by `tau_phosphorylation`.
3. `TAU_seeds_Neuron` is a lumped seed species representing transferable prion-like conformers.
4. Several seed release/amplification constants are estimated placeholders for calibration.

## Validation Status
- Module schema fields align with `ModuleSpec` (`name`, `compartments`, `species`, `reactions`, `parameters`, `evidence`).
- Recommended next checks:
  1. `python -m antimony_bootstrap.cli validate-module models/alzheimers/modules/tau_aggregation.yaml`
  2. full module-set validation and antimony assembly pipeline.
