# Validate Model

## When to Use
Use this skill to run the full 4-level validation pipeline on an assembled model.

## Workflow

Run the full QC pipeline:
```bash
just qc <disease>
```

This runs in sequence:

### Level 1: Schema Validation
```bash
just validate-modules <disease>
```
Checks that all module YAMLs conform to the Pydantic ModuleSpec schema.

### Level 2: Assembly
```bash
just assemble <disease>
```
Composes modules into a single Antimony model. Checks for:
- Compartment conflicts
- Species naming issues
- Rate equation errors

### Level 3: Antimony Parse
```bash
just validate-antimony <disease>
```
Loads the generated .ant file with `antimony.loadString()`. Catches:
- Syntax errors
- Undefined species/parameters
- Malformed rate equations

### Level 4: Simulation Smoke Test
```bash
just smoke-test <disease>
```
Runs a quick tellurium simulation. Checks for:
- NaN values (unstable dynamics)
- Inf values (overflow)
- Simulation errors

## Troubleshooting

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| Schema validation fails | Invalid YAML structure | Check field names and types |
| Assembly fails | Missing compartment/species | Add to module YAML |
| Antimony parse fails | Undefined parameter | Add parameter to module or manifest |
| Simulation NaN | Parameter values too large/small | Adjust rate constants |
| Simulation error | Missing initial conditions | Set initial amounts for all species |

## Output
Console output showing pass/fail for each validation level.
