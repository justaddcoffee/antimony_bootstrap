# Retrieve BioModels Reference Models

## When to Use
Use this skill to search BioModels for published ODE models relevant to a disease mechanism, download them, and convert to Antimony format for reference.

## Workflow

1. **Search BioModels**
   ```bash
   uv run antimony-bootstrap search-biomodels "<query>"
   ```
   Try multiple queries: disease name, mechanism name, key proteins.

2. **Review results** — Identify models that:
   - Cover the mechanism of interest
   - Have realistic parameter values
   - Are well-cited

3. **Download and convert** — For each useful model:
   ```python
   from antimony_bootstrap.retrieval.biomodels import fetch_and_convert
   ant_string = fetch_and_convert("BIOMD0000000123", output_dir="reference_models/")
   ```

4. **Extract useful information**:
   - Parameter values and units
   - Species names and initial conditions
   - Rate laws and kinetic expressions
   - Compartment volumes

5. **Record attribution** — Note the BioModels ID, original publication, and which parameters were borrowed.

## Output
- Antimony files in `reference_models/` directory
- Notes on which parameters/rate laws to use in the module
