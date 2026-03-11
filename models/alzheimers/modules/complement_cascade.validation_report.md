# Validation Report: `complement_cascade.yaml`

- Module path: `models/alzheimers/modules/complement_cascade.yaml`
- Validation timestamp: `2026-02-25 07:54:08 EST`
- Overall result: **PASS**

## 1) Schema Validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/complement_cascade.yaml
```
Result:
- `Valid: complement_cascade (14 reactions, 25 parameters)`

## 2) Internal Consistency Checks
A Python validation script was written and run (`/tmp/check_complement_module.py`) to enforce:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants`/`products` exists in `species`
- Every species compartment suffix matches a declared compartment
- No obvious division-by-zero risks in `rate_equation` denominators
- Species `initial_amount` values are numeric and strictly > 0
- Rate constants (`k_*`) are numeric, > 0, and within a conservative sanity bound (<= 1e3)

Execution result:
- `INTERNAL_CHECKS_PASSED`
- `Checked 18 species, 25 parameters, 14 reactions`

## 3) Repairs Applied
- No repairs were required. The module passed schema and internal checks as-is.

## 4) Re-validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/complement_cascade.yaml
```
Result:
- `Valid: complement_cascade (14 reactions, 25 parameters)`
