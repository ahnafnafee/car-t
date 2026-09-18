"""Published per-patient product attributes used instead of illustrative defaults.

This module answers the checklist item "map published per-patient product
attributes (transduction efficiency, viability, dose recovered) into empirical
cohort distributions instead of defaults" in ``docs/ONE_TO_ONE.md``.

Evidence discipline
    Every statistic in :data:`ATTRIBUTES` is transcribed verbatim from a file
    retained under ``data/references/`` (see ``data/references/README.md`` for
    hashes and source URLs). ``tests/test_lot_distributions.py`` asserts each
    ``quote`` is a byte-exact substring of the retained file, so a statistic
    cannot drift away from its source. The retained Fong 2023 file is a
    PDF-to-markdown parse, so its quotes carry the parse artefacts (``£`` for
    the multiplication sign, ``<sup>`` tags, ``CARpositive``); they are quoted
    as stored, not retypeset.

Sampling discipline
    Median/range entries are drawn with
    :func:`simulator.cart_sim.publication_stats.calibrate` - the two-sided
    log-normal whose median is the published median and whose expected extremes
    are the published range. The distribution family and the range-to-sigma
    rule are documented modelling conventions, not published facts. The 2025
    Japanese out-of-specification cohort is used as an *empirical* resample of
    its 23 published patients, so it assumes no family at all.

    A profile never relaxes a release criterion (see ``lot_criteria.py``), and
    no value here is a simulation output.
"""

import random

from . import publication_stats

#: Retrieved and byte-checked 2026-09-18 against the retained files.
FONG_URL = "https://doi.org/10.1016/j.jtct.2023.06.007"
PASQUINI_URL = "https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/"
PI_URL = "https://www.fda.gov/media/107296/download"
PATENT_URL = "https://patents.google.com/patent/US20050113564A1/en"
KATO_URL = "https://www.sciencedirect.com/science/article/pii/S1465324925006851"

FONG = "Fong et al., Transplant Cell Ther 2023;29(9):579.e1-e10, doi:10.1016/j.jtct.2023.06.007"
PASQUINI = "Pasquini et al., Blood Advances 2020, doi:10.1182/bloodadvances.2020003092"
PI = "KYMRIAH prescribing information (retained copy, FDA media 107296)"
KATO = "Kato et al., Cytotherapy 2025 (NCT04094311, Japan OOS study)"

_PASQUINI_VIABILITY_QUOTE = (
    "Median cell viabilities were 87.1% (range, 66.7% to 96.8%) and "
    "83.8% (range, 61.4% to 94.9%) for patients with ALL and NHL, respectively."
)

#: Published lot attributes, keyed by attribute. Same schema as
#: ``publication_stats.STATS`` (merged into it at import below).
ATTRIBUTES = {
    # -- Commercial final product and leukapheresis input (Fong 2023):
    # post-approval commercial tisagenlecleucel for r/r B-ALL age <3 y; 146
    # quality-control batches (86 US / 60 non-US) with manufacturing data
    # starting after the 2017-08-30 first US approval.
    "fong2023_dose_per_kg": {
        "median": 2.65e6,
        "low": 0.23e6,
        "high": 4.98e6,
        "n": 146,
        "n_basis": "146 manufactured commercial batches (86 US batches / 84 patients, 60 non-US)",
        "unit": "CAR-positive viable T cells/kg body weight (manufactured product)",
        "source": FONG + ", Results, Manufacturing Outcomes",
        "url": FONG_URL,
        "file": "data/references/fong_2023_tct_fulltext_oa.md",
        "quote": "The median manufactured cell dose was 2.65 £ 10<sup>6</sup> CAR"
        "positive viable T cells/kg (range, .23 to 4.98 £ 10<sup>6</sup>",
        "population": "pediatric B-ALL age <3 y, commercial product, manufactured dose",
    },
    "fong2023_viability_pct": {
        "median": 91.5,
        "low": 66.7,
        "high": 98.3,
        "n": 146,
        "n_basis": "the same 146 manufactured commercial batches",
        "unit": "% viable cells in the final product (assay improved 2019-2020)",
        "source": FONG + ", Results, Manufacturing Outcomes",
        "url": FONG_URL,
        "file": "data/references/fong_2023_tct_fulltext_oa.md",
        "quote": "median cell viability was 91.5% (range, 66.7% to 98.3%",
        "population": "pediatric B-ALL age <3 y, commercial final product",
    },
    "fong2023_car_fraction": {
        "median": 0.12,
        "low": 0.021,
        "high": 0.372,
        "n": 146,
        "n_basis": "the same 146 manufactured commercial batches",
        "unit": "fraction of final-product cells that are CAR-positive (flow)",
        "source": FONG + ", Results, Manufacturing Outcomes",
        "url": FONG_URL,
        "file": "data/references/fong_2023_tct_fulltext_oa.md",
        "quote": "median CAR-positive expression was 12% (range, 2.1% to 37.2%",
        "population": "pediatric B-ALL age <3 y, commercial final product",
        "note": "Final-product CAR positivity, not a transduction assay on an "
        "intermediate process sample; it is the only public commercial "
        "final-product CAR-positive distribution in the retained corpus.",
    },
    "fong2023_leukapheresis_cd3_cells": {
        "median": 1.29e9,
        "low": 1.64e8,
        "high": 5.98e9,
        "n": 146,
        "n_basis": "146 batches analyzed for CD3+ count and CD3+/TNC%",
        "unit": "CD3+ cells in the incoming leukapheresis material",
        "source": FONG + ", Results, Leukapheresis Characteristics",
        "url": FONG_URL,
        "file": "data/references/fong_2023_tct_fulltext_oa.md",
        "quote": "the median incoming CD3<sup>+</sup> cell\ncount was 1.29 £ 10<sup>9</sup>"
        " CD3<sup>+</sup> cells (range, 1.64 £ 10<sup>8</sup> to\n5.98 £ 10<sup>9</sup>)",
        "population": "pediatric B-ALL age <3 y, collected leukapheresis material",
    },
    "fong2023_weight_kg": {
        "median": 10.4,
        "low": 5.8,
        "high": 20.0,
        "n": 84,
        "n_basis": "US-site patients behind the 86 US batches (median age 1.2 y)",
        "unit": "kg body weight",
        "source": FONG + ", Results, Patient Characteristics",
        "url": FONG_URL,
        "file": "data/references/fong_2023_tct_fulltext_oa.md",
        "quote": "median body weight was 10.4 kg (range, 5.8 to\n20 kg)",
        "population": "pediatric B-ALL age <3 y, US sites",
    },
    # -- Real-world US registry product attributes (Pasquini 2020, CIBMTR) --
    "pasquini2020_viability_all_pct": {
        "median": 87.1,
        "low": 66.7,
        "high": 96.8,
        "n": 255,
        "n_basis": "255 infused ALL patients; batch numbers available for 383 of 410",
        "unit": "% viable T cells in the final product",
        "source": PASQUINI + ", Results",
        "url": PASQUINI_URL,
        "file": "data/references/pasquini_2020_rwe.txt",
        "quote": _PASQUINI_VIABILITY_QUOTE,
        "population": "US registry (CIBMTR) real-world tisagenlecleucel, ALL",
    },
    "pasquini2020_viability_nhl_pct": {
        "median": 83.8,
        "low": 61.4,
        "high": 94.9,
        "n": 155,
        "n_basis": "155 infused NHL patients; batch numbers available for 383 of 410",
        "unit": "% viable T cells in the final product",
        "source": PASQUINI + ", Results",
        "url": PASQUINI_URL,
        "file": "data/references/pasquini_2020_rwe.txt",
        "quote": _PASQUINI_VIABILITY_QUOTE,
        "population": "US registry (CIBMTR) real-world tisagenlecleucel, NHL (DLBCL/FL)",
    },
    "pasquini2020_accept_to_infuse_days": {
        "median": 32.0,
        "low": 21.0,
        "high": 130.0,
        "n": 383,
        "n_basis": "383 analysis-set patients with an identifiable batch number",
        "unit": "days from leukapheresis acceptance at the facility to infusion",
        "source": PASQUINI + ", Results, final product attributes",
        "url": PASQUINI_URL,
        "file": "data/references/pasquini_2020_rwe.txt",
        "quote": "Median time from leukapheresis acceptance to infusion was 32 days "
        "(range, 21–130 days).",
        "population": "US registry (CIBMTR) real-world tisagenlecleucel, both indications",
    },
    # -- Label (FDA prescribing information) administered doses --
    "pi_juliet_dose_cells": {
        "median": 3.5e8,
        "low": 1.0e8,
        "high": 5.2e8,
        "n": 115,
        "n_basis": "115 adults with r/r DLBCL dosed (PI section 6.1); the median-dose "
        "sentence is in the DLBCL clinical-study description",
        "unit": "CAR-positive viable T cells administered (total)",
        "source": PI + ", Clinical Studies - DLBCL",
        "url": PI_URL,
        "file": "data/references/fda_pi_kymriah_current.txt",
        "quote": "The median dose was 3.5 × 108 CAR-positive viable T cells "
        "(range, 1.0 to 5.2 × 108 cells).",
        "population": "JULIET r/r DLBCL, commercial product, administered dose",
    },
    "pi_elara_dose_cells": {
        "median": 2.06e8,
        "low": 0.1e8,
        "high": 6.0e8,
        "n": 97,
        "n_basis": "97 adults with r/r follicular lymphoma dosed (PI section 6.1)",
        "unit": "CAR-positive viable T cells administered (total)",
        "source": PI + ", Clinical Studies - FL",
        "url": PI_URL,
        "file": "data/references/fda_pi_kymriah_current.txt",
        "quote": "The median dose administered was 2.06 × 108 CAR-positive \nviable "
        "T-cells (range, 0.1 to 6.0 × 108 CAR-positive viable T cells).",
        "population": "ELARA r/r follicular lymphoma, commercial product, administered dose",
    },
    # -- Academic (CTL019-process) transduction efficiency --
    "us20050113564_te_bbzeta_pct": {
        "median": 65.0,
        "low": 31.0,
        "high": 86.0,
        "n": 75,
        "n_basis": "75 retroviral transduction experiments of activated human T cells "
        "(the same experiments report 31%-86% GFP+ mononuclear cells, median 64%)",
        "unit": "% transduced cells (anti-CD19-BB-zeta, academic retroviral process)",
        "source": "US 2005/0113564 A1, Example 9 (anti-CD19 4-1BB CD3-zeta CAR)",
        "url": PATENT_URL,
        "file": "data/references/us20050113564a1_gp_text.txt",
        "quote": "median transduction efficiency was 65% (range, 31% to 86%) for "
        "anti-CD19-BB-\u03b6 receptors",
        "population": "academic-process transductions, not commercial final product",
        "note": "Academic-process transduction efficiency. Not comparable with the "
        "commercial final-product CAR-positive fraction (fong2023_car_fraction, "
        "median 12%); the two profiles are never merged.",
    },
    # -- Out-of-specification tail (Kato 2025, Japan, NCT04094311) --
    "kato2025_oos_dose_cells": {
        "median": 1.7e8,
        "low": 0.2e8,
        "high": 4.3e8,
        "n": 23,
        "n_basis": "23 r/r DLBCL patients infused with out-of-specification product",
        "unit": "CAR-positive viable T cells in the final product (total)",
        "source": KATO + ", Results",
        "url": KATO_URL,
        "file": "data/references/kato_2025_cytotherapy_oos_japan.md",
        "quote": "The median final product cell dose and the median cell viability "
        "were 1.7 × 108 CAR+ viable [T cells](https://www.sciencedirect.com/topics/"
        "medicine-and-dentistry/t-cell) (range, 0.2–4.3 × 108) and 68.9%, respectively.",
        "population": "r/r DLBCL, out-of-specification-conditioned product",
    },
}

#: Patient-level final-product attributes published in Kato 2025 Table 2
#: (r/r DLBCL infused with out-of-specification product):
#: ``(patient label, viability %, dose in 1e8 CAR+ viable T cells, OOS reason)``.
#: The transcription reproduces the paper's own summary (n=23, viability median
#: 68.9% exactly; dose median 1.661e8, reported as 1.7e8), which the tests
#: assert. Japan's viability criterion
#: was 70%, so this cohort is a conditioned tail, not a typical released lot.
KATO2025_OOS_DLBCL = (
    ("A", 69.9, 3.385, "low viability"),
    ("B", 69.2, 2.685, "low viability"),
    ("C", 68.9, 2.343, "low viability"),
    ("D", 68.5, 2.413, "low viability"),
    ("E", 68.4, 1.632, "low viability"),
    ("F", 68.3, 1.661, "low viability"),
    ("G", 66.4, 1.707, "low viability"),
    ("H", 64.8, 2.200, "low viability"),
    ("I", 63.4, 1.256, "low viability"),
    ("J", 62.4, 3.200, "low viability"),
    ("K", 60.9, 1.400, "low viability"),
    ("L", 60.2, 2.300, "low viability"),
    ("M", 86.8, 0.404, "low dose"),
    ("N", 88.0, 0.300, "low dose"),
    ("O", 77.7, 0.300, "low dose"),
    ("P", 85.7, 0.200, "low dose"),
    ("Q", 87.8, 0.167, "low dose"),
    ("R", 64.2, 0.527, "low viability + low dose"),
    ("S", 85.1, 0.484, "low dose + low CAR expression + low transduction efficiency"),
    ("T", 57.7, 0.266, "low viability + low dose + low release of IFN-gamma"),
    ("U", 80.8, 4.279, "high transduction efficiency"),
    ("V", 93.2, 3.613, "others"),
    ("W", 85.0, 2.219, "others"),
)

#: Summary statistics the KATO2025_OOS_DLBCL transcription must reproduce.
KATO2025_PUBLISHED_SUMMARY = {"n": 23, "viability_pct_median": 68.9, "dose_cells_median": 1.7e8}

#: Lot-attribute profiles. Each field maps a simulator lot input to a published
#: attribute key, to ``("empirical_pair", table)`` for a uniform resample of
#: published patients, or is absent - meaning no public value exists for that
#: population, so the caller keeps its scenario default and must report it as an
#: assumption (``unpublished_fields`` names them). ``derived_fields`` names inputs
#: that are instead inverted from published attributes by :func:`implied_net_yield`.
LOT_PROFILES = {
    "commercial_ball_2023": {
        "description": "Post-approval commercial B-ALL batches (Fong 2023, patients age <3 y).",
        "indication": "B-ALL",
        "fields": {
            "te": "fong2023_car_fraction",
            "viability": "fong2023_viability_pct",
            "starting_t_cells": "fong2023_leukapheresis_cd3_cells",
            "weight_kg": "fong2023_weight_kg",
            "dose_per_kg": "fong2023_dose_per_kg",
        },
        "derived_fields": ("net_yield",),
        "unpublished_fields": ("vcn",),
        "population_caveat": "patients younger than 3 years (median 1.2 y, 10.4 kg); the "
        "strongest commercial final-product evidence available, not an adult population",
    },
    "commercial_dlbcl_2020": {
        "description": "Real-world US NHL viability plus JULIET label administered dose.",
        "indication": "DLBCL",
        "fields": {
            "viability": "pasquini2020_viability_nhl_pct",
            "dose_cells": "pi_juliet_dose_cells",
        },
        "borrowed_fields": {"te": "fong2023_car_fraction"},
        "unpublished_fields": ("net_yield", "vcn", "starting_t_cells"),
        "population_caveat": "viability is real-world NHL product, dose is the JULIET label "
        "population, and final-product CAR positivity is borrowed from the pediatric "
        "commercial cohort because no adult commercial CAR-positive distribution is "
        "published in the retained corpus",
    },
    "oos_tail_2025": {
        "description": "Out-of-specification Japanese DLBCL products (Kato 2025, empirical).",
        "indication": "DLBCL",
        "fields": {"empirical_pair": KATO2025_OOS_DLBCL},
        "unpublished_fields": ("te", "net_yield", "vcn", "starting_t_cells"),
        "population_caveat": "conditioned on being out of specification (the Japanese "
        "viability criterion was 70%); use for failure scenarios, not for a typical lot",
    },
    "academic_2005": {
        "description": "Academic CTL019-process transduction efficiency (US 2005/0113564 A1).",
        "indication": None,
        "fields": {"te": "us20050113564_te_bbzeta_pct"},
        "unpublished_fields": ("viability", "dose_cells", "net_yield", "vcn"),
        "population_caveat": "retroviral transductions of activated T cells from healthy "
        "donors, not a commercial final product",
    },
}


def profile_names():
    """Names accepted by :func:`published_lot`."""
    return sorted(LOT_PROFILES)


def published_lot(rng, profile, *, indication=None, weight_kg=None):
    """Draw one lot's product attributes from the published distributions.

    ``rng`` may be a ``random.Random`` or an int seed. Returns the sampled values
    (``te`` and ``viability`` as fractions, cells and kilograms as published),
    plus ``provenance`` (field to source attribute key) and ``assumptions``
    (everything that is not a published fact). Fields with no public value for
    that population are absent from the result so the caller keeps, and reports,
    its scenario default.
    """
    if not isinstance(rng, random.Random):
        rng = random.Random(rng)
    try:
        spec = LOT_PROFILES[profile]
    except KeyError:
        raise ValueError(
            f"Unknown lot profile: {profile}; choose from " + ", ".join(profile_names())
        ) from None
    wanted = spec["indication"]
    if wanted and indication and indication != wanted:
        raise ValueError(f"lot profile {profile} describes {wanted} product, got {indication}")
    fields = spec["fields"]
    out, provenance = {}, {}
    assumptions = [
        "log-normal family and range-to-sigma rule are modelling conventions, not published facts",
        f"population: {spec['population_caveat']}",
    ]
    if "empirical_pair" in fields:
        table = fields["empirical_pair"]
        _, viability_pct, dose_e8, reason = table[rng.randrange(len(table))]
        out["viability"] = viability_pct / 100.0
        out["dose_cells"] = dose_e8 * 1e8
        out["oos_reason"] = reason
        provenance["viability"] = "kato2025_oos_dlbcl_table2"
        provenance["dose_cells"] = "kato2025_oos_dlbcl_table2"
        assumptions.append("empirical uniform resample of 23 published patients (no family)")
    for name in ("te", "viability", "starting_t_cells", "weight_kg"):
        key = fields.get(name)
        if key is None or (name == "viability" and "viability" in out):
            continue
        value = publication_stats.sample(rng, key)
        out[name] = value / 100.0 if key.endswith("_pct") else value
        provenance[name] = key
    if "dose_per_kg" in fields:
        per_kg = publication_stats.sample(rng, fields["dose_per_kg"])
        out["dose_per_kg"] = per_kg
        provenance["dose_per_kg"] = fields["dose_per_kg"]
        weight = weight_kg if weight_kg is not None else out.get("weight_kg")
        if weight is None:
            raise ValueError(f"lot profile {profile} needs weight_kg or a published weight field")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError(f"weight_kg must be positive, got {weight!r}")
        out["dose_cells"] = per_kg * weight
        provenance["dose_cells"] = fields["dose_per_kg"] + " x weight_kg"
        if weight_kg is not None:
            assumptions.append(f"weight {weight:g} kg is a scenario weight, not a published draw")
    elif "dose_cells" in fields and "dose_cells" not in out:
        out["dose_cells"] = publication_stats.sample(rng, fields["dose_cells"])
        provenance["dose_cells"] = fields["dose_cells"]
    for name, key in spec.get("borrowed_fields", {}).items():
        out[name] = publication_stats.sample(rng, key)
        provenance[name] = key
        assumptions.append(f"{name} borrowed from {key} (different population)")
    for name in spec.get("derived_fields", ()):
        if name == "net_yield":
            assumptions.append(
                "net_yield inverted from published dose, viability, CAR-positive fraction and "
                "leukapheresis input by implied_net_yield(); a consistency inversion, not a "
                "measured unit-operation recovery"
            )
    for name in spec["unpublished_fields"]:
        if name not in out:
            assumptions.append(f"{name} unpublished for this population; scenario default retained")
    return {**out, "profile": profile, "provenance": provenance, "assumptions": assumptions}


def implied_net_yield(starting_t_cells, dose_car_cells, viability, te):
    """Overall product recovery implied by the published attributes.

    ``dose_car_cells = starting_t_cells * net_yield * viability * te`` is the
    manufacturing chain in :mod:`simulator.cart_sim.manufacturing`, so a
    published dose, viability and CAR-positive fraction imply the recovery the
    process must have reached. Returns ``(implied_yield, total_product_cells)``.

    This is a derived consistency diagnostic on the illustrative ``net_yield``
    default, not a measured yield: the manufacturer's unit-operation
    recoveries are ``(b)(4)`` redactions.
    """
    for name, value in (
        ("starting_t_cells", starting_t_cells),
        ("dose_car_cells", dose_car_cells),
        ("viability", viability),
        ("te", te),
    ):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{name} must be positive to imply a yield")
    total_cells = dose_car_cells / (viability * te)
    return total_cells / starting_t_cells, total_cells


def published_medians(profile):
    """Published median of each field of a profile, for the report's comparison table."""
    spec = LOT_PROFILES[profile]
    out = {}
    for name, key in spec["fields"].items():
        if name == "empirical_pair":
            out["viability"] = KATO2025_PUBLISHED_SUMMARY["viability_pct_median"] / 100.0
            out["dose_cells"] = KATO2025_PUBLISHED_SUMMARY["dose_cells_median"]
        elif name in ("dose_per_kg", "dose_cells"):
            out[name] = publication_stats.STATS[key]["median"]
        elif name == "weight_kg":
            out["weight_kg"] = publication_stats.STATS[key]["median"]
        else:
            median = publication_stats.STATS[key]["median"]
            out[name] = median / 100.0 if key.endswith("_pct") else median
    for name, key in spec.get("borrowed_fields", {}).items():
        out[name] = publication_stats.STATS[key]["median"]
    return out


# One evidence set: the published lot attributes live with the rest of the
# published statistics, so reports and tests see a single dictionary.
publication_stats.STATS.update(ATTRIBUTES)

__all__ = [
    "ATTRIBUTES",
    "KATO2025_OOS_DLBCL",
    "KATO2025_PUBLISHED_SUMMARY",
    "LOT_PROFILES",
    "implied_net_yield",
    "profile_names",
    "published_lot",
    "published_medians",
]
