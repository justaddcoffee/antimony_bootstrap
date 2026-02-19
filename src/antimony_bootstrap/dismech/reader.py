"""Load dismech YAML files and extract disease mechanisms."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_dismech_yaml(path: str | Path) -> dict[str, Any]:
    """Load a dismech disorder YAML file."""
    with open(path) as f:
        return yaml.safe_load(f)


def extract_mechanisms(data: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract pathophysiology mechanisms from a dismech disorder.

    Returns a list of mechanism dicts, each with:
      - name: mechanism name
      - description: mechanism description
      - cell_types: list of cell type names
      - biological_processes: list of GO process names
      - downstream: list of downstream target names
      - evidence: list of evidence items (with PMIDs)
    """
    mechanisms = []
    for mech in data.get("pathophysiology", []):
        cell_types = []
        for ct in mech.get("cell_types", []):
            label = ct.get("preferred_term") or ct.get("term", {}).get("label", "")
            if label:
                cell_types.append(label)

        bio_processes = []
        for bp in mech.get("biological_processes", []):
            label = bp.get("preferred_term") or bp.get("term", {}).get("label", "")
            if label:
                bio_processes.append(label)

        downstream = [d["target"] for d in mech.get("downstream", []) if "target" in d]

        evidence = []
        for ev in mech.get("evidence", []):
            evidence.append({
                "reference": ev.get("reference", ""),
                "supports": ev.get("supports", ""),
                "snippet": ev.get("snippet", ""),
                "explanation": ev.get("explanation", ""),
            })

        mechanisms.append({
            "name": mech.get("name", ""),
            "description": mech.get("description", "").strip(),
            "cell_types": cell_types,
            "biological_processes": bio_processes,
            "downstream": downstream,
            "evidence": evidence,
        })

    return mechanisms


def extract_genetic_factors(data: dict[str, Any]) -> list[dict[str, str]]:
    """Extract genetic factors from a dismech disorder."""
    factors = []
    for gene in data.get("genetic", []):
        factors.append({
            "name": gene.get("name", ""),
            "association": gene.get("association", ""),
            "notes": gene.get("notes", ""),
        })
    return factors


def extract_disease_metadata(data: dict[str, Any]) -> dict[str, Any]:
    """Extract top-level disease metadata."""
    disease_term = data.get("disease_term", {})
    term = disease_term.get("term", {})
    return {
        "name": data.get("name", ""),
        "description": data.get("description", "").strip(),
        "category": data.get("category", ""),
        "disease_id": term.get("id", ""),
        "disease_label": term.get("label", ""),
        "parents": data.get("parents", []),
    }
