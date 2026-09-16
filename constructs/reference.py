"""Read the disclosed patent reference without changing its nucleotide spelling."""

import re
from pathlib import Path

REFERENCES = Path(__file__).resolve().parents[1] / "data" / "references"


def patent_sequences(path=None):
    """Parse only the explicitly numbered sequence cells in the retained Table F."""
    path = Path(path) if path is not None else REFERENCES / "US11535869B2_table_f.md"
    sequences = {}
    current = None
    for line in path.read_text(encoding="utf-8").splitlines():
        cols = [part.strip() for part in line.split("|")]
        if len(cols) < 4:
            continue
        identifier, cell = cols[1:3]
        if identifier.isdecimal():
            current = identifier if identifier in ("1131", "1132") else None
            if current:
                if current in sequences:
                    raise ValueError(f"Duplicate sequence {current}")
                sequences[current] = ""
        if current and (identifier == current or not identifier):
            if not re.fullmatch(r"[A-Za-z-]+", cell):
                raise ValueError(f"Invalid sequence cell in {current}: {cell!r}")
            sequences[current] += cell.replace("-", "").upper()
    for identifier, length, alphabet in (
        ("1131", 1458, "ACGT"),
        ("1132", 486, "ACDEFGHIKLMNPQRSTVWY"),
    ):
        sequence = sequences.get(identifier, "")
        if len(sequence) != length or set(sequence) - set(alphabet):
            raise ValueError(f"Invalid or missing sequence {identifier}")
    return sequences
