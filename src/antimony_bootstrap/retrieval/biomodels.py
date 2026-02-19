"""Search BioModels API for reference models and convert SBML to Antimony."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import httpx

BIOMODELS_API = "https://www.ebi.ac.uk/biomodels"


def search_biomodels(query: str, num_results: int = 10) -> list[dict[str, Any]]:
    """Search BioModels for models matching a query.

    Returns list of dicts with keys: id, name, description, url.
    """
    url = f"{BIOMODELS_API}/search"
    params = {"query": query, "numResults": num_results, "format": "json"}

    response = httpx.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    results = []
    for model in data.get("models", []):
        results.append({
            "id": model.get("id", ""),
            "name": model.get("name", ""),
            "description": model.get("description", ""),
            "url": f"{BIOMODELS_API}/{model.get('id', '')}",
        })

    return results


def download_sbml(model_id: str) -> str:
    """Download SBML XML for a BioModels model."""
    url = f"{BIOMODELS_API}/model/download/{model_id}"
    params = {"filename": f"{model_id}_url.xml"}
    response = httpx.get(url, params=params, timeout=60, follow_redirects=True)
    response.raise_for_status()
    return response.text


def sbml_to_antimony(sbml_string: str) -> str:
    """Convert an SBML string to Antimony format."""
    import antimony

    antimony.clearPreviousLoads()
    result = antimony.loadSBMLString(sbml_string)
    if result == -1:
        raise ValueError(f"Failed to load SBML: {antimony.getLastError()}")
    return antimony.getAntimonyString(antimony.getMainModuleName())


def fetch_and_convert(model_id: str, output_dir: str | Path | None = None) -> str:
    """Download a BioModels model and convert to Antimony.

    If output_dir is provided, saves the .ant file there.
    Returns the Antimony string.
    """
    sbml = download_sbml(model_id)
    ant_string = sbml_to_antimony(sbml)

    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{model_id}.ant"
        output_path.write_text(ant_string)

    return ant_string
