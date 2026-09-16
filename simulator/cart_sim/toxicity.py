"""Toxicity grading proxies: CRS (IL-6-driven) and ICANS (probabilistic CRS complication)."""

import random

# Model-specific IL-6 thresholds, not ASTCT grading criteria.
# ASTCT uses clinical findings; see docs/EVIDENCE.md.
CRS_IL6_CUTS = (12.0, 170.0, 500.0, 3000.0)


def crs_grade(IL6_peak, IFN_peak, TNF_peak, lysis_peak):
    """Synthetic severity category based only on peak IL-6."""
    if IL6_peak < CRS_IL6_CUTS[0]:
        return 0
    if IL6_peak < CRS_IL6_CUTS[1]:
        return 1
    if IL6_peak < CRS_IL6_CUTS[2]:
        return 2
    if IL6_peak < CRS_IL6_CUTS[3]:
        return 3
    return 4


# P(ICANS | CRS grade) - neurotoxicity tracks CRS severity but affects a subset
ICANS_P_BY_CRS = {0: 0.01, 1: 0.06, 2: 0.28, 3: 0.55, 4: 0.75}


def icans_grade(crs, seed):
    """ICANS proxy: probabilistic complication of CRS (grade tracks CRS severity)."""
    r = random.Random(f"icans-{seed}").random()
    p = ICANS_P_BY_CRS[crs]
    if r >= p:
        return 0
    if crs >= 3 and r < p * 0.55:
        return 3
    return 2
