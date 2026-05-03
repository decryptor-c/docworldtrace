# DocWorldTrace 数据规模扩展专项计划

> **目标**: 从当前 pilot（5 PDF / 54 seeds / 162 rollouts）扩展到 proposal 目标（40-60 PDF / 100-200 seeds / 2K-5K 候选轨迹 / 1K-3K 过滤后轨迹）  
> **前置条件**: H1-H5 pilot 通过；已确认 DocEnv 工具执行可行、Teacher 轨迹可生成、DocVerify++ 在注入式负例上有效、trajectory SFT 显著优于 answer-only SFT  
> **已知缺陷**: (1) 文档池偏 arXiv+ARS，缺真 10-K/扫描件；(2) unanswerable 场景 trajectory adapter 重复 search 到 budget exhausted；(3) 当前训练集 `keep_all=true`，未使用 DocVerify++ 过滤；(4) table/verification seeds 统计能力不足；(5) 自然分布 GT confusion matrix 未做

---

## 1. 文档池构建方案

### 1.1 文档来源与采集策略

#### 1.1.1 arXiv 科学论文（目标 20-30 篇）

**采集标准**:

| 参数 | 标准 | 理由 |
|------|------|------|
| 子领域 | cs.CL, cs.CV, cs.AI, cs.LG, cs.IR | NLP/CV/AI/ML/IR 领域含丰富表格（实验结果表）、跨页引用（相关工作→方法论→实验）、公式密集 |
| 页数范围 | 8-60 页 | 下限排除短文（<8 页无跨页推理价值）；上限匹配典型会议/期刊论文 |
| 最小表格数 | ≥3 个 | 确保 table_lookup 和 numeric_computation 种子可被派生 |
| 最小图表数 | ≥2 个 | 预留 Phase 2 chart reasoning |
| OCR 质量 | 原生 PDF（非扫描件），文本可提取 | 通过 `pdfinfo` + 前 3 页 OCR CER 检查 |
| 多栏排版 | 至少 30% 含两栏 | 覆盖更多样的 layout 场景 |
| 时间范围 | 2023-2026 | 保证与当前 LLM 训练数据截止期的独立性 |

**与 pilot 3 篇 arXiv 的差异**: pilot 文档以单栏为主、表格结构简单。扩展需主动引入：
- 两栏排版论文（layout 解析更困难，crop bbox 更精确需求）
- 公式密集页面（`read_page` 的 OCR 输出含大量 LaTeX 残留）
- 算法伪代码页面（code-like 文本块，不同于 narrative text）
- 跨页表格（`parse_table` 需要处理跨页表格的连续性）

**采集流程**:

```text
1. arXiv API 搜索:
   GET http://export.arxiv.org/api/query?search_query=cat:cs.CL+AND+submittedDate:[202301010000+TO+202601010000]&start=0&max_results=200
   按子领域轮询，每领域取 50 篇候选

2. 自动预筛选:
   - 下载 PDF → pdfinfo 检查页数 (8 ≤ pages ≤ 60)
   - pdftotext 提取全文 → 检查文本长度 >5000 chars（排除扫描件/空文档）
   - 检测表格环境 (\begin{table} / \begin{tabular}) → 计数
   - 检测 \includegraphics → 计数
   - 检查是否含 \twocolumn / \begin{multicols}

3. 人工终筛:
   - 从候选池随机抽样 40 篇
   - 人工检查: 文档是否含可读表格（非纯图片表格）、是否有多页交叉引用、OCR 质量是否可接受
   - 保留 20-30 篇，按简单/中等/复杂分级
```

#### 1.1.2 SEC/EDGAR 金融年报（目标 15-20 篇）

**关键区分 — 真 10-K vs ARS**:

| 特征 | 真 10-K (Form 10-K) | ARS (Annual Report to Shareholders) |
|------|---------------------|-------------------------------------|
| 法律地位 | SEC 法定备案文件 | 营销文件 |
| 数值密度 | 极高（财务报表、附注、风险因子量化） | 中高（选择性呈现亮点数据） |
| 表格结构 | 标准 GAAP 财务报表（资产负债表/损益表/现金流量表） | 自定义格式 KPI 汇总表 |
| 文本特征 | 法律措辞（Item 1/1A/7/7A/8/9A 等标准结构） | 叙事性、营销语言 |
| 跨页引用 | 大量（正文→财务报表→附注） | 较少 |
| XBRL 可用 | ✓（结构化数据可作为 reference answer ground truth） | ✗ |
| 页数 | 100-300 页 | 80-150 页 |

**pilot 的 ARS 不等于 10-K** — 这是 analysis report 明确指出的缺口。扩展需要真 10-K。

**采集标准**:

| 参数 | 标准 | 理由 |
|------|------|------|
| 行业覆盖 | 科技 (SIC 35-36)、金融 (SIC 60-67)、制造业 (SIC 20-39)、医疗 (SIC 80) | 跨行业保证数值类型和表格结构多样性 |
| 页数范围 | 80-250 页 | 对标真实 10-K 典型长度 |
| 最小表格密度 | ≥15 个可解析表格 | 财务三表 + 附注表 + 管理层讨论与分析中的汇总表 |
| PDF 类型 | 仅数字化 PDF（排除扫描件 10-K） | pilot 阶段限定数字化以保证 parse_table 质量 |
| 时间范围 | FY2022-FY2025 | 近三年数据，数值与当前经济环境相关 |

**具体采集流程**:

```text
1. EDGAR Full-Text Search API:
   https://efts.sec.gov/LATEST/search-index?q=formType:"10-K"+AND+filingDate:[2022-01-01+TO+2025-12-31]
   筛选条件: 数字化 PDF（非 scanned/image-based）

2. 按 SIC 代码分层采样:
   - Technology (SIC 3570-3577): 5 篇 (Apple, Microsoft, NVIDIA 等)
   - Financial (SIC 6021-6282): 4 篇 (JPMorgan, Bank of America 等)
   - Manufacturing (SIC 2000-3990): 3 篇
   - Healthcare (SIC 8000-8099): 3 篇

3. 自动预筛选:
   - 下载 PDF + 对应 XBRL 实例文档（如可用）
   - pdfinfo 检查页数 (80 ≤ pages ≤ 250)
   - 检查文本可提取（pdftotext >20K chars）
   - 使用 TableTransformer 检测表格数 ≥15
   - 检查是否含 "Item 8. Financial Statements" 及标准财务报表标题

4. XBRL 辅助 (可选):
   - 解析 XBRL 实例文档提取结构化财务数据
   - 映射到 PDF 中的对应表格页面/行列
   - 作为 reference answer 的 ground truth

5. 人工终筛:
   - 验证 10-K 标准结构：Part I/II/III/IV 完整性
   - 验证财务报表三表齐全
   - 排除特殊实体（SPAC、pre-revenue biotech、破产重组）
```

**真 10-K 的特殊挑战**:

| 挑战 | 影响 | 缓解 |
|------|------|------|
| 极高数值密度（每页可能含 50+ 数字） | numeric seeds 的 reference answer 更难提取 | 优先使用 XBRL 作为 GT |
| 财务报表附注跨页引用（"See Note 7"） | cross-page 种子需要跟踪多跳引用 | 设计"附注追踪"类 cross-page 模板 |
| FASB/GAAP 术语密度极高 | Teacher 可能不理解特定会计术语 | seed question 中用简单语言替换术语 |
| 非标准表格格式（嵌套表头、合并单元格） | parse_table 结构正确率下降 | 限制为"管理层讨论"中的简单表格 |

#### 1.1.3 其他文档类型（目标 5-10 篇）

**扫描型 PDF（2-3 篇）**:

| 属性 | 要求 |
|------|------|
| 来源 | 学术论文扫描版（1990s-2000s 经典论文）、历史政府文件 |
| 特征 | 无原生文本层，需通过 OCR 引擎提取 |
| OCR 质量 | 使用 surya/paddleocr 双重 OCR 后取更高置信度 |
| 用途 | 压力测试 DocEnv 在非理想 PDF 上的工具执行成功率、验证降级触发器 |

**政府/法律文档（2-3 篇）**:

| 属性 | 要求 |
|------|------|
| 来源 | 美国联邦法规 (CFR)、欧盟 AI Act、FDA 指南文件 |
| 特征 | 层级结构（Part→Subpart→Section→Paragraph）、定义引用、法律措辞 |
| 页数 | 30-100+ 页 |
| 用途 | cross_page（定义追踪）、verification（条款支持性判断）、text_lookup |

**医疗/临床文档（2-3 篇）**:

| 属性 | 要求 |
|------|------|
| 来源 | FDA 药品说明书 (Prescribing Information)、临床试验报告 |
| 特征 | 术语密集、表格+文本混合（剂量表、不良事件表）、数值型指标多 |
| 页数 | 20-50 页 |
| 用途 | table_lookup（剂量表）、numeric_computation（不良事件率计算）、verification（适应症支持性） |

### 1.2 文档质量筛选标准

**入池前自动检查 Pipeline**:

```text
for each pdf in candidate_pool:
    checks = {
        # 基础完整性
        "page_count": (8 <= pdf.pages <= 300),
        "file_size_mb": (0.1 <= pdf.size_mb <= 50),
        "not_encrypted": pdf.is_unlocked(),
        "not_corrupted": pdf.can_open(),

        # 文本可提取性
        "ocr_coverage": text_chars / expected_chars > 0.80,  # 80%+ 文本可提取
        "ocr_quality_cer": sample_ocr_cer(pdf.pages[:3]) < 0.10,  # 前三页 CER <10%

        # 结构化元素
        "table_detected": len(detect_tables(pdf)) >= 2,  # 至少 2 个表格
        "text_blocks_per_page": mean(text_blocks_per_page) >= 3,

        # 拒收条件
        "no_all_image_pages": not all(is_image_only(p) for p in pdf.pages),
        "no_handwritten_dominant": handwritten_ratio < 0.3,
    }
    if all(checks.values()):
        approved_pool.append(pdf)
```

**文档难度分级标准**:

| 级别 | 条件 | pilot 占比 | 扩展目标占比 |
|------|------|:---:|:---:|
| **简单** | 数字化 PDF, ≤30 页, 表格 <5 个, 单栏, 无特殊排版 | 60% | **30-40%** |
| **中等** | 数字化 PDF, 30-100 页, 表格 5-15 个, 可能含两栏或多结构混合 | 40% | **40-50%** |
| **复杂** | 两栏/扫描件/法律文档, >100 页或含手写/特殊符号, 表格嵌套 | 0% | **15-25%** |

**去重策略**:
- 同一公司/第一作者只保留最近的 1 篇（避免同质化）
- 同一 cs.* 子领域不超过 8 篇
- 页数分布确保均匀：每 10 页 bin 至少 3-5 篇文档

### 1.3 文档池多样性指标

扩展后文档池的量化多样性指标：

| 指标 | 最小值 | 目标值 | 测量方式 |
|------|:---:|:---:|------|
| 领域/来源数 | 3 | 4+ | arXiv / SEC / Government / Medical |
| SIC 行业代码数（金融） | 3 | 5+ | 跨科技/金融/制造/医疗 |
| cs.* 子领域数（arXiv） | 3 | 5+ | CL/CV/AI/LG/IR |
| 页数范围 | 8-250 | 8-300 | min/max；要求 20th 和 80th percentile 间距 >100 页 |
| 页数分布均匀度 | — | 每 20 页 bin≥2 篇 | 直方图 bin count |
| 表格密度范围 | 2-50 | 3-80 | per-doc table count distribution |
| 表格密度分布 | — | 至少 6 篇含 ≥15 表 | 用于 table/numeric 种子密集派生 |
| OCR 质量梯度 | — | 至少 3 篇 OCR CER 5-10% | 不同质量梯度的工具鲁棒性测试 |
| 文档结构类型 | 3 | 4+ | 单栏/两栏/法律层级/表格中心 |
| 扫描件/低质 PDF | 0 | 2-3 | 压力测试专用 |

---

## 2. 种子任务（Q/A）设计方案

### 2.1 来源 A — 已有 QA 数据集映射

#### 2.1.1 DocVQA → text_lookup / table_lookup

**映射规则**:

```text
输入: DocVQA 样本 = {image, question, answer, question_id, doc_id}

映射逻辑:
1. 检查 doc_id 是否有对应的 PDF 文件在文档池中
2. 按 question 的答案来源分类:
   - 答案来自纯文本段落 → text_lookup
   - 答案来自表格单元格 → table_lookup
3. Rewrite question:
   原文: "What is the title of the document?"
   改写: "Use read_page to examine page 1. What is the title of the document? Report the exact text."
4. 添加工具指令:
   text_lookup:   添加 "Use search/read_page to find the answer in the document."
   table_lookup:  添加 "Use parse_table on the relevant page to extract the value."
5. 定义 expected_tools:
   text_lookup:   ["read_page"] 或 ["search", "read_page"]
   table_lookup:  ["read_page", "parse_table"]
6. 定义 expected_pages: 从 DocVQA 原标注中提取页码
7. reference_answer 保留 DocVQA 原始答案
```

**改写模板**:

```text
TEXT_LOOKUP_TEMPLATE = """
{document_context}
Question: {question}
Instructions: Use the appropriate document tools (search, read_page) to locate and read the relevant information before answering. Report the exact text from the document.
"""

TABLE_LOOKUP_TEMPLATE = """
{document_context}
Question: {question}
Instructions: Use parse_table on the relevant page to extract the value from the table. Answer with the exact cell content, not from memory.
"""
```

**覆盖量估算**: DocVQA 训练集 ~10K 样本。筛选文档池中有对应 PDF 的样本，按 task_type 分层采样 → 预计贡献 **25-35 seeds**（text: ~15, table: ~10, 其余不可用）。

#### 2.1.2 MP-DocVQA → cross_page

**映射规则**:

```text
MP-DocVQA 样本天然需要多页检索 → 映射为 cross_page 类型

问题改写: 原始 MP-DocVQA 问题是自包含的，一般不需要改写
工具指令: "You may need to search across multiple pages to answer this question.
           Use search to find relevant pages, then read_page to examine them."
expected_tools: ["search", "read_page"]
expected_pages: 从 MP-DocVQA evidence page 标注中提取
```

**覆盖量估算**: 筛选文档池中有 PDF 的样本 → 预计贡献 **12-18 seeds**。

#### 2.1.3 MMLongBench-Doc → unanswerable / cross_page

**Unanswerable 映射（关键 — H5 已暴露薄弱点）**:

```text
MMLongBench-Doc 的 unanswerable 标注直接可用:
  answerable=false, reference_answer="REFUSE"

种子改写（以解决 H5 无限 search 问题）:

CURRENT (导致问题):
  "Is the following claim true? [claim]. First check the document with tools;
   if the document does not provide the answer, refuse."

FIXED V3 TEMPLATE:
  "Is the following claim true? [claim].
   Step 1: Use search with <specific_query> to check if the document mentions it.
   Step 2: If no relevant pages found after 2 different search queries, refuse
           with 'The document does not contain this information.'
   Step 3: If relevant pages are found but don't confirm the claim,
           read them and refuse with specific evidence."

关键改变:
  - max_negative_searches=2（硬约束）
  - 提供 negative_search_queries 示例（教模型如何搜"反证"）
  - refuse 理由必须引用具体已读页面的内容
  - trajectory 模板中显式展示 "search → read → search(变体) → read → refuse" 的终止路径
```

**覆盖量估算**: MMLongBench-Doc 的 unanswerable 子集 + 跨页子集 → 预计贡献 **15-20 seeds**（unanswerable: 8-10, cross_page: 7-10）。

#### 2.1.4 TATQA / FinQA → numeric_computation

**映射规则**:

```text
TATQA/FinQA 样本含表格 + 数值推理 → numeric_computation

种子设计关键:
1. 保留原始表格引用（指定页码）
2. 改写 question 使其需要显式计算:
   原文: "What was the revenue growth?"
   改写: "Based on the table on page P, compute the percentage change in Revenue
           from year A to year B. Use parse_table to extract the values, then
           compute the result. Report as 'X%'."
3. expected_tools: ["parse_table", "compute"]
4. reference_answer 格式: 数值 + 单位 + 计算中间步骤（用于 compute 验证）
```

**覆盖量估算**: 筛选文档池 PDF 对应的 FinQA/TATQA 样本 → 预计贡献 **15-20 seeds**。

**来源 A 总覆盖量**: 70-90 seeds（text: 15-20, table: 10-15, cross: 20-28, numeric: 15-20, unanswerable: 8-10, verification: 2-5）

### 2.2 来源 B — 文档结构自动派生

#### 2.2.1 表格驱动种子（核心产量来源）

**Table Lookup 派生**:

```text
触发条件:
  - 检测到表格 ≥3×3 行列
  - 表头行明确（第一行/第二行为列名）
  - 表格含至少 1 个非数值单元格（行标签）和 1 个数值单元格
  - 无合并单元格（跨行/跨列）

派生逻辑:
  for each qualifying_table in doc:
    # 随机选取 1-2 个行标签
    row_labels = sample(non_numeric_rows, k=min(2, len(non_numeric_rows)))
    # 随机选取 1 个列标签
    col_labels = sample(numeric_columns, k=1)

    for row in row_labels:
      seed = {
        "task_type": "table_lookup",
        "question": f"On page {table.page}, in the table '{table.caption or ''}',
                     what is the value for row '{row}' under column '{col}'?
                     Use parse_table on page {table.page} to extract the exact value.",
        "reference_answer": extract_cell_value(table, row, col),
        "required_tools": ["read_page", "parse_table"],
        "expected_pages": [table.page],
        "expected_evidence_types": ["table"],
        "answerable": true,
        "difficulty": "easy" if table.rows * table.cols <= 20 else "medium",
        "source": "auto_derived_table"
      }
```

**Numeric Computation 派生**:

```text
触发条件:
  - 表格含 ≥2 个数值列 AND ≥2 个数值行
  - 至少能找到一对"同一指标、不同时间段"的值（如 FY2023 vs FY2024 Revenue）

派生逻辑:
  for each table_with_time_series in doc:
    # 识别时间序列对
    for pair in find_value_pairs(table, time_axis):
      seed = {
        "task_type": "numeric_computation",
        "question": f"Based on the table on page {table.page}, compute the
                     percentage change in '{pair.metric}' from {pair.time_a}
                     to {pair.time_b}. Use parse_table to extract the values,
                     then compute the result. Report as '<number>%'.",
        "reference_answer": compute_percent_change(pair.value_a, pair.value_b),
        "required_tools": ["parse_table", "compute"],
        "expected_pages": [table.page],
        "difficulty": "medium",
        "source": "auto_derived_numeric"
      }

    # 额外派生: 差值计算
    seed_diff = {
      "task_type": "numeric_computation",
      "question": f"Based on the table on page {table.page}, compute
                   '{pair.metric_a}' minus '{pair.metric_b}'.
                   Use parse_table then compute.",
      "reference_answer": pair.value_a - pair.value_b,
      "required_tools": ["parse_table", "compute"],
      ...
    }
```

**表格质量标准（用于判断"可问的"表格）**:

```python
def is_queryable_table(table):
    return (
        table.rows >= 3 and table.cols >= 3 and          # 最小尺寸
        table.header_row is not None and                   # 有明确表头
        table.merged_cell_ratio < 0.1 and                  # 合并单元格 <10%
        table.has_row_labels and                           # 有行标签
        table.has_numeric_values and                       # 有数值
        table.bbox is not None                             # 可定位
    )
```

**覆盖量估算**: 按 40 篇 PDF × 平均 8 个可问表格 × 1-2 seeds/表 → 预计贡献 **50-70 seeds**（table: 25-30, numeric: 25-40）

#### 2.2.2 标题/章节驱动种子

**Cross-page 派生**:

```text
触发条件:
  - 检测到目录 (TOC) 或编号章节标题 (如 "1 / 1.1 / 2.3")
  - 章节标题在目录页 (p_toc) 而内容在另一页 (p_content)，且 p_toc ≠ p_content

派生逻辑:
  for each toc_entry in extract_toc(doc):
    if toc_entry.page != toc_entry.content_page:
      seed = {
        "task_type": "cross_page",
        "question": f"According to the table of contents, '{toc_entry.title}'
                     starts on page {toc_entry.content_page}. Use read_page to
                     examine that page and report its first sentence or topic.",
        "expected_pages": [toc_entry.content_page],
        "required_tools": ["read_page"],
        "difficulty": "easy",
        "source": "auto_derived_section"
      }
```

**Text Lookup 派生**:

```text
触发条件:
  - 检测到大标题或粗体文本段落

派生逻辑:
  # 简单版: 指定页码
  seed_text = {
    "task_type": "text_lookup",
    "question": f"On page {p}, what is the heading or leading phrase?
                 Use read_page on page {p} and report exactly.",
    "reference_answer": extract_first_heading(doc, p),
    "required_tools": ["read_page"],
    "expected_pages": [p],
    "difficulty": "easy",
    "source": "auto_derived_heading"
  }
```

**覆盖量估算**: 40 篇 PDF × 3-5 个标题/章节 seed → 预计贡献 **15-25 seeds**（text: 10-15, cross: 5-10）

#### 2.2.3 数值/实体驱动种子

**Verification 派生**:

```text
触发条件:
  - 检测到明确数值陈述（如 "Revenue increased by 15%"）
  - 该陈述对应的数值可从邻近表格中验证

派生逻辑:
  for each factual_claim in extract_numeric_claims(doc):
    # 保持原样: 验证正确的 claim
    seed_supported = {
      "task_type": "verification",
      "question": f"Is the following claim supported by the document:
                   '{factual_claim.text}'? Answer SUPPORTED or UNSUPPORTED.
                   Use verify with evidence from page {factual_claim.page}.",
      "reference_answer": "SUPPORTED",
      "required_tools": ["read_page", "verify"],
      "expected_pages": [factual_claim.page],
      "answerable": true,
      "source": "auto_derived_claim"
    }

    # 微小篡改: 制造 UNSUPPORTED 变体
    perturbed_claim = perturb_numeric(factual_claim)  # "15%" → "18%"
    seed_unsupported = {
      ...,
      "question": f"Is the following claim supported: '{perturbed_claim}'?",
      "reference_answer": "UNSUPPORTED",
      ...
    }
```

**覆盖量估算**: 40 篇 × 2-3 个事实陈述 seed → 预计贡献 **12-18 seeds**（verification: 6-9 supported + 6-9 unsupported）

**来源 B 总覆盖量**: 77-113 seeds（table: 25-30, numeric: 25-40, text: 10-15, cross: 5-10, verification: 12-18）

### 2.3 来源 C — LLM 任务合成

**Prompt 设计（分任务类型）**:

```text
SYSTEM_PROMPT = """
You are a document QA designer. Given a document profile, generate questions
that require multi-step tool use to answer. Each question must require the
agent to use document tools (search, read_page, parse_table, compute, verify)
rather than answering from memory.

For each question, specify:
- task_type: one of {text_lookup, table_lookup, numeric_computation,
  cross_page, verification, unanswerable}
- required_tools: list of tool names
- expected_pages: page numbers where evidence can be found
- reference_answer: the correct answer (or REFUSE for unanswerable)
- difficulty: easy/medium/hard
"""

DOCUMENT_PROFILE_FIELDS = {
    "total_pages": int,
    "domain": str,
    "table_count": int,
    "tables_summary": [{"page": int, "caption": str, "rows": int, "cols": int}],
    "section_headings": [{"title": str, "page": int}],
    "key_entities": [str],  # 公司名/产品名/关键术语
    "num_numeric_claims": int,
    "ocr_quality": "high" | "medium",
    "document_structure": "single_column" | "two_column" | "legal_hierarchy",
    "page_summaries_sample": {page_id: "brief summary of page content"},
}
```

**Unanswerable 种子合成（H5 薄弱环节重点设计）**:

```text
子类型 1 — 文档外事实 (target: 4-6 seeds):
  "What is the CEO's personal mobile phone number?"
  "What is the home address of the first author?"
  → refuse 理由: "The document does not contain personal contact information."

子类型 2 — 未披露预测 (target: 3-4 seeds):
  "What exact revenue does the document forecast for fiscal year 2035?"
  "What is the company's projected market share in 2030?"
  → refuse 理由: "The document only contains historical data, not forward-looking
    projections beyond [stated period]."

子类型 3 — 不当请求 (target: 2-3 seeds):
  "Based on this clinical trial, should I take [drug X] for my condition?"
  "Is it legal to [action] according to this document?"
  → refuse 理由: "This document provides factual information, not personal
    medical/legal advice."

子类型 4 — 跨文档信息 (target: 2-3 seeds):
  "How does this company's revenue compare to its top competitor?"
  → refuse 理由: "The document only contains this company's financial data,
    not competitor comparison."

每种 unanswerable 子类型的关键 trajetory 模板:
{
  "steps": [
    {"thought": "I need to search for [specific_target].", "action": "search(...)"},
    {"thought": "The search results don't mention [target]. Let me try a different query.",
     "action": "search(different_query)"},
    {"thought": "After two searches, the document does not provide [target].
                 I should refuse with evidence-based reason.",
     "action": "refuse('The document does not contain [specific_target]. '
              'Searched for [q1] and [q2], neither returned relevant pages.')"}
  ],
  "max_negative_searches": 2  # 硬约束，防止 H5 无限 search
}
```

**合成种子自动验证 Pipeline**:

```text
for each llm_synthesized_seed:
    # 验证 1: 参考答案确实在文档中/不在文档中
    if seed.answerable:
        # 用 DocEnv search + read_page 实际验证
        evidence = find_evidence_in_doc(seed.question, seed.expected_pages)
        assert evidence.contains(seed.reference_answer), "Answer not verifiable"
    else:
        # 验证文档中确实没有答案
        evidence = exhaustive_search(seed.question, doc)
        assert not evidence.contains_answer(), "Answerable question labeled unanswerable"

    # 验证 2: required_tools 是资源词 task_type 的最小工具集
    assert is_minimal_tool_set(seed.required_tools, seed.task_type)

    # 验证 3: expected_pages 在文档范围内
    assert all(1 <= p <= doc.pages for p in seed.expected_pages)
```

**覆盖量估算**: 40 篇 PDF × 1-2 个 LLM 合成 seed → 预计贡献 **20-30 seeds**（text: 5, numeric: 5, cross: 3, verification: 5-7, unanswerable: 10-14）

**来源 C 总覆盖量**: 20-30 seeds

### 2.4 种子任务元数据 Schema 与质控

**必填元数据字段**:

```json
{
  "task_id": "doc_id__task_type__short_descriptor",  // 如 "ti2025ars__numeric__free_cash_flow_change"
  "doc_id": "unique document identifier",
  "question": "full question text with tool instructions",
  "reference_answer": "correct answer or REFUSE",
  "task_type": "text_lookup|table_lookup|numeric_computation|cross_page|verification|unanswerable",
  "difficulty": "easy|medium|hard",
  "required_tools": ["tool1", "tool2"],
  "acceptable_paths": [["alt_tool1", "alt_tool2"]],  // 等价工具路径
  "source": "seed_qa|auto_derived|llm_synthesized",
  "source_dataset": "DocVQA|MP-DocVQA|MMLongBench|TATQA|FinQA|null",
  "answerable": true|false,
  "expected_pages": [1, 5],
  "expected_evidence_types": ["table", "text"],
  "expected_evidence_bbox": [[x1,y1,x2,y2]],  // 可选，用于 parse_table/crop 验证
  "negative_search_queries": ["q1", "q2"],  // 仅 unanswerable
  "max_negative_searches": 2,  // 仅 unanswerable
  "creation_date": "2026-05-XX",
  "review_status": "pending|approved|rejected"
}
```

**自动质控规则**:

```python
def validate_seed(seed):
    errors = []
    # question
    if not (20 <= len(seed.question) <= 500):
        errors.append("question length out of range")
    # reference_answer
    if seed.answerable and not seed.reference_answer:
        errors.append("missing reference_answer for answerable seed")
    if not seed.answerable and seed.reference_answer != "REFUSE":
        errors.append("unanswerable seed must have reference_answer='REFUSE'")
    # required_tools consistency
    if seed.task_type == "numeric_computation" and "compute" not in seed.required_tools:
        errors.append("numeric_computation requires compute tool")
    if seed.task_type == "table_lookup" and "parse_table" not in seed.required_tools:
        errors.append("table_lookup requires parse_table tool")
    if seed.task_type == "verification" and "verify" not in seed.required_tools:
        errors.append("verification requires verify tool")
    # pages
    if any(p < 1 or p > doc_pages[seed.doc_id] for p in seed.expected_pages):
        errors.append("expected_pages out of document range")
    # unanswerable specific
    if not seed.answerable:
        if seed.max_negative_searches is None:
            errors.append("unanswerable seed must specify max_negative_searches")
        if not seed.negative_search_queries:
            errors.append("unanswerable seed should have negative_search_queries")
    return errors
```

**人工抽检策略**: 按来源分层抽样，整体抽检率 **20%**（100-200 seeds → 抽 20-40 seeds）。重点检查：LLM 合成种子 100% 审查、unanswerable 种子 100% 审查（高失败风险）。

### 2.5 任务分布平衡策略

**从当前偏差到目标分布的调整**:

| 任务类型 | 目标占比 | Pilot 实际 (H2) | Pilot 实际 (H5 diverse) | 调整策略 |
|---------|:---:|:---:|:---:|------|
| text_lookup | 25% | 25% (5/20) | 偏多 (33/144 train) | 来源 A+B 自然提供足够量；**不需要额外过采样** |
| table_lookup | 20% | 10% (2/20) ⚠️ | 偏少 (18/144 train) | **过采样来源 B 表格派生 + 来源 A DocVQA 表格子集** |
| numeric_computation | 20% | 15% (3/20) | 偏少 (12/144 train) | **过采样来源 B 数值派生 + 来源 A FinQA/TATQA** |
| cross_page | 15% | 20% (4/20) | 偏少 (15/144 train) | 来源 A MP-DocVQA + 来源 B 章节派生 |
| verification | 10% | 10% (2/20) ⚠️ | 偏少 (27/427 sample) | **来源 C LLM 合成重点补充，来源 B claim 派生辅助** |
| unanswerable | 10% | 20% (4/20) | 偏多 (39/144 train) | **控制总量**，来源 A MMLongBench + 来源 C LLM 合成 |

**最终 150-seed 分布目标表**（取中位数）:

| 任务类型 | 目标 seeds | easy | medium | hard | 来源 A | 来源 B | 来源 C |
|---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| text_lookup | 38 (25%) | 20 | 15 | 3 | 15 | 18 | 5 |
| table_lookup | 30 (20%) | 12 | 14 | 4 | 10 | 18 | 2 |
| numeric_computation | 30 (20%) | 2 | 18 | 10 | 8 | 20 | 2 |
| cross_page | 22 (15%) | 8 | 10 | 4 | 12 | 8 | 2 |
| verification | 15 (10%) | 3 | 8 | 4 | 2 | 6 | 7 |
| unanswerable | 15 (10%) | 5 | 8 | 2 | 5 | 0 | 10 |
| **合计** | **150** | **50** | **73** | **27** | **52** | **70** | **28** |

**最小值约束**: 每种任务类型 ≥12 seeds（确保统计能力）；每种任务 × 难度组合 ≥2 seeds。

---

## 3. 从种子到轨迹的采样扩展

### 3.1 采样方法选择策略

| 方法 | 扩展阶段角色 | 覆盖种子类型 | 产量目标 | 占比 |
|------|------------|------------|:---:|:---:|
| **Rule-based** | 简单任务的低成本覆盖 | text_lookup (easy), table_lookup (easy) | 300-400 条 | 12-13% |
| **Teacher Rollout** | 核心产量来源 | **全部 6 类任务** | 1,500-3,000 条 | 60-67% |
| **Hard Negative** | DPO/PRM 训练数据 | 从 Teacher 正例中派生 | 300-500 条 | 12-17% |
| **MCTS 消融** | 高价值搜索路径 | cross_page (medium/hard), numeric (hard) | 50-150 条 | 2-5% |
| **合计** | — | — | **2,150-4,050 条** | **100%** |

**Teacher Rollout 细节**:

| 参数 | 值 | 理由 |
|------|-----|------|
| seeds 覆盖 | 全部 100-200 seeds | 不挑拣 |
| rollout/seed | 2-3 次 (×2 Teacher) | = 4-6 条轨迹/seed |
| Teacher 模型 | GPT-4o (75%) + Gemini-2.5-Flash (25%) | GPT-4o 质量优先；Gemini 降成本 |
| 复用 pilot 经验 | system prompt 已稳定（H2 100% 合规） | 沿用 pilot prompt 模板 |
| 预计产出 | 150 seeds × 2.5 avg × 2 teachers × 2 repeats = **~1,500 条** | 若扩展到 200 seeds → ~2,000 条 |
| 每 seed 成本 | GPT-4o ~$0.15, Gemini ~$0.03 | 加权平均 ~$0.09/轨迹 |
| 总 API 成本 | 1,500 条 × $0.09 = **~$135** | 如全用 GPT-4o ≈ $225 |

**Hard Negative 派生比例**:

| 扰动类型 | 占比 | 每 100 正例派生 | 用途 |
|---------|:---:|:---:|------|
| 工具选择错误 | 15% | 15 | DPO tool selection |
| 参数错误 | 10% | 10 | DPO parameter correctness |
| 过早回答 | 15% | 15 | sufficiency training |
| 过度搜索 | 10% | 10 | efficiency training |
| 答案错误 | 20% | 20 | answer verification |
| 证据遗漏 | 15% | 15 | grounding training |
| 虚假拒答 | 15% | 15 | anti-over-refusal |

### 3.2 Unanswerable/Refuse 种子的特殊处理

**问题根因（来自 H5）**:

```text
当前 unanswerable 轨迹结构:
  search(q1) → read_page → search(q2) → read_page → search(q3) → ... → budget exhausted

根因: 训练数据中的 trajectory 没有教模型 "search 2 次找不到了就 refuse"
       — 模型学会了"需要查证"但没有学会"何时停止"

修复方案 (V3):
```

**V3 Unanswerable Seed 设计**:

```json
{
  "task_type": "unanswerable",
  "question": "What is the CEO's personal mobile phone number? First use search
               to check. If the document does not provide it after at most 2
               different search attempts, refuse with a specific reason.",
  "reference_answer": "REFUSE",
  "required_tools": ["search", "read_page", "refuse"],
  "answerable": false,
  "negative_search_queries": [
    "phone number OR mobile OR contact number",
    "CEO contact OR executive contact OR personal phone"
  ],
  "max_negative_searches": 2,
  "acceptable_paths": [
    ["search", "read_page", "search", "read_page", "refuse"],
    ["search", "read_page", "refuse"],
    ["overview", "search", "read_page", "refuse"]
  ],
  "expected_evidence_types": [],
  "trajectory_template": {
    "steps": [
      {"thought": "I need to search for phone number or contact info.",
       "action": "search", "action_input": {"query": "phone number OR mobile OR contact number", "top_k": 5}},
      {"thought": "Let me check these pages for any contact information.",
       "action": "read_page", "action_input": {"page_ids": [results]}},
      {"thought": "These pages don't have a phone number. Let me try a different search.",
       "action": "search", "action_input": {"query": "CEO contact OR executive contact", "top_k": 5}},
      {"thought": "Still no phone number found. After two searches, the document
                   does not provide personal contact information. I will refuse.",
       "action": "refuse", "action_input": {
         "reason": "The document does not contain personal contact information such as phone numbers. Searched for 'phone number OR mobile OR contact number' (found no relevant pages) and 'CEO contact OR executive contact' (found no personal phone numbers)."
       }}
    ]
  }
}
```

**Over-refuse 防御 — "看似不可答但实际可答"的 hard negative**:

```text
构造方式:
  取一条 answerable seed（如 "What is the revenue in FY2023? Answer is $3.2B on page 5"）
  → 改写 question 使其看似 unanswerable:
    "Can you tell me what the company's financial performance was like?
     If the document does not explicitly state revenue figures, refuse."
  → 在 trajectory 中插入 "refuse"
  → 这是一个 WRONG trajectory（模型应该 answer，但被诱导 refuse）
  → 标记为 Negative，用于 anti-over-refusal 训练

数量: 每 5 条 unanswerable 种子构造 1 条 over-refuse 负例
```

### 3.3 DocVerify++ 过滤的规模扩展

**从 80 条 → 2K-5K 条的 Pipeline 适配**:

```text
Stage 1: 批量格式检查 (L1-L2)
  - 纯规则，无 LLM 调用 → 无成本
  - 预计过滤率: <5%（H2 已证明 Teacher 格式合规 100%）

Stage 2: 批量答案检查 (L3)
  - 需调用 DocVerify++ 做 answer matching
  - 每条 ~1-2 秒（字符串匹配 + NLI）
  - 2K 条 → ~1 hour

Stage 3: 批量证据+过程检查 (L4-L5)
  - 需调用 DocVerify++-lite（claim decomposition + evidence retrieval + support judgment）
  - 每条 ~5-10 秒
  - 2K 条 → ~3-6 hours (可并行)
```

**四级分级预期分布**（基于 pilot H3 100% keep + 注入式负例 100% caught 的先验）:

| 等级 | 预期占比 | 预期数量 (from 3K) | 特征 |
|:---:|:---:|:---:|------|
| Gold | 25-30% | 750-900 | L1-L5 全通过，答案正确 + 证据支持 + 无冗余 |
| Silver | 30-35% | 900-1,050 | 答案正确，部分 grounding 细节可能不完整 |
| Bronze | 15-20% | 450-600 | 答案正确但过程有瑕疵（如非最优工具选择） |
| Negative | 20-25% | 600-750 | 答案错误、不当拒答、证据不支持 |

**人工抽检分层策略**（按等级分层，共抽 150-200 条）:

| 等级 | 抽检比例 | 抽检数量 | 重点检查 |
|:---:|:---:|:---:|------|
| Gold | 10% | 75-90 | 验证"全通过"是否有漏检；spot-check 证据支持性 |
| Silver | 15% | 135-160 | 验证 grounding 缺失的类型和程度 |
| Bronze | 20% | 90-120 | 验证"过程瑕疵"的分类边界是否合理 |
| Negative | 25% | 150-190 | **重点审查** — 验证是否为真正错误，防止 false-negative |
| Unanswerable 全量 | 100% | ~50 | 最高风险类型 — H5 已知问题 |

---

## 4. 执行时间线与成本估算

### Phase A: 文档池构建（预计 5-6 天）

| 任务 | 工期 | 人力 | 说明 |
|------|:---:|:---:|------|
| A1: arXiv 论文采集+筛选 | 1d | 0.5 人 | 脚本自动化为主 |
| A2: SEC/EDGAR 10-K 采集+筛选 | 2d | 1 人 | 手动验证 Form 10-K 完整性 |
| A3: 其他类型文档采集 | 1d | 0.5 人 | 手动寻找+下载 |
| A4: 文档质量筛选 Pipeline 运行 | 0.5d | 0.25 人 | 全自动 |
| A5: 人工终筛 + 难度分级 | 1.5d | 1 人 | ~60 篇 × 3-5 min/篇 = 3-5 hours |
| **Phase A 合计** | **5-6d** | **2-2.5 人天** | |

### Phase B: 种子任务生成（预计 6-8 天，三来源可并行）

| 任务 | 工期 | 人力 | API 成本 |
|------|:---:|:---:|:---:|
| B1: 来源 A — 外部数据集映射 | 2d | 1 人 | $0（数据已有） |
| B2: 来源 B — 文档结构自动派生 | 2d | 1 人（脚本开发）+ 0.5d（人工验证） | $0 |
| B3: 来源 C — LLM 任务合成 | 1d | 0.5 人 | ~$10-20（LLM 生成 30-40 个 seed 的 prompt） |
| B4: 种子质控 (自动规则 + 人工抽检) | 1.5d | 1 人 | $0 |
| B5: 分布平衡调整 + 过采样补充 | 1.5d | 0.5 人 | 视缺口而定 |
| **Phase B 合计** | **6-8d** | **4-4.5 人天** | **$10-20** |

### Phase C: 轨迹采样（预计 8-10 天，可部分并行）

| 任务 | 工期 | 人力 | API 成本 |
|------|:---:|:---:|:---:|
| C1: Rule-based 模板轨迹 (300-400 条) | 1d | 0.5 人 | $0（本地执行） |
| C2: Teacher Rollout (1,500-3,000 条) | 5-7d | 0.5 人（监控） | **$135-450**（取决于 Gemini 占比） |
| C3: Hard Negative 派生 (300-500 条) | 1d | 0.5 人 | $0（本地扰动） |
| C4: MCTS 消融 (50-150 条) | 2d | 0.5 人 | **$50-100**（VLM 生成候选 action） |
| **Phase C 合计** | **8-10d** | **7-10 人天** | **$185-550** |

### Phase D: 质量过滤与分级（预计 5-6 天）

| 任务 | 工期 | 人力 | 成本 |
|------|:---:|:---:|:---:|
| D1: 五层自动质检运行 | 1d | 0.25 人 | $0 |
| D2: DocVerify++-lite 批量运行 | 1d | 0.25 人 | ~$20-50（LLM 调用 NLI 部分） |
| D3: 四级分级标注 | 0.5d | 0.25 人 | $0（自动） |
| D4: 人工抽检 (150-300 条) | 4d | 2 人（并行） | **2 人天** |
| D5: 质量报告 + Failure taxonomy 统计 | 1d | 0.5 人 | $0 |
| **Phase D 合计** | **5-6d** | **3-3.5 人天** | **$20-50** |

### Phase E: 数据打包与统计报告（预计 3-4 天）

| 任务 | 工期 | 人力 |
|------|:---:|:---:|
| E1: 三种格式转换 (ReAct/SFT/ADP) | 1d | 0.5 人 |
| E2: 数据集统计报告 | 1d | 0.5 人 |
| E3: README + datacard + 使用示例 | 1.5d | 1 人 |
| E4: 最终数据完整性验证 | 0.5d | 0.5 人 |
| **Phase E 合计** | **3-4d** | **2.5 人天** |

### 总成本汇总

| 类别 | 金额 |
|------|------|
| LLM API (Teacher + LLM 合成 + NLI) | **$215-620** |
| 人工标注/审核 | **~13 人天**（视当地人力成本） |
| 计算资源 (GPU for SFT/MCTS/OCR) | 已有基础设施，边际成本低 |
| **总计（API + 人工）** | **$215-620 + 13 人天** |

### 关键路径

```text
Phase A (文档池 6d)
  → Phase B (种子 8d) [可与 A 最后 2d 并行]
    → Phase C (轨迹 10d) [C2 Teacher Rollout 是瓶颈，5-7d]
      → Phase D (过滤 6d) [D4 人工抽检是瓶颈，需提前准备]
        → Phase E (打包 4d)

总工期: ~5 周 (含并行时间)
关键瓶颈: Teacher Rollout (C2) 和 人工抽检 (D4)
加速策略: Teacher Rollout 多用 Gemini-Flash ($0.02/条) 异步并行;
          人工抽检提前培训标注者
```

---

## 5. 质控指标与防跑偏检查点

### 5.1 各阶段关键质控指标

#### Phase A: 文档池质控

| 指标 | 目标值 | 测量频率 | 不达标处理 |
|------|:---:|:---:|------|
| OCR 文本覆盖率 | ≥85% 的 PDF ≥80% | 每篇入池时 | <80% → 降为"低质 PDF"类别 |
| 表格检测成功率 | ≥90% 的检测表人工确认正确 | 抽样 10 篇 | <80% → 调整 TableTransformer 阈值 |
| 文档类型分布均匀度 | 每类型 ≥3 篇 | 入池完成时 | 不足 → 针对性补充 |
| PDF 完整性 (无加密/损坏) | 100% | 入池时 | 丢弃 + 替换 |
| 难度分级一致率 | 分级与人工判断一致率 ≥85% | 抽样 20% 文档 | 不一致 → 修订分级标准 |

#### Phase B: 种子质控

| 指标 | 目标值 | 测量频率 | 不达标处理 |
|------|:---:|:---:|------|
| 任务分布偏差 | 每类与目标偏差 <10% | 种子生成完成时 | 过采样不足类型 |
| 答案可验证率 | ≥90% 的 answer 可在文档中实际找到 | 全量自动 + 20% 人工抽检 | <90% → 重审来源 A/C 种子 |
| required_tools 一致率 | 100%（规则检查） | 全量自动 | 不一致 → 修正 |
| Unanswerable 种子正确性 | 100% 确认为真正不可答 | 100% 人工审查 | 假 unanswerable → 改写为 answerable |
| 每类最少种子数 | ≥12 | 生成完成时 | <10 → 该类降级为"探索性" |

#### Phase C: 轨迹质控

| 指标 | 目标值 | 测量频率 | 不达标处理 |
|------|:---:|:---:|------|
| Teacher 格式合规率 | ≥95% | 每 100 条抽检 | <85% → 强化 prompt 或换 Teacher |
| 工具执行成功率 | ≥90% | Teacher rollout 中实时监控 | 某工具 <85% → 排查该工具实现 |
| Adjusted 答案正确率 | ≥80% | 全量 | <80% → 审查种子质量或 Teacher 能力 |
| Direct answer 率 | <5% | 全量 | >5% → prompt 强化强制工具使用 |
| Unanswerable 轨迹 budget exhausted 率 | <20% | 全量 unanswerable | >20% → 确认 V3 种子修复生效 |

#### Phase D: 过滤质控

| 指标 | 目标值 | 测量频率 | 不达标处理 |
|------|:---:|:---:|------|
| Gold 比例 | 20-35% | 全量自动 | >40% → 阈值过宽，收紧 L4/L5 标准 |
| Negative 比例 | 15-30% | 全量自动 | <10% → 阈值过严或有系统性训练问题 |
| 人工审核 evidence support precision | ≥80% | 150-300 条抽检 | <75% → DocVerify++ 降为分析工具 |
| Unsupported answer 过滤后下降 | ≥25% | 过滤前/后对比 | <25% → filtering 效果不显著 |

### 5.2 Phase 级别降级触发器

```text
Week 1-2 (Phase A-B):
  ├── 文档池 <30 篇 → 缩小 scale 目标 (V0.1 而非 Proposal)
  ├── 某类种子 <10 → 该类降为探索性，paper 中不 claim 普适性
  └── parse_table 成功率 <70% → 限制为 OCR text + markdown table

Week 3-4 (Phase C):
  ├── Teacher 格式合规 <85% → 暂停, prompt 强化后再试
  ├── 某 Teacher 模型持续低质 → 替换为备选模型
  └── MCTS 成本 >$5/seed → 缩小消融范围 (50 样本)

Week 4-5 (Phase D):
  ├── DocVerify++ precision <75% → 降为分析工具；论文转 Resource-only 叙事
  ├── 人工抽检发现系统性 false-positive → 修复 verifier 规则后重新过滤
  └── Gold 比例 >50% → 重新校准阈值（当前太宽）

Week 5-6 (Phase E):
  └── 最终过滤后轨迹 <800 条 → 论文降为 V0.1 规模叙事
```

---

## 6. 最终交付物清单

| 交付物 | 格式 | 规模 |
|------|------|------|
| DocEnv-lite 完整环境 | Python 包 + Docker | 支持 40-60 PDF |
| DocWorldTrace Dataset | ReAct JSONL + SFT JSONL + ADP JSONL | 1K-3K 过滤后轨迹 |
| 种子任务集 | JSONL (task_id, question, reference, metadata) | 100-200 seeds |
| 质量分析报告 | Markdown + CSV | 五层分布 + 四级分级 + Failure taxonomy |
| 人工抽检报告 | Markdown | confusion matrix, precision/recall per label |
| 数据使用文档 | README + datacard | 含使用示例和许可 |
| 成本报告 | CSV | per-phase API/人工 breakdown |
| Phase 1 论文初稿 | LaTeX | 基于 pilot + 扩展数据 |
