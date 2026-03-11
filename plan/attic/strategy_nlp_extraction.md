# Strategy: NLP-Based Extraction of Biological Mechanisms, Kinetic Parameters, and Reaction Networks from Scientific Papers

**Date**: 2026-02-24
**Context**: antimony_bootstrap -- automating extraction of disease mechanisms for ODE modeling

---

## 1. Problem Statement

We need to process 3000+ scientific papers (PMC XML format) to extract:
- **Species** (proteins, metabolites, drugs, cell types)
- **Reactions** (enzymatic, binding, transport, degradation)
- **Kinetic parameters** (rate constants, Km, Vmax, IC50, half-lives)
- **Causal mechanisms** (A activates B, C inhibits D)
- **Compartment context** (brain ISF, plasma, CSF, intracellular)

And map these to ODE model structures compatible with Antimony/SBML.

---

## 2. Pipeline Architecture Overview

```
PMC XML -> Parsing -> Section Segmentation -> Parallel Extraction Tracks -> Knowledge Graph -> ODE Mapping
                                                |
                            +-------------------+-------------------+
                            |                   |                   |
                      Text Extraction     Table Extraction    Figure Caption
                      (NER + RE)          (Parameter Mining)  Extraction
                            |                   |                   |
                            +-------------------+-------------------+
                                                |
                                        Consolidation & Dedup
                                                |
                                        ModuleSpec YAML Output
```

---

## 3. Stage 1: Document Parsing and Preprocessing

### 3.1 PMC XML Parsing

PMC XML (JATS/NLM DTD) is well-structured. Key elements to extract:

```python
# Priority sections for mechanism extraction
SECTIONS_OF_INTEREST = {
    "abstract": "high-level mechanism summaries",
    "introduction": "established mechanisms, motivation",
    "methods": "model equations, parameter estimation details",
    "results": "quantitative findings, measured parameters",
    "discussion": "mechanistic interpretations",
    "supplementary-material": "often contains full parameter tables",
}
```

**Recommended tools**:
- `lxml` for XML parsing (fast, reliable for JATS DTD)
- `pubget` (Python package for bulk PMC download + parse)
- Custom JATS parser that preserves section hierarchy, table structures, and inline references

### 3.2 Section Segmentation Strategy

Not all sections are equally valuable:

| Section | Species | Reactions | Parameters | Mechanisms |
|---------|---------|-----------|------------|------------|
| Abstract | Medium | Low | Low | High |
| Introduction | High | Medium | Low | High |
| Methods/Model | High | High | High | High |
| Results | Medium | Medium | High | Medium |
| Tables | Low | Low | Very High | Low |
| Supplementary | Medium | High | Very High | Medium |

**Recommendation**: Prioritize Methods/Model sections and Tables for parameter extraction. Use Abstract + Introduction for mechanism/species identification.

---

## 4. Stage 2: Entity Recognition (NER)

### 4.1 Traditional NLP Approaches

**Pre-trained biomedical NER models**:

| Model | Entities | Performance | Notes |
|-------|----------|-------------|-------|
| **PubMedBERT + BioBERT** | Proteins, chemicals, diseases | F1 ~87-92% | Best general-purpose biomedical NER |
| **BERN2** | Genes, diseases, chemicals, species, mutations | F1 ~89% | Ensemble model, good API |
| **HunFlair2** (Flair) | Proteins, chemicals, diseases, cell lines | F1 ~85-90% | Easy to use, good for batch |
| **SciSpacy** (en_core_sci_lg) | Broad biomedical entities | F1 ~82% | SpaCy-based, fast |
| **OGER** | Any ontology-backed entity | Depends on dict | Dictionary-based, very fast |
| **GNormPlus** | Genes/proteins specifically | F1 ~87% | NCBI tool, gene normalization |

**For our use case**, the critical entity types are:

1. **Proteins/Genes**: AB42, tau, BACE1, APP, ApoE -- use PubMedBERT fine-tuned on CRAFT/BC5CDR
2. **Metabolites/Small molecules**: glucose, glutamate, cholesterol -- use ChemBERT or BERN2
3. **Drugs**: donepezil, lecanemab, aducanumab -- use RxNorm-backed dictionary + NER
4. **Cell types**: microglia, astrocytes, neurons -- use Cell Ontology dictionary lookup
5. **Compartments**: brain, plasma, CSF, extracellular -- custom dictionary from Elbert model
6. **Numerical values + units**: "k = 0.05 h-1", "Km = 2.3 uM" -- regex + custom NER

### 4.2 LLM-Based Entity Recognition

**Claude/GPT approach** (structured extraction):

```python
ENTITY_EXTRACTION_PROMPT = (
    "Given this paragraph from a biomedical paper, extract all biological entities:\n"
    "{paragraph}\n"
    "Return JSON with keys: proteins, metabolites, drugs, cell_types, compartments, parameters"
)
```

**LLM advantages**:
- Handles ambiguity well ("tau" as protein vs. time constant)
- Can resolve coreferences ("the enzyme" -> BACE1)
- Understands context-dependent meaning
- Can normalize names to standard identifiers

**LLM disadvantages**:
- Cost at scale (3000 papers x ~50 paragraphs x $0.01-0.03/call = $1,500-$4,500)
- Rate limits
- Hallucination risk for IDs (UniProt, ChEBI)
- Slower than dictionary/ML approaches

### 4.3 Recommended Hybrid Approach

```
Step 1: Fast dictionary-based pre-annotation (OGER + custom dictionaries)
        -> Catches known entities with high precision
        -> Maps to ontology IDs immediately

Step 2: PubMedBERT NER for entities missed by dictionary
        -> Catches novel/variant names
        -> F1 ~90% on biomedical text

Step 3: LLM pass on ambiguous/complex paragraphs only
        -> Resolve "the protein" coreferences
        -> Disambiguate context-dependent terms
        -> ~10-20% of paragraphs need this
```

**Estimated cost**: Dictionary (free) + PubMedBERT (GPU time ~$50) + Claude for 20% of paragraphs (~$500) = ~$550 total.

---

## 5. Stage 3: Relation Extraction (Causal Mechanisms)

### 5.1 What We Need to Extract

For ODE modeling, we need directed causal relations:

```
Subject -> Relation -> Object [with modifiers]

Examples:
  BACE1 -> cleaves -> APP [in endosome, producing sAPPbeta and C99]
  Microglia -> phagocytose -> AB42_oligomers [rate depends on TREM2 expression]
  Insulin -> activates -> IDE [Km = 100 nM, Vmax = 0.5 uM/min]
  AB42 -> inhibits -> LTP [IC50 = 200 nM, in hippocampus]
```

### 5.2 Traditional NLP for Relation Extraction

**Dependency-parse based approaches**:
- Extract Subject-Verb-Object triples from parsed sentences
- Use biomedical verb lexicons (activates, inhibits, phosphorylates, cleaves, transports)
- Tools: SciSpacy dependency parser + custom relation patterns

**Pre-trained RE models**:

| Model | Relations | Performance |
|-------|-----------|-------------|
| **BioRE-BERT** | Protein-protein interactions | F1 ~82% |
| **REACH/Eidos** (Arizona) | Causal biological events | Good for signaling |
| **INDRA** (Harvard) | Assembly of causal mechanisms | Best existing tool for this exact task |
| **PathIE** | Pathway relations | F1 ~78% |
| **DeepEventMine** | Biomedical events (BioNLP format) | F1 ~80% |

### 5.3 INDRA -- The Most Relevant Existing System

**INDRA** (Integrated Network and Dynamical Reasoning Assembler) from Harvard Medical School is the closest existing system to what we need:

- Reads papers via REACH, Sparser, RLIMS-P, MedScan
- Extracts **Statements**: Activation, Inhibition, Phosphorylation, Complex, etc.
- Assembles into **causal networks**
- Can export to **PySB models** (rule-based, convertible to ODE)
- Has SBML/Antimony-adjacent output capabilities

**INDRA integration strategy**:
```python
from indra.sources import reach, biopax
from indra.assemblers.pysb import PysbAssembler

# Extract statements from text
processor = reach.process_text(paper_text)
statements = processor.statements

# Assemble into model
assembler = PysbAssembler()
assembler.add_statements(statements)
model = assembler.make_model()
```

**Limitation**: INDRA excels at signaling pathways but is weaker for:
- Compartmental transport reactions
- Metabolic rate laws with specific kinetics
- Parameter extraction (focuses on topology, not kinetics)

### 5.4 LLM-Based Relation Extraction

This is where LLMs dramatically outperform traditional NLP. Use structured prompts requesting mechanism type, reactants, products, modifiers, rate law type, parameters mentioned, and evidence sentences.

**Why LLMs excel here**:
- Can understand complex multi-sentence mechanism descriptions
- Can infer implied reactions ("AB42 accumulates in plaques" -> deposition reaction)
- Can handle negation and conditional language
- Can distinguish between established facts and hypotheses
- Can map qualitative descriptions to rate law types

**Cost estimate for RE**: ~$0.05/page x 3000 papers x 15 pages = ~$2,250

### 5.5 Recommended Approach for Relation Extraction

```
Layer 1: INDRA (REACH reader) for known signaling relations
         -> High precision, well-validated, free
         -> Covers ~40% of extractable relations

Layer 2: Rule-based extraction for transport/compartment reactions
         -> Pattern: "species is transported from comp1 to comp2"
         -> Pattern: "species crosses the barrier"
         -> Covers ~15% of relations

Layer 3: Claude structured extraction for remaining text
         -> Complex mechanisms, multi-step processes
         -> Novel/unusual reaction types
         -> Covers remaining ~45%

Consolidation: Merge all three layers, resolve conflicts by confidence
```

---

## 6. Stage 4: Table Extraction for Kinetic Parameters

### 6.1 Why Tables Are Critical

In systems biology papers, **80%+ of usable kinetic parameters** appear in tables, not running text. Common table formats:

- "Table 1: Model Parameters" (rate constants, initial conditions)
- "Table 2: Kinetic Constants" (Km, Vmax, kcat values)
- "Table S1: Supplementary Parameters" (full parameter sets)

### 6.2 PMC XML Table Parsing

PMC XML tables use `<table-wrap>` with `<thead>` and `<tbody>`. Use lxml to parse header rows and data rows directly from the XML structure.

### 6.3 Parameter Extraction from Tables

**Heuristic approach** (fast, works for well-structured tables):
- Match column headers against patterns: parameter/name, value/estimate, unit/dimension, source/reference
- Score tables by caption keywords (parameter, kinetic, rate constant, model, simulation, ODE)
- Score by header content (presence of units like uM, nM, h-1, s-1)
- Classify as parameter table if score >= 5

**LLM approach** (handles messy tables):
- Feed table caption, headers, and rows to Claude
- Request structured extraction of parameter name, symbol, value, units, species context, compartment, source type, and confidence

### 6.4 Unit Standardization

Critical for ODE models -- all parameters must be in consistent units:

| From | To | Factor |
|------|----|--------|
| nM | M | 1e-9 |
| uM | M | 1e-6 |
| mM | M | 1e-3 |
| min | h | 1/60 |
| s | h | 1/3600 |
| day | h | 24 |
| min-1 | h-1 | 60 |
| s-1 | h-1 | 3600 |

### 6.5 Recommended Table Pipeline

```
Step 1: Parse all tables from PMC XML (lxml)
Step 2: Classify tables by type (parameter table? results table? demographics?)
Step 3: For parameter tables with clean structure -> rule-based extraction
Step 4: For complex/merged/multi-level tables -> LLM extraction
Step 5: Unit standardization and validation
Step 6: Cross-reference with text mentions for context
```

---

## 7. Stage 5: Mapping Extracted Knowledge to ODE Structures

### 7.1 From Extracted Relations to ModuleSpec YAML

The mapping from extracted knowledge to antimony_bootstrap's ModuleSpec:

| Extracted Relation | ModuleSpec Component |
|-------------------|---------------------|
| "BACE1 cleaves APP" | ReactionSpec (enzymatic, Michaelis-Menten) |
| "AB42 transported from ISF to CSF" | ReactionSpec (UDF transport) |
| "Microglia activated by AB42" | ReactionSpec (activation, Hill function) |
| "k_clearance = 0.05 h-1" | ParameterSpec (measured, with PMID) |
| "AB42 concentration in ISF" | Species "AB42_BrainISF" |
| "Blood-brain barrier" | Compartment pair (Plasma, BrainISF) |

### 7.2 Rate Law Assignment Logic

- **Transport reactions**: BDF if bidirectional, UDF if unidirectional
- **Enzymatic reactions**: custom_conc_per_time if Km provided, MA otherwise
- **Binding/association**: RMA if reversible, MA otherwise
- **Degradation/clearance**: MA (first-order)
- **Explicit equation provided**: custom
- **Default**: MA

### 7.3 Species Naming Standardization

Species follow Elbert convention: `{species}_{compartment}` (e.g., `AB42_BrainISF`). Use alias dictionaries to map variant names (e.g., "amyloid-beta 42" -> "AB42", "phosphorylated tau" -> "pTau").

### 7.4 Confidence Scoring for Extracted Parameters

Score based on weighted combination of:
- Source quality (40%): measured > fitted > estimated > assumed
- Agreement score (30%): how many papers agree on similar values
- Recency score (10%): newer papers score higher
- Species relevance (20%): human > primate > rodent > in vitro

Overall confidence: >0.7 = measured, >0.4 = estimated, else = assumed.

---

## 8. Scalability: Processing 3000+ Papers

### 8.1 Cost and Time Estimates

| Approach | Time (3000 papers) | Cost | Accuracy |
|----------|-------------------|------|----------|
| Pure LLM (Claude) | ~48 hours | ~$3,000-5,000 | ~85-90% |
| Pure traditional NLP | ~4 hours (GPU) | ~$50 (compute) | ~70-80% |
| **Hybrid (recommended)** | **~12 hours** | **~$800-1,200** | **~88-92%** |
| INDRA only | ~8 hours | Free | ~75% (topology only) |

### 8.2 Recommended Processing Pipeline

```
Phase 1: Bulk preprocessing (2 hours, cheap)
  - Download PMC XML via pubget or E-utilities API
  - Parse XML, extract sections + tables
  - Dictionary-based NER pre-annotation
  - Classify tables (parameter vs. other)
  - Output: structured JSON per paper

Phase 2: ML-based extraction (4 hours, moderate cost)
  - PubMedBERT NER on all text sections
  - INDRA/REACH for relation extraction
  - Rule-based parameter extraction from clean tables
  - Output: preliminary knowledge graph

Phase 3: LLM refinement (6 hours, main cost)
  - Claude for complex/ambiguous paragraphs (~20% of text)
  - Claude for messy table extraction (~30% of tables)
  - Claude for mechanism consolidation and conflict resolution
  - Claude for rate law assignment on novel reactions
  - Output: refined knowledge graph with confidence scores

Phase 4: Assembly and validation (1 hour)
  - Map to ModuleSpec YAML
  - Standardize species names to Elbert convention
  - Unit harmonization
  - Cross-validation against Elbert reference model
  - Output: validated ModuleSpec files
```

### 8.3 Parallelization Strategy

- **CPU-bound** (XML parsing, dictionary NER): ProcessPoolExecutor with 8 workers
- **GPU-bound** (PubMedBERT NER): Batch inference with batch_size=32
- **API-bound** (Claude calls): asyncio with Semaphore(10) for rate limiting

### 8.4 Caching and Incremental Processing

Four-level cache:
- Level 1: Raw parse cache (invalidate if XML changes)
- Level 2: NER cache (invalidate if model changes)
- Level 3: LLM extraction cache (invalidate if prompt changes)
- Level 4: Assembled knowledge graph (rebuild from L1-L3)

---

## 9. Quality Assurance

### 9.1 Validation Against Reference Model

The Elbert model provides ground truth for Alzheimer's. For each extracted parameter, find the matching Elbert parameter and check if the ratio is within 0.1-10x.

### 9.2 Cross-Paper Consistency

Flag parameters with coefficient of variation > 1.0 across papers. Use median values for parameters with high variance.

### 9.3 Human-in-the-Loop Checkpoints

Given antimony_bootstrap's interactive workflow, the pipeline should pause for human review at:

1. **After entity extraction**: Review species list, confirm naming conventions
2. **After relation extraction**: Validate mechanism topology against dismech
3. **After parameterization**: Review parameter values, especially outliers
4. **After assembly**: Run `just qc` before accepting

---

## 10. Tool and Library Summary

### Must-Have
| Tool | Purpose | Install |
|------|---------|---------|
| `lxml` | PMC XML parsing | `pip install lxml` |
| `transformers` + `PubMedBERT` | Biomedical NER | `pip install transformers` |
| `indra` | Mechanism extraction + assembly | `pip install indra` |
| `anthropic` | Claude API for LLM extraction | `pip install anthropic` |
| `pydantic` | Schema validation | Already in project |

### Nice-to-Have
| Tool | Purpose | Install |
|------|---------|---------|
| `scispacy` | Fast biomedical NLP | `pip install scispacy` |
| `biopython` | PubMed/Entrez API | `pip install biopython` |
| `pubget` | Bulk PMC download | `pip install pubget` |
| `chemdataextractor` | Chemical entity + table extraction | `pip install chemdataextractor` |
| `tabula-py` | PDF table extraction (fallback) | `pip install tabula-py` |

### Infrastructure
| Tool | Purpose |
|------|---------|
| SQLite or DuckDB | Parameter database for dedup + querying |
| Redis | Caching layer for API responses |
| Prefect or Airflow | Pipeline orchestration for 3000 papers |

---

## 11. Recommended Implementation Order

### Phase 1 (Week 1-2): Foundation
1. Build PMC XML parser with section segmentation
2. Implement dictionary-based NER with Elbert species list
3. Build table extractor for well-structured parameter tables
4. Create extraction schema (Pydantic models for extracted knowledge)

### Phase 2 (Week 3-4): ML Layer
5. Integrate PubMedBERT NER
6. Set up INDRA for relation extraction
7. Build unit standardization module
8. Create parameter database (SQLite)

### Phase 3 (Week 5-6): LLM Layer
9. Design and test Claude extraction prompts
10. Build hybrid extraction pipeline (dictionary -> ML -> LLM)
11. Implement caching and incremental processing
12. Build confidence scoring system

### Phase 4 (Week 7-8): Integration
13. Map extracted knowledge to ModuleSpec YAML
14. Cross-validate against Elbert reference model
15. Build human review interface (CLI-based)
16. Process pilot batch (100 papers) and validate

### Phase 5 (Week 9-10): Scale
17. Process full 3000 paper corpus
18. Aggregate and deduplicate parameters
19. Generate ModuleSpec files for all identified mechanisms
20. Run full `just qc` validation

---

## 12. Key Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| LLM hallucination of parameter values | Incorrect model | Always require source citation; cross-validate |
| Unit conversion errors | Model simulation failure | Standardize early; validate against Elbert |
| Duplicate/conflicting parameters | Confusion | Dedup by reaction + parameter type; use median |
| PMC XML format variations | Parser failures | Test on diverse journals; graceful fallbacks |
| Cost overrun on LLM calls | Budget | Aggressive caching; tiered processing |
| INDRA dependency complexity | Setup difficulty | Docker containerize INDRA |

---

## 13. Conclusion

The most effective pipeline for processing 3000+ papers combines:

1. **Fast, cheap traditional methods first** (dictionary NER, XML table parsing, INDRA)
2. **ML models for coverage** (PubMedBERT for entities missed by dictionaries)
3. **LLMs for the hard cases** (ambiguous text, complex mechanisms, messy tables)
4. **Human review at key checkpoints** (aligned with antimony_bootstrap's interactive philosophy)

This hybrid approach achieves ~90% extraction accuracy at ~$1,000 total cost, compared to ~$4,000 for pure LLM or ~75% accuracy for pure traditional NLP. The key insight is that most extractable knowledge follows predictable patterns that cheap methods handle well -- LLMs should be reserved for the genuinely difficult 20-30% of cases.
