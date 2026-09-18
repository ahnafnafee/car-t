"""COHORT - maps viable CAR-positive lot counts to infused dose, samples patients,
aggregates ORR / CR / relapse / persistence / CRS / ICANS."""

import math
import random
from statistics import median

from .construct import CD19_TUMOR_ALL, CD19_TUMOR_DLBCL
from .lot_criteria import dose_interval
from .lot_distributions import (
    LOT_PROFILES,
    implied_net_yield,
    published_lot,
    published_medians,
)
from .manufacturing import manufacture
from .publication_stats import sample as published_sample
from .micro_engine import run_patient_micro
from .ode_engine import run_patient
from .params import default_params

# product_stats mode names -> published per-patient dose statistic to draw from.
PUBLISHED_DOSE_SOURCES = {"eliana_2018": "eliana2018_dose_per_kg"}


def run_cohort(
    base=None,
    n=120,
    seed=1001,
    indication="DLBCL",
    agloss_mode="natural",
    engine="micro",
    *,
    weight_kg=30.0,
    lot_params=None,
    product_stats=None,
    lot_stats=None,
):
    """Sample patients from parameter distributions; aggregate ORR / CR / relapse /
    persistence / B-aplasia / CRS / ICANS.

    Assumed patient variation represents the following model hypotheses:
      - manufacturing outcome (TE, net yield -> viable CAR+ dose)
      - product potency F (T-cell fitness -> expansion + memory formation)
      - tumor burden and CD19 density / antigen heterogeneity
      - antigen-loss clone presence (CD19-negative relapse / refractory disease)
      - antigen-dim subclone presence (micro layer; CD19-dim escape)
      - cytokine amplification (monocyte / IL-6 axis -> CRS severity)

    agloss_mode: "natural" = sampled per patient; "heavy" = enriched (ablation);
                 "none" = no seeded or newly generated dim/negative clones.
    engine: "micro" (default) = stochastic cell-event engine (run_patient_micro);
            "ode" = compartmental population model (run_patient).
    The cohort samples E0, T0, cd19_tumor, f_agloss, f_dimgloss and cyto_amp;
    direct overrides of these patient fields are not cohort distribution controls.
    Use run_patient() or run_patient_micro() for fixed patient parameters.
    Default B-ALL weight (30 kg) and target (1e6 viable CAR+ cells/kg at <=50 kg,
    otherwise 1e8 cells) are explicit scenarios, not fitted patient distributions.
    lot_params overrides manufacturing inputs; dose_scale is a subsequent model
    ablation and does not alter the source assessment of the manufactured lot.
    product_stats: None (default) = scenario dose target; "eliana_2018" = draw
    each patient's infused dose per kg from the published ELIANA dose
    distribution (publication_stats.py), requiring indication="B-ALL". The
    source assessment still applies to the resulting lot, so doses outside the
    disclosed label interval are reported as failing it, as observed clinically.
    lot_stats: None (default) = illustrative manufacturing inputs (TE, viability,
    leukapheresis input); otherwise a published product-attribute profile name
    from lot_distributions.LOT_PROFILES ("commercial_ball_2023",
    "commercial_dlbcl_2020", "oos_tail_2025", "academic_2005"), which replaces
    every attribute that cohort has published values for and reports the rest as
    retained scenario defaults. Each patient then carries lot_provenance, and the
    cohort reports implied_net_yield_median: the overall product recovery the
    published dose, viability and CAR-positive fraction imply from the published
    leukapheresis input (a derived diagnostic, not a measured yield). lot_params
    still override anything set here.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if indication not in ("DLBCL", "B-ALL"):
        raise ValueError("indication must be DLBCL or B-ALL")
    if engine not in ("micro", "ode"):
        raise ValueError("engine must be micro or ode")
    if agloss_mode not in ("natural", "heavy", "none"):
        raise ValueError("agloss_mode must be natural, heavy, or none")
    if product_stats is not None:
        if product_stats not in PUBLISHED_DOSE_SOURCES:
            raise ValueError(f"Unknown product_stats: {product_stats}")
        if indication != "B-ALL":
            raise ValueError("product_stats populations are B-ALL cohorts; pass indication='B-ALL'")
    if lot_stats is not None:
        if lot_stats not in LOT_PROFILES:
            raise ValueError(f"Unknown lot_stats: {lot_stats}; choose from " + ", ".join(sorted(LOT_PROFILES)))
        wanted = LOT_PROFILES[lot_stats]["indication"]
        if wanted and indication != wanted:
            raise ValueError(f"lot_stats={lot_stats} describes {wanted} product; pass indication='{wanted}'")
    dose_interval(indication, weight_kg)
    lot_params = dict(lot_params or {})
    allowed_lot_keys = {
        "apheresis_wbc",
        "t_cell_frac",
        "net_yield",
        "te",
        "vcn",
        "viability",
        "dose_target",
        "sterility",
        "mycoplasma",
        "appearance_ok",
    }
    if set(lot_params) - allowed_lot_keys:
        raise ValueError(
            "Unknown lot_params keys: " + ", ".join(sorted(set(lot_params) - allowed_lot_keys))
        )
    b = dict(default_params())
    if base:
        b.update(base)
    if b["t_end"] < 120:
        raise ValueError("cohort endpoints require t_end >= 120 days")
    if not math.isfinite(b.get("dose_scale", 1.0)) or b.get("dose_scale", 1.0) < 0:
        raise ValueError("dose_scale must be finite and nonnegative")
    rng = random.Random(seed)
    p_dimseed = 0.35 if indication != "DLBCL" else 0.25  # antigen-dim subclone prev.
    out = []
    lot_assumptions = []
    implied_yields = []
    dose_attainment = []
    for i in range(n):
        p = dict(b)
        if indication == "DLBCL":
            p["T0"] = math.exp(rng.gauss(math.log(1.0e10), 0.42))
            p["cd19_tumor"] = CD19_TUMOR_DLBCL
            amp_mu, F_mu, F_sd, agloss_p = 0.0, 0.0, 0.65, 0.34
        else:  # B-ALL
            p["T0"] = math.exp(rng.gauss(math.log(1.2e10), 0.5))
            p["cd19_tumor"] = CD19_TUMOR_ALL
            amp_mu = math.log(1.30)  # B-ALL: more frequent severe CRS (ELIANA)
            # Scenario hypothesis: higher/narrower fitness and less antigen loss;
            # these distributions are not fitted to the clinical source records.
            F_mu, F_sd, agloss_p = 0.15, 0.40, 0.25
        # ---- manufacturing chain -> infused dose ----
        lot = (
            published_lot(rng, lot_stats, indication=indication, weight_kg=weight_kg)
            if lot_stats
            else None
        )
        if lot is not None and i == 0:
            lot_assumptions = list(lot["assumptions"])
        published_weight = lot.pop("weight_kg", None) if lot else None
        te = (
            lot["te"]
            if lot and "te" in lot
            else min(0.92, max(0.05, rng.gauss(0.55, 0.18)))
        )
        net_yield = math.exp(rng.gauss(math.log(0.05), 0.4))
        target = 2e8 if indication == "DLBCL" else (1e6 * weight_kg if weight_kg <= 50 else 1e8)
        if lot is not None and "dose_cells" in lot:
            # Published administered/final-product dose replaces the scenario target.
            target = lot["dose_cells"]
        if product_stats is not None:
            # Published per-patient dose distribution (publication_stats.STATS)
            # replaces the scenario target; the scenario weight scales per-kg.
            target = published_sample(rng, PUBLISHED_DOSE_SOURCES[product_stats]) * weight_kg
        # Illustrative scenario assumption: sterility and mycoplasma cultures
        # came back negative and the product passed visual appearance, as they
        # do for the overwhelming majority of released lots (Rossoff 2021
        # reports no microbial OOS reasons).
        # Override with lot_params {"sterility": False} etc. for a positive.
        inputs = {
            "te": te,
            "net_yield": net_yield,
            "dose_target": target,
            "sterility": True,
            "mycoplasma": True,
            "appearance_ok": True,
        }
        implied_this = None
        if lot is not None:
            if "viability" in lot:
                inputs["viability"] = lot["viability"]
            if "starting_t_cells" in lot:
                # The published leukapheresis CD3+ count is the starting material
                # itself, so the illustrative WBC-to-T-cell fraction step is removed.
                inputs["apheresis_wbc"] = lot["starting_t_cells"]
                inputs["t_cell_frac"] = 1.0
        inputs.update(lot_params)
        if lot is not None and "starting_t_cells" in lot and "viability" in inputs:
            # Derived, never published: the minimum overall recovery the published
            # dose, viability and CAR-positive fraction imply from the published
            # leukapheresis input. Used instead of the illustrative net_yield
            # default so the simulated lot is consistent with the published product
            # attributes; the manufacturer's unit-operation recoveries are (b)(4)
            # redactions, so this is a consistency inversion, not a measured yield.
            implied_this, _total = implied_net_yield(
                inputs["apheresis_wbc"] * inputs.get("t_cell_frac", 1.0),
                inputs["dose_target"],
                inputs["viability"],
                inputs["te"],
            )
            implied_yields.append(implied_this)
            if "net_yield" not in lot_params:
                inputs["net_yield"] = implied_this
        man = manufacture(**inputs, indication=indication, weight_kg=weight_kg)
        attainment_this = None
        if implied_this is not None:
            # 1.0 when the derived recovery reaches the published dose; below 1.0
            # when lot_params forced a lower recovery than the published dose needs.
            attainment_this = man["dose_CARplus_cells"] / man["dose_target_viable_car_cells"]
            dose_attainment.append(attainment_this)
        # Latent fitness affects dynamics, not physical dose or manufacturing yield.
        F = math.exp(rng.gauss(F_mu, F_sd))
        p["E0"] = man["dose_viable_car_cells"] * b.get("dose_scale", 1.0)
        p["pE"] = max(0.15, b["pE"] * (0.4 + 0.6 * min(F, 2.0)))
        p["fMem_fit"] = b["fMem_fit"] * min(1.4, 0.15 + 0.75 * min(F, 1.5))
        # ---- antigen-loss clone ----
        if agloss_mode == "none":
            p["f_agloss"] = 0.0
        elif agloss_mode == "heavy":
            p["f_agloss"] = min(0.6, math.exp(rng.gauss(math.log(0.12), 0.8)))
        else:
            u = rng.random()
            p["f_agloss"] = (
                0.0 if u < (1.0 - agloss_p) else min(0.5, math.exp(rng.gauss(math.log(0.02), 1.1)))
            )
        # ---- CD19 density heterogeneity (lognormal, capped) ----
        p["cd19_tumor"] = min(2.0e6, max(3.0e4, p["cd19_tumor"] * math.exp(rng.gauss(0.0, 0.4))))
        p["cyto_amp"] = math.exp(rng.gauss(amp_mu, 0.80))
        p["sigma"] = b["sigma"]
        # ---- antigen-dim subclone (micro layer: dim escape, partial engagement) ----
        # Drawn in BOTH engines so that a given seed samples the identical patient
        # population regardless of engine (the ODE engine simply ignores the field).
        u_dim = rng.random()
        p["f_dimgloss"] = (
            0.0 if u_dim > p_dimseed else min(0.5, math.exp(rng.gauss(math.log(0.02), 0.9)))
        )
        p["f_dimgloss"] = min(p["f_dimgloss"], 1.0 - p["f_agloss"])
        if agloss_mode == "none":
            p.update(f_dimgloss=0.0, mu_hi_dim=0.0, mu_dim_null=0.0)
        patient_seed = f"{seed}:{i}"
        result = (
            run_patient_micro(p, seed=patient_seed)
            if engine == "micro"
            else run_patient(p, seed=patient_seed)
        )
        result["manufacturing"] = man
        if lot is not None:
            result["lot_profile"] = lot_stats
            result["lot_provenance"] = lot["provenance"]
            if published_weight is not None:
                result["published_weight_kg"] = published_weight
            if "oos_reason" in lot:
                result["oos_reason"] = lot["oos_reason"]
            if implied_this is not None:
                result["implied_net_yield"] = implied_this
            if "dose_cells" in lot and "dose_target" not in lot_params:
                result["infused_dose_per_kg"] = man["dose_viable_car_cells"] / weight_kg
                result["dose_source"] = "published " + lot["provenance"].get("dose_cells", lot_stats)
        if product_stats is not None and "dose_target" not in lot_params:
            result["infused_dose_per_kg"] = man["dose_viable_car_cells"] / weight_kg
            result["dose_source"] = "published " + PUBLISHED_DOSE_SOURCES[product_stats]
        out.append(result)
    n = len(out)
    nresp = sum(r["responds"] for r in out)
    ncr = sum(r["CR"] for r in out)
    nrel = sum(r["relapses"] for r in out)
    npers = sum(r["persistent"] for r in out)
    nB = sum(r["B_aplasia"] for r in out)
    crs_any = sum(r["CRS_grade"] >= 1 for r in out)
    crs_g2 = sum(r["CRS_grade"] >= 2 for r in out)
    crs_g3 = sum(r["CRS_grade"] >= 3 for r in out)
    crs_g4 = sum(r["CRS_grade"] >= 4 for r in out)
    icans_g2 = sum(r["ICANS_grade"] >= 2 for r in out)
    icans_g3 = sum(r["ICANS_grade"] >= 3 for r in out)
    il6 = sorted(r["IL6_peak"] for r in out)
    ret = {
        "indication": indication,
        "n": n,
        "weight_kg": weight_kg if indication == "B-ALL" else None,
        "product_stats": product_stats,
        "lot_stats": lot_stats,
        "lot_assumptions": lot_assumptions,
        "lot_published_medians": published_medians(lot_stats) if lot_stats else None,
        "implied_net_yield_median": median(implied_yields) if implied_yields else None,
        "published_dose_attainment_median": median(dose_attainment) if dose_attainment else None,
        "lot_assessment_counts": {
            status: sum(r["manufacturing"]["source_assessment"]["status"] == status for r in out)
            for status in ("meets_disclosed_criteria", "fails_disclosed_criteria", "incomplete")
        },
        "patients": out,
        "ORR": nresp / n,
        "CR_rate": ncr / n,
        "relapse_rate": nrel / n,
        "persistent_rate": npers / n,
        "B_aplasia_pct": 100 * nB / n,
        "CRS_any_pct": 100 * crs_any / n,
        "CRS_g2pct": 100 * crs_g2 / n,
        "CRS_g3pct": 100 * crs_g3 / n,
        "CRS_g4pct": 100 * crs_g4 / n,
        "ICANS_g2pct": 100 * icans_g2 / n,
        "ICANS_g3pct": 100 * icans_g3 / n,
        "IL6_peak_median": median(il6),
        "E_peak_median": median(r["E_peak"] for r in out),
        "E_peak_day_median": median(r["E_peak_day"] for r in out),
        "engine": engine,
    }
    if engine == "micro":

        def med(key):
            return median(r[key] for r in out)

        de_novo = sum(
            1
            for r in out
            if r["f_agloss"] < 1.0e-3 and (r["null_born"] > 50 or r["dim_born"] > 1.0e4)
        )
        ret.update(
            {
                "exhausted_peak_frac_median": med("exhausted_peak_frac"),
                "divisions_median": med("divisions"),
                "aicd_events_median": med("aicd_events"),
                "mem_transitions_median": med("mem_transitions"),
                "kill_events_median": med("kill_events"),
                "de_novo_escape_n": de_novo,
            }
        )
    return ret
