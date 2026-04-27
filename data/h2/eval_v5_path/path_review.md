# H2 Path Review

- Rollout dir: `/home/kimilabra/DocWorldTrace/data/h2/rollouts_v5`

## Overall

- count: `120`
- strict_path_ok_rate: `0.7667`
- evidence_path_ok_rate: `0.9917`
- acceptable_path_ok_rate: `0.9833`
- proper_termination_rate: `0.9917`
- expected_terminal_rate: `0.9917`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.7667`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 92, 'format_error': 1, 'missing_required_tool': 27}`
- acceptable_path_issues: `{'acceptable_path_ok': 118, 'format_error': 1, 'tool_path_not_acceptable': 1}`

## By Teacher

### dmxapi_gemini_2_5_flash
- count: `40`
- strict_path_ok_rate: `0.875`
- evidence_path_ok_rate: `0.975`
- acceptable_path_ok_rate: `0.975`
- proper_termination_rate: `0.975`
- expected_terminal_rate: `0.975`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.875`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 35, 'format_error': 1, 'missing_required_tool': 4}`
- acceptable_path_issues: `{'acceptable_path_ok': 39, 'format_error': 1}`

### dmxapi_gemini_3_1_flash_lite_preview
- count: `40`
- strict_path_ok_rate: `0.675`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `0.975`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.675`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 27, 'missing_required_tool': 13}`
- acceptable_path_issues: `{'acceptable_path_ok': 39, 'tool_path_not_acceptable': 1}`

### dmxapi_gpt4o_2024_11_20
- count: `40`
- strict_path_ok_rate: `0.75`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.75`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 30, 'missing_required_tool': 10}`
- acceptable_path_issues: `{'acceptable_path_ok': 40}`

## By Task Type

### cross_page
- count: `24`
- strict_path_ok_rate: `1.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `1.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 24}`
- acceptable_path_issues: `{'acceptable_path_ok': 24}`

### numeric_computation
- count: `18`
- strict_path_ok_rate: `0.1111`
- evidence_path_ok_rate: `0.9444`
- acceptable_path_ok_rate: `0.9444`
- proper_termination_rate: `0.9444`
- expected_terminal_rate: `0.9444`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.1111`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'format_error': 1, 'missing_required_tool': 15, 'path_ok': 2}`
- acceptable_path_issues: `{'format_error': 1, 'acceptable_path_ok': 17}`

### table_lookup
- count: `12`
- strict_path_ok_rate: `0.5`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `0.9167`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.5`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 6, 'missing_required_tool': 6}`
- acceptable_path_issues: `{'acceptable_path_ok': 11, 'tool_path_not_acceptable': 1}`

### text_lookup
- count: `30`
- strict_path_ok_rate: `1.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `1.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 30}`
- acceptable_path_issues: `{'acceptable_path_ok': 30}`

### unanswerable
- count: `24`
- strict_path_ok_rate: `1.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `1.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 24}`
- acceptable_path_issues: `{'acceptable_path_ok': 24}`

### verification
- count: `12`
- strict_path_ok_rate: `0.5`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.5`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 6, 'missing_required_tool': 6}`
- acceptable_path_issues: `{'acceptable_path_ok': 12}`

## Non-Acceptable Path Cases

### format_error | dmxapi_gemini_2_5_flash | ti2025ars__numeric_free_cash_flow_margin_change_p29
- file: `/home/kimilabra/DocWorldTrace/data/h2/rollouts_v5/dmxapi_gemini_2_5_flash/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01.json`
- task: `numeric_computation`
- sequence: `['parse_table']`
- final action: `None`, expected: `answer`
- missing required: `['read_page', 'compute']`
- failed required: `[]`

### tool_path_not_acceptable | dmxapi_gemini_3_1_flash_lite_preview | ti2025ars__table__p7
- file: `/home/kimilabra/DocWorldTrace/data/h2/rollouts_v5/dmxapi_gemini_3_1_flash_lite_preview/ti2025ars__table__p7__run01.json`
- task: `table_lookup`
- sequence: `['read_page', 'answer']`
- final action: `answer`, expected: `answer`
- missing required: `['parse_table']`
- failed required: `[]`
