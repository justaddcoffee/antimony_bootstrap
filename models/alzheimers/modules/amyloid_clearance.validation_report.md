# Amyloid Clearance Module Validation Report

- Module: `models/alzheimers/modules/amyloid_clearance.yaml`
- Validation date: 2026-02-25

## 1. Schema Validation
Command run:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/amyloid_clearance.yaml
```

Final result:
- `Valid: amyloid_clearance (20 reactions, 37 parameters)`

## 2. Internal Consistency Checks
A Python checker script was written and executed at:
- `/tmp/check_module_internal_consistency.py`

Command run:
```bash
python3 /tmp/check_module_internal_consistency.py models/alzheimers/modules/amyloid_clearance.yaml
```

Checks performed:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in reaction `reactants`/`products` exists in `species`
- Species compartment suffixes match declared compartments
- Potential division-by-zero risks in rate equations (heuristic denominator scan)
- Presence and positivity requirements for initial values where denominator safety depends on them
- Kinetic parameter positivity and broad magnitude sanity

## 3. Issues Found
Initial internal consistency run reported 28 errors:
- Missing parameter declarations for compartment volumes used in kinetics:
  - `V_BrainISF`
  - `V_Microglia`
  - `V_Perivascular`
- These were referenced in both `rate_parameters` and `rate_equation` fields across multiple reactions.

## 4. Fixes Applied
Updated `models/alzheimers/modules/amyloid_clearance.yaml` by adding these parameters to `parameters`:
- `V_BrainISF = 0.25 L`
- `V_Microglia = 0.01 L`
- `V_Perivascular = 0.03 L`

These values match the declared compartment volumes.

## 5. Re-Validation Results
- Schema validation: **pass**
- Internal consistency checker: **0 issues**

Note:
- One checker warning remains from a conservative regex heuristic on a Hill-form denominator in `MicrogliaActivation_Resting_to_Phagocytic`.
- Manual review indicates denominator safety is maintained because `Kact_microglia_AB42 > 0` and the additive term is non-negative.

## 6. Final Status
- Module YAML repaired and validated.
- Report generated at `models/alzheimers/modules/amyloid_clearance.validation_report.md`.
