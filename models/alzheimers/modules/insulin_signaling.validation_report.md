# Validation Report: `insulin_signaling.yaml`

- Module path: `models/alzheimers/modules/insulin_signaling.yaml`
- Validation timestamp: `2026-02-25 07:45:20 EST`

## 1) Schema validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/insulin_signaling.yaml
```
Result:
- `Valid: insulin_signaling (22 reactions, 33 parameters)`

## 2) Internal consistency checks
A Python validation script was written and executed (`/tmp/validate_insulin_signaling.py`) to enforce:
- Every parameter referenced in `rate_parameters` and `rate_equation` exists in `parameters`
- Every species in reaction `reactants`/`products` exists in `species`
- Every species compartment suffix maps to a declared compartment
- No rate equations with potential division-by-zero risks
- Initial values are positive where required
- Kinetic/scale parameters are positive and within conservative sanity bounds

Command:
```bash
python /tmp/validate_insulin_signaling.py
```
Result:
- `PASSED internal consistency checks: no issues found`

## 3) Fixes applied
- No fixes were required.
- No edits were made to `models/alzheimers/modules/insulin_signaling.yaml`.

## 4) Re-validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/insulin_signaling.yaml
```
Result:
- `Valid: insulin_signaling (22 reactions, 33 parameters)`
