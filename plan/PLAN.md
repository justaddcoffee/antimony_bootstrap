# Massively Parallel Codex Agent Plan: Alzheimer's Knowledge → Antimony ODE Models

**Date**: 2026-02-24
**Corpus**: 1,325 Primary Alzforum papers + 2,139 Secondary Alzforum papers (PMC XML)
**Target**: Elbert-scale model (~50 compartments, hundreds of species, ~800 reactions)
**Framework**: antimony_bootstrap ModuleSpec YAML → Antimony → SBML → Tellurium
**Execution**: Up to 100 parallel Codex agents via `mcp__codex__codex` in background Task workers

---

## Executive Summary

This plan replaces the sequential 16-week pipeline with **massively parallel Codex agent orchestration**. Every stage splits work across N autonomous agents (up to 100), each running in the background via `Task(subagent_type="Bash", run_in_background=True)` calling `mcp__codex__codex` with `sandbox: "danger-full-access"` and `approval-policy: "never"`.

**Timeline compression**: 16 weeks → ~3-5 days of wall-clock time.

**Key principle**: Each agent gets a self-contained prompt with its exact slice of work, writes output to a deterministic path, and requires no human intervention. A thin orchestrator (Claude Code main session) launches agents, monitors completion, and runs merge steps between stages.

---

## Orchestrator Pattern

All codex agents are launched identically:

```python
# In the main Claude Code session:
Task(
    subagent_type="Bash",
    run_in_background=True,
    prompt="""
    Use mcp__codex__codex to run a codex session with these parameters:
    - prompt: <AGENT_PROMPT>
    - sandbox: "danger-full-access"
    - approval-policy: "never"
    - cwd: "/Users/jtr4v/PythonProject/antimony_bootstrap"
    """
)
```

Output files go to deterministic paths so the orchestrator can verify completion by checking file existence.

---

## Step 0: Preparation — Paper Index & Triage

**Agents**: 1 (synchronous, must complete before all other steps)
**Time**: ~30-60 minutes
**Output**: `data/paper_index.json`

This step parses all 3,463 XMLs, builds a searchable index, and tiers every paper.

### Agent 0 Prompt

```
You are a biomedical paper indexing agent. Your task:

1. Find all PMC XML files under the data/ directory (both primary/ and secondary/ subdirectories).

2. For each XML file, extract:
   - pmcid (from filename or XML)
   - title
   - abstract text (first 500 chars)
   - has_tables (boolean: does the XML contain <table-wrap> elements?)
   - section_count (number of <sec> elements)
   - word_count (approximate body text length)

3. Score each paper for ODE relevance using keyword density in abstract + body:
   - kinetic_score: count of (rate, kinetic, Km, Kd, IC50, half-life, clearance, production, degradation, turnover, flux)
   - mechanism_score: count of (pathway, signaling, phosphorylation, aggregation, binding, transport, cleavage, secretion)
   - table_score: 2 if has kinetic tables, 1 if has any tables, 0 otherwise

4. Compute total_score = kinetic_score * 3 + mechanism_score + table_score * 5

5. Assign tiers:
   - Tier A: top 200 by total_score (deep parameter extraction)
   - Tier B: next 300 (mechanistic extraction)
   - Tier C: next 1000 (pathway extraction)
   - Tier D: remainder (calibration only)

6. Write the complete index to data/paper_index.json as a JSON array:
   [{"pmcid": "PMC...", "title": "...", "tier": "A", "total_score": 42, "kinetic_score": 8, ...}, ...]

7. Also write tier-specific lists:
   - data/tier_a_papers.json (just PMCIDs, ~200 papers)
   - data/tier_b_papers.json (~300 papers)
   - data/tier_c_papers.json (~1000 papers)
   - data/tier_d_papers.json (~2000 papers)

8. Write a summary to data/paper_index_summary.txt with counts per tier and top-20 papers by score.

Use Python with xml.etree.ElementTree for parsing. Process all files, don't skip any.
```

### Verification
- `data/paper_index.json` exists and contains ~3,463 entries
- All four tier files exist
- Tier A has 150-250 papers, Tier B has 250-350

---

## Step 1: Deep Paper Reading — 100 Agents in Parallel

**Agents**: 100
**Time**: ~1-2 hours (all parallel)
**Input**: `data/paper_index.json` (from Step 0)
**Output**: `data/extracted/batch_{00-99}.json`

Each agent reads the full text of ~35 papers and extracts structured mechanistic knowledge.

### Batch Assignment

```python
import json
papers = json.load(open("data/paper_index.json"))
batch_size = len(papers) // 100 + 1
for i in range(100):
    batch = papers[i * batch_size : (i + 1) * batch_size]
    # Launch agent with this batch
```

### Agent Template (for batch N)

```
You are a biomedical knowledge extraction agent. You will read {BATCH_SIZE} Alzheimer's disease papers and extract structured mechanistic information for ODE modeling.

Your batch: papers index {START_IDX} to {END_IDX} from data/paper_index.json

For each paper in your batch:

1. Load the paper index entry to get the PMCID and file path.
2. Read the full PMC XML file.
3. Parse the XML to extract body text, tables, and figure captions.
4. Extract the following structured information:

{
  "pmcid": "PMC...",
  "title": "...",
  "tier": "A/B/C/D",
  "pathways": ["amyloid_processing", "tau_phosphorylation", ...],
  "species": [
    {"name": "AB42", "compartment": "BrainISF", "elbert_name": "AB42_BrainISF", "type": "protein"}
  ],
  "compartments": ["BrainISF", "CSF", "Neuron", ...],
  "reactions": [
    {
      "name": "AB42_production",
      "reactants": ["APP_Neuron", "BACE1_Neuron"],
      "products": ["AB42_BrainISF", "sAPPb_BrainISF"],
      "rate_type": "custom",
      "rate_equation": "Vmax_BACE1 * APP_Neuron / (Km_BACE1 + APP_Neuron)",
      "evidence": "direct measurement"
    }
  ],
  "parameters": [
    {
      "name": "Km_BACE1",
      "value": 20.0,
      "units": "uM",
      "context": "BACE1 cleavage of APP",
      "measurement_type": "in_vitro",
      "species_source": "human",
      "table_reference": "Table 2"
    }
  ],
  "kinetic_values": [
    {
      "parameter": "AB42_half_life_ISF",
      "value": 7.0,
      "units": "hr",
      "method": "SILK",
      "context": "healthy controls"
    }
  ],
  "evidence_quality": "high/medium/low",
  "notes": "Key findings relevant to ODE modeling..."
}

5. Use Elbert species naming convention: {species}_{compartment} (e.g., AB42_BrainISF).

> **TODO (post-pilot)**: The JSON extraction schema examples above are heavily amyloid-biased (AB42, BACE1, Km_BACE1, BrainISF). In future extraction runs, broaden examples to cover multiple pathways (tau, neuroinflammation, lipid, calcium, etc.) to reduce anchoring bias and improve extraction quality for non-amyloid modules.

6. Map to these pathway categories:
   amyloid_production, amyloid_aggregation, amyloid_clearance, amyloid_transport,
   tau_phosphorylation, tau_aggregation, neuroinflammation_microglia, neuroinflammation_astrocyte,
   synaptic_dysfunction, calcium_homeostasis, oxidative_stress, apoptosis,
   lipid_metabolism, insulin_signaling, autophagy, metal_homeostasis,
   bbb_integrity, vascular_caa, apoe_genetics, complement_cascade

7. For Tier A/B papers, be especially thorough with parameter extraction — read tables carefully, convert units to nM/L/hr standard.

8. For Tier C/D papers, focus on pathway identification and species lists; skip detailed parameter extraction.

Write your results to: data/extracted/batch_{BATCH_NUM:02d}.json
as a JSON array of paper extraction objects.

Write a summary line count to: data/extracted/batch_{BATCH_NUM:02d}.summary.txt
Format: "{N_PAPERS} papers processed, {N_PARAMS} parameters extracted, {N_REACTIONS} reactions identified"
```

### Merge Step (orchestrator, after all 100 agents complete)

```
Merge all 100 batch files into a single consolidated extraction:

1. Read all data/extracted/batch_*.json files
2. Concatenate into data/extracted/all_papers.json
3. Build summary statistics:
   - Total parameters extracted
   - Parameters per pathway
   - Top 50 most-cited species
   - Top 50 most-cited reactions
4. Write to data/extracted/extraction_summary.json
5. Build a parameter database: data/parameters/all_parameters.json
   - Deduplicated by (parameter_name, context)
   - For duplicate values, compute geometric mean
   - Track source count and PMCIDs
```

---

## Step 2: Parameter Extraction from Tier A Papers — 50 Agents

**Agents**: 50
**Time**: ~1-2 hours (all parallel)
**Input**: `data/tier_a_papers.json`, raw XML files
**Output**: `data/parameters/deep_batch_{00-49}.json`

This is the deep-reading pass focused exclusively on extracting every kinetic parameter from the highest-value papers.

### Agent Template (for batch N)

```
You are a kinetic parameter extraction specialist. You will perform deep reading of {BATCH_SIZE} high-priority Alzheimer's research papers to extract every quantitative kinetic parameter suitable for ODE modeling.

Your batch: papers {START_IDX} to {END_IDX} from data/tier_a_papers.json

For each paper:

1. Read the FULL text of the PMC XML file — every section, every table, every figure caption.

2. Extract EVERY quantitative parameter you find:
   - Rate constants (k, kcat, kon, koff)
   - Michaelis-Menten parameters (Km, Vmax)
   - Binding affinities (Kd, Ka, Ki, IC50, EC50)
   - Half-lives (t1/2)
   - Concentrations (baseline levels, Cmax, steady-state)
   - Production/clearance rates
   - Transport rates
   - Hill coefficients
   - Stoichiometric coefficients

3. For each parameter, record:
{
  "parameter_name": "Km_BACE1_APP",
  "value": 20.0,
  "units": "uM",
  "standard_value": 20000.0,
  "standard_units": "nM",
  "context": "BACE1 cleavage of APP Swedish mutation",
  "measurement_type": "in_vitro/in_vivo/computational",
  "species_source": "human/mouse/rat/cell_line",
  "cell_line": "HEK293",
  "method": "enzyme kinetics assay",
  "pmcid": "PMC...",
  "table_or_figure": "Table 2",
  "text_excerpt": "The Km for BACE1 cleavage of APP was determined to be 20 ± 3 uM...",
  "target_module": "abeta_production",
  "target_reaction": "APP_cleavage_by_BACE1",
  "confidence": "measured",
  "notes": ""
}

4. ALSO extract rate law form evidence — when a paper describes the functional form of a kinetic relationship (not just parameter values), record:
{
  "rate_law_form": "Michaelis-Menten",
  "rate_equation": "Vmax * S / (Km + S)",
  "context": "BACE1 cleavage of APP",
  "pmcid": "PMC...",
  "text_excerpt": "BACE1 processing of APP followed classical Michaelis-Menten kinetics...",
  "target_module": "abeta_production",
  "target_reaction": "APP_cleavage_by_BACE1",
  "supports": "Michaelis-Menten functional form for BACE1"
}

   This is critical — it provides evidence for WHY a rate equation has a particular form, not just what the parameter values are. Look for:
   - Statements about kinetic mechanism (Michaelis-Menten, Hill, mass action, etc.)
   - Nucleation-elongation models with specific monomer/fibril dependencies
   - Cooperative binding (Hill coefficients)
   - Competitive/noncompetitive inhibition patterns
   - Transport kinetics (facilitated vs passive)

5. Unit conversion to standard units (ALWAYS convert):
   - Concentration: convert to nM (1 uM = 1000 nM, 1 mM = 1e6 nM, 1 pM = 0.001 nM)
   - Time: convert to hr (1 min = 1/60 hr, 1 day = 24 hr, 1 s = 1/3600 hr)
   - Volume: convert to L (1 mL = 0.001 L, 1 uL = 1e-6 L)
   - Rate (1st order): convert to 1/hr
   - Rate (2nd order): convert to 1/(nM·hr)
   - From half-life: k = ln(2) / t_half

5. Map each parameter to one of these 25 modules:
   abeta_production, abeta_transport, abeta_aggregation, abeta_clearance,
   tau_phosphorylation, tau_aggregation,
   neuroinflammation_microglia, neuroinflammation_astrocyte,
   synaptic_dysfunction, calcium_homeostasis, oxidative_stress, apoptosis_neuronal_death,
   lipid_metabolism, insulin_signaling, autophagy_proteostasis, metal_homeostasis,
   bbb_integrity, vascular_caa,
   apoe_genetics, presenilin_mutations, app_genetics, trem2_signaling,
   peripheral_immune, complement_cascade

Write to: data/parameters/deep_batch_{BATCH_NUM:02d}.json
```

### Merge Step

```
Merge all 50 deep parameter batches:

1. Read all data/parameters/deep_batch_*.json
2. Merge with data/parameters/all_parameters.json from Step 1
3. Deduplicate: for same (parameter_name, target_module, target_reaction):
   - If multiple measured values: geometric mean, track min/max/N
   - Prefer human > mouse > rat > cell_line
   - Prefer in_vivo > in_vitro > computational
4. Write: data/parameters/consolidated_parameters.json
5. Write per-module parameter files: data/parameters/module/{module_name}.json
6. Write: data/parameters/parameter_coverage.json
   - Per module: how many parameters found vs estimated needed
   - Flag modules with <50% coverage for Elbert fallback
```

---

## Step 3: Module YAML Generation — 25 Agents in Parallel

**Agents**: 25 (one per module)
**Time**: ~1-2 hours (all parallel)
**Input**: Per-module parameter files, strategy docs, Elbert reference
**Output**: `models/alzheimers/modules/{module_name}.yaml`

Each agent builds a complete ModuleSpec YAML for one module.

### Agent Template (for module M)

```
You are a systems biology module builder. You will create a complete antimony_bootstrap ModuleSpec YAML for the "{MODULE_NAME}" module of an Alzheimer's disease ODE model.

## Your inputs:

1. Module parameters: Read data/parameters/module/{MODULE_NAME}.json
2. Strategy document: Read plan/strategy_{STRATEGY_DOC}.md
3. Elbert reference model: Read ../Elbert_Esguerra_model_v2026b/ for species names, rate laws, and parameter values
4. Schema reference: Read src/antimony_bootstrap/schema/ for ModuleSpec, ReactionSpec, ParameterSpec definitions
5. Existing module examples: Read any existing files in models/alzheimers/modules/ for format reference

## Module specification:

Name: {MODULE_NAME}
Tier: {TIER}
Compartments: {COMPARTMENT_LIST}
Key species: {SPECIES_LIST}
Expected reactions: {REACTION_COUNT_RANGE}
Rate law types: {RATE_TYPES}

## Requirements:

1. Follow the ModuleSpec Pydantic schema exactly
2. Use Elbert species naming convention: {species}_{compartment}
3. Every reaction needs:
   - Descriptive name
   - Reactants and products with stoichiometry
   - Rate type from: MA, RMA, BDF, UDF, custom_conc_per_time, custom_amt_per_time, custom
   - Rate equation string
   - All parameters referenced in the rate equation
   - `evidence`: EvidenceRef list for the reaction's biological existence (PMID, snippet)
   - `rate_law_evidence`: EvidenceRef list for the rate equation form and specific terms.
     Use the `supports` field to indicate what part of the equation the citation justifies.
     Examples:
       - supports: "Michaelis-Menten functional form for BACE1 cleavage"
       - supports: "k2 * monomer^n2 * fibril term (secondary nucleation)"
       - supports: "Hill coefficient n=2 for cooperative binding"
       - supports: "bidirectional transport via LRP1/RAGE"
     This is REQUIRED for every custom rate equation. Mass action reactions need at least
     one EvidenceRef justifying why mass action is appropriate.
4. Every parameter needs:
   - Name matching the rate equation reference
   - Numeric value (from extracted parameters, Elbert, or steady-state estimate)
   - Units in standard convention (nM, L, hr)
   - Confidence level: measured, estimated, or assumed
   - Source with PMID where available
   - `evidence`: list of EvidenceRef with pmid, snippet quoting the value, and source
5. Species need initial amounts/concentrations
6. Include assignment rules for derived quantities where appropriate

## Parameter sourcing priority:
1. Elbert_Esguerra_model_v2026b (copy directly)
2. data/parameters/module/{MODULE_NAME}.json (extracted from literature)
3. Steady-state estimation: k_prod = k_deg × [Species]_ss
4. Order-of-magnitude from analogous reactions

## Output:
Write the complete YAML to: models/alzheimers/modules/{MODULE_NAME}.yaml

Also write a brief build report to: models/alzheimers/modules/{MODULE_NAME}.build_report.md
containing:
- Number of reactions, species, parameters
- Parameter coverage (measured/estimated/assumed counts)
- Any assumptions or gaps noted
- Cross-module species dependencies (what this module imports/exports)
```

### Module-Specific Agent Assignments

| Agent | Module | Strategy Doc | Compartments | Est. Reactions |
|-------|--------|-------------|--------------|----------------|
| 1 | `abeta_production` | strategy_amyloid_cascade.md | Neuron, BrainISF | 15-25 |
| 2 | `abeta_transport` | strategy_vascular_bbb.md | BrainISF, CSF, Plasma, BBB | 20-30 |
| 3 | `abeta_aggregation` | strategy_amyloid_cascade.md | BrainISF, BrainParenchyma | 20-40 |
| 4 | `abeta_clearance` | strategy_amyloid_cascade.md | BrainISF, Microglia, Perivascular | 15-25 |
| 5 | `tau_phosphorylation` | strategy_tau_pathology.md | Neuron | 15-25 |
| 6 | `tau_aggregation` | strategy_tau_pathology.md | Neuron | 10-20 |
| 7 | `neuroinflammation_microglia` | strategy_neuroinflammation.md | Microglia, BrainISF | 30-50 |
| 8 | `neuroinflammation_astrocyte` | strategy_neuroinflammation.md | Astrocyte, BrainISF | 20-30 |
| 9 | `oxidative_stress` | strategy_synaptic_neuronal.md | Neuron, Mitochondria | 15-25 |
| 10 | `synaptic_dysfunction` | strategy_synaptic_neuronal.md | Synapse, Neuron | 20-30 |
| 11 | `calcium_homeostasis` | strategy_synaptic_neuronal.md | Neuron, ER, Mitochondria | 15-25 |
| 12 | `apoptosis_neuronal_death` | strategy_synaptic_neuronal.md | Neuron | 10-20 |
| 13 | `lipid_metabolism` | strategy_lipid_apoe.md | Astrocyte, BrainISF | 20-30 |
| 14 | `insulin_signaling` | strategy_synaptic_neuronal.md | Neuron | 15-25 |
| 15 | `autophagy_proteostasis` | strategy_synaptic_neuronal.md | Neuron | 15-25 |
| 16 | `metal_homeostasis` | strategy_synaptic_neuronal.md | Neuron, BrainISF | 10-15 |
| 17 | `bbb_integrity` | strategy_vascular_bbb.md | BBB, BrainISF, Plasma | 15-25 |
| 18 | `vascular_caa` | strategy_vascular_bbb.md | Perivascular, BrainParenchyma | 10-20 |
| 19 | `apoe_genetics` | strategy_lipid_apoe.md | BrainISF | 5-15 |
| 20 | `presenilin_mutations` | strategy_amyloid_cascade.md | Neuron | 5-10 |
| 21 | `app_genetics` | strategy_amyloid_cascade.md | Neuron | 5-10 |
| 22 | `trem2_signaling` | strategy_neuroinflammation.md | Microglia | 5-10 |
| 23 | `peripheral_immune` | strategy_neuroinflammation.md | Plasma, BrainISF | 10-20 |
| 24 | `complement_cascade` | strategy_neuroinflammation.md | BrainISF, Synapse | 10-15 |
| 25 | `model_manifest` | strategy_module_decomposition.md | (all shared) | N/A — manifest only |

---

## Step 4: Validation & Fix — 25 Agents in Parallel

**Agents**: 25 (one per module)
**Time**: ~30-60 minutes (all parallel)
**Input**: Module YAMLs from Step 3
**Output**: Validated module YAMLs (fixed in place)

Each agent validates its module through the 4-level validation SOP and fixes any issues.

### Agent Template (for module M)

```
You are a model validation and repair agent. You will validate and fix the module YAML at models/alzheimers/modules/{MODULE_NAME}.yaml.

## Validation sequence (run each, fix errors, re-run until passing):

1. Schema validation:
   cd /Users/jtr4v/PythonProject/antimony_bootstrap
   just validate-modules

   If this fails: fix the YAML to match the Pydantic ModuleSpec schema.
   Read src/antimony_bootstrap/schema/ to understand the expected structure.

2. Assembly:
   just assemble

   If this fails: fix species naming conflicts, missing compartments, or duplicate definitions.

3. Antimony parse:
   just validate-antimony

   If this fails: fix rate law syntax, undefined species references, or unit mismatches.

4. Smoke test:
   just smoke-test

   If this fails with NaN/Inf:
   - Check for division by zero in rate equations
   - Check for missing initial conditions (species with 0 initial amount in denominators)
   - Check for extremely large rate constants causing stiffness
   - Reduce any rate constant > 1e6 to 1e6 and flag as needs_review

## Retry logic:
- After each fix, re-run the failing validation step
- Maximum 5 fix-validate cycles per level
- If still failing after 5 attempts, write the error to models/alzheimers/modules/{MODULE_NAME}.validation_errors.txt and move to the next level

## Output:
- Fixed YAML in place at models/alzheimers/modules/{MODULE_NAME}.yaml
- Validation report at models/alzheimers/modules/{MODULE_NAME}.validation_report.md
  containing: pass/fail for each level, fixes applied, any remaining issues
```

---

## Step 5: Cross-Module Integration — 5 Agents (Tiered)

**Agents**: 5 (sequential tiers, but agents within can be parallel)
**Time**: ~1-2 hours (sequential tiers, ~15-30 min each)
**Input**: Validated module YAMLs from Step 4
**Output**: Integrated model `.ant` files at each tier

Integration must be sequential because each tier depends on the previous.

### Agent 1: Tier 1 Core (Amyloid + Tau)

```
You are a model integration agent. Integrate the Tier 1 core modules into a working Antimony model.

Modules to integrate:
- abeta_production
- abeta_transport
- abeta_aggregation
- abeta_clearance
- tau_phosphorylation
- tau_aggregation

Steps:
1. Read models/alzheimers/model.yaml (manifest) and all 6 module YAMLs
2. Run: just assemble
3. Run: just validate-antimony
4. Run: just smoke-test
5. If smoke test passes, verify:
   - Steady-state AB42_BrainISF is in range 1-10 nM
   - Steady-state AB42_CSF is in range 0.1-2 nM
   - Tau half-life is approximately 11 days (264 hr)
   - pTau/Tau ratio is reasonable (0.1-0.5 at baseline)
6. Fix any integration issues:
   - Shared species conflicts (duplicate definitions)
   - Compartment volume mismatches
   - Missing cross-module species references
7. Write integration report to models/alzheimers/integration_tier1_report.md
8. Save working .ant file as models/alzheimers/output/alzheimers_tier1.ant
```

### Agent 2: Tier 2 Addition (Cellular Response)

```
You are a model integration agent. Add Tier 2 modules to the working Tier 1 model.

Starting point: models/alzheimers/output/alzheimers_tier1.ant (must exist and pass smoke test)

Modules to add:
- neuroinflammation_microglia
- neuroinflammation_astrocyte
- oxidative_stress
- synaptic_dysfunction
- calcium_homeostasis
- apoptosis_neuronal_death

Steps:
1. Update model.yaml manifest to include Tier 2 modules
2. Run: just assemble
3. Run: just validate-antimony
4. Run: just smoke-test
5. Verify:
   - AB42 oligomers trigger microglial activation (M0 → DAM transition)
   - TNFa/IL1b produced by activated microglia
   - Synaptic loss correlates with oligomer exposure
   - No NaN/Inf in any species trajectory
6. Fix integration issues, especially cross-module species wiring:
   - AB42_oligo_BrainISF from aggregation → synaptic, neuroinflammation
   - pTau_Neuron from tau → apoptosis
   - TNFa_BrainISF from microglia → astrocyte, bbb
   - ROS_Neuron from oxidative → calcium, apoptosis
7. Write integration report to models/alzheimers/integration_tier2_report.md
8. Save as models/alzheimers/output/alzheimers_tier2.ant
```

### Agent 3: Tier 3 Addition (Modulatory Pathways)

```
You are a model integration agent. Add Tier 3 modules to the working Tier 1+2 model.

Starting point: models/alzheimers/output/alzheimers_tier2.ant

Modules to add:
- lipid_metabolism
- insulin_signaling
- autophagy_proteostasis
- metal_homeostasis
- bbb_integrity
- vascular_caa

Steps:
1. Update model.yaml manifest to include Tier 3 modules
2. Run: just assemble && just validate-antimony && just smoke-test
3. Verify:
   - ApoE_BrainISF modulates AB42 clearance
   - BBB integrity affects AB42 transport
   - Insulin signaling affects GSK3b activity (tau phosphorylation)
   - Autophagy modulates protein aggregate clearance
4. Fix integration issues — Tier 3 modules mostly modulate Tier 1+2 via shared species
5. Write report and save as models/alzheimers/output/alzheimers_tier3.ant
```

### Agent 4: Tier 4 Addition (Genetics & Systemic)

```
You are a model integration agent. Add Tier 4 modules to the working Tier 1+2+3 model.

Starting point: models/alzheimers/output/alzheimers_tier3.ant

Modules to add:
- apoe_genetics
- presenilin_mutations
- app_genetics
- trem2_signaling
- peripheral_immune
- complement_cascade

Steps:
1. Update manifest, assemble, validate, smoke-test
2. Verify genetic modifier modules correctly alter parameters:
   - ApoE4 genotype: reduced clearance, increased aggregation
   - Swedish APP mutation: increased BACE1 cleavage rate
   - PSEN1 mutations: altered gamma-secretase AB42/40 ratio
   - TREM2 R47H: impaired microglial DAM transition
3. Fix integration issues — genetic modules are mostly parameter modifiers
4. Write report and save as models/alzheimers/output/alzheimers_tier4.ant
```

### Agent 5: Final Integration & Full QC

```
You are the final integration and quality control agent. Perform comprehensive validation of the complete 25-module Alzheimer's model.

Starting point: models/alzheimers/output/alzheimers_tier4.ant

Steps:
1. Run full QC: just qc
2. Run extended simulation:
   - Baseline: 10,000 hr (>1 year) simulation
   - Check all species reach steady state or reasonable trajectory
   - No NaN, Inf, or negative concentrations
3. Perturbation tests:
   - BACE1 inhibition (50% reduction): AB42 decreases, tau unaffected short-term
   - GSK3b activation (2x): pTau increases, downstream effects
   - ApoE4 genotype: increased AB42, reduced clearance
   - Anti-TNFa (50% reduction): reduced neuroinflammation
4. Clinical biomarker validation:
   - CSF AB42: 0.5-2 nM range
   - CSF p-tau181: within published ranges
   - AB42 production rate: consistent with SILK data
5. Model statistics report:
   - Total species, reactions, parameters
   - Parameters by confidence level
   - Cross-module dependency graph
6. Write comprehensive report: models/alzheimers/output/final_validation_report.md
7. Save final model: models/alzheimers/output/alzheimers_full.ant
```

---

## Step 6: Parameterization Refinement — 25 Agents in Parallel

**Agents**: 25 (one per module)
**Time**: ~1-2 hours (all parallel)
**Input**: Integrated model, consolidated parameter database, Elbert reference
**Output**: Fully parameterized module YAMLs

### Agent Template (for module M)

```
You are a parameter refinement agent for the {MODULE_NAME} module.

## Inputs:
- Module YAML: models/alzheimers/modules/{MODULE_NAME}.yaml
- Extracted parameters: data/parameters/module/{MODULE_NAME}.json
- Consolidated parameters: data/parameters/consolidated_parameters.json
- Elbert reference: ../Elbert_Esguerra_model_v2026b/

## Tasks:

1. Cross-reference every parameter in the module YAML against:
   a. Elbert model values (highest priority — copy if within reasonable range)
   b. Extracted literature values (second priority)
   c. Current value in YAML

2. For any parameter still set to null, 0, or placeholder:
   a. Try steady-state estimation: k_prod = k_deg × [Species]_ss
   b. Try analogous reaction scaling
   c. Use order-of-magnitude estimate as last resort
   d. NEVER leave a parameter as null — the model must simulate

3. Assign confidence levels:
   - measured: value directly from Elbert or primary literature with PMID
   - estimated: derived from related data, scaling, or steady-state calculation
   - assumed: order-of-magnitude guess or analogy

4. Verify unit consistency:
   - All concentrations in nM
   - All times in hr
   - All volumes in L
   - All 1st-order rate constants in 1/hr
   - All 2nd-order rate constants in 1/(nM·hr)

5. Check parameter reasonableness:
   - No rate constant > 1e8 or < 1e-15
   - No concentration > 1e6 nM (1 mM) or < 0 (no negative concentrations)
   - Half-lives between 1 second (0.00028 hr) and 100 years (876,000 hr)

6. Update the YAML in place with refined parameters
7. Re-run: just validate-modules && just assemble && just validate-antimony && just smoke-test
8. Write refinement report: models/alzheimers/modules/{MODULE_NAME}.param_report.md
   - Parameters changed (old → new)
   - Confidence distribution
   - Remaining gaps or concerns
```

---

## Step 7: Sensitivity Analysis & Calibration — 10 Agents in Parallel

**Agents**: 10
**Time**: ~1-2 hours (all parallel)
**Input**: Fully parameterized model from Steps 5-6
**Output**: Sensitivity reports and parameter adjustments

### Agent Assignments

| Agent | Focus | Perturbation Tests |
|-------|-------|--------------------|
| 1 | Amyloid pathway sensitivity | BACE1 ±50%, gamma-secretase ±50%, NEP ±50%, IDE ±50% |
| 2 | Tau pathway sensitivity | GSK3b ±50%, PP2A ±50%, CDK5 ±50% |
| 3 | Clearance pathway sensitivity | LRP1 ±50%, RAGE ±50%, ApoE ±50%, glymphatic ±50% |
| 4 | Neuroinflammation sensitivity | TNFa prod ±50%, IL1b prod ±50%, TREM2 ±50% |
| 5 | Synaptic/neuronal sensitivity | AMPAR ±50%, CaMKII ±50%, calcineurin ±50% |
| 6 | Drug target simulations | BACE1 inhibitor, anti-AB42 antibody, anti-tau antibody, anti-TNFa |
| 7 | Genetic variant effects | ApoE2/3/4, Swedish APP, PSEN1, TREM2 R47H |
| 8 | Timescale validation | 1hr, 24hr, 1week, 1month, 1year, 10year simulations |
| 9 | Mass conservation checks | Verify conservation laws, no species creation from nothing |
| 10 | Clinical calibration | Fit to DIAN-TU biomarker trajectories, SILK kinetics, CSF ranges |

### Agent Template (for agent N)

```
You are a sensitivity analysis agent for an Alzheimer's disease ODE model.

## Your focus: {FOCUS_AREA}

## Setup:
1. Load the full model: models/alzheimers/output/alzheimers_full.ant
2. Use tellurium/roadrunner for simulation

## Perturbation tests to run:
{PERTURBATION_LIST}

For each perturbation:
1. Load baseline model
2. Modify the specified parameter(s)
3. Simulate for appropriate timescale (acute: 100 hr, chronic: 10,000 hr)
4. Record:
   - Key species trajectories (AB42_BrainISF, pTau_Neuron, TNFa_BrainISF, Neuron_count, Synapse_count)
   - Steady-state values (or final values if not at steady state)
   - Percent change from baseline for each key species
   - Time to reach new steady state (if applicable)
5. Flag any unexpected behaviors:
   - Wrong direction of change
   - Unreasonable magnitude
   - Oscillations or instability
   - Species going negative

## Output:
Write: models/alzheimers/output/sensitivity_{AGENT_NUM:02d}_{FOCUS}.md
Write: models/alzheimers/output/sensitivity_{AGENT_NUM:02d}_{FOCUS}.json (machine-readable results)

If parameter adjustments are needed, write recommended changes to:
models/alzheimers/output/param_adjustments_{AGENT_NUM:02d}.json
Format: [{"module": "...", "parameter": "...", "current_value": N, "recommended_value": M, "reason": "..."}]
```

---

## Timeline Summary

| Step | Agents | Wall Time | Depends On | Output |
|------|--------|-----------|------------|--------|
| 0: Paper Index | 1 | 30-60 min | — | `data/paper_index.json`, tier files |
| 1: Deep Reading | 100 | 1-2 hr | Step 0 | `data/extracted/all_papers.json` |
| 2: Parameter Extraction | 50 | 1-2 hr | Step 0 | `data/parameters/consolidated_parameters.json` |
| 3: Module YAML Gen | 25 | 1-2 hr | Steps 1, 2 | 25 module YAMLs |
| 4: Validation & Fix | 25 | 30-60 min | Step 3 | 25 validated YAMLs |
| 5: Integration | 5 (seq) | 1-2 hr | Step 4 | `alzheimers_full.ant` |
| 6: Param Refinement | 25 | 1-2 hr | Step 5 | Refined YAMLs |
| 7: Sensitivity | 10 | 1-2 hr | Step 6 | Sensitivity reports |

**Steps 1 and 2 run in parallel** (both depend only on Step 0).

**Total wall time**: ~6-12 hours (vs. 16 weeks sequential)
**Total agent-hours**: ~200-300 agent-hours of compute

---

## Dependency Graph

```
Step 0 ──┬──→ Step 1 (100 agents) ──┐
         │                           ├──→ Step 3 (25 agents) ──→ Step 4 (25 agents) ──→ Step 5 (5 agents, sequential)
         └──→ Step 2 (50 agents)  ──┘                                                        │
                                                                                              ↓
                                                                                   Step 6 (25 agents) ──→ Step 7 (10 agents)
```

---

## Orchestrator Script (Main Session)

The main Claude Code session acts as orchestrator. Pseudocode:

```python
# Step 0: Synchronous
launch_agent(step0_prompt)
wait_for_completion()
verify("data/paper_index.json")

# Steps 1 & 2: Parallel
agents_step1 = [launch_agent(step1_prompt(i), background=True) for i in range(100)]
agents_step2 = [launch_agent(step2_prompt(i), background=True) for i in range(50)]
wait_for_all(agents_step1 + agents_step2)
run_merge_step1()
run_merge_step2()

# Step 3: Parallel (depends on 1+2)
agents_step3 = [launch_agent(step3_prompt(module), background=True) for module in MODULES_25]
wait_for_all(agents_step3)

# Step 4: Parallel
agents_step4 = [launch_agent(step4_prompt(module), background=True) for module in MODULES_25]
wait_for_all(agents_step4)

# Step 5: Sequential tiers
for tier_agent in [tier1, tier2, tier3, tier4, final]:
    launch_agent(tier_agent_prompt)
    wait_for_completion()

# Step 6: Parallel
agents_step6 = [launch_agent(step6_prompt(module), background=True) for module in MODULES_25]
wait_for_all(agents_step6)

# Step 7: Parallel
agents_step7 = [launch_agent(step7_prompt(i), background=True) for i in range(10)]
wait_for_all(agents_step7)
```

---

## Risk Mitigation for Parallel Execution

| Risk | Mitigation |
|------|-----------|
| Agent writes to wrong file path | Deterministic output paths per agent; verify before merge |
| Agent produces malformed JSON | Merge step validates JSON schema before aggregation |
| Two agents modify same file | Each agent owns exactly one output path; no shared writes |
| Agent hangs or fails silently | Check `TaskOutput(block=False)` periodically; timeout at 2hr |
| Rate limiting on codex API | Stagger launches by 5-10 seconds; retry failed agents |
| Merge conflicts in module integration | Sequential tier integration (Step 5) prevents parallel conflicts |
| Parameter inconsistency across modules | Step 6 cross-references all modules against single consolidated DB |
| Disk space for outputs | Each batch JSON is ~1-5 MB; total < 1 GB |

---

## Appendix A: Preserved Reference Material

The following reference material from the original plan remains valid and should be consulted by agents:

### Corpus Statistics
- ~200-400 papers with directly extractable kinetic parameters
- ~1,500 papers with mechanistic pathway information
- ~1,000 papers with calibration data (biomarker levels, imaging, clinical)
- ~500 papers with limited ODE relevance

### 25-Module Architecture (4 Tiers)

**Tier 1 — Core Pathology** (~100-160 reactions):
`abeta_production`, `abeta_transport`, `abeta_aggregation`, `abeta_clearance`, `tau_phosphorylation`, `tau_aggregation`

**Tier 2 — Cellular Response** (~130-190 reactions):
`neuroinflammation_microglia`, `neuroinflammation_astrocyte`, `oxidative_stress`, `synaptic_dysfunction`, `calcium_homeostasis`, `apoptosis_neuronal_death`

**Tier 3 — Modulatory Pathways** (~100-170 reactions):
`lipid_metabolism`, `insulin_signaling`, `autophagy_proteostasis`, `metal_homeostasis`, `bbb_integrity`, `vascular_caa`

**Tier 4 — Genetic & Systemic** (~40-85 reactions):
`apoe_genetics`, `presenilin_mutations`, `app_genetics`, `trem2_signaling`, `peripheral_immune`, `complement_cascade`

**Total: ~370-625 reactions across 25 modules**

### Shared Compartments

| Compartment | Volume (L) |
|-------------|-----------|
| BrainISF | 0.25 |
| CSF | 0.14 |
| Plasma | 3.0 |
| Neuron | 0.5 |
| Microglia | 0.0005 |
| Astrocyte | 0.001 |
| Synapse | 0.0001 |
| Mitochondria | 0.0001 |
| ER | 0.0001 |
| BBB | 0.0001 |
| BrainParenchyma | 1.0 |
| Perivascular | 0.01 |

### Critical Shared Species (Cross-Module Interfaces)

| Species | Producer Module | Consumer Modules |
|---------|----------------|-----------------|
| `AB42_BrainISF` | abeta_production | aggregation, clearance, transport, neuroinflammation, synaptic |
| `AB42_oligo_BrainISF` | abeta_aggregation | synaptic_dysfunction, neuroinflammation, calcium |
| `pTau_Neuron` | tau_phosphorylation | tau_aggregation, apoptosis |
| `NFT_Neuron` | tau_aggregation | apoptosis, neuroinflammation |
| `TNFa_BrainISF` | neuroinflammation_microglia | astrocyte, bbb_integrity, apoptosis |
| `IL1b_BrainISF` | neuroinflammation_microglia | astrocyte, synaptic |
| `ROS_Neuron` | oxidative_stress | calcium, mitochondrial, apoptosis |
| `Ca_cyt_Neuron` | calcium_homeostasis | synaptic, apoptosis, tau_phosphorylation |
| `Neuron_count` | apoptosis | synaptic, neurotransmitters |
| `ApoE_BrainISF` | lipid_metabolism | abeta_clearance, abeta_transport |
| `Plaque_BrainParenchyma` | abeta_aggregation | neuroinflammation, complement |

### Parameter Ranges

| Reaction Type | Parameter | Typical Range | Units |
|---------------|-----------|---------------|-------|
| AB42 production | k_prod | 1e-12 to 1e-10 | mol/hr |
| AB42 ISF degradation | t_half | 7-14 | hr |
| AB42 ISF-to-CSF transport | k_transport | 0.02-0.05 | 1/hr |
| AB42 BBB efflux (LRP1) | Vmax | 1-10 | nmol/hr |
| AB42 BBB efflux (LRP1) | Km | 10-100 | nM |
| Nucleation | k_nuc | 1e-8 to 1e-5 | M^-1 hr^-1 |
| Fibril elongation | k_elong | 1e3-1e6 | M^-1 hr^-1 |
| Tau production | k_prod | ~0.02 | nmol/hr |
| Tau ISF half-life | t_half | ~11 | days |
| GSK3b Vmax | Vmax | 0.1-1.0 | nM/hr |
| Cytokine half-lives | t_half | 0.3-3 | hr |

### Unit Conventions

| Quantity | Unit |
|----------|------|
| Concentration | nM |
| Amount | nmol |
| Volume | L |
| Time | hr |
| Rate constants (1st order) | 1/hr |
| Rate constants (2nd order) | 1/(nM·hr) |

### Strategy Documents

| Document | Location |
|----------|----------|
| Module Decomposition | `plan/strategy_module_decomposition.md` |
| NLP Extraction Pipeline | `plan/strategy_nlp_extraction.md` |
| Amyloid Cascade | `plan/strategy_amyloid_cascade.md` |
| Tau Pathology | `plan/strategy_tau_pathology.md` |
| Neuroinflammation | `plan/strategy_neuroinflammation.md` |
| Synaptic/Neuronal | `plan/strategy_synaptic_neuronal.md` |
| Vascular/BBB | `plan/strategy_vascular_bbb.md` |
| Lipid/ApoE | `plan/strategy_lipid_apoe.md` |
| Existing Models | `plan/strategy_existing_models.md` |
| Parameterization | `plan/strategy_parameterization.md` |
