# Validation Report: `amyloid_transport.yaml`

Date: 2026-02-25
Module: `models/alzheimers/modules/amyloid_transport.yaml`

## 1) Schema validation
Command run:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/amyloid_transport.yaml
```

Result:
- `Valid: amyloid_transport (26 reactions, 40 parameters)`

## 2) Internal consistency checks
A Python validation script was written and executed at:
- `/tmp/check_amyloid_transport_internal.py`

Checks implemented:
- Every parameter referenced in `rate_parameters` exists in `parameters`
- Every identifier referenced in `rate_equation` is a declared species or parameter
- Every species in `reactants`/`products` exists in `species`
- Every species compartment suffix matches a declared compartment
- Rate equations were scanned for denominator terms with potential divide-by-zero risk
- Species appearing in denominator expressions have positive initial values
- Kinetic/transport parameter positivity and unit-aware range heuristics

Execution result:
- Reactions: 26
- Species: 24
- Parameters: 40
- Errors: none
- Warnings: none

## 3) Repairs applied
- No YAML repairs were required.
- Module is internally consistent under the requested checks.

## 4) Re-validation after checks
Command rerun:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/amyloid_transport.yaml
```

Result:
- `Valid: amyloid_transport (26 reactions, 40 parameters)`
