"""Reaction dict creation, adapted from Elbert's reaction_creation.py."""

from __future__ import annotations

import warnings


VALID_RATE_TYPES = {"RMA", "BDF", "MA", "UDF", "custom_conc_per_time", "custom_amt_per_time", "custom"}


def create_reaction(
    reaction_name: str,
    reactants: str,
    products: str,
    rate_type: str,
    rate_equation_prototype: str,
) -> dict:
    """Create a single reaction dictionary.

    Adapted from Elbert's reaction_creation.py.

    Args:
        reaction_name: Reaction identifier (spaces will be stripped).
        reactants: Reactants string, e.g. "[AB42_BrainISF]" or "[0]" for source.
        products: Products string, e.g. "[AB42_CSF]" or "[0]" for sink.
        rate_type: One of VALID_RATE_TYPES.
        rate_equation_prototype: Rate constant(s) or custom equation.

    Returns:
        Reaction dictionary compatible with RxnDict_to_antimony.
    """
    missing = []
    if not reaction_name:
        missing.append("reaction_name")
        reaction_name = "NA"
    if reactants is None:
        missing.append("reactants")
    if products is None:
        missing.append("products")
    if not rate_type:
        missing.append("rate_type")
    if not rate_equation_prototype:
        missing.append("rate_equation_prototype")

    if missing:
        warnings.warn(
            f"Missing elements in reaction creation: {', '.join(missing)}",
            UserWarning,
            stacklevel=2,
        )

    if rate_type and rate_type not in VALID_RATE_TYPES:
        warnings.warn(
            f"Invalid rate_type '{rate_type}'. Valid: {', '.join(sorted(VALID_RATE_TYPES))}",
            UserWarning,
            stacklevel=2,
        )

    reaction_name = reaction_name.replace(" ", "")

    return {
        "Reaction_name": reaction_name,
        "Reactants": reactants,
        "Products": products,
        "Rate_type": rate_type,
        "Rate_eqtn_prototype": rate_equation_prototype,
    }


def reaction_lines_count(rate_type: str) -> int:
    """Return how many Antimony lines a reaction of this type generates."""
    if rate_type in ("RMA", "BDF"):
        return 2
    return 1
