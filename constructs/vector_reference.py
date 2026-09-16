"""Audit a historical patent transfer vector without inferring commercial identity."""

import difflib
import json
import re
from pathlib import Path

from .build_car import translate
from .reference import REFERENCES, patent_sequences


def genbank_sequences(path):
    """Read nucleotide records, validating declared length and record termination."""
    records = {}
    text = Path(path).read_text(encoding="utf-8")
    if not text.rstrip().endswith("//"):
        raise ValueError("Unterminated GenBank record")
    for block in text.split("//"):
        if not block.strip():
            continue
        locus = re.search(r"^LOCUS\s+\S+\s+(\d+) bp\b", block, re.M)
        version = re.search(r"^VERSION\s+(\S+)", block, re.M)
        parts = re.split(r"^ORIGIN\s*$", block, flags=re.M)
        if not locus or not version or len(parts) != 2:
            raise ValueError("Invalid nucleotide GenBank record")
        raw = parts[1]
        if re.search(r"[^acgtACGT\d\s]", raw):
            raise ValueError("Invalid nucleotide sequence")
        sequence = re.sub(r"[\d\s]", "", raw).upper()
        accession = version[1]
        if len(sequence) != int(locus[1]) or accession in records:
            raise ValueError("Length mismatch or duplicate accession")
        records[accession] = sequence
    return records


def compare_vector():
    records = genbank_sequences(REFERENCES / "EP2649086_vector.gb")
    vector, car = records["JC053548.1"], records["JC053555.1"]
    current = patent_sequences()["1131"]
    differences = []
    for tag, a, b, c, d in difflib.SequenceMatcher(
        None, current, car, autojunk=False
    ).get_opcodes():
        if tag != "equal":
            differences.append(
                {
                    "kind": tag,
                    "current_slice_0based": [a, b],
                    "historical_slice_0based": [c, d],
                    "current_bases": current[a:b],
                    "historical_bases": car[c:d],
                }
            )
    position = vector.find(car)
    current_position = vector.find(current)
    return {
        "source": "EP2649086 / GenBank JC053548.1 and JC053555.1",
        "scope": "historical patent transfer vector; commercial identity unverified",
        "vector_nt": len(vector),
        "historical_car_nt": len(car),
        "current_car_nt": len(current),
        "historical_car_start_1based": position + 1 if position >= 0 else None,
        "current_car_start_1based": current_position + 1 if current_position >= 0 else None,
        "current_car_end_1based": current_position + len(current)
        if current_position >= 0
        else None,
        "triplet_after_current_car": vector[
            current_position + len(current) : current_position + len(current) + 3
        ]
        if current_position >= 0
        else None,
        "historical_car_complete_codons": len(car) % 3 == 0,
        "same_translation": translate(car) == translate(current) if len(car) % 3 == 0 else None,
        "alignment_differences": differences,
    }


if __name__ == "__main__":
    print(json.dumps(compare_vector(), indent=2))
