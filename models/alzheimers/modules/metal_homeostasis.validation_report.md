# Validation Report: `metal_homeostasis.yaml`

Date: 2026-02-25
File: `models/alzheimers/modules/metal_homeostasis.yaml`

## 1) Schema validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/metal_homeostasis.yaml
```

Initial result: **PASS** (`Valid: metal_homeostasis (15 reactions, 19 parameters)`).

After edits, intermediate result: **FAIL** (new parameter entries used invalid `confidence: fixed`).

Final result: **PASS** (`Valid: metal_homeostasis (15 reactions, 21 parameters)`).

## 2) Internal consistency checks
A Python checker script was written and executed to validate:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in reaction `reactants`/`products` exists in `species`
- Species compartment suffixes match declared compartments
- No rate equations with potential division-by-zero from declared denominator parameters/literals
- Species initial values are positive
- Kinetic constants are positive and within a broad heuristic range

Initial result: **FAIL**

Detected issues:
- `V_BrainISF` and `V_Neuron` were referenced in `rate_parameters` and `rate_equation` but not declared in `parameters`.

Final result after fixes: **PASS** (`PASS: internal consistency checks`).

## 3) Fixes applied
Updated `models/alzheimers/modules/metal_homeostasis.yaml` by adding two missing parameter entries:
- `V_Neuron = 0.0005 L`
- `V_BrainISF = 0.25 L`

Both were set with `confidence: assumed` and sources tied to matching compartment volumes.

## 4) Final status
- Schema validation: **PASS**
- Internal consistency checks: **PASS**
- Module is now validated and internally consistent under the requested checks.
