#!/usr/bin/env python3
import glob
import json
import math
import os
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Optional, Tuple


BASE_DIR = "data/parameters"
DEEP_BATCH_GLOB = os.path.join(BASE_DIR, "deep_batch_*.json")
STEP1_MERGE_FILE = os.path.join(BASE_DIR, "all_parameters.json")
CONSOLIDATED_OUT = os.path.join(BASE_DIR, "consolidated_parameters.json")
MODULE_DIR = os.path.join(BASE_DIR, "module")
COVERAGE_OUT = os.path.join(BASE_DIR, "parameter_coverage.json")

MODULES_25 = [
    "amyloid_production",
    "amyloid_aggregation",
    "amyloid_clearance",
    "amyloid_transport",
    "tau_phosphorylation",
    "tau_aggregation",
    "neuroinflammation_microglia",
    "neuroinflammation_astrocyte",
    "complement_cascade",
    "synaptic_dysfunction",
    "calcium_homeostasis",
    "oxidative_stress",
    "apoptosis",
    "lipid_metabolism",
    "insulin_signaling",
    "autophagy",
    "metal_homeostasis",
    "bbb_integrity",
    "vascular_caa",
    "apoe_genetics",
    "peripheral_immune",
    "circadian_rhythm",
    "gut_brain_axis",
    "epigenetics",
    "exercise_neuroprotection",
]

MODULE_ALIASES = {
    "abeta_production": "amyloid_production",
    "abeta_aggregation": "amyloid_aggregation",
    "abeta_clearance": "amyloid_clearance",
    "abeta_transport": "amyloid_transport",
    "autophagy_proteostasis": "autophagy",
    "apoptosis_neuronal_death": "apoptosis",
    "vascular": "vascular_caa",
    "trem2_signaling": "neuroinflammation_microglia",
}

SPECIES_RANK = {
    "human": 0,
    "mouse": 1,
    "rat": 2,
    "cell_line": 3,
    "unknown": 4,
}

CONTEXT_RANK = {
    "in_vivo": 0,
    "in_vitro": 1,
    "computational": 2,
    "unknown": 3,
}

FALLBACK_THRESHOLD = 5


def _as_list(data: Any) -> List[Dict[str, Any]]:
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    return []


def _extract_deep_records(payload: Any) -> List[Dict[str, Any]]:
    if not isinstance(payload, dict):
        return _as_list(payload)

    records: List[Dict[str, Any]] = []
    for key in ("parameter_records", "all_parameter_records"):
        records.extend(_as_list(payload.get(key)))

    if not records:
        for paper in _as_list(payload.get("papers")):
            for key in ("parameter_records", "all_parameter_records", "parameters"):
                records.extend(_as_list(paper.get(key)))

    return records


def _normalize_module(module: Any) -> str:
    raw = str(module or "").strip()
    if not raw:
        return "unspecified"
    canonical = MODULE_ALIASES.get(raw, raw)
    return canonical


def _normalize_species(value: Any) -> str:
    text = str(value or "").strip().lower()
    if not text or text == "unspecified":
        return "unknown"
    parts = [p.strip() for p in text.split(",") if p.strip()]
    if not parts:
        return "unknown"
    best = "unknown"
    best_rank = SPECIES_RANK[best]
    for p in parts:
        token = p
        if "human" in p:
            token = "human"
        elif "mouse" in p or "mice" in p:
            token = "mouse"
        elif "rat" in p:
            token = "rat"
        elif "cell" in p:
            token = "cell_line"
        rank = SPECIES_RANK.get(token, SPECIES_RANK["unknown"])
        if rank < best_rank:
            best = token if token in SPECIES_RANK else "unknown"
            best_rank = rank
    return best


def _normalize_context(measurement_type: Any, context: Any) -> str:
    mtext = str(measurement_type or "").strip().lower()
    ctext = str(context or "").strip().lower()
    combined = f"{mtext} {ctext}"
    if "in_vivo" in combined or "in vivo" in combined:
        return "in_vivo"
    if "in_vitro" in combined or "in vitro" in combined:
        return "in_vitro"
    if "computational" in combined or "in_silico" in combined or "in silico" in combined:
        return "computational"
    return "unknown"


def _as_float(value: Any) -> Optional[float]:
    try:
        v = float(value)
        if math.isfinite(v):
            return v
    except (TypeError, ValueError):
        return None
    return None


def _choose_value(record: Dict[str, Any]) -> Optional[float]:
    for field in ("standard_value", "value", "geometric_mean_value", "standard_value_nM_or_1hr"):
        v = _as_float(record.get(field))
        if v is not None:
            return v
    return None


def _load_deep_batch_records(files: Iterable[str]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            payload = json.load(f)
        for r in _extract_deep_records(payload):
            rr = dict(r)
            rr["_source"] = os.path.basename(path)
            rr["_source_kind"] = "deep_batch"
            out.append(rr)
    return out


def _load_step1_records(path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    records: List[Dict[str, Any]] = []
    for row in _as_list(payload):
        r = {
            "parameter_name": row.get("parameter_name"),
            "value": row.get("geometric_mean_value"),
            "standard_value": row.get("geometric_mean_value"),
            "units": row.get("units"),
            "standard_units": row.get("standard_units"),
            "species_source": "unspecified",
            "measurement_type": "unspecified",
            "context": row.get("context_module"),
            "target_module": row.get("context_module"),
            "target_reaction": "unspecified",
            "pmcid": row.get("pmcids", []),
            "confidence": "step1_merged",
            "_weight": int(row.get("value_count") or 1),
            "_source_kind": "step1_all_parameters",
            "_source": os.path.basename(path),
        }
        records.append(r)
    return records


def _iter_pmcids(value: Any) -> List[str]:
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, list):
        return [str(x) for x in value if x]
    return []


def _group_key(record: Dict[str, Any]) -> Tuple[str, str, str]:
    param_name = str(record.get("parameter_name") or "unspecified_parameter").strip() or "unspecified_parameter"
    module = _normalize_module(record.get("target_module"))
    reaction = str(record.get("target_reaction") or "unspecified").strip() or "unspecified"
    return (param_name.lower(), module, reaction.lower())


def consolidate(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = defaultdict(list)
    for r in records:
        grouped[_group_key(r)].append(r)

    consolidated: List[Dict[str, Any]] = []
    for key in sorted(grouped.keys()):
        rows = grouped[key]
        best_row = None
        best_rank = (999, 999)

        weighted_logs = 0.0
        positive_n = 0
        all_numeric_values: List[float] = []
        pmcids = set()
        source_files = set()

        for r in rows:
            species = _normalize_species(r.get("species_source") or r.get("species"))
            context = _normalize_context(r.get("measurement_type"), r.get("context"))
            rank = (SPECIES_RANK.get(species, 999), CONTEXT_RANK.get(context, 999))
            if rank < best_rank:
                best_rank = rank
                best_row = r

            value = _choose_value(r)
            weight = int(r.get("_weight") or 1)
            if value is not None:
                all_numeric_values.extend([value] * max(1, weight))
                if value > 0:
                    weighted_logs += math.log(value) * max(1, weight)
                    positive_n += max(1, weight)

            pmcids.update(_iter_pmcids(r.get("pmcid")))
            source_files.add(str(r.get("_source") or "unknown"))

        geometric_mean = math.exp(weighted_logs / positive_n) if positive_n > 0 else None
        min_value = min(all_numeric_values) if all_numeric_values else None
        max_value = max(all_numeric_values) if all_numeric_values else None

        exemplar = best_row or rows[0]
        canonical_species = _normalize_species(exemplar.get("species_source") or exemplar.get("species"))
        canonical_context = _normalize_context(exemplar.get("measurement_type"), exemplar.get("context"))

        consolidated.append(
            {
                "parameter_name": exemplar.get("parameter_name") or "unspecified_parameter",
                "target_module": _normalize_module(exemplar.get("target_module")),
                "target_reaction": exemplar.get("target_reaction") or "unspecified",
                "value_geometric_mean": geometric_mean,
                "value_min": min_value,
                "value_max": max_value,
                "value_count": len(all_numeric_values),
                "positive_value_count": positive_n,
                "units": exemplar.get("units"),
                "standard_units": exemplar.get("standard_units"),
                "preferred_species": canonical_species,
                "preferred_context": canonical_context,
                "confidence": exemplar.get("confidence"),
                "pmcids": sorted(pmcids),
                "pmcid_count": len(pmcids),
                "source_record_count": len(rows),
                "source_files": sorted(source_files),
                "evidence_text": exemplar.get("text_excerpt") or exemplar.get("evidence_text"),
                "supports": exemplar.get("supports"),
                "measurement_type": exemplar.get("measurement_type"),
            }
        )
    return consolidated


def write_outputs(consolidated: List[Dict[str, Any]]) -> None:
    os.makedirs(MODULE_DIR, exist_ok=True)

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_files": sorted(glob.glob(DEEP_BATCH_GLOB)) + ([STEP1_MERGE_FILE] if os.path.exists(STEP1_MERGE_FILE) else []),
        "total_parameters": len(consolidated),
        "parameters": consolidated,
    }
    with open(CONSOLIDATED_OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=True)

    by_module: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for p in consolidated:
        by_module[p["target_module"]].append(p)

    for module in sorted(set(list(by_module.keys()) + MODULES_25)):
        file_path = os.path.join(MODULE_DIR, f"{module}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "module": module,
                    "parameter_count": len(by_module.get(module, [])),
                    "parameters": by_module.get(module, []),
                },
                f,
                indent=2,
                ensure_ascii=True,
            )

    coverage = {}
    for module in MODULES_25:
        count = len(by_module.get(module, []))
        coverage[module] = {
            "parameter_count": count,
            "elbert_fallback_needed": count < FALLBACK_THRESHOLD,
        }

    with open(COVERAGE_OUT, "w", encoding="utf-8") as f:
        json.dump(
            {
                "generated_at_utc": datetime.now(timezone.utc).isoformat(),
                "fallback_threshold": FALLBACK_THRESHOLD,
                "module_coverage": coverage,
                "modules_below_threshold": [m for m, v in coverage.items() if v["elbert_fallback_needed"]],
            },
            f,
            indent=2,
            ensure_ascii=True,
        )


def main() -> None:
    deep_files = sorted(glob.glob(DEEP_BATCH_GLOB))
    if not deep_files:
        raise FileNotFoundError(f"No deep batch files found using pattern: {DEEP_BATCH_GLOB}")

    deep_records = _load_deep_batch_records(deep_files)
    step1_records = _load_step1_records(STEP1_MERGE_FILE)
    consolidated = consolidate(deep_records + step1_records)
    write_outputs(consolidated)

    print(f"Loaded deep batch files: {len(deep_files)}")
    print(f"Loaded deep records: {len(deep_records)}")
    print(f"Loaded Step 1 records: {len(step1_records)}")
    print(f"Wrote: {CONSOLIDATED_OUT}")
    print(f"Wrote module files to: {MODULE_DIR}")
    print(f"Wrote: {COVERAGE_OUT}")
    print(f"Consolidated parameter rows: {len(consolidated)}")


if __name__ == "__main__":
    main()
