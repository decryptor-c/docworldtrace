# DocWorldTrace 数据来源实用指南：外部数据集复用 vs 自有文档建 Q&A

> **核心问题 1**: 能否直接用现成的多模态 QA 数据集？哪些能用、哪些不能用？  
> **核心问题 2**: 自有文档（arXiv/10-K/其他）如何确认 Q&A 的正确性？验证 pipeline 怎么设计？

---

## 1. 现有多模态 QA 数据集的可复用性分析

### 1.1 一句话结论

**MMLongBench-Doc 可以直接用。DocVQA/MP-DocVQA 基本不可用。TATQA/FinQA 部分可用。总体：外部数据集最多贡献 ~30% 的种子（40-60 seeds），主力产量必须靠来源 B（自动派生）和来源 C（LLM 合成）。**

### 1.2 逐数据集分析

#### DocVQA / MP-DocVQA — ❌ 基本不可用

| 维度 | 现状 | 对 DocWorldTrace 的影响 |
|------|------|----------------------|
| **文档来源** | UCSF Industry Documents Library（烟草/制药/化工行业内部文件） | 领域偏窄（非 arXiv/10-K 目标域） |
| **文档格式** | **扫描页面图像**（JPG/PNG），非原始 PDF | **致命问题** — 没有 PDF 就无法运行 DocEnv 的 search/crop/parse_table 工具链 |
| **原始 PDF 可获得性** | 需逐一追溯到 UCSF 库下载，非数据集分发的一部分 | 人工成本极高（6,000 篇文档逐一查找和验证） |
| **OCR 质量** | 扫描件 OCR，含手写、低质打印 | H1 pilot 限定数字化 PDF，扫描件 OCR 质量未经系统验证 |
| **问答格式** | 自然语言问题 + 短答案（span/extractive） | 答案格式可直接作为 reference_answer；但问题不包含工具调用指令 |
| **页码标注** | 有 evidence page 标注 | 可用于 expected_pages 字段 |

**结论**: DocVQA/MP-DocVQA 的页面图像可作为 Phase 2 的"扫描件压力测试"资源，但不适合 Phase 1 pilot 扩展。真正可用的路径是：下载 HuggingFace 上的 QA 文本 + evidence page 标注 → 追溯到 UCSF 库找对应 PDF → 但这需要逐篇人工操作，投入产出比太低。

**替代方案 — 仅取 QA 文本不用原文档**:
也可以把 DocVQA 的 (question, answer, evidence_page) 三元组映射到**我们已有的自有文档**上。例如：取 DocVQA 中一个 table-lookup 问题模板 → 替换为自有文档中的对应表格 → 保持 question 结构、修改具体值。这实际上变成了"模板迁移"而非"数据复用"。

#### MMLongBench-Doc — ✅ 直接可用（最佳外部来源）

| 维度 | 现状 | 对 DocWorldTrace 的影响 |
|------|------|----------------------|
| **文档格式** | **135 篇 PDF**（非扫描件） | ✅ 可直接输入 DocEnv pipeline |
| **文档领域** | 7 个领域（论文、报告、法律、财务等） | 覆盖 arXiv 和金融，且额外涵盖法律/医疗 |
| **PDF 可获取性** | GitHub + HuggingFace 直接可下载 | ✅ 零成本 |
| **问题数量** | 1,082 个 expert-annotated Q&A | 非常适合：筛选文档池中已有的 30-50 篇 → 取其 Q&A |
| **unanswerable 标注** | **20.6% (223 个)** | ✅ 直接可做 unanswerable 种子 |
| **cross-page 标注** | **33.7% (365 个)** | ✅ 直接可做 cross_page 种子 |
| **evidence 标注** | 有 page-level evidence 标注 | ✅ 可填 expected_pages |
| **答案格式** | 短答案 + F1 评估 | 可直接作为 reference_answer |

**具体复用流程**:

```text
Step 1: 下载 MMLongBench-Doc 的 PDF 集合 + Q&A JSON
  git clone https://github.com/mayubo2333/MMLongBench-Doc
  # PDF 位置: data/pdfs/
  # Q&A 位置: data/questions/

Step 2: 筛选与 DocWorldTrace 文档池重叠的 PDF（如果有）
  # 或直接用 MMLongBench-Doc 的 PDF 扩充我们的文档池
  # 135 篇 × 筛选（数字化/英语/页数适合）→ 估计可用 60-80 篇

Step 3: 按 task_type 分类映射每个 Q&A:
  for qa in mmlongbench_questions:
      if qa.answerable == false:
          task_type = "unanswerable"
      elif qa.evidence_pages 跨多页:
          task_type = "cross_page"
      elif 答案来自表格:
          task_type = "table_lookup"
      else:
          task_type = "text_lookup"

      # 改写 question，添加工具调用指令:
      rewritten_q = f"{qa.question} Use the document tools to find the answer.
                     Do not answer from memory."

Step 4: 补充元数据:
      seed = {
          "task_type": mapped_type,
          "question": rewritten_q,
          "reference_answer": qa.answer,
          "source": "MMLongBench-Doc",
          "expected_pages": qa.evidence_pages,
          "required_tools": infer_required_tools(mapped_type, qa),
          "answerable": qa.answerable,
          "doc_id": qa.doc_id
      }
```

**数量估算**: 从 MMLongBench-Doc 中筛选 40-50 个高质量 Q&A → 贡献 **40-50 seeds**（unanswerable: 12-15, cross_page: 12-15, text: 10-12, table: 6-8）

**注意**: MMLongBench-Doc 不包含 numeric_computation 类型的多步计算问题，也不包含需要 verify 动作的 verification 问题。

#### TATQA / FinQA — ⚠️ 部分可用

| 维度 | 现状 | 对 DocWorldTrace 的影响 |
|------|------|----------------------|
| **数据格式** | pre-extracted table markdown + text passages, 非原始 PDF | **核心问题** — TATQA/FinQA 提供的"表格"已经是提取好的文本，没有原始 PDF 页面。DocWorldTrace 需要 PDF 才能走 search→parse_table→compute 工具链 |
| **QA 质量** | 16,552 (TATQA) + 8,000+ (FinQA) 高质量专家标注 | ✅ 数值推理 Q&A 质量很高 |
| **答案格式** | TATQA: 含 evidence/equation/answer/scale；FinQA: 含 derivation program | ✅ 可提供中间计算步骤，适配 compute action 验证 |
| **原始 PDF** | 部分可追溯到 FinTabNet/财务报告公开源 | 需要逐一匹配 PDF，工作量大 |
| **覆盖量** | 如只取有对应 PDF 的样本 | 估计可用 **10-20 seeds**（numeric_computation） |

**具体复用策略**:

```text
方案 A（推荐 — 模板迁移）:
  不自找 PDF。取 TATQA/FinQA 的问题模板和 equation 结构，
  应用到自有 10-K/ARS 文档的对应表格上:
    原始 TATQA: "What was the total revenue in 2019?" (from company X's report)
    迁移到自有: "Based on the table on page P of [our 10-K], what was
                  the total revenue in 2023? Use parse_table to extract the value."
    reference_answer: 从自有文档的 XBRL/手动验证中获得

方案 B（部分直接复用）:
  筛选 TATQA/FinQA 中能追溯到原始 PDF 的样本（如 FinTabNet 中有 PDF 的）
  → 下载对应 PDF → 纳入文档池 → 原始 Q&A 直接作为种子
```

**数量估算**: 方案 A 可贡献 **15-25 numeric seeds**（模板迁移）；方案 B 可贡献 **5-10 seeds**（直接复用）。

### 1.3 外部数据集总可用量

| 数据集 | 可直接复用 | 模板迁移 | 主要贡献类型 |
|------|:---:|:---:|------|
| MMLongBench-Doc | **40-50** | — | text, cross_page, unanswerable, table |
| TATQA/FinQA | 5-10 | 15-25 | numeric_computation |
| DocVQA/MP-DocVQA | ~0 | 可选 | text, table（模板迁移成本高，优先级低） |
| **合计** | **45-60** | **15-25** | 占目标 100-200 seeds 的 **60-85** |

**剩余 40-115 seeds 必须来自来源 B（自动派生）和来源 C（LLM 合成）。**

---

## 2. 自有文档的 Q&A 验证方案

### 2.1 问题分解

对自有文档（arXiv/10-K/政府/医疗），核心挑战是：**如何确认构造的 question 是正确的、answer 是准确的、required_tools 是合理的？**

这与外部数据集的根本区别：外部数据集的 Q&A 是专家标注的（我们信任其质量）；自有文档的 Q&A 是我们自己构造的（需要验证后才能真正用作训练数据）。

### 2.2 按来源分类的验证策略

#### 来源 B（自动派生）— 可全量自动验证

自动派生的核心优势：**question 是从文档中提取的已知事实，answer 直接从文档中提取，因此可以实现 100% 自动验证。**

```text
验证 Pipeline:

INPUT: seed = {question, reference_answer, expected_pages, expected_evidence_bbox, ...}

Step 1 — 答案可追溯性验证 (全量自动):
  对于 table_lookup:
    - 在 seed.expected_pages 上运行 parse_table
    - 检查 seed.reference_answer 是否存在于解析后的表格中
    - 检查对应的 (row, col) 是否匹配

  对于 numeric_computation:
    - 从 parse_table 结果中提取 seed 中引用的数值
    - 重新执行 compute(expr) 验证结果 = seed.reference_answer
    - 允许浮点精度容差 (|computed - reference| < 0.01)

  对于 text_lookup:
    - 在 seed.expected_pages 上运行 read_page
    - 检查 seed.reference_answer 是否出现在 OCR 输出中
    - 使用 fuzzy matching (token overlap ≥80%)

  对于 cross_page:
    - 运行 search(seed.question 中的关键实体)
    - 检查 seed.expected_pages 是否在 top-k 结果中
    - 验证跨页信息的连贯性

Step 2 — 工具链合理性验证 (全量自动):
  - 检查 required_tools 是否组成最小可行工具集
  - 运行对应模板轨迹 (Rule-based) 验证工具链可执行
  - 记录每步的 tool execution status — 任何 failure 标记为需要人工审查

Step 3 — 边界条件验证 (全量自动):
  - seed.question 中的页码是否在文档范围内
  - seed.expected_evidence_bbox 是否在页面尺寸内
  - seed.reference_answer 长度是否合理 (非空、非过长)
  - 对于 answerable=false，检查文档中确实无法找到答案

Step 4 — 人工抽检 (20% 抽样):
  重点审查:
  - cross_page seeds（跨页信息关联可能出错）
  - numeric_computation seeds（计算逻辑可能错误）
  - 任何自动验证中 Step 1 未 100% 通过但偏差小的 seeds
```

**验证脚本伪代码**:

```python
def validate_auto_derived_seed(seed, docenv):
    """对自动派生的 seed 执行全量自动验证"""
    results = {"passed": [], "failed": [], "warnings": []}

    # Step 1: 答案可追溯性
    if seed.task_type == "table_lookup":
        table = docenv.parse_table(seed.expected_pages[0], seed.expected_evidence_bbox[0])
        cell_value = table.get_cell(seed.row_label, seed.col_label)
        if not fuzzy_match(cell_value, seed.reference_answer):
            results["failed"].append(f"table_lookup answer mismatch: "
                                     f"expected '{seed.reference_answer}' got '{cell_value}'")

    elif seed.task_type == "numeric_computation":
        values = extract_values_from_table(docenv, seed)
        computed = eval(seed.compute_expr, values)
        if abs(computed - float(seed.reference_answer)) > 0.01:
            results["failed"].append(f"computation mismatch: "
                                     f"computed {computed} vs reference {seed.reference_answer}")

    elif seed.task_type == "text_lookup":
        ocr_text = docenv.read_page(seed.expected_pages[0])
        if not fuzzy_find(seed.reference_answer, ocr_text, threshold=0.8):
            results["failed"].append(f"text_lookup: answer not found on page")

    elif seed.task_type == "cross_page":
        search_results = docenv.search(extract_key_entity(seed.question))
        if not any(p in seed.expected_pages for p in search_results.pages):
            results["warnings"].append(f"search may not find expected pages")

    # Step 2: 工具链执行验证
    for tool in seed.required_tools:
        result = execute_tool(docenv, tool, seed)
        if result.status == "error":
            results["failed"].append(f"tool {tool} execution failed")

    # Step 3: 边界条件
    for p in seed.expected_pages:
        if p < 1 or p > docenv.total_pages:
            results["failed"].append(f"page {p} out of range [1, {docenv.total_pages}]")

    return results
```

#### 来源 C（LLM 合成）— 必须全量人工审查 + 自动验证

LLM 合成的风险远高于自动派生：LLM 可能编造不存在的表格、虚构数值、或把可答问题标为 unanswerable。

```text
验证 Pipeline:

Step 1 — 答案存在性验证 (全量自动):
  对于 answerable=true 的 seed:
    - 尝试在 seed.expected_pages 上实际找到 seed.reference_answer
    - 如果找不到 → 标记为 "potentially_hallucinated"
    - 如果找到了但位置/上下文不同 → 标记为 "partial_match"

  对于 answerable=false 的 seed:
    - 全量人工审查（最高优先级 — H5 已知薄弱环节）
    - 人工确认: 文档中确实没有答案
    - 人工确认: seed.negative_search_queries 确实查不到
    - 人工确认: max_negative_searches 不会过早截断合法搜索

Step 2 — 问题质量评估 (人工, 100%):
  评估维度:
  - 清晰度 (1-5): question 是否清晰无歧义？
  - 工具必要性 (1-5): 是否确实需要多步工具调用才能回答？
  - 领域合理性 (1-5): 对目标文档来说是否合理的问题？
  - 答案准确性 (0/1): reference_answer 是否正确？
  → 总分 <12/16 的 seed 送回 LLM 重新生成或丢弃

Step 3 — LLM 自我验证 (可选, 低成本):
  用不同的 LLM 模型 (区别于生成用的模型) 做 cross-check:
    Prompt: "Given document page [content], is the answer '{answer}'
             to question '{question}' correct? Answer YES or NO with reason."
    如果 cross-check LLM 说 NO → 强制人工审查
```

#### 来源 A（外部数据集）— 信任原标注 + 适配验证

外部数据集的 Q&A 已经有专家标注，核心验证是**适配质量**而非答案正确性：

```text
验证 Pipeline:

Step 1 — 适配正确性验证 (全量自动):
  - 改写后的 question 是否保留了原 question 的语义？
  - 工具指令是否与 task_type 对齐？
  - required_tools 推断是否正确？

Step 2 — 文档匹配验证 (全量自动):
  - 原数据集中的文档 ID 是否在 DocWorldTrace 文档池中？
  - 原 evidence page 是否在文档范围内？
  - 如果需要，PDF 的页面编号是否与数据集中的页面编号一致？

Step 3 — 人工抽检 (10%):
  仅抽样检查适配质量，不重复验证答案（信任原标注）
```

### 2.3 综合 Q&A 质量保证层级

```text
             ┌──────────────────────────────────┐
             │  全量自动验证 (100% seeds)        │
             │  - 答案存在性 / 可追溯性           │
             │  - 工具链可执行性                  │
             │  - 边界条件 (页码/bboox/格式)      │
             └──────────────┬───────────────────┘
                            │
             ┌──────────────▼───────────────────┐
             │  来源分层人工审查                   │
             │  来源 C (LLM): 100% 人工审查       │
             │  来源 B (自动派生): 20% 人工抽检    │
             │  来源 A (外部数据集): 10% 人工抽检   │
             │  Unanswerable (所有来源): 100% 人工  │
             └──────────────┬───────────────────┘
                            │
             ┌──────────────▼───────────────────┐
             │  Pilot 轨迹验证 (最终确认)         │
             │  对每条通过筛选的 seed，             │
             │  运行 1 次 Teacher Rollout          │
             │  → 如果 Teacher 找不到答案/答案错误， │
             │    说明 seed 本身有质量问题          │
             │  → Teacher 成功率作为最终验证信号     │
             └──────────────────────────────────┘
```

**Teacher Rollout 作为最终 Q&A 验证**: 这实际上是最强的验证方式。如果 GPT-4o 在 DocEnv 中即使使用工具也找不到正确答案，那么要么 seed 有问题，要么任务难度过高。Pilot 中 H2 的 100% adjusted correct 说明：对于质量合格的 seed，强 Teacher 应该能找到答案。

**设定阈值**: 如果某 seed 的 Teacher Rollout 答案正确率 <50%（2+ 次 rollout 中多次失败），该 seed 应标记为"需人工重审"。

### 2.4 具体操作检查清单

**对每一篇自有文档，播种前执行**:

```text
□ 文档质量检查 (Phase A 筛选)
  □ pdfinfo: 页数、是否加密、文件大小
  □ 前三页 OCR 抽查: CER <10%
  □ 表格检测: ≥2 个可解析表格
  □ 文本可提取: pdftotext > 5000 字符

□ 文档 profile 生成
  □ 自动: 页数、表格列表、章节标题列表、关键实体列表
  □ 人工: spot-check 1-2 页验证自动提取的表格/标题是否正确

□ 每个 seed 生成后的验证 (见 §2.2 各来源的验证 Pipeline)

□ 每个 seed 入库前的最终检查
  □ task_type ∈ 合法类型
  □ required_tools 与 task_type 一致性（规则检查）
  □ reference_answer 非空
  □ expected_pages 在文档范围内
  □ answerable=false → max_negative_searches 已设定
  □ negative_search_queries 已提供 (unanswerable)
```

---

## 3. 实际数据构造的推荐路线

### 3.1 Phase 1 推荐优先级

```
Priority 1 (确定性高、成本低):
  ① MMLongBench-Doc 直接复用 → 40-50 seeds
     └─ 1-2 天完成（下载 + 适配 + 验证）
  ② 来源 B 表格/数值自动派生 → 50-70 seeds
     └─ 核心产量, P0 优先级, 脚本开发 2d + 验证 1d

Priority 2 (有价值但需模板迁移):
  ③ TATQA/FinQA 模板迁移 → 15-25 numeric seeds
     └─ 1-2 天（取模板 + 应用到自有文档 + 验证）

Priority 3 (补充覆盖):
  ④ 来源 B 标题/章节派生 → 15-25 seeds (text + cross_page)
  ⑤ 来源 C LLM 合成 → 20-30 seeds (特别是 verification + unanswerable)
     └─ LLM 合成的 verification seeds 填充 MMLongBench 不覆盖的类型
```

### 3.2 快速路线 vs 完整路线

**快速路线 (3-4 天, ~110-140 seeds)**:
- MMLongBench-Doc: 40-50
- 表格/数值自动派生: 50-70
- TATQA 模板迁移: 15-20
- 跳过 LLM 合成（暂不覆盖 verification）；跳过标题/章节派生

**完整路线 (8-10 天, 150-200 seeds)**:
- MMLongBench-Doc: 40-50
- 表格/数值自动派生: 50-70
- TATQA 模板迁移: 15-25
- 标题/章节自动派生: 15-25
- LLM 合成: 20-30
- 全量人工审查 + 分布平衡调整 + 过采样缺口类型

### 3.3 最大风险点和缓解

| 风险 | 概率 | 影响 | 缓解 |
|------|:---:|------|------|
| MMLongBench-Doc 中能用的 PDF 远少于预期（扫描件多/非英语） | 中 | 外部来源种子大幅减少 | 提前下载 20 篇做 spot-check；准备 fallback |
| 自动派生的 table 解析在 10-K 上失败率 >30% | 中 | numeric/table 种子质量堪忧 | 提高 parse_table 前的表格质量阈值；手动验证 Top N 表格 |
| LLM 合成的 unanswerable 假阳性率高（把可答标为不可答） | 高 | 训练数据中拒绝行为被错误激励 | **100% 人工审查 unanswerable** — 不可跳过 |
| 某些任务类型的种子始终达不到目标量 | 中 | 分布偏差过大 | 接受小幅偏差（±3%），在论文中坦诚分布限制 |
