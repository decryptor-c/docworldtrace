# H4 Trajectory Diversity Analysis

- Rollout dir: `data/h2/rollouts_v5`
- DocVerify++ input: `data/h3/docverify_plus_v5/docverify_review.json`
- H4-lite passed: `False`

## Overall

- Count: `120`
- Unique seed count: `20`
- Unique sequence count: `12`
- Unique sequence ratio: `10.00%`
- Seed-level unique sequence ratio: `60.00%`
- Action coverage: `8/10` `['answer', 'compute', 'crop', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`
- Core pilot action coverage: `7/7` `['answer', 'compute', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`
- Step count mean/std: `2.8167` / `0.6706`
- Step count distribution: `{3: 68, 2: 36, 4: 14, 1: 1, 5: 1}`
- Rule-based template match rate: `73.33%`
- Rule-based deviation rate: `26.67%`
- Search calls: `54`
- Unique search query count: `15`
- Unique search query ratio: `27.78%`
- Seeds with search: `10`
- Unique seed-query pair count: `15`
- Unique seed-query pair ratio: `27.78%`

## H4-Lite Decision

- h4_lite_passed: `False`
- task_coverage_ok: `True`
- core_action_coverage_ok: `True`
- sequence_diversity_ok: `True`
- search_query_diversity_ok: `False`
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
- rule_based_deviation_ok: `False`
- search_duplicate_rate_ok: `False`
- thresholds: `{'unique_sequence_ratio': '>= 0.50', 'seed_level_unique_sequence_ratio': '>= 0.50', 'action_coverage_count': '>= 7', 'step_count_std': '>= 1.50', 'rule_based_deviation_rate': '>= 0.40', 'search_duplicate_rate': '< 0.30'}`
- observed: `{'unique_sequence_ratio': 0.1, 'seed_level_unique_sequence_ratio': 0.6, 'action_coverage_count': 8, 'step_count_std': 0.6706, 'rule_based_deviation_rate': 0.2667, 'search_duplicate_rate': 0.7222}`

## Top Tool Sequences

- `read_page -> answer`: `31`
- `search -> read_page -> refuse`: `24`
- `search -> read_page -> answer`: `17`
- `parse_table -> compute -> answer`: `15`
- `search -> read_page -> read_page -> answer`: `7`
- `search -> read_page -> verify -> answer`: `6`
- `read_page -> parse_table -> answer`: `6`
- `read_page -> verify -> answer`: `6`
- `parse_table -> answer`: `5`
- `parse_table`: `1`
- `read_page -> parse_table -> compute -> answer`: `1`
- `read_page -> crop -> compute -> compute -> answer`: `1`

## By Task Type

### cross_page
- Count: `24`
- Unique sequence count: `2`
- Step mean/std: `3.2917` / `0.4545`
- Action coverage: `['answer', 'read_page', 'search']`
- Paths:
  - `search -> read_page -> answer`: `17`
  - `search -> read_page -> read_page -> answer`: `7`

### numeric_computation
- Count: `18`
- Unique sequence count: `4`
- Step mean/std: `3.0556` / `0.7049`
- Action coverage: `['answer', 'compute', 'crop', 'parse_table', 'read_page']`
- Paths:
  - `parse_table -> compute -> answer`: `15`
  - `parse_table`: `1`
  - `read_page -> parse_table -> compute -> answer`: `1`
  - `read_page -> crop -> compute -> compute -> answer`: `1`

### table_lookup
- Count: `12`
- Unique sequence count: `3`
- Step mean/std: `2.5` / `0.5`
- Action coverage: `['answer', 'parse_table', 'read_page']`
- Paths:
  - `read_page -> parse_table -> answer`: `6`
  - `parse_table -> answer`: `5`
  - `read_page -> answer`: `1`

### text_lookup
- Count: `30`
- Unique sequence count: `1`
- Step mean/std: `2` / `0.0`
- Action coverage: `['answer', 'read_page']`
- Paths:
  - `read_page -> answer`: `30`

### unanswerable
- Count: `24`
- Unique sequence count: `1`
- Step mean/std: `3` / `0.0`
- Action coverage: `['read_page', 'refuse', 'search']`
- Paths:
  - `search -> read_page -> refuse`: `24`

### verification
- Count: `12`
- Unique sequence count: `2`
- Step mean/std: `3.5` / `0.5`
- Action coverage: `['answer', 'read_page', 'search', 'verify']`
- Paths:
  - `search -> read_page -> verify -> answer`: `6`
  - `read_page -> verify -> answer`: `6`

## Rule-Based Template Baseline

### cross_page
- Template: `search -> read_page -> read_page -> answer`
- Match rate: `29.17%`
- Deviation rate: `70.83%`
- Deviating sequences:
  - `search -> read_page -> answer`: `17`

### numeric_computation
- Template: `parse_table -> compute -> answer`
- Match rate: `83.33%`
- Deviation rate: `16.67%`
- Deviating sequences:
  - `parse_table`: `1`
  - `read_page -> parse_table -> compute -> answer`: `1`
  - `read_page -> crop -> compute -> compute -> answer`: `1`

### table_lookup
- Template: `read_page -> parse_table -> answer`
- Match rate: `50.00%`
- Deviation rate: `50.00%`
- Deviating sequences:
  - `parse_table -> answer`: `5`
  - `read_page -> answer`: `1`

### text_lookup
- Template: `read_page -> answer`
- Match rate: `100.00%`
- Deviation rate: `0.00%`
- Deviating sequences:

### unanswerable
- Template: `search -> read_page -> refuse`
- Match rate: `100.00%`
- Deviation rate: `0.00%`
- Deviating sequences:

### verification
- Template: `read_page -> verify -> answer`
- Match rate: `50.00%`
- Deviation rate: `50.00%`
- Deviating sequences:
  - `search -> read_page -> verify -> answer`: `6`

## Kept Trajectories Only

- Count: `116`
- Unique sequence count: `11`
- Unique sequence ratio: `9.48%`
- Action coverage: `8/10` `['answer', 'compute', 'crop', 'parse_table', 'read_page', 'refuse', 'search', 'verify']`

## Interpretation

H4 evaluates whether supported trajectories are diverse enough to serve as process data rather than repeated answer-only templates.
For the current pilot, the strict original threshold of unique_sequence_ratio >= 50% may be too high because each seed is repeated across two teachers and two runs. H4-lite therefore emphasizes task coverage, core action coverage, and task-specific path separation.