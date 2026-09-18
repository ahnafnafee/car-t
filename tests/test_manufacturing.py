import math
import unittest

from simulator.cart_sim import ACADEMIC_CTL019, assess_lot, dose_interval, manufacture, run_cohort


class ManufacturingTests(unittest.TestCase):
    def test_viability_applied_once_to_recovered_total(self):
        lot = manufacture(
            apheresis_wbc=1000,
            t_cell_frac=0.5,
            net_yield=2,
            te=0.25,
            viability=0.8,
            dose_target=1000,
        )
        self.assertEqual(lot["product_total_cells"], 1000)
        self.assertEqual(lot["product_viable_cells"], 800)
        self.assertEqual(lot["dose_total_cells"], 1000)
        self.assertEqual(lot["dose_viable_car_cells"], 200)
        self.assertIsNone(lot["VCN"])

    def test_target_caps_viable_car_not_total_cells(self):
        lot = manufacture(
            apheresis_wbc=1000,
            t_cell_frac=0.5,
            net_yield=2,
            te=0.25,
            viability=0.8,
            dose_target=100,
        )
        self.assertEqual(lot["dose_total_cells"], 500)
        self.assertEqual(lot["dose_viable_cells"], 400)
        self.assertEqual(lot["dose_viable_car_cells"], 100)
        self.assertEqual(lot["dose_CARplus_cells"], 100)

    def test_cap_boundary_is_not_lost_to_roundoff(self):
        for target in (6e7, 6e8):
            lot = manufacture(
                net_yield=1, dose_target=target, te=0.57, viability=0.83,
                sterility=True, mycoplasma=True,
            )
            self.assertEqual(lot["dose_viable_car_cells"], target)
            self.assertEqual(lot["source_assessment"]["status"], "meets_disclosed_criteria")
        for values in ({"te": True}, {"vcn": "2"}, {"apheresis_wbc": 1e308, "net_yield": 1e308}):
            with self.assertRaises(ValueError):
                manufacture(**values)

    def test_zero_inputs_produce_no_dose(self):
        for name in ("te", "viability", "net_yield", "t_cell_frac", "apheresis_wbc", "dose_target"):
            lot = manufacture(**{name: 0})
            self.assertEqual(lot["dose_viable_car_cells"], 0)
            self.assertEqual(lot["dose_total_cells"], 0)

    def test_weight_boundary_and_indication_ranges(self):
        self.assertEqual(dose_interval("DLBCL"), (6e7, 6e8))
        self.assertEqual(dose_interval("B-ALL", 30), (6e6, 1.5e8))
        self.assertEqual(dose_interval("B-ALL", 50), (1e7, 2.5e8))
        self.assertEqual(dose_interval("B-ALL", 50.1), (1e7, 2.5e8))
        for weight in (None, 0, -1, True, math.nan, math.inf):
            with self.assertRaises(ValueError):
                dose_interval("B-ALL", weight)
        with self.assertRaises(ValueError):
            dose_interval("unknown")

    def test_commercial_boundaries_do_not_authorize_release(self):
        clean = {"sterility_negative": True, "mycoplasma_negative": True}
        for dose in (6e7, 6e8):
            result = assess_lot({"viability": 0.8, "dose_viable_car_cells": dose, **clean})
            self.assertEqual(result["status"], "meets_disclosed_criteria")
            self.assertTrue(result["unreported_specifications"])
            self.assertFalse(result["commercial_release_established"])
        for viability, dose in ((0.799, 6e7), (0.8, 6e7 - 1), (0.8, 6e8 + 1)):
            self.assertEqual(
                assess_lot({"viability": viability, "dose_viable_car_cells": dose, **clean})["status"],
                "fails_disclosed_criteria",
            )
        # Unredacted SBRA qualitative requirements are enforced when supplied.
        self.assertEqual(
            assess_lot({"viability": 0.8, "dose_viable_car_cells": 6e7,
                        "sterility_negative": False, "mycoplasma_negative": True})["status"],
            "fails_disclosed_criteria",
        )
        self.assertEqual(
            assess_lot({"viability": 0.8, "dose_viable_car_cells": 6e7})["missing"],
            ["sterility_negative", "mycoplasma_negative"],
        )

    def test_unknown_and_invalid_measurements(self):
        result = assess_lot({"viability": 0.9})
        self.assertEqual(result["status"], "incomplete")
        self.assertEqual(
            result["missing"], ["dose_viable_car_cells", "sterility_negative", "mycoplasma_negative"]
        )
        for value in (math.nan, math.inf, -0.1, 1.1, True, "0.9"):
            with self.assertRaises(ValueError):
                assess_lot({"viability": value})
        with self.assertRaises(ValueError):
            assess_lot({}, "typo")

    def test_academic_profile_is_separate_and_requires_all_assays(self):
        measurements = {
            "viability": 0.7,
            "cd3_fraction": 0.8,
            "residual_beads_per_3m": 100,
            "endotoxin_eu_ml": 3.5,
            "bsa_ug_ml": 1,
            "vsvg_copies_ug_dna": 50,
            "car_fraction": 0.02,
            "vcn_copies_cell": 4,
            "mycoplasma_negative": True,
            "bacterial_negative": True,
            "fungal_negative": True,
        }
        result = assess_lot(measurements, ACADEMIC_CTL019)
        self.assertEqual(result["status"], "meets_disclosed_criteria")
        self.assertFalse(result["commercial_release_established"])
        self.assertEqual(assess_lot({"viability": 0.7}, ACADEMIC_CTL019)["status"], "incomplete")
        for key, value in (
            ("vcn_copies_cell", 20),
            ("vcn_copies_cell", 0.019),
            ("residual_beads_per_3m", 101),
            ("fungal_negative", False),
        ):
            bad = dict(measurements, **{key: value})
            self.assertIn(key, assess_lot(bad, ACADEMIC_CTL019)["failed"])
        with self.assertRaises(ValueError):
            assess_lot({"fungal_negative": "negative"}, ACADEMIC_CTL019)

    def test_cohort_uses_physical_dose_even_when_partial_criteria_fail(self):
        for engine in ("ode", "micro"):
            result = run_cohort(n=2, engine=engine, lot_params={"viability": 0.79})
            for patient in result["patients"]:
                lot = patient["manufacturing"]
                self.assertEqual(patient["params"]["E0"], lot["dose_viable_car_cells"])
                self.assertIn("viability", lot["source_assessment"]["failed"])
                self.assertIsNone(lot["VCN"])
            self.assertEqual(result["lot_assessment_counts"]["fails_disclosed_criteria"], 2)

    def test_cohort_does_not_invent_cells_for_empty_lot(self):
        result = run_cohort(n=2, engine="ode", lot_params={"net_yield": 0})
        self.assertTrue(all(p["params"]["E0"] == 0 for p in result["patients"]))
        self.assertEqual(result["ORR"], 0)

    def test_all_weight_scenario_and_input_validation(self):
        result = run_cohort(n=1, engine="ode", indication="B-ALL", weight_kg=20)
        self.assertEqual(result["weight_kg"], 20)
        self.assertEqual(
            result["patients"][0]["manufacturing"]["dose_target_viable_car_cells"], 2e7
        )
        with self.assertRaises(ValueError):
            run_cohort(n=1, lot_params={"typo": 1})
