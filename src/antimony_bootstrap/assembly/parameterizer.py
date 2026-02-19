"""Parameter assignment with provenance tracking."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from antimony_bootstrap.schema.module_spec import Confidence, ModuleSpec, ParameterSpec


def load_parameter_file(path: str | Path) -> list[ParameterSpec]:
    """Load parameter values from a YAML file."""
    with open(path) as f:
        data = yaml.safe_load(f)
    return [ParameterSpec(**p) for p in data.get("parameters", [])]


def apply_parameters(module: ModuleSpec, param_values: dict[str, dict[str, Any]]) -> ModuleSpec:
    """Apply parameter values to a module.

    param_values maps parameter name -> dict with keys: value, units, confidence, source.
    """
    for param in module.parameters:
        if param.name in param_values:
            update = param_values[param.name]
            if "value" in update:
                param.value = update["value"]
            if "units" in update:
                param.units = update["units"]
            if "confidence" in update:
                param.confidence = Confidence(update["confidence"])
            if "source" in update:
                param.source = update["source"]
    return module


def generate_provenance_report(modules: list[ModuleSpec]) -> str:
    """Generate a markdown provenance report for all parameters."""
    lines = ["# Parameter Provenance Report", ""]

    for module in modules:
        lines.append(f"## {module.name}")
        lines.append("")

        if not module.parameters:
            lines.append("No parameters defined.")
            lines.append("")
            continue

        lines.append("| Parameter | Value | Units | Confidence | Source |")
        lines.append("|-----------|-------|-------|------------|--------|")

        for p in module.parameters:
            value = str(p.value) if p.value is not None else "**MISSING**"
            units = p.units or ""
            confidence = p.confidence.value if p.confidence else ""
            source = p.source or ""
            lines.append(f"| {p.name} | {value} | {units} | {confidence} | {source} |")

        lines.append("")

    # Summary
    total = sum(len(m.parameters) for m in modules)
    missing = sum(len(m.get_unparameterized()) for m in modules)
    lines.append("## Summary")
    lines.append(f"- Total parameters: {total}")
    lines.append(f"- Parameterized: {total - missing}")
    lines.append(f"- Missing: {missing}")

    return "\n".join(lines)
