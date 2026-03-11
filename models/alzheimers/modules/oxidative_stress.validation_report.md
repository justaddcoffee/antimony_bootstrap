# Oxidative Stress Module Validation Report

- Module: `models/alzheimers/modules/oxidative_stress.yaml`
- Validation date: 2026-02-25

## 1. Schema Validation
Command run:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/oxidative_stress.yaml
```

Initial result:
- `Valid: oxidative_stress (24 reactions, 41 parameters)`

## 2. Internal Consistency Checks
A Python checker script was written and executed (`/tmp/check_oxidative_module.py`) to verify:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants`/`products` exists in `species`
- Species compartment suffixes match declared compartments
- No rate equations with potential division by zero (including evaluation at initial values)
- Initial species values are present and positive
- Rate constants/kinetic terms are positive and within a broad sanity range

Initial internal-check result:
- 16 issues, 0 warnings
- All 16 issues were missing parameter declarations for compartment volumes:
  - `V_Neuron`
  - `V_Mitochondria`

## 3. Repairs Applied
Updated `models/alzheimers/modules/oxidative_stress.yaml` by adding explicit parameter entries:
- `V_Neuron = 0.0005 L`
- `V_Mitochondria = 0.0001 L`

These match the declared compartment `volume_value` fields.

## 4. Re-Validation
Internal checker rerun:
- `Issues: 0`
- `Warnings: 0`

Schema validator rerun:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/oxidative_stress.yaml
```
Result:
- `Valid: oxidative_stress (24 reactions, 43 parameters)`

## Final Status
- Validation complete
- Module repaired and internally consistent under requested checks
