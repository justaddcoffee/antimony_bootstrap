"""Validate SBML models using libsbml."""

from __future__ import annotations


def validate_sbml(sbml_string: str) -> tuple[bool, list[str]]:
    """Validate an SBML string using libsbml.

    Returns (success, list of error messages).
    """
    import libsbml

    doc = libsbml.readSBMLFromString(sbml_string)
    errors = []

    for i in range(doc.getNumErrors()):
        err = doc.getError(i)
        if err.getSeverity() >= libsbml.LIBSBML_SEV_ERROR:
            errors.append(f"L{err.getLine()}: {err.getMessage()}")

    return len(errors) == 0, errors


def antimony_to_sbml(antimony_string: str) -> str:
    """Convert Antimony string to SBML."""
    import antimony

    antimony.clearPreviousLoads()
    result = antimony.loadString(antimony_string)
    if result == -1:
        raise ValueError(f"Failed to load Antimony: {antimony.getLastError()}")

    sbml = antimony.getSBMLString(antimony.getMainModuleName())
    return sbml
