"""Convert reaction dictionaries to Antimony model strings.

Ported from Elbert's RxnDict_to_antimony.py with adaptations for the
ModuleSpec workflow.
"""

from __future__ import annotations

import re


def _parse_species_list(species_str: str) -> list[str]:
    """Parse a bracketed, comma-separated species string into a list."""
    if species_str in ("0", "[0]", ""):
        return []
    cleaned = species_str.strip("[]")
    if not cleaned:
        return []
    return [item.strip() for item in cleaned.split(",")]


def _extract_compartment(species: str) -> str | None:
    """Extract compartment from species name (text after final underscore)."""
    if "_" in species:
        comp = species.rsplit("_", 1)[-1]
        if comp.startswith("[") or comp.endswith("]") or "'" in comp:
            return None
        return comp
    return None


def generate_single_reaction(reaction_dict: dict) -> str:
    """Generate Antimony reaction string(s) from a single reaction dict.

    Handles all rate types: MA, RMA, BDF, UDF, custom_conc_per_time,
    custom_amt_per_time, custom.
    """
    reactants = _parse_species_list(reaction_dict["Reactants"])
    products = _parse_species_list(reaction_dict["Products"])
    rate_proto = reaction_dict["Rate_eqtn_prototype"]
    rate_type = reaction_dict["Rate_type"]

    # Determine compartments for volume multiplication
    compartment = None
    compartment_reverse = None
    if reactants:
        compartment = _extract_compartment(reactants[0])
    if products:
        compartment_reverse = _extract_compartment(products[0])

    lines = []

    if rate_type == "RMA":
        rate_constants = [c.strip() for c in rate_proto.strip("[]").split(",")]
        if len(rate_constants) < 2:
            raise ValueError(
                f"RMA reaction '{reaction_dict.get('Reaction_name', 'UNKNOWN')}' "
                f"requires two rate constants, got: '{rate_proto}'"
            )
        # Forward
        fwd_rate = f"{rate_constants[0]} * {' * '.join(reactants)}" if reactants else rate_constants[0]
        if compartment:
            fwd_rate = f"{fwd_rate} * V_{compartment}"
        lines.append(f"{' + '.join(reactants)} -> {' + '.join(products)}; {fwd_rate}")
        # Reverse
        rev_rate = f"{rate_constants[1]} * {' * '.join(products)}" if products else rate_constants[1]
        if compartment_reverse:
            rev_rate = f"{rev_rate} * V_{compartment_reverse}"
        lines.append(f"{' + '.join(products)} -> {' + '.join(reactants)}; {rev_rate}")

    elif rate_type == "BDF":
        rate_constants = [c.strip() for c in rate_proto.strip("[]").split(",")]
        # Forward
        fwd_rate = f"{rate_constants[0]} * {' * '.join(reactants)}" if reactants else rate_constants[0]
        lines.append(f"{' + '.join(reactants)} -> {' + '.join(products)}; {fwd_rate}")
        # Reverse (same rate constant)
        rev_rate = f"{rate_constants[0]} * {' * '.join(products)}" if products else rate_constants[0]
        lines.append(f"{' + '.join(products)} -> {' + '.join(reactants)}; {rev_rate}")

    elif rate_type in ("MA", "UDF"):
        rate_constants = [c.strip() for c in rate_proto.strip("[]").split(",")]
        fwd_rate = f"{rate_constants[0]} * {' * '.join(reactants)}" if reactants else rate_constants[0]
        if rate_type == "MA" and compartment:
            fwd_rate = f"{fwd_rate} * V_{compartment}"
        if rate_type == "MA" and not reactants and compartment_reverse:
            fwd_rate = f"{fwd_rate} * V_{compartment_reverse}"
        lines.append(f"{' + '.join(reactants)} -> {' + '.join(products)}; {fwd_rate}")

    elif rate_type == "custom_conc_per_time":
        rate_eqtn = rate_proto.strip("[]")
        if compartment:
            rate_eqtn = f"{rate_eqtn} * V_{compartment}"
        reactants_side = " + ".join(reactants)
        products_side = " + ".join(products)
        lines.append(f"{reactants_side} -> {products_side}; {rate_eqtn}")

    elif rate_type == "custom_amt_per_time":
        rate_eqtn = rate_proto.strip("[]")
        reactants_side = " + ".join(reactants)
        products_side = " + ".join(products)
        lines.append(f"{reactants_side} -> {products_side}; {rate_eqtn}")

    elif rate_type == "custom":
        rate_eqtn = rate_proto.strip("[]")
        reactants_side = " + ".join(reactants)
        products_side = " + ".join(products)
        lines.append(f"{reactants_side} -> {products_side}; {rate_eqtn}")

    return "\n".join(lines)


def collect_compartments_from_reactions(reactions: list[dict]) -> set[str]:
    """Collect unique compartment names from reaction dicts."""
    compartments: set[str] = set()
    for rxn in reactions:
        for key in ("Reactants", "Products"):
            species_list = _parse_species_list(rxn.get(key, ""))
            for sp in species_list:
                comp = _extract_compartment(sp)
                if comp:
                    compartments.add(comp)
    return compartments


def extract_species_and_parameters(reaction_string: str) -> tuple[list[str], list[str]]:
    """Extract unique species and parameters from an Antimony reaction string.

    Returns (sorted species list, sorted parameters list).
    """
    species: set[str] = set()
    parameters: set[str] = set()

    for line in reaction_string.split("\n"):
        line = line.strip()
        if not line or line.startswith("compartment ") or line.startswith("substanceOnly species"):
            continue

        parts = line.split(";")
        if len(parts) != 2:
            continue

        # Extract species from left side (reactants/products)
        left_side = parts[0].strip()
        # Remove reaction name prefix if present
        if ":" in left_side:
            left_side = left_side.split(":", 1)[1].strip()
        species_parts = re.split(r"[+\->]+", left_side)
        for part in species_parts:
            part = part.strip()
            part = re.sub(r"^\d+\s*", "", part)
            if part and not part.isdigit() and re.search(r"[A-Za-z]", part):
                if " " in part:
                    part = part.split(" ", 1)[1]
                species.add(part)

        # Extract parameters from right side (rate equation)
        right_side = parts[1].strip()
        param_matches = re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", right_side)
        parameters.update(param_matches)

    parameters -= species
    return sorted(species), sorted(parameters)


def generate_species_declarations(species_list: list[str]) -> str:
    """Generate substanceOnly species declarations."""
    declarations = []
    for sp in species_list:
        if "_" in sp:
            compartment = sp.rsplit("_", 1)[-1]
            declarations.append(f"substanceOnly species {sp} in {compartment}")
        else:
            declarations.append(f"substanceOnly species {sp} in {sp}")
    return "\n".join(declarations)


def convert_species_to_concentrations(reaction_string: str, species_list: list[str]) -> str:
    """Convert species in rate equations from amounts to concentrations.

    For each species in a rate equation, replace with (species/V_compartment).
    """
    species_to_compartment = {}
    for sp in species_list:
        if "_" in sp:
            species_to_compartment[sp] = sp.rsplit("_", 1)[-1]
        else:
            species_to_compartment[sp] = sp

    modified_lines = []
    for line in reaction_string.split("\n"):
        line = line.strip()
        if not line or line.startswith("compartment ") or line.startswith("substanceOnly species"):
            modified_lines.append(line)
            continue

        parts = line.split(";")
        if len(parts) != 2:
            modified_lines.append(line)
            continue

        rate_equation = parts[1].strip()
        for sp in species_list:
            if sp in rate_equation:
                compartment = species_to_compartment[sp]
                pattern = r"\b" + re.escape(sp) + r"\b"
                replacement = f"({sp}/V_{compartment})"
                rate_equation = re.sub(pattern, replacement, rate_equation)

        modified_lines.append(f"{parts[0].strip()}; {rate_equation}")

    return "\n".join(modified_lines)


def add_reaction_names(reaction_string: str, reactions: list[dict]) -> str:
    """Add reaction names to each reaction line."""
    lines = reaction_string.split("\n")
    modified = []
    rxn_idx = 0
    line_count = 0

    for line in lines:
        line = line.strip()
        if not line or line.startswith("compartment ") or line.startswith("substanceOnly species"):
            modified.append(line)
            continue

        if rxn_idx < len(reactions):
            name = reactions[rxn_idx].get("Reaction_name", "UNKNOWN")
            rate_type = reactions[rxn_idx].get("Rate_type", "")

            if rate_type in ("RMA", "BDF"):
                suffix = "_fwd" if line_count == 0 else "_rev"
                modified.append(f"{name}{suffix} : {line}")
                line_count += 1
                if line_count >= 2:
                    rxn_idx += 1
                    line_count = 0
            else:
                modified.append(f"{name} : {line}")
                rxn_idx += 1
                line_count = 0
        else:
            modified.append(line)

    return "\n".join(modified)


def generate_antimony_from_reactions(reactions: list[dict]) -> tuple[str, list[str], list[str], set[str]]:
    """Generate a complete Antimony model string from reaction dicts.

    Returns (antimony_string, species_list, parameters_list, compartments_set).
    """
    compartments = collect_compartments_from_reactions(reactions)

    # Generate raw reaction lines
    reaction_lines = []
    for rxn in reactions:
        reaction_lines.append(generate_single_reaction(rxn))
    raw_reactions = "\n".join(reaction_lines)

    # Extract species and parameters
    species, parameters = extract_species_and_parameters(raw_reactions)

    # Convert to concentrations
    conc_reactions = convert_species_to_concentrations(raw_reactions, species)

    # Add reaction names
    named_reactions = add_reaction_names(conc_reactions, reactions)

    # Build complete script
    parts = []

    # Compartment declarations
    for comp in sorted(compartments):
        parts.append(f"compartment {comp} = V_{comp}")
    parts.append("")

    # Species declarations
    parts.append(generate_species_declarations(species))
    parts.append("")

    # Reactions
    parts.append(named_reactions)

    return "\n".join(parts), species, parameters, compartments
