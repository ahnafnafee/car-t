import tempfile
import unittest
from pathlib import Path

from constructs.vector_reference import compare_vector, genbank_sequences


class VectorReferenceTests(unittest.TestCase):
    def test_historical_vector_contains_current_cds(self):
        comparison = compare_vector()
        self.assertEqual(comparison["vector_nt"], 9174)
        self.assertEqual(comparison["current_car_start_1based"], 6391)
        self.assertEqual(comparison["current_car_end_1based"], 7848)
        self.assertEqual(comparison["triplet_after_current_car"], "TAA")
        self.assertEqual(comparison["historical_car_nt"], 1459)
        self.assertFalse(comparison["historical_car_complete_codons"])
        self.assertIsNone(comparison["same_translation"])
        self.assertEqual(len(comparison["alignment_differences"]), 1)
        difference = comparison["alignment_differences"][0]
        self.assertEqual(difference["current_slice_0based"], [1458, 1458])
        self.assertEqual(difference["historical_bases"], "T")

    def test_genbank_validation(self):
        valid = "LOCUS       TEST 3 bp DNA\nVERSION     TEST.1\nORIGIN\n 1 atg\n//\n"
        invalid = (
            valid.replace("3 bp", "4 bp"),
            valid.replace("atg", "atn"),
            valid.replace("//", ""),
            valid + valid,
            "",
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.gb"
            path.write_text(valid, encoding="utf-8")
            self.assertEqual(genbank_sequences(path), {"TEST.1": "ATG"})
            for text in invalid:
                with self.subTest(text=text):
                    path.write_text(text, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        genbank_sequences(path)
