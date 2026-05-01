# Pilot Exp-2 Evaluation

- Rollout dir: `data/h2/rollouts_diverse_v2`
- Format compliance: `100.00%`
- Proper termination: `100.00%`
- Strict answer correct rate: `89.51%`
- Adjusted answer correct rate: `100.00%`
- Mean answer F1: `91.60%`
- Avg steps: `2.9444`
- Verify usage: `18.52%`
- Refuse usage: `25.93%`
- Direct answer rate: `0.00%`

## By Teacher

### dmxapi_gemini_2_5_flash
- Count: `54`
- Format compliance: `100.00%`
- Proper termination: `100.00%`
- Strict answer correct rate: `98.15%`
- Adjusted answer correct rate: `100.00%`
- Mean answer F1: `98.97%`
- Avg steps: `3.0`

### dmxapi_gemini_3_1_flash_lite_preview
- Count: `54`
- Format compliance: `100.00%`
- Proper termination: `100.00%`
- Strict answer correct rate: `90.74%`
- Adjusted answer correct rate: `100.00%`
- Mean answer F1: `91.60%`
- Avg steps: `2.7407`

### dmxapi_gpt4o_2024_11_20
- Count: `54`
- Format compliance: `100.00%`
- Proper termination: `100.00%`
- Strict answer correct rate: `79.63%`
- Adjusted answer correct rate: `100.00%`
- Mean answer F1: `84.24%`
- Avg steps: `3.0926`

## By Task Type

### cross_page
- Count: `18`
- Strict answer correct rate: `72.22%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.2778`

### unanswerable
- Count: `42`
- Strict answer correct rate: `100.00%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.619`

### verification
- Count: `30`
- Strict answer correct rate: `100.00%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.3`

### text_lookup
- Count: `36`
- Strict answer correct rate: `97.22%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `2.0`

### table_lookup
- Count: `21`
- Strict answer correct rate: `57.14%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `2.0`

### numeric_computation
- Count: `15`
- Strict answer correct rate: `86.67%`
- Adjusted answer correct rate: `100.00%`
- Avg steps: `3.5333`

## Failure Categories

- strict_correct: `145`
- strict_eval_false_negative: `17`
