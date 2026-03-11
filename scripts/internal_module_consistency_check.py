#!/usr/bin/env python3
import argparse
import ast
import math
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml

IDENT_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def extract_identifiers(expr: str) -> Set[str]:
    tokens = set(IDENT_RE.findall(expr or ""))
    keywords = {"and", "or", "not"}
    return {t for t in tokens if not t.isdigit() and t not in keywords}


def extract_denominators(expr: str) -> List[str]:
    denoms: List[str] = []
    i = 0
    n = len(expr)
    while i < n:
        if expr[i] != "/":
            i += 1
            continue
        i += 1
        while i < n and expr[i].isspace():
            i += 1
        if i >= n:
            break
        if expr[i] == "(":
            depth = 0
            start = i
            while i < n:
                if expr[i] == "(":
                    depth += 1
                elif expr[i] == ")":
                    depth -= 1
                    if depth == 0:
                        i += 1
                        denoms.append(expr[start:i])
                        break
                i += 1
        else:
            start = i
            while i < n and (expr[i].isalnum() or expr[i] in "_."):
                i += 1
            token = expr[start:i].strip()
            if token:
                denoms.append(token)
    return denoms


def safe_eval_expr(expr: str, values: Dict[str, float]) -> float:
    node = ast.parse(expr, mode="eval")

    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Num,
        ast.Constant,
        ast.Name,
        ast.Load,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Call,
    )
    for n in ast.walk(node):
        if not isinstance(n, allowed_nodes):
            raise ValueError(f"Unsupported syntax in equation: {type(n).__name__}")
        if isinstance(n, ast.Call):
            if not isinstance(n.func, ast.Name) or n.func.id not in {"exp", "log", "sqrt", "min", "max", "abs"}:
                raise ValueError("Unsupported function call")

    env = {
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "min": min,
        "max": max,
        "abs": abs,
    }
    env.update(values)
    return float(eval(compile(node, "<expr>", "eval"), {"__builtins__": {}}, env))


def check_module(path: Path) -> Dict[str, List[str]]:
    data = load_yaml(path)
    errors: List[str] = []
    warnings: List[str] = []

    compartments = data.get("compartments", [])
    species = data.get("species", [])
    reactions = data.get("reactions", [])
    parameters = data.get("parameters", [])

    compartment_names = {c["name"] for c in compartments}
    volume_params = {c["volume_parameter"] for c in compartments}

    species_names = {s["name"] for s in species}
    param_names = {p["name"] for p in parameters}
    allowed_param_like = param_names | volume_params

    param_values: Dict[str, float] = {p["name"]: float(p["value"]) for p in parameters}
    for c in compartments:
        param_values[c["volume_parameter"]] = float(c["volume_value"])

    species_values: Dict[str, float] = {s["name"]: float(s["initial_amount"]) for s in species}

    for c in compartments:
        if float(c["volume_value"]) <= 0:
            errors.append(f"Compartment '{c['name']}' has non-positive volume_value={c['volume_value']}")

    for s in species:
        name = s["name"]
        init = float(s["initial_amount"])
        if init <= 0:
            errors.append(f"Species '{name}' has non-positive initial_amount={s['initial_amount']}")

        if "_" not in name:
            errors.append(f"Species '{name}' is missing '_<Compartment>' suffix")
        else:
            suffix = name.rsplit("_", 1)[1]
            if suffix not in compartment_names:
                errors.append(
                    f"Species '{name}' suffix '{suffix}' does not match declared compartments {sorted(compartment_names)}"
                )

    for p in parameters:
        pname = p["name"]
        val = float(p["value"])
        if pname.startswith("k_"):
            if val <= 0:
                errors.append(f"Rate constant '{pname}' must be > 0, found {val}")
            if not (1e-15 <= val <= 1e3):
                warnings.append(f"Rate constant '{pname}'={val:g} is outside heuristic range [1e-15, 1e3]")

    for r in reactions:
        rname = r["name"]
        for side in ("reactants", "products"):
            for sp in r.get(side, []) or []:
                if sp not in species_names:
                    errors.append(f"Reaction '{rname}' references unknown species '{sp}' in {side}")

        for rp in r.get("rate_parameters", []) or []:
            if rp not in allowed_param_like:
                errors.append(
                    f"Reaction '{rname}' rate_parameters includes '{rp}' not found in parameters or compartment volume parameters"
                )

        eq = r.get("rate_equation")
        if not eq:
            continue

        ids = extract_identifiers(eq)
        unknown = ids - species_names - allowed_param_like - {"exp", "log", "sqrt", "min", "max", "abs"}
        if unknown:
            errors.append(f"Reaction '{rname}' rate_equation has unknown identifiers: {sorted(unknown)}")

        used_params = (ids & allowed_param_like)
        missing_in_rate_parameters = sorted(used_params - set(r.get("rate_parameters", []) or []))
        if missing_in_rate_parameters:
            warnings.append(
                f"Reaction '{rname}' uses parameter(s) in rate_equation not listed in rate_parameters: {missing_in_rate_parameters}"
            )

        denoms = extract_denominators(eq)
        for d in denoms:
            ident_in_d = extract_identifiers(d)
            for ident in ident_in_d:
                if ident in allowed_param_like and param_values.get(ident, 0.0) <= 0:
                    errors.append(
                        f"Reaction '{rname}' denominator {d!r} includes non-positive parameter '{ident}'={param_values.get(ident)}"
                    )

        eval_values = {}
        eval_values.update(param_values)
        eval_values.update(species_values)
        try:
            val = safe_eval_expr(eq, eval_values)
            if not math.isfinite(val):
                errors.append(f"Reaction '{rname}' rate_equation evaluates to non-finite value at initial state")
        except ZeroDivisionError:
            errors.append(f"Reaction '{rname}' rate_equation has division by zero at initial state")
        except Exception as ex:
            warnings.append(f"Reaction '{rname}' rate_equation could not be safely evaluated at initial state: {ex}")

    return {"errors": errors, "warnings": warnings}


def report_markdown(module_path: Path, schema_stdout: str, result: Dict[str, List[str]]) -> str:
    errors = result["errors"]
    warnings = result["warnings"]

    lines = []
    lines.append(f"# Validation Report: {module_path.name}")
    lines.append("")
    lines.append("## Schema Validation")
    lines.append("")
    lines.append("```text")
    lines.append(schema_stdout.strip() or "(no output)")
    lines.append("```")
    lines.append("")
    lines.append("## Internal Consistency Checks")
    lines.append("")
    if not errors:
        lines.append("- Errors: none")
    else:
        lines.append(f"- Errors ({len(errors)}):")
        for e in errors:
            lines.append(f"  - {e}")

    if not warnings:
        lines.append("- Warnings: none")
    else:
        lines.append(f"- Warnings ({len(warnings)}):")
        for w in warnings:
            lines.append(f"  - {w}")

    lines.append("")
    lines.append("## Outcome")
    lines.append("")
    if errors:
        lines.append("- Result: FAIL")
    else:
        lines.append("- Result: PASS")

    if warnings:
        lines.append("- Notes: warnings are advisory heuristic checks.")
    else:
        lines.append("- Notes: all required checks passed.")

    lines.append("")
    return "\n".join(lines)


def run_schema_validate(module_path: Path) -> Tuple[int, str]:
    import subprocess

    cmd = ["uv", "run", "antimony-bootstrap", "validate-module", str(module_path)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def main() -> int:
    parser = argparse.ArgumentParser(description="Internal consistency checker for module YAML files")
    parser.add_argument("modules", nargs="+", help="Module YAML paths")
    args = parser.parse_args()

    overall_fail = 0
    for m in args.modules:
        module_path = Path(m)
        schema_rc, schema_out = run_schema_validate(module_path)
        result = check_module(module_path)

        report = report_markdown(module_path, schema_out, result)
        report_path = module_path.with_suffix(".validation_report.md")
        report_path.write_text(report, encoding="utf-8")

        if schema_rc != 0 or result["errors"]:
            overall_fail = 1

        print(f"{module_path}: schema_rc={schema_rc}, errors={len(result['errors'])}, warnings={len(result['warnings'])}")
        print(f"report: {report_path}")

    return overall_fail


if __name__ == "__main__":
    raise SystemExit(main())
