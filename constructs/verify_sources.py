"""Compare the reference and generated CDS with independently stored source records."""

from . import build_car as build
from .reference import REFERENCES, patent_sequences


def fasta_records(path):
    records = {}
    name = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(">"):
            name = line[1:]
            records[name] = ""
        elif line.strip():
            if name is None:
                raise ValueError(f"FASTA sequence before header: {path}")
            records[name] += line.strip()
    return records


def check_sources():
    build.validate()
    patent = patent_sequences()
    checks = {
        "patent protein (PDF-reviewed Table F, 1132)": build.CAR_AA == patent["1132"],
        "patent CDS translation (PDF-reviewed Table F, 1131)": build.translate(patent["1131"])
        == build.CAR_AA,
    }
    for name, identifier in (
        ("car_patent_cds.fasta", "1131"),
        ("car_patent_protein.fasta", "1132"),
    ):
        artifact = next(iter(fasta_records(build.HERE / name).values()))
        checks[f"exact reference artifact: {name}"] = artifact == patent[identifier]
    pdb = fasta_records(REFERENCES / "7URV.fasta")
    scfv = next(seq for name, seq in pdb.items() if name.startswith("7URV_2|"))
    checks["7URV entity 2 = CAR residues 22-263"] = scfv == build.CAR_AA[21:263]
    uniprot = {
        name: next(iter(fasta_records(REFERENCES / f"{name}.fasta").values()))
        for name in ("P01732", "Q07011", "P20963")
    }
    cd8 = uniprot["P01732"]
    checks["CD8A reference segment 1-21"] = build.LEADER == cd8[:21]
    checks["CD8A hinge/TM reference segments"] = build.HINGE + build.TM in cd8
    checks["CD137 residues 214-255"] = build.F1BB == uniprot["Q07011"][213:255]
    canonical = uniprot["P20963"]
    # Canonical CD247 residues 52-164 with Q65K and deletion of Q101.
    expected = canonical[51:64] + "K" + canonical[65:100] + canonical[101:]
    checks["CD247 Q65K and deletion Q101"] = build.CD3Z == expected
    checks["three paired CD3z ITAM motifs"] = len(build.itam_motifs()) == 3
    for name, ok in checks.items():
        if not ok:
            raise ValueError(f"Source comparison failed: {name}")
    return checks


def main():
    for name in check_sources():
        print(f"MATCH: {name}")
    patent = patent_sequences()
    differences = sum(a != b for a, b in zip(build.ORF, patent["1131"]))
    print(f"Generated CDS vs patent CDS: {differences} nucleotide substitutions; same translation")


if __name__ == "__main__":
    main()
