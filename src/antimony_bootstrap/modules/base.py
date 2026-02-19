"""Load ModuleSpec YAML files and generate reaction dicts."""

from __future__ import annotations

from pathlib import Path

from antimony_bootstrap.schema.module_spec import ModuleSpec


def load_module(path: str | Path) -> ModuleSpec:
    """Load a ModuleSpec from a YAML file."""
    return ModuleSpec.from_yaml(path)


def load_modules_from_dir(directory: str | Path) -> list[ModuleSpec]:
    """Load all module YAML files from a directory."""
    directory = Path(directory)
    modules = []
    for yaml_file in sorted(directory.glob("*.yaml")):
        modules.append(ModuleSpec.from_yaml(yaml_file))
    return modules


def module_to_reaction_dicts(module: ModuleSpec) -> list[dict]:
    """Convert a ModuleSpec to a list of Elbert-style reaction dicts."""
    return module.to_reaction_dicts()
