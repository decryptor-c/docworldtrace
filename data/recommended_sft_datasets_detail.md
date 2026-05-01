# DocWorldTrace 候选 SFT 数据集详细说明

> 每个数据集按统一结构展开：来源 / 文档类型 / Query 类型 / Answer 格式 / 映射到 DWT 6 类任务 / 实操注意。

---

## Tier 1 — 主力候选（schema 与 DocWorldTrace 几乎完全兼容）

### 1. MMLongBench-Doc（最高优先级）

**Paper**: Ma et al., NeurIPS 2024 D&B
**规模**: 135 long PDFs / 1,082 questions（不是我之前误报的 13K，实测原版较小但内容稠密）
**许可**: research-only
**HuggingFace**: `yinanhe/MMLongBench-Doc`

#### 文档类型

7 个领域、长度通常 30-200 页：
| 类别 | 占比 | 典型文档 |
|---|---:|---|
| Research paper | ~25% | NeurIPS / NLP 论文（带 figure、table） |
| Tutorial / guidebook | ~20% | 软件手册 / 用户指南 |
| Technical spec / brochure | ~15% | 产品规格书 / 营销资料 |
| Financial report | ~15% | 上市公司年报 / 投资人材料 |
| Government doc | ~10% | 政策报告 / 标准 |
| Academic textbook | ~10% | 教材片段 |
| Other | ~5% | 杂项 |

#### Query 类型（5 个证据源 × 4 个推理类型）

**证据源（evidence sources）**:
1. **Text** — 段落级阅读
2. **Table** — 表格 cell 查找
3. **Chart** — 图表数值读取（柱图/折线/饼图）
4. **Figure** — 示意图 / 流程图理解
5. **Layout** — 跨布局元素推理（页眉、脚注、目录）

**推理类型（reasoning types）**:
- **Single-page (extraction)**: "What is the revenue in 2022?" → 答案在某一页某段
- **Cross-page**: "Compare Section 3.2 results with Table 4 conclusions" → 答案在 ≥2 页
- **Multi-page aggregation**: "How many techniques are mentioned in chapters 4-6?" → 跨多页计数 / 总结
- **Unanswerable**: "What is the company's 2050 revenue forecast?" → 文档不提供，需 refuse

**典型示例**:
```
Q: According to Figure 3 on page 12, which model achieves the highest BLEU score?
A: T5-base
Source: chart  Pages: [12]

Q: How does the safety strategy described in Chapter 5 differ from
   the one in Section 7.2?
A: The Chapter 5 strategy focuses on pre-training filters while
   Section 7.2 emphasizes RLHF fine-tuning.
Source: text  Pages: [54, 79]

Q: What is the paper's reported accuracy on the X-VL benchmark?
A: Not answerable (document does not mention X-VL).
Source: cross-doc  Unanswerable: True
```

#### 映射到 DocWorldTrace 6 类任务

| MMLongBench 标签 | → DWT 任务 | 比例 |
|---|---|---:|
| Single-page text/layout | text_lookup | ~20% |
| Single-page table | table_lookup | ~15% |
| Single-page chart/figure | numeric (待 parse_chart) | ~15% |
| Cross-page text + table | cross_page | ~25% |
| Multi-page aggregation | numeric_computation | ~10% |
| Unanswerable | **unanswerable** | **~15%** ← 最稀缺 |

**Verification 类**：MMLongBench 没有显式 SUPPORTED/UNSUPPORTED 标注，需要把"答案就在某页"和"答案不在文档"的对比当 verification 任务派生。

#### 实操注意

- PDF 完整附带，每篇有 metadata（页数、领域、language）
- 答案有 evidence_pages 标注（list of int）
- Unanswerable 占比 15-20%，**这是你目前 9 条 refuse_generic 之外唯一规模化的拒答源**
- 任务难度高：闭源 SOTA（GPT-4o）准确率仅 ~30-45%，所以 teacher rollout 会有真实失败模式
- 单 PDF 长 → API call 成本相对高（每 rollout 平均 5-10K token）

---

### 2. MP-DocVQA

**Paper**: Tito et al., 2023 (Pattern Recognition)
**规模**: 6,176 documents / 46,176 questions
**许可**: research-only (UCSF Industry Documents Library)
**HuggingFace**: `rubentito/mp-docvqa`

#### 文档类型

**单一来源**：UCSF Industry Documents Library（烟草、食品、化学等行业的内部文档）：
- 法律证词、产品包装、备忘录、研究报告、广告材料
- 平均长度 5-50 页
- **包含 OCR 噪声、扫描件、手写注释、表格、印章** —— 比 arXiv/SEC 更"真实"
- 文档样式：常常是 1980-2000 年代的工业文档（噪声大、字体杂）

#### Query 类型

DocVQA 系列的标准 4 类：
1. **Factoid**: "What is the date of this letter?" → 单 token / 短词答案
2. **Layout-based**: "What is in the top-right corner?" → 需要看页面位置
3. **Table extraction**: "What is the price of item X in column Y?"
4. **Form**: "What is filled in the 'Sender' field?"

**多页扩展**：MP-DocVQA 在 DocVQA 基础上把答案分散到多个页面：
- 答案可能在 page 1, 5, 12 中的任一页
- 模型必须先做 page identification 再做 answer extraction

**典型示例**:
```
Q: What is the title of the experiment described on page 3?
A: "Effects of menthol on smoke perception"
Pages: [3]

Q: How many pages does this document have?
A: 12
Pages: all (layout/global)

Q: What was the recipient's reply on page 5?
A: "Approved with modifications"
Pages: [5]
```

#### 映射到 DocWorldTrace 6 类任务

| 比例 | DWT 任务 |
|---:|---|
| ~50% | text_lookup（factoid extraction） |
| ~20% | table_lookup（form / table cell） |
| ~20% | cross_page（page identification + extraction） |
| ~5% | numeric（少量 counting） |
| ~5% | layout-only |

**没有原生 verification / unanswerable**——需要靠模板派生。

#### 实操注意

- PDF 全部附带，质量参差（很多扫描件，OCR 是必经步骤）
- 答案是 **extractive**（字符串子串），易于 EM/F1 评估
- **训练规模主力**：46K Q 中 ~30K-35K 可作 H2 seed
- 噪声 / 扫描件多 → 是 H1 stress test 真正"难"的素材

---

### 3. DocVQA

**Paper**: Mathew et al., WACV 2021
**规模**: 12,767 single-page documents / 50,000 questions
**许可**: CDLA-Permissive 2.0（最宽松）
**HuggingFace**: `lmms-lab/DocVQA`

#### 文档类型

同样来自 UCSF Industry Documents Library，但 **每条 sample 只有 1 页 PNG**。
- 工业文档：信件、备忘录、报告、规格书、广告
- 包含 typeset、印刷、手写、扫描混合
- 页面尺寸 ~600×800 像素

#### Query 类型

完全是 single-page 的 4 类：
1. **Form-style**: "Who is the sender?" → 单字段值
2. **Table cell**: "What is the value in row X column Y?"
3. **Layout / metadata**: "What is the document date?"
4. **Yes/No**: "Is this document signed?"
5. **Visual**: "What does the logo represent?"

**典型示例**:
```
Q: What is the name written in the 'TO' field?
A: John Smith

Q: How many items are listed in the table?
A: 7

Q: What date is mentioned at the top of the document?
A: October 15, 1998
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~60% | text_lookup |
| ~25% | table_lookup |
| ~10% | numeric（counting） |
| ~5% | yes/no（变种 verification） |

**全部 single-page**——无 cross_page 价值。

#### 实操注意

- 50K Q 是 Tier 1 里规模最大的
- 单页 → teacher rollout 短（平均 2-3 步），成本最低
- 适合**做 text_lookup / table_lookup 的"主体训练量"**，让 SFT 模型在最常见任务上有大规模监督
- 缺点：domain 单一，不能撑起 paper 里的"多领域"叙事

---

### 4. DUDE

**Paper**: Van Landeghem et al., ICDAR 2023
**规模**: 5,019 documents / 41,541 questions
**许可**: research-only
**HuggingFace**: `jordyvl/DUDE_loader`

#### 文档类型

**41 个行业**的真实业务文档（这是它最大优势——领域最多样）：
- 法律合同、专利、医疗记录、保险表单、政府报告、营销手册、技术规格、招聘说明、财务报表、用户手册、培训材料、税务表格、公开记录...
- 平均 5.7 页，最大 200+ 页
- 包含 form / table / paragraph / diagram 混合

#### Query 类型

DUDE 在 DocVQA 基础上 **大幅扩展了答案类型**：
1. **Extractive**: 字符串从原文抽取
2. **Abstractive**: 需要总结 / 改写
3. **List**: 答案是多个 item（["A", "B", "C"]）
4. **Yes/No**: 二元判断
5. **Not-answerable**: 显式标注（这是稀缺资源！）
6. **Multi-step**: 需要 ≥2 步推理（lookup + compute）

**典型示例**:
```
Q: List all the side effects mentioned in this drug label.
A: ["nausea", "headache", "fatigue", "dizziness"]
Type: list

Q: Is this contract still valid?
A: Yes
Type: yes/no

Q: What is the total amount due according to the invoice?
A: $4,532.50
Type: extractive numerical

Q: What is the patient's blood pressure on the third visit?
A: Not answerable (only first two visits documented)
Type: not-answerable

Q: Summarize the patient's recovery progress.
A: The patient showed marked improvement over the 12-week
   rehabilitation, with mobility scores rising from 3 to 8.
Type: abstractive
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~30% | text_lookup（extractive） |
| ~20% | table_lookup |
| ~15% | numeric_computation（含 currency / quantity） |
| ~10% | cross_page（multi-step） |
| ~10% | **unanswerable** |
| ~10% | list-style（可拆为多次 text_lookup 派生） |
| ~5% | yes/no（→ verification） |

#### 实操注意

- **领域多样性**：41 industries，是 paper 里"generalization across domains" 叙事的最佳支撑
- **唯一同时含 list + abstractive + not-answerable** 的大规模数据集
- 答案标注质量高（人工 + 多轮审核）
- PDF 通过 ICDAR 渠道获取，需要注册

---

### 5. TAT-QA

**Paper**: Zhu et al., ACL 2021
**规模**: 2,757 hybrid contexts / 16,552 questions
**许可**: MIT
**HuggingFace**: `next-tat/tat-qa`

#### 文档类型

**真实金融年报片段**（10-K、年度报告）：
- 每个 context 是一段 **混合 table + paragraph** 的内容（约 1 页）
- 表格通常是损益表 / 资产负债表 / 现金流量表片段
- 段落是表格的解释说明文字

#### Query 类型

按 **answer derivation** 分 4 类：
1. **Span (extractive)**: 答案直接从 table/text 抽取
2. **Multi-span**: 答案是多个抽取值组合（["$5M", "$8M"]）
3. **Counting**: 数表中满足条件的行/列数
4. **Arithmetic**: 必须用算术运算符算出（add, subtract, multiply, divide, change_ratio, average...）

**典型示例**:
```
Q: What was the revenue in fiscal 2022?
A: $5,432 million
Type: span

Q: Which segments had revenue above $1 billion?
A: ["Cloud", "Enterprise"]
Type: multi-span

Q: How many products had positive growth in 2022?
A: 4
Type: counting

Q: What was the percentage change in operating income from 2021 to 2022?
A: 14.2%
Derivation: (revenue_2022 - revenue_2021) / revenue_2021
Type: arithmetic
```

每个 arithmetic 题都附带 **derivation expression**（标准化算式），可以直接喂 `compute` 工具：
```json
{
  "answer": "14.2%",
  "scale": "percent",
  "derivation": "(5432 - 4756) / 4756"
}
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~35% | **numeric_computation**（核心） |
| ~30% | table_lookup |
| ~20% | text_lookup（多 span 单字段） |
| ~10% | counting（→ numeric） |
| ~5% | comparison（→ verification） |

#### 实操注意

- **唯一带显式算式的 numeric 数据集** —— 你的 `compute` 工具直接消费
- 给的是 HTML/JSON 表格 + 文本片段，需要拼成 PDF 喂 DocEnv（脚本可写：jinja → wkhtmltopdf）
- 适合解决你 numeric_computation 任务样本不足（pilot 仅 15 条）的问题
- 难度梯度：counting 简单 → multi-step arithmetic 较难，是 PRM 训练好素材

---

### 6. FinQA

**Paper**: Chen et al., EMNLP 2021
**规模**: 8,281 Q / 2,776 financial reports
**许可**: MIT
**HuggingFace**: `dreamerdeo/finqa`

#### 文档类型

**真实上市公司年报片段**（与 TAT-QA 类似但更长、更复杂）：
- 来源：S&P 500 公司 10-K 年报
- 每个 sample 含 1-2 个表格 + 多段文字 + 1 个 derivation question
- 由 11 名 CPA / MBA 标注

#### Query 类型

**全部是 numerical reasoning**，但深度不同：
- 1 步算术: `(a - b)`
- 2-3 步: `((a - b) / b) * 100`
- 4+ 步: 含表格查找 + 跨表 + 跨段 + 多步运算

**最大特色**：每题都有 **gold reasoning program**（程序化的 step-by-step 解题）：
```python
{
  "question": "What was the percentage change in net revenue from 2010 to 2011?",
  "answer": "1.5%",
  "program": "subtract(5829, 5743), divide(#0, 5743)",
  "steps": [
    {"op": "subtract", "args": ["5829", "5743"], "result": "86"},
    {"op": "divide", "args": ["86", "5743"], "result": "0.01497..."}
  ],
  "table_evidence": "Net revenue 5,829 ... 5,743",
  "text_evidence": "..."
}
```

操作符集合：`add / subtract / multiply / divide / exp / greater / table_sum / table_average / table_max / table_min`

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~70% | **numeric_computation**（多步） |
| ~20% | table_lookup（中间步骤） |
| ~10% | cross_page / cross-section（跨表） |

#### 实操注意

- 是 numeric 任务质量最高的资源（专家标注 + step-by-step）
- 可以**直接训 PRM**（中间 program step 是天然 process reward）
- 比 TAT-QA 推理深度更大（平均 2.5 步 vs TAT-QA 1.6 步）
- 没有 unanswerable / verification，纯 numeric

---

## Tier 2 — 需小改造或补工具

### 7. Qasper

**Paper**: Dasigi et al., NAACL 2021
**规模**: 1,585 NLP papers / 5,049 Q
**许可**: CC BY 4.0
**HuggingFace**: `allenai/qasper`

#### 文档类型

**全部是 NLP 学术论文**（来自 Semantic Scholar）：
- 平均 12 页 / 4-6K token
- 含 Abstract / Sections / Tables / Equations / References
- 论文质量高（已发表）

#### Query 类型

5 类（含 unanswerable）：
1. **Extractive**: 从 paper 段落抽取
2. **Abstractive**: 总结 / 转述
3. **Yes/No**: 二元
4. **Unanswerable**: 论文里不存在
5. **Multi-paragraph**: 跨段落综合

**典型示例**:
```
Q: What dataset did the authors use to evaluate their model?
A: WikiText-103
Type: extractive  Evidence: ["Section 4.1, paragraph 2"]

Q: Did the model outperform the baseline on all benchmarks?
A: No
Type: yes/no

Q: What hyperparameter optimization strategy was used?
A: Not in paper
Type: unanswerable

Q: How does the proposed approach differ from prior work in the related work section?
A: It introduces a novel attention mechanism while prior work...
Type: abstractive multi-paragraph
```

每题附带 **evidence paragraph**（标注的支撑段落）。

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~40% | text_lookup（含 cross_page） |
| ~25% | cross_page（multi-paragraph） |
| ~15% | unanswerable |
| ~15% | yes/no → verification |
| ~5% | abstractive |

#### 实操注意

- 学术论文 → 与 arXiv 风格高度一致，与你 pilot 5 篇 arXiv 直接对齐
- 长文档 + cross_page + unanswerable + verification 全覆盖
- PDF 来自 Semantic Scholar，可批量下载
- 5K Q 不算大，但**质量极高**

---

### 8. ChartQA（待 parse_chart 工具上线）

**Paper**: Masry et al., ACL 2022
**规模**: 9,608 Q / 4,804 charts
**许可**: GPL-3.0
**HuggingFace**: `HuggingFaceM4/ChartQA`

#### 文档类型

**单图表 PNG**（不是 PDF）：
- 来源：Statista / OWID / Pew Research / OECD
- 类型：bar (35%), line (30%), pie (15%), grouped/stacked (15%), other (5%)
- 含 axes labels / title / legend / data values

#### Query 类型

2 个 split:
- **Human (H)**: 6K 人工标注问题
- **Machine (M)**: 4K LLM 派生问题

题型：
1. **Data extraction**: "What is the value for X in 2020?"
2. **Comparison**: "Which year had the highest sales?"
3. **Trend**: "Is the trend increasing?"
4. **Computation**: "What is the average of A and B?"

**典型示例**:
```
Q: What is the value of category 'Asia' in 2021?
A: 23.5%
Type: extraction

Q: Which region had the largest decrease from 2018 to 2022?
A: Europe
Type: comparison

Q: What is the sum of values for North America and Africa?
A: 47.3
Type: computation
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~40% | numeric (chart-based) |
| ~30% | table_lookup (chart 数据 ≈ 表) |
| ~20% | comparison → verification |
| ~10% | trend → numeric/text |

#### 实操注意

- 你**目前 DocEnv 没有 `parse_chart`**，这是 Phase 2 才上线
- 单图 → 1 页 PDF 包装即可
- 是 paper 里 visual reasoning 叙事的关键资源
- 不建议 Phase A/B 启用，**等 parse_chart 工具就绪再加**

---

### 9. SlideVQA

**Paper**: Tanaka et al., AAAI 2023
**规模**: 2,619 slide decks / 14,500 Q（部分版本扩到 52K）
**许可**: research-only
**HuggingFace**: `Lakera/slidevqa`

#### 文档类型

**PowerPoint 演示文稿**（已转 PDF）：
- 平均 20 张 slide
- 每张 slide 高度视觉化（标题 + bullets + 图表 + 图片）
- 内容主题：商业培训 / 产品介绍 / 学术演讲

#### Query 类型

3 类：
1. **Single-hop**: 单 slide 内回答
2. **Multi-hop**: 跨 ≥2 张 slide
3. **Numerical**: 含计算

每题有 evidence_slide_ids 标注。

**典型示例**:
```
Q: Which slide shows the Q3 revenue breakdown?
A: Slide 7
Type: single-hop layout

Q: What is the difference between the values in Slide 3 and Slide 12?
A: 25 million
Type: multi-hop numerical
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~40% | text_lookup |
| ~30% | cross_page (跨 slide) |
| ~20% | table_lookup |
| ~10% | numeric |

#### 实操注意

- Slide → PDF 转换简单
- 视觉密集 → 是 multimodal 维度的好补充
- 平均 20 页 → 比 DocVQA 长比 MMLongBench 短，难度适中

---

### 10. TabFact

**Paper**: Chen et al., ICLR 2020
**规模**: 117K claims / 16K Wikipedia tables
**许可**: CC BY-SA 4.0
**HuggingFace**: `ibm/tab_fact`

#### 文档类型

**Wikipedia 表格** + 自然语言 claim：
- 表格平均 14 行 × 5 列
- 主题：体育 / 政治 / 经济 / 历史 / 流行文化

#### Query 类型

**全部是 claim verification**：
- 输入：一句 claim + 一个 table
- 输出：ENTAILED 或 REFUTED
- 包含简单 lookup claim 与复杂 multi-hop reasoning claim

**典型示例**:
```
Table: Olympic medals by country
Claim: "USA won more gold medals than China in 2008."
Label: ENTAILED

Claim: "France ranked above Germany in total medals."
Label: REFUTED
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| 100% | **verification**（你目前最缺！） |

注意：要把 verification 任务的 SUPPORTED/UNSUPPORTED 与 TabFact 的 ENTAILED/REFUTED 对齐。

#### 实操注意

- Table → PDF 包装（HTML 渲染即可）
- **117K 是 verification 任务的最大单一来源**
- 你目前 verification 仅 30 条 rollout（10 seed × 3 teacher），加 TabFact 后能轻松扩到 5K-10K 多样化 verification

---

### 11. HybridQA

**Paper**: Chen et al., EMNLP Findings 2020
**规模**: ~70K Q / Wikipedia
**许可**: MIT
**HuggingFace**: `wenhu/hybrid_qa`

#### 文档类型

每题有 1 个 Wikipedia table + 多个 linked passages（hyperlink 跳转的页面）。

#### Query 类型

**Multi-hop**：必须先在 table 找 anchor，再跳到 passage 找答案（或反向）：
- table-to-text: 表里的实体 → 链接段落里找答案
- text-to-table: 段落里某个值 → 表里查另一列

**典型示例**:
```
Table: List of films directed by Christopher Nolan
Q: In which year was the lead actor of "Inception" born?
Steps:
  1. Table lookup: lead actor of "Inception" = Leonardo DiCaprio
  2. Text passage about Leonardo DiCaprio: born 1974
A: 1974
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~50% | cross_page |
| ~30% | table_lookup |
| ~20% | text_lookup |

#### 实操注意

- 包装成多页 PDF（Table 1 page + linked passages 各 1 page）
- 是 cross_page reasoning 大规模训练的最佳来源

---

### 12. ConvFinQA

**Paper**: Chen et al., EMNLP 2022
**规模**: 3,892 conversations / 14K turns
**许可**: MIT
**HuggingFace**: `nltext/convfinqa`

#### 文档类型

与 FinQA 同源（金融年报 table + text），但每个 context 关联**多轮对话**。

#### Query 类型

**多轮 numerical reasoning**：每一轮都依赖前一轮答案。

**典型示例**:
```
Q1: What was the revenue in 2018?
A1: $4,500M

Q2: How about in 2019?
A2: $5,200M

Q3: What is the growth rate?
A3: 15.6%   (uses values from Q1 & Q2)
```

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~80% | numeric_computation（多步、跨轮） |
| ~20% | table_lookup |

#### 实操注意

- 你目前 pipeline 是单轮，**需要把每个 conversation 拆成 N 个独立 sample**
- 或者扩展 DocEnv 支持 multi-turn state（论文 Phase 2 工作）
- 现阶段建议拆单轮使用

---

### 13. InfographicVQA

**Paper**: Mathew et al., WACV 2022
**规模**: 5,485 infographics / 30,035 Q
**许可**: research-only
**HuggingFace**: `lmms-lab/infographicVQA`

#### 文档类型

**信息图表**（infographic PNG）：
- 高度视觉化、布局复杂、文字与图形混排
- 来源：网络收集 + 人工筛选
- 平均含 5-15 个数据点

#### Query 类型

5 类：
1. Lookup
2. Numerical reasoning
3. Comparison
4. List
5. Visual recognition (color/shape/icon)

#### 映射到 DWT 任务

| 比例 | DWT 任务 |
|---:|---|
| ~40% | text_lookup |
| ~30% | numeric |
| ~15% | table_lookup（嵌入式 table） |
| ~15% | cross_page（跨视觉区域） |

#### 实操注意

- 视觉非常密集 → 对纯 OCR 工具不友好，**需要强 VLM read_page**
- 适合后期做 visual reasoning 维度
- 单图 = 1 页

---

## Tier 3 — PDF 原料库（自派生 seed）

下面这些没有现成 QA，但有大量高质量 PDF。配合你的 `structure_heuristic_v2_review`（自动从表格/标题/句子派生题目）可以无限产出 seed。

### 14. arXiv

- 2.5M+ PDFs
- 学科分布：物理（35%）/ 数学（25%）/ 计算机（20%）/ 生物（10%）/ 统计（5%）/ 其他（5%）
- 每月新增 ~12K
- API: `arxiv.org/list/cs/2024-01`
- 派生方向：text_lookup（heading）、verification（abstract claim）、cross_page（intro vs conclusion）

### 15. SEC EDGAR

- 数百万 filings：10-K（年报）/ 10-Q（季报）/ 8-K（重大事件）/ DEF 14A（代理）/ S-1（IPO）
- 来源：sec.gov
- 派生方向：table_lookup（财务报表）、numeric_computation（YoY 变化）、unanswerable（"未来 N 年预测"）

### 16. PubMed Central OAI

- 4M+ open-access 医学论文
- 含 figure / table / 临床数据
- 派生方向：verification（医学结论）、text_lookup（治疗方案）、numeric（剂量计算）

### 17. Federal Register

- 美国联邦政府每日规章公告
- 高度结构化（rule / proposed rule / notice）
- 派生方向：cross_page（多 section）、verification（合规声明）

### 18. EUR-Lex

- 欧盟法律全文（28 种语言！）
- 数十万文档
- 派生方向：cross_page（条款引用）、verification（条款适用）

### 19. WHO Publications + IPCC

- 全球公共卫生 + 气候科学
- 长文档（100-500 页）
- 派生方向：cross_page、numeric、verification（既有 SOTA 数据集，也可补 unanswerable）

### 20. NASA Tech Reports + GAO + World Bank

- 政府 / 国际组织报告
- 表格 + 图表 + 长文密集
- 类似 IPCC 风格

### 21. CommonCrawl PDFs

- TB 级开放抓取
- 噪声大但量无限
- 适合做 H1 stress test

### 22. Project Gutenberg

- 7 万+ 经典书籍
- 仅作 long-context cross-page 测试，不适合训练（domain 错配）

---

## Tier 4 — Agent trajectory 对照集

### 23. AgentTrek（ICLR 2025）

- 10K+ web GUI trajectories
- 你 related work 已引用
- 用途：cross-domain comparison（GUI vs Doc methodology）

### 24. ToolBench（Qin et al.）

- 16K tool-use trajectories
- 通用 API 工具
- 用途：tool-use baseline 对照

### 25. APIBench / Gorilla

- 16K API 调用样本
- 用途：与 ToolBench 类似

### 26. Mind2Web

- 2K real web tasks
- 真实分布
- 用途：web agent 对照

### 27. AgentInstruct

- 1.8K agent SFT 指令
- 用途：通用 agent SFT 配方

---

## 跨数据集任务覆盖矩阵

| 任务类型 | DocVQA | MP-DocVQA | DUDE | TAT-QA | FinQA | MMLong | Qasper | TabFact | SlideVQA | ChartQA |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| text_lookup | ✓✓ | ✓✓ | ✓✓ | ✓ | — | ✓ | ✓ | — | ✓✓ | — |
| table_lookup | ✓ | ✓ | ✓ | ✓✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| numeric_computation | — | — | ✓ | ✓✓ | ✓✓ | ✓ | — | ✓ | ✓ | ✓ |
| cross_page | — | ✓✓ | ✓ | — | — | ✓✓ | ✓ | — | ✓ | — |
| verification | — | — | ✓ | — | — | — | ✓ | ✓✓ | — | ✓ |
| unanswerable | — | — | ✓ | — | — | ✓✓ | ✓ | — | — | — |

✓✓ = 主力 / 大量；✓ = 可用 / 部分；— = 不覆盖

---

## 给你的实施建议（Phase A → C）

### Phase A: 1 周内启动

**只跑 MMLongBench-Doc**：
- 1,082 Q × 2 teacher × 2 run ≈ 4.3K rollout
- DocVerify++ keep 后预期 3K-3.5K trajectory
- 覆盖：cross_page + unanswerable（pilot 缺口）+ verify
- 成本: ~$200

### Phase B: 2-3 周

**+ DocVQA + MP-DocVQA + TAT-QA + FinQA**：
- DocVQA 50K Q（采样 20K）× 1 teacher（Gemini-Flash）= 20K rollout（占 SFT 主体）
- MP-DocVQA 46K Q（采样 15K）× 1 teacher = 15K rollout（cross_page 主力）
- TAT-QA 16K × 1 teacher = 16K rollout（numeric 主力）
- FinQA 8K × 2 teacher = 16K rollout（高质量 numeric + PRM 数据）
- 总计：~67K rollout，过滤后预期 50K keep
- 成本：~$3K-5K（Gemini Flash 主力）

### Phase C: 5-8 周（投稿规模）

**+ DUDE + Qasper + TabFact + 自派生（arXiv/SEC 1万 PDF）**：
- DUDE 41K（domain 多样性主力）
- Qasper 5K（学术 unanswerable）
- TabFact 100K 采样 30K（verification 主力）
- 自派生 ~30K
- 总计：~150K-200K rollout，过滤后预期 100K-150K keep
- 成本：~$10-25K
- 可投稿 ACL Resource / NeurIPS D&B

---

## 推荐的 1-3-5 部署优先级

如果只能选 **1 个**：MMLongBench-Doc（covers everything, has unanswerable）

如果只能选 **3 个**：MMLongBench-Doc + MP-DocVQA + TAT-QA（cross_page + numeric + unanswerable 全覆盖）

如果选 **5 个**：以上 3 个 + DocVQA（量）+ FinQA（高质量 numeric）

如果选 **10 个**：再加 DUDE（领域）+ TabFact（verification 量）+ Qasper（学术 unanswerable）+ SlideVQA（视觉）+ ChartQA（等 parse_chart）
