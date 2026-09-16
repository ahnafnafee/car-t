"""Exploratory model ranges and distinct, endpoint-specific trial observations.

BANDS are author-selected calibration ranges, not published confidence intervals.
No model endpoint is a 1:1 implementation of trial response or toxicity grading.
"""

TRIALS = [
    (
        "JULIET",
        "DLBCL",
        "tisagenlecleucel",
        93,
        "Best overall response / complete response",
        "52% / 40%",
        "https://doi.org/10.1056/NEJMoa1804980",
    ),
    (
        "ELIANA",
        "B-ALL",
        "tisagenlecleucel",
        75,
        "Remission within 3 months (CR + CRi)",
        "81%",
        "https://doi.org/10.1056/NEJMoa1709866",
    ),
    (
        "ZUMA-1",
        "Large B-cell lymphoma",
        "axicabtagene ciloleucel",
        101,
        "Objective response / complete response",
        "82% / 54%",
        "https://doi.org/10.1056/NEJMoa1707447",
    ),
]

KINETICS = [
    (
        "ELIANA",
        "CR/CRi at day 28",
        61,
        "Blood qPCR transgene",
        9.91,
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7433345/",
    ),
    (
        "ELIANA",
        "NR at day 28",
        7,
        "Blood qPCR transgene",
        20.0,
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7433345/",
    ),
    (
        "JULIET",
        "CR/PR at month 3",
        34,
        "Blood flow CAR+ fraction of CD3+ cells",
        6.35,
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7013261/",
    ),
    (
        "JULIET",
        "SD/PD/unknown at month 3",
        50,
        "Blood flow CAR+ fraction of CD3+ cells",
        7.64,
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC7013261/",
    ),
]

_RANGE_NOTE = "Model assumption; see docs/EVIDENCE.md for endpoint differences"


def _band(label, key, lo, hi, factor=1):
    return label, lambda c: factor * c[key], lo, hi, _RANGE_NOTE


BANDS = {
    "DLBCL": [
        _band("Response proxy (%)", "ORR", 50, 83, 100),
        _band("Deep response proxy (%)", "CR_rate", 40, 58, 100),
        _band("Relapse proxy by d120 (%)", "relapse_rate", 5, 30, 100),
        _band("Memory threshold at d120 (%)", "persistent_rate", 60, 90, 100),
        _band("B-cell threshold at d90 (%)", "B_aplasia_pct", 60, 85),
        _band("CRS proxy >=1 (%)", "CRS_any_pct", 58, 100),
        _band("CRS proxy >=2 (%)", "CRS_g2pct", 30, 75),
        _band("CRS proxy >=3 (%)", "CRS_g3pct", 10, 25),
        _band("ICANS proxy >=2 (%)", "ICANS_g2pct", 21, 64),
        _band("ICANS proxy >=3 (%)", "ICANS_g3pct", 3, 30),
        _band("Effector peak day (median)", "E_peak_day_median", 7, 16),
    ],
    "B-ALL": [
        _band("Response proxy (%)", "ORR", 60, 85, 100),
        _band("Deep response proxy (%)", "CR_rate", 40, 80, 100),
        _band("Relapse proxy by d120 (%)", "relapse_rate", 5, 30, 100),
        _band("CRS proxy >=1 (%)", "CRS_any_pct", 58, 100),
        _band("CRS proxy >=3 (%)", "CRS_g3pct", 20, 48),
        _band("ICANS proxy >=3 (%)", "ICANS_g3pct", 5, 30),
        _band("B-cell threshold at d90 (%)", "B_aplasia_pct", 60, 90),
    ],
}

# Ablation arms: name, cohort base-params, agloss_mode
ARMS = [
    ("base (4-1BB, natural)", {}, None),
    ("1st-gen (CD3z only)", {"f41": 0.0}, "natural"),
    (
        "CD28-costim proxy",
        {
            "f41": 0.0,
            "cs28": 0.22,
            "pE": 0.70 * 1.35,
            "fMem_base": 0.03 * 0.45,
            "dMem_base": 0.03 * 2.5,
        },
        "natural",
    ),
    ("antigen-loss heavy", {}, "heavy"),
    ("low dose (0.1x)", {"dose_scale": 0.1}, "natural"),
    ("no lymphodepletion", {"Emax": 3.0e9 * 0.25, "sE": 1.6}, "natural"),
]


def band_table(cohort, indication):
    """Return numerical range checks; IN RANGE does not mean validation."""
    return [
        (label, fn(cohort), lo, hi, source, lo <= fn(cohort) <= hi)
        for label, fn, lo, hi, source in BANDS[indication]
    ]
