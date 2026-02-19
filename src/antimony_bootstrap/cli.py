"""Typer CLI for antimony_bootstrap."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(name="antimony-bootstrap", help="Build parameterized Antimony ODE models from disease mechanisms.")
console = Console()

MODELS_DIR = Path("models")


def _get_disease_dir(disease: str) -> Path:
    return MODELS_DIR / disease


@app.command()
def validate_module(file: Path = typer.Argument(..., help="Path to module YAML file")):
    """Validate a single module YAML against the Pydantic schema."""
    from antimony_bootstrap.schema.module_spec import ModuleSpec

    try:
        module = ModuleSpec.from_yaml(file)
        console.print(f"[green]Valid[/green]: {module.name} ({len(module.reactions)} reactions, {len(module.parameters)} parameters)")
    except Exception as e:
        console.print(f"[red]Invalid[/red]: {e}")
        raise typer.Exit(1)


@app.command()
def validate_modules(disease: str = typer.Option("alzheimers", help="Disease name")):
    """Validate all module YAMLs for a disease."""
    from antimony_bootstrap.schema.module_spec import ModuleSpec

    modules_dir = _get_disease_dir(disease) / "modules"
    if not modules_dir.exists():
        console.print(f"[red]No modules directory: {modules_dir}[/red]")
        raise typer.Exit(1)

    yaml_files = sorted(modules_dir.glob("*.yaml"))
    if not yaml_files:
        console.print(f"[yellow]No module YAML files found in {modules_dir}[/yellow]")
        raise typer.Exit(1)

    errors = 0
    for f in yaml_files:
        try:
            module = ModuleSpec.from_yaml(f)
            console.print(f"  [green]OK[/green] {f.name}: {module.name}")
        except Exception as e:
            console.print(f"  [red]FAIL[/red] {f.name}: {e}")
            errors += 1

    if errors:
        console.print(f"\n[red]{errors} module(s) failed validation[/red]")
        raise typer.Exit(1)
    console.print(f"\n[green]All {len(yaml_files)} modules valid[/green]")


@app.command()
def validate_params(disease: str = typer.Option("alzheimers", help="Disease name")):
    """Check parameter completeness for all modules."""
    from antimony_bootstrap.modules.base import load_modules_from_dir
    from antimony_bootstrap.validation.completeness import check_completeness

    modules_dir = _get_disease_dir(disease) / "modules"
    modules = load_modules_from_dir(modules_dir)

    complete, issues = check_completeness(modules)
    for issue in issues:
        console.print(f"  [yellow]{issue}[/yellow]")

    if complete:
        console.print("[green]All parameters complete[/green]")
    else:
        console.print(f"\n[red]{len(issues)} completeness issue(s)[/red]")
        raise typer.Exit(1)


@app.command()
def assemble(disease: str = typer.Option("alzheimers", help="Disease name")):
    """Compose modules into an Antimony model."""
    from antimony_bootstrap.assembly.composer import compose_from_manifest
    from antimony_bootstrap.export.antimony_writer import write_antimony

    manifest_path = _get_disease_dir(disease) / "model.yaml"
    if not manifest_path.exists():
        console.print(f"[red]No manifest: {manifest_path}[/red]")
        raise typer.Exit(1)

    antimony_str, species, parameters, compartments = compose_from_manifest(manifest_path)

    output_dir = _get_disease_dir(disease) / "generated"
    ant_path = write_antimony(antimony_str, output_dir / f"{disease}_model.ant")

    console.print(f"[green]Assembled[/green]: {ant_path}")
    console.print(f"  {len(compartments)} compartments, {len(species)} species, {len(parameters)} parameters")


@app.command()
def validate_antimony(disease: str = typer.Option("alzheimers", help="Disease name")):
    """Parse check with antimony library."""
    from antimony_bootstrap.validation.antimony_check import validate_antimony_file

    ant_path = _get_disease_dir(disease) / "generated" / f"{disease}_model.ant"
    if not ant_path.exists():
        console.print(f"[red]No .ant file: {ant_path}. Run 'assemble' first.[/red]")
        raise typer.Exit(1)

    success, errors = validate_antimony_file(str(ant_path))
    if success:
        console.print(f"[green]Antimony parse OK[/green]: {ant_path}")
    else:
        for err in errors:
            console.print(f"  [red]{err}[/red]")
        raise typer.Exit(1)


@app.command()
def smoke_test(disease: str = typer.Option("alzheimers", help="Disease name")):
    """Quick tellurium simulation."""
    from antimony_bootstrap.validation.simulation_check import smoke_test as run_smoke

    ant_path = _get_disease_dir(disease) / "generated" / f"{disease}_model.ant"
    if not ant_path.exists():
        console.print(f"[red]No .ant file: {ant_path}. Run 'assemble' first.[/red]")
        raise typer.Exit(1)

    antimony_str = ant_path.read_text()
    success, errors, result = run_smoke(antimony_str)

    if success:
        console.print(f"[green]Simulation OK[/green]: {result.shape[0]} timepoints, {result.shape[1]} columns")
    else:
        for err in errors:
            console.print(f"  [red]{err}[/red]")
        raise typer.Exit(1)


@app.command()
def qc(disease: str = typer.Option("alzheimers", help="Disease name")):
    """Full pipeline: validate modules + assemble + antimony check + simulate."""
    console.print("[bold]Running full QC pipeline...[/bold]\n")

    console.print("[bold]1. Validating modules...[/bold]")
    try:
        validate_modules(disease=disease)
    except SystemExit:
        console.print("[red]Module validation failed. Stopping.[/red]")
        raise typer.Exit(1)

    console.print("\n[bold]2. Assembling model...[/bold]")
    try:
        assemble(disease=disease)
    except SystemExit:
        console.print("[red]Assembly failed. Stopping.[/red]")
        raise typer.Exit(1)

    console.print("\n[bold]3. Validating Antimony...[/bold]")
    try:
        validate_antimony(disease=disease)
    except SystemExit:
        console.print("[red]Antimony validation failed. Stopping.[/red]")
        raise typer.Exit(1)

    console.print("\n[bold]4. Running smoke test...[/bold]")
    try:
        smoke_test(disease=disease)
    except SystemExit:
        console.print("[red]Smoke test failed.[/red]")
        raise typer.Exit(1)

    console.print("\n[bold green]All QC checks passed![/bold green]")


@app.command()
def read_dismech(file: Path = typer.Argument(..., help="Path to dismech disorder YAML")):
    """Extract mechanisms from a dismech YAML file."""
    from antimony_bootstrap.dismech.mechanism_graph import build_mechanism_graph, topological_order
    from antimony_bootstrap.dismech.reader import extract_disease_metadata, extract_mechanisms

    from antimony_bootstrap.dismech.reader import load_dismech_yaml

    data = load_dismech_yaml(file)
    metadata = extract_disease_metadata(data)
    mechanisms = extract_mechanisms(data)
    graph = build_mechanism_graph(mechanisms)
    order = topological_order(graph)

    console.print(f"[bold]{metadata['name']}[/bold] ({metadata['disease_id']})")
    console.print(f"  {metadata['description'][:100]}...")
    console.print(f"\n[bold]Mechanisms ({len(mechanisms)}):[/bold]")

    for name in order:
        mech = next((m for m in mechanisms if m["name"] == name), None)
        if mech:
            downstream = ", ".join(mech["downstream"]) if mech["downstream"] else "none"
            pmids = [e["reference"] for e in mech["evidence"] if e["reference"].startswith("PMID:")]
            console.print(f"  {name}")
            console.print(f"    downstream: {downstream}")
            console.print(f"    evidence: {len(pmids)} PMIDs")


@app.command()
def search_biomodels(query: str = typer.Argument(..., help="Search query")):
    """Search BioModels API for reference models."""
    from antimony_bootstrap.retrieval.biomodels import search_biomodels as search

    results = search(query)

    if not results:
        console.print("[yellow]No results found[/yellow]")
        return

    table = Table(title=f"BioModels search: '{query}'")
    table.add_column("ID", style="cyan")
    table.add_column("Name")
    table.add_column("URL", style="dim")

    for r in results:
        table.add_row(r["id"], r["name"][:60], r["url"])

    console.print(table)


@app.command()
def provenance(disease: str = typer.Option("alzheimers", help="Disease name")):
    """Generate parameter provenance report."""
    from antimony_bootstrap.assembly.parameterizer import generate_provenance_report
    from antimony_bootstrap.modules.base import load_modules_from_dir

    modules_dir = _get_disease_dir(disease) / "modules"
    modules = load_modules_from_dir(modules_dir)

    report = generate_provenance_report(modules)
    output_dir = _get_disease_dir(disease) / "generated"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "provenance.md"
    output_path.write_text(report)

    console.print(f"[green]Provenance report written to {output_path}[/green]")


if __name__ == "__main__":
    app()
