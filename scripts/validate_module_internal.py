#!/usr/bin/env python3
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

import yaml


def extract_names(expr: str) -> set[str]:
    tree = ast.parse(expr, mode="eval")
    out: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            out.add(node.id)
    return out


def denominator_nodes(expr: str):
    tree = ast.parse(expr, mode="eval")
    dens = []
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
            dens.append(node.right)
    return dens


def node_uses_only_safe_terms(node: ast.AST, positive_names: set[str]) -> bool:
    # Conservative rule for denominators: allow positive constants,
    # names known positive, sums/products of positive terms.
    if isinstance(node, ast.Constant):
        return isinstance(node.value, (int, float)) and node.value > 0
    if isinstance(node, ast.Name):
        return node.id in positive_names
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
        return node_uses_only_safe_terms(node.operand, positive_names)
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, (ast.Add, ast.Mult)):
            return node_uses_only_safe_terms(node.left, positive_names) and node_uses_only_safe_terms(node.right, positive_names)
        if isinstance(node.op, ast.Div):
            return node_uses_only_safe_terms(node.left, positive_names) and node_uses_only_safe_terms(node.right, positive_names)
        return False
    return False


def compartment_suffix(species_name: str) -> str | None:
    if "_" not in species_name:
        return None
    return species_name.rsplit("_", 1)[-1]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_module_internal.py <module_yaml>")
        return 2

    path = Path(sys.argv[1])
    data = yaml.safe_load(path.read_text())

    errors: list[str] = []
    warnings: list[str] = []

    parameters = {p["name"]: p for p in data.get("parameters", [])}
    parameter_names = set(parameters.keys())

    species = {s["name"]: s for s in data.get("species", [])}
    species_names = set(species.keys())

    compartment_names = {c["name"] for c in data.get("compartments", [])}

    # Positive-known symbols for denominator safety checks.
    positive_names = set()
    for pname, p in parameters.items():
        val = p.get("value")
        if isinstance(val, (int, float)) and val > 0:
            positive_names.add(pname)
    for sname, s in species.items():
        init = s.get("initial_amount")
        if isinstance(init, (int, float)) and init > 0:
            positive_names.add(sname)

    for rxn in data.get("reactions", []):
        rname = rxn.get("name", "<unnamed>")

        for p in rxn.get("rate_parameters", []):
            if p not in parameter_names:
                errors.append(f"{rname}: rate_parameters references undefined parameter '{p}'")

        eq = rxn.get("rate_equation")
        if eq:
            try:
                eq_names = extract_names(eq)
            except SyntaxError as exc:
                errors.append(f"{rname}: invalid rate_equation syntax: {exc}")
                eq_names = set()

            unknown = sorted(eq_names - parameter_names - species_names)
            if unknown:
                errors.append(
                    f"{rname}: rate_equation references unknown symbols: {', '.join(unknown)}"
                )

            try:
                dens = denominator_nodes(eq)
            except SyntaxError:
                dens = []
            for i, den in enumerate(dens, start=1):
                if not node_uses_only_safe_terms(den, positive_names):
                    warnings.append(
                        f"{rname}: denominator #{i} may hit zero or become non-positive: {ast.unparse(den)}"
                    )

        for role in ("reactants", "products"):
            for sp in rxn.get(role, []):
                if sp not in species_names:
                    errors.append(f"{rname}: {role} references undefined species '{sp}'")

    for sname, s in species.items():
        suffix = compartment_suffix(sname)
        if suffix is None:
            errors.append(f"species '{sname}' has no compartment suffix")
        elif suffix not in compartment_names:
            errors.append(
                f"species '{sname}' suffix '{suffix}' is not a declared compartment"
            )

        init = s.get("initial_amount")
        if not isinstance(init, (int, float)):
            errors.append(f"species '{sname}' initial_amount is not numeric")
        elif init <= 0:
            errors.append(f"species '{sname}' initial_amount must be > 0")

    # Sanity range for kinetic-like constants.
    for pname, p in parameters.items():
        if not re.match(r"^(k_|beta_)", pname):
            continue
        val = p.get("value")
        if not isinstance(val, (int, float)):
            errors.append(f"parameter '{pname}' value is not numeric")
            continue
        if val <= 0:
            errors.append(f"parameter '{pname}' must be > 0")
        if not (1e-9 <= float(val) <= 1e3):
            warnings.append(
                f"parameter '{pname}'={val} outside nominal range [1e-9, 1e3]"
            )

    print(f"Module: {data.get('name', path.name)}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"- {e}")

    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"- {w}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
