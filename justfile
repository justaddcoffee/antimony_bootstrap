# antimony_bootstrap justfile

# Install dependencies
install:
    uv sync

# Run tests
test:
    uv run pytest tests/ -v

# Validate a module YAML against Pydantic schema
validate-module file:
    uv run antimony-bootstrap validate-module {{file}}

# Validate all modules for a disease
validate-modules disease="alzheimers":
    uv run antimony-bootstrap validate-modules --disease {{disease}}

# Check parameter completeness
validate-params disease="alzheimers":
    uv run antimony-bootstrap validate-params --disease {{disease}}

# Compose modules into Antimony
assemble disease="alzheimers":
    uv run antimony-bootstrap assemble --disease {{disease}}

# Parse check with antimony library
validate-antimony disease="alzheimers":
    uv run antimony-bootstrap validate-antimony --disease {{disease}}

# Quick tellurium simulation
smoke-test disease="alzheimers":
    uv run antimony-bootstrap smoke-test --disease {{disease}}

# Full pipeline: schema + assemble + validate + simulate
qc disease="alzheimers":
    uv run antimony-bootstrap qc --disease {{disease}}

# Extract mechanisms from dismech YAML
read-dismech file:
    uv run antimony-bootstrap read-dismech {{file}}

# Search BioModels API
search-biomodels query:
    uv run antimony-bootstrap search-biomodels "{{query}}"

# Generate parameter provenance report
provenance disease="alzheimers":
    uv run antimony-bootstrap provenance --disease {{disease}}
