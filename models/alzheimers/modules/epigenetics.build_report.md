# epigenetics Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/epigenetics.yaml`
- Tier: 4 (exploratory)
- Compartments: `Neuron`
- Reaction count: 10
- Rate law types used: `MA`, `custom_conc_per_time`
- Cross-module outputs: `mod_epigenetic_gene_expression`, `mod_epigenetic_inflammatory_tone`

## Inputs Consumed
1. `data/parameters/module/epigenetics.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Input Findings
- `data/parameters/module/epigenetics.json` is minimal (`parameter_count: 0`), so no direct kinetic constants were available.
- `plan/strategy_synaptic_neuronal.md` supplied compartment conventions (`Neuron`) and naming style, but no dedicated epigenetics reaction block.
- Elbert antimony files were scanned for direct epigenetics motifs (`DNMT`, `HDAC`, `SIRT1`, `miR146a`, `miR155`) and no direct module-equivalent reaction set was found.
- Existing module examples were used for YAML formatting, Tier-4 notes style, and rule-based cross-module modifiers.

## Design Summary
Implemented requested key species in `Neuron`:
- `DNMT1_Neuron`, `DNMT3A_Neuron`
- `HDAC_Neuron`, `HAT_Neuron`, `SIRT1_Neuron`
- `global_methylation_Neuron`, `H3K9ac_Neuron`, `H3K27me3_Neuron`
- `miR146a_Neuron`, `miR155_Neuron`

Implemented reaction groups (10 total):
1. DNA methylation addition (DNMT1/DNMT3A-driven, saturable)
2. DNA demethylation (first-order)
3. H3K9 acetylation (HAT-driven)
4. H3K9 deacetylation (combined HDAC + SIRT1 axis)
5. H3K27me3 deposition (DNMT3A/global methylation-linked)
6. H3K27me3 demethylation (first-order)
7. miR-146a synthesis (permissive chromatin favored)
8. miR-146a turnover
9. miR-155 synthesis (enhanced by low SIRT1/low methylation context)
10. miR-155 turnover

## Cross-Module Coupling Outputs
Assignment rules were included so this module can modulate rates in other modules:
- `mod_epigenetic_gene_expression`
  - Increases with `H3K9ac` activation pressure
  - Decreases with `global_methylation` and `H3K27me3` repression pressure
- `mod_epigenetic_inflammatory_tone`
  - Increases with `miR155`
  - Decreases with `miR146a`

These are intended as multiplicative scaling terms for transcription-linked production rates and inflammatory reaction terms in connected modules.

## Parameterization Notes
- All parameters are exploratory placeholders because direct parameter inputs were unavailable.
- Confidence flags are predominantly `assumed`, with `estimated` used for first-order turnover scales.
- Concentration-form custom rates use explicit `amount / V_Neuron` expressions for consistency with `custom_conc_per_time` semantics.

## Assumptions
1. Enzyme pools (`DNMT1`, `DNMT3A`, `HDAC`, `HAT`, `SIRT1`) are state variables without explicit synthesis/degradation in this reduced Tier-4 layer.
2. `global_methylation`, `H3K9ac`, and `H3K27me3` are lumped proxies, not locus-specific marks.
3. miRNA regulation of inflammation is represented via an exported modifier rule rather than explicit cytokine species dynamics.
4. This module is intended for later calibration/sensitivity analysis before mechanistic claims are made.

## Validation Status
- Ran:
  - `uv run antimony-bootstrap validate-module models/alzheimers/modules/epigenetics.yaml`
- Result:
  - `Valid: epigenetics (10 reactions, 30 parameters)`
