"""Phenomenological CD19 CAR-T models and shared simulation interfaces."""

from .cohort import run_cohort
from .construct import (
    CD19_KO,
    CD19_NORMAL_B,
    CD19_TUMOR_ALL,
    CD19_TUMOR_DLBCL,
    CONSTRUCT,
    binder_engagement,
    binder_specificity_table,
)
from .lot_criteria import ACADEMIC_CTL019, COMMERCIAL_US, assess_lot, dose_interval
from .manufacturing import manufacture, vector_production
from .micro_engine import (
    MICRO_CD19_DIM,
    MICRO_DT,
    MICRO_E0_ACT,
    MICRO_FITNESS_BINS,
    MICRO_K_ACT,
    MICRO_K_REACT,
    MICRO_MU_DIM_NULL,
    MICRO_MU_HI_DIM,
    MICRO_P_EXH0,
    MICRO_R_DIM,
    _lognormal_sum,
    _micro_bin_weights,
    _poisson,
    run_patient_micro,
)
from .ode_engine import _derivs, p_kill_memfrac, run_patient
from .params import default_params
from . import publication_stats
from .toxicity import CRS_IL6_CUTS, ICANS_P_BY_CRS, crs_grade, icans_grade

__all__ = [
    # construct
    "CONSTRUCT",
    "CD19_TUMOR_DLBCL",
    "CD19_TUMOR_ALL",
    "CD19_NORMAL_B",
    "CD19_KO",
    "binder_engagement",
    "binder_specificity_table",
    # params / manufacturing
    "default_params",
    "vector_production",
    "manufacture",
    "assess_lot",
    "dose_interval",
    "COMMERCIAL_US",
    "ACADEMIC_CTL019",
    # toxicity
    "CRS_IL6_CUTS",
    "ICANS_P_BY_CRS",
    "crs_grade",
    "icans_grade",
    # engines
    "run_patient",
    "p_kill_memfrac",
    "run_patient_micro",
    # cohort
    "run_cohort",
    # micro internals (used by diagnostics/)
    "MICRO_DT",
    "MICRO_FITNESS_BINS",
    "MICRO_CD19_DIM",
    "MICRO_K_ACT",
    "MICRO_E0_ACT",
    "MICRO_P_EXH0",
    "MICRO_K_REACT",
    "MICRO_R_DIM",
    "MICRO_MU_HI_DIM",
    "MICRO_MU_DIM_NULL",
    "_derivs",
    "_poisson",
    "_lognormal_sum",
    "_micro_bin_weights",
]
