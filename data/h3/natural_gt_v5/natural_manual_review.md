# H3 Natural-Distribution Manual GT Sample

- Source DocVerify review: `data/h3/docverify_plus_v5/docverify_review.json`
- Sample count: `100`

Labels to fill:

- `human_support_label`: one of `SUPPORTED`, `PARTIAL`, `NOT_SUPPORTED`, `INSUFFICIENT`, `INVALID`
- `human_sufficiency`: one of `SUFFICIENT`, `INSUFFICIENT`, `MISSING`, `INVALID`
- `human_filter_decision`: one of `keep`, `review`, `reject`
- `human_tool_path_reasonable_1_to_5`: integer score for tool-path reasonableness

| # | Auto | Task | Teacher | Seed | Adjusted | Final | Human Notes |
|---:|---|---|---|---|---:|---|---|
| 1 | `reject/INVALID/INVALID` | `numeric_computation` | `dmxapi_gemini_2_5_flash` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `False` | `None: None` |  |
| 2 | `review/PARTIAL/INSUFFICIENT` | `table_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `ti2025ars__table__p7` | `True` | `answer: The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.` |  |
| 3 | `reject/NOT_SUPPORTED/INSUFFICIENT` | `verification` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__verify__p4` | `True` | `answer: SUPPORTED` |  |
| 4 | `reject/NOT_SUPPORTED/INSUFFICIENT` | `verification` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__verify__p4` | `True` | `answer: SUPPORTED` |  |
| 5 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__cross__p1_p2` | `True` | `answer: 1 Introduction` |  |
| 6 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__cross__p1_p2` | `True` | `answer: The heading on the page following the VisIT-Bench benchmark description is '1 Introduction'.` |  |
| 7 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__cross__p1_p2` | `True` | `answer: 1 Introduction` |  |
| 8 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_2_5_flash` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `True` | `answer: 7.0 percentage points` |  |
| 9 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_3_1_flash_lite_preview` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `True` | `answer: 7.0 percentage points` |  |
| 10 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gpt4o_2024_11_20` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `True` | `answer: 7 percentage points` |  |
| 11 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gemini_2_5_flash` | `ti2025ars__table__p7` | `True` | `answer: TXN` |  |
| 12 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `ti2025ars__table__p7` | `True` | `answer: The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.` |  |
| 13 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gpt4o_2024_11_20` | `ti2025ars__table__p7` | `True` | `answer: The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.` |  |
| 14 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__text__p7` | `True` | `answer: BLIP2 Caption It is not possible to determine if a` |  |
| 15 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__text__p7` | `True` | `answer: BLIP2 Caption` |  |
| 16 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__text__p7` | `True` | `answer: BLIP2 Caption It is not possible to determine if a` |  |
| 17 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__refuse__external_fact` | `True` | `refuse: The document does not provide information about the current physical location of the paper's first author. The search results and the content of page 24, which was the most relevant search result, did not contain any such details.` |  |
| 18 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__refuse__external_fact` | `True` | `refuse: The document lists the authors but does not provide any information about their current physical location.` |  |
| 19 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__refuse__external_fact` | `True` | `refuse: The document does not provide information about the current physical location of the first author, as confirmed by searching and reviewing relevant pages.` |  |
| 20 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__verify__p81` | `True` | `answer: SUPPORTED` |  |
| 21 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__verify__p4` | `True` | `answer: SUPPORTED` |  |
| 22 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__verify__p4` | `True` | `answer: SUPPORTED` |  |
| 23 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__cross__p1_p2` | `True` | `answer: 1 Introduction` |  |
| 24 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__cross__p1_p2` | `True` | `answer: The heading on page 2 is '1 Introduction'.` |  |
| 25 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__cross__p1_p2` | `True` | `answer: 1 Introduction` |  |
| 26 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__numeric_margin_change_p2` | `True` | `answer: 14.8 percentage points` |  |
| 27 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_3_1_flash_lite_preview` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `True` | `answer: 7.0 percentage points` |  |
| 28 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gpt4o_2024_11_20` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `True` | `answer: 7 percentage points` |  |
| 29 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gemini_2_5_flash` | `ti2025ars__table__p7` | `True` | `answer: TXN` |  |
| 30 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__table__p2` | `True` | `answer: $14.0B` |  |
| 31 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gpt4o_2024_11_20` | `ti2025ars__table__p7` | `True` | `answer: The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.` |  |
| 32 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__text__p7` | `True` | `answer: BLIP2 Caption It is not possible to determine if a` |  |
| 33 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__text__p7` | `True` | `answer: BLIP2 Caption` |  |
| 34 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__text__p7` | `True` | `answer: BLIP2 Caption It is not possible to determine if a` |  |
| 35 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_2_5_flash` | `2308.06595v4__refuse__external_fact` | `True` | `refuse: The document does not provide information about the current physical location of the paper's first author. I have searched for relevant terms and read the introductory pages, but no such details were found.` |  |
| 36 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__refuse__external_fact` | `True` | `refuse: The document does not provide information regarding the current physical location of the paper's first author.` |  |
| 37 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__refuse__external_fact` | `True` | `refuse: The document does not provide information about the current physical location of the first author.` |  |
| 38 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__verify__p81` | `True` | `answer: SUPPORTED` |  |
| 39 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gemini_3_1_flash_lite_preview` | `2308.06595v4__verify__p4` | `True` | `answer: SUPPORTED` |  |
| 40 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gpt4o_2024_11_20` | `2308.06595v4__verify__p4` | `True` | `answer: SUPPORTED` |  |
| 41 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_2_5_flash` | `2310.03302v2__cross__p1_p2` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 42 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_3_1_flash_lite_preview` | `2310.03302v2__cross__p1_p2` | `True` | `answer: The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.` |  |
| 43 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gpt4o_2024_11_20` | `2310.03302v2__cross__p1_p2` | `True` | `answer: MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation` |  |
| 44 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__numeric_margin_change_p2` | `True` | `answer: 14.8 percentage points` |  |
| 45 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__numeric_margin_change_p2` | `True` | `answer: 14.8 percentage points` |  |
| 46 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__numeric_margin_change_p2` | `True` | `answer: 14.8 percentage points` |  |
| 47 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__table__p2` | `True` | `answer: $14.0B` |  |
| 48 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__table__p2` | `True` | `answer: $14.0B` |  |
| 49 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__table__p2` | `True` | `answer: $14.0B` |  |
| 50 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_2_5_flash` | `2310.03302v2__text__p11` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 51 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `2310.03302v2__text__p11` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 52 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gpt4o_2024_11_20` | `2310.03302v2__text__p11` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 53 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_2_5_flash` | `2310.03302v2__refuse__legal_risk` | `True` | `refuse: The document does not disclose any confidential or non-public legal case number or regulatory investigation ID for the authors or their institution. Searches for relevant terms yielded no results, and reviewing a sample page confirmed the absence of such information.` |  |
| 54 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_3_1_flash_lite_preview` | `2310.03302v2__refuse__legal_risk` | `True` | `refuse: The document is a research paper on machine learning and does not contain any confidential legal case numbers or regulatory investigation IDs.` |  |
| 55 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gpt4o_2024_11_20` | `2310.03302v2__refuse__legal_risk` | `True` | `refuse: The document does not disclose any confidential or non-public legal case numbers or regulatory investigation IDs for the authors or their institution, as confirmed by the search and review of relevant pages.` |  |
| 56 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__verify__p81` | `True` | `answer: SUPPORTED` |  |
| 57 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__verify__p81` | `True` | `answer: SUPPORTED` |  |
| 58 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_2_5_flash` | `2310.03302v2__cross__p1_p2` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 59 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_3_1_flash_lite_preview` | `2310.03302v2__cross__p1_p2` | `True` | `answer: The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.` |  |
| 60 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gpt4o_2024_11_20` | `2310.03302v2__cross__p1_p2` | `True` | `answer: MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation` |  |
| 61 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__numeric_total_growth_gap_p2` | `True` | `answer: 0.4 percentage points` |  |
| 62 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__numeric_margin_change_p2` | `True` | `answer: 14.8 percentage points` |  |
| 63 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__numeric_margin_change_p2` | `True` | `answer: 14.8 percentage points` |  |
| 64 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__table__p2` | `True` | `answer: $14.0B` |  |
| 65 | `keep/SUPPORTED/SUFFICIENT` | `table_lookup` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__table__p2` | `True` | `answer: $14.0B` |  |
| 66 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_2_5_flash` | `2310.03302v2__text__p11` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 67 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `2310.03302v2__text__p11` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 68 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gpt4o_2024_11_20` | `2310.03302v2__text__p11` | `True` | `answer: MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation` |  |
| 69 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_2_5_flash` | `2310.03302v2__refuse__legal_risk` | `True` | `refuse: The document does not disclose any confidential or non-public legal case numbers or regulatory investigation IDs for the authors or their institution. Searches for relevant terms yielded no results, and a review of page 3 confirmed the absence of such information.` |  |
| 70 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_3_1_flash_lite_preview` | `2310.03302v2__refuse__legal_risk` | `True` | `refuse: The document is a research paper and does not contain any information regarding confidential legal cases or regulatory investigation IDs.` |  |
| 71 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gpt4o_2024_11_20` | `2310.03302v2__refuse__legal_risk` | `True` | `refuse: The document does not disclose any confidential or non-public legal case numbers or regulatory investigation IDs for the authors or their institution, as confirmed by searching and reviewing relevant pages.` |  |
| 72 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__verify__p81` | `True` | `answer: SUPPORTED` |  |
| 73 | `keep/SUPPORTED/SUFFICIENT` | `verification` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__verify__p81` | `True` | `answer: SUPPORTED` |  |
| 74 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_2_5_flash` | `2503.00808v4__cross__p1_p2` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 75 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_3_1_flash_lite_preview` | `2503.00808v4__cross__p1_p2` | `True` | `answer: The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.` |  |
| 76 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gpt4o_2024_11_20` | `2503.00808v4__cross__p1_p2` | `True` | `answer: The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.` |  |
| 77 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__numeric_total_growth_gap_p2` | `True` | `answer: 0.4 percentage points` |  |
| 78 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__numeric_total_growth_gap_p2` | `True` | `answer: 0.4 percentage points` |  |
| 79 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__numeric_total_growth_gap_p2` | `True` | `answer: 0.4 percentage points` |  |
| 80 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_2_5_flash` | `2503.00808v4__text__p18` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 81 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `2503.00808v4__text__p18` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 82 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gpt4o_2024_11_20` | `2503.00808v4__text__p18` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 83 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_2_5_flash` | `2503.00808v4__refuse__external_fact` | `True` | `refuse: The document does not contain information about the current employer of the paper's first author.` |  |
| 84 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_3_1_flash_lite_preview` | `2503.00808v4__refuse__external_fact` | `True` | `refuse: The document lists the authors but does not provide information regarding their current employer.` |  |
| 85 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gpt4o_2024_11_20` | `2503.00808v4__refuse__external_fact` | `True` | `refuse: The document does not provide information about the current employer of the first author.` |  |
| 86 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_2_5_flash` | `2503.00808v4__cross__p1_p2` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 87 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_3_1_flash_lite_preview` | `2503.00808v4__cross__p1_p2` | `True` | `answer: The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.` |  |
| 88 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gpt4o_2024_11_20` | `2503.00808v4__cross__p1_p2` | `True` | `answer: The heading or leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.` |  |
| 89 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__numeric_total_growth_gap_p2` | `True` | `answer: 0.4 percentage points` |  |
| 90 | `keep/SUPPORTED/SUFFICIENT` | `numeric_computation` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__numeric_total_growth_gap_p2` | `True` | `answer: 0.4 percentage points` |  |
| 91 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_2_5_flash` | `2503.00808v4__text__p18` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 92 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_3_1_flash_lite_preview` | `2503.00808v4__text__p18` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 93 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gpt4o_2024_11_20` | `2503.00808v4__text__p18` | `True` | `answer: PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches` |  |
| 94 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_2_5_flash` | `2503.00808v4__refuse__external_fact` | `True` | `refuse: The document does not contain information about the current employer of the paper's first author. Research papers typically list affiliations at the time of publication, not current employment status.` |  |
| 95 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gemini_3_1_flash_lite_preview` | `2503.00808v4__refuse__external_fact` | `True` | `refuse: The document does not contain information regarding the current employer of the first author, Kashun Shum.` |  |
| 96 | `keep/SUPPORTED/SUFFICIENT` | `unanswerable` | `dmxapi_gpt4o_2024_11_20` | `2503.00808v4__refuse__external_fact` | `True` | `refuse: The document does not provide information about the current employer of the first author today.` |  |
| 97 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_2_5_flash` | `tm2529296d2_ars__cross__p1_p2` | `True` | `answer: About Us Shareholder and Media Information` |  |
| 98 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gemini_3_1_flash_lite_preview` | `tm2529296d2_ars__cross__p1_p2` | `True` | `answer: The heading on page 2 is 'About Us Shareholder and Media Information'.` |  |
| 99 | `keep/SUPPORTED/SUFFICIENT` | `cross_page` | `dmxapi_gpt4o_2024_11_20` | `tm2529296d2_ars__cross__p1_p2` | `True` | `answer: About Us Shareholder and Media Information` |  |
| 100 | `keep/SUPPORTED/SUFFICIENT` | `text_lookup` | `dmxapi_gemini_2_5_flash` | `ti2025ars__text__p42` | `True` | `answer: Government incentives` |  |
