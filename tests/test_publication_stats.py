"""Provenance and calibration tests for simulator/cart_sim/publication_stats.py.

Every published statistic must remain traceable to its retained source file,
and the two-sided log-normal calibration must reproduce the published median.
"""

import math
import random
import statistics
import unittest
from pathlib import Path

from simulator.cart_sim import run_cohort
from simulator.cart_sim.publication_stats import STATS, _z_max, calibrate, sample

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FIELDS = (
    "median",
    "low",
    "high",
    "n",
    "unit",
    "source",
    "url",
    "file",
    "quote",
    "population",
)


class PublicationStatsProvenanceTests(unittest.TestCase):
    def test_entries_are_complete_and_ordered(self):
        self.assertGreaterEqual(len(STATS), 6)
        for key, s in STATS.items():
            with self.subTest(key=key):
                for field in REQUIRED_FIELDS:
                    self.assertIn(field, s)
                self.assertLess(s["low"], s["median"])
                self.assertLess(s["median"], s["high"])
                self.assertGreaterEqual(s["n"], 2)
                self.assertTrue(s["url"].startswith("https://"))

    def test_quotes_are_verbatim_in_retained_files(self):
        for key, s in STATS.items():
            with self.subTest(key=key):
                path = ROOT / s["file"]
                self.assertTrue(path.is_file(), f"missing retained file {s['file']}")
                text = path.read_text(encoding="utf-8")
                self.assertIn(s["quote"], text, f"quote not byte-exact in {s['file']}")


class CalibrationTests(unittest.TestCase):
    def test_z_max_matches_stdlib_inverse_normal(self):
        normal = statistics.NormalDist()
        for n in (2, 10, 37, 60, 75, 1000):
            expected = normal.inv_cdf((n - 0.375) / (n + 0.25))
            self.assertAlmostEqual(_z_max(n), expected, places=6)

    def test_calibration_reproduces_published_medians(self):
        for key, s in STATS.items():
            with self.subTest(key=key):
                median, sigma_down, sigma_up, z = calibrate(key)
                self.assertAlmostEqual(median, s["median"], delta=1e-9 * s["median"])
                self.assertGreater(sigma_down, 0)
                self.assertGreater(sigma_up, 0)
                self.assertGreater(z, 0)
                # In-expectation range reproduction: median * exp(sigma * z) == bound.
                self.assertAlmostEqual(median * math.exp(sigma_up * z), s["high"], delta=1e-6 * s["high"])
                self.assertAlmostEqual(median * math.exp(-sigma_down * z), s["low"], delta=1e-6 * s["low"])

    def test_sample_is_deterministic_and_centered_on_the_median(self):
        for key, s in STATS.items():
            with self.subTest(key=key):
                rng_a, rng_b = random.Random(42), random.Random(42)
                draws = [sample(rng_a, key) for _ in range(4)]
                replay = [sample(rng_b, key) for _ in range(4)]
                self.assertEqual(draws, replay)
                self.assertGreater(len(set(draws)), 1)
                rng = random.Random(7)
                values = [sample(rng, key) for _ in range(4000)]
                self.assertTrue(all(v > 0 and math.isfinite(v) for v in values))
                self.assertLess(
                    abs(statistics.median(values) - s["median"]) / s["median"], 0.10
                )
                # The published range is the observed range of an n-sample, so the
                # calibrated tail may exceed it; most of the mass must stay inside.
                inside = sum(s["low"] <= v <= s["high"] for v in values)
                self.assertGreater(inside / len(values), 0.90)


class CohortProductStatsTests(unittest.TestCase):
    def test_eliana_mode_samples_published_doses(self):
        cohort = run_cohort(n=10, seed=5, indication="B-ALL", engine="ode", product_stats="eliana_2018")
        self.assertEqual(cohort["product_stats"], "eliana_2018")
        doses = [r["infused_dose_per_kg"] for r in cohort["patients"]]
        self.assertTrue(all(d > 0 for d in doses))
        self.assertGreater(len(set(doses)), 1, "doses should be drawn, not a fixed scenario target")
        self.assertTrue(all(r["dose_source"] == "published eliana2018_dose_per_kg" for r in cohort["patients"]))
        replay = run_cohort(n=10, seed=5, indication="B-ALL", engine="ode", product_stats="eliana_2018")
        self.assertEqual([r["infused_dose_per_kg"] for r in replay["patients"]], doses)

    def test_product_stats_validation(self):
        with self.assertRaises(ValueError):
            run_cohort(n=1, indication="DLBCL", product_stats="eliana_2018")
        with self.assertRaises(ValueError):
            run_cohort(n=1, indication="B-ALL", product_stats="unknown_2099")

    def test_default_path_unchanged(self):
        cohort = run_cohort(n=2, seed=3, engine="ode")
        self.assertIsNone(cohort["product_stats"])
        self.assertTrue(all("dose_source" not in r for r in cohort["patients"]))


if __name__ == "__main__":
    unittest.main()
