# BBB Integrity Module Validation Report

- Module: `models/alzheimers/modules/bbb_integrity.yaml`
- Date: 2026-02-25

## 1. Schema Validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/bbb_integrity.yaml
```
Result:
- `Valid: bbb_integrity (24 reactions, 32 parameters)`

## 2. Internal Consistency Checks
A checker script was created and run:
- `scripts/validate_module_internal.py`

Command:
```bash
uv run python scripts/validate_module_internal.py models/alzheimers/modules/bbb_integrity.yaml
```

Checks performed:
- Every parameter referenced in `rate_parameters` exists in `parameters`
- Every symbol referenced in `rate_equation` exists in `parameters` or `species`
- Every species in reaction `reactants`/`products` exists in `species`
- Every species compartment suffix matches a declared compartment
- Division denominators in rate equations are analyzed for potential zero/non-positive risk
- Species initial values are numeric and strictly `> 0`
- Kinetic-like constants (`k_*`, `beta_*`) are numeric, `> 0`, and within nominal range `[1e-9, 1e3]`

Result:
- `Errors: 0`
- `Warnings: 0`

## 3. Repairs Applied
- No changes were required in `bbb_integrity.yaml`.
- Internal checker logic was refined to avoid false positives in denominator safety checks for nested positive divisions.

## 4. Final Status
- Module is schema-valid and internally consistent under the requested checks.
