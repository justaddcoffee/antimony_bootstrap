# lipid_metabolism.yaml Validation Report

Date: 2026-02-25
Module: `models/alzheimers/modules/lipid_metabolism.yaml`

## 1) Schema validation
Command:
`uv run antimony-bootstrap validate-module models/alzheimers/modules/lipid_metabolism.yaml`

Result: **PASS**
- Valid: lipid_metabolism (28 reactions, 43 parameters)

## 2) Internal consistency checks
A Python validation script was written and executed at `/tmp/lipid_internal_check.py` with the following checks:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants`/`products` exists in `species`
- Species compartment suffix matches declared compartments
- No rate equations with potential division by zero (baseline denominator evaluation)
- Initial values are positive where required
- Rate constants are within a nominal range (`k_*` in `[1e-12, 1e3]`)

Final result: **PASS**

## 3) Issues found and fixes applied
### Issue
Missing parameter definitions for compartment volumes used in reactions/equations:
- `V_Astrocyte`
- `V_BrainISF`

### Fix
Added both as explicit entries in `parameters`:
- `V_Astrocyte: 0.2 L`
- `V_BrainISF: 0.28 L`

## 4) Re-validation status
- Schema validation: **PASS**
- Internal consistency validation: **PASS**

