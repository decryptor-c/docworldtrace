# Exp-3 DocVerify++ Review

- Rollout dir: `data/h2/rollouts_corrected_v1`
- Verifier: `DocVerifyPlus(rule_claim_evidence_v1)`

## Overall

- Count: `162`
- Support rate: `85.80%`
- Sufficiency rate: `85.80%`
- Keep rate: `85.80%`
- Review rate: `0.62%`
- Reject rate: `13.58%`
- Adjusted answer correct rate: `87.65%`
- Mean quality score: `0.9103`
- Support labels: `{'SUPPORTED': 139, 'NOT_SUPPORTED': 18, 'INVALID': 4, 'PARTIAL': 1}`
- Sufficiency labels: `{'SUFFICIENT': 139, 'INSUFFICIENT': 19, 'INVALID': 4}`
- Filter decisions: `{'keep': 139, 'reject': 22, 'review': 1}`
- Failure taxonomy: `{'none': 139, 'answer_mismatch': 9, 'format_error': 4, 'verification_label_mismatch': 2, 'table_value_mismatch': 6, 'insufficient_negative_evidence': 1, 'numeric_mismatch': 1}`

## Manual Calibration

- manual_label_count: `0`
- support_precision: `None`
- support_recall: `None`
- unsupported_identification_rate: `None`
- sufficiency_accuracy: `None`

## By Task Type

### cross_page
- Count: `18`
- Support rate: `77.78%`
- Sufficiency rate: `77.78%`
- Keep/review/reject: `{'keep': 14, 'reject': 4}`
- Failure taxonomy: `{'none': 14, 'answer_mismatch': 4}`

### numeric_computation
- Count: `15`
- Support rate: `73.33%`
- Sufficiency rate: `73.33%`
- Keep/review/reject: `{'keep': 11, 'reject': 4}`
- Failure taxonomy: `{'none': 11, 'format_error': 3, 'numeric_mismatch': 1}`

### table_lookup
- Count: `24`
- Support rate: `70.83%`
- Sufficiency rate: `70.83%`
- Keep/review/reject: `{'keep': 17, 'reject': 7}`
- Failure taxonomy: `{'none': 17, 'format_error': 1, 'table_value_mismatch': 6}`

### text_lookup
- Count: `33`
- Support rate: `84.85%`
- Sufficiency rate: `84.85%`
- Keep/review/reject: `{'keep': 28, 'reject': 5}`
- Failure taxonomy: `{'none': 28, 'answer_mismatch': 5}`

### unanswerable
- Count: `42`
- Support rate: `97.62%`
- Sufficiency rate: `97.62%`
- Keep/review/reject: `{'keep': 41, 'review': 1}`
- Failure taxonomy: `{'none': 41, 'insufficient_negative_evidence': 1}`

### verification
- Count: `30`
- Support rate: `93.33%`
- Sufficiency rate: `93.33%`
- Keep/review/reject: `{'keep': 28, 'reject': 2}`
- Failure taxonomy: `{'none': 28, 'verification_label_mismatch': 2}`

## Review / Reject Cases

### reject | answer_mismatch | dmxapi_gemini_2_5_flash | 2310.03302v2__cross__p1_p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/2310.03302v2__cross__p1_p2__run01.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Starter Files`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | format_error | dmxapi_gemini_2_5_flash | ipcc_ar6_syr_longer_report__table__p11
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/ipcc_ar6_syr_longer_report__table__p11__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page']`
- Final: `None` / `None`
- Reference: `1292`
- Support: `INVALID`
- Sufficiency: `INVALID`
- Quality score: `0.25`
- Claim `c1`: `INVALID` / `The rollout did not terminate with a valid answer/refuse action.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash | irs_2025_form_1040__verify__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/irs_2025_form_1040__verify__p2__run01.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED. Line 15 on page 2 states: "Subtract line 14 from line 11b. If zero or less, enter -0-. This is your taxable income."`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash | nasa_fy2025_budget_summary__verify__p12
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/nasa_fy2025_budget_summary__verify__p12__run01.json`
- Task: `verification`
- Tool sequence: `['search', 'verify', 'verify', 'read_page', 'verify', 'verify', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.534`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash | scotus_loper_bright_2024__text__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/scotus_loper_bright_2024__text__p2__run01.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `2 LOPER BRIGHT ENTERPRISES v. RAIMONDO`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`
- Claim `c2`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | format_error | dmxapi_gemini_2_5_flash | ti2025ars__numeric__p97
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/ti2025ars__numeric__p97__run01.json`
- Task: `numeric_computation`
- Tool sequence: `[]`
- Final: `None` / `None`
- Reference: `162.31%`
- Support: `INVALID`
- Sufficiency: `INVALID`
- Quality score: `0.1`
- Claim `c1`: `INVALID` / `The rollout did not terminate with a valid answer/refuse action.`

### reject | format_error | dmxapi_gemini_2_5_flash | tm2529296d2_ars__numeric__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/tm2529296d2_ars__numeric__p2__run01.json`
- Task: `numeric_computation`
- Tool sequence: `[]`
- Final: `None` / `None`
- Reference: `-85.71%`
- Support: `INVALID`
- Sufficiency: `INVALID`
- Quality score: `0.1`
- Claim `c1`: `INVALID` / `The rollout did not terminate with a valid answer/refuse action.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash | tm2529296d2_ars__table__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/tm2529296d2_ars__table__p2__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'search', 'ocr', 'refuse']`
- Final: `refuse` / `The question asks for information from a table on page 2, but no table is present on page 2 according to the document's text and OCR results.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview | 2310.03302v2__cross__p1_p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/2310.03302v2__cross__p1_p2__run01.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on the next page (page 2) is 'Starter Files'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview | ipcc_ar6_syr_longer_report__table__p11
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/ipcc_ar6_syr_longer_report__table__p11__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `The table containing 'Population (million persons, 2019)' for 'Africa' is not present on page 11 of the provided document.`
- Reference: `1292`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview | irs_2025_form_1040__refuse__generic
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/irs_2025_form_1040__refuse__generic__run01.json`
- Task: `unanswerable`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `The document is an IRS Form 1040 and does not contain information regarding a CEO, an author, or any private mobile phone numbers.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/nasa_fy2025_budget_summary__cross__p2_p3__run01.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `$2.4 billion investment`
- Reference: `Drives scientific discovery through a balanced portfolio of space-based observatories`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | format_error | dmxapi_gemini_3_1_flash_lite_preview | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/nasa_fy2025_budget_summary__numeric__p4__run01.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table']`
- Final: `None` / `None`
- Reference: `-42.71%`
- Support: `INVALID`
- Sufficiency: `INVALID`
- Quality score: `0.25`
- Claim `c1`: `INVALID` / `The rollout did not terminate with a valid answer/refuse action.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview | scotus_loper_bright_2024__text__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/scotus_loper_bright_2024__text__p2__run01.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `2 LOPER BRIGHT ENTERPRISES v. RAIMONDO`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`
- Claim `c2`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview | tm2529296d2_ars__table__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/tm2529296d2_ars__table__p2__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'search', 'read_page', 'search', 'ocr', 'search', 'read_page', 'refuse']`
- Final: `refuse` / `The requested table is not present on page 2, and a search of the document did not locate the specified revenue data in a table format.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.234`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview | usgs_mcs_2025__text__p21
- File: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/usgs_mcs_2025__text__p21__run01.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `17`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20 | ipcc_ar6_syr_longer_report__table__p11
- File: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/ipcc_ar6_syr_longer_report__table__p11__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'ocr', 'parse_table', 'ocr', 'refuse']`
- Final: `refuse` / `The table content on page 11 is unclear and does not provide the requested row and column data for 'Population (million persons, 2019)' under 'Africa'.`
- Reference: `1292`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.296`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20 | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/nasa_fy2025_budget_summary__cross__p2_p3__run01.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The first bullet's leading phrase on page 3 is 'Drives scientific discovery'.`
- Reference: `Drives scientific discovery through a balanced portfolio of space-based observatories`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20 | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/nasa_fy2025_budget_summary__numeric__p4__run01.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20 | scotus_loper_bright_2024__text__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/scotus_loper_bright_2024__text__p2__run01.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `2 LOPER BRIGHT ENTERPRISES v. RAIMONDO`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`
- Claim `c2`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20 | ti2025ars__table__p7
- File: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/ti2025ars__table__p7__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'ocr', 'refuse']`
- Final: `refuse` / `The table information on page 7 could not be extracted using parsing or OCR tools.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20 | tm2529296d2_ars__table__p2
- File: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/tm2529296d2_ars__table__p2__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'ocr', 'refuse']`
- Final: `refuse` / `No table is present on page 2 to extract the requested information.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20 | usgs_mcs_2025__text__p21
- File: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/usgs_mcs_2025__text__p21__run01.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `17`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

## Notes

This implementation performs the full DocVerify++ pipeline for the pilot setting: claim decomposition, evidence collection from trajectory observations, evidence ranking, claim-evidence support judgment, sufficiency judgment, reward scoring, filtering, and optional human calibration.
The current support judge is a deterministic rule/NLI-lite implementation. It is suitable for pilot filtering and auditing; it can be replaced by an external NLI or LLM judge without changing the output schema.