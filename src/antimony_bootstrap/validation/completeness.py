"""Check model completeness: all params defined, species declared, etc."""

from __future__ import annotations

from antimony_bootstrap.schema.module_spec import ModuleSpec


def check_completeness(modules: list[ModuleSpec]) -> tuple[bool, list[str]]:
    """Check that all modules are complete.

    Returns (all_complete, list of issue messages).
    """
    issues = []

    for module in modules:
        prefix = f"[{module.name}]"

        # Check for unparameterized parameters
        missing_params = module.get_unparameterized()
        if missing_params:
            issues.append(f"{prefix} Missing parameter values: {', '.join(missing_params)}")

        # Check species have compartments
        for sp in module.species:
            if sp.compartment is None and "_" not in sp.name:
                issues.append(f"{prefix} Species '{sp.name}' has no compartment")

        # Check reactions reference declared species
        declared_species = {s.name for s in module.species}
        for rxn in module.reactions:
            for sp_name in rxn.reactants + rxn.products:
                if sp_name not in declared_species:
                    issues.append(
                        f"{prefix} Reaction '{rxn.name}' references undeclared species '{sp_name}'"
                    )

        # Check reactions have rate parameters or equations
        for rxn in module.reactions:
            if rxn.rate_type.value in ("MA", "RMA", "BDF", "UDF"):
                if not rxn.rate_parameters:
                    issues.append(
                        f"{prefix} Reaction '{rxn.name}' ({rxn.rate_type.value}) has no rate parameters"
                    )
            else:
                if not rxn.rate_equation:
                    issues.append(
                        f"{prefix} Reaction '{rxn.name}' ({rxn.rate_type.value}) has no rate equation"
                    )

    return len(issues) == 0, issues
