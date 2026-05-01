# Exp-3 DocVerify++ Review

- Rollout dir: `data/h2/rollouts_diverse_v2`
- Verifier: `DocVerifyPlus(rule_claim_evidence_v1)`

## Overall

- Count: `162`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep rate: `100.00%`
- Review rate: `0.00%`
- Reject rate: `0.00%`
- Adjusted answer correct rate: `100.00%`
- Mean quality score: `0.988`
- Support labels: `{'SUPPORTED': 162}`
- Sufficiency labels: `{'SUFFICIENT': 162}`
- Filter decisions: `{'keep': 162}`
- Failure taxonomy: `{'none': 162}`

## Manual Calibration

- manual_label_count: `0`
- support_precision: `None`
- support_recall: `None`
- unsupported_identification_rate: `None`
- sufficiency_accuracy: `None`

## By Task Type

### cross_page
- Count: `18`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 18}`
- Failure taxonomy: `{'none': 18}`

### numeric_computation
- Count: `15`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 15}`
- Failure taxonomy: `{'none': 15}`

### table_lookup
- Count: `21`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 21}`
- Failure taxonomy: `{'none': 21}`

### text_lookup
- Count: `36`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 36}`
- Failure taxonomy: `{'none': 36}`

### unanswerable
- Count: `42`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 42}`
- Failure taxonomy: `{'none': 42}`

### verification
- Count: `30`
- Support rate: `100.00%`
- Sufficiency rate: `100.00%`
- Keep/review/reject: `{'keep': 30}`
- Failure taxonomy: `{'none': 30}`

## Review / Reject Cases

## Notes

This implementation performs the full DocVerify++ pipeline for the pilot setting: claim decomposition, evidence collection from trajectory observations, evidence ranking, claim-evidence support judgment, sufficiency judgment, reward scoring, filtering, and optional human calibration.
The current support judge is a deterministic rule/NLI-lite implementation. It is suitable for pilot filtering and auditing; it can be replaced by an external NLI or LLM judge without changing the output schema.