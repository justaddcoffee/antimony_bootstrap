"""Pydantic schema for module specifications.

The intermediate representation that bridges qualitative biology to quantitative Antimony models.
"""

from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field, model_validator


class RateType(str, Enum):
    """Supported reaction rate types, matching Elbert's RxnDict_to_antimony.py."""

    MA = "MA"  # Mass action (unidirectional), rate * V_compartment
    RMA = "RMA"  # Reversible mass action, forward + reverse reactions
    BDF = "BDF"  # Bidirectional flow, same rate constant both directions
    UDF = "UDF"  # Unidirectional flow, no volume multiplication
    CUSTOM_CONC = "custom_conc_per_time"  # Custom rate in conc/time, * V_compartment
    CUSTOM_AMT = "custom_amt_per_time"  # Custom rate in amt/time, no volume mult
    CUSTOM = "custom"  # Custom rate expression used as-is


class Confidence(str, Enum):
    """Confidence level for parameter values."""

    MEASURED = "measured"  # Directly measured in relevant system
    ESTIMATED = "estimated"  # Estimated from related data
    ASSUMED = "assumed"  # Assumed/placeholder value


class EvidenceRef(BaseModel):
    """A literature reference supporting a claim."""

    pmid: Optional[str] = None
    doi: Optional[str] = None
    source: Optional[str] = None  # Free text source description
    snippet: Optional[str] = None  # Quoted text from the source


class CompartmentSpec(BaseModel):
    """A compartment in the model."""

    name: str
    volume_parameter: Optional[str] = None  # e.g., "V_BrainISF"
    volume_value: Optional[float] = None
    volume_units: Optional[str] = "L"
    notes: Optional[str] = None

    @model_validator(mode="after")
    def set_volume_parameter(self) -> "CompartmentSpec":
        if self.volume_parameter is None:
            self.volume_parameter = f"V_{self.name}"
        return self


class SpeciesSpec(BaseModel):
    """A species (molecular entity) in the model."""

    name: str  # Full name including compartment suffix, e.g., AB42_BrainISF
    compartment: Optional[str] = None  # Inferred from name if not set
    initial_amount: Optional[float] = None
    initial_concentration: Optional[float] = None
    units: Optional[str] = None
    substance_only: bool = True  # Use substanceOnly in Antimony
    notes: Optional[str] = None

    @model_validator(mode="after")
    def infer_compartment(self) -> "SpeciesSpec":
        if self.compartment is None and "_" in self.name:
            self.compartment = self.name.rsplit("_", 1)[-1]
        return self


class ParameterSpec(BaseModel):
    """A parameter with value, provenance, and confidence."""

    name: str
    value: Optional[float] = None  # Nullable until parameterized
    units: Optional[str] = None
    confidence: Optional[Confidence] = None
    source: Optional[str] = None  # Where the value came from
    evidence: list[EvidenceRef] = Field(default_factory=list)
    notes: Optional[str] = None


class ReactionSpec(BaseModel):
    """A reaction specification."""

    name: str  # Reaction identifier, e.g., "AB42_production_neurons"
    reactants: list[str] = Field(default_factory=list)  # Species names; empty = source
    products: list[str] = Field(default_factory=list)  # Species names; empty = sink
    rate_type: RateType = RateType.MA
    rate_equation: Optional[str] = None  # For custom rate types
    rate_parameters: list[str] = Field(default_factory=list)  # Parameter names used
    evidence: list[EvidenceRef] = Field(default_factory=list)
    notes: Optional[str] = None

    def to_reaction_dict(self) -> dict:
        """Convert to Elbert-style reaction dictionary."""
        reactants_str = (
            "[" + ", ".join(self.reactants) + "]" if self.reactants else "[0]"
        )
        products_str = (
            "[" + ", ".join(self.products) + "]" if self.products else "[0]"
        )

        if self.rate_type in (RateType.CUSTOM, RateType.CUSTOM_CONC, RateType.CUSTOM_AMT):
            rate_proto = self.rate_equation or ""
        else:
            rate_proto = "[" + ", ".join(self.rate_parameters) + "]"

        return {
            "Reaction_name": self.name,
            "Reactants": reactants_str,
            "Products": products_str,
            "Rate_type": self.rate_type.value,
            "Rate_eqtn_prototype": rate_proto,
        }


class RuleSpec(BaseModel):
    """An algebraic or assignment rule."""

    name: str
    equation: str  # e.g., "total_AB42 = AB42_BrainISF + AB42_CSF + AB42_Plasma"
    notes: Optional[str] = None


class ModuleSpec(BaseModel):
    """A complete module specification for one mechanism."""

    name: str  # e.g., "abeta_production"
    description: Optional[str] = None
    mechanism: Optional[str] = None  # Link to dismech mechanism name
    compartments: list[CompartmentSpec] = Field(default_factory=list)
    species: list[SpeciesSpec] = Field(default_factory=list)
    reactions: list[ReactionSpec] = Field(default_factory=list)
    parameters: list[ParameterSpec] = Field(default_factory=list)
    rules: list[RuleSpec] = Field(default_factory=list)
    evidence: list[EvidenceRef] = Field(default_factory=list)
    notes: Optional[str] = None

    @classmethod
    def from_yaml(cls, path: str | Path) -> "ModuleSpec":
        """Load a ModuleSpec from a YAML file."""
        with open(path) as f:
            data = yaml.safe_load(f)
        return cls(**data)

    def to_yaml(self, path: str | Path) -> None:
        """Write this ModuleSpec to a YAML file."""
        with open(path, "w") as f:
            yaml.dump(
                self.model_dump(exclude_none=True, exclude_defaults=True),
                f,
                default_flow_style=False,
                sort_keys=False,
            )

    def get_all_species_names(self) -> list[str]:
        """Return all species names defined in this module."""
        return [s.name for s in self.species]

    def get_all_compartment_names(self) -> list[str]:
        """Return all compartment names defined in this module."""
        return [c.name for c in self.compartments]

    def get_all_parameter_names(self) -> list[str]:
        """Return all parameter names defined in this module."""
        return [p.name for p in self.parameters]

    def get_unparameterized(self) -> list[str]:
        """Return parameter names that have no value assigned."""
        return [p.name for p in self.parameters if p.value is None]

    def to_reaction_dicts(self) -> list[dict]:
        """Convert all reactions to Elbert-style reaction dictionaries."""
        return [r.to_reaction_dict() for r in self.reactions]


class ModelManifest(BaseModel):
    """Top-level manifest describing a complete disease model."""

    name: str  # e.g., "Alzheimer's Disease"
    disease_id: Optional[str] = None  # MONDO term, e.g., "MONDO:0004975"
    description: Optional[str] = None
    modules: list[str] = Field(default_factory=list)  # Module YAML filenames
    shared_compartments: list[CompartmentSpec] = Field(default_factory=list)
    shared_parameters: list[ParameterSpec] = Field(default_factory=list)
    notes: Optional[str] = None

    @classmethod
    def from_yaml(cls, path: str | Path) -> "ModelManifest":
        """Load a ModelManifest from a YAML file."""
        with open(path) as f:
            data = yaml.safe_load(f)
        return cls(**data)
