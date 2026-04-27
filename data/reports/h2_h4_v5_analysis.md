# H2-H4 V5 Analysis

## Scope

- Seed file: `data/h2/seeds/pilot_seeds_v5.jsonl`
- Teacher models:
  - `gpt-4o-2024-11-20`
  - `gemini-2.5-flash`
  - `gemini-3.1-flash-lite-preview`
- Rollouts: `120 = 20 seeds x 3 teachers x 2 repeats`
- Rollout dir: `data/h2/rollouts_v5`

## H2 Result

| Metric | Result |
|---|---:|
| Count | 120 |
| Format compliance | 99.17% |
| Proper termination | 99.17% |
| Strict answer correct | 85.83% |
| Adjusted answer correct | 99.17% |
| Direct answer rate | 0% |
| Average steps | 2.825 |

By teacher:

| Teacher | Count | Format | Proper | Adjusted Correct | Direct Answer |
|---|---:|---:|---:|---:|---:|
| `dmxapi_gpt4o_2024_11_20` | 40 | 100% | 100% | 100% | 0% |
| `dmxapi_gemini_2_5_flash` | 40 | 97.5% | 97.5% | 97.5% | 0% |
| `dmxapi_gemini_3_1_flash_lite_preview` | 40 | 100% | 100% | 100% | 0% |

Main H2 failure:

| File | Teacher | Seed | Issue |
|---|---|---|---|
| `data/h2/rollouts_v5/dmxapi_gemini_2_5_flash/ti2025ars__numeric_free_cash_flow_margin_change_p29__run01.json` | `gemini-2.5-flash` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | Format error: trajectory stopped after `parse_table` and did not terminate with `answer` |

## H2 Path Review

| Metric | Result |
|---|---:|
| Evidence path OK | 99.17% |
| Acceptable path OK | 98.33% |
| Proper termination | 99.17% |
| Non-terminal tool use | 100% |
| Successful evidence observation | 100% |
| Strict path OK | 76.67% |

The strict path rate is lower because strict checking requires exact required-tool coverage. The more important pilot indicators are evidence path and acceptable path.

Non-acceptable cases:

| Case | Teacher | Seed | Path | Reason |
|---|---|---|---|---|
| Format error | `gemini-2.5-flash` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `parse_table` | Missing terminal `answer` and missing `compute` |
| Tool path not acceptable | `gemini-3.1-flash-lite-preview` | `ti2025ars__table__p7` | `read_page -> answer` | Correct answer but missing `parse_table`, so table evidence is insufficient |

## H3 Positive DocVerify++

| Metric | Result |
|---|---:|
| Count | 120 |
| Support rate | 98.33% |
| Sufficiency rate | 98.33% |
| Keep rate | 98.33% |
| Review rate | 0.83% |
| Reject rate | 0.83% |
| Adjusted answer correct | 99.17% |

H3 flags exactly the two important cases:

| Decision | Failure | Teacher | Seed | Reason |
|---|---|---|---|---|
| `reject` | `format_error` | `gemini-2.5-flash` | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | Invalid rollout without final answer/refuse |
| `review` | `missing_table_evidence` | `gemini-3.1-flash-lite-preview` | `ti2025ars__table__p7` | Answer matches `TXN`, but path skipped `parse_table` |

Interpretation: H3 behaves correctly. It keeps supported trajectories and catches the two questionable trajectories.

## H3 Negative-Control

| Metric | Result |
|---|---:|
| Negative count | 214 |
| Caught bad count | 214 |
| Caught bad rate | 100% |
| Missed keep count | 0 |
| Missed keep rate | 0% |
| Reject decisions | 190 |
| Review decisions | 24 |

Failure taxonomy:

| Failure Type | Count |
|---|---:|
| `missing_evidence` | 95 |
| `answer_mismatch` | 54 |
| `insufficient_negative_evidence` | 24 |
| `verification_label_mismatch` | 12 |
| `numeric_mismatch` | 17 |
| `table_value_mismatch` | 12 |

Interpretation: H3 negative-control passes. No corrupted trajectory is incorrectly kept.

## H4 Diversity

| Metric | Result |
|---|---:|
| Count | 120 |
| H4-lite passed | false |
| Task coverage OK | true |
| Core action coverage OK | true |
| Sequence diversity OK | true |
| Search query diversity OK | false |
| Unique sequence count | 12 |
| Core pilot action coverage | 7 / 7 |
| Covered task types | 6 / 6 |
| Unique search query count | 15 |
| Unique search query ratio | 27.78% |

Top paths:

| Path | Count |
|---|---:|
| `read_page -> answer` | 31 |
| `search -> read_page -> refuse` | 24 |
| `search -> read_page -> answer` | 17 |
| `parse_table -> compute -> answer` | 15 |
| `search -> read_page -> read_page -> answer` | 7 |
| `search -> read_page -> verify -> answer` | 6 |
| `read_page -> parse_table -> answer` | 6 |
| `read_page -> verify -> answer` | 6 |

Interpretation: H4 core evidence is strong: all task types and all core actions are covered, with 12 unique tool sequences. The only failing H4-lite submetric is search-query diversity. This is partly expected because each seed is repeated across three teachers and two runs, so repeated anchor queries lower the unique search-query ratio.

## Overall Decision

V5 improves refusal diversity and adds `gemini-3.1-flash-lite-preview`. The new refuse seeds are successful: all 24 unanswerable rollouts terminate with evidence-based `refuse`.

Strictly, V5 is not a clean full pass because:

- H2 has 1 malformed rollout.
- H3 positive has 1 reject and 1 review.
- H4-lite is false due to search-query diversity.

For pilot validation, V5 still supports the main claims:

- Teacher agents generate non-direct, tool-using trajectories.
- DocVerify++ catches bad or insufficient trajectories.
- The kept trajectory set covers the core tools and task types.

Recommended action before treating V5 as the final report baseline:

- Rerun or exclude the one malformed Gemini 2.5 numeric rollout.
- Keep the Gemini 3.1 table case as a useful H3 review example, or rerun it if the final dataset requires only `keep` trajectories.
- Adjust H4 search-query diversity to be computed at seed level rather than rollout level, or add more search-based seeds if strict H4-lite must pass unchanged.
