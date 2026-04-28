# H2 Seed Review Draft

人工审查重点：question 是否无歧义，reference_answer 是否能由 supporting_refs 直接验证，unanswerable 是否确实不可回答。

## 2308.06595v4__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "visit bench a benchmark for vision". What is the heading or leading phrase on the next page?
- Reference: `1 Introduction`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "visit bench a benchmark for vision", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2308.06595v4__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2308.06595v4__table__p3

- Type: `table_lookup`
- Question: On page 3, in the table, what is the value for row "How much is the
browser usage for
Firefox and Safari?" under column "Art Knowledge"?
- Reference: `Teach me about this
painting.`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 3, "bbox": [113.47879446279998, 73.13514863924, 263.77319592, 167.6252836]}]`
- Metadata: `{"page": 3, "bbox": [113.47879446279998, 73.13514863924, 263.77319592, 167.6252836], "row_label": "How much is the\nbrowser usage for\nFirefox and Safari?", "column_label": "Art Knowledge", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2308.06595v4__text__p7

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 7?
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Required tools: `read_page`
- Supporting refs: `[{"page": 7}]`
- Metadata: `{"page": 7}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2308.06595v4__verify__p4

- Type: `verification`
- Question: Is the following claim supported by the document: "2 visit bench areal worldinspiredvlinstruction followingbenchmark"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 4}]`
- Metadata: `{"page": 4, "claim": "2 visit bench areal worldinspiredvlinstruction followingbenchmark"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2310.03302v2__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "mlagentbench evaluating language agents on". What is the heading or leading phrase on the next page?
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "mlagentbench evaluating language agents on", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2310.03302v2__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2310.03302v2__text__p11

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 11?
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Required tools: `read_page`
- Supporting refs: `[{"page": 11}]`
- Metadata: `{"page": 11}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2503.00808v4__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "predictive data selection the data that". What is the heading or leading phrase on the next page?
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "predictive data selection the data that", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2503.00808v4__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## 2503.00808v4__text__p18

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 18?
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Required tools: `read_page`
- Supporting refs: `[{"page": 18}]`
- Metadata: `{"page": 18}`
- Human review: PASS / REVISE / DROP
- Notes:

## apple_2025_10k__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## apple_2025_10k__table__p3

- Type: `table_lookup`
- Question: On page 3, in the table, what is the value for row "Item 1A." under column "Business"?
- Reference: `Risk Factors`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 3, "bbox": [18.22499732062509, 161.3250228941237, 593.8874323986892, 241.95683198246488]}]`
- Metadata: `{"page": 3, "bbox": [18.22499732062509, 161.3250228941237, 593.8874323986892, 241.95683198246488], "row_label": "Item 1A.", "column_label": "Business", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## apple_2025_10k__text__p9

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 9?
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Required tools: `read_page`
- Supporting refs: `[{"page": 9}]`
- Metadata: `{"page": 9}`
- Human review: PASS / REVISE / DROP
- Notes:

## apple_2025_10k__verify__p18

- Type: `verification`
- Question: Is the following claim supported by the document: "the company s business is subject to a variety of"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 18}]`
- Metadata: `{"page": 18, "claim": "the company s business is subject to a variety of"}`
- Human review: PASS / REVISE / DROP
- Notes:

## epa_ghg_inventory_1990_2022__cross__p2_p3

- Type: `cross_page`
- Question: First find the page about "front cover photo credit for cow". What is the heading or leading phrase on the next page?
- Reference: `HOW TO OBTAIN COPIES`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 3}]`
- Metadata: `{"anchor_page": 2, "answer_page": 3, "anchor_phrase": "front cover photo credit for cow", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## epa_ghg_inventory_1990_2022__numeric__p41

- Type: `numeric_computation`
- Question: Based on the table on page 41, for column "Percent", what is the percentage change from row "Gas/Source" (1990) to row "CH (excludes LULUCF sources)a
4" (-19.4)?
- Reference: `-100.97%`
- Required tools: `parse_table, compute`
- Supporting refs: `[{"page": 41, "bbox": [74.904, 481.005997, 540.1, 694.289688947368]}]`
- Metadata: `{"page": 41, "bbox": [74.904, 481.005997, 540.1, 694.289688947368], "column_label": "Percent", "first_label": "Gas/Source", "second_label": "CH (excludes LULUCF sources)a\n4", "first_value": 1990.0, "second_value": -19.4, "formula": "(second_value - first_value) / abs(first_value) * 100", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## epa_ghg_inventory_1990_2022__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## epa_ghg_inventory_1990_2022__table__p41

- Type: `table_lookup`
- Question: On page 41, in the table, what is the value for row "Gas/Source" under column "Percent"?
- Reference: `1990`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 41, "bbox": [74.904, 481.005997, 540.1, 694.289688947368]}]`
- Metadata: `{"page": 41, "bbox": [74.904, 481.005997, 540.1, 694.289688947368], "row_label": "Gas/Source", "column_label": "Percent", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## epa_ghg_inventory_1990_2022__text__p134

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 134?
- Reference: `CO 2 1,173.8 1,136.4 1,110.7 1,118.3 1,036.9 1,071.1 1,080.8 17.0%`
- Required tools: `read_page`
- Supporting refs: `[{"page": 134}]`
- Metadata: `{"page": 134}`
- Human review: PASS / REVISE / DROP
- Notes:

## epa_ghg_inventory_1990_2022__verify__p697

- Type: `verification`
- Question: Is the following claim supported by the document: "lake forest park wa 12 76 2 63 0 49"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 697}]`
- Metadata: `{"page": 697, "claim": "lake forest park wa 12 76 2 63 0 49"}`
- Human review: PASS / REVISE / DROP
- Notes:

## fda_ozempic_2025_label__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "highlights of prescribing information contraindications". What is the heading or leading phrase on the next page?
- Reference: `FULL PRESCRIBING INFORMATION: CONTENTS* 8.6Renal Impairment`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "highlights of prescribing information contraindications", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## fda_ozempic_2025_label__numeric__p4

- Type: `numeric_computation`
- Question: Based on the table on page 4, for column "Total Strength
per Total Volume", what is the percentage change from row "0.25 mg
0.5 mg" (2) to row "1 mg" (4)?
- Reference: `100.00%`
- Required tools: `parse_table, compute`
- Supporting refs: `[{"page": 4, "bbox": [36.239999999999995, 410.52, 303.8405, 495.3595]}]`
- Metadata: `{"page": 4, "bbox": [36.239999999999995, 410.52, 303.8405, 495.3595], "column_label": "Total Strength\nper Total Volume", "first_label": "0.25 mg\n0.5 mg", "second_label": "1 mg", "first_value": 2.0, "second_value": 4.0, "formula": "(second_value - first_value) / abs(first_value) * 100", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## fda_ozempic_2025_label__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## fda_ozempic_2025_label__table__p4

- Type: `table_lookup`
- Question: On page 4, in the table, what is the value for row "0.25 mg
0.5 mg" under column "Total Strength
per Total Volume"?
- Reference: `2 mg / 3 mL`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 4, "bbox": [36.239999999999995, 410.52, 303.8405, 495.3595]}]`
- Metadata: `{"page": 4, "bbox": [36.239999999999995, 410.52, 303.8405, 495.3595], "row_label": "0.25 mg\n0.5 mg", "column_label": "Total Strength\nper Total Volume", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## fda_ozempic_2025_label__text__p1

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 1?
- Reference: `HIGHLIGHTS OF PRESCRIBING INFORMATION --------------------------------CONTRAINDICATIONS--------------------------------`
- Required tools: `read_page`
- Supporting refs: `[{"page": 1}]`
- Metadata: `{"page": 1}`
- Human review: PASS / REVISE / DROP
- Notes:

## fda_ozempic_2025_label__verify__p33

- Type: `verification`
- Question: Is the following claim supported by the document: "ozempic is injected under the skin subcutaneously of your stomach"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 33}]`
- Metadata: `{"page": 33, "claim": "ozempic is injected under the skin subcutaneously of your stomach"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ipcc_ar6_syr_longer_report__numeric__p11

- Type: `numeric_computation`
- Question: Based on the table on page 11, for column "Africa", what is the percentage change from row "Population (million persons, 2019)" (1292) to row "GDP per capita (USD1000PPP 2017 per person) 1" (5)?
- Reference: `-99.61%`
- Required tools: `parse_table, compute`
- Supporting refs: `[{"page": 11, "bbox": [53.022, 598.03, 556.283, 725.009]}]`
- Metadata: `{"page": 11, "bbox": [53.022, 598.03, 556.283, 725.009], "column_label": "Africa", "first_label": "Population (million persons, 2019)", "second_label": "GDP per capita (USD1000PPP 2017 per person) 1", "first_value": 1292.0, "second_value": 5.0, "formula": "(second_value - first_value) / abs(first_value) * 100", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ipcc_ar6_syr_longer_report__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ipcc_ar6_syr_longer_report__table__p11

- Type: `table_lookup`
- Question: On page 11, in the table, what is the value for row "Population (million persons, 2019)" under column "Africa"?
- Reference: `1292`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 11, "bbox": [53.022, 598.03, 556.283, 725.009]}]`
- Metadata: `{"page": 11, "bbox": [53.022, 598.03, 556.283, 725.009], "row_label": "Population (million persons, 2019)", "column_label": "Africa", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ipcc_ar6_syr_longer_report__text__p50

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 50?
- Reference: `Section 3`
- Required tools: `read_page`
- Supporting refs: `[{"page": 50}]`
- Metadata: `{"page": 50}`
- Human review: PASS / REVISE / DROP
- Notes:

## ipcc_ar6_syr_longer_report__verify__p43

- Type: `verification`
- Question: Is the following claim supported by the document: "long term climate and development futures"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 43}]`
- Metadata: `{"page": 43, "claim": "long term climate and development futures"}`
- Human review: PASS / REVISE / DROP
- Notes:

## irs_2025_form_1040__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "mrof 1040 department of the treasury". What is the heading or leading phrase on the next page?
- Reference: `Form 1040 (2025) Page 2`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "mrof 1040 department of the treasury", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## irs_2025_form_1040__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## irs_2025_form_1040__table__p1

- Type: `table_lookup`
- Question: On page 1, in the table, what is the value for row "(5) Check if lived
with you more
than half of 2025" under column "Dependent 1"?
- Reference: `(a) Yes
(b) And in the U.S.`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 1, "bbox": [91.599, 295.85714285714283, 576.0, 423.27009090909087]}]`
- Metadata: `{"page": 1, "bbox": [91.599, 295.85714285714283, 576.0, 423.27009090909087], "row_label": "(5) Check if lived\nwith you more\nthan half of 2025", "column_label": "Dependent 1", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## irs_2025_form_1040__text__p1

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 1?
- Reference: `mroF 1040 Department of the Treasury—Internal Revenue Service 2025`
- Required tools: `read_page`
- Supporting refs: `[{"page": 1}]`
- Metadata: `{"page": 1}`
- Human review: PASS / REVISE / DROP
- Notes:

## irs_2025_form_1040__verify__p2

- Type: `verification`
- Question: Is the following claim supported by the document: "form 1040 2025 page 2"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"page": 2, "claim": "form 1040 2025 page 2"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nasa_fy2025_budget_summary__cross__p2_p3

- Type: `cross_page`
- Question: First find the page about "advancing u s leadership in exploration". What is the heading or leading phrase on the next page?
- Reference: `Advancing U.S. Leadership in Exploration and Discovery`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 3}]`
- Metadata: `{"anchor_page": 2, "answer_page": 3, "anchor_phrase": "advancing u s leadership in exploration", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nasa_fy2025_budget_summary__numeric__p4

- Type: `numeric_computation`
- Question: Based on the table on page 4, for column "FY 2023
Operating
Plan1/", what is the percentage change from row "Deep Space Exploration Systems" (7447.6) to row "Space Operations" (4266.7)?
- Reference: `-42.71%`
- Required tools: `parse_table, compute`
- Supporting refs: `[{"page": 4, "bbox": [35.769999999999996, 54.08699999999999, 924.2299999999997, 503.0902222222222]}]`
- Metadata: `{"page": 4, "bbox": [35.769999999999996, 54.08699999999999, 924.2299999999997, 503.0902222222222], "column_label": "FY 2023\nOperating\nPlan1/", "first_label": "Deep Space Exploration Systems", "second_label": "Space Operations", "first_value": 7447.6, "second_value": 4266.7, "formula": "(second_value - first_value) / abs(first_value) * 100", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nasa_fy2025_budget_summary__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nasa_fy2025_budget_summary__table__p4

- Type: `table_lookup`
- Question: On page 4, in the table, what is the value for row "Budget Authority ($M)" under column "FY 2025 Request"?
- Reference: `FY 2025
Request`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 4, "bbox": [35.769999999999996, 54.08699999999999, 924.2299999999997, 503.0902222222222]}]`
- Metadata: `{"page": 4, "bbox": [35.769999999999996, 54.08699999999999, 924.2299999999997, 503.0902222222222], "row_label": "Budget Authority ($M)", "column_label": "FY 2025 Request", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nasa_fy2025_budget_summary__text__p4

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 4?
- Reference: `NASA’s FY 2025 Budget Request`
- Required tools: `read_page`
- Supporting refs: `[{"page": 4}]`
- Metadata: `{"page": 4}`
- Human review: PASS / REVISE / DROP
- Notes:

## nasa_fy2025_budget_summary__verify__p12

- Type: `verification`
- Question: Is the following claim supported by the document: "nasa s fy 2025 budget request"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 12}]`
- Metadata: `{"page": 12, "claim": "nasa s fy 2025 budget request"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nist_ai_600_1_genai_profile__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "nist trustworthy and responsible ai". What is the heading or leading phrase on the next page?
- Reference: `NIST Trustworthy and Responsible AI`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "nist trustworthy and responsible ai", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nist_ai_600_1_genai_profile__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nist_ai_600_1_genai_profile__table__p29

- Type: `table_lookup`
- Question: On page 29, in the table, what is the value for row "MP-2.3-003" under column "Harmful Bias and Homogenization;
Intellectual Property"?
- Reference: `Information Integrity`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 29, "bbox": [28.8779661016949, 72.19999999999999, 575.9932203389831, 283.6]}]`
- Metadata: `{"page": 29, "bbox": [28.8779661016949, 72.19999999999999, 575.9932203389831, 283.6], "row_label": "MP-2.3-003", "column_label": "Harmful Bias and Homogenization;\nIntellectual Property", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## nist_ai_600_1_genai_profile__text__p7

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 7?
- Reference: `the abuse, misuse, and unsafe repurposing by humans (adversarial or not), and others result`
- Required tools: `read_page`
- Supporting refs: `[{"page": 7}]`
- Metadata: `{"page": 7}`
- Human review: PASS / REVISE / DROP
- Notes:

## nist_ai_600_1_genai_profile__verify__p54

- Type: `verification`
- Question: Is the following claim supported by the document: "participatory engagement methods"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 54}]`
- Metadata: `{"page": 54, "claim": "participatory engagement methods"}`
- Human review: PASS / REVISE / DROP
- Notes:

## scotus_loper_bright_2024__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "slip opinion october term 2023 1". What is the heading or leading phrase on the next page?
- Reference: `2 LOPER BRIGHT ENTERPRISES v. RAIMONDO`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "slip opinion october term 2023 1", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## scotus_loper_bright_2024__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## scotus_loper_bright_2024__text__p2

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 2?
- Reference: `2 LOPER BRIGHT ENTERPRISES v. RAIMONDO`
- Required tools: `read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"page": 2}`
- Human review: PASS / REVISE / DROP
- Notes:

## scotus_loper_bright_2024__verify__p4

- Type: `verification`
- Question: Is the following claim supported by the document: "4 loper bright enterprises v raimondo"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 4}]`
- Metadata: `{"page": 4, "claim": "4 loper bright enterprises v raimondo"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ti2025ars__numeric__p97

- Type: `numeric_computation`
- Question: Based on the table on page 97, for column "2025 Absolute Performance", what is the percentage change from row "Revenue Growth: Total TI" (13) to row "Profit from Operations as a % of Revenue
(Operating Profit Margin)" (34.1)?
- Reference: `162.31%`
- Required tools: `parse_table, compute`
- Supporting refs: `[{"page": 97, "bbox": [84.96, 114.0, 562.71002, 215.25]}]`
- Metadata: `{"page": 97, "bbox": [84.96, 114.0, 562.71002, 215.25], "column_label": "2025 Absolute Performance", "first_label": "Revenue Growth: Total TI", "second_label": "Profit from Operations as a % of Revenue\n(Operating Profit Margin)", "first_value": 13.0, "second_value": 34.1, "formula": "(second_value - first_value) / abs(first_value) * 100", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ti2025ars__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ti2025ars__table__p7

- Type: `table_lookup`
- Question: On page 7, in the table, what is the value for row "Common Stock, par value $1.00" under column "Trading Symbol(s)"?
- Reference: `TXN`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 7, "bbox": [49.5, 335.89999, 562.5, 364.39999]}]`
- Metadata: `{"page": 7, "bbox": [49.5, 335.89999, 562.5, 364.39999], "row_label": "Common Stock, par value $1.00", "column_label": "Trading Symbol(s)", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## ti2025ars__text__p42

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 42?
- Reference: `Government incentives`
- Required tools: `read_page`
- Supporting refs: `[{"page": 42}]`
- Metadata: `{"page": 42}`
- Human review: PASS / REVISE / DROP
- Notes:

## tm2529296d2_ars__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "2025 annual report". What is the heading or leading phrase on the next page?
- Reference: `About Us Shareholder and Media Information`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "2025 annual report", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## tm2529296d2_ars__numeric__p2

- Type: `numeric_computation`
- Question: Based on the table on page 2, for column "High-Touch Solutions N.A.", what is the percentage change from row "Revenue" (14) to row "Reported sales growth" (2)?
- Reference: `-85.71%`
- Required tools: `parse_table, compute`
- Supporting refs: `[{"page": 2, "bbox": [35.94, 333.96, 535.455, 458.2800500000001]}]`
- Metadata: `{"page": 2, "bbox": [35.94, 333.96, 535.455, 458.2800500000001], "column_label": "High-Touch Solutions N.A.", "first_label": "Revenue", "second_label": "Reported sales growth", "first_value": 14.0, "second_value": 2.0, "formula": "(second_value - first_value) / abs(first_value) * 100", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## tm2529296d2_ars__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## tm2529296d2_ars__table__p2

- Type: `table_lookup`
- Question: On page 2, in the table, what is the value for row "Revenue" under column "High-Touch Solutions N.A."?
- Reference: `$14.0B`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 2, "bbox": [35.94, 333.96, 535.455, 458.2800500000001]}]`
- Metadata: `{"page": 2, "bbox": [35.94, 333.96, 535.455, 458.2800500000001], "row_label": "Revenue", "column_label": "High-Touch Solutions N.A.", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## tm2529296d2_ars__text__p27

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 27?
- Reference: `Technology Risks`
- Required tools: `read_page`
- Supporting refs: `[{"page": 27}]`
- Metadata: `{"page": 27}`
- Human review: PASS / REVISE / DROP
- Notes:

## tm2529296d2_ars__verify__p81

- Type: `verification`
- Question: Is the following claim supported by the document: "10 2 frozen executive death benefit plan as amended incorporated"? Answer SUPPORTED or UNSUPPORTED.
- Reference: `SUPPORTED`
- Required tools: `search, read_page, verify`
- Supporting refs: `[{"page": 81}]`
- Metadata: `{"page": 81, "claim": "10 2 frozen executive death benefit plan as amended incorporated"}`
- Human review: PASS / REVISE / DROP
- Notes:

## usgs_mcs_2025__cross__p1_p2

- Type: `cross_page`
- Question: First find the page about "u s department of the interior". What is the heading or leading phrase on the next page?
- Reference: `Cover: Photograph of 1 of the 66 antennas that make up the Atacama Large Millimeter/submillimeter Array`
- Required tools: `search, read_page`
- Supporting refs: `[{"page": 2}]`
- Metadata: `{"anchor_page": 1, "answer_page": 2, "anchor_phrase": "u s department of the interior", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## usgs_mcs_2025__refuse__generic

- Type: `unanswerable`
- Question: What is the private mobile phone number of the first author or CEO listed in the document?
- Reference: `REFUSE`
- Required tools: `search, read_page, refuse`
- Supporting refs: `[]`
- Metadata: `{"review_status": "needs_human_review", "negative_evidence_query": "private mobile phone number first author CEO"}`
- Human review: PASS / REVISE / DROP
- Notes:

## usgs_mcs_2025__table__p21

- Type: `table_lookup`
- Question: On page 21, in the table, what is the value for row "Aluminum" under column "Applications"?
- Reference: `Metallurgy and many sectors of the economy.`
- Required tools: `read_page, parse_table`
- Supporting refs: `[{"page": 21, "bbox": [49.645714285714284, 59.639999999999986, 561.8314285714287, 696.16]}]`
- Metadata: `{"page": 21, "bbox": [49.645714285714284, 59.639999999999986, 561.8314285714287, 696.16], "row_label": "Aluminum", "column_label": "Applications", "review_status": "needs_human_review"}`
- Human review: PASS / REVISE / DROP
- Notes:

## usgs_mcs_2025__text__p18

- Type: `text_lookup`
- Question: What is the heading or leading phrase on page 18?
- Reference: `Figure 6.—Value of Other Industrial Minerals Produced in 2024, by Region`
- Required tools: `read_page`
- Supporting refs: `[{"page": 18}]`
- Metadata: `{"page": 18}`
- Human review: PASS / REVISE / DROP
- Notes:
