"""Compose multiple modules into a single Antimony model."""

from __future__ import annotations

from pathlib import Path

from antimony_bootstrap.assembly.rxndict_to_antimony import generate_antimony_from_reactions
from antimony_bootstrap.modules.base import load_module, load_modules_from_dir
from antimony_bootstrap.schema.module_spec import ModelManifest, ModuleSpec


def compose_modules(
    modules: list[ModuleSpec],
    manifest: ModelManifest | None = None,
) -> tuple[str, list[str], list[str], set[str]]:
    """Merge multiple modules into a single Antimony model.

    Combines all reaction dicts, resolves shared compartments/species,
    and generates the complete Antimony string.

    Returns (antimony_string, species_list, parameters_list, compartments_set).
    """
    all_reactions: list[dict] = []
    for module in modules:
        all_reactions.extend(module.to_reaction_dicts())

    antimony_str, species, parameters, compartments = generate_antimony_from_reactions(all_reactions)

    # Collect parameter values from modules for the assignment block
    param_values: dict[str, float] = {}
    for module in modules:
        for p in module.parameters:
            if p.value is not None:
                param_values[p.name] = p.value

    # Add shared parameters from manifest
    if manifest:
        for p in manifest.shared_parameters:
            if p.value is not None:
                param_values[p.name] = p.value
        for c in manifest.shared_compartments:
            if c.volume_value is not None:
                param_values[c.volume_parameter or f"V_{c.name}"] = c.volume_value

    # Collect initial amounts from modules
    initial_amounts: dict[str, float] = {}
    for module in modules:
        for s in module.species:
            if s.initial_amount is not None:
                initial_amounts[s.name] = s.initial_amount

    # Append parameter assignments
    param_lines = []
    if param_values:
        param_lines.append("")
        param_lines.append("// Parameter values")
        for name in sorted(param_values):
            param_lines.append(f"{name} = {param_values[name]}")

    # Append initial amounts
    if initial_amounts:
        param_lines.append("")
        param_lines.append("// Initial amounts")
        for name in sorted(initial_amounts):
            param_lines.append(f"{name} = {initial_amounts[name]}")

    if param_lines:
        antimony_str += "\n" + "\n".join(param_lines)

    return antimony_str, species, parameters, compartments


def compose_from_manifest(manifest_path: str | Path) -> tuple[str, list[str], list[str], set[str]]:
    """Load a manifest and compose the full model.

    Returns (antimony_string, species_list, parameters_list, compartments_set).
    """
    manifest_path = Path(manifest_path)
    manifest = ModelManifest.from_yaml(manifest_path)
    modules_dir = manifest_path.parent / "modules"

    modules = []
    for module_file in manifest.modules:
        module_path = modules_dir / module_file
        modules.append(load_module(module_path))

    return compose_modules(modules, manifest)
