"""Tests for simulator/cart_sim/version_anchor.py (docs/ONE_TO_ONE.md checklist item 3).

A constant without a record version is not a 1:1 anchor: the same number can be
true in a 2017 label, a 2018 assessment report and a 2025 revision, and only the
version makes the claim checkable. These tests pin every anchor to the exact bytes
of the retained record it cites.
"""

import re
import unittest
from pathlib import Path

from simulator.cart_sim.version_anchor import ANCHORS, anchor_lines

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = ("id", "role", "source", "url", "file", "quote", "version", "caveat")


class VersionAnchorTests(unittest.TestCase):
    def test_anchors_are_complete(self):
        self.assertGreaterEqual(len(ANCHORS), 10)
        ids = [a["id"] for a in ANCHORS]
        self.assertEqual(len(ids), len(set(ids)), "anchor ids must be unique")
        for anchor in ANCHORS:
            with self.subTest(anchor=anchor["id"]):
                for field in REQUIRED:
                    self.assertIn(field, anchor)
                    self.assertTrue(str(anchor[field]).strip())
                self.assertTrue(anchor["url"].startswith("https://"))

    def test_quotes_are_byte_exact_in_the_retained_records(self):
        for anchor in ANCHORS:
            with self.subTest(anchor=anchor["id"]):
                path = ROOT / anchor["file"]
                self.assertTrue(path.is_file(), f"missing retained file {anchor['file']}")
                self.assertIn(anchor["quote"], path.read_text(encoding="utf-8"))

    def test_every_regulatory_record_version_is_named(self):
        versions = {anchor["id"]: anchor["version"] for anchor in ANCHORS}
        self.assertEqual(versions["us_pi_kymriah_revised_2025_06"], "2025-06")
        self.assertEqual(versions["us_bla_125646_0_sbra_2017_08_30"], "2017-08-30")
        self.assertEqual(versions["us_bla_125646_76_sbra_2018_04_13"], "2018-04-13")
        self.assertEqual(versions["eu_ema_chmp_assessment_2018_06_28"], "2018-06-28")

    def test_the_eu_record_is_described_as_the_assessment_report(self):
        # The retained EU record is the CHMP assessment report; it carries neither
        # the 'B/2202' product number nor an August-2018 date, so no anchor may
        # claim them from it.
        text = (ROOT / "data/references/ema_kymriah_epar_2018.txt").read_text(
            encoding="utf-8", errors="replace"
        )
        self.assertNotIn("B/2202", text)
        self.assertNotIn("23 August 2018", text)
        eu = [a for a in ANCHORS if a["file"].endswith("ema_kymriah_epar_2018.txt")]
        self.assertTrue(eu)
        for anchor in eu:
            self.assertIn("EMA/", anchor["source"])

    def test_the_two_release_dose_criteria_agree_across_records(self):
        # lot_criteria.dose_interval implements the disclosed US intervals; the EU
        # assessment report states the same protocol intervals and, separately, a
        # stricter non-release floor for patients above 50 kg.
        from simulator.cart_sim.lot_criteria import dose_interval

        eu_text = (ROOT / "data/references/ema_kymriah_epar_2018.txt").read_text(
            encoding="utf-8", errors="replace"
        )
        self.assertIn("0.2 to 5.0 x 106 CAR positive viable T cells/kg body weight", eu_text)
        self.assertIn("0.1 to 2.5 x 108 CAR positive viable T cells (non weight based)", eu_text)
        self.assertIn("0.6 to 6.0 x 10 8 CAR positive viable T cells", eu_text)
        self.assertIn("0.2×106 CAR-\npositive viable T-cells per kg or 1.0×108 CAR-positive viable T-cells", eu_text)

        # <=50 kg: identical per-kg rule (0.2-5.0e6 per kg).
        self.assertEqual(dose_interval("B-ALL", weight_kg=30.0), (0.2e6 * 30.0, 5.0e6 * 30.0))
        # >50 kg: identical protocol interval (0.1-2.5e8).
        self.assertEqual(dose_interval("B-ALL", weight_kg=70.0), (1e7, 2.5e8))
        # DLBCL: the EU range matches the US interval.
        self.assertEqual(dose_interval("DLBCL"), (6e7, 6e8))
        # The EU record's non-release floor (1.0e8) is above the interval's lower
        # bound (1e7), so dose_interval is the more permissive of the two rules.
        self.assertGreater(1.0e8, dose_interval("B-ALL", weight_kg=70.0)[0])

    def test_report_lines_name_versions_and_caveats(self):
        lines = anchor_lines()
        body = "\n".join(lines)
        self.assertIn("Version anchors", body)
        for anchor in ANCHORS:
            with self.subTest(anchor=anchor["id"]):
                self.assertIn(anchor["id"], body)
                self.assertIn(f"version {anchor['version']}", body)
        self.assertGreaterEqual(len([ln for ln in lines if ln.strip().startswith("caveat:")]), len(ANCHORS))

    def test_caveat_quotes_that_look_like_citations_are_verbatim(self):
        for anchor in ANCHORS:
            quoted = re.findall(r"'([^']{25,})'", anchor["caveat"])
            for snippet in quoted:
                with self.subTest(anchor=anchor["id"], snippet=snippet[:40]):
                    path = ROOT / anchor["file"]
                    text = path.read_text(encoding="utf-8", errors="replace")
                    self.assertIn(snippet, text)


if __name__ == "__main__":
    unittest.main()
