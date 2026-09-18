"""Illustrative vector and cell-lot arithmetic, not a manufacturing specification."""

import math

from .lot_criteria import COMMERCIAL_US, assess_lot


def _nonnegative(**values):
    for name, value in values.items():
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
            or value < 0
        ):
            raise ValueError(f"{name} must be finite and nonnegative")


def _fraction(**values):
    _nonnegative(**values)
    for name, value in values.items():
        if value > 1:
            raise ValueError(f"{name} must be at most one")


def vector_production(titer_target=1.0e8, packaging_efficiency=0.9):
    """Hypothetical titer arithmetic (TU/mL)."""
    _nonnegative(titer_target=titer_target)
    _fraction(packaging_efficiency=packaging_efficiency)
    unconc = 1.0e7 * packaging_efficiency
    conc = unconc * 8.0
    return {
        "titer_unconc_TU_mL": unconc,
        "titer_conc_TU_mL": conc,
        "meets_target": conc >= titer_target,
        "target_TU_mL": titer_target,
    }


def manufacture(
    apheresis_wbc=1.5e10,
    t_cell_frac=0.45,
    net_yield=0.05,
    te=0.55,
    vcn=None,
    viability=0.92,
    dose_target=2.0e8,
    *,
    profile=COMMERCIAL_US,
    indication="DLBCL",
    weight_kg=None,
    sterility=None,
    mycoplasma=None,
):
    """Apheresis -> T isolation -> bead activation -> lentiviral transduction ->
    expansion -> cryo -> dose. Yield and composition defaults remain illustrative.

    net_yield is recovered total T cells per starting T cell, BEFORE viability.
    te is CAR-positive fraction among viable T cells. dose_target is viable CAR+
    cells. Viability is applied exactly once. VCN is unknown unless supplied.
    sterility and mycoplasma are the boolean negative-culture results behind the
    unredacted SBRA qualitative requirements; None keeps them unknown.
    The source-profile comparison does not authorize release of an actual lot.
    """
    _nonnegative(apheresis_wbc=apheresis_wbc, net_yield=net_yield, dose_target=dose_target)
    if vcn is not None:
        _nonnegative(vcn=vcn)
    _fraction(t_cell_frac=t_cell_frac, te=te, viability=viability)
    t_cells = apheresis_wbc * t_cell_frac
    product_total = t_cells * net_yield
    _nonnegative(product_total_cells=product_total)
    product_viable = product_total * viability
    product_car = product_viable * te
    scale = min(1.0, dose_target / product_car) if product_car > 0 else 0.0
    dose_total = product_total * scale
    car_frac = te
    dose_viable = dose_total * viability
    dose_car = min(product_car, dose_target)
    assessment = assess_lot(
        {
            "viability": viability,
            "car_fraction": te,
            "vcn_copies_cell": vcn,
            "dose_viable_car_cells": dose_car,
            "sterility_negative": sterility,
            "mycoplasma_negative": mycoplasma,
        },
        profile,
        indication=indication,
        weight_kg=weight_kg,
    )
    return {
        "apheresis_WBC": apheresis_wbc,
        "T_cells": t_cells,
        "TE_pct": 100 * te,
        "VCN": vcn,
        "viability_pct": 100 * viability,
        "product_total_cells": product_total,
        "product_viable_cells": product_viable,
        "product_viable_car_cells": product_car,
        "dose_total_cells": dose_total,
        "dose_viable_cells": dose_viable,
        "dose_viable_car_cells": dose_car,
        "dose_CARplus_cells": dose_car,
        "dose_target_viable_car_cells": dose_target,
        "CARplus_frac": car_frac,
        "source_assessment": assessment,
    }
