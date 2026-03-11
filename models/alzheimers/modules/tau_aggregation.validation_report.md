# tau_aggregation Module Validation Report

## Module
- Path: `models/alzheimers/modules/tau_aggregation.yaml`
- Date: 2026-02-25

## 1) Schema validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/tau_aggregation.yaml
```

- Initial result: **PASS** (`Valid: tau_aggregation (14 reactions, 16 parameters)`)
- Post-fix result: **PASS** (`Valid: tau_aggregation (14 reactions, 17 parameters)`)

## 2) Internal consistency checks
A Python checker script was written and executed at `/tmp/validate_tau_internal.py` to validate:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants`/`products` exists in `species`
- Species compartment suffix matches declared compartments
- No rate equations with potential division by zero
- Initial values are positive where required
- Rate constants are positive and within a broad heuristic range

Initial check result:
- **FAIL** (`errors=5, warnings=0`)
- Errors were all missing declaration of `V_Neuron` in `parameters` while referenced by custom rate laws.

Post-fix check result:
- **PASS** (`errors=0, warnings=0`)

## 3) Fixes applied
File updated in place:
- `models/alzheimers/modules/tau_aggregation.yaml`

Change made:
- Added parameter declaration:
  - `name: V_Neuron`
  - `value: 0.5`
  - `units: L`
  - `confidence: measured`
  - `source: Module compartment specification (Neuron volume)`

## Final status
- Module is schema-valid and internally consistent based on requested checks.
