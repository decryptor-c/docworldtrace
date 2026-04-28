# Diverse PDF Candidates v1

用途：扩充 DocWorldTrace 原始文档池，重点解决报告里 H4 数据多样性不足，以及 H3 规则评估缺少更自然错误分布的问题。

## Selection Criteria

- 来源：官方或稳定公共来源，包括政府、法院、标准机构、国际组织和公司投资者关系页。
- 结构：覆盖短表单、长报告、财报、法律意见、药品标签、标准/框架、预算、气候/地质/气象统计。
- 任务覆盖：每篇文档都标注适合生成的任务类型，避免只扩充同一种 annual report。
- 风险控制：下载后仍需先跑 H1 suitability；特别长或图表密集 PDF 不应整篇无差别进入 H2。

## Candidate Set

| ID | Domain | Target file | Main diversity value | Recommended tasks |
|---|---|---|---|---|
| `apple_2025_10k` | Corporate filing | `apple_2025_10k.pdf` | SEC filing, financial tables, risk factors | table, numeric, verification, cross-page |
| `microsoft_2025_10k` | Corporate filing | `microsoft_2025_10k.pdf` | long 10-K, large tables, AI/security narrative | table, numeric, verification, cross-page |
| `irs_2025_form_1040` | Government form | `irs_2025_form_1040.pdf` | fillable form, line-numbered fields, short dense layout | text, table, verification |
| `fda_ozempic_2025_label` | Medical regulatory | `fda_ozempic_2025_label.pdf` | boxed warnings, dosage tables, section references | text, verification, cross-page |
| `who_global_tb_2024` | Global health | `who_global_tb_2024.pdf` | public-health statistics and country/region tables | table, numeric, verification, cross-page |
| `usgs_mcs_2025` | Geoscience statistics | `usgs_mcs_2025.pdf` | repeated commodity tables, long reference layout | table, numeric, verification |
| `nasa_fy2025_budget_summary` | Government budget | `nasa_fy2025_budget_summary.pdf` | mission budget tables and program descriptions | table, numeric, cross-page |
| `epa_ghg_inventory_1990_2022` | Environmental inventory | `epa_ghg_inventory_1990_2022.pdf` | time-series emissions tables and methodology | table, numeric, verification |
| `ipcc_ar6_syr_longer_report` | Scientific assessment | `ipcc_ar6_syr_longer_report.pdf` | confidence language, figures, footnotes | text, verification, cross-page |
| `nist_ai_600_1` | Technical standard | `nist_ai_600_1_genai_profile.pdf` | risk taxonomy, action tables, definitions | table, verification, cross-page |
| `scotus_loper_bright_2024` | Legal opinion | `scotus_loper_bright_2024.pdf` | majority/concurrence/dissent, citations, footnotes | text, verification, cross-page |
| `nhc_beryl_2024_report` | Meteorological report | `nhc_beryl_2024_report.pdf` | event chronology, track tables, maps | table, numeric, verification, cross-page |

## Integration Plan

1. Download the PDFs into `data/raw_pdfs/` using the `download_url` fields in `diverse_pdf_candidates_v1.json`.
2. Run H1 raw data evaluation on the expanded directory.
3. Keep a balanced subset by domain and layout before regenerating H2 seeds.
4. Regenerate H2/H3/H4 on the balanced subset, then compare:
   - per-document coverage,
   - task-type coverage,
   - seed-level unique sequence ratio,
   - rule-based path deviation,
   - H3 negative-control catch rate.
5. Do not use medical/legal content for advice; use it only as document-grounding material.
