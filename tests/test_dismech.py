"""Tests for dismech reader and mechanism graph."""

from antimony_bootstrap.dismech.mechanism_graph import (
    build_mechanism_graph,
    get_upstream,
    topological_order,
)
from antimony_bootstrap.dismech.reader import (
    extract_disease_metadata,
    extract_mechanisms,
    load_dismech_yaml,
)

ALZHEIMERS_YAML = "models/alzheimers/test_fixtures/alzheimers_mini.yaml"


def _sample_mechanisms():
    """Create sample mechanism data for graph tests."""
    return [
        {"name": "A", "downstream": ["C", "D"]},
        {"name": "B", "downstream": ["D"]},
        {"name": "C", "downstream": ["E"]},
        {"name": "D", "downstream": ["E"]},
        {"name": "E", "downstream": []},
    ]


class TestMechanismGraph:
    def test_build_graph(self):
        mechs = _sample_mechanisms()
        graph = build_mechanism_graph(mechs)
        assert graph["A"] == ["C", "D"]
        assert graph["E"] == []

    def test_topological_order(self):
        mechs = _sample_mechanisms()
        graph = build_mechanism_graph(mechs)
        order = topological_order(graph)
        # A and B should come before C, D, E
        assert order.index("A") < order.index("C")
        assert order.index("A") < order.index("D")
        assert order.index("C") < order.index("E")
        assert order.index("D") < order.index("E")

    def test_get_upstream(self):
        mechs = _sample_mechanisms()
        graph = build_mechanism_graph(mechs)
        upstream = get_upstream(graph, "E")
        assert "A" in upstream
        assert "B" in upstream
        assert "C" in upstream
        assert "D" in upstream
        assert "E" not in upstream

    def test_get_upstream_root(self):
        mechs = _sample_mechanisms()
        graph = build_mechanism_graph(mechs)
        upstream = get_upstream(graph, "A")
        assert upstream == set()
