# diverse_pdf_seeds_v1_corrected — changelog

- source: `data/h2/seeds/diverse_pdf_seeds_v1_checked.jsonl` (55 seeds)
- output: `data/h2/seeds/diverse_pdf_seeds_v1_corrected.jsonl` (54 seeds)
- dropped: `data/h2/seeds/diverse_pdf_seeds_v1_corrected.dropped.jsonl` (1 seeds)

| 状态 | 数量 |
|---|---:|
| KEEP (无修改) | 34 |
| REVISE (改写) | 20 |
| DROP (丢弃) | 1 |

## 改动条目

| 原 seed_id | 新 seed_id | 改动说明 |
|---|---|---|
| `apple_2025_10k__table__p3` | `apple_2025_10k__table__p3` | W1: Column Business → Page; row uses full TOC item label. |
| `apple_2025_10k__verify__p18` | `apple_2025_10k__verify__p18` | W2: Truncated fragment → full sentence. |
| `epa_ghg_inventory_1990_2022__cross__p2_p3` | `epa_ghg_inventory_1990_2022__cross__p2_p3` | W3: Extended cross_page anchor to longer unique phrase. |
| `epa_ghg_inventory_1990_2022__numeric__p41` | `epa_ghg_inventory_1990_2022__numeric__p41` | B1: Replaced header-row vs data-row with Total Gross vs Net Emissions in same column. |
| `epa_ghg_inventory_1990_2022__table__p41` | `epa_ghg_inventory_1990_2022__table__p41` | B2: Switched to genuine row × column data cell. |
| `epa_ghg_inventory_1990_2022__text__p134` | `epa_ghg_inventory_1990_2022__table__p134` | B3: Changed task_type text_lookup → table_lookup; renamed seed_id; chose a labeled row. |
| `epa_ghg_inventory_1990_2022__verify__p697` | `epa_ghg_inventory_1990_2022__verify__p41` | W4: Garbled city-row claim → ES-table verifiable claim on p41. |
| `fda_ozempic_2025_label__numeric__p4` | `fda_ozempic_2025_label__numeric__p4` | W5: Removed multi-line row label; clarified units. |
| `ipcc_ar6_syr_longer_report__numeric__p11` | `(dropped)` | B4: Compared Population (1292) with GDP per capita (5) — unit-incompatible. No clean replacement on p11; dropping. Recommend new IPCC numeric seed from a uniform-units table elsewhere (e.g., Table 3.1 emissions pathways). |
| `ipcc_ar6_syr_longer_report__text__p50` | `ipcc_ar6_syr_longer_report__text__p50` | W6: Reference expanded to 'Section 3 Table 3.1: ...'. |
| `irs_2025_form_1040__verify__p2` | `irs_2025_form_1040__verify__p2` | W7: Page-footer claim → real form line text. |
| `nasa_fy2025_budget_summary__cross__p2_p3` | `nasa_fy2025_budget_summary__cross__p2_p3` | B5: Re-anchored to unique p2 content; answer = first bullet on p3. |
| `nasa_fy2025_budget_summary__numeric__p4` | `nasa_fy2025_budget_summary__numeric__p4` | W8: Reworded cross-program comparison as 'how much smaller'. |
| `nasa_fy2025_budget_summary__table__p4` | `nasa_fy2025_budget_summary__table__p4` | B6: Switched to genuine NASA Total × FY 2025 Request cell. |
| `nasa_fy2025_budget_summary__verify__p12` | `nasa_fy2025_budget_summary__verify__p12` | W9: Trivial heading claim → specific cell-value claim. |
| `nist_ai_600_1_genai_profile__cross__p1_p2` | `nist_ai_600_1_genai_profile__cross__p2_p3` | B7: Renamed to cross__p2_p3; anchor on unique p2 phrase. |
| `nist_ai_600_1_genai_profile__text__p7` | `nist_ai_600_1_genai_profile__text__p5` | B8: Page 7 → page 5 (clean section heading). |
| `scotus_loper_bright_2024__text__p2` | `scotus_loper_bright_2024__text__p2` | W10: Running page-header → Syllabus section heading. |
| `scotus_loper_bright_2024__verify__p4` | `scotus_loper_bright_2024__verify__p4` | W11: Running page-header → substantive opinion sentence. |
| `usgs_mcs_2025__cross__p1_p2` | `usgs_mcs_2025__text__p1` | B9: cross_page → text_lookup p1. |
| `usgs_mcs_2025__text__p18` | `usgs_mcs_2025__text__p21` | W12: Page 18 figure → page 21 Table 4 heading. |

## 任务分布对照

| task_type | 修复前 | 修复后 |
|---|---:|---:|
| cross_page | 7 | 6 |
| numeric_computation | 6 | 5 |
| table_lookup | 7 | 8 |
| text_lookup | 11 | 11 |
| unanswerable | 14 | 14 |
| verification | 10 | 10 |

## Followup Fixes (post first-round review)

| # | seed_id | 改动 |
|---:|---|---|
| F1 | `epa_ghg_inventory_1990_2022__table__p134` | 用 pdfplumber 在 p134 检测到 1 个表（57 行），写入真实 bbox `[73.512, 83.78, 540.1, 707.85]` 到 `supporting_refs` 与 `metadata.bbox`；并交叉验证 'Transportation' 行 2022 列 = '1,807.8'。 |
| F2 | `apple_2025_10k__table__p3` | 题目从「row × column」契约改为自然语言 TOC 问法 ("In the table of contents on page 3, what page is 'Item 1A. Risk Factors' listed on?")；删除 metadata 里的 `row_label` / `column_label`，避免与 `parse_table` 的实际输出 `['Item 1A.', 'Risk Factors', '5']` 冲突。 |
| F3 | `usgs_mcs_2025__text__p1` | 任务已从 cross_page 改为 text_lookup，但 metadata 还残留 `anchor_page` / `answer_page` / `anchor_phrase`。本轮清理掉这 3 个字段，只保留 `page` 与 `audit_note`。 |
| F4 | `epa_ghg_inventory_1990_2022__table__p41` | 将 CH4 / Percent Change 单元改为 `HFCs` × `2022` = `182.8`，避免当前 parser 把化学式下标和跨行表头拆散后造成 metadata 与解析文本不一致。 |
| F5 | `epa_ghg_inventory_1990_2022__table__p134` | p134 是续表页，解析结果没有重复列头 `2022`；题目改为定位 `Transportation` 行中 `28.5%` 前一个值，保留同一答案 `1,807.8`，删除 strict `column_label`。 |
| F6 | `ipcc_ar6_syr_longer_report__text__p50` | 当前 `read_page` 文本只稳定抽取到首个 heading `Section 3`，长 Table 3.1 caption 不在文本中；将 reference_answer 改回 `Section 3` 并收窄问题表述。 |

### Followup Validation

re-ran 5 项一致性自检：

- duplicate seed_id: 0
- numeric formula mismatch: 0
- table_lookup 缺 bbox: 0
- text_lookup metadata 残留 cross_page 字段: 0
- 总 seed 数: 54

Additional parser-alignment check after F4-F6:

- table_lookup bbox parse failure: 0
- EPA p41/p134 parser-label warnings: 0
- IPCC p50 text answer missing from `read_page`: 0
