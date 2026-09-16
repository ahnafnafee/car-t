# CD19 CAR sequence report

The amino-acid reference is transcribed from US11535869B2 Table F,
SEQ ID 1132. Its scFv matches PDB 7URV entity 2. The generated DNA is
a synonymous encoding, not an assertion of the commercial product's CDS.
See the [evidence map](../docs/EVIDENCE.md) for comparison scope.

## Exact patent reference

`car_patent_cds.fasta` reproduces SEQ ID 1131 exactly, without adding a stop
or changing codons. `car_patent_protein.fasta` reproduces SEQ ID 1132.
Both rows were visually checked in the source PDF, pages 70-71
(printed columns 99-102). These are disclosed patent references; the
complete commercial vector and manufacturing specification remain unverified.

## Sequence checks

- Protein: 486 aa
- Coding region: 1458 bp; with terminal stop: 1461 bp
- GC content, including stop: 50.2%
- Translation matches the amino-acid reference; one terminal stop
- No runs of five identical nucleotides in the complete CDS
- Excluded recognition sites: BamHI, NotI, XhoI, SacI, EcoRI, PstI, HindIII, XbaI, KpnI, SmaI, AgeI, AatII

## Domain map

| Domain | Residues (1-based) | Length |
| --- | --- | ---: |
| CD8a leader (signal peptide) | 1–21 | 21 |
| FMC63 VL (light-chain variable) | 22–128 | 107 |
| (G4S)3 linker | 129–143 | 15 |
| FMC63 VH (heavy-chain variable) | 144–263 | 120 |
| CD8a hinge | 264–308 | 45 |
| CD8a transmembrane | 309–332 | 24 |
| 4-1BB cytoplasmic (CD137) | 333–374 | 42 |
| CD3z cytoplasmic | 375–486 | 112 |

## CD3ζ annotation

Three paired YxxL/I motifs are present; motif detection does not test signaling.
The reference differs from canonical UniProt P20963 by Q65K and deletion
of Q101 (canonical numbering).

| Domain start | Paired motif |
| ---: | --- |
| 21 | YNELNLGRREEYDVL |
| 59 | YNELQKDKMAEAYSEI |
| 90 | YQGLSTATKDTYDAL |

## Scope

The outputs contain the CAR coding sequence only. Promoter, WPRE, LTRs,
packaging elements and the remainder of a vector are not assembled.
No sequence comparison establishes biological activity, manufacturing
equivalence, clinical performance or patent clearance.

Sources: [patent Table F](https://patents.google.com/patent/US11535869B2/en),
[PDB 7URV](https://www.rcsb.org/structure/7URV),
[CD247 / P20963](https://www.uniprot.org/uniprotkb/P20963/entry).
