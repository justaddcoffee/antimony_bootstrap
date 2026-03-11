# Validation Report: `apoe_genetics.yaml`

Date: 2026-02-25
Module: `models/alzheimers/modules/apoe_genetics.yaml`

## 1) Schema Validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/apoe_genetics.yaml
```

- Initial result: **PASS** (`Valid: apoe_genetics (10 reactions, 20 parameters)`)
- Final result after repair: **PASS** (`Valid: apoe_genetics (10 reactions, 21 parameters)`)

## 2) Internal Consistency Checks
A dedicated Python checker script was written and executed:
- Script path: `/tmp/check_apoe_internal.py`
- Command:
```bash
python3 /tmp/check_apoe_internal.py
```

Checks implemented:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants/products` exists in `species`
- Species compartment suffix matches a declared compartment
- No rate equations with potential division-by-zero denominators
- Species initial amounts are numeric and `> 0`
- `k_*` rate constants are numeric and within heuristic range `[1e-15, 1e3]`

### Initial Internal Check Result
**FAIL** with these issues:
- `V_BrainISF` referenced in multiple reactions (`rate_parameters` and `rate_equation`) but missing from `parameters`

### Repair Applied
Updated `models/alzheimers/modules/apoe_genetics.yaml` by adding parameter:
- `V_BrainISF = 0.25 L`

### Final Internal Check Result
**PASS**
- Issues: none
- Warnings: none

## 3) Files Modified
- `models/alzheimers/modules/apoe_genetics.yaml`
- `models/alzheimers/modules/apoe_genetics.validation_report.md`
