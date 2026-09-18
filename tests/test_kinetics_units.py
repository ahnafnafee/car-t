"""Tests for simulator/cart_sim/kinetics_units.py (docs/ONE_TO_ONE.md checklist item 2).

The published transgene axis is copies per microgram of genomic DNA; the model's
axis is cells. These tests pin the claim that the amplitude bridge is *open* (its
factors are unretained) while the time and cell axes are directly comparable, so
the distinction cannot quietly disappear from the repository.
"""

import unittest
from pathlib import Path

from simulator.cart_sim import kinetics_units as ku
from simulator.cart_sim.params import default_params
from simulator.cart_sim.publication_stats import STATS

ROOT = Path(__file__).resolve().parents[1]


class DenominatorTests(unittest.TestCase):
    def test_time_denominator_stats_are_published_in_days(self):
        self.assertTrue(ku.TIME_DENOMINATOR_STATS)
        for key in ku.TIME_DENOMINATOR_STATS:
            with self.subTest(key=key):
                self.assertIn(key, STATS)
                self.assertIn("day", STATS[key]["unit"])

    def test_cell_denominator_stats_are_published_in_cells(self):
        for key in ku.CELL_DENOMINATOR_STATS:
            with self.subTest(key=key):
                self.assertIn(key, STATS)
                self.assertIn("T cells", STATS[key]["unit"])

    def test_amplitude_bridge_factors_are_all_unretained(self):
        self.assertEqual(len(ku.AMPLITUDE_BRIDGE_FACTORS), 3)
        for factor in ku.AMPLITUDE_BRIDGE_FACTORS:
            with self.subTest(factor=factor["name"]):
                self.assertIn("not supplied by any retained record", factor["status"])
                self.assertTrue(factor["symbol"] and factor["needed_for"])

    def test_amplitude_stays_declared_non_fitted(self):
        self.assertIs(ku.AMPLITUDE_IS_FITTED, False)
        params = default_params()
        for name in ku.NON_FITTED_AMPLITUDE_PARAMS:
            self.assertIn(name, params, f"{name} is no longer a model parameter")

    def test_no_amplitude_statistic_is_claimed_as_comparable(self):
        # If a copies-per-microgram statistic is ever added to the evidence set it
        # must not silently join the directly-comparable lists.
        for key in ku.TIME_DENOMINATOR_STATS + ku.CELL_DENOMINATOR_STATS:
            self.assertNotIn("microgram", STATS[key]["unit"])
            self.assertNotIn("copies", STATS[key]["unit"])


class ConversionTests(unittest.TestCase):
    def test_conversion_is_the_stated_identity(self):
        # 1e6 CAR+ cells/mL, VCN 1, 7.2e6 leukocytes/mL, 6.6e-6 ug DNA per cell
        # -> 47.52 ug gDNA per mL -> 21,043.8 copies per microgram.
        value = ku.transgene_per_microgram_dna(1e6, 1.0, 7.2e6, 6.6e-6)
        self.assertAlmostEqual(value, 1e6 / (7.2e6 * 6.6e-6), places=6)
        # 1e6 CAR+ cells/mL at VCN 1 in blood with 7.2e6 leukocytes/mL at 6.6e-6 ug
        # gDNA per cell: 47.52 ug gDNA per mL, so 1e6/47.52 copies per ug.
        self.assertAlmostEqual(value, 21043.771043771044, places=6)

    def test_conversion_moves_in_the_physically_correct_direction(self):
        base = ku.transgene_per_microgram_dna(1e6, 1.0, 7.2e6, 6.6e-6)
        self.assertLess(ku.transgene_per_microgram_dna(1e6, 1.0, 1.44e7, 6.6e-6), base)
        self.assertGreater(ku.transgene_per_microgram_dna(2e6, 1.0, 7.2e6, 6.6e-6), base)
        self.assertAlmostEqual(
            ku.transgene_per_microgram_dna(1e6, 2.0, 7.2e6, 6.6e-6), 2 * base, places=6
        )

    def test_conversion_rejects_non_positive_inputs(self):
        for args in ((0, 1, 7.2e6, 6.6e-6), (1e6, 0, 7.2e6, 6.6e-6), (1e6, 1, 0, 6.6e-6), (1e6, 1, 7.2e6, 0)):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    ku.transgene_per_microgram_dna(*args)

    def test_bridge_status_names_the_open_bridge(self):
        body = "\n".join(ku.bridge_status())
        self.assertIn("Kinetic unit denominators", body)
        self.assertIn("model amplitude state", body)
        self.assertIn("AMPLITUDE_IS_FITTED = False", body)
        for factor in ku.AMPLITUDE_BRIDGE_FACTORS:
            self.assertIn(factor["symbol"], body)


class DocsStayInSyncTests(unittest.TestCase):
    def test_kinetics_doc_records_the_open_bridge(self):
        text = (ROOT / "docs/KINETICS_SOURCES.md").read_text(encoding="utf-8")
        self.assertIn("Unit denominators", text)
        self.assertIn("not-fitted", text)

    def test_one_to_one_ledger_marks_the_checklist_state(self):
        text = (ROOT / "docs/ONE_TO_ONE.md").read_text(encoding="utf-8")
        self.assertIn("Checklist to get closer to 1:1", text)


if __name__ == "__main__":
    unittest.main()
