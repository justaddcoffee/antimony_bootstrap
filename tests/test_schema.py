"""Tests for the Pydantic schema."""

from pathlib import Path

import pytest

from antimony_bootstrap.schema.module_spec import (
    CompartmentSpec,
    Confidence,
    ModelManifest,
    ModuleSpec,
    ParameterSpec,
    RateType,
    ReactionSpec,
    SpeciesSpec,
)
from antimony_bootstrap.schema.naming import (
    extract_compartment,
    parse_species_name,
    species_name,
    validate_species_name,
    volume_parameter,
)


class TestNaming:
    def test_species_name(self):
        assert species_name("AB42", "BrainISF") == "AB42_BrainISF"

    def test_parse_species_name(self):
        base, comp = parse_species_name("AB42_BrainISF")
        assert base == "AB42"
        assert comp == "BrainISF"

    def test_parse_species_name_multiple_underscores(self):
        base, comp = parse_species_name("AB42_O12_ISF")
        assert base == "AB42_O12"
        assert comp == "ISF"

    def test_parse_species_name_no_underscore(self):
        with pytest.raises(ValueError):
            parse_species_name("AB42")

    def test_volume_parameter(self):
        assert volume_parameter("BrainISF") == "V_BrainISF"

    def test_extract_compartment(self):
        assert extract_compartment("AB42_BrainISF") == "BrainISF"
        assert extract_compartment("AB42") == "AB42"

    def test_validate_species_name_valid(self):
        assert validate_species_name("AB42_BrainISF") == []

    def test_validate_species_name_no_compartment(self):
        errors = validate_species_name("AB42")
        assert len(errors) == 1
        assert "compartment" in errors[0].lower()


class TestCompartmentSpec:
    def test_auto_volume_parameter(self):
        comp = CompartmentSpec(name="BrainISF")
        assert comp.volume_parameter == "V_BrainISF"

    def test_explicit_volume_parameter(self):
        comp = CompartmentSpec(name="BrainISF", volume_parameter="Vol_ISF")
        assert comp.volume_parameter == "Vol_ISF"


class TestSpeciesSpec:
    def test_infer_compartment(self):
        sp = SpeciesSpec(name="AB42_BrainISF")
        assert sp.compartment == "BrainISF"

    def test_explicit_compartment(self):
        sp = SpeciesSpec(name="AB42_BrainISF", compartment="ISF")
        assert sp.compartment == "ISF"


class TestReactionSpec:
    def test_to_reaction_dict_ma(self):
        rxn = ReactionSpec(
            name="AB42_deg",
            reactants=["AB42_BrainISF"],
            products=[],
            rate_type=RateType.MA,
            rate_parameters=["k_deg"],
        )
        d = rxn.to_reaction_dict()
        assert d["Reaction_name"] == "AB42_deg"
        assert d["Reactants"] == "[AB42_BrainISF]"
        assert d["Products"] == "[0]"
        assert d["Rate_type"] == "MA"
        assert d["Rate_eqtn_prototype"] == "[k_deg]"

    def test_to_reaction_dict_rma(self):
        rxn = ReactionSpec(
            name="AB42_bind",
            reactants=["AB42_BrainISF"],
            products=["AB42_bound_BrainISF"],
            rate_type=RateType.RMA,
            rate_parameters=["k_on", "k_off"],
        )
        d = rxn.to_reaction_dict()
        assert d["Rate_type"] == "RMA"
        assert d["Rate_eqtn_prototype"] == "[k_on, k_off]"

    def test_to_reaction_dict_custom(self):
        rxn = ReactionSpec(
            name="AB42_mm",
            reactants=["AB42_BrainISF"],
            products=[],
            rate_type=RateType.CUSTOM_CONC,
            rate_equation="Vmax * AB42_BrainISF / (Km + AB42_BrainISF)",
        )
        d = rxn.to_reaction_dict()
        assert d["Rate_type"] == "custom_conc_per_time"
        assert "Vmax" in d["Rate_eqtn_prototype"]


class TestModuleSpec:
    def test_from_yaml(self, tmp_path):
        yaml_content = """
name: test_module
description: A test module
compartments:
  - name: BrainISF
    volume_value: 0.25
species:
  - name: AB42_BrainISF
    initial_amount: 1.0e-9
reactions:
  - name: AB42_deg
    reactants:
      - AB42_BrainISF
    products: []
    rate_type: MA
    rate_parameters:
      - k_deg
parameters:
  - name: k_deg
    value: 0.069
    units: 1/hr
    confidence: estimated
"""
        yaml_file = tmp_path / "test.yaml"
        yaml_file.write_text(yaml_content)

        module = ModuleSpec.from_yaml(yaml_file)
        assert module.name == "test_module"
        assert len(module.compartments) == 1
        assert len(module.species) == 1
        assert len(module.reactions) == 1
        assert len(module.parameters) == 1
        assert module.parameters[0].value == 0.069

    def test_get_unparameterized(self):
        module = ModuleSpec(
            name="test",
            parameters=[
                ParameterSpec(name="k1", value=0.1),
                ParameterSpec(name="k2", value=None),
                ParameterSpec(name="k3", value=0.3),
            ],
        )
        missing = module.get_unparameterized()
        assert missing == ["k2"]

    def test_roundtrip_yaml(self, tmp_path):
        module = ModuleSpec(
            name="roundtrip",
            compartments=[CompartmentSpec(name="ISF", volume_value=0.25)],
            species=[SpeciesSpec(name="X_ISF", initial_amount=1.0)],
            reactions=[
                ReactionSpec(
                    name="X_deg",
                    reactants=["X_ISF"],
                    products=[],
                    rate_type=RateType.MA,
                    rate_parameters=["k"],
                )
            ],
            parameters=[ParameterSpec(name="k", value=0.1, units="1/hr")],
        )

        yaml_file = tmp_path / "roundtrip.yaml"
        module.to_yaml(yaml_file)

        loaded = ModuleSpec.from_yaml(yaml_file)
        assert loaded.name == "roundtrip"
        assert len(loaded.reactions) == 1
        assert loaded.parameters[0].value == 0.1


class TestModelManifest:
    def test_from_yaml(self, tmp_path):
        yaml_content = """
name: "Test Disease"
disease_id: "MONDO:0000001"
modules:
  - module1.yaml
shared_compartments:
  - name: Plasma
    volume_value: 3.0
"""
        yaml_file = tmp_path / "model.yaml"
        yaml_file.write_text(yaml_content)

        manifest = ModelManifest.from_yaml(yaml_file)
        assert manifest.name == "Test Disease"
        assert len(manifest.modules) == 1
        assert manifest.shared_compartments[0].volume_value == 3.0
