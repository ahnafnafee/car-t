"""Provenance tests for simulator/cart_sim/lot_distributions.py.

The point of this module is that a simulated lot is built from published
per-patient product attributes instead of invented defaults, so the tests are
mostly provenance tests: every attribute must remain byte-exactly traceable to a
retained source file, the Kato patient-level transcription must reproduce the
paper's own summary, and the derived net-yield inversion must be exactly the
inverse of the manufacturing chain.
"""

import random
import re
import statistics
import unittest
from pathlib import Path

from simulator.cart_sim import lot_distributions as ld
from simulator.cart_sim.cohort import run_cohort
from simulator.cart_sim.lot_distributions import (
    ATTRIBUTES,
    KATO2025_OOS_DLBCL,
    KATO2025_PUBLISHED_SUMMARY,
    LOT_PROFILES,
    implied_net_yield,
    profile_names,
    published_lot,
    published_medians,
)
from simulator.cart_sim.manufacturing import manufacture
from simulator.cart_sim.publication_stats import STATS

ROOT = Path(__file__).resolve().parents[1]

KATO_FILE = "data/references/kato_2025_cytotherapy_oos_japan.md"


class AttributesProvenanceTests(unittest.TestCase):
    def test_merged_into_the_single_evidence_set(self):
        for key in ATTRIBUTES:
            self.assertIn(key, STATS, f"{key} is not reachable through publication_stats.STATS")
            self.assertIs(STATS[key], ATTRIBUTES[key])

    def test_quotes_are_byte_exact_in_retained_files(self):
        for key, attr in ATTRIBUTES.items():
            with self.subTest(key=key):
                path = ROOT / attr["file"]
                self.assertTrue(path.is_file(), f"missing retained file {attr['file']}")
                self.assertIn(attr["quote"], path.read_text(encoding="utf-8"))

    def test_quotes_state_the_recorded_population_size(self):
        # Guards the n= claim: the retained text must contain the cohort size the
        # distribution is calibrated with.
        expected = {
            "fong2023_dose_per_kg": "146 tisagenlecleucel quality",
            "fong2023_weight_kg": "86 batches (84 patients)",
            "pi_juliet_dose_cells": "115 patients",
            "us20050113564_te_bbzeta_pct": "75 transduction experiments",
        }
        text = {}
        for key, needle in expected.items():
            path = ROOT / ATTRIBUTES[key]["file"]
            text.setdefault(key, path.read_text(encoding="utf-8"))
            self.assertIn(needle, text[key], f"{key}: population size not in the retained text")

    def test_kato_table_rows_are_in_the_retained_table(self):
        text = (ROOT / KATO_FILE).read_text(encoding="utf-8")
        segment = text[text.index("Table 2. Patient-level") :][:9000]
        rows = {}
        for line in segment.splitlines():
            m = re.match(r"^\| ([A-Z])(?: \[a\]\([^)]*\))? \|(.*)$", line)
            if m:
                rows[m.group(1)] = [c.strip() for c in m.group(2).split("|")]
        self.assertEqual(len(rows), KATO2025_PUBLISHED_SUMMARY["n"])
        for patient, viability, dose, _reason in KATO2025_OOS_DLBCL:
            with self.subTest(patient=patient):
                self.assertIn(patient, rows)
                self.assertAlmostEqual(float(rows[patient][5]), viability, delta=1e-9)
                self.assertAlmostEqual(float(rows[patient][6]), dose, delta=1e-9)

    def test_kato_transcription_reproduces_the_published_summary(self):
        viabilities = [row[1] for row in KATO2025_OOS_DLBCL]
        doses = [row[2] for row in KATO2025_OOS_DLBCL]
        self.assertEqual(len(viabilities), KATO2025_PUBLISHED_SUMMARY["n"])
        self.assertAlmostEqual(
            statistics.median(viabilities), KATO2025_PUBLISHED_SUMMARY["viability_pct_median"],
            delta=1e-9,
        )
        # The paper reports the dose median rounded to two significant digits (1.7e8).
        self.assertAlmostEqual(round(statistics.median(doses), 1), 1.7, delta=1e-9)

    def test_kato_table_is_an_out_of_specification_tail(self):
        below = [row for row in KATO2025_OOS_DLBCL if row[1] < 70.0]
        self.assertGreaterEqual(len(below), 9, "low-viability rows are the Japanese criterion tail")
        self.assertTrue(all(row[3] for row in KATO2025_OOS_DLBCL), "every row needs an OOS reason")


class ProfileTests(unittest.TestCase):
    def test_profile_fields_point_at_attributes(self):
        for name, spec in LOT_PROFILES.items():
            with self.subTest(profile=name):
                for field, key in spec["fields"].items():
                    if field == "empirical_pair":
                        self.assertIs(key, KATO2025_OOS_DLBCL)
                        self.assertEqual(len(key), KATO2025_PUBLISHED_SUMMARY["n"])
                    else:
                        self.assertIn(key, ATTRIBUTES, f"{name}.{field} has no attribute")
                for key in spec.get("borrowed_fields", {}).values():
                    self.assertIn(key, ATTRIBUTES)
                self.assertFalse(
                    set(spec["fields"]) & set(spec.get("borrowed_fields", {})),
                    f"{name} publishes and borrows the same field",
                )
                self.assertFalse(
                    set(spec["unpublished_fields"]) & set(spec["fields"]),
                    f"{name} calls a published field unpublished",
                )
                self.assertTrue(spec["population_caveat"], f"{name} needs its population caveat")

    def test_published_medians_match_the_attributes(self):
        medians = published_medians("commercial_ball_2023")
        self.assertAlmostEqual(medians["te"], ATTRIBUTES["fong2023_car_fraction"]["median"])
        self.assertAlmostEqual(
            medians["viability"], ATTRIBUTES["fong2023_viability_pct"]["median"] / 100.0
        )
        self.assertEqual(medians["starting_t_cells"], ATTRIBUTES["fong2023_leukapheresis_cd3_cells"]["median"])

    def test_lot_is_deterministic_and_provenanced(self):
        a = published_lot(random.Random(11), "commercial_ball_2023", indication="B-ALL", weight_kg=30.0)
        b = published_lot(random.Random(11), "commercial_ball_2023", indication="B-ALL", weight_kg=30.0)
        strip = lambda lot: {k: v for k, v in lot.items() if k != "assumptions"}  # noqa: E731
        self.assertEqual(strip(a), strip(b))
        self.assertEqual(a["profile"], "commercial_ball_2023")
        for field, key in a["provenance"].items():
            if " x " in key:
                continue
            self.assertIn(key, ATTRIBUTES, f"{field} provenance is not a recorded attribute")
        for field in ("te", "viability", "starting_t_cells", "weight_kg", "dose_cells"):
            self.assertIn(field, a)
        self.assertGreater(a["dose_cells"], 0.0)
        # Percent-valued attributes must come back as fractions.
        self.assertTrue(0.0 < a["viability"] < 1.0 and 0.0 < a["te"] < 1.0)

    def test_assumptions_stay_labelled(self):
        lot = published_lot(random.Random(3), "commercial_dlbcl_2020", indication="DLBCL")
        text = " | ".join(lot["assumptions"])
        self.assertIn("borrowed", text)
        self.assertIn("scenario default retained", text)
        self.assertIn("modelling conventions", text)
        self.assertIn("population:", text)
        oos = published_lot(random.Random(3), "oos_tail_2025", indication="DLBCL")
        self.assertIn("empirical uniform resample", " | ".join(oos["assumptions"]))
        ball = published_lot(random.Random(3), "commercial_ball_2023", indication="B-ALL", weight_kg=30.0)
        self.assertIn("net_yield inverted", " | ".join(ball["assumptions"]))
        self.assertIn("scenario weight", " | ".join(ball["assumptions"]))

    def test_dose_scales_with_the_published_or_scenario_weight(self):
        published = published_lot(random.Random(5), "commercial_ball_2023", indication="B-ALL")
        self.assertAlmostEqual(
            published["dose_cells"], published["dose_per_kg"] * published["weight_kg"], delta=1e-6
        )
        scenario = published_lot(
            random.Random(5), "commercial_ball_2023", indication="B-ALL", weight_kg=30.0
        )
        self.assertAlmostEqual(scenario["dose_cells"], scenario["dose_per_kg"] * 30.0, delta=1e-6)

    def test_empirical_profile_medians_converge_on_the_table(self):
        rng = random.Random(17)
        lots = [published_lot(rng, "oos_tail_2025", indication="DLBCL") for _ in range(2000)]
        self.assertLess(
            abs(statistics.median(lot["viability"] for lot in lots) - 0.689) / 0.689, 0.05
        )
        self.assertLess(
            abs(statistics.median(lot["dose_cells"] for lot in lots) - 1.661e8) / 1.661e8, 0.05
        )
        self.assertEqual(len({lot["oos_reason"] for lot in lots}), len({r[3] for r in KATO2025_OOS_DLBCL}))

    def test_profile_validation(self):
        rng = random.Random(0)
        with self.assertRaises(ValueError):
            published_lot(rng, "made_up_2030")
        with self.assertRaises(ValueError):
            published_lot(rng, "commercial_ball_2023", indication="DLBCL")
        with self.assertRaises(ValueError):
            published_lot(rng, "commercial_ball_2023", indication="B-ALL", weight_kg=0)
        self.assertEqual(
            profile_names(),
            ["academic_2005", "commercial_ball_2023", "commercial_dlbcl_2020", "oos_tail_2025"],
        )


class ImpliedYieldTests(unittest.TestCase):
    def test_inversion_is_the_exact_inverse_of_the_chain(self):
        starting = ATTRIBUTES["fong2023_leukapheresis_cd3_cells"]["median"]
        viability = ATTRIBUTES["fong2023_viability_pct"]["median"] / 100.0
        te = ATTRIBUTES["fong2023_car_fraction"]["median"]
        weight = ATTRIBUTES["fong2023_weight_kg"]["median"]
        dose = ATTRIBUTES["fong2023_dose_per_kg"]["median"] * weight
        implied, total = implied_net_yield(starting, dose, viability, te)
        self.assertAlmostEqual(total, starting * implied, delta=1e-6)
        man = manufacture(
            apheresis_wbc=starting,
            t_cell_frac=1.0,
            net_yield=implied,
            te=te,
            viability=viability,
            dose_target=dose,
        )
        self.assertAlmostEqual(man["dose_CARplus_cells"], dose, delta=1e-6 * dose)
        self.assertAlmostEqual(man["product_viable_car_cells"], dose, delta=1e-6 * dose)

    def test_implied_recovery_is_far_above_the_illustrative_default(self):
        # Published B-ALL attributes at the published median weight: the recovery
        # they imply, versus the invented 0.05 scenario default.
        dose = (
            ATTRIBUTES["fong2023_dose_per_kg"]["median"] * ATTRIBUTES["fong2023_weight_kg"]["median"]
        )
        implied, _total = implied_net_yield(
            ATTRIBUTES["fong2023_leukapheresis_cd3_cells"]["median"],
            dose,
            ATTRIBUTES["fong2023_viability_pct"]["median"] / 100.0,
            ATTRIBUTES["fong2023_car_fraction"]["median"],
        )
        self.assertGreater(implied, 0.05)

    def test_input_validation(self):
        for args in ((0, 1.0, 0.9, 0.1), (1.0, 0.0, 0.9, 0.1), (1.0, 1.0, 0.0, 0.1), (1.0, 1.0, 0.9, 0.0)):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    implied_net_yield(*args)


class CohortLotTests(unittest.TestCase):
    def test_cohort_uses_published_attributes_and_reports_provenance(self):
        cohort = run_cohort(
            n=8, seed=21, indication="B-ALL", engine="ode", lot_stats="commercial_ball_2023"
        )
        self.assertEqual(cohort["lot_stats"], "commercial_ball_2023")
        self.assertIsNotNone(cohort["implied_net_yield_median"])
        self.assertEqual(cohort["published_dose_attainment_median"], 1.0)
        for patient in cohort["patients"]:
            self.assertEqual(patient["lot_profile"], "commercial_ball_2023")
            self.assertEqual(
                patient["lot_provenance"]["viability"], "fong2023_viability_pct"
            )
            self.assertIn("implied_net_yield", patient)
            # The published leukapheresis count is the starting material itself.
            self.assertIn("fong2023_leukapheresis_cd3_cells", patient["lot_provenance"].values())
        replay = run_cohort(
            n=8, seed=21, indication="B-ALL", engine="ode", lot_stats="commercial_ball_2023"
        )
        self.assertEqual(
            [p["manufacturing"]["dose_viable_car_cells"] for p in replay["patients"]],
            [p["manufacturing"]["dose_viable_car_cells"] for p in cohort["patients"]],
        )

    def test_derived_yield_reaches_the_published_dose(self):
        cohort = run_cohort(
            n=6, seed=4, indication="B-ALL", engine="ode", lot_stats="commercial_ball_2023"
        )
        for patient in cohort["patients"]:
            man = patient["manufacturing"]
            self.assertAlmostEqual(
                man["dose_CARplus_cells"], man["dose_target_viable_car_cells"], delta=1e-6
            )

    def test_forced_low_yield_shows_as_dose_shortfall(self):
        cohort = run_cohort(
            n=4,
            seed=9,
            indication="B-ALL",
            engine="ode",
            lot_stats="commercial_ball_2023",
            lot_params={"net_yield": 0.01},
        )
        self.assertLess(cohort["published_dose_attainment_median"], 1.0)

    def test_oos_profile_reports_the_published_oos_reason(self):
        cohort = run_cohort(n=5, seed=2, indication="DLBCL", engine="ode", lot_stats="oos_tail_2025")
        reasons = {p["oos_reason"] for p in cohort["patients"]}
        self.assertTrue(reasons <= {row[3] for row in KATO2025_OOS_DLBCL})

    def test_lot_stats_validation(self):
        with self.assertRaises(ValueError):
            run_cohort(n=1, indication="DLBCL", lot_stats="made_up_2030")
        with self.assertRaises(ValueError):
            run_cohort(n=1, indication="DLBCL", lot_stats="commercial_ball_2023")
        with self.assertRaises(ValueError):
            run_cohort(n=1, indication="B-ALL", lot_stats="oos_tail_2025")

    def test_default_path_unchanged(self):
        cohort = run_cohort(n=3, seed=3, engine="ode")
        self.assertIsNone(cohort["lot_stats"])
        self.assertIsNone(cohort["implied_net_yield_median"])
        self.assertEqual(cohort["lot_assumptions"], [])
        self.assertTrue(all("lot_provenance" not in p for p in cohort["patients"]))


if __name__ == "__main__":
    unittest.main()
