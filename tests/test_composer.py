"""Tests for multi-module composition."""

from pathlib import Path

from antimony_bootstrap.assembly.composer import compose_from_manifest, compose_modules
from antimony_bootstrap.modules.base import load_module
from antimony_bootstrap.schema.module_spec import ModuleSpec, ModelManifest

MANIFEST = Path("models/alzheimers/model.yaml")
ABETA_MODULE = Path("models/alzheimers/modules/abeta_production.yaml")


class TestCompose:
    def test_compose_single_module(self):
        if not ABETA_MODULE.exists():
            import pytest
            pytest.skip("abeta_production.yaml not found")

        module = load_module(ABETA_MODULE)
        antimony_str, species, params, compartments = compose_modules([module])

        assert "compartment BrainISF" in antimony_str
        assert "AB42_BrainISF" in antimony_str
        assert "AB42_production" in antimony_str
        assert len(species) >= 3
        assert "BrainISF" in compartments

    def test_compose_from_manifest(self):
        if not MANIFEST.exists():
            import pytest
            pytest.skip("model.yaml not found")

        antimony_str, species, params, compartments = compose_from_manifest(MANIFEST)
        assert "compartment" in antimony_str
        assert "substanceOnly species" in antimony_str

    def test_parameter_values_included(self):
        if not ABETA_MODULE.exists():
            import pytest
            pytest.skip("abeta_production.yaml not found")

        module = load_module(ABETA_MODULE)
        antimony_str, _, _, _ = compose_modules([module])

        # Check that parameter values are assigned
        assert "k_AB42_prod" in antimony_str
        assert "k_AB42_deg_ISF" in antimony_str
