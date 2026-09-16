"""Fast executable checks for both simulation interfaces."""

from .micro_engine import run_patient_micro
from .ode_engine import run_patient


def main():
    for engine in (run_patient, run_patient_micro):
        result = engine({"t_end": 2.1}, seed=7)
        if result["t"][-1] != 2.1 or result["T_d90"] is not None:
            raise RuntimeError(f"{engine.__name__}: invalid observation horizon")
        if any(value < 0 for key in ("E", "M", "T", "B") for value in result[key]):
            raise RuntimeError(f"{engine.__name__}: negative cell count")
        print(f"{engine.__name__}: finite-horizon smoke check passed")
    print("Full regression suite: python -m unittest discover -s tests -v")
