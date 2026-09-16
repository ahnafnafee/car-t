"""Compare matched, deterministic ODE patients with stochastic micro trajectories."""

import argparse
import sys
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "simulator"))

from cart_sim import run_patient, run_patient_micro


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=int, default=10)
    args = parser.parse_args()
    if args.seeds <= 0:
        parser.error("--seeds must be positive")
    params = {"sigma": 0, "mu_hi_dim": 0, "mu_dim_null": 0}
    ode = run_patient(params)
    micro = [run_patient_micro(params, seed=i) for i in range(args.seeds)]
    print("Metric                 ODE       Micro median       Micro range")
    for key in ("E_peak", "M_d120", "T_d90", "B_d90", "IL6_peak"):
        values = [r[key] for r in micro]
        print(
            f"{key:18s} {ode[key]:11.4g} {median(values):16.4g} "
            f"{min(values):11.4g} .. {max(values):.4g}"
        )
    print("Shared assumptions and population rescaling limit independence of this comparison.")


if __name__ == "__main__":
    main()
