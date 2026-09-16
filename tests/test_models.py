import math
import random
import unittest
from statistics import median

from simulator.cart_sim import (
    binder_engagement,
    default_params,
    manufacture,
    run_cohort,
    run_patient,
    run_patient_micro,
    vector_production,
)
from simulator.cart_sim.micro_engine import _lognormal_sum
from simulator.cart_sim.ode_engine import _derivs
from simulator.cart_sim.outcomes import at_day, summarize
from simulator.cart_sim.validation import decay_integral


class ModelTests(unittest.TestCase):
    def test_short_runs_have_no_future_outcomes(self):
        for engine in (run_patient, run_patient_micro):
            result = engine({"t_end": 1.13}, seed=3)
            self.assertEqual(result["t"][-1], 1.13)
            for key in ("T_d90", "M_d120", "responds", "CR", "relapses", "B_aplasia"):
                self.assertIsNone(result[key])

    def test_invalid_inputs(self):
        for engine in (run_patient, run_patient_micro):
            for params in (
                {"T0": 0},
                {"E0": -1},
                {"t_end": math.nan},
                {"Kd_app": 0},
                {"f_agloss": 0.8, "f_dimgloss": 0.4},
            ):
                with self.subTest(engine=engine.__name__, params=params):
                    with self.assertRaises(ValueError):
                        engine(params)
        for params in (
            {"n": 0},
            {"engine": "typo"},
            {"indication": "ALL"},
            {"agloss_mode": "typo"},
            {"base": {"t_end": 119}},
        ):
            with self.assertRaises(ValueError):
                run_cohort(**params)

    def test_no_target_means_no_lysis(self):
        params = default_params()
        params["cIL6_bg"] = 0
        derivative = _derivs([1e8, 1e7, 0, 0, 0, 0, 0, 0], params)
        self.assertEqual(derivative[2:5], [0, 0, 0])
        self.assertEqual(derivative[6], 0)

    def test_zero_dose_is_preserved(self):
        cohort = run_cohort(base={"dose_scale": 0}, n=2, engine="ode")
        self.assertTrue(all(r["params"]["E0"] == 0 for r in cohort["patients"]))
        self.assertEqual(cohort["ORR"], 0)

    def test_median_and_seed_reproducibility(self):
        first = run_cohort(n=2, engine="ode", seed=11)
        second = run_cohort(n=2, engine="ode", seed=11)
        self.assertEqual(first, second)
        self.assertEqual(first["IL6_peak_median"], median(r["IL6_peak"] for r in first["patients"]))

    def test_engine_tumor_contract(self):
        for engine in (run_patient, run_patient_micro):
            result = engine({"t_end": 2, "f_agloss": 0.2}, seed=3)
            for positive, negative, total in zip(result["Ton"], result["Toff"], result["T"]):
                self.assertAlmostEqual(positive + negative, total, places=4)
            for key in ("E", "M", "T", "B", "IFN", "IL6", "TNF"):
                self.assertTrue(all(math.isfinite(v) and v >= 0 for v in result[key]))

    def test_small_population_transfers(self):
        p = {
            "E0": 1,
            "T0": 2,
            "B0": 1,
            "t_end": 5,
            "f_agloss": 0.4,
            "f_dimgloss": 0.5,
            "mu_hi_dim": 5,
            "mu_dim_null": 5,
        }
        for seed in range(10):
            result = run_patient_micro(p, seed)
            for key in ("E", "M", "N_rest", "X_exh", "T_hi", "T_dim", "T_null", "B"):
                self.assertTrue(all(v >= 0 for v in result[key]), key)

    def test_clearance_and_lognormal_limits(self):
        self.assertEqual(decay_integral(0, 0.25), 0.25)
        self.assertAlmostEqual(_lognormal_sum(random.Random(1), 100, 0, 0), 100)
        result = run_patient_micro({"t_end": 1, "clIFN": 0, "clIL6": 0, "clTNF": 0}, 1)
        self.assertTrue(math.isfinite(result["IL6_peak"]))

    def test_b_cells_above_capacity_contract_without_effectors(self):
        params = {"E0": 0, "B0": 2e9, "t_end": 1}
        for engine in (run_patient, run_patient_micro):
            result = engine(params, seed=1)
            self.assertLess(result["B"][-1], params["B0"])

    def test_endpoint_uses_day90_not_future_nadir(self):
        times = [0, 80, 90, 120]
        series = {key: [0, 0, 0, 0] for key in ("E", "M", "IFN", "IL6", "TNF")}
        series.update(T=[100, 30, 15, 1], B=[1e9, 1e5, 1e8, 1e8])
        result = summarize(times, series, {"T0": 100}, 0, 1)
        self.assertFalse(result["responds"])
        self.assertFalse(result["B_aplasia"])
        self.assertEqual(at_day([0, 2], [0, 10], 1), 5)

    def test_lot_and_engagement_domains(self):
        self.assertEqual(
            manufacture(net_yield=0)["source_assessment"]["status"], "fails_disclosed_criteria"
        )
        with self.assertRaises(ValueError):
            manufacture(te=2)
        with self.assertRaises(ValueError):
            vector_production(packaging_efficiency=-1)
        with self.assertRaises(ValueError):
            binder_engagement(1, 0)
        self.assertEqual(binder_engagement(0, 1), 0)
