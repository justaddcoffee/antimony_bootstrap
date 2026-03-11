# tau_phosphorylation.yaml Validation Report

Date: 2026-02-25
Module: `models/alzheimers/modules/tau_phosphorylation.yaml`

## 1) Schema validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/tau_phosphorylation.yaml
```

Initial result:
- `Valid: tau_phosphorylation (22 reactions, 42 parameters)`

Post-fix result:
- `Valid: tau_phosphorylation (22 reactions, 43 parameters)`

## 2) Internal consistency checks
A Python script was written and executed:
- Script: `/tmp/tau_phosphorylation_consistency_check.py`
- Command:
```bash
uv run python /tmp/tau_phosphorylation_consistency_check.py
```

Checks implemented:
- Every parameter referenced in `rate_parameters` and `rate_equation` exists in `parameters`
- Every species in reactants/products exists in `species`
- Every species compartment suffix matches a declared compartment
- Rate equations screened for potential division-by-zero denominators
- Species and key parameter initial values checked for positivity
- Heuristic range checks for kinetic constants (`k_`, `Km_`, `Vmax_`)

## 3) Issues found
Root issue:
- `V_Neuron` was referenced in multiple `rate_parameters` and `rate_equation` entries but was missing from `parameters`.

Internal-check failure before fix:
- 36 issues total, all caused by missing `V_Neuron` references.

## 4) Fixes applied
Updated file:
- `models/alzheimers/modules/tau_phosphorylation.yaml`

Change made:
- Added parameter entry:
  - `name: V_Neuron`
  - `value: 0.5`
  - `units: L`
  - `confidence: assumed`
  - `source: Compartment volume parameter (Neuron)`

## 5) Final status
Final internal-check result:
- Issues: none
- Warnings: none

Final schema-validation result:
- `Valid: tau_phosphorylation (22 reactions, 43 parameters)`

Conclusion:
- Module is schema-valid and internally consistent for the requested checks.
