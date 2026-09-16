"""Illustrative parameters for a 4-1BB CD19 CAR model; see docs/EVIDENCE.md."""

from .construct import CD19_NORMAL_B, CD19_TUMOR_DLBCL


def default_params():
    return {
        # Infused viable CAR-positive dose; standalone scenario, not a fitted median.
        "E0": 1.2e8,  # infused CAR+ effector T cells (set by manufacture() in cohorts)
        "T0": 1.0e10,  # tumor cell burden (DLBCL)
        "B0": 1.0e9,  # measurable (blood) CD19+ B cells; marrow reservoir via homeostasis
        "f_agloss": 0.0,  # fraction of T0 that is CD19-low antigen-loss clone at infusion
        # ---- CAR-T effector expansion / contraction ----
        "pE": 0.75,  # max proliferation rate (1/day) at full antigen saturation
        "dE0": 0.35,  # basal effector death (1/day)
        "Ks_E": 8.5e8,  # antigen half-saturation for expansion (target cells)
        "sE": 0.8,  # density-dependent contraction coefficient
        "Emax": 3.0e9,  # effector carrying capacity (lymphodepletion-created space)
        # ---- CAR-T memory (persistence) ----
        "fMem_base": 0.03,  # effector -> memory conversion (1/day), pre-costim
        "dMem_base": 0.03,  # memory death (1/day), pre-costim
        "fMem_fit": 1.0,  # product-fitness scaling of memory formation (cohort-sampled)
        "kill_mem_frac": 0.5,  # memory contribution to kill (per cell)
        # ---- tumor ----
        "rT": 0.15,  # CD19+ tumor intrinsic growth at high burden (1/day)
        "rT_off": 0.04,  # antigen-loss clone growth (less fit; slow escape)
        "T_niche": 1.5e8,  # regrowth niche saturation (slow seed regrowth below this)
        "kKill0": 4.0,  # mass-action kill rate per effector (1/day), pre-engagement/costim
        "Kd_T": 5.0e9,  # mass-action saturation (tumor cells)
        "kKill_fixed": 0.008,  # fixed kill capacity per effector (1/day) at low target density
        "Kd_app": 8.0e4,  # avidity half-saturation (copies/cell)
        "cd19_tumor": CD19_TUMOR_DLBCL,
        "cd19_B": CD19_NORMAL_B,
        "eng_neg": 0.004,  # residual CAR kill efficiency on CD19-negative cells (bystander)
        # ---- normal B cells (on-target / off-tumor) ----
        "rB": 0.012,  # B-cell homeostatic regrowth (1/day); recovery takes months
        "Bmax": 1.0e9,  # B-cell compartment carrying capacity
        "kKillB_frac": 0.38,  # fraction of tumor-kill efficiency on normal B
        "Kd_B": 1.0e10,  # mass-action saturation for B cells
        # ---- costimulation (4-1BB) ----
        "f41": 0.30,  # 4-1BB boost to expansion + kill; 0 for 1st-gen (CD3z only)
        "cs28": 0.0,  # CD28-costim survival proxy (arm-specific; see benchmarks.py ARMS)
        # ---- cytokines (pg/mL); steady-state = production / clearance ----
        "IL60": 4.0,
        "TNF0": 0.0,
        "IFN0": 0.0,
        "cIFN": 1.5e-7,
        "clIFN": 1.5,
        "cIL6_anti": 1.5e-8,
        "cIL6_bg": 1.5e-7,
        "clIL6": 1.0,
        "cTNF": 7.0e-8,
        "clTNF": 1.8,
        "cyto_amp": 1.0,  # per-patient cytokine amplification (monocyte/IL-6 axis)
        # ---- time / numerics ----
        "t_end": 120.0,
        "dt": 0.2,
        # ---- stochasticity ----
        "sigma": 0.06,  # relative process noise on E and Ton
    }
