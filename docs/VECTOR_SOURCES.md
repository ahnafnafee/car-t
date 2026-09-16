# Patent vector sequence recovery

The literature search recovered a complete historical transfer-vector record,
which narrows the earlier sequence gap substantially. GenBank **JC053548.1** is
the 9,174-nt sequence 1 of EP2649086; the patent's Table 5 identifies sequence 1
as pELPS-CD19-BBz. The associated **JC053555.1** is the 1,459-nt sequence 8.
Both versioned nucleotide records were downloaded on 2026-09-16 and retained
unchanged in [`EP2649086_vector.gb`](../data/references/EP2649086_vector.gb).
[NCBI retrieval](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JC053548.1,JC053555.1&rettype=gb&retmode=text),
[EP2649086, Table 5](https://patents.google.com/patent/EP2649086B1/en).

## Reproducible comparison

Run `python -m constructs.vector_reference`. Coordinates below are 1-based and
refer to the deposited orientation, without circular rotation or reverse complementation.

| Comparison | Computed result |
| --- | --- |
| Complete deposited transfer-vector length | 9,174 nt |
| Repository's US11535869B2 sequence 1131 within JC053548.1 | Exact match at 6,391–7,848 |
| Triplet immediately after that coding region | TAA, positions 7,849–7,851 |
| EP2649086 sequence 8 within sequence 1 | Exact match at 6,391–7,849 |
| Sequence 8 versus the repository's 1,458-nt reference | Identical prefix plus one trailing T |

These are results computed from the retained records, not an alignment inferred
from a diagram. The extra T in sequence 8 is the first nucleotide of the following
TAA in sequence 1. Translating the 1,459-nt entry as a complete CDS would therefore
be incorrect. The source record remains unchanged; the comparison does not silently
trim it, recode it or substitute a guessed vector backbone.

Table 5 also names the RSV U3, HIV repeats, partial Gag/Pol, cPPT, EF1-alpha promoter
and WPRE entries. This establishes a source for the historical vector beyond a
CAR-only sequence. It does not show that every commercial manufacturing version
uses an identical complete transfer plasmid, nor equate that plasmid with the
integrated sequence in a patient's cells.
[US20150093822A1, Table 5 and accompanying early clinical example](https://patents.google.com/patent/US20150093822A1/en).

## Excluded substitute

Another patent points to GenBank MP123113.1 as a pELPS source. Its actual GenBank
annotation identifies a 9,714-nt pELPS-hFVIII-C2-BBz-T2A-mCherry construct from
EP3443076, not the CD19 vector. It was not substituted for the target merely
because it shares the pELPS name.
[NCBI MP123113.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=MP123113.1&rettype=gb&retmode=text).

The remaining sequence question is commercial version identity, not whether a
full historical patent transfer-vector sequence can be recovered. The retrieved
record closes the latter gap and provides a concrete reference for further
comparisons; laboratory authentication and commercial comparability are separate.
