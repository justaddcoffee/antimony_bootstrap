# Validation Report: neuroinflammation_astrocyte

## Target
- Module: `models/alzheimers/modules/neuroinflammation_astrocyte.yaml`
- Date: 2026-02-25

## 1) Schema validation
Command run:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/neuroinflammation_astrocyte.yaml
```
Result:
- `Valid: neuroinflammation_astrocyte (30 reactions, 44 parameters)`

## 2) Internal consistency checks
A Python validation script was written and executed to verify:
- Every parameter referenced in `rate_parameters` exists in `parameters`
- Every species used in reaction `reactants`/`products` exists in `species`
- Species compartment suffixes match declared `compartments`
- No reaction `rate_equation` has obvious division-by-zero risk from zero-valued denominator parameters
- Initial values are non-negative and present where expected
- Rate constants are positive and in a reasonable magnitude range

Script execution result:
- `ERRORS: none`
- `WARNINGS: none`

## 3) Fixes applied
- No YAML fixes were required.

## 4) Re-validation
Command re-run:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/neuroinflammation_astrocyte.yaml
```
Result:
- `Valid: neuroinflammation_astrocyte (30 reactions, 44 parameters)`

## Final status
- Module passes schema validation and internal consistency checks.
