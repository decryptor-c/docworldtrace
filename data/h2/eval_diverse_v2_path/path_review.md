# H2 Path Review

- Rollout dir: `/home/kimilabra/DocWorldTrace/data/h2/rollouts_diverse_v2`

## Overall

- count: `162`
- strict_path_ok_rate: `0.716`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.7222`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 116, 'missing_required_tool': 45, 'required_tool_no_success_observation': 1}`
- acceptable_path_issues: `{'acceptable_path_ok': 162}`

## By Teacher

### dmxapi_gemini_2_5_flash
- count: `54`
- strict_path_ok_rate: `0.7593`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.7593`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 41, 'missing_required_tool': 13}`
- acceptable_path_issues: `{'acceptable_path_ok': 54}`

### dmxapi_gemini_3_1_flash_lite_preview
- count: `54`
- strict_path_ok_rate: `0.7037`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.7222`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 38, 'missing_required_tool': 15, 'required_tool_no_success_observation': 1}`
- acceptable_path_issues: `{'acceptable_path_ok': 54}`

### dmxapi_gpt4o_2024_11_20
- count: `54`
- strict_path_ok_rate: `0.6852`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.6852`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 37, 'missing_required_tool': 17}`
- acceptable_path_issues: `{'acceptable_path_ok': 54}`

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
- strict_path_ok_rate: `1.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `1.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 15}`
- acceptable_path_issues: `{'acceptable_path_ok': 15}`

### table_lookup
- count: `21`
- strict_path_ok_rate: `0.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'missing_required_tool': 21}`
- acceptable_path_issues: `{'acceptable_path_ok': 21}`

### text_lookup
- count: `36`
- strict_path_ok_rate: `1.0`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `1.0`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'path_ok': 36}`
- acceptable_path_issues: `{'acceptable_path_ok': 36}`

### unanswerable
- count: `42`
- strict_path_ok_rate: `0.9286`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.9524`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'missing_required_tool': 2, 'path_ok': 39, 'required_tool_no_success_observation': 1}`
- acceptable_path_issues: `{'acceptable_path_ok': 42}`

### verification
- count: `30`
- strict_path_ok_rate: `0.2667`
- evidence_path_ok_rate: `1.0`
- acceptable_path_ok_rate: `1.0`
- proper_termination_rate: `1.0`
- expected_terminal_rate: `1.0`
- nonterminal_tool_use_rate: `1.0`
- required_tool_coverage_rate: `0.2667`
- successful_evidence_observation_rate: `1.0`
- strict_path_issues: `{'missing_required_tool': 22, 'path_ok': 8}`
- acceptable_path_issues: `{'acceptable_path_ok': 30}`

## Non-Acceptable Path Cases
