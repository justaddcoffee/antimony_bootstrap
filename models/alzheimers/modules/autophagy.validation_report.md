# Autophagy Module Validation Report

- Module: `models/alzheimers/modules/autophagy.yaml`
- Validation date: 2026-02-25 07:46:40 EST

## 1) Schema validation
Command run:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/autophagy.yaml
```

Result:
- `Valid: autophagy (25 reactions, 40 parameters)`

## 2) Internal consistency checks
A Python checker script was written and run (`/tmp/check_autophagy_internal.py`) to verify:
- every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- every species in reaction `reactants`/`products` exists in `species`
- species compartment suffix matches a declared compartment
- no obvious division-by-zero risks in rate equations
- required initial values are positive
- rate constants are in reasonable heuristic ranges

Initial run result:
- Errors: 0
- Warnings: 2
- Warnings identified:
  - `k_cargo_recognition` parsed as non-numeric literal (`1.4e8`)
  - `k_p62_autolys_deg` parsed as non-numeric literal (`8.0e7`)

## 3) Fixes applied
Updated numeric literals in YAML to ensure strict numeric parsing by PyYAML:
- `k_cargo_recognition.value`: `1.4e8` -> `1.4e+8`
- `k_p62_autolys_deg.value`: `8.0e7` -> `8.0e+7`

## 4) Re-validation
Schema re-validation:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/autophagy.yaml
```
- Result: `Valid: autophagy (25 reactions, 40 parameters)`

Internal consistency re-check:
```bash
uv run python /tmp/check_autophagy_internal.py
```
- Errors: 0
- Warnings: 0

## Final status
- `autophagy.yaml` is schema-valid and internally consistent per requested checks.
