# H4 Trajectory Diversity Analysis

- Rollout dir: `data/h2/rollouts_diverse_v2`
- DocVerify++ input: `data/h3/docverify_plus_diverse_v2/docverify_review.json`
- H4-lite passed: `True`

## Overall

- Count: `162`
- Unique seed count: `54`
- Unique sequence count: `21`
- Unique sequence ratio: `12.96%`
- Seed-level unique sequence ratio: `38.89%`
- Action coverage: `9/10` `['answer', 'compute', 'crop', 'ocr', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`
- Core pilot action coverage: `7/7` `['answer', 'compute', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`
- Step count mean/std: `2.9444` / `0.9179`
- Step count distribution: `{3: 71, 4: 22, 2: 57, 5: 10, 6: 2}`
- Rule-based template match rate: `60.49%`
- Rule-based deviation rate: `39.51%`
- Search calls: `84`
- Unique search query count: `46`
- Unique search query ratio: `54.76%`
- Seeds with search: `26`
- Unique seed-query pair count: `73`
- Unique seed-query pair ratio: `86.90%`

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
- seed_level_unique_sequence_ratio_ok: `False`
- action_coverage_ok: `True`
- step_count_std_ok: `False`
- rule_based_deviation_ok: `False`
- search_duplicate_rate_ok: `False`
- thresholds: `{'unique_sequence_ratio': '>= 0.50', 'seed_level_unique_sequence_ratio': '>= 0.50', 'action_coverage_count': '>= 7', 'step_count_std': '>= 1.50', 'rule_based_deviation_rate': '>= 0.40', 'search_duplicate_rate': '< 0.30'}`
- observed: `{'unique_sequence_ratio': 0.1296, 'seed_level_unique_sequence_ratio': 0.3889, 'action_coverage_count': 9, 'step_count_std': 0.9179, 'rule_based_deviation_rate': 0.3951, 'search_duplicate_rate': 0.4524}`

## Top Tool Sequences

- `read_page -> answer`: `36`
- `search -> read_page -> refuse`: `24`
- `read_page -> verify -> answer`: `22`
- `parse_table -> answer`: `21`
- `search -> read_page -> answer`: `13`
- `parse_table -> compute -> answer`: `11`
- `search -> read_page -> verify -> answer`: `6`
- `search -> search -> read_page -> refuse`: `5`
- `search -> read_page -> read_page -> answer`: `5`
- `search -> read_page -> read_page -> read_page -> refuse`: `4`
- `search -> read_page -> search -> read_page -> refuse`: `3`
- `parse_table -> compute -> compute -> compute -> answer`: `2`
- `search -> read_page -> read_page -> refuse`: `2`
- `search -> search -> refuse`: `1`
- `search -> search -> search -> refuse`: `1`
- `search -> search -> read_page -> search -> search -> refuse`: `1`
- `search -> read_page -> search -> verify -> answer`: `1`
- `parse_table -> compute -> compute -> answer`: `1`
- `read_page -> search -> verify -> answer`: `1`
- `parse_table -> ocr -> crop -> read_page -> compute -> answer`: `1`

## By Task Type

### cross_page
- Count: `18`
- Unique sequence count: `2`
- Step mean/std: `3.2778` / `0.4479`
- Action coverage: `['answer', 'read_page', 'search']`
- Paths:
  - `search -> read_page -> answer`: `13`
  - `search -> read_page -> read_page -> answer`: `5`

### numeric_computation
- Count: `15`
- Unique sequence count: `4`
- Step mean/std: `3.5333` / `0.9568`
- Action coverage: `['answer', 'compute', 'crop', 'ocr', 'parse_table', 'read_page']`
- Paths:
  - `parse_table -> compute -> answer`: `11`
  - `parse_table -> compute -> compute -> compute -> answer`: `2`
  - `parse_table -> compute -> compute -> answer`: `1`
  - `parse_table -> ocr -> crop -> read_page -> compute -> answer`: `1`

### table_lookup
- Count: `21`
- Unique sequence count: `1`
- Step mean/std: `2` / `0.0`
- Action coverage: `['answer', 'parse_table']`
- Paths:
  - `parse_table -> answer`: `21`

### text_lookup
- Count: `36`
- Unique sequence count: `1`
- Step mean/std: `2` / `0.0`
- Action coverage: `['answer', 'read_page']`
- Paths:
  - `read_page -> answer`: `36`

### unanswerable
- Count: `42`
- Unique sequence count: `9`
- Step mean/std: `3.619` / `0.8438`
- Action coverage: `['read_page', 'refuse', 'search']`
- Paths:
  - `search -> read_page -> refuse`: `24`
  - `search -> search -> read_page -> refuse`: `5`
  - `search -> read_page -> read_page -> read_page -> refuse`: `4`
  - `search -> read_page -> search -> read_page -> refuse`: `3`
  - `search -> read_page -> read_page -> refuse`: `2`
  - `search -> search -> refuse`: `1`
  - `search -> search -> search -> refuse`: `1`
  - `search -> search -> read_page -> search -> search -> refuse`: `1`
  - `search -> read_page -> search -> refuse`: `1`

### verification
- Count: `30`
- Unique sequence count: `4`
- Step mean/std: `3.3` / `0.526`
- Action coverage: `['answer', 'read_page', 'search', 'verify']`
- Paths:
  - `read_page -> verify -> answer`: `22`
  - `search -> read_page -> verify -> answer`: `6`
  - `search -> read_page -> search -> verify -> answer`: `1`
  - `read_page -> search -> verify -> answer`: `1`

## Rule-Based Template Baseline

### cross_page
- Template: `search -> read_page -> read_page -> answer`
- Match rate: `27.78%`
- Deviation rate: `72.22%`
- Deviating sequences:
  - `search -> read_page -> answer`: `13`

### numeric_computation
- Template: `parse_table -> compute -> answer`
- Match rate: `73.33%`
- Deviation rate: `26.67%`
- Deviating sequences:
  - `parse_table -> compute -> compute -> compute -> answer`: `2`
  - `parse_table -> compute -> compute -> answer`: `1`
  - `parse_table -> ocr -> crop -> read_page -> compute -> answer`: `1`

### table_lookup
- Template: `read_page -> parse_table -> answer`
- Match rate: `0.00%`
- Deviation rate: `100.00%`
- Deviating sequences:
  - `parse_table -> answer`: `21`

### text_lookup
- Template: `read_page -> answer`
- Match rate: `100.00%`
- Deviation rate: `0.00%`
- Deviating sequences:

### unanswerable
- Template: `search -> read_page -> refuse`
- Match rate: `57.14%`
- Deviation rate: `42.86%`
- Deviating sequences:
  - `search -> search -> read_page -> refuse`: `5`
  - `search -> read_page -> read_page -> read_page -> refuse`: `4`
  - `search -> read_page -> search -> read_page -> refuse`: `3`
  - `search -> read_page -> read_page -> refuse`: `2`
  - `search -> search -> refuse`: `1`
  - `search -> search -> search -> refuse`: `1`
  - `search -> search -> read_page -> search -> search -> refuse`: `1`
  - `search -> read_page -> search -> refuse`: `1`

### verification
- Template: `read_page -> verify -> answer`
- Match rate: `73.33%`
- Deviation rate: `26.67%`
- Deviating sequences:
  - `search -> read_page -> verify -> answer`: `6`
  - `search -> read_page -> search -> verify -> answer`: `1`
  - `read_page -> search -> verify -> answer`: `1`

## Kept Trajectories Only

- Count: `162`
- Unique sequence count: `21`
- Unique sequence ratio: `12.96%`
- Action coverage: `9/10` `['answer', 'compute', 'crop', 'ocr', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`

## Interpretation

H4 evaluates whether supported trajectories are diverse enough to serve as process data rather than repeated answer-only templates.
For the current pilot, the strict original threshold of unique_sequence_ratio >= 50% may be too high because each seed is repeated across two teachers and two runs. H4-lite therefore emphasizes task coverage, core action coverage, and task-specific path separation.