# antimony_bootstrap

Extract known disease mechanisms from biological knowledge sources and produce fully parameterized Antimony ODE models.

## TODO

- **Equation extraction from literature is broken.** The parallel LLM extraction pipeline (Steps 1-2 in `plan/PLAN.md`) successfully identifies papers, species, pathways, and parameter metadata, but does not actually extract ODE equations from the papers. The `rate_equation` fields in `data/extracted/all_papers.json` are virtually all empty. Root causes: (1) PMC XML stores equations as MathML or images, which the XML text parser cannot read, and (2) the extraction prompts asked agents to synthesize equations from prose, which they consistently skipped. The module YAMLs that contain equations (`models/alzheimers/modules/*.yaml`) were sourced from the Elbert reference model, not extracted from the corpus. A working equation extraction pipeline would need MathML parsing, equation image OCR, or a more targeted LLM prompting strategy.
