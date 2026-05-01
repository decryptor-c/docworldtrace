# Exp-3 DocVerify++ Review

- Rollout dir: `data/h3/negative_diverse_v2/corrupted_rollouts`
- Verifier: `DocVerifyPlus(rule_claim_evidence_v1)`

## Overall

- Count: `764`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep rate: `0.00%`
- Review rate: `3.27%`
- Reject rate: `96.73%`
- Adjusted answer correct rate: `62.30%`
- Mean quality score: `0.4341`
- Support labels: `{'NOT_SUPPORTED': 697, 'PARTIAL': 67}`
- Sufficiency labels: `{'MISSING': 240, 'INSUFFICIENT': 524}`
- Filter decisions: `{'reject': 739, 'review': 25}`
- Failure taxonomy: `{'missing_evidence': 240, 'invalid_evidence_ref': 138, 'answer_mismatch': 108, 'search_only_evidence': 2, 'insufficient_negative_evidence': 42, 'verification_label_mismatch': 88, 'table_value_mismatch': 63, 'weak_evidence_support': 8, 'compute_expression_mismatch': 15, 'missing_compute': 15, 'numeric_mismatch': 45}`

## Manual Calibration

- manual_label_count: `0`
- support_precision: `None`
- support_recall: `None`
- unsupported_identification_rate: `None`
- sufficiency_accuracy: `None`

## By Task Type

### cross_page
- Count: `108`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 106, 'review': 2}`
- Failure taxonomy: `{'missing_evidence': 36, 'invalid_evidence_ref': 34, 'answer_mismatch': 36, 'search_only_evidence': 2}`

### numeric_computation
- Count: `120`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 105, 'review': 15}`
- Failure taxonomy: `{'compute_expression_mismatch': 15, 'missing_evidence': 30, 'missing_compute': 15, 'invalid_evidence_ref': 15, 'numeric_mismatch': 45}`

### table_lookup
- Count: `126`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 126}`
- Failure taxonomy: `{'missing_evidence': 42, 'invalid_evidence_ref': 21, 'table_value_mismatch': 63}`

### text_lookup
- Count: `180`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 180}`
- Failure taxonomy: `{'missing_evidence': 72, 'invalid_evidence_ref': 36, 'answer_mismatch': 72}`

### unanswerable
- Count: `42`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 42}`
- Failure taxonomy: `{'insufficient_negative_evidence': 42}`

### verification
- Count: `188`
- Support rate: `0.00%`
- Sufficiency rate: `0.00%`
- Keep/review/reject: `{'reject': 180, 'review': 8}`
- Failure taxonomy: `{'missing_evidence': 60, 'invalid_evidence_ref': 32, 'verification_label_mismatch': 88, 'weak_evidence_support': 8}`

## Review / Reject Cases

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2308.06595v4__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2310.03302v2__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/2503.00808v4__text__p18__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__table__p3__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `5`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__table__p3__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `5`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__table__p3__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `5`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__table__p3__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__table__p3__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__table__p3__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__text__p9__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__text__p9__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__text__p9__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__text__p9__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__text__p9__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__verify__p18__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__verify__p18__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__verify__p18__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__verify__p18__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__verify__p18__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__verify__p18__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/apple_2025_10k__verify__p18__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-13.94`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p134__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `1,807.8`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p134__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `1,807.8`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p134__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `1,807.8`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p134__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p134__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p134__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p41__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `182.8`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p41__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `182.8`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p41__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `182.8`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p41__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p41__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__table__p41__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `101`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__numeric__p4__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__verify__p33__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__verify__p33__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__verify__p33__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__verify__p33__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__verify__p33__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__verify__p33__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/fda_ozempic_2025_label__verify__p33__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p50__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p50__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p50__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p50__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__text__p50__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | irs_2025_form_1040__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/irs_2025_form_1040__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/irs_2025_form_1040__verify__p2__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/irs_2025_form_1040__verify__p2__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/irs_2025_form_1040__verify__p2__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/irs_2025_form_1040__verify__p2__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/irs_2025_form_1040__verify__p2__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/irs_2025_form_1040__verify__p2__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.446`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-41.71`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.296`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__numeric__p4__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'search', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__table__p4__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `25,383.7`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__table__p4__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `25,383.7`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__table__p4__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `25,383.7`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__table__p4__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__table__p4__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__table__p4__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__text__p4__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__text__p4__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__text__p4__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__text__p4__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__text__p4__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__verify__p12__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__verify__p12__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__verify__p12__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__verify__p12__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__verify__p12__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nasa_fy2025_budget_summary__verify__p12__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements,`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements,`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements,`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements,`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__text__p5__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__text__p5__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__text__p5__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__text__p5__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__text__p5__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__verify__p54__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__verify__p54__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__verify__p54__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__verify__p54__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__verify__p54__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/nist_ai_600_1_genai_profile__verify__p54__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__text__p2__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__text__p2__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__text__p2__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__text__p2__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__text__p2__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__verify__p4__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/scotus_loper_bright_2024__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `163.31`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__numeric__p97__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'search', 'read_page', 'search', 'search', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.242`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `TXN`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__table__p7__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/ti2025ars__text__p42__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-84.71`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__numeric__p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__table__p2__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__text__p27__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_2_5_flash__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/tm2529296d2_ars__verify__p81__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__table__p21__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Metallurgy and many sectors of the economy.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__table__p21__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `Metallurgy and many sectors of the economy.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__table__p21__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `Metallurgy and many sectors of the economy.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__table__p21__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__table__p21__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__table__p21__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p1__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p1__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p1__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p1__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p1__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p21__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p21__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p21__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p21__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_2_5_flash__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_2_5_flash__negative/usgs_mcs_2025__text__p21__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### review | search_only_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `1 Introduction`
- Reference: `1 Introduction`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches, but only search-level evidence remains for a task that requires more specific document evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2308.06595v4__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2310.03302v2__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/2503.00808v4__text__p18__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__table__p3__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Item 1A. Risk Factors is listed on page 5.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__table__p3__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `Item 1A. Risk Factors is listed on page 5.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__table__p3__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `Item 1A. Risk Factors is listed on page 5.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__table__p3__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__table__p3__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__table__p3__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__text__p9__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__text__p9__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__text__p9__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__text__p9__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__text__p9__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__verify__p18__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__verify__p18__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__verify__p18__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__verify__p18__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__verify__p18__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/apple_2025_10k__verify__p18__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading on page 3 is 'HOW TO OBTAIN COPIES'.`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 3 is 'HOW TO OBTAIN COPIES'.`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 3 is 'HOW TO OBTAIN COPIES'.`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 3 is 'HOW TO OBTAIN COPIES'.`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-13.94`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p134__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `1,807.8`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p134__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `1,807.8`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p134__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `1,807.8`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p134__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p134__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p134__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p41__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'HFCs' in 2022 is 182.8.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p41__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'HFCs' in 2022 is 182.8.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p41__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'HFCs' in 2022 is 182.8.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p41__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p41__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__table__p41__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `+100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `+100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `+100.00%`
- Reference: `100.00%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `+100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `+100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `101`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__numeric__p4__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__verify__p33__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__verify__p33__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__verify__p33__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.446`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__verify__p33__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'search', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.296`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__verify__p33__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__verify__p33__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/fda_ozempic_2025_label__verify__p33__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['search', 'read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p50__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p50__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p50__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p50__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__text__p50__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | irs_2025_form_1040__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/irs_2025_form_1040__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/irs_2025_form_1040__verify__p2__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/irs_2025_form_1040__verify__p2__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/irs_2025_form_1040__verify__p2__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/irs_2025_form_1040__verify__p2__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/irs_2025_form_1040__verify__p2__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/irs_2025_form_1040__verify__p2__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'answer']`
- Final: `answer` / `-41.71`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__numeric__p4__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__table__p4__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'NASA Total' under the 'FY 2025 Request' column is 25,383.7.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__table__p4__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'NASA Total' under the 'FY 2025 Request' column is 25,383.7.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__table__p4__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'NASA Total' under the 'FY 2025 Request' column is 25,383.7.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__table__p4__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__table__p4__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__table__p4__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__text__p4__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__text__p4__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__text__p4__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__text__p4__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__text__p4__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__verify__p12__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__verify__p12__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__verify__p12__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__verify__p12__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__verify__p12__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nasa_fy2025_budget_summary__verify__p12__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The page containing 'Gina M. Raimondo, Secretary' is page 2. The following page is page 3, which begins with the heading 'About AI at NIST'.`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c3`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The page containing 'Gina M. Raimondo, Secretary' is page 2. The following page is page 3, which begins with the heading 'About AI at NIST'.`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c3`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The page containing 'Gina M. Raimondo, Secretary' is page 2. The following page is page 3, which begins with the heading 'About AI at NIST'.`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c3`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The page containing 'Gina M. Raimondo, Secretary' is page 2. The following page is page 3, which begins with the heading 'About AI at NIST'.`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c3`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__text__p5__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__text__p5__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__text__p5__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__text__p5__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__text__p5__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__verify__p54__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__verify__p54__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__verify__p54__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__verify__p54__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__verify__p54__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/nist_ai_600_1_genai_profile__verify__p54__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__text__p2__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__text__p2__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__text__p2__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__text__p2__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__text__p2__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'search', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### review | weak_evidence_support | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__verify__p4__run01__weak_search_only_evidence.json`
- Task: `verification`
- Tool sequence: `['read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `PARTIAL` / `The final answer matches the reference, but evidence match is weak.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/scotus_loper_bright_2024__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'search', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `162.31%`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `163.31`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__numeric__p97__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is TXN.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is TXN.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is TXN.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__table__p7__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/ti2025ars__text__p42__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-85.71%`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-84.71`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__numeric__p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__table__p2__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__text__p27__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/tm2529296d2_ars__verify__p81__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__table__p21__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'Aluminum' under the 'Applications' column is 'Metallurgy and many sectors of the economy.'`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__table__p21__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Aluminum' under the 'Applications' column is 'Metallurgy and many sectors of the economy.'`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__table__p21__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Aluminum' under the 'Applications' column is 'Metallurgy and many sectors of the economy.'`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__table__p21__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__table__p21__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__table__p21__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p1__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p1__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p1__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p1__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p1__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p21__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p21__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p21__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p21__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gemini_3_1_flash_lite_preview__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gemini_3_1_flash_lite_preview__negative/usgs_mcs_2025__text__p21__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The heading on page 2 is '1 Introduction'.`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1 Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.246`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2308.06595v4__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2308.06595v4__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.246`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2310.03302v2__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2310.03302v2__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__cross__p1_p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__cross__p1_p2__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.246`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | 2503.00808v4__text__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/2503.00808v4__text__p18__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.246`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__table__p3__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `'Item 1A. Risk Factors' is listed on page 5.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__table__p3__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `'Item 1A. Risk Factors' is listed on page 5.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__table__p3__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `'Item 1A. Risk Factors' is listed on page 5.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__table__p3__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__table__p3__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__table__p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__table__p3__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `5`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__text__p9__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural disasters, public health issues, industrial accidents and other business interruptions.`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__text__p9__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural disasters, public health issues, industrial accidents and other business interruptions.`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__text__p9__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural disasters, public health issues, industrial accidents and other business interruptions.`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__text__p9__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__text__p9
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__text__p9__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `The Company’s business can be impacted by political events, trade and other international disputes, geopolitical tensions, conflict, terrorism, natural`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__verify__p18__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__verify__p18__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__verify__p18__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__verify__p18__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__verify__p18__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | apple_2025_10k__verify__p18
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/apple_2025_10k__verify__p18__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `HOW TO OBTAIN COPIES`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `HOW TO OBTAIN COPIES`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'ocr', 'crop', 'read_page', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.542`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'ocr', 'crop', 'read_page', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.496`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'ocr', 'crop', 'read_page', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.542`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'ocr', 'crop', 'read_page', 'compute', 'answer']`
- Final: `answer` / `-14.94%`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.442`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'ocr', 'crop', 'read_page', 'compute', 'answer']`
- Final: `answer` / `-13.94`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.542`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'ocr', 'crop', 'read_page', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.292`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__numeric__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__numeric__p41__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'ocr', 'crop', 'read_page', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-14.94%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.542`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p134__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value in the 'Transportation' row immediately before the percent-change value '28.5%' is '1,807.8'.`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p134__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value in the 'Transportation' row immediately before the percent-change value '28.5%' is '1,807.8'.`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p134__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value in the 'Transportation' row immediately before the percent-change value '28.5%' is '1,807.8'.`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p134__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p134__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p134
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p134__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `1,807.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p41__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'HFCs' under the column '2022' is 182.8.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p41__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'HFCs' under the column '2022' is 182.8.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p41__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'HFCs' under the column '2022' is 182.8.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p41__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p41__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__table__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__table__p41__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `182.8`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | epa_ghg_inventory_1990_2022__verify__p41
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/epa_ghg_inventory_1990_2022__verify__p41__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `100.00%`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `101`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__numeric__p4__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `100.00%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.246`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__verify__p33__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__verify__p33__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__verify__p33__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__verify__p33__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__verify__p33__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | fda_ozempic_2025_label__verify__p33
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/fda_ozempic_2025_label__verify__p33__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p11__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p11__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p11__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Current Status and Trends`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p11__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p11
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p11__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Current Status and Trends`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p50__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p50__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p50__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Section 3`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p50__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__text__p50
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__text__p50__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Section 3`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | ipcc_ar6_syr_longer_report__verify__p43
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ipcc_ar6_syr_longer_report__verify__p43__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | irs_2025_form_1040__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/irs_2025_form_1040__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/irs_2025_form_1040__verify__p2__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/irs_2025_form_1040__verify__p2__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/irs_2025_form_1040__verify__p2__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/irs_2025_form_1040__verify__p2__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/irs_2025_form_1040__verify__p2__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | irs_2025_form_1040__verify__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/irs_2025_form_1040__verify__p2__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Drives scientific discovery`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Drives scientific discovery`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-42.71%`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.446`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `-41.71`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.296`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__numeric__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__numeric__p4__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'compute', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-42.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.546`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__table__p4__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'NASA Total' under 'FY 2025 Request' is 25,383.7.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__table__p4__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'NASA Total' under 'FY 2025 Request' is 25,383.7.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__table__p4__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'NASA Total' under 'FY 2025 Request' is 25,383.7.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__table__p4__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__table__p4__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__table__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__table__p4__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `25,383.7`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__text__p4__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__text__p4__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__text__p4__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `NASA’s FY 2025 Budget Request`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__text__p4__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__text__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__text__p4__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `NASA’s FY 2025 Budget Request`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__verify__p12__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__verify__p12__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__verify__p12__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__verify__p12__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__verify__p12__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | nasa_fy2025_budget_summary__verify__p12
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nasa_fy2025_budget_summary__verify__p12__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__direct_answer_without_tools.json`
- Task: `cross_page`
- Tool sequence: `['answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements, technology, tools, and standards to advance reliable, safe, transparent, explainable, privacy-enhanced, and fair artificial intelligence (AI).`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__hallucinated_evidence_ref.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements, technology, tools, and standards to advance reliable, safe, transparent, explainable, privacy-enhanced, and fair artificial intelligence (AI).`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__missing_evidence_observations.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements, technology, tools, and standards to advance reliable, safe, transparent, explainable, privacy-enhanced, and fair artificial intelligence (AI).`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__over_refusal_for_answerable.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__weak_search_only_evidence.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `About AI at NIST: The National Institute of Standards and Technology (NIST) develops measurements, technology, tools, and standards to advance reliable, safe, transparent, explainable, privacy-enhanced, and fair artificial intelligence (AI).`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__cross__p2_p3
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__cross__p2_p3__run01__wrong_final_answer.json`
- Task: `cross_page`
- Tool sequence: `['search', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `About AI at NIST`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__text__p5__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__text__p5__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__text__p5__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `1. Introduction`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__text__p5__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__text__p5
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__text__p5__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `1. Introduction`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__verify__p54__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__verify__p54__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__verify__p54__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__verify__p54__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__verify__p54__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | nist_ai_600_1_genai_profile__verify__p54
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/nist_ai_600_1_genai_profile__verify__p54__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'read_page', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.246`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__text__p2__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__text__p2__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__text__p2__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Syllabus`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__text__p2__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__text__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__text__p2__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Syllabus`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__verify__p4__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__verify__p4__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__verify__p4__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__verify__p4__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__verify__p4__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | scotus_loper_bright_2024__verify__p4
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/scotus_loper_bright_2024__verify__p4__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `The percentage change from 'Revenue Growth: Total TI' to 'Profit from Operations as a % of Revenue (Operating Profit Margin)' is 162.31%.`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `The percentage change from 'Revenue Growth: Total TI' to 'Profit from Operations as a % of Revenue (Operating Profit Margin)' is 162.31%.`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The percentage change from 'Revenue Growth: Total TI' to 'Profit from Operations as a % of Revenue (Operating Profit Margin)' is 162.31%.`
- Reference: `162.31%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `The percentage change from 'Revenue Growth: Total TI' to 'Profit from Operations as a % of Revenue (Operating Profit Margin)' is 162.31%.`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `The percentage change from 'Revenue Growth: Total TI' to 'Profit from Operations as a % of Revenue (Operating Profit Margin)' is 162.31%.`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `163.31`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__numeric__p97
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__numeric__p97__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `162.31%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.246`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The value for 'Common Stock, par value $1.00' under 'Trading Symbol(s)' is 'TXN'.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__table__p7
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__table__p7__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `TXN`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Government incentives`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | ti2025ars__text__p42
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/ti2025ars__text__p42__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Government incentives`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | compute_expression_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__compute_expression_mismatch.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `The percentage change for 'High-Touch Solutions N.A.' from 'Revenue' to 'Reported sales growth' is -85.71%.`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final numeric answer matches, but the successful compute provenance is inconsistent when recomputed.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__direct_answer_without_tools.json`
- Task: `numeric_computation`
- Tool sequence: `['answer']`
- Final: `answer` / `The percentage change for 'High-Touch Solutions N.A.' from 'Revenue' to 'Reported sales growth' is -85.71%.`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### review | missing_compute | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__dropped_compute_step.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `The percentage change for 'High-Touch Solutions N.A.' from 'Revenue' to 'Reported sales growth' is -85.71%.`
- Reference: `-85.71%`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `PARTIAL` / `The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__hallucinated_evidence_ref.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `The percentage change for 'High-Touch Solutions N.A.' from 'Revenue' to 'Reported sales growth' is -85.71%.`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__missing_evidence_observations.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `The percentage change for 'High-Touch Solutions N.A.' from 'Revenue' to 'Reported sales growth' is -85.71%.`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__numeric_near_miss.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `-84.71`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__over_refusal_for_answerable.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | numeric_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__numeric__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__numeric__p2__run01__wrong_final_answer.json`
- Task: `numeric_computation`
- Tool sequence: `['parse_table', 'compute', 'answer']`
- Final: `answer` / `999 percentage points`
- Reference: `-85.71%`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The numeric answer does not match the expected value or unit.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `$14.0B`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__table__p2
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__table__p2__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `$14.0B`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Technology Risks`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__text__p27
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__text__p27__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Technology Risks`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__direct_answer_without_tools.json`
- Task: `verification`
- Tool sequence: `['answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__hallucinated_evidence_ref.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__missing_evidence_observations.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4167`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__over_refusal_for_answerable.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.2667`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__verify_label_mismatch.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `SUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | verification_label_mismatch | dmxapi_gpt4o_2024_11_20__negative | tm2529296d2_ars__verify__p81
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/tm2529296d2_ars__verify__p81__run01__wrong_final_answer.json`
- Task: `verification`
- Tool sequence: `['read_page', 'verify', 'answer']`
- Final: `answer` / `UNSUPPORTED`
- Reference: `SUPPORTED`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5167`
- Claim `c1`: `NOT_SUPPORTED` / `The verify tool was used, but the final verification answer, verify observation label, or verify sufficiency does not match the expected label.`

### reject | insufficient_negative_evidence | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__refuse__generic
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__refuse__generic__run01__false_answer_for_unanswerable.json`
- Task: `unanswerable`
- Tool sequence: `['search', 'read_page', 'search', 'answer']`
- Final: `answer` / `The private mobile phone number is 555-0100.`
- Reference: `REFUSE`
- Support: `PARTIAL`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `PARTIAL` / `The refusal lacks the expected search/read_page negative-evidence path.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__table__p21__run01__direct_answer_without_tools.json`
- Task: `table_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Metallurgy and many sectors of the economy.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__table__p21__run01__hallucinated_evidence_ref.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `Metallurgy and many sectors of the economy.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__table__p21__run01__missing_evidence_observations.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `Metallurgy and many sectors of the economy.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.4`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__table__p21__run01__over_refusal_for_answerable.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.25`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__table__p21__run01__table_row_label_as_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `the requested row label`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | table_value_mismatch | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__table__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__table__p21__run01__wrong_final_answer.json`
- Task: `table_lookup`
- Tool sequence: `['parse_table', 'answer']`
- Final: `answer` / `NOT_IN_TABLE`
- Reference: `Metallurgy and many sectors of the economy.`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.5`
- Claim `c1`: `NOT_SUPPORTED` / `The table evidence contains the expected value, but the final answer does not match it.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p1__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p1__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p1__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `U.S. Department of the Interior`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p1__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p1
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p1__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `U.S. Department of the Interior`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p21__run01__direct_answer_without_tools.json`
- Task: `text_lookup`
- Tool sequence: `['answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.35`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | invalid_evidence_ref | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p21__run01__hallucinated_evidence_ref.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`
- Claim `c2`: `NOT_SUPPORTED` / `The terminal answer cites evidence_refs that were not observed in the trajectory.`

### reject | missing_evidence | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p21__run01__missing_evidence_observations.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Table 4.—The 2022 U.S. Critical Minerals List`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `MISSING`
- Quality score: `0.45`
- Claim `c1`: `NOT_SUPPORTED` / `No evidence was available for the claim.`
- Claim `c2`: `NOT_SUPPORTED` / `No evidence was available for the claim.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p21__run01__over_refusal_for_answerable.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'refuse']`
- Final: `refuse` / `I cannot answer because the document does not provide sufficient evidence.`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.3`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

### reject | answer_mismatch | dmxapi_gpt4o_2024_11_20__negative | usgs_mcs_2025__text__p21
- File: `data/h3/negative_diverse_v2/corrupted_rollouts/dmxapi_gpt4o_2024_11_20__negative/usgs_mcs_2025__text__p21__run01__wrong_final_answer.json`
- Task: `text_lookup`
- Tool sequence: `['read_page', 'answer']`
- Final: `answer` / `Incorrect heading not supported by the document`
- Reference: `Table 4.—The 2022 U.S. Critical Minerals List`
- Support: `NOT_SUPPORTED`
- Sufficiency: `INSUFFICIENT`
- Quality score: `0.55`
- Claim `c1`: `NOT_SUPPORTED` / `The final answer does not match the expected answer or evidence.`

## Notes

This implementation performs the full DocVerify++ pipeline for the pilot setting: claim decomposition, evidence collection from trajectory observations, evidence ranking, claim-evidence support judgment, sufficiency judgment, reward scoring, filtering, and optional human calibration.
The current support judge is a deterministic rule/NLI-lite implementation. It is suitable for pilot filtering and auditing; it can be replaced by an external NLI or LLM judge without changing the output schema.