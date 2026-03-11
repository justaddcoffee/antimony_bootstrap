# vascular_caa Validation Report

Date: 2026-02-25
Module: `models/alzheimers/modules/vascular_caa.yaml`

## 1) Schema validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/vascular_caa.yaml
```
Result:
- Passed (`Valid: vascular_caa (18 reactions, 26 parameters)`)

## 2) Internal consistency checks
A Python validator script was written and executed (`/tmp/validate_vascular_caa_internal.py`) to check:
- Every parameter referenced in `rate_parameters` resolves to a declared parameter (or declared compartment volume parameter)
- Every species in `reactants` / `products` exists in the species list
- Every species name has a compartment suffix matching a declared compartment
- No denominator symbols in rate equations have non-positive initialization/values
- Initial values used in denominator contexts are positive
- `k_*` rate constants are within a reasonable range `(1e-6, 1e2]`

Command:
```bash
python /tmp/validate_vascular_caa_internal.py
```
Result after repair:
- `INTERNAL CHECK PASSED`
- `Compartments: 2 | Species: 11 | Parameters: 26 | Reactions: 18`

## 3) Issues found and repaired

### A. Species compartment suffix inconsistencies
Several species did not end with a declared compartment suffix (`Perivascular` or `BrainParenchyma`).

Repairs:
- `AB40_perivascular` -> `AB40_Perivascular`
- `AB42_perivascular` -> `AB42_Perivascular`
- `AB40_CAA_deposit` -> `AB40_CAA_Deposit_Perivascular`
- `AB42_CAA_deposit` -> `AB42_CAA_Deposit_Perivascular`
- `SMC` -> `SMC_Perivascular`
- `COLLAGEN_IV` -> `COLLAGEN_IV_Perivascular`
- `PERIVASCULAR_drainage_rate` -> `PERIVASCULAR_DrainageRate_Perivascular`
- `CAA_severity` -> `CAA_Severity_Perivascular`
- `MICROHEMORRHAGE_risk` -> `MICROHEMORRHAGE_Risk_Perivascular`

All references in reactions and rate equations were updated accordingly.

### B. Invalid species entries in `rate_parameters`
`PERIVASCULAR_drainage_rate` (species) was incorrectly listed under `rate_parameters` for drainage reactions.

Repairs:
- Removed species entries from `rate_parameters` in:
  - `AB40_Perivascular_Drainage`
  - `AB42_Perivascular_Drainage`

## 4) Re-validation status
- Schema validation: Passed
- Internal consistency checks: Passed
- No division-by-zero flags detected under current initial values/parameter values
- All checked `k_*` constants fall within configured reasonable range

## 5) Files changed
- `models/alzheimers/modules/vascular_caa.yaml`
- `models/alzheimers/modules/vascular_caa.validation_report.md`
