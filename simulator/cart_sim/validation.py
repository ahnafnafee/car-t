"""Validate model domains before numerical integration."""

import math


def validate_params(params, step):
    for key, value in params.items():
        if isinstance(value, (int, float)) and (not math.isfinite(value) or value < 0):
            raise ValueError(f"{key} must be finite and nonnegative")
    for key in ("T0", "Ks_E", "Emax", "T_niche", "Kd_T", "Kd_B", "Kd_app", "Bmax"):
        if params[key] <= 0:
            raise ValueError(f"{key} must be positive")
    if not math.isfinite(step) or step <= 0:
        raise ValueError("time step must be finite and positive")
    for key in ("f_agloss", "f_dimgloss", "eng_neg"):
        if params.get(key, 0) > 1:
            raise ValueError(f"{key} must be between zero and one")
    if params.get("f_agloss", 0) + params.get("f_dimgloss", 0) > 1:
        raise ValueError("antigen-loss and dim fractions must sum to at most one")


def decay_integral(rate, dt):
    """Integral of exponential clearance, including zero clearance."""
    return -math.expm1(-rate * dt) / rate if rate else dt
