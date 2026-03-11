# peripheral_immune.yaml Validation Report

Date: 2026-02-25
Target: `models/alzheimers/modules/peripheral_immune.yaml`

## 1) Schema validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/peripheral_immune.yaml
```

Result (initial):
- `Valid: peripheral_immune (19 reactions, 30 parameters)`

Result (after fixes):
- `Valid: peripheral_immune (19 reactions, 32 parameters)`

## 2) Internal consistency checks
A Python validation script was written and executed at `/tmp/check_peripheral_immune.py` to verify:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants`/`products` exists in `species`
- Every species compartment suffix matches a declared compartment
- No rate equations have potential division-by-zero from non-positive denominator parameters/species
- Initial values are positive where denominator usage requires it
- Rate constants are in a reasonable positive range

Initial script result:
- 14 issues
- 0 warnings

Issues found:
- Missing parameter references for volume terms used in equations/rate parameters:
  - `V_Plasma`
  - `V_BrainISF`

## 3) Fixes applied
File updated in place:
- `models/alzheimers/modules/peripheral_immune.yaml`

Changes:
- Added parameter entry:
  - `V_Plasma = 3.0 L`
- Added parameter entry:
  - `V_BrainISF = 0.25 L`

Both values were aligned with the declared compartment `volume_value` fields.

## 4) Re-validation outcome
Schema validation:
- Pass

Internal consistency script:
- `TOTAL_ISSUES=0`
- `TOTAL_WARNINGS=0`

## Conclusion
`models/alzheimers/modules/peripheral_immune.yaml` is now consistent with schema and internal validation checks.
