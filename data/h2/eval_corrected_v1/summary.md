# Pilot Exp-2 Evaluation

- Rollout dir: `data/h2/rollouts_corrected_v1`
- Format compliance: `97.53%`
- Proper termination: `97.53%`
- Strict answer correct rate: `75.93%`
- Adjusted answer correct rate: `87.65%`
- Mean answer F1: `77.46%`
- Avg steps: `3.2284`
- Verify usage: `17.90%`
- Refuse usage: `29.63%`
- Direct answer rate: `0.00%`

## By Teacher

### dmxapi_gemini_2_5_flash
- Count: `54`
- Format compliance: `94.44%`
- Proper termination: `94.44%`
- Strict answer correct rate: `83.33%`
- Adjusted answer correct rate: `88.89%`
- Mean answer F1: `83.75%`
- Avg steps: `3.3704`

### dmxapi_gemini_3_1_flash_lite_preview
- Count: `54`
- Format compliance: `98.15%`
- Proper termination: `98.15%`
- Strict answer correct rate: `72.22%`
- Adjusted answer correct rate: `87.04%`
- Mean answer F1: `73.83%`
- Avg steps: `2.8704`

### dmxapi_gpt4o_2024_11_20
- Count: `54`
- Format compliance: `100.00%`
- Proper termination: `100.00%`
- Strict answer correct rate: `72.22%`
- Adjusted answer correct rate: `87.04%`
- Mean answer F1: `74.81%`
- Avg steps: `3.4444`

## By Task Type

### cross_page
- Count: `18`
- Strict answer correct rate: `38.89%`
- Adjusted answer correct rate: `77.78%`
- Avg steps: `3.2222`

### unanswerable
- Count: `42`
- Strict answer correct rate: `100.00%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.6667`

### verification
- Count: `30`
- Strict answer correct rate: `96.67%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `4.0`

### text_lookup
- Count: `33`
- Strict answer correct rate: `81.82%`
- Adjusted answer correct rate: `84.85%`
- Avg steps: `2.0`

### table_lookup
- Count: `24`
- Strict answer correct rate: `37.50%`
- Adjusted answer correct rate: `70.83%`
- Avg steps: `3.125`

### numeric_computation
- Count: `15`
- Strict answer correct rate: `60.00%`
- Adjusted answer correct rate: `73.33%`
- Avg steps: `3.3333`

## Failure Categories

- format_error: `4`
- incorrect_refusal: `6`
- strict_correct: `122`
- strict_eval_false_negative: `20`
- strict_metric_false_positive: `1`
- wrong_answer: `9`
