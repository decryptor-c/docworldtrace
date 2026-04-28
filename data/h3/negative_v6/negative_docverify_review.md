# Exp-3 DocVerify++ Review

- Rollout dir: `data/h3/negative_v6/corrupted_rollouts`
- Verifier: `DocVerifyPlus(rule_claim_evidence_v1)`

## Overall

- Count: `604`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep rate: `0.00%`
- Review rate: `5.63%`
- Reject rate: `94.37%`
- Adjusted answer correct rate: `61.75%`
- Mean quality score: `0.4398`
- Support labels: `{'NOT_SUPPORTED': 546, 'PARTIAL': 58}`
- Sufficiency labels: `{'MISSING': 190, 'INSUFFICIENT': 414}`
- Filter decisions: `{'reject': 570, 'review': 34}`
- Failure taxonomy: `{'missing_evidence': 190, 'invalid_evidence_ref': 108, 'answer_mismatch': 108, 'search_only_evidence': 11, 'insufficient_negative_evidence': 24, 'verification_label_mismatch': 36, 'weak_evidence_support': 6, 'compute_expression_mismatch': 17, 'missing_compute': 17, 'numeric_mismatch': 51, 'table_value_mismatch': 36}`

## Manual Calibration

- manual_label_count: `0`
- support_precision: `None`
- support_recall: `None`
- unsupported_identification_rate: `None`
- sufficiency_accuracy: `None`

## By Task Type

### cross_page
- Count: `144`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 133, 'review': 11}`
- Failure taxonomy: `{'missing_evidence': 48, 'invalid_evidence_ref': 37, 'answer_mismatch': 48, 'search_only_evidence': 11}`

### numeric_computation
- Count: `136`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 119, 'review': 17}`
- Failure taxonomy: `{'compute_expression_mismatch': 17, 'missing_evidence': 34, 'missing_compute': 17, 'invalid_evidence_ref': 17, 'numeric_mismatch': 51}`

### table_lookup
- Count: `72`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 72}`
- Failure taxonomy: `{'missing_evidence': 24, 'invalid_evidence_ref': 12, 'table_value_mismatch': 36}`

### text_lookup
- Count: `150`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 150}`
- Failure taxonomy: `{'missing_evidence': 60, 'invalid_evidence_ref': 30, 'answer_mismatch': 60}`

### unanswerable
- Count: `24`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 24}`
- Failure taxonomy: `{'insufficient_negative_evidence': 24}`

### verification
- Count: `78`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 72, 'review': 6}`
- Failure taxonomy: `{'missing_evidence': 24, 'invalid_evidence_ref': 12, 'verification_label_mismatch': 36, 'weak_evidence_support': 6}`

## Review / Reject Cases

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__refuse__external_fact__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__refuse__external_fact__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__text__p7__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run02__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run02__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run02__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run02__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run02__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run02__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run02__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__refuse__legal_risk
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__refuse__legal_risk__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__refuse__legal_risk
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__refuse__legal_risk__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__refuse__external_fact__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__refuse__external_fact__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.45`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `8 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__refuse__undisclosed_forecast
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__refuse__undisclosed_forecast__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__refuse__undisclosed_forecast
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__refuse__undisclosed_forecast__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run02__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run02__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run02__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run02__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run02__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run02__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `15.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `15.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'parse_table', 'compute', 'answer']`
- Final: `answer` / `1.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `1.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run02__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run02__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run02__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run02__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run02__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run02__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run02__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run02__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run02__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run02__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run02__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run02__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run02__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading on the page following the VisIT-Bench benchmark description is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on the page following the VisIT-Bench benchmark description is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on the page following the VisIT-Bench benchmark description is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on the page following the VisIT-Bench benchmark description is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__refuse__external_fact__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__refuse__external_fact__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `BLIP2 Caption`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `BLIP2 Caption`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__text__p7__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run02__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run02__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run02__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run02__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run02__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run02__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation'.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__refuse__legal_risk
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__refuse__legal_risk__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__refuse__legal_risk
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__refuse__legal_risk__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__refuse__external_fact__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__refuse__external_fact__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.45`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `8 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.45`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7.0 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `8 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__refuse__undisclosed_forecast
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__refuse__undisclosed_forecast__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__refuse__undisclosed_forecast
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__refuse__undisclosed_forecast__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run02__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run02__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run02__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run02__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run02__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run02__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information'.`
- Reference: `About Us Shareholder and Media Information`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `15.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `15.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `1.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `1.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run02__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run02__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run02__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run02__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run02__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run02__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run02__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run02__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run02__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run02__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run02__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run02__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__refuse__external_fact__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__refuse__external_fact__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `BLIP2 Caption It is not possible to determine if a`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__text__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__text__p7__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `BLIP2 Caption It is not possible to determine if a`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run02__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run02__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run02__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run02__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run02__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run02__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__refuse__legal_risk
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__refuse__legal_risk__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__refuse__legal_risk
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__refuse__legal_risk__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The heading or leading phrase on page 2 is 'PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches'.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__refuse__external_fact__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__refuse__external_fact
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__refuse__external_fact__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'crop', 'compute', 'compute', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'crop', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'crop', 'compute', 'compute', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'crop', 'compute', 'compute', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.446`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'crop', 'compute', 'compute', 'answer']`
- Final: `answer` / `8 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'crop', 'compute', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.296`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['read_page', 'crop', 'compute', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.45`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `7 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `8 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric_free_cash_flow_margin_change_p29
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric_free_cash_flow_margin_change_p29__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `7.0 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__refuse__undisclosed_forecast
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__refuse__undisclosed_forecast__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__refuse__undisclosed_forecast
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__refuse__undisclosed_forecast__run02__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run02__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run02__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run02__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run02__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run02__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run02__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['read_page', 'parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About Us Shareholder and Media Information`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run02__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information.'`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run02__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information.'`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run02__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information.'`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run02__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run02__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is 'About Us Shareholder and Media Information.'`
- Reference: `About Us Shareholder and Media Information`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__cross__p1_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__cross__p1_p2__run02__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About Us Shareholder and Media Information`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `15.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `14.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `15.8 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_margin_change_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_margin_change_p2__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `14.8 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `1.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.4833`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `0.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `1.4 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric_total_growth_gap_p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric_total_growth_gap_p2__run02__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `0.4 percentage points`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run02__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run02__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run02__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run02__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run02__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run02__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run02__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run02__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run02__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run02__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run02__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run02__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run02__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run02__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run02__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run02__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run02__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_v6/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run02__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

## Notes

This implementation performs the full DocVerify++ pipeline for the pilot setting: claim decomposition, evidence collection from trajectory observations, evidence ranking, claim-evidence support judgment, sufficiency judgment, reward scoring, filtering, and optional human calibration.
The current support judge is a deterministic rule/NLI-lite implementation. It is suitable for pilot filtering and auditing; it can be replaced by an external NLI or LLM judge without changing the output schema.