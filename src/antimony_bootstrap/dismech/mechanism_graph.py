"""Build a causal graph from dismech mechanism downstream links."""

from __future__ import annotations

from typing import Any


def build_mechanism_graph(mechanisms: list[dict[str, Any]]) -> dict[str, list[str]]:
    """Build an adjacency list from mechanism downstream links.

    Returns a dict mapping mechanism name -> list of downstream mechanism names.
    """
    graph: dict[str, list[str]] = {}
    for mech in mechanisms:
        name = mech["name"]
        graph[name] = mech.get("downstream", [])
    return graph


def topological_order(graph: dict[str, list[str]]) -> list[str]:
    """Return mechanisms in topological order (upstream first).

    Uses Kahn's algorithm. Cycles are broken arbitrarily.
    """
    # Build in-degree map
    in_degree: dict[str, int] = {node: 0 for node in graph}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1

    # Start with nodes that have no incoming edges
    queue = [node for node, deg in in_degree.items() if deg == 0]
    result = []

    while queue:
        queue.sort()  # Deterministic ordering
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Add any remaining nodes (cycles)
    for node in sorted(in_degree):
        if node not in result:
            result.append(node)

    return result


def get_upstream(graph: dict[str, list[str]], target: str) -> set[str]:
    """Return all mechanisms upstream of the target."""
    reverse: dict[str, list[str]] = {}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reverse.setdefault(neighbor, []).append(node)

    visited: set[str] = set()
    stack = [target]
    while stack:
        node = stack.pop()
        for parent in reverse.get(node, []):
            if parent not in visited:
                visited.add(parent)
                stack.append(parent)

    return visited
