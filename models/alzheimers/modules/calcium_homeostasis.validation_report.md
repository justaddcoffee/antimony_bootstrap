# calcium_homeostasis.yaml Validation Report

Date: 2026-02-25
Module: `models/alzheimers/modules/calcium_homeostasis.yaml`

## 1. Schema validation
Command:
```bash
uv run antimony-bootstrap validate-module models/alzheimers/modules/calcium_homeostasis.yaml
```
Final result:
- `Valid: calcium_homeostasis (22 reactions, 43 parameters)`

## 2. Internal consistency checks
A Python checker script was written and executed (`/tmp/calcium_internal_check.py`) to validate:
- Every parameter referenced in `rate_parameters` or `rate_equation` exists in `parameters`
- Every species in `reactants`/`products` exists in `species`
- Every species compartment suffix matches a declared compartment
- No rate equations with potential division-by-zero risk
- Positive initial values where required (species amounts, compartment volumes)
- Rate constants in a reasonable positive range

Final command:
```bash
python /tmp/calcium_internal_check.py
```
Final result:
- `Issues: 0`
- `Warnings: 0`

## 3. Issues found and repairs made
Initial internal check identified missing volume parameters used in equations:
- `V_Neuron`
- `V_ER`

Fix applied in-place:
- Added explicit parameter entries under `parameters` for:
  - `V_Neuron = 0.0005 L`
  - `V_ER = 0.00005 L`
  - `V_Mitochondria = 0.0001 L`
- Each added with `confidence: assumed` and `source: compartment definition`

## 4. Re-validation status
After patching:
- Schema validation: pass
- Internal consistency checks: pass
- Module is now consistent with the requested validation rules.
