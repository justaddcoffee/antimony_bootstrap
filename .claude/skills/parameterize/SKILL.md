# Parameterize Module

## When to Use
Use this skill to fill in missing parameter values for a module, drawing from Elbert reference model, BioModels, and literature.

## Workflow

1. **Identify missing parameters** — Check module YAML for null-valued parameters
   ```bash
   just validate-params <disease>
   ```

2. **Search Elbert model** — Primary source for parameter values
   - Check `../Elbert_Esguerra_model_v2026b/` for matching parameters
   - Match by reaction name and species names

3. **Search BioModels** — Secondary source
   - Download reference models and extract parameter values
   - Convert units if needed

4. **Literature search** — Tertiary source
   - Search PubMed for kinetic parameters
   - Record PMIDs for all values

5. **Assign values** — Update module YAML with:
   - `value`: the numeric value
   - `units`: parameter units
   - `confidence`: measured / estimated / assumed
   - `source`: where the value came from
   - `evidence`: PMIDs supporting the value

6. **Validate** — Check completeness
   ```bash
   just validate-params <disease>
   ```

## Confidence Levels
- **measured**: Value directly measured in relevant biological system
- **estimated**: Value estimated from related data or fitted from model
- **assumed**: Placeholder value, needs verification

## Output
Updated module YAML with all parameter values filled in and cited.
