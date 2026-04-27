# Exp-3 DocVerify++ Review

- Rollout dir: `data/h2/rollouts_v5`
- Verifier: `DocVerifyPlus(rule_claim_evidence_v1)`

## Overall

- Count: `120`
- Support rate: `98.33%`
- Sufficiency rate: `98.33%`
- Keep rate: `98.33%`
- Review rate: `0.83%`
- Reject rate: `0.83%`
- Adjusted answer correct rate: `99.17%`
- Mean quality score: `0.9807`
- Support labels: `{'SUPPORTED': 118, 'INVALID': 1, 'PARTIAL': 1}`
- Sufficiency labels: `{'SUFFICIENT': 118, 'INVALID': 1, 'INSUFFICIENT': 1}`
- Filter decisions: `{'keep': 118, 'reject': 1, 'review': 1}`
- Failure taxonomy: `{'none': 118, 'format_error': 1, 'missing_table_evidence': 1}`

## Manual Calibration

- manual_label_count: `0`
- support_precision: `None`
- support_recall: `None`
- unsupported_identification_rate: `None`
- sufficiency_accuracy: `None`

## By Task Type

### cross_page
- Count: `24`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 24}`
- Failure taxonomy: `{'none': 24}`

### numeric_computation
- Count: `18`
- Support rate: `94.44%`
- Sufficiency rate: `94.44%`
- Keep/review/reject: `{'reject': 1, 'keep': 17}`
- Failure taxonomy: `{'format_error': 1, 'none': 17}`

### table_lookup
- Count: `12`
- Support rate: `91.67%`
- Sufficiency rate: `91.67%`
- Keep/review/reject: `{'keep': 11, 'review': 1}`
- Failure taxonomy: `{'none': 11, 'missing_table_evidence': 1}`

### text_lookup
- Count: `30`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 30}`
- Failure taxonomy: `{'none': 30}`

### unanswerable
- Count: `24`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 24}`
- Failure taxonomy: `{'none': 24}`

### verification
- Count: `12`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 12}`
- Failure taxonomy: `{'none': 12}`

## Review / Reject Cases

### reject | format_error | dmxapi_gemini_2_5_flash | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h2/rollouts_v5/dmxapi_gemini_2_5_flash/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table']`
- Final: `None` / `None`
- Reference: `7.0 percentage points`
- Support: `INVALID`
- Sufficiency: `INVALID`
- Quality score: `0.2`
- Claim `c1`: `INVALID` / `The rollout did not terminate with a valid answer/refuse action.`

### review | missing_table_evidence | dmxapi_gemini_3_1_flash_lite_preview | ti2025ars__table__p7
- File: `data/h2/rollouts_v5/dmxapi_gemini_3_1_flash_lite_preview/ti2025ars__table__p7__run01.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The answer matches, but table-structured evidence is missing.`

## Notes

This implementation performs the full DocVerify++ pipeline for the pilot setting: claim decomposition, evidence collection from trajectory observations, evidence ranking, claim-evidence support judgment, sufficiency judgment, reward scoring, filtering, and optional human calibration.
The current support judge is a deterministic rule/NLI-lite implementation. It is suitable for pilot filtering and auditing; it can be replaced by an external NLI or LLM judge without changing the output schema.