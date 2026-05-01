# H4 Trajectory Diversity Analysis

- Rollout dir: `data/h2/rollouts_corrected_v1`
- DocVerify++ input: `data/h3/docverify_plus_corrected_v1/docverify_review.json`
- H4-lite passed: `True`

## Overall

- Count: `162`
- Unique seed count: `54`
- Unique sequence count: `39`
- Unique sequence ratio: `24.07%`
- Seed-level unique sequence ratio: `72.22%`
- Action coverage: `8/10` `['answer', 'compute', 'ocr', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`
- Core pilot action coverage: `7/7` `['answer', 'compute', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`
- Step count mean/std: `3.2037` / `1.238`
- Step count distribution: `{3: 65, 5: 14, 4: 32, 2: 41, 7: 2, 1: 2, 8: 2, 0: 2, 6: 2}`
- Rule-based template match rate: `45.68%`
- Rule-based deviation rate: `54.32%`
- Search calls: `113`
- Unique search query count: `70`
- Unique search query ratio: `61.95%`
- Seeds with search: `31`
- Unique seed-query pair count: `95`
- Unique seed-query pair ratio: `84.07%`

## H4-Lite Decision

- h4_lite_passed: `True`
- task_coverage_ok: `True`
- core_action_coverage_ok: `True`
- sequence_diversity_ok: `True`
- search_query_diversity_ok: `True`
- covered_tasks: `['cross_page', 'numeric_computation', 'table_lookup', 'text_lookup', 'unanswerable', 'verification']`
- expected_tasks: `['cross_page', 'numeric_computation', 'table_lookup', 'text_lookup', 'unanswerable', 'verification']`
- rationale: `H4-lite passes when six task types are covered, core pilot actions are used, at least six unique tool sequences appear, and seed-level search queries are not highly duplicated.`

## Original H4 Gates

- strict_original_passed: `False`
- seed_normalized_passed: `False`
- unique_sequence_ratio_ok: `False`
- seed_level_unique_sequence_ratio_ok: `True`
- action_coverage_ok: `True`
- step_count_std_ok: `False`
- rule_based_deviation_ok: `True`
- search_duplicate_rate_ok: `False`
- thresholds: `{'unique_sequence_ratio': '>= 0.50', 'seed_level_unique_sequence_ratio': '>= 0.50', 'action_coverage_count': '>= 7', 'step_count_std': '>= 1.50', 'rule_based_deviation_rate': '>= 0.40', 'search_duplicate_rate': '< 0.30'}`
- observed: `{'unique_sequence_ratio': 0.2407, 'seed_level_unique_sequence_ratio': 0.7222, 'action_coverage_count': 8, 'step_count_std': 1.238, 'rule_based_deviation_rate': 0.5432, 'search_duplicate_rate': 0.3805}`

## Top Tool Sequences

- `read_page -> answer`: `39`
- `search -> read_page -> refuse`: `23`
- `search -> read_page -> verify -> answer`: `17`
- `search -> read_page -> answer`: `15`
- `read_page -> parse_table -> answer`: `11`
- `search -> verify -> answer`: `6`
- `search -> read_page -> search -> read_page -> refuse`: `5`
- `search -> search -> read_page -> refuse`: `4`
- `parse_table -> compute -> answer`: `4`
- `parse_table -> read_page -> compute -> answer`: `3`
- `read_page -> compute -> answer`: `2`
- `search -> search -> refuse`: `2`
- `<empty>`: `2`
- `read_page -> refuse`: `2`
- `search -> read_page -> read_page -> read_page -> refuse`: `2`
- `search -> read_page -> read_page -> answer`: `2`
- `search -> search -> read_page -> search -> search -> read_page -> refuse`: `1`
- `read_page -> parse_table -> parse_table -> ocr -> ocr -> compute -> answer`: `1`
- `read_page`: `1`
- `search -> read_page -> verify -> verify -> answer`: `1`

## By Task Type

### cross_page
- Count: `18`
- Unique sequence count: `3`
- Step mean/std: `3.2222` / `0.5329`
- Action coverage: `['answer', 'read_page', 'search']`
- Paths:
  - `search -> read_page -> answer`: `15`
  - `search -> read_page -> read_page -> answer`: `2`
  - `search -> read_page -> read_page -> read_page -> answer`: `1`

### numeric_computation
- Count: `15`
- Unique sequence count: `8`
- Step mean/std: `3.1333` / `1.7461`
- Action coverage: `['answer', 'compute', 'ocr', 'parse_table', 'read_page']`
- Paths:
  - `parse_table -> compute -> answer`: `4`
  - `parse_table -> read_page -> compute -> answer`: `3`
  - `read_page -> compute -> answer`: `2`
  - `<empty>`: `2`
  - `read_page -> parse_table -> parse_table -> ocr -> ocr -> compute -> answer`: `1`
  - `parse_table`: `1`
  - `parse_table -> ocr -> read_page -> compute -> answer`: `1`
  - `parse_table -> ocr -> compute -> answer`: `1`

### table_lookup
- Count: `24`
- Unique sequence count: `10`
- Step mean/std: `3.0833` / `1.3202`
- Action coverage: `['answer', 'ocr', 'parse_table', 'read_page', 'refuse', 'search']`
- Paths:
  - `read_page -> parse_table -> answer`: `11`
  - `read_page -> answer`: `5`
  - `read_page`: `1`
  - `read_page -> parse_table -> ocr -> answer`: `1`
  - `read_page -> search -> ocr -> refuse`: `1`
  - `read_page -> refuse`: `1`
  - `read_page -> search -> read_page -> search -> ocr -> search -> read_page -> refuse`: `1`
  - `read_page -> ocr -> parse_table -> ocr -> refuse`: `1`
  - `read_page -> parse_table -> ocr -> refuse`: `1`
  - `read_page -> ocr -> refuse`: `1`

### text_lookup
- Count: `33`
- Unique sequence count: `1`
- Step mean/std: `2` / `0.0`
- Action coverage: `['answer', 'read_page']`
- Paths:
  - `read_page -> answer`: `33`

### unanswerable
- Count: `42`
- Unique sequence count: `11`
- Step mean/std: `3.6667` / `1.0389`
- Action coverage: `['read_page', 'refuse', 'search']`
- Paths:
  - `search -> read_page -> refuse`: `23`
  - `search -> read_page -> search -> read_page -> refuse`: `5`
  - `search -> search -> read_page -> refuse`: `4`
  - `search -> search -> refuse`: `2`
  - `search -> read_page -> read_page -> read_page -> refuse`: `2`
  - `search -> search -> read_page -> search -> search -> read_page -> refuse`: `1`
  - `search -> search -> search -> refuse`: `1`
  - `search -> search -> read_page -> search -> refuse`: `1`
  - `search -> read_page -> read_page -> refuse`: `1`
  - `read_page -> refuse`: `1`
  - `search -> read_page -> search -> read_page -> search -> refuse`: `1`

### verification
- Count: `30`
- Unique sequence count: `9`
- Step mean/std: `4` / `1.0646`
- Action coverage: `['answer', 'read_page', 'search', 'verify']`
- Paths:
  - `search -> read_page -> verify -> answer`: `17`
  - `search -> verify -> answer`: `6`
  - `search -> read_page -> verify -> verify -> answer`: `1`
  - `search -> verify -> verify -> read_page -> verify -> verify -> verify -> answer`: `1`
  - `read_page -> answer`: `1`
  - `read_page -> verify -> answer`: `1`
  - `search -> search -> read_page -> verify -> answer`: `1`
  - `search -> read_page -> search -> read_page -> verify -> answer`: `1`
  - `search -> read_page -> read_page -> verify -> answer`: `1`

## Rule-Based Template Baseline

### cross_page
- Template: `search -> read_page -> read_page -> answer`
- Match rate: `11.11%`
- Deviation rate: `88.89%`
- Deviating sequences:
  - `search -> read_page -> answer`: `15`
  - `search -> read_page -> read_page -> read_page -> answer`: `1`

### numeric_computation
- Template: `parse_table -> compute -> answer`
- Match rate: `26.67%`
- Deviation rate: `73.33%`
- Deviating sequences:
  - `parse_table -> read_page -> compute -> answer`: `3`
  - `read_page -> compute -> answer`: `2`
  - `<empty>`: `2`
  - `read_page -> parse_table -> parse_table -> ocr -> ocr -> compute -> answer`: `1`
  - `parse_table`: `1`
  - `parse_table -> ocr -> read_page -> compute -> answer`: `1`
  - `parse_table -> ocr -> compute -> answer`: `1`

### table_lookup
- Template: `read_page -> parse_table -> answer`
- Match rate: `45.83%`
- Deviation rate: `54.17%`
- Deviating sequences:
  - `read_page -> answer`: `5`
  - `read_page`: `1`
  - `read_page -> parse_table -> ocr -> answer`: `1`
  - `read_page -> search -> ocr -> refuse`: `1`
  - `read_page -> refuse`: `1`
  - `read_page -> search -> read_page -> search -> ocr -> search -> read_page -> refuse`: `1`
  - `read_page -> ocr -> parse_table -> ocr -> refuse`: `1`
  - `read_page -> parse_table -> ocr -> refuse`: `1`
  - `read_page -> ocr -> refuse`: `1`

### text_lookup
- Template: `read_page -> answer`
- Match rate: `100.00%`
- Deviation rate: `0.00%`
- Deviating sequences:

### unanswerable
- Template: `search -> read_page -> refuse`
- Match rate: `54.76%`
- Deviation rate: `45.24%`
- Deviating sequences:
  - `search -> read_page -> search -> read_page -> refuse`: `5`
  - `search -> search -> read_page -> refuse`: `4`
  - `search -> search -> refuse`: `2`
  - `search -> read_page -> read_page -> read_page -> refuse`: `2`
  - `search -> search -> read_page -> search -> search -> read_page -> refuse`: `1`
  - `search -> search -> search -> refuse`: `1`
  - `search -> search -> read_page -> search -> refuse`: `1`
  - `search -> read_page -> read_page -> refuse`: `1`
  - `read_page -> refuse`: `1`
  - `search -> read_page -> search -> read_page -> search -> refuse`: `1`

### verification
- Template: `read_page -> verify -> answer`
- Match rate: `3.33%`
- Deviation rate: `96.67%`
- Deviating sequences:
  - `search -> read_page -> verify -> answer`: `17`
  - `search -> verify -> answer`: `6`
  - `search -> read_page -> verify -> verify -> answer`: `1`
  - `search -> verify -> verify -> read_page -> verify -> verify -> verify -> answer`: `1`
  - `read_page -> answer`: `1`
  - `search -> search -> read_page -> verify -> answer`: `1`
  - `search -> read_page -> search -> read_page -> verify -> answer`: `1`
  - `search -> read_page -> read_page -> verify -> answer`: `1`

## Kept Trajectories Only

- Count: `139`
- Unique sequence count: `28`
- Unique sequence ratio: `20.14%`
- Action coverage: `8/10` `['answer', 'compute', 'ocr', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`

## Interpretation

H4 evaluates whether supported trajectories are diverse enough to serve as process data rather than repeated answer-only templates.
For the current pilot, the strict original threshold of unique_sequence_ratio >= 50% may be too high because each seed is repeated across two teachers and two runs. H4-lite therefore emphasizes task coverage, core action coverage, and task-specific path separation.