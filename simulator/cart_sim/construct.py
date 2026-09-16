"""Reference sequence metadata and phenomenological antigen-density engagement."""

import math

from constructs.build_car import CAR_AA, DOMAIN_MAP, ORF, ORF_FULL

CONSTRUCT = {
    "name": "CD19 CAR (tisagenlecleucel; FMC63-CD8a-4-1BB-CD3z, 486 aa VL-first)",
    "total_aa": len(CAR_AA),
    "orf_bp": len(ORF),
    "orf_stop_bp": len(ORF_FULL),
    "gc_pct": round(100 * sum(base in "GC" for base in ORF_FULL) / len(ORF_FULL), 1),
    "vector": "Conceptual lentiviral process; no vector sequence is assembled",
    "domains": [(name, end - start + 1, "See docs/EVIDENCE.md") for name, start, end in DOMAIN_MAP],
}

# Scenario antigen densities (copies/cell); not measurements from the sequence.
CD19_TUMOR_DLBCL = 4.0e5  # bulk B-cell malignancy, high CD19
CD19_TUMOR_ALL = 5.0e5  # B-ALL blasts, very high CD19
CD19_NORMAL_B = 2.5e5  # normal CD19+ B cells
CD19_KO = 0.0  # CD19-negative / knockout target (specificity control)


def binder_engagement(cd19_density, Kd_app):
    """Fractional 'kill-permissibility' for a target with cd19_density copies/cell.

    Avidity model: multivalent CAR engagement of a high-density antigen is approximated by a
    saturating (Langmuir-like) function of antigen density with an apparent half-saturation
    Kd_app (copies/cell). High CD19 -> high engagement; CD19-negative -> ~0.
    """
    if not math.isfinite(cd19_density) or cd19_density < 0:
        raise ValueError("CD19 density must be finite and nonnegative")
    if not math.isfinite(Kd_app) or Kd_app <= 0:
        raise ValueError("Kd_app must be finite and positive")
    if cd19_density == 0:
        return 0.0
    return cd19_density / (cd19_density + Kd_app)


def binder_specificity_table(Kd_app, cd19_densities=(0, 1e4, 1e5, 2.5e5, 4e5, 1e6)):
    """Does the construct bind specifically to CD19?"""
    ref = binder_engagement(4e5, Kd_app)
    rows = []
    for d in cd19_densities:
        eng = binder_engagement(d, Kd_app)
        rows.append(
            {
                "cd19": d,
                "engagement": eng,
                "rel_kill": (eng / ref) if ref > 0 else 0.0,
            }
        )
    return rows
