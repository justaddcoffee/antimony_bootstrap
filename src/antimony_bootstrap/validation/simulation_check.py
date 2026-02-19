"""Tellurium smoke test for Antimony models."""

from __future__ import annotations

from typing import Any


def smoke_test(
    antimony_string: str,
    start: float = 0,
    end: float = 100,
    points: int = 50,
) -> tuple[bool, list[str], Any]:
    """Run a quick tellurium simulation.

    Returns (success, list of error/warning messages, result array or None).
    """
    import numpy as np
    import tellurium as te

    errors = []

    try:
        r = te.loada(antimony_string)
        result = r.simulate(start, end, points)
    except Exception as e:
        return False, [f"Simulation failed: {e}"], None

    # Check for NaN/Inf
    if np.any(np.isnan(result)):
        errors.append("Simulation produced NaN values")
    if np.any(np.isinf(result)):
        errors.append("Simulation produced Inf values")

    success = len(errors) == 0
    return success, errors, result
