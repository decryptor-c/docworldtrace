# H1-H4 Pilot Experiment Summary

> 汇总时间：2026-04-27  
> 范围：DocWorldTrace pilot H1-H4，不包含 H5 训练收益实验。  
> 结论：H1-H4 当前均通过 pilot 验收标准，可进入 H5/扩大规模阶段。

---

## Overall Conclusion

| Hypothesis | Experiment | Status | Main Evidence |
|---|---|---:|---|
| H1 | DocEnv 工具环境可行性 | PASS | 5 篇 PDF、50 次标准工具调用全部成功 |
| H2 | Teacher 可生成多步工具轨迹 | PASS | 80 条 rollout 格式合规率、正常终止率、调整后答案正确率均为 100% |
| H3 | DocVerify++ 可过滤/保留 supported 轨迹 | PASS | 80/80 轨迹 supported、sufficient、keep |
| H4 | 轨迹具有任务与工具路径多样性 | PASS | 覆盖 6 类任务、7/7 核心工具、10 类工具序列 |

---

## H1: DocEnv 工具环境可行性

### Goal

验证真实 PDF 是否可以被建模为稳定、可复现的交互式文档环境。H1 不调用大模型，重点验证工具本身：

```text
overview / search / read_page / crop / ocr / parse_table / compute / verify / detect_layout
```

### Data

使用 5 篇 PDF：

| Document | Pages | Words | Table Pages | Type |
|---|---:|---:|---:|---|
| `2308.06595v4` | 28 | 5,816 | 6 | arXiv |
| `2310.03302v2` | 39 | 11,644 | 5 | arXiv |
| `2503.00808v4` | 24 | 7,160 | 8 | arXiv |
| `ti2025ars` | 140 | 62,127 | 66 | annual report |
| `tm2529296d2_ars` | 98 | 39,995 | 49 | annual report |

Raw data quality screening:

| Metric | Result |
|---|---:|
| Document count | 5 |
| High quality | 4 |
| Medium quality | 1 |
| Low quality | 0 |

### Method

每篇文档执行 10 个标准工具调用：

```text
overview_doc
search_primary_page
search_primary_page_cached
read_primary_page
crop_evidence_region
ocr_evidence_region
parse_table_primary_table
compute_sanity_check
verify_supported_claim
detect_layout_primary_page
```

同时检查：

```text
status success
expected text/table/numeric output
retrieval target page
cache hit
support label
```

### Result

| Metric | Result |
|---|---:|
| Total standard calls | 50 |
| Successful calls | 50 |
| Tool success rate | 100% |
| Expectation checks | 105 / 105 |
| Expectation pass rate | 100% |
| Retrieval checks | 10 / 10 |
| Retrieval pass rate | 100% |
| Cache checks | 5 / 5 |
| Cache pass rate | 100% |

Per-document reports:

| Document | Calls | Success Rate | Expectation Rate | Retrieval Rate | Cache Rate |
|---|---:|---:|---:|---:|---:|
| `2308.06595v4` | 10 | 100% | 100% | 100% | 100% |
| `2310.03302v2` | 10 | 100% | 100% | 100% | 100% |
| `2503.00808v4` | 10 | 100% | 100% | 100% | 100% |
| `ti2025ars` | 10 | 100% | 100% | 100% | 100% |
| `tm2529296d2_ars` | 10 | 100% | 100% | 100% | 100% |

### Manual Review

人工核验对象包括：

```text
整页渲染图
crop 局部图
OCR 输出文本
parse_table 输出表格
```

展示图：

```text
data/reports/h1_manual_review/contact_sheet.png
```

![H1 manual review contact sheet](data/reports/h1_manual_review/contact_sheet.png)

### H1 Decision

H1 通过。DocEnv 在 5 篇真实 PDF 上能够稳定执行核心工具调用，支持进入 H2。

---

## H2: Teacher 多步轨迹生成可行性

### Goal

验证强模型 teacher 是否能在 DocEnv 中按照工具协议逐步解决文档问题，而不是直接 answer-only。

H2 的核心输出是 ReAct-style trajectory：

```text
question -> tool call -> observation -> next tool call -> ... -> answer/refuse
```

### Data

使用 20 个 H2 seed，覆盖 6 类任务：

| Task Type | Rollout Count |
|---|---:|
| text_lookup | 20 |
| cross_page | 16 |
| unanswerable | 16 |
| numeric_computation | 12 |
| table_lookup | 8 |
| verification | 8 |

Teacher models:

```text
gpt-4o-2024-11-20
gemini-2.5-flash
```

Rollout 设置：

```text
20 seeds × 2 teachers × 2 repeats = 80 trajectories
```

### Method

每条轨迹给 teacher 提供：

```text
tool API specification
ReAct JSON action protocol
task metadata
document overview
task-specific hints
```

DocEnv 执行每一步工具调用，teacher 只能基于真实 observation 继续下一步。

终止动作：

```text
answer
refuse
```

非终止工具：

```text
search / read_page / crop / ocr / parse_table / compute / verify
```

### Result: Answer and Format Metrics

| Metric | Result |
|---|---:|
| Count | 80 |
| Format compliance rate | 100% |
| Proper termination rate | 100% |
| Strict answer correct rate | 81.25% |
| Adjusted answer correct rate | 100% |
| Mean answer F1 | 84.25% |
| Average steps | 2.925 |
| Verify usage rate | 10% |
| Refuse usage rate | 20% |
| Direct answer rate | 0% |

By teacher:

| Teacher | Count | Format | Proper Termination | Adjusted Correct | Direct Answer |
|---|---:|---:|---:|---:|---:|
| `dmxapi_gemini_2_5_flash` | 40 | 100% | 100% | 100% | 0% |
| `dmxapi_gpt4o_2024_11_20` | 40 | 100% | 100% | 100% | 0% |

By task type:

| Task Type | Count | Adjusted Correct | Avg Steps |
|---|---:|---:|---:|
| cross_page | 16 | 100% | 3.5 |
| unanswerable | 16 | 100% | 3.0625 |
| text_lookup | 20 | 100% | 2.0 |
| verification | 8 | 100% | 3.375 |
| numeric_computation | 12 | 100% | 3.1667 |
| table_lookup | 8 | 100% | 3.0 |

The strict answer correct rate is lower than adjusted correctness because exact/F1 matching under-counts semantically correct table/cross-page/text answers. The adjusted evaluator and DocVerify++ results resolve this mismatch.

### Result: Path Review

| Metric | Result |
|---|---:|
| Evidence path OK rate | 100% |
| Acceptable path OK rate | 100% |
| Proper termination rate | 100% |
| Expected terminal rate | 100% |
| Non-terminal tool use rate | 100% |
| Successful evidence observation rate | 100% |
| Strict path OK rate | 81.25% |

Strict path failures are all `missing_required_tool` under a narrow required-tool definition. They are not evidence failures: all trajectories satisfy acceptable path and evidence observation checks.

### Concrete H2 Trajectory Examples

Annotated visual examples:

![H2-H4 annotated examples](data/reports/h2_h4_annotated_examples/h2_h4_annotated_examples.png)

| Task | Query Summary | Tool Path | Final Output | Why It Matters |
|---|---|---|---|---|
| Cross-page | Find the page about `"visit bench a benchmark for vision"`, then inspect the following page. | `search -> read_page -> answer` | `1 Introduction` | Shows that the agent uses search to locate an anchor page and then reads the target page before answering. |
| Numeric computation | Compute the percentage-point increase in free cash flow margin from 2024 to 2025. | `read_page -> crop -> compute -> answer` | `7 percentage points` | Shows that the agent can inspect a table region and delegate arithmetic to `compute` instead of doing unsupported mental math. |
| Unanswerable/refusal | Ask for a private mobile phone number not provided by the document. | `search -> read_page -> refuse` | Refuses with evidence-based reason | Shows that `refuse` is not direct refusal; the agent first searches and reads candidate pages. |
| Verification | Check whether `"10 2 frozen executive death benefit plan as amended incorporated"` is supported. | `read_page -> verify -> answer` | `SUPPORTED` | Shows explicit use of `verify` before final claim-support answer. |

Example detailed traces:

```text
Cross-page example:
query: Use search to find the page about "visit bench a benchmark for vision".
path: search("visit bench a benchmark for vision") -> read_page([2]) -> answer("1 Introduction")
evidence: page 2 summary = "1 Introduction"

Numeric example:
query: compute free cash flow margin increase from 2024 to 2025
path: read_page([29]) -> crop(page=29, bbox=[48.96, 365.70001, 561.96002, 493.95001]) -> compute(16.6 - 9.6) -> answer
result: 7 percentage points

Refusal example:
query: private mobile phone number of the first author or CEO
path: search("phone number OR contact OR mobile number") -> read_page([9, 16, 19]) -> refuse
result: document does not provide private contact information

Verification example:
query: is the claim supported?
path: read_page([81]) -> verify(claim, evidence_refs=[{"page": 81}]) -> answer("SUPPORTED")
verify result: SUPPORTED / SUFFICIENT
```

### H2 Decision

H2 通过。Teacher 能稳定生成格式合规、非直接回答、证据可追踪的多步工具轨迹。

---

## H3: DocVerify++ 轨迹验证过滤

### Goal

验证 DocVerify++ 是否可以判断 H2 轨迹的最终答案是否被文档证据支持、证据是否充分，以及轨迹是否应进入训练数据。

### Method

对 H2 的 80 条轨迹运行 DocVerify++：

```text
final answer/refuse
evidence refs
tool observations
claim support
sufficiency
filter decision
```

### Result

| Metric | Result |
|---|---:|
| Count | 80 |
| Support rate | 100% |
| Sufficiency rate | 100% |
| Keep rate | 100% |
| Review rate | 0% |
| Reject rate | 0% |
| Adjusted answer correct rate | 100% |
| Mean quality score | 0.9933 |

Support labels:

| Label | Count |
|---|---:|
| SUPPORTED | 80 |

Sufficiency labels:

| Label | Count |
|---|---:|
| SUFFICIENT | 80 |

Filter decisions:

| Decision | Count |
|---|---:|
| keep | 80 |

Failure taxonomy:

| Failure Type | Count |
|---|---:|
| none | 80 |

By teacher:

| Teacher | Count | Support | Sufficiency | Keep |
|---|---:|---:|---:|---:|
| `dmxapi_gemini_2_5_flash` | 40 | 100% | 100% | 100% |
| `dmxapi_gpt4o_2024_11_20` | 40 | 100% | 100% | 100% |

### Concrete H3 Verification Examples

| Seed | Claim Checked by DocVerify++ | Evidence Used | Support | Sufficiency | Decision |
|---|---|---|---|---|---|
| `2308.06595v4__cross__p1_p2` | `1 Introduction` | search snippets + page 2 read_page evidence | SUPPORTED | SUFFICIENT | keep |
| `ti2025ars__numeric_free_cash_flow_margin_change_p29` | computed answer is `7.0 percentage points` | page 29 table/crop evidence + compute result | SUPPORTED | SUFFICIENT | keep |
| `2310.03302v2__refuse__generic` | requested private phone number is not provided by the document | negative search/read evidence | SUPPORTED | SUFFICIENT | keep |
| `tm2529296d2_ars__verify__p81` | claim about frozen executive death benefit plan is supported | page 81 evidence + verify result | SUPPORTED | SUFFICIENT | keep |

These examples show that H3 is not only checking final answer strings. It checks whether the trajectory contains enough document-grounded evidence to justify answer, computation, verification, or refusal.

### H3 Negative-Control Experiment

为了验证 DocVerify++ 不是只会保留正例，本轮在 80 条 H2 正常轨迹上构造了负例轨迹。负例不重新调用 teacher model，而是在已有轨迹上注入可控错误，用来测试 verifier 是否能发现 unsupported / insufficient trajectory。

负例构造：

| Negative Type | Count | Meaning |
|---|---:|---|
| `wrong_final_answer` | 64 | 保留工具调用路径，但把最终答案改错 |
| `missing_evidence_observations` | 64 | 删除关键 evidence observation，使答案缺少可审查证据 |
| `false_answer_for_unanswerable` | 16 | 对本应 refuse 的问题强行给出虚假答案 |
| Total | 144 | 由 80 条 H2 正例派生 |

负例验证结果：

| Metric | Result |
|---|---:|
| Negative count | 144 |
| Caught bad count | 144 |
| Caught bad rate | 100% |
| Missed keep count | 0 |
| Missed keep rate | 0% |
| Reject decisions | 128 |
| Review decisions | 16 |

Failure taxonomy:

| Failure Type | Count | Interpretation |
|---|---:|---|
| `missing_evidence` | 64 | 轨迹缺少支撑答案的文档观察 |
| `answer_mismatch` | 36 | 最终答案与 reference 不一致 |
| `insufficient_negative_evidence` | 16 | 拒绝题缺少足够 negative evidence |
| `verification_label_mismatch` | 8 | verify 结论与 expected verification label 不一致 |
| `numeric_mismatch` | 12 | 数值答案错误 |
| `table_value_mismatch` | 8 | 表格证据存在，但最终表格答案错误 |

人工审查输出：

| File | Purpose |
|---|---|
| `data/h3/negative_v4/negative_manual_review.md` | 面向人工阅读的负例审查清单 |
| `data/h3/negative_v4/negative_manual_review.jsonl` | 逐条负例、路径、verifier 判定和错误类型 |
| `data/h3/negative_v4/negative_manual_labels_template.jsonl` | 人工标注模板，可记录 accept/reject/review |
| `data/h3/negative_v4/negative_docverify_review.md` | 完整 DocVerify++ 负例判定报告 |

这次负例测试还暴露并修复了两个 verifier 规则问题：

| Fixed Issue | Why It Matters |
|---|---|
| verify label exact matching | 避免把 `UNSUPPORTED` 当成包含 `SUPPORTED` 的正确标签 |
| table final-answer matching | 避免表格 evidence 中有正确值时，错误 final answer 仍被误判为 supported |

### H3 Decision

H3 通过。正例侧，80/80 条 H2 轨迹被判定为 `SUPPORTED / SUFFICIENT / keep`。负例侧，144/144 条注入错误的轨迹被 `reject` 或 `review` 捕获，没有错误轨迹被误保留为 `keep`。这说明当前 DocVerify++ 同时具备保留有效轨迹和拦截明显坏轨迹的能力。

---

## H4: 轨迹多样性分析

### Goal

验证 H2/H3 保留下来的轨迹是否不是单一模板，而是覆盖不同任务类型、工具组合和推理路径。

### Method

对 80 条 H2 trajectory 统计：

```text
unique action sequence
action coverage
core pilot action coverage
step count distribution
search query diversity
task type × tool path
```

### Result

| Metric | Result |
|---|---:|
| Count | 80 |
| H4-lite passed | true |
| Unique sequence count | 10 |
| Unique sequence ratio | 12.5% |
| Action coverage | 8 / 10 |
| Core pilot action coverage | 7 / 7 |
| Average step count | 2.925 |
| Search calls | 36 |
| Unique search query count | 19 |
| Unique search query ratio | 52.78% |
| Unique seed-query pair ratio | 58.33% |

Covered task types:

```text
cross_page
numeric_computation
table_lookup
text_lookup
unanswerable
verification
```

Covered core actions:

```text
answer
compute
parse_table
read_page
refuse
search
verify
```

Additional action used:

```text
crop
```

Top tool sequences:

| Tool Sequence | Count |
|---|---:|
| `read_page -> answer` | 20 |
| `search -> read_page -> refuse` | 15 |
| `parse_table -> compute -> answer` | 10 |
| `search -> read_page -> answer` | 8 |
| `search -> read_page -> read_page -> answer` | 8 |
| `read_page -> parse_table -> answer` | 8 |
| `read_page -> verify -> answer` | 5 |
| `search -> read_page -> verify -> answer` | 3 |
| `read_page -> crop -> compute -> answer` | 2 |
| `search -> search -> read_page -> refuse` | 1 |

### Concrete H4 Diversity Examples

| Pattern | Example Seed | Typical Path | Covered Capability |
|---|---|---|---|
| Direct page lookup after page target is known | `2308.06595v4__text__p7` | `read_page -> answer` | single-page textual grounding |
| Cross-page retrieval | `2308.06595v4__cross__p1_p2` | `search -> read_page -> answer` | locating relevant pages by search |
| Multi-page follow-up | cross-page seeds | `search -> read_page -> read_page -> answer` | anchor page plus following page inspection |
| Table extraction | `tm2529296d2_ars__table__p2` | `read_page -> parse_table -> answer` | structured table lookup |
| Numeric reasoning | `ti2025ars__numeric_free_cash_flow_margin_change_p29` | `parse_table -> compute -> answer` or `read_page -> crop -> compute -> answer` | table/crop evidence plus arithmetic |
| Verification | `tm2529296d2_ars__verify__p81` | `read_page -> verify -> answer` | claim support checking |
| Evidence-based refusal | `2310.03302v2__refuse__generic` | `search -> read_page -> refuse` | unanswerable detection with negative evidence |

### Interpretation

The raw unique sequence ratio is only 12.5% because each seed is repeated across two teachers and two runs. H4-lite therefore emphasizes task coverage, core action coverage, task-specific path separation, and search query diversity rather than requiring every repeated rollout to have a unique path.

### H4 Decision

H4 通过。当前轨迹覆盖 6 类任务、7 个核心动作和 10 类工具序列，足以作为 pilot-stage process data。

---

## Final H1-H4 Decision

| Experiment | Pass? | Reason |
|---|---:|---|
| H1 | Yes | DocEnv tools execute reliably on real PDFs |
| H2 | Yes | Teacher trajectories are format-correct, evidence-based, and non-direct |
| H3 | Yes | DocVerify++ keeps all supported/sufficient trajectories |
| H4 | Yes | Trajectories cover multiple tasks, tools, and path patterns |

Current pilot supports the core claim that static PDFs can be converted into verified, multi-step document-agent trajectories. The remaining open claim is H5: whether these trajectories improve a student model after SFT compared with answer-only training.

---

## H2-H4 Annotated Example Figures

以下四张图把 H2-H4 中的代表性例子拆开展示。每张图左侧是对应 PDF 页面证据，彩色框标出答案或证据区域；右侧说明问题、标准路径、groundtruth 和 H3/H4 的验证含义。

### Example 1: H2 Cross-page

![H2 cross-page annotated example](data/reports/h2_h4_annotated_examples/example_01_h2_cross_page.png)

### Example 2: H2 Numeric Computation

![H2 numeric annotated example](data/reports/h2_h4_annotated_examples/example_02_h2_numeric.png)

### Example 3: H3 Verification

![H3 verification annotated example](data/reports/h2_h4_annotated_examples/example_03_h3_verification.png)

### Example 4: H4 Table Path Diversity

![H4 table path annotated example](data/reports/h2_h4_annotated_examples/example_04_h4_table_path.png)

---

---

## Appendix: HuggingFace-Style Seed Records

以下为最新标准 seed v5 的可读版。完整 HuggingFace JSONL 文件保存在 `data/h2/seeds/huggingface/pilot_seeds_v5_hf.jsonl`，字段包括 `id`、`question`、`doc_id`、`acceptable_paths`、`ground_truth`、`messages` 等。

### ID 1: `2308.06595v4__cross__p1_p2`

- `doc_id`: `2308.06595v4`
- `task_type`: `cross_page`
- `query`: Use search to find the page about "visit bench a benchmark for vision". Then inspect the following page and report its heading or leading phrase.
- `traj`: `search -> read_page -> answer / search -> read_page -> read_page -> answer`
- `answer`: `1 Introduction`
- `required_tools`: `search, read_page`
- `evidence`: `[{"page": 2}]`

### ID 2: `2308.06595v4__refuse__external_fact`

- `doc_id`: `2308.06595v4`
- `task_type`: `unanswerable`
- `query`: What current physical location today does the document give for the paper's first author? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason.
- `traj`: `search -> read_page -> refuse / overview -> search -> read_page -> refuse`
- `answer`: `REFUSE`
- `required_tools`: `search, read_page, refuse`
- `evidence`: `[]`

### ID 3: `2308.06595v4__text__p7`

- `doc_id`: `2308.06595v4`
- `task_type`: `text_lookup`
- `query`: What is the heading or leading phrase on page 7? Return the page summary or the first visible leading phrase exactly. Do not choose a later figure caption, table caption, or section title unless it is the first visible leading phrase.
- `traj`: `read_page -> answer`
- `answer`: `BLIP2 Caption It is not possible to determine if a`
- `required_tools`: `read_page`
- `evidence`: `[{"page": 7}]`

### ID 4: `2308.06595v4__verify__p4`

- `doc_id`: `2308.06595v4`
- `task_type`: `verification`
- `query`: Is the following claim supported by the document: "2 visit bench areal worldinspiredvlinstruction followingbenchmark"? Answer SUPPORTED or UNSUPPORTED.
- `traj`: `search -> read_page -> verify -> answer / read_page -> verify -> answer`
- `answer`: `SUPPORTED`
- `required_tools`: `search, read_page, verify`
- `evidence`: `[{"page": 4}]`

### ID 5: `2310.03302v2__cross__p1_p2`

- `doc_id`: `2310.03302v2`
- `task_type`: `cross_page`
- `query`: Use search to find the page about "mlagentbench evaluating language agents on". Then inspect the following page and report its heading or leading phrase.
- `traj`: `search -> read_page -> answer / search -> read_page -> read_page -> answer`
- `answer`: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- `required_tools`: `search, read_page`
- `evidence`: `[{"page": 2}]`

### ID 6: `2310.03302v2__refuse__legal_risk`

- `doc_id`: `2310.03302v2`
- `task_type`: `unanswerable`
- `query`: What confidential or non-public legal case number or regulatory investigation ID does the document disclose for the authors or their institution? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason.
- `traj`: `search -> read_page -> refuse / overview -> search -> read_page -> refuse`
- `answer`: `REFUSE`
- `required_tools`: `search, read_page, refuse`
- `evidence`: `[]`

### ID 7: `2310.03302v2__text__p11`

- `doc_id`: `2310.03302v2`
- `task_type`: `text_lookup`
- `query`: What is the heading or leading phrase on page 11? Return the page summary or the first visible leading phrase exactly. Do not choose a later figure caption, table caption, or section title unless it is the first visible leading phrase.
- `traj`: `read_page -> answer`
- `answer`: `MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation`
- `required_tools`: `read_page`
- `evidence`: `[{"page": 11}]`

### ID 8: `2503.00808v4__cross__p1_p2`

- `doc_id`: `2503.00808v4`
- `task_type`: `cross_page`
- `query`: Use search to find the page about "predictive data selection the data that". Then inspect the following page and report its heading or leading phrase.
- `traj`: `search -> read_page -> answer / search -> read_page -> read_page -> answer`
- `answer`: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- `required_tools`: `search, read_page`
- `evidence`: `[{"page": 2}]`

### ID 9: `2503.00808v4__refuse__external_fact`

- `doc_id`: `2503.00808v4`
- `task_type`: `unanswerable`
- `query`: What is the current employer of the paper's first author today, according to the document? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason.
- `traj`: `search -> read_page -> refuse / overview -> search -> read_page -> refuse`
- `answer`: `REFUSE`
- `required_tools`: `search, read_page, refuse`
- `evidence`: `[]`

### ID 10: `2503.00808v4__text__p18`

- `doc_id`: `2503.00808v4`
- `task_type`: `text_lookup`
- `query`: What is the heading or leading phrase on page 18? Return the page summary or the first visible leading phrase exactly. Do not choose a later figure caption, table caption, or section title unless it is the first visible leading phrase.
- `traj`: `read_page -> answer`
- `answer`: `PredictiveDataSelection:TheDataThatPredictsIstheDataThatTeaches`
- `required_tools`: `read_page`
- `evidence`: `[{"page": 18}]`

### ID 11: `ti2025ars__numeric_free_cash_flow_margin_change_p29`

- `doc_id`: `ti2025ars`
- `task_type`: `numeric_computation`
- `query`: Based on the table on page 29, compute the percentage-point increase in "Free cash flow as a percentage of revenue (non-GAAP)" from 2024 to 2025. Report only the final result as "<number> percentage points", not as a percent.
- `traj`: `read_page -> parse_table -> compute -> answer / parse_table -> compute -> answer / read_page -> crop -> compute -> answer / crop -> compute -> answer`
- `answer`: `7.0 percentage points`
- `required_tools`: `read_page, compute`
- `evidence`: `[{"bbox": [48.96, 365.70001, 561.96002, 493.95001], "page": 29}]`

### ID 12: `ti2025ars__refuse__undisclosed_forecast`

- `doc_id`: `ti2025ars`
- `task_type`: `unanswerable`
- `query`: What exact revenue does the document forecast for Texas Instruments in fiscal year 2035? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason.
- `traj`: `search -> read_page -> refuse / overview -> search -> read_page -> refuse`
- `answer`: `REFUSE`
- `required_tools`: `search, read_page, refuse`
- `evidence`: `[]`

### ID 13: `ti2025ars__table__p7`

- `doc_id`: `ti2025ars`
- `task_type`: `table_lookup`
- `query`: On page 7, in the table, what is the value for row "Common Stock, par value $1.00" under column "Trading Symbol(s)"? Use the table evidence on that page; do not answer from memory.
- `traj`: `read_page -> parse_table -> answer / parse_table -> answer`
- `answer`: `TXN`
- `required_tools`: `read_page, parse_table`
- `evidence`: `[{"bbox": [49.5, 335.89999, 562.5, 364.39999], "page": 7}]`

### ID 14: `ti2025ars__text__p42`

- `doc_id`: `ti2025ars`
- `task_type`: `text_lookup`
- `query`: What is the heading or leading phrase on page 42? Return the page summary or the first visible leading phrase exactly. Do not choose a later figure caption, table caption, or section title unless it is the first visible leading phrase.
- `traj`: `read_page -> answer`
- `answer`: `Government incentives`
- `required_tools`: `read_page`
- `evidence`: `[{"page": 42}]`

### ID 15: `tm2529296d2_ars__cross__p1_p2`

- `doc_id`: `tm2529296d2_ars`
- `task_type`: `cross_page`
- `query`: Use search to find the page about "2025 annual report". Then inspect the following page and report its heading or leading phrase.
- `traj`: `search -> read_page -> answer / search -> read_page -> read_page -> answer`
- `answer`: `About Us Shareholder and Media Information`
- `required_tools`: `search, read_page`
- `evidence`: `[{"page": 2}]`

### ID 16: `tm2529296d2_ars__numeric_margin_change_p2`

- `doc_id`: `tm2529296d2_ars`
- `task_type`: `numeric_computation`
- `query`: Based on the table on page 2, for column "High-Touch Solutions N.A.", compute the value in row "Adjusted Operating Margin2" minus the value in row "Reported sales growth". Report only the final result as "<number> percentage points", not as a percent.
- `traj`: `read_page -> parse_table -> compute -> answer / parse_table -> compute -> answer / read_page -> crop -> compute -> answer / crop -> compute -> answer`
- `answer`: `14.8 percentage points`
- `required_tools`: `read_page, parse_table, compute`
- `evidence`: `[{"bbox": [35.94, 333.96, 535.455, 458.28005], "page": 2}]`

### ID 17: `tm2529296d2_ars__numeric_total_growth_gap_p2`

- `doc_id`: `tm2529296d2_ars`
- `task_type`: `numeric_computation`
- `query`: Based on the table on page 2, for column "Total Company1", compute the value in row "Daily, organic constant currency sales growth2" minus the value in row "Reported sales growth". Report only the final result as "<number> percentage points", not as a percent.
- `traj`: `read_page -> parse_table -> compute -> answer / parse_table -> compute -> answer / read_page -> crop -> compute -> answer / crop -> compute -> answer`
- `answer`: `0.4 percentage points`
- `required_tools`: `read_page, parse_table, compute`
- `evidence`: `[{"bbox": [35.94, 333.96, 535.455, 458.28005], "page": 2}]`

### ID 18: `tm2529296d2_ars__table__p2`

- `doc_id`: `tm2529296d2_ars`
- `task_type`: `table_lookup`
- `query`: On page 2, in the table, what is the value for row "Revenue" under column "High-Touch Solutions N.A."? Use the table evidence on that page; do not answer from memory.
- `traj`: `read_page -> parse_table -> answer / parse_table -> answer`
- `answer`: `$14.0B`
- `required_tools`: `read_page, parse_table`
- `evidence`: `[{"bbox": [35.94, 333.96, 535.455, 458.28005], "page": 2}]`

### ID 19: `tm2529296d2_ars__text__p27`

- `doc_id`: `tm2529296d2_ars`
- `task_type`: `text_lookup`
- `query`: What is the heading or leading phrase on page 27? Return the page summary or the first visible leading phrase exactly. Do not choose a later figure caption, table caption, or section title unless it is the first visible leading phrase.
- `traj`: `read_page -> answer`
- `answer`: `Technology Risks`
- `required_tools`: `read_page`
- `evidence`: `[{"page": 27}]`

### ID 20: `tm2529296d2_ars__verify__p81`

- `doc_id`: `tm2529296d2_ars`
- `task_type`: `verification`
- `query`: Is the following claim supported by the document: "10 2 frozen executive death benefit plan as amended incorporated"? Answer SUPPORTED or UNSUPPORTED.
- `traj`: `search -> read_page -> verify -> answer / read_page -> verify -> answer`
- `answer`: `SUPPORTED`
- `required_tools`: `search, read_page, verify`
- `evidence`: `[{"page": 81}]`
