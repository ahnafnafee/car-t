"""Which published kinetic quantities can constrain this model, and which cannot.

The published CAR-T kinetics literature is reported on two different axes:

* **Time** - days to peak transgene (Tmax), duration of detectable transgene,
  manufacturing cycle time. These are reported in days and are denominator-free,
  so they constrain the simulator's time axis directly.
* **Amplitude** - blood transgene as copies per microgram of genomic DNA (qPCR) or
  as a percentage of CD3-positive cells (flow). The simulator's state variable is a
  *cell count*, so comparing amplitudes requires a sample-denominator conversion.

That conversion needs three factors that no retained record in
``data/references/`` supplies: the leukocyte concentration of the sampled blood, the
genomic-DNA mass per leukocyte, and the vector copy number per CAR-positive cell.
Until a record supplying them is retained, the simulator's expansion amplitude is
declared non-fitted; only its timing is comparable to published kinetics. See
``docs/KINETICS_SOURCES.md``.
"""

#: Model state whose magnitude is a cell count.
MODEL_AMPLITUDE_STATE = "E (CAR-positive effector cells) and M (memory CAR-positive cells)"

#: Parameters whose values are therefore not fitted to published transgene amplitudes.
NON_FITTED_AMPLITUDE_PARAMS = ("pE", "dE0", "Ks_E", "sE", "Emax", "kKill0", "Kd_T", "kKill_fixed")

#: Published statistics whose published unit is a day count, i.e. directly
#: comparable to the simulated time axis without any conversion.
TIME_DENOMINATOR_STATS = (
    "eliana2018_tmax_responders_days",
    "eliana2018_persistence_days",
    "eliana2018_screen_to_infuse_days",
    "tyagarajan2020_cycle_days",
)

#: Published statistics whose published unit is a cell count per kg or per patient,
#: i.e. directly comparable to the manufacturing chain's output.
CELL_DENOMINATOR_STATS = ("eliana2018_dose_per_kg", "eliana2018_total_dose")

#: The conversion factors required to compare amplitudes, and their status.
AMPLITUDE_BRIDGE_FACTORS = (
    {
        "name": "leukocyte_concentration_in_sampled_blood",
        "symbol": "WBC (cells per mL of whole blood)",
        "needed_for": "converting per-mL transgene to per-cell, or per-microgram DNA to per-mL",
        "status": "not supplied by any retained record",
    },
    {
        "name": "genomic_dna_mass_per_leukocyte",
        "symbol": "gDNA (micrograms per cell)",
        "needed_for": "converting copies/microgram genomic DNA to copies per cell",
        "status": "not supplied by any retained record",
    },
    {
        "name": "vector_copy_number_per_car_positive_cell",
        "symbol": "VCN (integrations per cell)",
        "needed_for": "converting transgene copies to CAR-positive cells",
        "status": "not supplied by any retained record; the commercial release VCN "
        "limit is a (b)(4) redaction, see docs/RELEASE_SOURCES.md",
    },
)

#: Permanent label: never present a simulated peak amplitude as a fitted value.
AMPLITUDE_IS_FITTED = False


def bridge_status():
    """Plain-language statement of what the kinetics can and cannot be compared to."""
    lines = [
        "Kinetic unit denominators:",
        "  comparable without conversion (time): " + ", ".join(TIME_DENOMINATOR_STATS),
        "  comparable without conversion (cells): " + ", ".join(CELL_DENOMINATOR_STATS),
        f"  model amplitude state: {MODEL_AMPLITUDE_STATE}",
        "  amplitude bridge factors, each required to compare peak transgene with qPCR",
        "  or flow data:",
    ]
    for factor in AMPLITUDE_BRIDGE_FACTORS:
        lines.append(f"    - {factor['symbol']}: {factor['needed_for']} [{factor['status']}]")
    lines.append(
        "  therefore AMPLITUDE_IS_FITTED = "
        f"{AMPLITUDE_IS_FITTED}; non-fitted amplitude parameters: "
        + ", ".join(NON_FITTED_AMPLITUDE_PARAMS)
    )
    return lines


def transgene_per_microgram_dna(car_positive_cells_per_ml, vcn_copies_per_cell, leukocytes_per_ml, dna_ug_per_cell):
    """Model blood transgene on the published qPCR axis, given the bridge factors.

    ``copies per microgram genomic DNA = VCN * CAR+ cells per mL / (leukocytes per mL
    * micrograms DNA per leukocyte)``. Every argument must be supplied by the caller;
    none of them comes from a retained record, so a value produced here is a
    scenario, not a prediction of a published number.
    """
    for name, value in (
        ("car_positive_cells_per_ml", car_positive_cells_per_ml),
        ("vcn_copies_per_cell", vcn_copies_per_cell),
        ("leukocytes_per_ml", leukocytes_per_ml),
        ("dna_ug_per_cell", dna_ug_per_cell),
    ):
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
            raise ValueError(f"{name} must be a positive number, got {value!r}")
    dna_ug_per_ml = leukocytes_per_ml * dna_ug_per_cell
    return vcn_copies_per_cell * car_positive_cells_per_ml / dna_ug_per_ml
