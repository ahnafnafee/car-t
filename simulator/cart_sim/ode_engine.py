"""Eight-state RK4 population model: E, M, Ton, Toff, B, IFN, IL6, TNF.

Rate constants and outcome thresholds are phenomenological assumptions.
See docs/EVIDENCE.md for source correspondence and numerical limitations.
"""

import math
import random

from .construct import binder_engagement
from .outcomes import summarize
from .params import default_params
from .validation import validate_params


def _derivs(y, p, rng=None):
    E, M, Ton, Toff, B, IFN, IL6, TNF = y
    E = max(E, 0.0)
    M = max(M, 0.0)
    Ton = max(Ton, 0.0)
    Toff = max(Toff, 0.0)
    B = max(B, 0.0)

    eng_T = binder_engagement(p["cd19_tumor"], p["Kd_app"])
    eng_B = binder_engagement(p["cd19_B"], p["Kd_app"])
    eng_neg = p["eng_neg"]
    costim = 1.0 + p["f41"]
    fMem_eff = p["fMem_base"] * (1.0 + 2.0 * p["f41"]) * p["fMem_fit"]
    # weak products lose memory faster; 4-1BB costimulation is the memory-persistence
    # signal; the survival penalty is >= 1 before costimulation scaling.
    surv = 1.0 + max(0.0, 1.0 - p["fMem_fit"]) * 4.5
    dMem_eff = p["dMem_base"] * surv * (1.0 + p["f41"]) / (1.0 + 2.0 * p["f41"])
    kmf = p["kill_mem_frac"] * (1.0 + p["f41"])
    Ekill = E + kmf * M
    amp = p["cyto_amp"]
    A = Ton + 0.05 * Toff + B  # antigen-positive stimulation mass
    stim = A / (A + p["Ks_E"]) if A > 0 else 0.0

    # effector CAR-T: antigen-driven proliferation, death, contraction, -> memory.
    # Costimulation supports basal effector survival, and chronic antigen stimulation
    # without any costimulation drives activation-induced cell death (two-signal
    # paradigm): the historical 1st-gen failure mode. csurv lets a CD28-style arm
    # keep survival signaling while losing 4-1BB-style memory persistence.
    csurv = p["f41"] + p.get("cs28", 0.0)
    dE0_eff = p["dE0"] / (1.0 + csurv)
    aicd = 0.25 / (1.0 + 2.0 * csurv)
    rE = p["pE"] * stim * costim - dE0_eff - p["sE"] * E / p["Emax"] - aicd * stim
    dE = rE * E - fMem_eff * E
    dM = fMem_eff * E - dMem_eff * M

    # CD19+ tumor: slow-seed regrowth (logistic-in-niche) - CAR-T kill
    grow_on = p["rT"] * (Ton / (Ton + p["T_niche"])) * Ton
    kill_on = (
        Ekill
        * eng_T
        * costim
        * (p["kKill0"] * Ton / (Ton + p["Kd_T"]) + (p["kKill_fixed"] if Ton > 0 else 0.0))
    )
    dTon = grow_on - kill_on

    # antigen-loss clone: slow-growing, killed only at residual (bystander) efficiency
    grow_off = p["rT_off"] * (Toff / (Toff + p["T_niche"])) * Toff
    kill_off = (
        Ekill
        * eng_neg
        * costim
        * (
            p["kKill0"] * Toff / (Toff + p["Kd_T"])
            + (p["kKill_fixed"] * eng_neg if Toff > 0 else 0.0)
        )
    )
    dToff = grow_off - kill_off

    # normal B cells: marrow homeostasis (logistic) - on-target/off-tumor kill
    kill_B = (
        Ekill
        * eng_B
        * costim
        * p["kKillB_frac"]
        * (p["kKill0"] * B / (B + p["Kd_B"]) + (p["kKill_fixed"] if B > 0 else 0.0))
    )
    dB = p["rB"] * B * (1.0 - B / p["Bmax"]) - kill_B

    # cytokines (pg/mL)
    dIFN = amp * p["cIFN"] * E * stim - p["clIFN"] * IFN
    dIL6 = amp * (p["cIL6_anti"] * kill_on + p["cIL6_bg"] * E * stim) - p["clIL6"] * IL6
    dTNF = amp * p["cTNF"] * E * stim - p["clTNF"] * TNF

    if rng is not None and p.get("sigma", 0.0) > 0:
        s = p["sigma"]
        dE *= 1 + rng.gauss(0, s)
        dTon *= 1 + rng.gauss(0, s)
    return [dE, dM, dTon, dToff, dB, dIFN, dIL6, dTNF]


def run_patient(p=None, seed=None):
    """Integrate one patient. Returns time series + summary metrics."""
    params = dict(default_params())
    if p:
        params.update(p)
    rng = random.Random(seed) if seed is not None else None
    validate_params(params, params["dt"])
    f_ag = params["f_agloss"]
    Ton0 = params["T0"] * (1.0 - f_ag)
    Toff0 = params["T0"] * f_ag
    y = [
        params["E0"],
        0.0,
        Ton0,
        Toff0,
        params["B0"],
        params["IFN0"],
        params["IL60"],
        params["TNF0"],
    ]
    dt = params["dt"]
    nsteps = math.ceil(params["t_end"] / dt)
    keys = ["E", "M", "Ton", "Toff", "B", "IFN", "IL6", "TNF"]
    t = [0.0]
    series = {k: [v] for k, v in zip(keys, y)}
    lysis_peak = 0.0

    for i in range(1, nsteps + 1):
        dt = min(params["dt"], params["t_end"] - t[-1])
        k1 = _derivs(y, params, rng)
        y2 = [y[j] + 0.5 * dt * k1[j] for j in range(8)]
        k2 = _derivs(y2, params, rng)
        y3 = [y[j] + 0.5 * dt * k2[j] for j in range(8)]
        k3 = _derivs(y3, params, rng)
        y4 = [y[j] + dt * k3[j] for j in range(8)]
        k4 = _derivs(y4, params, rng)
        y = [max(y[j] + dt / 6.0 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]), 0.0) for j in range(8)]
        lysis_peak = max(
            lysis_peak,
            (y[0] + p_kill_memfrac(params) * y[1])
            * binder_engagement(params["cd19_tumor"], params["Kd_app"])
            * (1 + params["f41"])
            * (
                params["kKill0"] * y[2] / (y[2] + params["Kd_T"])
                + (params["kKill_fixed"] if y[2] > 0 else 0.0)
            ),
        )
        t.append(min(i * params["dt"], params["t_end"]))
        for j, k in enumerate(keys):
            series[k].append(y[j])

    series["T"] = [a + b for a, b in zip(series["Ton"], series["Toff"])]
    return {
        "params": params,
        "engine": "ode",
        "dt": params["dt"],
        "t": t,
        **series,
        **summarize(t, series, params, lysis_peak, seed),
        "f_agloss": f_ag,
        "eng_T": binder_engagement(params["cd19_tumor"], params["Kd_app"]),
        "eng_B": binder_engagement(params["cd19_B"], params["Kd_app"]),
    }


def p_kill_memfrac(p):
    return p["kill_mem_frac"] * (1.0 + p["f41"])
