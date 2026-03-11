# synaptic_dysfunction.yaml Validation Report

Date: 2026-02-25
Module: `models/alzheimers/modules/synaptic_dysfunction.yaml`

## 1) Schema Validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/synaptic_dysfunction.yaml
```
Result:
- `Valid: synaptic_dysfunction (30 reactions, 66 parameters)`

## 2) Internal Consistency Checks
A Python validation script was written and executed to enforce:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists (with compartment volume parameters accepted from declared compartments)
- Every species in reactants/products exists in the module species list
- Species compartment suffixes match declared compartments
- No rate equations with denominator expressions evaluating to zero/non-positive at initialization
- Initial species values and compartment volumes are positive
- Rate constants (`k_*`) are positive and screened for extreme values via heuristic bounds

Execution summary:
- Issues: `0`
- Warnings: `0`

## 3) Repairs Applied
- No repairs were required.
- No changes were made to `synaptic_dysfunction.yaml`.

## 4) Re-validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/synaptic_dysfunction.yaml
```
Result:
- `Valid: synaptic_dysfunction (30 reactions, 66 parameters)`

## Conclusion
`models/alzheimers/modules/synaptic_dysfunction.yaml` passed schema and internal consistency validation with no issues detected.
