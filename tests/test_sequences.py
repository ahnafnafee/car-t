import contextlib
import importlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from constructs import build_car as build
from constructs.verify_sources import check_sources, fasta_records, patent_sequences
from simulator.cart_sim.construct import CONSTRUCT


class SequenceTests(unittest.TestCase):
    def test_independent_sources(self):
        self.assertTrue(all(check_sources().values()))

    def test_generated_files(self):
        root = Path(build.__file__).parent
        aa = next(iter(fasta_records(root / "car_aa.fasta").values()))
        dna = next(iter(fasta_records(root / "car_orf.fasta").values()))
        self.assertEqual(aa, patent_sequences()["1132"])
        self.assertEqual(dna, build.ORF_FULL)
        self.assertEqual(build.translate(dna), aa + "*")
        self.assertFalse(build._hits(dna, build.AVOID_SITES))
        self.assertIsNone(build.BAD_RUN.search(dna))

    def test_import_does_not_rewrite_outputs(self):
        files = [
            Path(build.__file__).parent / name
            for name in (
                "car_aa.fasta",
                "car_orf.fasta",
                "car_report.md",
                "car_patent_cds.fasta",
                "car_patent_protein.fasta",
            )
        ]
        before = [(p.stat().st_mtime_ns, p.read_bytes()) for p in files]
        with contextlib.redirect_stdout(io.StringIO()) as output:
            importlib.reload(build)
        self.assertEqual(output.getvalue(), "")
        self.assertEqual(before, [(p.stat().st_mtime_ns, p.read_bytes()) for p in files])

    def test_exact_patent_outputs(self):
        reference = patent_sequences()
        for name, identifier in (
            ("car_patent_cds.fasta", "1131"),
            ("car_patent_protein.fasta", "1132"),
        ):
            records = fasta_records(build.HERE / name)
            self.assertEqual(len(records), 1)
            self.assertEqual(next(iter(records.values())), reference[identifier])
        self.assertEqual(len(reference["1131"]), 1458)
        self.assertEqual(build.translate(reference["1131"]), reference["1132"])
        self.assertNotEqual(reference["1131"], build.ORF)

    def test_reference_only_preserves_synonymous_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            existing = ("car_aa.fasta", "car_orf.fasta", "car_report.md")
            for name in existing:
                (root / name).write_text("preserve this file", encoding="utf-8")
            before = [(root / name).stat().st_mtime_ns for name in existing]
            with (
                mock.patch.object(build, "HERE", root),
                mock.patch("sys.argv", ["build_car.py", "--reference-only"]),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                build.main()
            self.assertEqual(before, [(root / name).stat().st_mtime_ns for name in existing])
            for name in existing:
                self.assertEqual((root / name).read_text(encoding="utf-8"), "preserve this file")
            self.assertEqual(
                next(iter(fasta_records(root / "car_patent_cds.fasta").values())),
                patent_sequences()["1131"],
            )

    def test_patent_parser_rejects_invalid_records(self):
        reference = patent_sequences()
        valid = f"| 1131 | {reference['1131']} | CDS |\n| 1132 | {reference['1132']} | protein |\n"
        cases = (
            "",
            valid + f"| 1131 | {reference['1131']} | duplicate |\n",
            valid.replace(reference["1131"], "N" + reference["1131"][1:]),
            valid.replace(reference["1132"], reference["1132"][:-1]),
            valid.replace(reference["1131"], reference["1131"] + "*"),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "table.md"
            for text in cases:
                with self.subTest(text=text[:40]):
                    path.write_text(text, encoding="utf-8")
                    with self.assertRaises(ValueError):
                        patent_sequences(path)
            path.write_text(
                valid + "| 1133 | A | unrelated |\n| | B | continuation |\n", encoding="utf-8"
            )
            self.assertEqual(patent_sequences(path), reference)

    def test_metadata_comes_from_sequence(self):
        self.assertEqual(CONSTRUCT["total_aa"], len(build.CAR_AA))
        self.assertEqual(sum(row[1] for row in CONSTRUCT["domains"]), 486)
        self.assertEqual(len(build.itam_motifs()), 3)

    def test_codon_validation(self):
        for bad in ("AT", "ATN"):
            with self.assertRaises(ValueError):
                build.translate(bad)
        for bad in ("", "AX", "M*"):
            with self.assertRaises(ValueError):
                build.codon_opt(bad)
        for protein in ("GGGGGG", "MMMMM", "AAAAAA", "SSSSSS"):
            dna = build.codon_opt(protein)
            self.assertEqual(build.translate(dna), protein)
            self.assertIsNone(build.BAD_RUN.search(dna))
