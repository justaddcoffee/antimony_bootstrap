"""Write .ant and .sbml files from assembled models."""

from __future__ import annotations

from pathlib import Path


def write_antimony(antimony_string: str, path: str | Path) -> Path:
    """Write an Antimony model string to a .ant file."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(antimony_string)
    return path


def write_sbml(antimony_string: str, path: str | Path) -> Path:
    """Convert Antimony to SBML and write to a .sbml file."""
    from antimony_bootstrap.validation.sbml_check import antimony_to_sbml

    sbml_string = antimony_to_sbml(antimony_string)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(sbml_string)
    return path
