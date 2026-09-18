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

## Second-pass additions (checked 2026-09-17)

A second research pass retrieved the complete EP2649086 nucleotide deposit, the
US11535869B2 Table F records for the three approved CD19 CARs, the EMA EPAR
vector sections, and the patent-cache files behind the false leads below. Files
named in these subsections are retained in
[`../data/references/`](../data/references/README.md) with SHA-256 entries;
verification scripts and per-file provenance are recorded in
`.private/agent_drafts/vector/manifest.md`. Coordinates are 1-based in the
deposited orientation, checked 2026-09-17.

### Element map of the deposited vector

The EP2649086 nucleotide deposit (GenBank JC053548.1–JC053574.1, 20 records) was
retrieved on 2026-09-16 and retained unchanged in
`EP2649086_all_sequences.gb`. Patent Table 5 (US9328156B2, cached verbatim
extract in `us9328156B2_table5.txt`) names sequences 1–24: sequence 1 is the
pELPS-CD19-BBZ transfer vector, sequences 2–11 are the backbone elements,
sequence 12 is the CD19-BBζeta CAR amino acid sequence, sequences 13–18 are the
six CAR component nucleic acids (CD8 leader, anti-CD19 scFv, CD8 hinge, CD8
transmembrane, 4-1BB, CD3ζ) and sequences 19–24 are the six amino-acid
counterparts. Sequences 25–27 are deposited nucleotide records with no Table 5
entry.

All 20 deposited records were re-verified against JC053548.1 on 2026-09-17
(exact substring test, zero mismatches; coordinates 1-based, deposited
orientation). Sixteen — sequences 1–11 and 13–18 — occur in the vector at:

| Element (Table 5 name) | Record | Vector position | Length |
| --- | --- | --- | --- |
| RSV U3 | JC053549.1 (seq 2) | 2,840–3,067 | 228 nt |
| HIV R repeat | JC053550.1 (seq 3) | 3,068–3,165 | 98 nt |
| HIV U5 repeat (5′) | JC053551.1 (seq 4) | 3,166–3,250 | 85 nt |
| Partial Gag/Pol | JC053552.1 (seq 5) | 3,257–4,633 | 1,377 nt |
| cPPT | JC053553.1 (seq 6) | 4,638–5,184 | 547 nt |
| EF1α promoter | JC053554.1 (seq 7) | 5,201–6,378 | 1,178 nt |
| CD19-BBζeta CAR | JC053555.1 (seq 8) | 6,391–7,849 | 1,459 nt |
| Hu Woodchuck PRE (WPRE) | JC053556.1 (seq 9) | 7,859–8,449 | 591 nt |
| R repeat (3′) | JC053557.1 (seq 10) | 8,586–8,683 | 98 nt |
| U5 repeat (3′) | JC053558.1 (seq 11) | 8,684–8,767 | 84 nt |
| CD8 leader | JC053560.1 (seq 13) | 6,391–6,453 | 63 nt |
| Anti-CD19 scFv | JC053561.1 (seq 14) | 6,454–7,179 | 726 nt |
| CD8 hinge | JC053562.1 (seq 15) | 7,180–7,314 | 135 nt |
| CD8 transmembrane | JC053563.1 (seq 16) | 7,315–7,386 | 72 nt |
| 4-1BB | JC053564.1 (seq 17) | 7,387–7,512 | 126 nt |
| CD3ζ | JC053565.1 (seq 18) | 7,513–7,848 | 336 nt |

The 5′ LTR is therefore RSV U3 + HIV R + HIV U5 (2,840–3,250); the 3′ LTR is the
same 98-nt R block (8,586–8,683) plus an 84-nt U5 that is the 5′ U5 with its
final nucleotide removed (8,684–8,767), followed by a Moloney-type U3
(8,768–9,174). Between the CAR stop codon TAA (7,849–7,851) and the WPRE there
is a 6-nt linker GTCGAC (7,852–7,857). Downstream of the WPRE the vector carries
an EcoRI–SacI–KpnI cloning site with a poly-tract (8,450–8,529).

Sequences 25–27 (JC053572.1, JC053573.1, JC053574.1; 22, 22 and 15 nt) do not
occur in JC053548.1 in either strand orientation, including the
MCS/3′-LTR window. The US publication of the same family identifies them as
assay reagents rather than vector elements: the specification's VCN normalization
reaction uses "a primer/probe combination specific for non-transcribed genomic
sequence upstream of the CDKN1A gene (GENEBANK: Z85996) (sense primer:
GAAAGCTGACTGCCCCTATTTG; SEQ ID NO. 25, antisense primer:
GAGAGGAAGTGCTGGGAACAAT; SEQ ID NO. 26, probe: VIC-CTC CCC AGT CTC TTT; SEQ ID
NO. 27)" — all three printed sequences match the deposited records exactly (the
probe is printed with inter-triplet spaces). [US20150093822A1,
description](https://patents.google.com/patent/US20150093822A1/en); cached
310-kB full-text scrape retained in `us20150093822_patent_desc.txt`.

The consolidated multi-FASTA `ep2649086_elements.fa` and the per-record files in
`ep2649086_seqs/` were regenerated from the GenBank batch on 2026-09-16/17; every
one of the 20 sequences in them is byte-identical to the corresponding GenBank
record.

### WPRE element

The WPRE carried by the vector is a 592-nt core, not the intact canonical
element. JC053548.1 positions 7,858–8,449 (592 nt) are an exact match (zero
mismatches, verified 2026-09-17) to woodchuck hepatitis B virus genome
J04514.1 positions 1,093–1,684. The deposited sequence 9 (JC053556.1, 591 nt)
is the same span without its leading A: JC053548.1[7,859–8,449] =
J04514.1[1,094–1,684]. The canonical WPRE used in the source construction is
726 nt (J04514.1[1,093–1,818]; cf. US6136597); comparing that full element with
the vector window 7,858–8,583 shows agreement through position 592 followed by
97 mismatches over positions 593–726, so the intact 726-nt element is not
present in the vector. [NCBI J04514.1](https://www.ncbi.nlm.nih.gov/nuccore/J04514.1).
Retained records: `wpre_core_592.fa`, `wpre_seq9_591.fa`,
`wpre_extended_726nt_J04514_1093_1818.fa`, `J04514.gb`.

### Commercial plasmid identity (EMA EPAR)

The EPAR identifies the commercial vector system by plasmid name but does not
publish a complete commercial transfer-plasmid sequence. The vector system
"comprised of four plasmid constructs": pRKHVmuEC19, "the transfer plasmid,
containing the CTL019 vector genome"; pRKHSYNGP, "the HIV-1 Gag/Pol packaging
plasmid"; pRKHG, "the envelope packaging plasmid"; and pRKHREV, "the Rev
packaging plasmid". "The majority (approximately 85%) of the native HIV-1
sequence has been removed to produce a replication-defective lentiviral vector
system." [EMA EPAR, printed p. 17](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)
(retained full document: `ema_kymriah_epar_2018.pdf` with text layer
`ema_kymriah_epar_2018.txt`). The academic/patent-era record
JC053548.1 is therefore the closest complete authenticated sequence, and the
commercial pRKHVmuEC19 differs from it by at least the ~85% removal of native
HIV-1 sequence described for the commercial system; which parts were removed is
not stated in public sources.

### Integrated vector in patient cells

EPAR Figure 2 ("Genetic structure of the integrated vector", printed p. 18)
shows the element order in the integrated vector as SIN-LTR (ΔU3) → RRE → cPPT
→ WPRE → CTL019 (labelled 1,460 nt) → SIN-LTR (ΔU3). The WPRE is drawn upstream
of the CAR block, the reverse of the academic vector, where the WPRE lies
downstream of the CAR. The figure is a rasterized schematic; the reading was
made by vision transcription of a 3.0× render of the printed page on
2026-09-17 (retained renders: `epar_figure2_integrated_vector_p17.png`, and the
Oncologist-reprinted figure `oncologist_fig2_p3.png`), so the element order is stated at medium-to-
high confidence and the "1,460 nt" label is as printed. [EMA EPAR, printed p.
18](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf);
[Oncologist 2020;25:e321, Figure 2](https://academic.oup.com/oncolo/article/25/2/e321/6443357).

Three different CAR-block lengths coexist in the public record and are not
reconciled:

| Length | Source | Meaning |
| --- | --- | --- |
| 1,458 nt | US11535869B2 SEQ ID NO: 1131 | tisagenlecleucel CAR coding sequence (486-aa protein) |
| 1,459 nt | EP2649086 sequence 8 / JC053555.1 | deposited CAR entry; the extra 3′ T is the first base of the following TAA stop |
| 1,460 nt | EPAR Figure 2 label | integrated-vector CAR block as drawn |

Integration-site characterization (LISA, Reports 1620234 and 1620234a, both
non-GLP) was performed on tisagenlecleucel manufacturing samples from 6
paediatric ALL patients (CCTL019B2202), 6 DLBCL patients (CCTL019C2201) and 2
healthy volunteers. In all analysed products "a high degree of polyclonality
was observed and there was no evidence for preferential integration near genes
of concern, or preferential outgrowth of cells harbouring integration sites of
concern during the cell culture in the manufacturing process"; the
S-EPTS/LM-PCR (Report 1620234a) on the same DNA samples gave a consistent
pattern. [EMA EPAR, printed pp. 31–32](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report_en.pdf)
(verbatim in the retained text layer `ema_kymriah_epar_2018.txt`).

### SANA cross-check (US11535869B2 Table F)

US11535869B2 (Novartis) lists the three CD19 CARs as SEQ ID NO: 1131 (tisagen-
lecleucel), 1133 (lisocabtagene maraleucel) and 1135 (axicabtagene ciloleucel)
nucleotide sequences with corresponding amino-acid sequences 1132, 1134 and
1136, and its Table F rows are labelled "Tisagenlecleucel CD19 CAR nucleotide
sequence" and so on. [US11535869B2, Table F and
description](https://patents.google.com/patent/US11535869B2/en) (cached raw
table rows: `sana_us11535869B2_tableF_seq1131_1136_excerpt.txt`; FASTA records
`US11535869B2_SEQ1133_lisocabtagene_CAR_nt.fasta` and
`sana_us11535869B2_seq11*.fa`).

Internal consistency was verified on 2026-09-17 by translation: 1131 (1,458
nt) translates exactly to 1132 (486 aa); 1133 (1,383 nt) exactly to 1134
(461 aa); 1135 (1,467 nt) exactly to 1136 (489 aa). The cached Table F scrape
is cut off mid-way through the 1133 row and contains one broken line wrap
("tatcg ccaac…"); the 1,342-nt record derived from it is missing 41 nt at
positions 312–352 (TATCGCCACCTACTTTTGCCAGCAGGGCAACACACTGCCCT) and is retained
only as the documented scrape variant. The 1,383-nt record is the canonical
1133 form because its translation is exact.

### False leads and retrieval gaps

- **US9175308B2** is a Takara Bio Inc. / Mie University patent (GITR CAR,
  anti-CEA and anti-EGFR embodiments), not a Kite or Kymriah record. It was
  chased as a possible KTE-C19 source and resolved as a false lead on
  2026-09-16; do not re-chase. (Documented in `us9175308_seqids.txt`.)
- **US9701758B2** (Board of Regents, The University of Texas System) supplies
  FMC63 anti-CD19 scFv VH/VL sequences — a component-level provenance source for
  the FMC63 scFv, not a vector record. **US8399645B2** (St. Jude Children's
  Research Hospital, Campana et al.) covers 4-1BB signalling-domain chimeric
  receptors — component-level provenance for the 4-1BB domain, not a vector
  record. Neither is a Kite patent. In both, the ST.26 sequence listings are
  rendered as images in the cached FPO/Google Patents HTML, so per-SEQ lengths
  are unknown and are not guessed.
- **Addgene #194458** is not the Kite commercial vector. Addgene's metadata and
  the associated publication identify it as a Coroadinha "iBET" plasmid
  (Biomolecules 2023;13(3):459), a third-generation CD28 + 4-1BB + CD3ζ
  construct in a pRRLSIN.cPPT backbone. The plasmid map (Addgene sequence id
  384169) was fetched live on 2026-09-16 (`addgene_194458_map_seq384169.png`);
  the sequence endpoint is login-gated, so this identification rests on Addgene
  metadata plus the associated paper, not on a sequence comparison. It does not
  close the commercial-vector-sequence gap.
- **Remaining gaps.** No complete commercial transfer-plasmid (pRKHVmuEC19)
  sequence is published; the EPAR states that the detailed genetic-element
  documentation was supplied in the regulatory dossier. The authenticated
  records on hand are the academic/patent-era element map above and the
  US11535869B2 CAR coding sequences. Version identity between JC053548.1 and
  the commercial construct, and a complete commercial integrated-vector
  sequence, remain unestablished; the EPAR Figure 2 schematic and the LISA
  results are the closest regulatory descriptions.
