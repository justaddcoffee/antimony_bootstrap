"""Tests for module loading and the sample Alzheimer's module."""

from pathlib import Path

from antimony_bootstrap.modules.base import load_module, module_to_reaction_dicts
from antimony_bootstrap.schema.module_spec import ModuleSpec

ABETA_MODULE = Path("models/alzheimers/modules/abeta_production.yaml")


class TestLoadModule:
    def test_load_abeta_module(self):
        if not ABETA_MODULE.exists():
            import pytest
            pytest.skip("abeta_production.yaml not found")

        module = load_module(ABETA_MODULE)
        assert module.name == "abeta_production"
        assert len(module.compartments) == 3
        assert len(module.species) == 3
        assert len(module.reactions) == 5
        assert len(module.parameters) == 5

    def test_module_to_reaction_dicts(self):
        if not ABETA_MODULE.exists():
            import pytest
            pytest.skip("abeta_production.yaml not found")

        module = load_module(ABETA_MODULE)
        dicts = module_to_reaction_dicts(module)
        assert len(dicts) == 5
        assert all("Reaction_name" in d for d in dicts)
        assert all("Rate_type" in d for d in dicts)

    def test_no_unparameterized(self):
        if not ABETA_MODULE.exists():
            import pytest
            pytest.skip("abeta_production.yaml not found")

        module = load_module(ABETA_MODULE)
        missing = module.get_unparameterized()
        assert missing == [], f"Unparameterized: {missing}"
