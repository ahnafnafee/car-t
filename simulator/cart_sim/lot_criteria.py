"""Compare lot attributes with disclosed research criteria, never authorize release."""

import math

COMMERCIAL_US = "us_commercial_2020"
ACADEMIC_CTL019 = "academic_ctl019_2022"
SOURCES = {
    COMMERCIAL_US: "https://doi.org/10.1182/bloodadvances.2020003092",
    ACADEMIC_CTL019: "https://doi.org/10.1126/sciadv.abj2820",
}


def dose_interval(indication, weight_kg=None):
    """Published US viable CAR-positive cell interval, not a prescribed dose."""
    if indication == "DLBCL":
        return 6e7, 6e8
    if indication != "B-ALL":
        raise ValueError("indication must be DLBCL or B-ALL")
    if (
        isinstance(weight_kg, bool)
        or not isinstance(weight_kg, (int, float))
        or not math.isfinite(weight_kg)
        or weight_kg <= 0
    ):
        raise ValueError("B-ALL comparison requires a positive finite weight_kg")
    return (2e5 * weight_kg, 5e6 * weight_kg) if weight_kg <= 50 else (1e7, 2.5e8)


def assess_lot(measurements, profile=COMMERCIAL_US, *, indication="DLBCL", weight_kg=None):
    """Missing measurements stay unknown; passing a source subset is not lot release.

    Fractions use 0..1. VCN is copies/cell; residual beads are per 3 million
    cells, endotoxin EU/mL, BSA micrograms/mL, and VSV-G copies/microgram DNA.
    Negative microbial tests are represented by True for the corresponding
    ``*_negative`` key. Measurements must use the source's assay denominator.
    """
    if profile not in SOURCES:
        raise ValueError(f"Unknown lot profile: {profile}")
    if profile == COMMERCIAL_US:
        low, high = dose_interval(indication, weight_kg)
        rules = {"viability": (0.8, 1), "dose_viable_car_cells": (low, high)}
        microbial = ()
        unreported = ["complete_commercial_release_panel", "validated_assay_methods"]
    else:
        rules = {
            "viability": (0.7, 1),
            "cd3_fraction": (0.8, 1),
            "residual_beads_per_3m": (0, 100),
            "endotoxin_eu_ml": (0, 3.5),
            "bsa_ug_ml": (0, 1),
            "vsvg_copies_ug_dna": (0, 50),
            "car_fraction": (0.02, 1),
            "vcn_copies_cell": (0.02, 4),
        }
        microbial = ("mycoplasma_negative", "bacterial_negative", "fungal_negative")
        unreported = []
    checks = {}
    for name, (low, high) in rules.items():
        value = measurements.get(name)
        if value is not None:
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value < 0
            ):
                raise ValueError(f"{name} must be a finite nonnegative measurement")
            if name in ("viability", "car_fraction", "cd3_fraction") and value > 1:
                raise ValueError(f"{name} must be a fraction")
        checks[name] = {
            "value": value,
            "minimum": low,
            "maximum": high,
            "met": None if value is None else low <= value <= high,
        }
    for name in microbial:
        value = measurements.get(name)
        if value is not None and not isinstance(value, bool):
            raise ValueError(f"{name} must be boolean or None")
        checks[name] = {"value": value, "met": value}
    failed = [name for name, check in checks.items() if check["met"] is False]
    missing = [name for name, check in checks.items() if check["met"] is None]
    status = (
        "fails_disclosed_criteria"
        if failed
        else ("incomplete" if missing else "meets_disclosed_criteria")
    )
    return {
        "profile": profile,
        "source": SOURCES[profile],
        "status": status,
        "checks": checks,
        "failed": failed,
        "missing": missing,
        "unreported_specifications": unreported,
        "commercial_release_established": False,
    }
