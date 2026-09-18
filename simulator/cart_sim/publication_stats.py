"""Published product and kinetics statistics with per-statistic provenance.

Each entry is transcribed verbatim from a retained source file (see
data/references/README.md for hashes). These are the only public per-patient
product statistics recovered for commercial tisagenlecleucel; they anchor the
optional ``product_stats`` cohort mode and the report's anchor comparison
table. Median/range summaries are calibrated to a two-sided log-normal via the
``calibrate`` helper, with the range-to-sigma conversion documented there.
No entry here is a simulation output, and anchoring does not validate the model.
"""

import math

# Retrieval dates: ELIANA 2018 text retained 2026-09-16 (PMC5996391);
# Tyagarajan 2020 XML retained 2026-09-16 (PMC6970133).
STATS = {
    "eliana2018_dose_per_kg": {
        "median": 3.1e6,
        "low": 0.2e6,
        "high": 5.4e6,
        "n": 75,
        "unit": "transduced viable T cells/kg body weight (infused)",
        "source": "Maude et al., NEJM 2018;378:1029-1042 (ELIANA), Results, Infused product",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5996391/",
        "file": "data/references/maude_2018_eliana.txt",
        "quote": "median weight-adjusted dose of 3.1×106 transduced viable T cells "
        "per kilogram of body weight (range, 0.2×106 to 5.4×106 cells per kilogram)",
        "population": "pediatric/young-adult B-ALL, commercial product",
    },
    "eliana2018_total_dose": {
        "median": 1.0e8,
        "low": 0.03e8,
        "high": 2.6e8,
        "n": 75,
        "unit": "transduced viable T cells (infused, total)",
        "source": "Maude et al., NEJM 2018 (ELIANA), Results, Infused product",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5996391/",
        "file": "data/references/maude_2018_eliana.txt",
        "quote": "the median total dose of transduced viable T cells was 1.0×108 "
        "(range, 0.03×108 to 2.6×108 cells)",
        "population": "pediatric/young-adult B-ALL, commercial product",
    },
    "eliana2018_screen_to_infuse_days": {
        "median": 45.0,
        "low": 30.0,
        "high": 105.0,
        "n": 75,
        "unit": "days from enrollment to infusion",
        "source": "Maude et al., NEJM 2018 (ELIANA), Results",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5996391/",
        "file": "data/references/maude_2018_eliana.txt",
        "quote": "median time from enrollment to infusion of 45 days (range, 30 to 105)",
        "population": "enrolled B-ALL patients infused",
    },
    "eliana2018_tmax_responders_days": {
        "median": 10.0,
        "low": 5.7,
        "high": 28.0,
        "n": 60,
        "unit": "days from infusion to maximum blood transgene (qPCR)",
        "source": "Maude et al., NEJM 2018 (ELIANA), Results, cellular kinetics",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5996391/",
        "file": "data/references/maude_2018_eliana.txt",
        "quote": "the median time to maximum expansion (Tmax) was 10 days "
        "(range, 5.7 to 28)",
        "population": "responders evaluable for kinetics (CR/CRi at day 28)",
    },
    "eliana2018_persistence_days": {
        "median": 168.0,
        "low": 20.0,
        "high": 617.0,
        "n": 60,
        "unit": "days of detectable blood transgene (qPCR)",
        "source": "Maude et al., NEJM 2018 (ELIANA), Results, cellular kinetics",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5996391/",
        "file": "data/references/maude_2018_eliana.txt",
        "quote": "median duration of persistence of tisagenlecleucel in blood was "
        "168 days (range, 20 to 617 days; 60 patients) at data cutoff",
        "population": "responders evaluable for kinetics",
    },
    "tyagarajan2020_cycle_days": {
        "median": 23.0,
        "low": 21.0,
        "high": 37.0,
        "n": 37,
        "unit": "days from leukapheresis receipt at facility to product return (incl. shipping)",
        "source": "Tyagarajan et al., Mol Ther Methods Dev 2020;17:632-642, Results",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6970133/",
        "file": "data/references/tyagarajan_2020_mtmcd.xml",
        # The retained JATS XML uses non-breaking spaces (U+00A0) around number
        # units; the quote keeps them so it matches the file byte-exactly.
        "quote": "median throughput time of 23\u00a0days (range, 21–37\u00a0days) "
        "from receipt of the leukapheresed material at the manufacturing facility "
        "to return of tisagenlecleucel to the clinical site",
        "population": "first 37 commercial US B-ALL patients, 13 sites, cutoff 2018-01-30",
    },
}


def _z_max(n):
    """Blom-formula expected largest standard-normal order statistic for a sample of n."""
    return _inv_normal((n - 0.375) / (n + 0.25))


def _inv_normal(p):
    # Acklam's inverse-normal approximation (abs error < 1.15e-9); no runtime deps.
    a = (-3.969683028665376e01, 2.209460984245205e02, -2.759285104469687e02,
         1.383577518672690e02, -3.066479806614716e01, 2.506628277459239e00)
    b = (-5.447609879822406e01, 1.615858368580409e02, -1.556989798598866e02,
         6.680131188771972e01, -1.328068155288572e01)
    c = (-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e00,
         -2.549732539343734e00, 4.374664141464968e00, 2.938163982698783e00)
    d = (7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e00,
         3.754408661907416e00)
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    if p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = p - 0.5
    r = q * q
    return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / (
        (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1))


def calibrate(key):
    """Two-sided log-normal parameters (median, sigma_down, sigma_up) for a published
    median/range entry.

    The published range is treated as the expected sample maximum/minimum for n
    observations of a log-normal, giving sigma_up = ln(high/median)/z(n) and
    sigma_down = ln(median/low)/z(n) with z the Blom expected max. This is a
    documented calibration convention, not a claim about the true distribution;
    it reproduces the published median and (in expectation) the published range.
    """
    s = STATS[key]
    z = _z_max(s["n"])
    median = math.log(s["median"])
    sigma_up = (math.log(s["high"]) - median) / z
    sigma_down = (median - math.log(s["low"])) / z
    return math.exp(median), sigma_down, sigma_up, z


def sample(rng, key):
    """Draw one value from the calibrated two-sided log-normal for a published stat."""
    median, sigma_down, sigma_up, _ = calibrate(key)
    z = rng.gauss(0.0, 1.0)
    return median * math.exp((sigma_up if z >= 0 else sigma_down) * z)
