# H2 Path Review

- Rollout dir: `data/h2/rollouts_corrected_v1`

## Overall

- count: `162`
- strict_path_ok_rate: `0.7593`
- evidence_path_ok_rate: `0.9383`
- acceptable_path_ok_rate: `0.9383`
- proper_termination_rate: `0.9753`
- expected_terminal_rate: `0.9383`
- nonterminal_tool_use_rate: `0.9877`
- required_tool_coverage_rate: `0.8333`
- successful_evidence_observation_rate: `0.9877`
- strict_path_issues: `{'path_ok': 123, 'required_tool_no_success_observation': 10, 'missing_required_tool': 19, 'format_error': 4, 'wrong_terminal': 6}`
- acceptable_path_issues: `{'acceptable_path_ok': 152, 'format_error': 4, 'wrong_terminal': 6}`

## By Teacher

### dmxapi_gemini_2_5_flash
- count: `54`
- strict_path_ok_rate: `0.7593`
- evidence_path_ok_rate: `0.9259`
- acceptable_path_ok_rate: `0.9259`
- proper_termination_rate: `0.9444`
- expected_terminal_rate: `0.9259`
- nonterminal_tool_use_rate: `0.963`
- required_tool_coverage_rate: `0.8148`
- successful_evidence_observation_rate: `0.963`
- strict_path_issues: `{'path_ok': 41, 'required_tool_no_success_observation': 3, 'missing_required_tool': 6, 'format_error': 3, 'wrong_terminal': 1}`
- acceptable_path_issues: `{'acceptable_path_ok': 50, 'format_error': 3, 'wrong_terminal': 1}`

### dmxapi_gemini_3_1_flash_lite_preview
- count: `54`
- strict_path_ok_rate: `0.6296`
- evidence_path_ok_rate: `0.9444`
- acceptable_path_ok_rate: `0.9444`
- proper_termination_rate: `0.9815`
- expected_terminal_rate: `0.9444`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.7222`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 34, 'missing_required_tool': 12, 'required_tool_no_success_observation': 5, 'wrong_terminal': 2, 'format_error': 1}`
- acceptable_path_issues: `{'acceptable_path_ok': 51, 'wrong_terminal': 2, 'format_error': 1}`

### dmxapi_gpt4o_2024_11_20
- count: `54`
- strict_path_ok_rate: `0.8889`
- evidence_path_ok_rate: `0.9444`
- acceptable_path_ok_rate: `0.9444`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `0.9444`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.963`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 48, 'missing_required_tool': 1, 'required_tool_no_success_observation': 2, 'wrong_terminal': 3}`
- acceptable_path_issues: `{'acceptable_path_ok': 51, 'wrong_terminal': 3}`

## By Task Type

### cross_page
- count: `18`
- strict_path_ok_rate: `1.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `1.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 18}`
- acceptable_path_issues: `{'acceptable_path_ok': 18}`

### numeric_computation
- count: `15`
- strict_path_ok_rate: `0.2667`
- evidence_path_ok_rate: `0.8`
- acceptable_path_ok_rate: `0.8`
- proper_termination_rate: `0.8`
- expected_terminal_rate: `0.8`
- nonterminal_tool_use_rate: `0.8667`
- required_tool_coverage_rate: `0.6667`
- successful_evidence_observation_rate: `0.8667`
- strict_path_issues: `{'required_tool_no_success_observation': 6, 'missing_required_tool': 2, 'format_error': 3, 'path_ok': 4}`
- acceptable_path_issues: `{'acceptable_path_ok': 12, 'format_error': 3}`

### table_lookup
- count: `24`
- strict_path_ok_rate: `0.375`
- evidence_path_ok_rate: `0.7083`
- acceptable_path_ok_rate: `0.7083`
- proper_termination_rate: `0.9583`
- expected_terminal_rate: `0.7083`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.5833`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'required_tool_no_success_observation': 3, 'path_ok': 9, 'format_error': 1, 'wrong_terminal': 6, 'missing_required_tool': 5}`
- acceptable_path_issues: `{'acceptable_path_ok': 17, 'format_error': 1, 'wrong_terminal': 6}`

### text_lookup
- count: `33`
- strict_path_ok_rate: `1.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `1.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 33}`
- acceptable_path_issues: `{'acceptable_path_ok': 33}`

### unanswerable
- count: `42`
- strict_path_ok_rate: `0.881`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.9048`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 37, 'missing_required_tool': 4, 'required_tool_no_success_observation': 1}`
- acceptable_path_issues: `{'acceptable_path_ok': 42}`

### verification
- count: `30`
- strict_path_ok_rate: `0.7333`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.7333`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 22, 'missing_required_tool': 8}`
- acceptable_path_issues: `{'acceptable_path_ok': 30}`

## Non-Acceptable Path Cases

### format_error | dmxapi_gemini_2_5_flash | ipcc_ar6_syr_longer_report__table__p11
- file: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/ipcc_ar6_syr_longer_report__table__p11__run01.json`
- task: `table_lookup`
- sequence: `['read_page']`
- final action: `None`, expected: `answer`
- missing required: `['parse_table']`
- failed required: `[]`

### format_error | dmxapi_gemini_2_5_flash | ti2025ars__numeric__p97
- file: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/ti2025ars__numeric__p97__run01.json`
- task: `numeric_computation`
- sequence: `[]`
- final action: `None`, expected: `answer`
- missing required: `['parse_table', 'compute']`
- failed required: `[]`

### format_error | dmxapi_gemini_2_5_flash | tm2529296d2_ars__numeric__p2
- file: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/tm2529296d2_ars__numeric__p2__run01.json`
- task: `numeric_computation`
- sequence: `[]`
- final action: `None`, expected: `answer`
- missing required: `['parse_table', 'compute']`
- failed required: `[]`

### wrong_terminal | dmxapi_gemini_2_5_flash | tm2529296d2_ars__table__p2
- file: `data/h2/rollouts_corrected_v1/dmxapi_gemini_2_5_flash/tm2529296d2_ars__table__p2__run01.json`
- task: `table_lookup`
- sequence: `['read_page', 'search', 'ocr', 'refuse']`
- final action: `refuse`, expected: `answer`
- missing required: `['parse_table']`
- failed required: `[]`

### wrong_terminal | dmxapi_gemini_3_1_flash_lite_preview | ipcc_ar6_syr_longer_report__table__p11
- file: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/ipcc_ar6_syr_longer_report__table__p11__run01.json`
- task: `table_lookup`
- sequence: `['read_page', 'refuse']`
- final action: `refuse`, expected: `answer`
- missing required: `['parse_table']`
- failed required: `[]`

### format_error | dmxapi_gemini_3_1_flash_lite_preview | nasa_fy2025_budget_summary__numeric__p4
- file: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/nasa_fy2025_budget_summary__numeric__p4__run01.json`
- task: `numeric_computation`
- sequence: `['parse_table']`
- final action: `None`, expected: `answer`
- missing required: `['compute']`
- failed required: `[]`

### wrong_terminal | dmxapi_gemini_3_1_flash_lite_preview | tm2529296d2_ars__table__p2
- file: `data/h2/rollouts_corrected_v1/dmxapi_gemini_3_1_flash_lite_preview/tm2529296d2_ars__table__p2__run01.json`
- task: `table_lookup`
- sequence: `['read_page', 'search', 'read_page', 'search', 'ocr', 'search', 'read_page', 'refuse']`
- final action: `refuse`, expected: `answer`
- missing required: `['parse_table']`
- failed required: `[]`

### wrong_terminal | dmxapi_gpt4o_2024_11_20 | ipcc_ar6_syr_longer_report__table__p11
- file: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/ipcc_ar6_syr_longer_report__table__p11__run01.json`
- task: `table_lookup`
- sequence: `['read_page', 'ocr', 'parse_table', 'ocr', 'refuse']`
- final action: `refuse`, expected: `answer`
- missing required: `[]`
- failed required: `[]`

### wrong_terminal | dmxapi_gpt4o_2024_11_20 | ti2025ars__table__p7
- file: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/ti2025ars__table__p7__run01.json`
- task: `table_lookup`
- sequence: `['read_page', 'parse_table', 'ocr', 'refuse']`
- final action: `refuse`, expected: `answer`
- missing required: `[]`
- failed required: `['parse_table']`

### wrong_terminal | dmxapi_gpt4o_2024_11_20 | tm2529296d2_ars__table__p2
- file: `data/h2/rollouts_corrected_v1/dmxapi_gpt4o_2024_11_20/tm2529296d2_ars__table__p2__run01.json`
- task: `table_lookup`
- sequence: `['read_page', 'ocr', 'refuse']`
- final action: `refuse`, expected: `answer`
- missing required: `['parse_table']`
- failed required: `[]`
