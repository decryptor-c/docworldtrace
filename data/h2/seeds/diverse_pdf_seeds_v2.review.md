# Diverse PDF Seeds V2 Review

- Seed count: `54`
- Source: `data/h2/seeds/diverse_pdf_seeds_v1_corrected.jsonl`
- Output: `data/h2/seeds/diverse_pdf_seeds_v2.jsonl`

## V2 Fixes

### 2310.03302v2__cross__p1_p2
- Query now excludes figure captions.

### epa_ghg_inventory_1990_2022__numeric__p41
- GT -14.93% -> -14.94%.

### ipcc_ar6_syr_longer_report__table__p11
- Converted unreliable IPCC table seed to text_lookup.

### nasa_fy2025_budget_summary__cross__p2_p3
- GT shortened to first three words.

### nasa_fy2025_budget_summary__numeric__p4
- Query now makes the negative sign explicit.

### scotus_loper_bright_2024__text__p2
- Query now excludes the running page header.

### usgs_mcs_2025__text__p21
- Query now excludes page numbers.

## Seeds

### 1. `2308.06595v4__cross__p1_p2`
- doc_id: `2308.06595v4`
- task_type: `cross_page`
- question: First find the page about "visit bench a benchmark for vision". What is the heading or leading phrase on the next page?
- reference_answer: `1 Introduction`
- required_tools: `['search', 'read_page']`
- tool_hints: `{"target_page": 2}`

### 2. `2308.06595v4__refuse__generic`
- doc_id: `2308.06595v4`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 3. `2308.06595v4__verify__p4`
- doc_id: `2308.06595v4`
- task_type: `verification`
- question: Is the following claim supported by the document: "2 visit bench areal worldinspiredvlinstruction followingbenchmark"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 4}`

### 4. `2310.03302v2__cross__p1_p2`
- doc_id: `2310.03302v2`
- task_type: `cross_page`
- question: Use search to find the page about "mlagentbench evaluating language agents on". Then inspect the following page and report the running paper title printed at the very top of that page. Ignore figure captions such as "Starter Files".
- reference_answer: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- required_tools: `['search', 'read_page']`
- tool_hints: `{"target_page": 2}`

### 5. `2310.03302v2__refuse__generic`
- doc_id: `2310.03302v2`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 6. `2310.03302v2__text__p11`
- doc_id: `2310.03302v2`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 11?
- reference_answer: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 11}`

### 7. `2503.00808v4__cross__p1_p2`
- doc_id: `2503.00808v4`
- task_type: `cross_page`
- question: First find the page about "predictive data selection the data that". What is the heading or leading phrase on the next page?
- reference_answer: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- required_tools: `['search', 'read_page']`
- tool_hints: `{"target_page": 2}`

### 8. `2503.00808v4__refuse__generic`
- doc_id: `2503.00808v4`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 9. `2503.00808v4__text__p18`
- doc_id: `2503.00808v4`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 18?
- reference_answer: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 18}`

### 10. `apple_2025_10k__refuse__generic`
- doc_id: `apple_2025_10k`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 11. `apple_2025_10k__table__p3`
- doc_id: `apple_2025_10k`
- task_type: `table_lookup`
- question: In the table of contents on page 3, what page is "Item 1A. Risk Factors" listed on? Use the table on that page; do not answer from memory.
- reference_answer: `5`
- required_tools: `['read_page', 'parse_table']`
- tool_hints: `{"target_page": 3, "table_bbox_hint": [18.22499732062509, 161.3250228941237, 593.8874323986892, 241.95683198246488], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table"}`

### 12. `apple_2025_10k__text__p9`
- doc_id: `apple_2025_10k`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 9?
- reference_answer: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 9}`

### 13. `apple_2025_10k__verify__p18`
- doc_id: `apple_2025_10k`
- task_type: `verification`
- question: Is the following claim supported by the document: "the company is subject to an increasing number of federal state and international laws relating to the collection use retention protection and transfer of various types of personal data"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 18}`

### 14. `epa_ghg_inventory_1990_2022__cross__p2_p3`
- doc_id: `epa_ghg_inventory_1990_2022`
- task_type: `cross_page`
- question: Use search to find the page about "front cover photo credit for cow and digester". Then inspect the following page and report the heading or leading phrase.
- reference_answer: `HOW TO OBTAIN COPIES`
- required_tools: `['search', 'read_page']`
- tool_hints: `{"target_page": 3}`

### 15. `epa_ghg_inventory_1990_2022__numeric__p41`
- doc_id: `epa_ghg_inventory_1990_2022`
- task_type: `numeric_computation`
- question: Based on the table on page 41, in column "1990", compute the percentage by which the value in row "Net Emissions (Sources and Sinks)" (5560.2) differs from the value in row "Total Gross Emissions (Sources)" (6536.9). Report only the final result as a signed percentage with two decimals.
- reference_answer: `-14.94%`
- required_tools: `['parse_table', 'compute']`
- tool_hints: `{"target_page": 41, "table_bbox_hint": [74.904, 481.005997, 540.1, 694.289688947368], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table", "compute_note": "Use the numeric formula in the question and preserve the sign of the percentage change."}`

### 16. `epa_ghg_inventory_1990_2022__refuse__generic`
- doc_id: `epa_ghg_inventory_1990_2022`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 17. `epa_ghg_inventory_1990_2022__table__p41`
- doc_id: `epa_ghg_inventory_1990_2022`
- task_type: `table_lookup`
- question: On page 41, in the table, what is the value for row "HFCs" under column "2022"? Use the table evidence on that page; do not answer from memory.
- reference_answer: `182.8`
- required_tools: `['read_page', 'parse_table']`
- tool_hints: `{"target_page": 41, "table_bbox_hint": [74.904, 481.005997, 540.1, 694.289688947368], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table"}`

### 18. `epa_ghg_inventory_1990_2022__table__p134`
- doc_id: `epa_ghg_inventory_1990_2022`
- task_type: `table_lookup`
- question: On page 134, in the table, what value appears in the "Transportation" row immediately before the percent-change value "28.5%"? Use the table evidence on that page; do not answer from memory.
- reference_answer: `1,807.8`
- required_tools: `['read_page', 'parse_table']`
- tool_hints: `{"target_page": 134, "table_bbox_hint": [73.512, 83.78, 540.1, 707.85], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table"}`

### 19. `epa_ghg_inventory_1990_2022__verify__p41`
- doc_id: `epa_ghg_inventory_1990_2022`
- task_type: `verification`
- question: Is the following claim supported by the document: "total gross emissions in 2022 were 6 343 2 mmt co2 eq"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 41}`

### 20. `fda_ozempic_2025_label__numeric__p4`
- doc_id: `fda_ozempic_2025_label`
- task_type: `numeric_computation`
- question: Based on the table on page 4 ('DOSAGE FORMS AND STRENGTHS'), in the column "Total Strength per Total Volume" (mg per pen), compute the percentage increase from the 0.5 mg dose pen (2 mg / 3 mL) to the 1 mg dose pen (4 mg / 3 mL). Report only the final result as a signed percentage with two decimals.
- reference_answer: `100.00%`
- required_tools: `['parse_table', 'compute']`
- tool_hints: `{"target_page": 4, "table_bbox_hint": [36.239999999999995, 410.52, 303.8405, 495.3595], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table", "compute_note": "Use the numeric formula in the question and preserve the sign of the percentage change."}`

### 21. `fda_ozempic_2025_label__refuse__generic`
- doc_id: `fda_ozempic_2025_label`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 22. `fda_ozempic_2025_label__verify__p33`
- doc_id: `fda_ozempic_2025_label`
- task_type: `verification`
- question: Is the following claim supported by the document: "ozempic is injected under the skin subcutaneously of your stomach"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 33}`

### 23. `ipcc_ar6_syr_longer_report__refuse__generic`
- doc_id: `ipcc_ar6_syr_longer_report`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 24. `ipcc_ar6_syr_longer_report__text__p11`
- doc_id: `ipcc_ar6_syr_longer_report`
- task_type: `text_lookup`
- question: On page 11, what section heading appears at the top of the page? Return only the heading.
- reference_answer: `Current Status and Trends`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 11}`

### 25. `ipcc_ar6_syr_longer_report__text__p50`
- doc_id: `ipcc_ar6_syr_longer_report`
- task_type: `text_lookup`
- question: What is the first visible section heading on page 50?
- reference_answer: `Section 3`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 50}`

### 26. `ipcc_ar6_syr_longer_report__verify__p43`
- doc_id: `ipcc_ar6_syr_longer_report`
- task_type: `verification`
- question: Is the following claim supported by the document: "long term climate and development futures"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 43}`

### 27. `irs_2025_form_1040__refuse__generic`
- doc_id: `irs_2025_form_1040`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 28. `irs_2025_form_1040__verify__p2`
- doc_id: `irs_2025_form_1040`
- task_type: `verification`
- question: Is the following claim supported by the document: "subtract line 14 from line 11b if zero or less enter 0 this is your taxable income"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 2}`

### 29. `nasa_fy2025_budget_summary__cross__p2_p3`
- doc_id: `nasa_fy2025_budget_summary`
- task_type: `cross_page`
- question: Use search to find the page about "international space station while partnering with U.S. industry". Then inspect the following page and report only the first three words of the first bullet.
- reference_answer: `Drives scientific discovery`
- required_tools: `['search', 'read_page']`
- tool_hints: `{"target_page": 3}`

### 30. `nasa_fy2025_budget_summary__numeric__p4`
- doc_id: `nasa_fy2025_budget_summary`
- task_type: `numeric_computation`
- question: Based on the table on page 4, in column "FY 2023 Operating Plan", compute the signed percentage change from row "Deep Space Exploration Systems" (7447.6) to row "Space Operations" (4266.7), using (Space Operations - Deep Space Exploration Systems) / abs(Deep Space Exploration Systems) * 100. Report only the final signed percentage with two decimals.
- reference_answer: `-42.71%`
- required_tools: `['parse_table', 'compute']`
- tool_hints: `{"target_page": 4, "table_bbox_hint": [35.769999999999996, 54.08699999999999, 924.2299999999997, 503.0902222222222], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table", "compute_note": "Use the numeric formula in the question and preserve the sign of the percentage change."}`

### 31. `nasa_fy2025_budget_summary__refuse__generic`
- doc_id: `nasa_fy2025_budget_summary`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 32. `nasa_fy2025_budget_summary__table__p4`
- doc_id: `nasa_fy2025_budget_summary`
- task_type: `table_lookup`
- question: On page 4, in the table, what is the value for row "NASA Total" under column "FY 2025 Request"? Use the table evidence on that page; do not answer from memory.
- reference_answer: `25,383.7`
- required_tools: `['read_page', 'parse_table']`
- tool_hints: `{"target_page": 4, "table_bbox_hint": [35.769999999999996, 54.08699999999999, 924.2299999999997, 503.0902222222222], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table"}`

### 33. `nasa_fy2025_budget_summary__text__p4`
- doc_id: `nasa_fy2025_budget_summary`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 4?
- reference_answer: `NASA’s FY 2025 Budget Request`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 4}`

### 34. `nasa_fy2025_budget_summary__verify__p12`
- doc_id: `nasa_fy2025_budget_summary`
- task_type: `verification`
- question: Is the following claim supported by the document: "deep space exploration systems fy 2025 request equals 7 618 2 million"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 12}`

### 35. `nist_ai_600_1_genai_profile__cross__p2_p3`
- doc_id: `nist_ai_600_1_genai_profile`
- task_type: `cross_page`
- question: Use search to find the page about "gina m raimondo secretary". Then inspect the following page and report the heading or leading phrase.
- reference_answer: `About AI at NIST`
- required_tools: `['search', 'read_page']`
- tool_hints: `{"target_page": 3}`

### 36. `nist_ai_600_1_genai_profile__refuse__generic`
- doc_id: `nist_ai_600_1_genai_profile`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 37. `nist_ai_600_1_genai_profile__text__p5`
- doc_id: `nist_ai_600_1_genai_profile`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 5? Return the page summary or the first visible leading phrase exactly. Do not choose a later figure caption, table caption, or section title unless it is the first visible leading phrase.
- reference_answer: `1. Introduction`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 5}`

### 38. `nist_ai_600_1_genai_profile__verify__p54`
- doc_id: `nist_ai_600_1_genai_profile`
- task_type: `verification`
- question: Is the following claim supported by the document: "participatory engagement methods"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 54}`

### 39. `scotus_loper_bright_2024__refuse__generic`
- doc_id: `scotus_loper_bright_2024`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 40. `scotus_loper_bright_2024__text__p2`
- doc_id: `scotus_loper_bright_2024`
- task_type: `text_lookup`
- question: On page 2, ignore the running page header line "2 LOPER BRIGHT ENTERPRISES v. RAIMONDO". What section heading appears immediately below that header? Return only the heading.
- reference_answer: `Syllabus`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 2}`

### 41. `scotus_loper_bright_2024__verify__p4`
- doc_id: `scotus_loper_bright_2024`
- task_type: `verification`
- question: Is the following claim supported by the document: "chevron rested on a presumption that congress when it left ambiguity in a statute meant for implementation by an agency"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 4}`

### 42. `ti2025ars__numeric__p97`
- doc_id: `ti2025ars`
- task_type: `numeric_computation`
- question: Based on the table on page 97, for column "2025 Absolute Performance", what is the percentage change from row "Revenue Growth: Total TI" (13) to row "Profit from Operations as a % of Revenue
(Operating Profit Margin)" (34.1)?
- reference_answer: `162.31%`
- required_tools: `['parse_table', 'compute']`
- tool_hints: `{"target_page": 97, "table_bbox_hint": [84.96, 114.0, 562.71002, 215.25], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table", "compute_note": "Use the numeric formula in the question and preserve the sign of the percentage change."}`

### 43. `ti2025ars__refuse__generic`
- doc_id: `ti2025ars`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 44. `ti2025ars__table__p7`
- doc_id: `ti2025ars`
- task_type: `table_lookup`
- question: On page 7, in the table, what is the value for row "Common Stock, par value $1.00" under column "Trading Symbol(s)"?
- reference_answer: `TXN`
- required_tools: `['read_page', 'parse_table']`
- tool_hints: `{"target_page": 7, "table_bbox_hint": [49.5, 335.89999, 562.5, 364.39999], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table"}`

### 45. `ti2025ars__text__p42`
- doc_id: `ti2025ars`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 42?
- reference_answer: `Government incentives`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 42}`

### 46. `tm2529296d2_ars__numeric__p2`
- doc_id: `tm2529296d2_ars`
- task_type: `numeric_computation`
- question: Based on the table on page 2, for column "High-Touch Solutions N.A.", what is the percentage change from row "Revenue" (14) to row "Reported sales growth" (2)?
- reference_answer: `-85.71%`
- required_tools: `['parse_table', 'compute']`
- tool_hints: `{"target_page": 2, "table_bbox_hint": [35.94, 333.96, 535.455, 458.2800500000001], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table", "compute_note": "Use the numeric formula in the question and preserve the sign of the percentage change."}`

### 47. `tm2529296d2_ars__refuse__generic`
- doc_id: `tm2529296d2_ars`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 48. `tm2529296d2_ars__table__p2`
- doc_id: `tm2529296d2_ars`
- task_type: `table_lookup`
- question: On page 2, in the table, what is the value for row "Revenue" under column "High-Touch Solutions N.A."?
- reference_answer: `$14.0B`
- required_tools: `['read_page', 'parse_table']`
- tool_hints: `{"target_page": 2, "table_bbox_hint": [35.94, 333.96, 535.455, 458.2800500000001], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table"}`

### 49. `tm2529296d2_ars__text__p27`
- doc_id: `tm2529296d2_ars`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 27?
- reference_answer: `Technology Risks`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 27}`

### 50. `tm2529296d2_ars__verify__p81`
- doc_id: `tm2529296d2_ars`
- task_type: `verification`
- question: Is the following claim supported by the document: "10 2 frozen executive death benefit plan as amended incorporated"? Answer SUPPORTED or UNSUPPORTED.
- reference_answer: `SUPPORTED`
- required_tools: `['search', 'read_page', 'verify']`
- tool_hints: `{"target_page": 81}`

### 51. `usgs_mcs_2025__text__p1`
- doc_id: `usgs_mcs_2025`
- task_type: `text_lookup`
- question: What is the heading or leading phrase on page 1? Return the page summary or the first visible leading phrase exactly. Do not choose a later figure caption, table caption, or section title unless it is the first visible leading phrase.
- reference_answer: `U.S. Department of the Interior`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 1}`

### 52. `usgs_mcs_2025__refuse__generic`
- doc_id: `usgs_mcs_2025`
- task_type: `unanswerable`
- question: What is the private mobile phone number of the first author or CEO listed in the document?
- reference_answer: `REFUSE`
- required_tools: `['search', 'read_page', 'refuse']`

### 53. `usgs_mcs_2025__table__p21`
- doc_id: `usgs_mcs_2025`
- task_type: `table_lookup`
- question: On page 21, in the table, what is the value for row "Aluminum" under column "Applications"?
- reference_answer: `Metallurgy and many sectors of the economy.`
- required_tools: `['read_page', 'parse_table']`
- tool_hints: `{"target_page": 21, "table_bbox_hint": [49.645714285714284, 59.639999999999986, 561.8314285714287, 696.16], "bbox_note": "Use this bbox as the first parse_table/crop region; it covers the relevant table.", "preferred_first_tool": "parse_table"}`

### 54. `usgs_mcs_2025__text__p21`
- doc_id: `usgs_mcs_2025`
- task_type: `text_lookup`
- question: On page 21, ignore page numbers and footnote markers. What table caption begins the page? Return the caption text only.
- reference_answer: `Table 4.—The 2022 U.S. Critical Minerals List`
- required_tools: `['read_page']`
- tool_hints: `{"target_page": 21}`
