# Build Module YAML from Research

## When to Use
Use this skill after completing research on a mechanism to create the module YAML specification.

## Workflow

1. **Read research notes** — Load `models/<disease>/research/<mechanism_name>.md`

2. **Define compartments** — List all compartments involved (e.g., BrainISF, CSF, Plasma)
   - Use Elbert naming conventions
   - Include volume parameters (V_<compartment>)

3. **Define species** — List all molecular species with compartment suffixes
   - Follow naming convention: `{base}_{compartment}` (e.g., AB42_BrainISF)
   - Set initial amounts where known

4. **Define reactions** — Create reaction specifications
   - Choose appropriate rate type: MA, RMA, BDF, UDF, custom_conc_per_time, custom_amt_per_time, custom
   - List reactants and products using full species names
   - Specify rate parameters or custom rate equations

5. **Define parameters** — List all rate constants and other parameters
   - Set values where known (null if not yet determined)
   - Set confidence levels: measured, estimated, assumed
   - Include source citations

6. **Validate** — Check the module YAML against the schema
   ```bash
   just validate-module models/<disease>/modules/<mechanism>.yaml
   ```

## Rate Type Guide
- **MA**: Simple mass action, `k * [reactants] * V_compartment` — use for simple degradation, production
- **RMA**: Reversible mass action — use for binding/unbinding equilibria
- **BDF**: Bidirectional flow — use for transport between compartments (same rate both ways)
- **UDF**: Unidirectional flow — use for one-way transport, no volume multiplication
- **custom_conc_per_time**: Custom rate in concentration/time — use for Michaelis-Menten, Hill equations
- **custom_amt_per_time**: Custom rate in amount/time — use when rate is already in absolute units
- **custom**: Custom expression used as-is — use for complex rate laws

## Output
A module YAML file in `models/<disease>/modules/<mechanism_name>.yaml`.
