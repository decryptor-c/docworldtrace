# Pilot Exp-2 Evaluation

- Rollout dir: `data/h2/rollouts_v5`
- Format compliance: `99.17%`
- Proper termination: `99.17%`
- Strict answer correct rate: `85.83%`
- Adjusted answer correct rate: `99.17%`
- Mean answer F1: `88.26%`
- Avg steps: `2.825`
- Verify usage: `10.00%`
- Refuse usage: `20.00%`
- Direct answer rate: `0.00%`

## By Teacher

### dmxapi_gemini_2_5_flash
- Count: `40`
- Format compliance: `97.50%`
- Proper termination: `97.50%`
- Strict answer correct rate: `97.50%`
- Adjusted answer correct rate: `97.50%`
- Mean answer F1: `97.50%`
- Avg steps: `2.85`

### dmxapi_gemini_3_1_flash_lite_preview
- Count: `40`
- Format compliance: `100.00%`
- Proper termination: `100.00%`
- Strict answer correct rate: `75.00%`
- Adjusted answer correct rate: `100.00%`
- Mean answer F1: `80.54%`
- Avg steps: `2.675`

### dmxapi_gpt4o_2024_11_20
- Count: `40`
- Format compliance: `100.00%`
- Proper termination: `100.00%`
- Strict answer correct rate: `85.00%`
- Adjusted answer correct rate: `100.00%`
- Mean answer F1: `86.76%`
- Avg steps: `2.95`

## By Task Type

### cross_page
- Count: `24`
- Strict answer correct rate: `58.33%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.2917`

### unanswerable
- Count: `24`
- Strict answer correct rate: `100.00%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.0`

### text_lookup
- Count: `30`
- Strict answer correct rate: `93.33%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `2.0`

### verification
- Count: `12`
- Strict answer correct rate: `100.00%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.5`

### numeric_computation
- Count: `18`
- Strict answer correct rate: `94.44%`
- Adjusted answer correct rate: `94.44%`
- Avg steps: `3.1111`

### table_lookup
- Count: `12`
- Strict answer correct rate: `66.67%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `2.5`

## Failure Categories

- format_error: `1`
- strict_correct: `103`
- strict_eval_false_negative: `16`
