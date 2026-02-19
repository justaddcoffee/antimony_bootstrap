"""Species and parameter naming conventions following Elbert convention.

Species: {base}_{compartment}  e.g., AB42_BrainISF
Volume parameters: V_{compartment}  e.g., V_BrainISF
"""

import re


def species_name(base: str, compartment: str) -> str:
    """Create a species name from base and compartment."""
    return f"{base}_{compartment}"


def parse_species_name(name: str) -> tuple[str, str]:
    """Parse a species name into (base, compartment).

    The compartment is the text after the final underscore.
    """
    if "_" not in name:
        raise ValueError(f"Species name '{name}' has no compartment suffix (no underscore)")
    parts = name.rsplit("_", 1)
    return parts[0], parts[1]


def volume_parameter(compartment: str) -> str:
    """Return the volume parameter name for a compartment."""
    return f"V_{compartment}"


def extract_compartment(species: str) -> str:
    """Extract compartment from species name (text after final underscore)."""
    if "_" not in species:
        return species
    return species.rsplit("_", 1)[-1]


def validate_species_name(name: str) -> list[str]:
    """Validate a species name and return a list of error messages (empty if valid)."""
    errors = []
    if not name:
        errors.append("Species name is empty")
        return errors
    if not re.match(r"^[A-Za-z]", name):
        errors.append(f"Species name '{name}' must start with a letter")
    if re.search(r"[^A-Za-z0-9_]", name):
        errors.append(f"Species name '{name}' contains invalid characters (only alphanumeric and underscore allowed)")
    if "_" not in name:
        errors.append(f"Species name '{name}' has no compartment suffix")
    return errors
