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

## Extended reference set (promoted 2026-09-17)

The rows below were promoted from the three research tracks after per-file
verification (see docs/VECTOR_SOURCES.md, docs/PROCESS_SOURCES.md,
docs/RELEASE_SOURCES.md). Text files are `.txt`/`.md` extractions of the
named PDF/HTML source; hashes cover the exact bytes retained here.
`promoted_manifest.json` is the machine-readable duplicate of this table.

### FDA — BLA 125646 review package

| File | Source | SHA-256 |
| --- | --- | --- |
| `fda_sbra_107962_bla125646_0_ball_2017-08-30.pdf` | FDA SBRA-quality review, BLA 125646/0 (B-ALL), 30 Aug 2017, [source](https://www.fda.gov/media/107962/download) | `85db4a32d77953c24b2a4dfc218621e57897683208ca43a368e102a7ab1e1e22` |
| `fda_sbra_107962_bla125646_0_ball_2017-08-30.txt` | Text-layer extraction of the SBRA PDF (same row), [source](https://www.fda.gov/media/107962/download) | `390d9a6520bd08ee7a8685c7eba44c1dc16c449d68a9f2b5a435ea3ead75a148` |
| `fda_sbra_113215_bla125646_76_dlbcl_2018-04-13.pdf` | FDA SBRA, BLA 125646/76 (DLBCL sNDA), 13 Apr 2018, [source](https://www.fda.gov/media/113215/download) | `1274e6abcffa0f38c68b1a2bb7ec8f3eb055427ee34a78632dea829f51f760cf` |
| `fda_sbra_113215_bla125646_76_dlbcl_2018-04-13.txt` | Text-layer extraction of the 2018 SBRA PDF, [source](https://www.fda.gov/media/113215/download) | `7b3139a35f1e78339b5f2ad38768d0f30c2e9f044e5664792c1c39cb6d21f75d` |
| `fda_cmc_review_125646_2017-08-29.pdf` | FDA CMC Review 29 Aug 2017 (partial posting: printed pp. 1-12, 101-122, 143-151), [source](https://www.fda.gov/media/107978/download) | `904a3a096b28dc3f6a331f12fc9f14bba1859c2ac85583405aa96619d70aeaf7` |
| `fda_cmc_review_125646_2017-08-29.txt` | Text-layer extraction of the CMC Review PDF, [source](https://www.fda.gov/media/107978/download) | `d5908ff12e11a636ab4ab62b4ce9d9b68c2fee67206ac91f93dc0f7bb8aee0f7` |
| `fda_dmpq_primary_review_memo_vector_125646.pdf` | FDA DMPQ Primary Review Memo (vector production + cell process), BLA 125646, [source](https://www.fda.gov/media/107978/download) | `ce520108e1eee1a1c875ef739ab60dabe848cef403a8a837e2f467da9778d3e3` |
| `fda_dmpq_primary_review_memo_vector_125646.txt` | Text-layer extraction of the DMPQ memo PDF, [source](https://www.fda.gov/media/107978/download) | `ac8f6b5cad49349f31d27ee5cef4a322777e7722104f367d3596e39289bde453` |
| `fda_dp_review_memo_125646.pdf` | FDA DP review memo (Melhem), cell product, 46 posted of 70 pages, [source](https://www.fda.gov/media/107978/download) | `95cf326b72698aba0645bbe2ad5d2f50e7be329700046944d058359aaf0e1383` |
| `fda_dp_review_memo_125646.txt` | Text-layer extraction of the DP review memo PDF, [source](https://www.fda.gov/media/107978/download) | `b0fe5ed770039ee7e24b737a18564f8983f0588fdcc701bef850a31fb9fd9d57` |
| `fda_cmc_information_request_2017-07-28.pdf` | FDA CMC information request, 28 Jul 2017 (CPP names, Table 6-4 historical ranges), [source](https://www.fda.gov/media/107978/download) | `3383ec41db5ab6e90ddc70e4d42eb5f7a3c8449d5b966474d08eb664089406fd` |
| `fda_cmc_information_request_2017-07-28.txt` | Text-layer extraction, [source](https://www.fda.gov/media/107978/download) | `9829f963975bd47a253a56994bcfe7e5711cc6083e9737a4d45494a94d25704b` |
| `fda_re_cmc_information_request_2017-03-29.pdf` | Applicant response to CMC IR of 29 Mar 2017 (flow-gating review trigger), [source](https://www.fda.gov/media/107978/download) | `77b0551658c791b609f30a2e17a8f382c1215c8883e74b07386977df65a83d67` |
| `fda_re_cmc_information_request_2017-03-29.txt` | Text-layer extraction, [source](https://www.fda.gov/media/107978/download) | `5eec8cc27a9303349c5e43db543d8587990ca79ac4a15737712976f17bf94a00` |
| `fda_odac_briefing_document_125646.pdf` | FDA ODAC briefing document PDF, BLA 125646, [source](https://www.fda.gov/media/106081/download) | `8aa0b850e12997b823e6ffd37d24bc4bb24816054d4645358d7577f92e74b298` |
| `fda_odac_briefing_document_125646.txt` | FDA ODAC briefing document text extraction, BLA 125646 (12 Apr 2017 background package), [source](https://www.fda.gov/media/106081/download) | `dae43011713cef70cf341e3d948dd294bd1a0179b2f60c1e2b35e7fb3b43fd0b` |
| `fda_odac_presentation_2017-07-12.pdf` | FDA ODAC introductory remarks presentation, 12 Jul 2017, [source](https://www.fda.gov/media/106489/download) | `e03fd9c42cc54e46f8fbf8fb793bfce9bd33b454768fb2fd0b1c2514cfca968e` |
| `fda_odac_presentation_2017-07-12.txt` | Text-layer extraction of the ODAC deck, [source](https://www.fda.gov/media/106489/download) | `a86cb189ffed61426d28f2fa2b85a3408973a8f472e8611e91f9c2ae934f494c` |
| `fda_pi_kymriah_current.pdf` | US prescribing information, current label (FL version), [source](https://www.fda.gov/media/107296/download) | `b2025e715e75502e811955dd9d010ec5273eb19aa9eb9bc38c585ad911e582f0` |
| `fda_pi_kymriah_current.txt` | Text-layer extraction of the PI PDF, [source](https://www.fda.gov/media/107296/download) | `d9af5a5843dbe9f675983c976f3fcd98dfdfa8ec7115418af851af577bd32ea2` |
| `fda_approval_letter_125646_0_2017-08-30.pdf` | FDA approval letter STN 125646/0, 30 Aug 2017, [source](https://www.fda.gov/media/106989/download) | `2de46941c8c074a64343e363d81e48363c518e600d69da77577d7412a07eeb7a` |
| `fda_approval_letter_125646_76_2018-05-01.pdf` | FDA approval letter STN 125646/76 (DLBCL), 1 May 2018, [source](https://www.fda.gov/media/112803/download) | `154b930c8c48ea05f45e06149efae58e5d0d56b2cbe13eba0091ba9be3d2b1a4` |
| `fda_letter_125646_429_2021-06-11.pdf` | FDA letter STN 125646/429, 11 Jun 2021, [source](https://www.fda.gov/media/150087/download) | `21a63480cc424abc2373f605acd971506499400daf84507a72813875b12641de` |
| `fda_letter_125646_854_2024-04-12.pdf` | FDA letter STN 125646/854, 12 Apr 2024, [source](https://www.fda.gov/media/178030/download) | `81051f07716b99afe556aba081516c2f1e39866fc18494dcadbdf80b7ca539be` |
| `fda_letter_125646_860_2024-06-13.pdf` | FDA letter STN 125646/860, 13 Jun 2024, [source](https://www.fda.gov/media/179659/download) | `0a1a069513fe97a90a1d95d74ad68743ce13c295b69d9fe8064c4dd2ec3b6ece` |
| `fda_letter_125646_902_2024-08-16.pdf` | FDA letter STN 125646/902 (REMS minor modification), 16 Aug 2024, [source](https://www.fda.gov/media/181491/download) | `03a16ce058c34b8e505c0a408fcaddb17fe91e4e3e389803d8a91ad43a876bee` |
| `fda_label_section11.txt` | US PI section 11 (DESCRIPTION) extract, [source](https://www.fda.gov/media/107296/download) | `3a88ac1fcdb262d48ca77507ceca4b7a329b3956b53d880d1d13353f3e9d6f0d` |
| `fda_media_107978_bla125646_approval_history.zip` | FDA BLA 125646 approval-history package (109 documents); members promoted individually under fda_* names, [source](https://www.fda.gov/media/107978/download) | `261f22a71a682f08b193a81c4a080ba9d3591d3efd359e66d80a10925cf8322b` |

### EMA and PMDA

| File | Source | SHA-256 |
| --- | --- | --- |
| `ema_kymriah_epar_2018.pdf` | EMA public assessment report, EMA/CHMP/443047/2018, 28 Jun 2018, [source](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report-epar_en.pdf) | `02ad0cfd1752beb1901409ba3325746d8409dd1f4dcbda9d7a3dcfca7c3f74da` |
| `ema_kymriah_epar_2018.txt` | Text-layer extraction of the EPAR PDF (line refs in docs), [source](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report-epar_en.pdf) | `7b5129f94934632b81b2ea6b44e60a49437e4aeb8705ab1f093d88f259560a31` |
| `ema_kymriah_smpc.pdf` | EMA SmPC (Annex I), Kymriah 1.2x10^6-6x10^8 cells dispersion for infusion, [source](https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf) | `5fdcf1c90a6a6d90b0efde33fc48824329dc1e6d597877d217fad0263b61de71` |
| `ema_kymriah_smpc.txt` | Text-layer extraction of the SmPC PDF, [source](https://www.ema.europa.eu/en/documents/product-information/kymriah-epar-product-information_en.pdf) | `d536764bedc43750044bbb310c1108e5761960f38414469d6485957133668d3e` |
| `pmda_kymriah_review_2019.pdf` | PMDA review report, tisagenlecleucel, 20 Feb 2019, [source](https://www.pmda.go.jp/files/000252613.pdf) | `ec1aff5142ac97406b2542430ec7bf8c35d59a32c52ec2d5c8896588dd7cb827` |
| `pmda_kymriah_review_2019.txt` | Text-layer extraction of the PMDA PDF (line refs in docs), [source](https://www.pmda.go.jp/files/000252613.pdf) | `e940c2b22583cc737eb804aa9243b3dce42d03236152d569f1e910cb2193ff13` |
| `epar_figure2_integrated_vector_p17.png` | Render of EPAR printed pp. 17-18 (Figure 2, integrated vector), 3.0x; source of the vision transcription, [source](https://www.ema.europa.eu/en/documents/assessment-report/kymriah-epar-public-assessment-report-epar_en.pdf) | `79ad2fad88d69295295407024df3c20bd6575328208982f4426e091881b4c71d` |

### Vector sequence records (GenBank, derived elements, patent FASTAs)

| File | Source | SHA-256 |
| --- | --- | --- |
| `EP2649086_all_sequences.gb` | NCBI efetch GenBank batch JC053548.1-JC053574.1 (EP2649086 deposit, 20 nucleotide records), [source](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=JC053548.1-JC053574.1&rettype=gb&retmode=text) | `5c71babd14d7b73234ade75dc624d104b18ba35c6f2ab255a3024b36cccd74b1` |
| `ep2649086_elements.fa` | Consolidated multi-FASTA of the 20 deposited records (byte-identical bodies), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `9c087e4a3ff164b4725cc94fa4d6d501bb78b45322d9537a7d83013b6b120874` |
| `J04514.gb` | NCBI J04514.1 woodchuck hepatitis B virus genome (canonical WPRE source), [source](https://www.ncbi.nlm.nih.gov/nuccore/J04514.1) | `aeab640591c8e50b13ae4cbd425e099b18d3ae47201db383747ab9512bbb32c0` |
| `wpre_core_592.fa` | WPRE 592-nt core = JC053548.1[7858-8449] = J04514.1[1093-1684], derived; see [the vector comparison](../../docs/VECTOR_SOURCES.md) | `071ac93007173e555c238030d39817d21a9b9bf96a79d79cfc015aaf259b240b` |
| `wpre_seq9_591.fa` | Deposited seq 9 WPRE 591 nt = JC053548.1[7859-8449] = J04514.1[1094-1684], derived; see [the vector comparison](../../docs/VECTOR_SOURCES.md) | `dad1722749452e4005961f23754559151517a93b091216c2ac21a42fda8c8424` |
| `wpre_extended_726nt_J04514_1093_1818.fa` | Canonical 726-nt WPRE = J04514.1[1093-1818], derived; see [the vector comparison](../../docs/VECTOR_SOURCES.md) | `faae26646c3ec424dea0b964da29539d65bacdd62c4665394795832240031158` |
| `sana_us11535869B2_seq1131_tisagenlecleucel_car_nt.fa` | US11535869B2 SEQ 1131 (1,458 nt) tisagenlecleucel CAR CDS, [source](https://patents.google.com/patent/US11535869B2/en) | `5877f77806429770b3996f3b6277930ff0a0571c2ca3c53fc7fbeb856887ff17` |
| `sana_us11535869B2_seq1132_tisagenlecleucel_car_aa.fa` | US11535869B2 SEQ 1132 (486 aa), [source](https://patents.google.com/patent/US11535869B2/en) | `033dd22bf2705cbb0552df090de951494ce1849b546b95bc4dc6389cd6a81351` |
| `US11535869B2_SEQ1133_lisocabtagene_CAR_nt.fasta` | US11535869B2 SEQ 1133 canonical form (1,383 nt; translates exactly to SEQ 1134), [source](https://patents.google.com/patent/US11535869B2/en) | `025d0be23035b3be27c30c90712ab01d74a56a6c69658ffa1f6ce4b6baaf043f` |
| `sana_us11535869B2_seq1133_lisocabtagene_car_nt.fa` | US11535869B2 SEQ 1133 1,342-nt scrape variant (41-nt gap; documented artifact), [source](https://patents.google.com/patent/US11535869B2/en) | `1556a7ba8a9ad656cd722aeb98ef2b50249ef8347eb6d541afaafe80efb25c02` |
| `sana_us11535869B2_seq1134_lisocabtagene_car_aa.fa` | US11535869B2 SEQ 1134 (461 aa), [source](https://patents.google.com/patent/US11535869B2/en) | `2cb5dbd6d959e6aa4534dcb1a22bcc63ffbd95e46e7d19aa4514b7dc9fe644ab` |
| `sana_us11535869B2_seq1135_axicabtagene_car_nt.fa` | US11535869B2 SEQ 1135 (1,467 nt), [source](https://patents.google.com/patent/US11535869B2/en) | `53638146e0e0801b9e2cf0526acb0e5db7f165bbe24685e32848ccd6115dc654` |
| `sana_us11535869B2_seq1136_axicabtagene_car_aa.fa` | US11535869B2 SEQ 1136 (489 aa), [source](https://patents.google.com/patent/US11535869B2/en) | `15a0d78a44ea3e48ee5c43e7d7f5b6cef4c2d4f403644c6e20c472e0085a5104` |
| `sana_us11535869B2_tableF_seq1131_1136_excerpt.txt` | Raw Table F markdown rows (truncated mid-1133; one broken wrap), [source](https://patents.google.com/patent/US11535869B2/en) | `2fb3ca83a38233f6af8525adea925c026b2d2090f1ebac0dfb34fd472b221bcf` |
| `addgene_194458_map_seq384169.png` | Addgene #194458 plasmid map (sequence id 384169), live fetch 2026-09-16, [source](https://www.addgene.org/194458/) | `630d3e4ce52c8b9bede1cc87c72f620c99d1452d4c5e60a57cd3dd7f42bfafee` |
| `oncologist_fig2_p3.png` | Render of Oncologist 2020;25:e321 Figure 2 (integrated vector), [source](https://doi.org/10.1093/oncolo/ozaa003) | `d5f309e5bb3b7641bd066e7090cd53142f5264c119891bdcdbbce0217826e5be` |
| `ep2649086_seqs/seq10_R_repeat.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `b6f56ae5e15b87eab5b3d752aaff5f3619c7057c96fea921739d89f51d8da498` |
| `ep2649086_seqs/seq11_U5_repeat.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `84dbdcd9c339df0339993d01570aa584c4444a58c9e9626ffc30ef23b2947f01` |
| `ep2649086_seqs/seq13_CD8_leader.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `9020803fcca46c57fc24287918a6165aecc4083d24edbd48743aa958ad299eaf` |
| `ep2649086_seqs/seq14_antiCD19_scFv.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `0fe022c735dbdfdc778167d6253fb129637f3b03afff78aa612e5f7dbb383102` |
| `ep2649086_seqs/seq15_CD8_hinge.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `8412bcbb61c7edd4b2fdab61036f613428bb3d13aaa0f21c8697804aaf64c80e` |
| `ep2649086_seqs/seq16_CD8_TM.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `8facda9816f278d3ffe3e0f14684c0a2d024124fe68e44964526d187d18bc316` |
| `ep2649086_seqs/seq17_4-1BB.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `afccaf746898d23cba8cf7f8207d858eb104fe5abf196fa146e63eb860c2c82f` |
| `ep2649086_seqs/seq18_CD3zeta.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `374384693c35d3245ab66f4095bda421554ebc41ede7a23565e7ee23a8250977` |
| `ep2649086_seqs/seq1_pELPS_CD19_BBz_transfer_vector.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `6921dd726ef36c0a98fad42a01b822f0425925cc5c9776b8d6f3143ba2c20032` |
| `ep2649086_seqs/seq25_unknown.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `c5cdd9d793370a73f1fe4e6aead27555e09c7a5a394a26846e7aee8cfa88a1a6` |
| `ep2649086_seqs/seq26_unknown.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `bc3218cebb88465c68a2087b8ef7ad9a9d6bb850787746f712da419c70eaa7d1` |
| `ep2649086_seqs/seq27_unknown.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `c61303fb241d20cba7c13baf3f80bf622b37e95c1f514c9b473d847b7c0b1930` |
| `ep2649086_seqs/seq2_RSV_U3.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `deff47cc4fa46c24a06046039c213ed5c5f78469eb00bd2f4c57498bbb7343f8` |
| `ep2649086_seqs/seq3_HIV_R_repeat.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `3488ba97a2449eaabbe1cc9074f944b88c8be2c7dfa542a1480a2aa0f7a73e8b` |
| `ep2649086_seqs/seq4_HIV_U5_repeat.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `511d1eca62028a475e906d701e8ed39376aa9bae6a6478768878a7c51dc99899` |
| `ep2649086_seqs/seq5_partial_GagPol.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `6526d6b5800dc515249fbde77e81cdef1b6be8a4fc1f468b1191d6d300375691` |
| `ep2649086_seqs/seq6_cPPT.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `318e8e4645f501ee8f6b8013ee18620320f7f3baa1482e2cb586dae1f0f3b256` |
| `ep2649086_seqs/seq7_EF1alpha_promoter.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `7d891a8fb2f2aa6f9883df8b8c4d39a511175556ff0cd1fbbf138223d32f2ad2` |
| `ep2649086_seqs/seq8_CD19_BBzeta_CAR_nt.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `4bbe4f6bd9f6348f2df6e855f22236b51b3aa08b5c98a5a1d7b8ba80a5b11ede` |
| `ep2649086_seqs/seq9_Hu_Woodchuck_PRE_WPRE.fa` | per-record FASTA of the EP2649086 GenBank deposit (byte-identical body), derived from [EP2649086_all_sequences.gb](EP2649086_all_sequences.gb) | `1122f4b9bd8ef0040d04e87f4eb01ea32fc8b7c16e22dffd4581a430dfa65259` |

### Patent text caches and sequence-listing notes

| File | Source | SHA-256 |
| --- | --- | --- |
| `us9328156B2_table5.txt` | US9328156B2 Table 5 verbatim (cached scrape; truncated at ~2,000 chars), [source](https://patents.google.com/patent/US9328156B2/en) | `64dfb6abfb33140bd63b3a95c65d8a8bb9dec9257433372afdec665d0857270e` |
| `us20150093822_patent_desc.txt` | US20150093822A1 full-text cache (source of CDKN1A primer/probe passage), [source](https://patents.google.com/patent/US20150093822A1/en) | `a498d958669fb7279173bfd0398e77e512609434195b70e42c7ed9cf70c989da` |
| `us9175308_seqids.txt` | US9175308B2 (Takara/Mie, GITR CAR) — false-lead documentation, [source](https://patents.google.com/patent/US9175308B2/en) | `982d57e0c55e17066ff5f49f0063505c12a5e855f1fbb0e03041504d4506608d` |
| `US9175308B2_seq_id_contexts.txt` | US9175308B2 SEQ ID first-mention contexts, [source](https://patents.google.com/patent/US9175308B2/en) | `af368829e00f51753875926134bca2b5ef09aeb81899546dd7b37ff5b3daba01` |
| `US9175308B2_sequence_listing_freetext.txt` | US9175308B2 ST.26 listing free text (identifiers only), [source](https://patents.google.com/patent/US9175308B2/en) | `f9c6cf70814f601c2397efdd4e662b98ba34368ba230a32b0752e601e51629c7` |
| `us9701758_seqids.txt` | US9701758B2 (UT System, FMC63 scFv) identifiers + contexts, [source](https://patents.google.com/patent/US9701758B2/en) | `e89ded1e4eab15c1b3acf83a2869f706455ed3d6fe6da543a3f84e2d43ade300` |
| `US9701758B2_seq_id_contexts.txt` | US9701758B2 SEQ ID contexts, [source](https://patents.google.com/patent/US9701758B2/en) | `d9cc8ea74df0e6323a56492b9bbb19271fde9908a82df7a430c2988484b1ba8f` |
| `us8399645_seqids.txt` | US8399645B2 (St. Jude, 4-1BB CAR) identifiers + contexts, [source](https://patents.google.com/patent/US8399645B2/en) | `f4359ecc83f4a57f1029594a243168984608f5e4f8f7e7f089d0f93a455f18f6` |
| `US8399645B2_seq_id_contexts.txt` | US8399645B2 SEQ ID contexts, [source](https://patents.google.com/patent/US8399645B2/en) | `cbe6f2be2b3844e2db4cef57d0c552cc2dc0a226fe8cc729af93ccf448390680` |
| `USPTO_8399645_fulltext.txt` | fetch-failure stub (28 B) — evidence of attempt, [source](https://patft.uspto.gov/) | `98c3689f37aa605365100f6c2597bfd2e83f4bd296667130b844228fd68bcfba` |
| `USPTO_9701758_fulltext.txt` | fetch-failure stub (67 B) — evidence of attempt, [source](https://patft.uspto.gov/) | `a8fb4eafdaaca92f9674e1e36de45505444102a200a4ce73c13319ed0d108c9d` |
| `silva2023_backbone_notes.txt` | Silva et al. 2023 Biomolecules 13:459 plasmid/backbone notes (Addgene #194458 paper), [source](https://doi.org/10.3390/biom13030459) | `671b8b53ab71572b49a7a7a26344fe355e586af7b5e3a907db6c9eb10b09f472` |
| `integration_study_abstracts.txt` | Abstracts: PMC11985369 (BJH longitudinal integration), PMC9644589 (J Transl Med retroviral integration), [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985369/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9644589/) | `12c37eeb820379bde8ba7ba44b09883420c9104705baeb9e2f5f6f1bd7eb1a5d` |
| `us20210161959a1_gp_text.txt` | Google Patents full text US20210161959A1 (example process numerics, Table 26), [source](https://patents.google.com/patent/US20210161959A1/en) | `bd481ffb6b9731fbdc9464e9fd4d3b49391007e16ae3458c038a862f3174e28a` |
| `us12600775b2_gp_text.txt` | Google Patents full text US12600775B2, [source](https://patents.google.com/patent/US12600775B2/en) | `a070d1c89db40087750a8d9a25c2d99232ea45f8f50a32ab9afd3a7f96d7e542` |
| `us20220168389a1_gp.md` | Google Patents full text US20220168389A1 (Example 1 rapid process), [source](https://patents.google.com/patent/US20220168389A1/en) | `09e54716c5b30c7fc048f5e6310acdba61e4aa4ae2d71afed1ffb2cf9fd44d04` |
| `us20170107286a1_gp_text.txt` | Google Patents full text US20170107286A1 (anti-CD19 CAR; no usable process parameters), [source](https://patents.google.com/patent/US20170107286A1/en) | `83d76ee1b69cf7d2291ddc55ef98d3d1fe76f76f0245c499c5383f221c2ee198` |
| `us20050113564a1_gp_text.txt` | Google Patents full text US20050113564A1 (4-1BB CAR; qualitative only), [source](https://patents.google.com/patent/US20050113564A1/en) | `1c7cf4eb85b871e14618bcb502969d5b4dc6470ee25c3ea44b0eb6c99da16ab3` |
| `us9701758b2_gp_text.txt` | Google Patents full text US9701758B2 (UT System FMC63 scFv), [source](https://patents.google.com/patent/US9701758B2/en) | `f6ff1eb08ddc7c48c7f6dec9d80c73f2a0772849548131af9e3d6dc89312f513` |
| `us8262992b2_gp_text.txt` | Google Patents full text US8262992B2 (modular sensor cassette; non-CAR-T scan record), [source](https://patents.google.com/patent/US8262992B2/en) | `3a38e398bcba0f81c6b7c56f549a8249c13c96f53ddf533c360328dcbc788ace` |
| `us10125222b2_gp_text.txt` | Google Patents full text US10125222B2 (polyisocyanopeptides; non-CAR-T scan record), [source](https://patents.google.com/patent/US10125222B2/en) | `c27743be981c6a411a9b08d8c6d2f2638b5c25116d2d3aae4e9ced59d82a8113` |
| `us11535869b2_gp_text.txt` | fetch-failure stub (124 B) for US11535869B2 GP text, [source](https://patents.google.com/patent/US11535869B2/en) | `743291c40eee468a3f4c8c0d73580c7d8ee4bd0a3e1022f58eb39b2f70c1ba42` |

### Literature and corporate filings

| File | Source | SHA-256 |
| --- | --- | --- |
| `bai2022_ctl019_panel.txt` | Bai et al. Sci Adv 2022 full-text extraction (academic CTL019 release panel), [source](https://doi.org/10.1126/sciadv.abj2820) | `4c73b0b4473e24b2bd1146511d2e67cdb8c7c29080dbda1a4926b148e599b048` |
| `pasquini_2020_rwe.txt` | Pasquini et al. Blood Adv 2020 text extraction (US commercial 80% viability, doses), [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC7656920/) | `0106cd8e99d1e6bb38af6acdefcbe9d760724e76083407f251d96738dc458bcb` |
| `rossoff_2021_out_of_spec.txt` | Rossoff et al. Blood 2021 text extraction (OOS reasons), [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC8617436/) | `906d45b4cbbd375e17208b80aeaaac6dbd6d1d1d3037fe202ea40606133b8ea4` |
| `maude_2014_nejm_ctlo19.txt` | Maude et al. NEJM 2014 PMC full-text extraction (incomplete: panel not in main body), [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC4267531/) | `7d3b9edc2707cc4a698d52646b16db917030b47813602ef7512920b6bf392518` |
| `maude_2018_eliana.txt` | Maude et al. NEJM 2018 (ELIANA) PMC full-text extraction, [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC5996391/) | `9f4c5849a8e92c4b1afe092c15d934b64b8bdd783dee4ef7dc0ffc74fc87eb3f` |
| `kato_2025_cytotherapy_oos_japan.md` | Kato et al. Cytotherapy 2025 full text (Japan OOS trial, 70% criterion), [source](https://www.sciencedirect.com/science/article/pii/S1465324925006851) | `25fe0f7479636194f0fc8f23fe5c7d943e8352f0cd4971af65f4873f94d81b19` |
| `bachanova_2019_ash_abstract_242.html` | Bachanova et al. ASH 2019 abstract #242 (IFNgamma 23.7-938 fg/CAR+ cell), [source](https://ashpublications.org/blood/article/134/Supplement_1/242/426221/) | `c7183f4fb176c31ad7cabf7e14730bcc503f47044caaefd8e4fa61ad89320a14` |
| `fong_2023_tct_fulltext_oa.md` | Fong et al. Transplant Cell Ther 2023 open-access full text (viability assay change 2019-2020), [source](https://www.astctjournal.org/article/S2666-6367(23)01355-6/pdf) | `a3cc9f3d4d8bbba7f55fe4177d04ec748dfbb9c606525c61931854e1a4993579` |
| `iwamoto2025_japan_pmc11891598.txt` | Iwamoto et al. 2025 (Regen Ther 28:619-624) full text (Japan MSR/SSR/OOS trend), [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11891598/) | `8330648d9711673abc844e8e94ca5f08811d49905ac42edd912af60c6740608c` |
| `tyagarajan_2020_mtmcd.xml` | Tyagarajan et al. MTMCD 2020 Europe PMC full-text XML (median 23-day cycle, CQA framework), [source](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6970133/fullTextXML) | `11084cf701f57bee428a954a39307d174fb06cb056330fff5f8b23930152b6d9` |
| `levine2017_global_mfg_car_t_pmc5363291.xml` | Levine et al. 2017 PMC full-text XML (global CAR-T manufacturing context), [source](https://pmc.ncbi.nlm.nih.gov/articles/PMC5363291/) | `4935a1513ee1834cc3ccfd8f5e0dd7ffd81a3943710f22e086e5430d9ea1e2f3` |
| `kymriah_reviewer_article_oncologist_2020.txt` | Ali et al. Oncologist 2020;25:e321 (published EMA review) text extraction, [source](https://doi.org/10.1093/oncolo/ozaa003) | `c93d2d148916ca5fcb9f748ad05f91826c17a2737668f8b8cc9014f9268c67ba` |
| `edgar_10k_fy2016.md` | Kite Pharma Form 10-K FY2016 (14-16 day turnaround, El Segundo plan), [source](https://www.sec.gov/Archives/edgar/data/1510580/000151058017000003/kite20161231-10k.htm) | `19097a32ec710ad77c50577ac592db781da0c656f7a6fdf98c92782f1a336ff5` |
| `edgar_s1a_20141209.md` | Kite Pharma Form S-1/A 9 Dec 2014 (pre-commercial vendor reliance), [source](https://www.sec.gov/Archives/edgar/data/1510580/000119312514437675/d824808ds1a.htm) | `5fcd15d4c31b725622fc6d10149a1f6b82098af7cedcff0503644c8e161f2161` |

### Rendered figures

| File | Source | SHA-256 |
| --- | --- | --- |
| `figures/odac_slide22.png` | Render of ODAC deck (media/106489) slides 22-24 at 2160x1620; lot-release charts (IFN-gamma potency, transduction efficiency, integrated vector) read via vision bridge 2026-09-16, [source](https://www.fda.gov/media/106489/download) | `86c539e7057ad0d4288de690b050cad8d27441e89c79cbbce581603c129b746d` |
| `figures/odac_slide23.png` | Render of ODAC deck (media/106489) slides 22-24 at 2160x1620; lot-release charts (IFN-gamma potency, transduction efficiency, integrated vector) read via vision bridge 2026-09-16, [source](https://www.fda.gov/media/106489/download) | `d1fa8218b76e00e1f99f4044227d71396d0913259008af5dd9a9c8084688689f` |
| `figures/odac_slide24.png` | Render of ODAC deck (media/106489) slides 22-24 at 2160x1620; lot-release charts (IFN-gamma potency, transduction efficiency, integrated vector) read via vision bridge 2026-09-16, [source](https://www.fda.gov/media/106489/download) | `caa1680d444ecb92937f8dd67c67bea27adf28c630a5d2fbb3d591040aa77c94` |
