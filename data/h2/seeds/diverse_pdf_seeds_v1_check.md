# Diverse PDF Seed Check

- Source seed file: `data/h2/seeds/diverse_pdf_seeds_v1.jsonl`
- Checked seed file: `data/h2/seeds/diverse_pdf_seeds_v1_checked.jsonl`
- Source count: `66`
- Checked count: `55`
- Removed / revise-needed count: `11`

## Checked Task Distribution

- `cross_page`: `7`
- `numeric_computation`: `6`
- `table_lookup`: `7`
- `text_lookup`: `11`
- `unanswerable`: `14`
- `verification`: `10`

## Removed / Revise Needed Seeds

| Seed | Task | Reason |
|---|---|---|
| `2308.06595v4__table__p3` | `table_lookup` | awkward table row label; question is unnatural |
| `2308.06595v4__text__p7` | `text_lookup` | reference phrase is unstable in page text extraction |
| `fda_ozempic_2025_label__cross__p1_p2` | `cross_page` | cross-page anchor/answer phrase unstable in PDF text extraction |
| `fda_ozempic_2025_label__table__p4` | `table_lookup` | table row/column labels contain line-break dosage formatting |
| `fda_ozempic_2025_label__text__p1` | `text_lookup` | heading phrase contains noisy rule separators |
| `irs_2025_form_1040__cross__p1_p2` | `cross_page` | anchor phrase is OCR/reversed-text artifact |
| `irs_2025_form_1040__table__p1` | `table_lookup` | form table label/value too awkward for clean QA |
| `irs_2025_form_1040__text__p1` | `text_lookup` | reference contains reversed Form artifact |
| `nist_ai_600_1_genai_profile__table__p29` | `table_lookup` | column label too long/multiline for stable table QA |
| `scotus_loper_bright_2024__cross__p1_p2` | `cross_page` | anchor phrase is generic slip-opinion boilerplate |
| `tm2529296d2_ars__cross__p1_p2` | `cross_page` | answer phrase unstable in raw page-text check |
