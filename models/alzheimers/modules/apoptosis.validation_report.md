# Apoptosis Module Validation Report

- Module: `models/alzheimers/modules/apoptosis.yaml`
- Validation date: 2026-02-25

## 1) Schema Validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/apoptosis.yaml
```
Result:
- Initial: `Valid: apoptosis (20 reactions, 25 parameters)`
- After repair: `Valid: apoptosis (20 reactions, 26 parameters)`

## 2) Internal Consistency Checks
A Python validation script was written and executed at:
- `/tmp/check_apoptosis_module.py`

Checks implemented:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants`/`products` exists in `species`
- Every species has a declared compartment; compartment-like suffix mismatches are rejected
- No denominator terms in rate equations use non-positive/undefined parameters (division-by-zero risk check)
- Species requiring positive initialization (consumed and never produced) have `initial_amount > 0`
- Parameter values are numeric, finite, positive, and within a heuristic range

Initial internal-check result:
- `errors=6 warnings=0`
- All errors were due to missing `V_Neuron` in the `parameters` list while being used by reactions/rate equations.

## 3) Repairs Applied
Updated file:
- `models/alzheimers/modules/apoptosis.yaml`

Change made:
- Added parameter entry:
  - `name: V_Neuron`
  - `value: 0.0005`
  - `units: L`
  - `confidence: measured`
  - `source: module compartment specification`

## 4) Post-Repair Validation
Schema validation:
- Passed

Internal consistency checks:
- `errors=0 warnings=0`

## Final Status
- Module is valid against schema.
- Module passes requested internal consistency checks.
