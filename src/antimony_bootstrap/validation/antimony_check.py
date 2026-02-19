"""Validate Antimony model strings using the antimony library."""

from __future__ import annotations


def validate_antimony(antimony_string: str) -> tuple[bool, list[str]]:
    """Validate an Antimony model string.

    Returns (success, list of error messages).
    """
    import antimony

    antimony.clearPreviousLoads()
    result = antimony.loadString(antimony_string)

    if result == -1:
        error = antimony.getLastError()
        return False, [error]

    return True, []


def validate_antimony_file(path: str) -> tuple[bool, list[str]]:
    """Validate an Antimony model from a file."""
    with open(path) as f:
        content = f.read()
    return validate_antimony(content)
