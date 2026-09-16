"""Hybrid stochastic population model with fitness bins and three tumor clones.

Poisson event counts use a Gaussian approximation at large means. A deterministic
midpoint rescale constrains the non-memory pool. Resting, activated and exhausted
labels share aggregate division and kill rates; they do not implement functional
exhaustion. Fitness bins are fixed assumptions, not sampled manufacturing VCN.
"""

import math
import random

from .construct import binder_engagement
from .outcomes import summarize
from .params import default_params
from .validation import decay_integral, validate_params

MICRO_DT = 0.25  # days per event tick
# Assumed fitness bins; sampled manufacturing VCN does not set these values.
_MICRO_FITNESS_RAW = (0.62, 0.75, 0.85, 0.93, 1.0, 1.09, 1.19, 1.33, 1.52)
# Normalize the arithmetic mean; pool-weighted rate corrections are applied below.
_MICRO_FITNESS_MEAN = sum(_MICRO_FITNESS_RAW) / len(_MICRO_FITNESS_RAW)
MICRO_FITNESS_BINS = tuple(f / _MICRO_FITNESS_MEAN for f in _MICRO_FITNESS_RAW)
MICRO_CD19_DIM = 2.0e4  # copies/cell for the antigen-dim escape clone
MICRO_K_ACT = 1.50  # resting -> activated (1/day) at full stim
MICRO_E0_ACT = 0.90  # fraction of infused product pre-activated (cultured ex vivo)
MICRO_P_EXH0 = 0.12  # exhaustion prob per division, no costim
MICRO_K_REACT = 0.25  # reactivation rate (fraction of K_ACT): exhausted -> activated
MICRO_R_DIM = 0.12  # dim-clone intrinsic growth (1/day); mild fitness cost
MICRO_MU_HI_DIM = 5.0e-7  # per-cell/day high -> dim mutation
MICRO_MU_DIM_NULL = 5.0e-5  # per-cell/day dim -> null mutation


def _micro_bin_weights():
    """Lognormal(0, 0.5) weights over the fitness bins, normalized."""
    s2 = 2.0 * 0.5**2
    ws = [math.exp(-(math.log(f) ** 2) / s2) for f in MICRO_FITNESS_BINS]
    tot = sum(ws)
    return [w / tot for w in ws]


def _poisson(rng, lam):
    """Poisson draw: Knuth for small lambda, gaussian approx for large."""
    if lam <= 1e-9:
        return 0
    if lam < 25.0:
        limit = math.exp(-lam)
        k, p = 0, 1.0
        while True:
            k += 1
            p *= rng.random()
            if p <= limit:
                return k - 1
    v = lam + rng.gauss(0.0, math.sqrt(lam))
    return max(0, int(round(v)))


def _lognormal_sum(rng, K, m, s):
    """Sum of K lognormal(m, s) draws (gamma moment-match for large K)."""
    K = int(K)
    if K <= 0:
        return 0.0
    if s == 0:
        return K * math.exp(m)
    if K < 64:
        return sum(rng.lognormvariate(m, s) for _ in range(K))
    mu = K * math.exp(m + 0.5 * s * s)
    var = K * (math.exp(s * s) - 1.0) * math.exp(2.0 * m + s * s)
    return rng.gammavariate(mu * mu / var, 1.0) * (var / mu)


def run_patient_micro(p=None, seed=None):
    """Integrate one patient with the stochastic cell-event engine.

    Returns the same keys as run_patient() (so all downstream metrics, CRS
    grading and band checks work unchanged) plus micro extras:
      engine, N_rest, X_exh, T_hi, T_dim, T_null series, car_peak,
      divisions, aicd_events, mem_transitions, kill_events, dim_born,
      null_born, exhausted_peak_frac
    """
    params = dict(default_params())
    if p:
        params.update(p)
    rng = random.Random(seed)
    dt = params.get("micro_dt", MICRO_DT)
    validate_params(params, dt)
    step = dt
    nsteps = math.ceil(params["t_end"] / step)

    # ---- initial populations ----
    f_ag = params["f_agloss"]
    f_dim = min(max(params.get("f_dimgloss", 0.0), 0.0), max(0.0, 1.0 - f_ag))
    T_hi = params["T0"] * (1.0 - f_ag - f_dim)
    T_dim = params["T0"] * f_dim
    T_null = params["T0"] * f_ag
    B = params["B0"]
    IFN, IL6, TNF = params["IFN0"], params["IL60"], params["TNF0"]

    FB = MICRO_FITNESS_BINS
    NW = _micro_bin_weights()
    nb = len(FB)
    E0 = max(0.0, params["E0"])
    nN = [E0 * w * (1.0 - MICRO_E0_ACT) for w in NW]
    nE = [E0 * w * MICRO_E0_ACT for w in NW]
    nX = [0.0] * nb
    nM = [0.0] * nb

    # ---- construct-level constants ----
    f41 = params["f41"]
    cs28 = params.get("cs28", 0.0)
    csurv = f41 + cs28
    costim = 1.0 + f41
    kmf = params["kill_mem_frac"] * costim
    micro_debug = bool(params.get("micro_debug", False))
    dbg = [] if micro_debug else None
    bkill_log = [] if micro_debug else None
    eng_hi = binder_engagement(params["cd19_tumor"], params["Kd_app"])
    eng_dim = binder_engagement(MICRO_CD19_DIM, params["Kd_app"])
    eng_B = binder_engagement(params["cd19_B"], params["Kd_app"])
    eng_neg = params["eng_neg"]
    fMem_eff = params["fMem_base"] * (1.0 + 2.0 * f41) * params["fMem_fit"]
    surv = 1.0 + max(0.0, 1.0 - params["fMem_fit"]) * 4.5
    dMem_eff = params["dMem_base"] * surv * (1.0 + f41) / (1.0 + 2.0 * f41)
    dE_base = params["dE0"] / (1.0 + csurv)  # costim-supported survival
    aicd0 = 0.25 / (1.0 + 2.0 * csurv)  # AICD (two-signal paradigm)
    p_exh = MICRO_P_EXH0 * (1.0 - 0.6 * min(1.0, csurv / 0.3))
    amp = params["cyto_amp"]
    # Production per event or effector-day; exponential clearance is applied below.
    b_kill_il6 = params["cIL6_anti"] * amp  # pg/mL per kill
    b_bg_il6 = params["cIL6_bg"] * amp  # pg/mL per effector-day
    b_ifn = params["cIFN"] * amp
    b_tnf = params["cTNF"] * amp
    k0 = params["kKill0"]
    kfix = params["kKill_fixed"]
    Kd_T = params["Kd_T"]
    Kd_B = params["Kd_B"]
    T_niche = params["T_niche"]
    mu_hd = params.get("mu_hi_dim", MICRO_MU_HI_DIM)
    mu_dn = params.get("mu_dim_null", MICRO_MU_DIM_NULL)

    t = [0.0]
    sE, sM, sN, sX = [E0], [0.0], [sum(nN)], [0.0]
    sThi, sTdim, sTnull = [T_hi], [T_dim], [T_null]
    sT = [T_hi + T_dim + T_null]
    sB, sIFN, sIL6, sTNF = [B], [IFN], [IL6], [TNF]
    sCar = [E0]

    divs = aicd_ev = mem_ev = kill_ev = 0
    dim_born = null_born = 0
    exh_peak_frac = 0.0
    car_peak = E0
    lysis_peak = 0.0

    for i in range(1, nsteps + 1):
        dt = min(step, params["t_end"] - t[-1])
        tick_time = min(i * step, params["t_end"])
        # ODE-comparable effector pool = ALL non-memory CAR-T (activated +
        # resting + exhausted): the ODE has a single E compartment, and the
        # micro's E series must reduce to it. Memory (M) is the only separate
        # fate; N/E/X are sub-states of the pool with mean-neutral partitioning.
        E_all = sum(nE[bi] + nN[bi] + nX[bi] for bi in range(nb))
        M_tot = sum(nM)
        N_tot = sum(nN)
        X_tot = sum(nX)
        # Carrying-capacity death acts on the whole non-memory pool,
        # exactly the ODE's sE*E/Emax term.
        dd = params["sE"] * (E_all / params["Emax"]) if E_all > 0.0 else 0.0
        S1all = sum(FB[bi] * (nE[bi] + nN[bi] + nX[bi]) for bi in range(nb))
        fmean = S1all / E_all if E_all > 0.0 else 1.0
        A = T_hi + 0.4 * T_dim + 0.05 * T_null + B
        stim = A / (A + params["Ks_E"]) if A > 0 else 0.0
        d_ode = dE_base + aicd0 * stim + dd
        E_start = E_all  # tick-start pool (for midpoint fluxes below)
        M_start = M_tot
        B_start = B
        T_start = T_hi  # for debug record
        T_dim_start = T_dim
        T_null_start = T_null
        rdiv_pool = params["pE"] * stim * costim  # pool mean division rate

        def gdt(rate):
            return math.expm1(rate * dt)

        def ldt(rate):
            return -math.expm1(-rate * dt) if rate > 0 else 0.0

        km_bin = [0.0] * nb  # memory transitions per bin this tick
        for bi in range(nb):
            f = FB[bi]
            rdiv = params["pE"] * params.get("micro_prolif_cal", 1.0) * (f / fmean) * stim * costim
            rmem = fMem_eff * (f / fmean)
            ldeath = ldt(d_ode)
            bin_divs = 0  # all divisions this bin, this tick
            div_resp = 0  # divisions from the responsive (E+N) pool
            bin_deaths = 0
            for si, arr in enumerate((nE, nN, nX)):
                n0 = arr[bi]
                if n0 <= 0.0:
                    continue
                Kd = min(n0, _poisson(rng, n0 * ldeath))  # ODE-structured death
                n1 = n0 - Kd
                Kb = _poisson(rng, n1 * gdt(rdiv))  # division, daughters keep state
                n2 = n1 + Kb
                rnet = rdiv - d_ode - rmem
                midf = (
                    math.expm1(rnet * dt) / (rnet * dt)
                    if abs(rnet * dt) > 1e-9
                    else 1.0 + rnet * dt / 2.0
                )
                Km = min(n2, _poisson(rng, n0 * rmem * dt * midf))
                arr[bi] = n2 - Km
                nM[bi] += Km
                km_bin[bi] += Km
                bin_divs += Kb
                bin_deaths += Kd
                mem_ev += Km
                if si < 2:
                    div_resp += Kb
            divs += bin_divs
            aicd_ev += bin_deaths * (aicd0 * stim / d_ode) if d_ode > 0.0 else 0.0
            # Exhaustion: a small fraction of divisions from the responsive
            # (activated + resting) pool ends in the exhausted state. Compound
            # Poisson over this tick's responsive divisions (mean p_exh *
            # div_resp); a within-pool move, mean-neutral for the E series.
            nen = nE[bi] + nN[bi]
            if nen > 0.0 and div_resp > 0:
                Kx = min(nen, _poisson(rng, div_resp * p_exh))
                if Kx:
                    move_E = Kx * (nE[bi] / nen)
                    nE[bi] -= move_E
                    nN[bi] -= Kx - move_E
                    nX[bi] += Kx
            # Activation (resting -> activated) and slow reactivation
            # (exhausted -> activated; 4-1BB hyporesponsiveness is reversible).
            # Within-pool moves: mean-neutral for the ODE-comparable series.
            Ka = min(nN[bi], _poisson(rng, nN[bi] * ldt(MICRO_K_ACT * stim)))
            if Ka:
                nN[bi] -= Ka
                nE[bi] += Ka
            Kr = min(nX[bi], _poisson(rng, nX[bi] * ldt(MICRO_K_REACT * MICRO_K_ACT * stim)))
            if Kr:
                nX[bi] -= Kr
                nE[bi] += Kr
            # Memory: ODE death structure only.
            if nM[bi] > 0.0:
                nM[bi] -= min(nM[bi], _poisson(rng, nM[bi] * ldt(dMem_eff)))
            nE[bi] = nE[bi] if nE[bi] > 0.0 else 0.0
            nN[bi] = nN[bi] if nN[bi] > 0.0 else 0.0
            nX[bi] = nX[bi] if nX[bi] > 0.0 else 0.0
            nM[bi] = nM[bi] if nM[bi] > 0.0 else 0.0

        E_end = sum(nE[bi] + nN[bi] + nX[bi] for bi in range(nb))

        # Deterministic midpoint correction constrains the sampled pool mean.
        E_mid_pool = 0.5 * (E_start + E_end)
        S_mid = E_mid_pool + kmf * 0.5 * (M_start + M_tot)

        def _mid_clone(Tv, r, ckill, logistic=True):
            """Trapezoid of a clone's level over the tick: half a tick of kill
            at the step-averaged effector pool, half a tick of growth."""
            if Tv <= 0.0:
                return 0.0
            T1 = max(0.0, Tv - ckill * S_mid * dt)
            if T1 > 0.0:
                gr = r * T1 / (T1 + T_niche) if logistic else r * (1.0 - T1 / params["Bmax"])
                T1 += T1 * math.expm1(gr * dt)
            return 0.5 * (Tv + T1)

        sat_hi_m = T_hi / (T_hi + Kd_T) if T_hi > 0 else 0.0
        sat_dim_m = T_dim / (T_dim + Kd_T) if T_dim > 0 else 0.0
        sat_null_m = T_null / (T_null + Kd_T) if T_null > 0 else 0.0
        sat_B_m = B / (B + Kd_B) if B > 0 else 0.0
        T_mid_hi = _mid_clone(T_hi, params["rT"], eng_hi * costim * (k0 * sat_hi_m + kfix))
        T_mid_dim = _mid_clone(T_dim, MICRO_R_DIM, eng_dim * costim * (k0 * sat_dim_m + kfix))
        T_mid_null = _mid_clone(
            T_null, params["rT_off"], eng_neg * costim * (k0 * sat_null_m + kfix * eng_neg)
        )
        B_mid = _mid_clone(
            B,
            params["rB"],
            eng_B * costim * params["kKillB_frac"] * (k0 * sat_B_m + kfix),
            logistic=False,
        )
        A_mid = T_mid_hi + 0.4 * T_mid_dim + 0.05 * T_mid_null + B_mid
        stim_mid = A_mid / (A_mid + params["Ks_E"]) if A_mid > 0 else 0.0
        d_mid = dE_base + aicd0 * stim_mid + params["sE"] * 0.5 * (E_start + E_end) / params["Emax"]
        g_ode = math.exp((params["pE"] * stim_mid * costim - d_mid - fMem_eff) * dt)
        g_mic = E_end / E_start if E_start > 0.0 else 1.0
        C = g_ode / g_mic if g_mic > 0.0 else 1.0
        if abs(C - 1.0) > 1e-12:
            for bi in range(nb):
                nE[bi] *= C
                nN[bi] *= C
                nX[bi] *= C
                nM[bi] = max(0.0, nM[bi] + km_bin[bi] * (C - 1.0))
            E_end = sum(nE[bi] + nN[bi] + nX[bi] for bi in range(nb))

        # ODE-comparable effector series: the whole non-memory pool — exactly
        # the ODE's single E pool — recorded at the END of the tick (the ODE
        # series likewise holds the post-step state at each time point).
        E_all = E_end
        M_tot = sum(nM)
        N_tot = sum(nN)
        X_tot = sum(nX)
        E_tot = E_all
        car_tot = E_tot + M_tot
        car_peak = max(car_peak, car_tot)
        if car_tot > 0.0:
            exh_peak_frac = max(exh_peak_frac, X_tot / car_tot)

        S_mid = 0.5 * (E_start + E_end) + kmf * 0.5 * (M_start + M_tot)
        K_tumor = 0.0
        K_positive = 0.0
        if T_hi > 0.0:
            sat = T_mid_hi / (T_mid_hi + Kd_T)
            rate = eng_hi * costim * (k0 * S_mid * sat + kfix * S_mid)
            lysis_peak = max(lysis_peak, rate)
            K = min(_poisson(rng, rate * dt), T_hi)
            T_hi -= K
            K_tumor += K
            K_positive += K
        if T_dim > 0.0:
            sat = T_mid_dim / (T_mid_dim + Kd_T)
            K = min(_poisson(rng, eng_dim * costim * (k0 * S_mid * sat + kfix * S_mid) * dt), T_dim)
            T_dim -= K
            K_tumor += K
            K_positive += K
        if T_null > 0.0:
            sat = T_mid_null / (T_mid_null + Kd_T)
            K = min(
                _poisson(rng, eng_neg * costim * (k0 * S_mid * sat + kfix * eng_neg * S_mid) * dt),
                T_null,
            )
            T_null -= K
            K_tumor += K
        if B > 0.0:
            sat = B_mid / (B_mid + Kd_B)
            lam_B = eng_B * costim * params["kKillB_frac"] * (k0 * S_mid * sat + kfix * S_mid) * dt
            K = min(_poisson(rng, lam_B), B)
            B -= K
            if micro_debug:
                bkill_log.append((tick_time, lam_B, K, B))
        kill_ev += int(K_tumor)

        # Midpoint growth is an approximation, including during depletion.
        Tg = 0.5 * (T_start + T_hi)
        T_hi += _poisson(rng, Tg * math.expm1(params["rT"] * Tg / (Tg + T_niche) * dt))
        Tg = 0.5 * (T_dim_start + T_dim)
        T_dim += _poisson(rng, Tg * math.expm1(MICRO_R_DIM * Tg / (Tg + T_niche) * dt))
        Tg = 0.5 * (T_null_start + T_null)
        T_null += _poisson(rng, Tg * math.expm1(params["rT_off"] * Tg / (Tg + T_niche) * dt))
        t1 = min(T_hi, _poisson(rng, mu_hd * T_hi * dt))
        if t1:
            T_hi -= t1
            T_dim += t1
            dim_born += t1
        t2 = min(T_dim, _poisson(rng, mu_dn * T_dim * dt))
        if t2:
            T_dim -= t2
            T_null += t2
            null_born += t2

        # ---- normal B-cell homeostasis ----
        if B > 0.0:
            Bg = 0.5 * (B_start + B)
            change = Bg * math.expm1(params["rB"] * (1.0 - Bg / params["Bmax"]) * dt)
            if change >= 0:
                B += _poisson(rng, change)
            else:
                B -= min(B, _poisson(rng, -change))

        A2 = (
            0.5 * (T_start + T_hi)
            + 0.4 * 0.5 * (T_dim_start + T_dim)
            + 0.05 * 0.5 * (T_null_start + T_null)
            + 0.5 * (B_start + B)
        )
        stim2 = A2 / (A2 + params["Ks_E"]) if A2 > 0 else 0.0
        E_mid = 0.5 * (E_start + E_all)
        noise = rng.lognormvariate(0.0, 0.05)
        fIFN = decay_integral(params["clIFN"], dt)
        fIL6 = decay_integral(params["clIL6"], dt)
        fTNF = decay_integral(params["clTNF"], dt)
        IFN = max(0.0, IFN * math.exp(-params["clIFN"] * dt)) + b_ifn * E_mid * stim2 * fIFN * noise
        IL6 = max(0.0, IL6 * math.exp(-params["clIL6"] * dt)) + (
            b_bg_il6 * E_mid * stim2 * fIL6
            + b_kill_il6 * _lognormal_sum(rng, K_positive, -0.125, 0.5) * (fIL6 / dt) * noise
        )
        TNF = max(0.0, TNF * math.exp(-params["clTNF"] * dt)) + b_tnf * E_mid * stim2 * fTNF * noise

        t.append(tick_time)
        sE.append(E_tot)
        sM.append(M_tot)
        sN.append(N_tot)
        sX.append(X_tot)
        sThi.append(T_hi)
        sTdim.append(T_dim)
        sTnull.append(T_null)
        sT.append(T_hi + T_dim + T_null)
        sB.append(B)
        sIFN.append(IFN)
        sIL6.append(IL6)
        sTNF.append(TNF)
        sCar.append(car_tot)
        if micro_debug:
            dbg.append(
                (
                    tick_time,
                    E_start,
                    E_end,
                    stim,
                    rdiv_pool,
                    d_ode,
                    fMem_eff,
                    fmean,
                    T_start,
                    T_hi,
                    B,
                    stim_mid,
                    C,
                )
            )

    series = {
        "E": sE,
        "M": sM,
        "N_rest": sN,
        "X_exh": sX,
        "Ton": [h + d for h, d in zip(sThi, sTdim)],
        "Toff": sTnull,
        "T_hi": sThi,
        "T_dim": sTdim,
        "T_null": sTnull,
        "T": sT,
        "B": sB,
        "IFN": sIFN,
        "IL6": sIL6,
        "TNF": sTNF,
    }
    out = {
        "params": params,
        "engine": "micro",
        "dt": step,
        "t": t,
        **series,
        **summarize(t, series, params, lysis_peak, seed),
        "f_agloss": f_ag,
        "f_dimgloss": f_dim,
        "eng_T": eng_hi,
        "eng_B": eng_B,
        # ---- micro extras (cell-event bookkeeping) ----
        "car_peak": car_peak,
        "divisions": divs,
        "aicd_events": aicd_ev,
        "mem_transitions": mem_ev,
        "kill_events": kill_ev,
        "dim_born": dim_born,
        "null_born": null_born,
        "exhausted_peak_frac": exh_peak_frac,
    }
    if micro_debug:
        out["debug"] = dbg
        out["debug_bkill"] = bkill_log
    return out
