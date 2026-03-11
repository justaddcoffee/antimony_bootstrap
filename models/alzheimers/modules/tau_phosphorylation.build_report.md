# tau_phosphorylation Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/tau_phosphorylation.yaml`
- Tier: 1
- Compartment scope: `Neuron`
- Reaction count: 22
- Rate law types used: `MA`, `custom_conc_per_time`

## Inputs Consumed
1. `data/parameters/module/tau_phosphorylation.json`
2. `plan/strategy_tau_pathology.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Design Summary
The module implements a site-specific tau phosphorylation cycle with the required key entities:
- Tau pool: `TAU_Neuron`
- Phospho-site pools: `PTAU_AT8_Neuron`, `PTAU_AT180_Neuron`, `PTAU_PHF1_Neuron`, `PTAU_MULTI_Neuron`
- Regulators: `GSK3B`, `CDK5`, `PP2A`, `PIN1` active/inactive states
- Control inputs: `AKT_active_Neuron`, `P25_Neuron`, `CIP2A_Neuron`, `ROS_Neuron`

Reaction groups:
- 7 kinase-driven phosphorylation/hyperphosphorylation reactions (Michaelis-Menten style)
- 5 PP2A-driven dephosphorylation reactions (Michaelis-Menten style)
- 2 PIN1-mediated interconversion reactions
- 8 regulator-state activation/inhibition reactions for GSK3B/CDK5/PP2A/PIN1

## Source-to-Model Mapping
- Strategy document provided the kinetic structure and parameter ranges for:
  - GSK3B/CDK5 phosphorylation
  - PP2A dephosphorylation
  - GSK3B activation/inactivation
- Module parameter JSON was reviewed; extracted values were mostly assay affinity/time summaries and not directly mappable to core ODE kinetic constants. They were used as supporting context, not direct assignments.
- Elbert reference files were used for compatibility conventions (naming style, rate-law compatibility) rather than direct tau equations, because tau-pathology reactions were not present in the available Elbert reaction files.

## Parameterization Notes
- `Vmax` and `Km` values were chosen within strategy-provided ranges and converted to consistent units (`mol/L/hr`, `mol/L`).
- Activation/inhibition constants were set as tier-1 estimated defaults with explicit `confidence` and `source` metadata.
- Enzyme reference parameters (`*_ref`) were added to normalize activity multipliers and stabilize scaling.

## Assumptions
1. A single neuronal compartment is sufficient for the tier-1 phosphorylation module.
2. `PTAU_MULTI_Neuron` represents lumped multisite/hyperphosphorylated tau beyond AT8/AT180/PHF1.
3. PIN1 effects are represented as effective phospho-state interconversion terms.
4. Upstream drivers (`AKT`, `P25`, `CIP2A`, `ROS`) are included as local modulators for activation/inhibition, enabling future coupling with insulin, stress, and inflammatory modules.

## Validation Status
- Schema-field compatibility checked against `ModuleSpec` (`name`, `compartments`, `species`, `reactions`, `parameters`, `evidence`).
- Recommended next check: load via `ModuleSpec.from_yaml` and run project validation/test pipeline.
