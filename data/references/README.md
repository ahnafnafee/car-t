# Reference records

FASTA records were retrieved on 2026-09-16. Hashes below cover the retained files
(text records use UTF-8 with LF line endings). Patent sequence checks use the preserved table cells
and do not infer the expected sequence from the implementation.

| File | Source | SHA-256 |
| --- | --- | --- |
| `7URV.fasta` | [RCSB FASTA](https://www.rcsb.org/fasta/entry/7URV/display), entities 1 and 2 | `458e164afadec7355d1f7a96f68c2fe2ecd3446b30c5c5748a528af673627a97` |
| `P01732.fasta` | [UniProt CD8A](https://rest.uniprot.org/uniprotkb/P01732.fasta), sequence version 1 | `92c066dee6494d561dec91b278e69423d714d52a046d9e5ef76c9bd64ec76f80` |
| `Q07011.fasta` | [UniProt CD137](https://rest.uniprot.org/uniprotkb/Q07011.fasta), sequence version 1 | `eb2509b8194cdbfe0c94d1d21c632f84938adf35b2301f25799da9b8eb003f68` |
| `P20963.fasta` | [UniProt CD247](https://rest.uniprot.org/uniprotkb/P20963.fasta), sequence version 2 | `e8fb2c771f7e246f40d540de12244bab15613f1056e1fb0599060ac16fc5110f` |
| `US11535869B2_table_f.md` | [Patent Table F](https://patents.google.com/patent/US11535869B2/en), SEQ IDs 1131–1132, PDF-reviewed transcription | `8422ca44637221a50bf6b34ef8affed77be9e421095fc9fcde05dda15f792e43` |
| `US11535869B2_page70.png` | Source PDF page 70, printed columns 99–100 | `ed242438a890873ca33c7b1417de87f70cdf635f2a9a031cb204aac6ede043d6` |
| `US11535869B2_page71.png` | Source PDF page 71, printed columns 101–102 | `f2466b1c01a0a2b448ec61efd1dd126179ac972f8e37fd98fa91751ddecbcf4c` |
| `EP2649086_vector.gb` | [NCBI JC053548.1 and JC053555.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JC053548.1,JC053555.1&rettype=gb&retmode=text), patent sequences 1 and 8 | `373a835f35db93843328981bd01aa6a3ceb1d54120edfdcfe8a3c2c9299d03f6` |

The patent excerpt was extracted from an existing cached source on 2026-09-16;
the original retrieval timestamp is unverified. On the same date, its sequence
rows were visually compared with pages 70–71 of the freshly downloaded
[original patent PDF](https://patentimages.storage.googleapis.com/84/4e/6c/a952b2f259ee0c/US11535869.pdf).
The PDF has 124 pages and SHA-256
`125abac5f566feb6981fd94b0b9e2240e4ba43a08d77223d8b2c5dc8419f5622`.
The retained images render those pages for review. This is manual transcription
review, not automated sequence extraction from the scanned PDF or authentication
of a commercial vector. See [the evidence map](../../docs/EVIDENCE.md).

The GenBank records were downloaded on 2026-09-16 without sequence editing.
Their accession versions and patent attribution are retained in the file.
The [vector comparison](../../docs/VECTOR_SOURCES.md) records the exact CAR match,
the sequence-8 boundary discrepancy and the limit on commercial-version identity.
