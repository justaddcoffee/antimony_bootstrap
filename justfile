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

# --- BioModels MCP Server ---

# Clone BioModelsRAG_MCP into vendor/
mcp-download:
    mkdir -p vendor
    @if [ ! -d vendor/BioModelsRAG_MCP ]; then \
        git clone https://github.com/DylanEsguerra/BioModelsRAG_MCP.git vendor/BioModelsRAG_MCP; \
    else \
        echo "vendor/BioModelsRAG_MCP already exists, skipping clone"; \
    fi

# Create venv and install deps for BioModelsRAG_MCP
mcp-setup: mcp-download
    @if [ ! -d vendor/BioModelsRAG_MCP/venv ]; then \
        python3 -m venv vendor/BioModelsRAG_MCP/venv; \
    fi
    vendor/BioModelsRAG_MCP/venv/bin/pip install -q -r vendor/BioModelsRAG_MCP/requirements.txt

# Install MCP server (download + setup) and generate .mcp.json
mcp-install: mcp-setup
    @echo '{"mcpServers":{"biomodels-rag":{"type":"stdio","command":"'"$(pwd)"'/vendor/BioModelsRAG_MCP/venv/bin/python3","args":["'"$(pwd)"'/vendor/BioModelsRAG_MCP/mcp_server.py"]}}}' | python3 -m json.tool > .mcp.json
    @echo "Wrote .mcp.json — restart Claude Code to pick up the MCP server"
