# Research a Disease Mechanism

## When to Use
Use this skill when you need to research a specific disease mechanism to gather quantitative data for building an Antimony module.

## Workflow

1. **Read dismech YAML** — Extract the mechanism description, cell types, downstream links, and evidence PMIDs
   ```bash
   uv run antimony-bootstrap read-dismech <dismech_yaml_path>
   ```

2. **Check Elbert reference model** — Look for existing reactions, species, and parameters in `../Elbert_Esguerra_model_v2026b/`
   - Check module files in `modules/` for relevant reaction creation code
   - Check `generated/` for reaction dictionaries with parameter values
   - Note compartment names, species naming conventions, rate types

3. **Search BioModels** — Find published ODE models for this mechanism
   ```bash
   uv run antimony-bootstrap search-biomodels "<mechanism name>"
   ```

4. **Literature search** — Search PubMed for quantitative kinetic data
   - Focus on rate constants, half-lives, concentrations, volumes
   - Record PMIDs for all data sources

5. **Write research notes** — Save to `models/<disease>/research/<mechanism_name>.md`
   - Include: quantitative values found, species list, compartment list
   - Include: rate constants with units, initial concentrations
   - Include: all PMIDs and source attributions

## Output
A research notes file in `models/<disease>/research/` that provides all the information needed for the `build-module` skill.
