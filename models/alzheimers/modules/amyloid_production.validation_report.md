# Validation Report: `amyloid_production.yaml`

## Scope
Validated module file:
- `models/alzheimers/modules/amyloid_production.yaml`

## Check Results

- Schema validation (`uv run antimony-bootstrap validate-module ...`): **PASS**
- Parameter references in `rate_parameters`/`rate_equation` exist in `parameters`: **PASS**
- Species in all `reactants`/`products` exist in `species`: **PASS**
- Species compartment suffix matches declared compartments: **PASS**
- No rate-equation denominator evaluates to zero at `t=0`: **PASS**
- Initial values > 0, or 0 only if species is not in a denominator: **PASS** (after fix)
- Rate constants in reasonable range (`<=1e8` and `>=1e-15` when nonzero): **PASS**

## Issues Found and Fixes Applied

### Issue
Three species had zero initial amounts while appearing in rate-equation denominators:
- `APP_Neuron`
- `C83_Neuron`
- `C99_Neuron`

### Fix
Updated initial amounts in-place to small positive values:
- `APP_Neuron`: `0.0` -> `1.0e-12`
- `C83_Neuron`: `0.0` -> `1.0e-12`
- `C99_Neuron`: `0.0` -> `1.0e-12`

## Re-validation After Fix

- Schema validation: **PASS**
- Internal consistency script: **PASS** for all checks

## Remaining Concerns

- No blocking validation concerns remain under the requested checks.
- The small seeded nonzero initial amounts are numerically conservative, but downstream calibration/sensitivity analysis should confirm they do not materially affect intended baseline dynamics.
