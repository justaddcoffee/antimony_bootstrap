# Validation Report: neuroinflammation_microglia

- Module: `models/alzheimers/modules/neuroinflammation_microglia.yaml`
- Validation date: 2026-02-25

## 1) Schema Validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/neuroinflammation_microglia.yaml
```
Result:
- `Valid: neuroinflammation_microglia (43 reactions, 68 parameters)`

## 2) Internal Consistency Checks
A dedicated Python script was written and executed (`/tmp/check_neuroinflammation_microglia.py`) to verify:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in reaction `reactants`/`products` exists in `species`
- Every species compartment suffix matches a declared compartment
- No rate equations show potential division-by-zero risks (parameter denominator terms must be positive)
- Initial values are positive
- Rate constants (`k_*`) are positive and within a heuristic reasonable range

Command:
```bash
python3 /tmp/check_neuroinflammation_microglia.py
```
Result:
- `reactions: 43, species: 20, parameters: 68, compartments: 2`
- `issues: 0`
- `warnings: 0`

## 3) Fixes Applied
- No fixes were required. The YAML passed both schema and internal consistency checks as-is.

## 4) Re-validation
Commands rerun after checks:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/neuroinflammation_microglia.yaml
python3 /tmp/check_neuroinflammation_microglia.py
```
Result:
- Both commands completed successfully with no issues.
