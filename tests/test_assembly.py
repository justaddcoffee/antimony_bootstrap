"""Tests for assembly: reaction dict to Antimony conversion."""

import pytest

from antimony_bootstrap.assembly.rxndict_to_antimony import (
    add_reaction_names,
    collect_compartments_from_reactions,
    convert_species_to_concentrations,
    extract_species_and_parameters,
    generate_antimony_from_reactions,
    generate_single_reaction,
    generate_species_declarations,
)
from antimony_bootstrap.modules.reaction_builder import create_reaction


class TestGenerateSingleReaction:
    def test_ma_reaction(self):
        rxn = create_reaction("AB42_deg", "[AB42_BrainISF]", "[0]", "MA", "[k_deg]")
        result = generate_single_reaction(rxn)
        assert "AB42_BrainISF ->" in result
        assert "k_deg * AB42_BrainISF" in result
        assert "V_BrainISF" in result

    def test_ma_zero_order(self):
        rxn = create_reaction("AB42_prod", "[0]", "[AB42_BrainISF]", "MA", "[k_prod]")
        result = generate_single_reaction(rxn)
        assert "-> AB42_BrainISF" in result
        assert "k_prod" in result
        assert "V_BrainISF" in result

    def test_rma_reaction(self):
        rxn = create_reaction(
            "AB42_bind", "[AB42_BrainISF]", "[AB42_bound_BrainISF]", "RMA", "[k_on, k_off]"
        )
        result = generate_single_reaction(rxn)
        lines = [l for l in result.split("\n") if l.strip()]
        assert len(lines) == 2  # Forward and reverse
        assert "k_on" in lines[0]
        assert "k_off" in lines[1]

    def test_bdf_reaction(self):
        rxn = create_reaction(
            "AB42_flow", "[AB42_BrainISF]", "[AB42_CSF]", "BDF", "[k_flow]"
        )
        result = generate_single_reaction(rxn)
        lines = [l for l in result.split("\n") if l.strip()]
        assert len(lines) == 2
        # Same rate constant for both directions
        assert "k_flow" in lines[0]
        assert "k_flow" in lines[1]

    def test_udf_reaction(self):
        rxn = create_reaction(
            "AB42_transport", "[AB42_BrainISF]", "[AB42_CSF]", "UDF", "[k_transport]"
        )
        result = generate_single_reaction(rxn)
        assert "V_" not in result  # UDF does not multiply by volume

    def test_custom_conc_per_time(self):
        rxn = create_reaction(
            "AB42_mm", "[AB42_BrainISF]", "[0]", "custom_conc_per_time",
            "Vmax * AB42_BrainISF / (Km + AB42_BrainISF)"
        )
        result = generate_single_reaction(rxn)
        assert "Vmax" in result
        assert "V_BrainISF" in result

    def test_custom_amt_per_time(self):
        rxn = create_reaction(
            "AB42_clear", "[AB42_BrainISF]", "[0]", "custom_amt_per_time",
            "k_clear * AB42_BrainISF"
        )
        result = generate_single_reaction(rxn)
        assert "k_clear" in result
        assert "V_" not in result


class TestCollectCompartments:
    def test_collects_from_reactants_and_products(self):
        reactions = [
            create_reaction("r1", "[AB42_BrainISF]", "[AB42_CSF]", "UDF", "[k]"),
            create_reaction("r2", "[AB42_CSF]", "[AB42_Plasma]", "UDF", "[k2]"),
        ]
        compartments = collect_compartments_from_reactions(reactions)
        assert compartments == {"BrainISF", "CSF", "Plasma"}


class TestExtractSpeciesAndParameters:
    def test_basic(self):
        rxn_str = "AB42_BrainISF -> AB42_CSF; k_transport * AB42_BrainISF"
        species, params = extract_species_and_parameters(rxn_str)
        assert "AB42_BrainISF" in species
        assert "AB42_CSF" in species
        assert "k_transport" in params


class TestSpeciesDeclarations:
    def test_generates_declarations(self):
        result = generate_species_declarations(["AB42_BrainISF", "AB42_CSF"])
        assert "substanceOnly species AB42_BrainISF in BrainISF" in result
        assert "substanceOnly species AB42_CSF in CSF" in result


class TestConvertToConcentrations:
    def test_converts_species_in_rate(self):
        rxn_str = "AB42_BrainISF -> ; k * AB42_BrainISF"
        result = convert_species_to_concentrations(rxn_str, ["AB42_BrainISF"])
        assert "(AB42_BrainISF/V_BrainISF)" in result


class TestAddReactionNames:
    def test_adds_names(self):
        rxn_str = "A_X -> B_X; k * A_X"
        reactions = [{"Reaction_name": "my_rxn", "Rate_type": "MA"}]
        result = add_reaction_names(rxn_str, reactions)
        assert "my_rxn : " in result

    def test_rma_fwd_rev(self):
        rxn_str = "A_X -> B_X; k1 * A_X\nB_X -> A_X; k2 * B_X"
        reactions = [{"Reaction_name": "bind", "Rate_type": "RMA"}]
        result = add_reaction_names(rxn_str, reactions)
        assert "bind_fwd : " in result
        assert "bind_rev : " in result


class TestGenerateAntimonyFromReactions:
    def test_full_generation(self):
        reactions = [
            create_reaction("AB42_prod", "[0]", "[AB42_BrainISF]", "MA", "[k_prod]"),
            create_reaction("AB42_deg", "[AB42_BrainISF]", "[0]", "MA", "[k_deg]"),
        ]
        antimony_str, species, params, compartments = generate_antimony_from_reactions(reactions)

        assert "compartment BrainISF" in antimony_str
        assert "substanceOnly species AB42_BrainISF in BrainISF" in antimony_str
        assert "AB42_prod :" in antimony_str
        assert "AB42_deg :" in antimony_str
        assert "AB42_BrainISF" in species
        assert "BrainISF" in compartments
