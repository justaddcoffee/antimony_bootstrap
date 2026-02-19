# CLAUDE.md

This file provides guidance to Claude Code when working with the antimony_bootstrap codebase.

## Project Overview

**antimony_bootstrap** extracts known disease mechanisms from biological knowledge sources (dismech YAML, Wikipedia, PubMed, BioModels) and produces fully parameterized Antimony models — compartmental ODE models with species, reactions, rate laws, and parameter values suitable for simulation with Tellurium.

**Key pattern**: This follows dismech's Claude Code agent workflow — a human expert works interactively with Claude Code to build models incrementally, guided by skills, validation hooks, and research-first approaches. Not an automated pipeline.

## Key Commands

```bash
just install          # uv sync
just test             # Run pytest
just validate-modules # Validate all module YAMLs for a disease
just assemble         # Compose modules into Antimony
just validate-antimony # Parse check with antimony library
just smoke-test       # Quick tellurium simulation
just qc               # Full pipeline (schema + assemble + validate + simulate)
just read-dismech FILE # Extract mechanisms from dismech YAML
```

## Architecture

### Five Stages (human + Claude Code interactive)

1. **Knowledge Extraction** — Read dismech, search literature, retrieve BioModels
2. **Module Specification** — Write module YAML specs (compartments, species, reactions, rate law templates)
3. **Parameterization** — Fill in parameter values from literature/Elbert/BioModels with citations
4. **Assembly** — Compose modules into full Antimony model
5. **Validation** — antimony parse → libsbml → tellurium smoke test → completeness audit

### Data Model (Pydantic)

- **ModuleSpec** — one per mechanism: compartments, species, reactions, rules, parameters
- **ReactionSpec** — name, reactants, products, rate_type (MA/RMA/BDF/UDF/custom), rate_equation, evidence
- **ParameterSpec** — name, value, units, confidence (measured/estimated/assumed), source, PMID
- **ModelManifest** — disease name, MONDO term, module filenames, shared compartments/parameters

### Species Naming Convention

Species follow Elbert convention: `{species}_{compartment}` (e.g., `AB42_BrainISF`).
Compartment is always the text after the final underscore.

### Rate Types

From Elbert's RxnDict_to_antimony.py:
- **MA** — Mass action (unidirectional), rate multiplied by compartment volume
- **RMA** — Reversible mass action, generates forward + reverse reactions
- **BDF** — Bidirectional flow, same rate constant both directions
- **UDF** — Unidirectional flow, no volume multiplication
- **custom_conc_per_time** — Custom rate in concentration/time, multiplied by volume
- **custom_amt_per_time** — Custom rate in amount/time, no volume multiplication
- **custom** — Custom rate expression used as-is

### Project Structure

```
src/antimony_bootstrap/
├── schema/           # Pydantic models (ModuleSpec, ReactionSpec, etc.)
├── dismech/          # dismech YAML reader and causal graph
├── modules/          # Module YAML loading and reaction building
├── assembly/         # Multi-module composition and Antimony generation
├── retrieval/        # BioModels API integration
├── validation/       # 4-level validation (antimony, SBML, tellurium, completeness)
├── export/           # .ant and .sbml file writers
└── cli.py            # Typer CLI
models/alzheimers/    # Disease-specific modules, parameters, and generated output
```

## Skills

Claude Code skills in `.claude/skills/`:
- **research-mechanism** — Research a disease mechanism from dismech + literature
- **build-module** — Build module YAML from research notes
- **parameterize** — Find/assign parameter values with citations
- **validate-model** — Run 4-level validation + simulate
- **retrieve-biomodels** — Search BioModels for reference models

## Validation SOP

Before considering a module complete:
1. `just validate-modules` — Module YAML validates against Pydantic schema
2. `just assemble` — Generates .ant file without errors
3. `just validate-antimony` — antimony.loadString() succeeds
4. `just smoke-test` — tellurium simulates without NaN/errors

## Reference Model

The Elbert_Esguerra Alzheimer's model (`../Elbert_Esguerra_model_v2026b/`) is the gold-standard target:
- ~50 compartments, hundreds of species, ~800 reactions
- Full parameterization with rate constants
- Use as primary source for parameter values and naming conventions
