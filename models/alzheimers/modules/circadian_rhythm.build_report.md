# circadian_rhythm Module Build Report

## Output
- Module YAML: `models/alzheimers/modules/circadian_rhythm.yaml`
- Tier: 4 (exploratory)
- Compartments: `Neuron`, `BrainISF`
- Reaction count: 10
- Rate law types used: `MA`, `custom_conc_per_time`
- Key output: `glymphatic_flow_rate_BrainISF`

## Inputs Consumed
1. `data/parameters/module/circadian_rhythm.json`
2. `plan/strategy_synaptic_neuronal.md`
3. `../Elbert_Esguerra_model_v2026b/antimony_models/`
4. `src/antimony_bootstrap/schema/module_spec.py`
5. `models/alzheimers/modules/abeta_production.yaml`

## Input Findings
- `data/parameters/module/circadian_rhythm.json` is effectively empty for kinetic assignment (`parameter_count: 0`).
- `plan/strategy_synaptic_neuronal.md` provides compartment conventions and naming style but does not define a circadian block.
- Elbert antimony references do not include a full circadian oscillator module, but they do provide a glymphatic-flow anchor parameter:
  - `Q_glymph = 0.008101366791213009` in `Antimony_elbert_Esguerra_noSILK_1a_parameters.txt`
  - variant values (e.g., `3.738934e-03`) in other model versions.

## Design Summary
This exploratory module implements a reduced circadian control architecture with explicit molecular state variables:
- Core clock species: `BMAL1_Neuron`, `CLOCK_Neuron`, `PER2_Neuron`, `CRY1_Neuron`, `REV_ERBa_Neuron`
- Sleep/wake mediators: `melatonin_Neuron`, `orexin_Neuron`
- Downstream clearance modulator: `glymphatic_flow_rate_BrainISF`

Mechanistic blocks:
1. **Core oscillator-like feedback**
   - `PER2` synthesis driven by BMAL1:CLOCK, repressed by CRY1 and REV-ERBa
   - `CRY1` synthesis driven by PER2
   - `REV-ERBa` synthesis driven by BMAL1:CLOCK, repressed by CRY1
   - First-order degradation for PER2/CRY1/REV-ERBa
2. **Sleep-wake signal layer**
   - Melatonin synthesis promoted by PER2 and inhibited by orexin
   - Orexin synthesis promoted by BMAL1:CLOCK and inhibited by melatonin and REV-ERBa
   - First-order degradation for melatonin and orexin
3. **AB-clearance coupling output**
   - Assignment rule computes `glymphatic_flow_rate_BrainISF` from melatonin/orexin balance around Elbert `Q_glymph` baseline.

## Parameterization Strategy
- Since no direct circadian parameter JSON data were provided, parameters are split as:
  - **Literature-informed timescale estimates** for turnover and oscillator cadence (confidence: `estimated`)
  - **Exploratory saturation/inhibition constants** for nonlinear couplings (confidence: `assumed`)
- `Q_glymph_base` is anchored to Elbert reference value (`0.008101366791213009 L/hr`) to keep downstream AB-clearance coupling on a compatible magnitude.

## Assumptions
1. BMAL1 and CLOCK are represented as slowly varying driver pools (explicit species, no direct turnover reactions in this reduced form).
2. REV-ERBa is included dynamically as a repressive arm to preserve core clock feedback structure.
3. Melatonin and orexin are modeled in `Neuron` as lumped local signaling proxies rather than separate endocrine compartments.
4. Glymphatic modulation is represented with an assignment rule output, intended to be consumed by AB-clearance reactions in other modules.
5. Parameter values marked `assumed` are placeholders for future calibration/sensitivity analysis.

## Schema and Consistency Check
- Conforms to `ModuleSpec` fields (`name`, `description`, `mechanism`, `compartments`, `species`, `reactions`, `parameters`, `rules`, `evidence`, `notes`).
- Uses supported rate types only: `MA`, `custom_conc_per_time`.
- Reaction count is within requested range (5-10).
- Required key species and requested compartments are present.

## Recommended Follow-up
1. Couple `glymphatic_flow_rate_BrainISF` into amyloid clearance flow terms (e.g., ISF-to-CSF or glymphatic sink rates).
2. Run dynamic checks for day-night alternation behavior and boundedness of melatonin/orexin states.
3. Calibrate exploratory constants against circadian biomarker datasets (CSF AB diurnal variation and sleep perturbation studies).
