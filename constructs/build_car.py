"""Build a reference CAR coding sequence and verify its sequence invariants.

The 486-aa reference is transcribed from US11535869B2 Table F, SEQ ID 1132.
Only its 242-aa scFv is compared with PDB 7URV. See docs/EVIDENCE.md.
"""

import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

KYMRIAH_486_AA = (
    "MALPVTALLLPLALLLHAARPDIQMTQTTSSLSASLGDRVTISCRASQDISKYLNWYQQK"
    "PDGTVKLLIYHTSRLHSGVPSRFSGSGSGTDYSLTISNLEQEDIATYFCQQGNTLPYTFG"
    "GGTKLEITGGGGSGGGGSGGGGSEVKLQESGPGLVAPSQSLSVTCTVSGVSLPDYGVSWI"
    "RQPPRKGLEWLGVIWGSETTYYNSALKSRLTIIKDNSKSQVFLKMNSLQTDDTAIYYCAK"
    "HYYYGGSYAMDYWGQGTSVTVSSTTTPAPRPPTPAPTIASQPLSLRPEACRPAAGGAVHT"
    "RGLDFACDIYIWAPLAGTCGVLLLSLVITLYCKRGRKKLLYIFKQPFMRPVQTTQEEDGC"
    "SCRFPEEEEGGCELRVKFSRSADAPAYKQGQNQLYNELNLGRREEYDVLDKRRGRDPEMG"
    "GKPRRKNPQEGLYNELQKDKMAEAYSEIGMKGERRRGKGHDGLYQGLSTATKDTYDALHM"
    "QALPPR"
)

# Domain map: (name, start, end), 1-based inclusive reference positions.
DOMAIN_MAP = [
    ("CD8a leader (signal peptide)", 1, 21),
    ("FMC63 VL (light-chain variable)", 22, 128),
    ("(G4S)3 linker", 129, 143),
    ("FMC63 VH (heavy-chain variable)", 144, 263),
    ("CD8a hinge", 264, 308),
    ("CD8a transmembrane", 309, 332),
    ("4-1BB cytoplasmic (CD137)", 333, 374),
    ("CD3z cytoplasmic", 375, 486),
]
# Audit-pinned per-domain lengths (aa); the map must reproduce them exactly.
_AUDIT_DOMAIN_AA = (21, 107, 15, 120, 45, 24, 42, 112)

assert len(KYMRIAH_486_AA) == 486, "verified Kymriah sequence must be 486 aa"
assert sum(_AUDIT_DOMAIN_AA) == 486, "audit domain lengths must total 486"
assert all(e - s + 1 == n for (_, s, e), n in zip(DOMAIN_MAP, _AUDIT_DOMAIN_AA)), (
    "domain map positions disagree with the audited lengths"
)
assert (
    DOMAIN_MAP[0][1] == 1
    and DOMAIN_MAP[-1][2] == 486
    and all(DOMAIN_MAP[i][2] + 1 == DOMAIN_MAP[i + 1][1] for i in range(len(DOMAIN_MAP) - 1))
), "domain map must tile 1..486 in order"


def _dom(name):
    """Slice one domain out of the verified source string by audited position."""
    for nm, s, e in DOMAIN_MAP:
        if nm == name:
            return KYMRIAH_486_AA[s - 1 : e]
    raise KeyError(name)


# ---- domain strings (VL-first build order, as in the verified reference) ----
LEADER = _dom("CD8a leader (signal peptide)")  # human CD8a signal peptide (UniProt P01732)
VL = _dom(
    "FMC63 VL (light-chain variable)"
)  # 107 aa; CDR-L3 context = QQGNTLPYTFGGG (7URV variant)
LINKER = _dom("(G4S)3 linker")  # (G4S)x3, 15 aa (VL -> VH)
VH = _dom(
    "FMC63 VH (heavy-chain variable)"
)  # 120 aa; CDR-H3 context = CAKHYYYGGSYAMDYWGQG (7URV variant)
HINGE = _dom("CD8a hinge")  # CD8a hinge, 45 aa (P01732)
TM = _dom("CD8a transmembrane")  # CD8a TM, 24 aa (P01732)
F1BB = _dom("4-1BB cytoplasmic (CD137)")  # CD137 Q07011 aa 214-255; see docs/EVIDENCE.md
CD3Z = _dom("CD3z cytoplasmic")  # P20963 C-terminus, Kymriah variant: Q->K at domain
#      pos 14 (AYKQGQ) and deletion of canonical Q101.
#      Three paired YxxL/I ITAM motifs remain in the sequence.

CAR_AA = LEADER + VL + LINKER + VH + HINGE + TM + F1BB + CD3Z
assert CAR_AA == KYMRIAH_486_AA, "domain concatenation must reproduce the verified 486-mer exactly"

DOMAINS = [
    ("CD8a leader (signal peptide)", LEADER),
    ("FMC63 VL (light-chain variable)", VL),
    ("(G4S)3 linker", LINKER),
    ("FMC63 VH (heavy-chain variable)", VH),
    ("CD8a hinge", HINGE),
    ("CD8a transmembrane", TM),
    ("4-1BB cytoplasmic (CD137)", F1BB),
    ("CD3z cytoplasmic", CD3Z),
]

# --------------------------------------------------------------------------
# CODON OPTIMIZATION
# --------------------------------------------------------------------------
GENETIC_CODE = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "AGT": "S",
    "AGC": "S",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGG": "R",
    "AGA": "R",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}
# Human-usage-preferred codon per amino acid (balanced GC, avoids rare codons).
CODON = {
    "A": "GCT",
    "R": "CGT",
    "N": "AAC",
    "D": "GAT",
    "C": "TGC",
    "Q": "CAA",
    "E": "GAA",
    "G": "GGT",
    "H": "CAT",
    "I": "ATC",
    "L": "CTG",
    "K": "AAA",
    "M": "ATG",
    "F": "TTT",
    "P": "CCT",
    "S": "AGC",
    "T": "ACC",
    "V": "GTG",
    "W": "TGG",
    "Y": "TAT",
}
# Synonymous alternatives to break homopolymers / avoid internal sites.
# Every multi-codon amino acid is listed (single-codon M and W are not);
# the preferred (CODON) choice comes first.
ALT = {
    "L": ["CTG", "CTC", "CTT", "TTA"],
    "S": ["AGC", "TCC", "TCT", "TCA", "AGT"],
    "A": ["GCT", "GCA", "GCC", "GCG"],
    "V": ["GTG", "GTC", "GTA", "GTT"],
    "E": ["GAA", "GAG"],
    "D": ["GAT", "GAC"],
    "Q": ["CAA", "CAG"],
    "K": ["AAA", "AAG"],
    "N": ["AAC", "AAT"],
    "T": ["ACC", "ACT", "ACA", "ACG"],
    "P": ["CCT", "CCC", "CCA", "CCG"],
    "F": ["TTT", "TTC"],
    "Y": ["TAT", "TAC"],
    "H": ["CAT", "CAC"],
    "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
    "I": ["ATC", "ATT", "ATA"],
    "C": ["TGC", "TGT"],
    "G": ["GGT", "GGC", "GGA", "GGG"],
}

# Sites to keep OUT of the internal CDS (for flexible cloning).
RESTRICTION_SITES = {
    "BamHI": "GGATCC",
    "NotI": "GCGGCCGC",
    "XhoI": "CTCGAG",
    "SacI": "GAGCTC",
    "EcoRI": "GAATTC",
    "PstI": "CTGCAG",
    "HindIII": "AAGCTT",
    "XbaI": "TCTAGA",
    "KpnI": "GGTACC",
    "SmaI": "CCCGGG",
    "AgeI": "ACCGGT",
    "AatII": "GACGTC",
}
AVOID_SITES = list(RESTRICTION_SITES.values())


def _hits(s, sites):
    return [st for st in sites if st in s]


# >=5-nt homopolymer runs are rejected alongside the avoid sites
BAD_RUN = re.compile(r"(?:A{5}|T{5}|G{5}|C{5})")


def codon_opt(aa: str, seed: int = 7) -> str:
    """Choose synonymous codons and remove configured sites and homopolymers.

    Each repair strictly reduces the number of problems. This heuristic does
    not establish improved expression or the manufacturer's nucleotide sequence.
    """
    if not aa or any(residue not in CODON for residue in aa):
        raise ValueError("aa must be a nonempty standard amino-acid sequence")
    r = random.Random(seed)
    out = []
    for i, a in enumerate(aa):
        if a == "M" or a not in ALT:
            out.append(CODON[a])
        else:
            choices = ALT[a]
            p = 0.6 if i % 3 == 0 else 0.5
            c = choices[0] if r.random() < p else r.choice(choices)
            out.append(c)

    def n_problems(seq):
        return sum(sum(seq.startswith(st, i) for i in range(len(seq))) for st in AVOID_SITES) + len(
            BAD_RUN.findall(seq)
        )

    for _ in range(10000):
        seq = "".join(out)
        n_bad = n_problems(seq)
        if n_bad == 0:
            break
        run = BAD_RUN.search(seq)
        pos = run.start() if run else min(seq.find(st) for st in _hits(seq, AVOID_SITES))
        c0 = pos // 3
        fixed = False
        # codons overlapping the problem first, then immediate neighbors
        for ci in (c0, c0 + 1, c0 + 2, c0 - 1, c0 + 3):
            if not (0 <= ci < len(aa)):
                continue
            for cand in ALT.get(aa[ci], [CODON[aa[ci]]]):
                if cand == out[ci]:
                    continue
                tseq = "".join(out[:ci] + [cand] + out[ci + 1 :])
                if n_problems(tseq) < n_bad:
                    out[ci] = cand
                    fixed = True
                    break
            if fixed:
                break
        if not fixed:
            raise RuntimeError(
                f"codon repair stuck: no synonymous substitution reduces the "
                f"{n_bad} remaining site/run problems (first near nt {pos})"
            )

    seq = "".join(out)
    if n_problems(seq) or translate(seq) != aa:
        raise RuntimeError("synonymous repair failed validation")
    return seq


def translate(s):
    if len(s) % 3 or any(base not in "ACGT" for base in s):
        raise ValueError("DNA must contain complete A/C/G/T codons")
    return "".join(GENETIC_CODE[s[i : i + 3]] for i in range(0, len(s), 3))


ORF = codon_opt(CAR_AA)
STOP_CODON = "TAA"  # single stop after the last codon
ORF_FULL = ORF + STOP_CODON

# --- verification ---
assert translate(ORF) == CAR_AA, "translation mismatch!"
assert "*" not in translate(ORF), "internal stop codon present!"
assert not BAD_RUN.search(ORF_FULL), "homopolymer in complete CDS"
assert not _hits(ORF, AVOID_SITES), f"internal site present: {_hits(ORF, AVOID_SITES)}"


def itam_motifs(sequence=CD3Z):
    """Return positions and sequences matching paired YxxL/I ITAM motifs."""
    return [(m.start() + 1, m.group()) for m in re.finditer(r"Y..[LI].{6,8}Y..[LI]", sequence)]


def validate():
    """Run build checks even when Python assertions are disabled."""
    lengths = tuple(end - start + 1 for _, start, end in DOMAIN_MAP)
    if lengths != _AUDIT_DOMAIN_AA or CAR_AA != KYMRIAH_486_AA:
        raise ValueError("domain reconstruction differs from reference")
    if len(CAR_AA) != 486 or translate(ORF_FULL) != CAR_AA + "*":
        raise ValueError("CDS translation differs from reference")
    if _hits(ORF_FULL, AVOID_SITES) or BAD_RUN.search(ORF_FULL):
        raise ValueError("complete CDS contains an excluded motif")
    if len(itam_motifs()) != 3:
        raise ValueError("expected three paired CD3z ITAM motifs")


def write_fasta(path, header, sequence):
    lines = [">" + " ".join(header.split())]
    lines.extend(sequence[i : i + 60] for i in range(0, len(sequence), 60))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    import argparse

    if __package__:
        from .reference import patent_sequences
    else:
        from reference import patent_sequences

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reference-only",
        action="store_true",
        help="write the disclosed patent protein and CDS without synonymous recoding",
    )
    args = parser.parse_args()
    validate()
    reference = patent_sequences()
    if reference["1132"] != CAR_AA or translate(reference["1131"]) != CAR_AA:
        raise ValueError("Patent CDS/protein disagrees with the assembled reference")
    write_fasta(
        HERE / "car_patent_cds.fasta",
        "US11535869B2 Table F SEQ ID 1131 | exact disclosed CDS | 1458 nt | no stop added",
        reference["1131"],
    )
    write_fasta(
        HERE / "car_patent_protein.fasta",
        "US11535869B2 Table F SEQ ID 1132 | exact disclosed protein | 486 aa",
        reference["1132"],
    )
    if args.reference_only:
        print("Patent reference written: exact 1458-nt CDS and 486-aa protein")
        return
    write_fasta(
        HERE / "car_aa.fasta",
        "CD19 CAR reference | US11535869B2 Table F SEQ ID 1132 | 486 aa",
        CAR_AA,
    )
    write_fasta(
        HERE / "car_orf.fasta",
        "Synonymous CDS for CD19 CAR reference | 1461 bp including TAA",
        ORF_FULL,
    )
    gc = 100 * sum(base in "GC" for base in ORF_FULL) / len(ORF_FULL)
    lines = [
        "# CD19 CAR sequence report",
        "",
        "The amino-acid reference is transcribed from US11535869B2 Table F,",
        "SEQ ID 1132. Its scFv matches PDB 7URV entity 2. The generated DNA is",
        "a synonymous encoding, not an assertion of the commercial product's CDS.",
        "See the [evidence map](../docs/EVIDENCE.md) for comparison scope.",
        "",
        "## Exact patent reference",
        "",
        "`car_patent_cds.fasta` reproduces SEQ ID 1131 exactly, without adding a stop",
        "or changing codons. `car_patent_protein.fasta` reproduces SEQ ID 1132.",
        "Both rows were visually checked in the source PDF, pages 70-71",
        "(printed columns 99-102). These are disclosed patent references; the",
        "complete commercial vector and manufacturing specification remain unverified.",
        "",
        "## Sequence checks",
        "",
        f"- Protein: {len(CAR_AA)} aa",
        f"- Coding region: {len(ORF)} bp; with terminal stop: {len(ORF_FULL)} bp",
        f"- GC content, including stop: {gc:.1f}%",
        "- Translation matches the amino-acid reference; one terminal stop",
        "- No runs of five identical nucleotides in the complete CDS",
        "- Excluded recognition sites: " + ", ".join(RESTRICTION_SITES),
        "",
        "## Domain map",
        "",
        "| Domain | Residues (1-based) | Length |",
        "| --- | --- | ---: |",
    ]
    lines.extend(
        f"| {name} | {start}–{end} | {end - start + 1} |" for name, start, end in DOMAIN_MAP
    )
    lines += [
        "",
        "## CD3ζ annotation",
        "",
        "Three paired YxxL/I motifs are present; motif detection does not test signaling.",
        "The reference differs from canonical UniProt P20963 by Q65K and deletion",
        "of Q101 (canonical numbering).",
        "",
        "| Domain start | Paired motif |",
        "| ---: | --- |",
    ]
    lines.extend(f"| {pos} | {motif} |" for pos, motif in itam_motifs())
    lines += [
        "",
        "## Scope",
        "",
        "The outputs contain the CAR coding sequence only. Promoter, WPRE, LTRs,",
        "packaging elements and the remainder of a vector are not assembled.",
        "No sequence comparison establishes biological activity, manufacturing",
        "equivalence, clinical performance or patent clearance.",
        "",
        "Sources: [patent Table F](https://patents.google.com/patent/US11535869B2/en),",
        "[PDB 7URV](https://www.rcsb.org/structure/7URV),",
        "[CD247 / P20963](https://www.uniprot.org/uniprotkb/P20963/entry).",
        "",
    ]
    (HERE / "car_report.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Sequence checks passed: {len(CAR_AA)} aa, {len(ORF_FULL)} bp, GC {gc:.1f}%")
    print(f"Outputs: {HERE}")


if __name__ == "__main__":
    main()
