"""COHORT - maps viable CAR-positive lot counts to infused dose, samples patients,
aggregates ORR / CR / relapse / persistence / CRS / ICANS."""

import math
import random
from statistics import median

from .construct import CD19_TUMOR_ALL, CD19_TUMOR_DLBCL
from .lot_criteria import dose_interval
from .manufacturing import manufacture
from .micro_engine import run_patient_micro
from .ode_engine import run_patient
from .params import default_params


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
    """
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if indication not in ("DLBCL", "B-ALL"):
        raise ValueError("indication must be DLBCL or B-ALL")
    if engine not in ("micro", "ode"):
        raise ValueError("engine must be micro or ode")
    if agloss_mode not in ("natural", "heavy", "none"):
        raise ValueError("agloss_mode must be natural, heavy, or none")
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
        te = min(0.92, max(0.05, rng.gauss(0.55, 0.18)))
        net_yield = math.exp(rng.gauss(math.log(0.05), 0.4))
        target = 2e8 if indication == "DLBCL" else (1e6 * weight_kg if weight_kg <= 50 else 1e8)
        # Illustrative scenario assumption: sterility and mycoplasma cultures
        # came back negative, as they do for the overwhelming majority of
        # released lots (Rossoff 2021 reports no microbial OOS reasons).
        # Override with lot_params {"sterility": False} etc. for a positive.
        inputs = {
            "te": te,
            "net_yield": net_yield,
            "dose_target": target,
            "sterility": True,
            "mycoplasma": True,
        }
        inputs.update(lot_params)
        man = manufacture(**inputs, indication=indication, weight_kg=weight_kg)
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
