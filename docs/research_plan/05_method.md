# 方法具体内容

> **概述**: DocWorldTrace 方法由四个核心模块组成：DocEnv-lite 环境构建、多源轨迹采样、质量控制与 Reward 设计、统一 Schema 与数据打包。

---

## 模块一: DocEnv-lite 环境构建

### 1.1 设计哲学

从 GUI Agent 环境（WebArena / OSWorld / AndroidWorld）中提炼的四条设计原则：

1. **环境即真实** — 尽可能使用真实工具执行（搜索/OCR/计算），而不是 LLM 模拟
2. **观测即结构化** — 每个 observation 必须包含可审计的 provenance 信息
3. **动作即确定性** — 同样的 action + 参数在同一文档上应返回相同结果
4. **重置即零成本** — PDF 不变 → observation 可缓存 → MCTS / 多次 rollout 零边际成本

### 1.2 环境架构

```text
┌─────────────────────────────────────────────────────────┐
│                     DocEnv Instance                      │
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Page Renderer │  │  OCR Engine  │  │ Layout Parser │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬────────┘  │
│         └─────────────────┼─────────────────┘            │
│                           ▼                              │
│                 ┌──────────────────┐                     │
│                 │ Document Index   │                     │
│                 │ (pages, blocks,  │                     │
│                 │  tables, charts) │                     │
│                 └────────┬─────────┘                     │
│                          ▼                               │
│              ┌───────────────────────┐                   │
│              │   Tool API Layer      │                   │
│              │ search / read_page /  │                   │
│              │ crop / ocr /          │                   │
│              │ parse_table / compute │                   │
│              │ verify / answer       │                   │
│              └───────────┬───────────┘                   │
│                          ▼                               │
│              ┌───────────────────────┐                   │
│              │ Observation Cache     │                   │
│              │ (action → result 映射) │                   │
│              └───────────────────────┘                   │
│                                                          │
│  State: {visited_pages, evidence_memory, search_history, │
│          remaining_budget}                               │
└─────────────────────────────────────────────────────────┘

       ▲ observation    │ action + params
       │                ▼
┌──────────────────────────────┐
│       Agent Policy           │
│  Thought → Action Selection  │
│  → Evidence Update           │
│  → Continue / Answer / Refuse│
└──────────────────────────────┘
```

### 1.3 环境初始化 Pipeline

```text
输入: PDF 文件

Step 1: 页面渲染
  PDF → N 张页面图像 (PNG/JPG, DPI=144/200)

Step 2: OCR + Layout 解析
  每页 → OCR 文本 + 字符 bbox + layout blocks (text/title/table/figure/list)

Step 3: 结构化元素检测
  每页 → 表格候选区域 (bbox + 初步结构)
  每页 → 图表候选区域 (bbox + 类型标签, Phase 2 启用)

Step 4: 检索索引构建
  所有 OCR 文本 → BM25 索引
  (可选) 页面图像 → ColPali/Embedding 索引

Step 5: 工具 API 封装
  将上述组件封装为标准化 tool API

Step 6: Observation 缓存初始化
  空缓存 → 随 rollout 逐步填充
```

### 1.4 状态空间设计

DocEnv 的 Agent 状态描述 Agent 对文档的当前知识，**核心特有组件是 `evidence_memory`**——记录跨步骤积累的证据：

```json
{
  "doc_id": "annual_report_2023.pdf",
  "doc_profile": {
    "total_pages": 42,
    "domain": "financial",
    "table_count": 8,
    "chart_count": 3,
    "ocr_quality": "high"
  },
  "step": 3,
  "visited_pages": [1, 5, 12],
  "evidence_memory": [
    {
      "eid": "e_001",
      "page": 5,
      "bbox": [100, 200, 400, 300],
      "element_type": "table",
      "content": "FY2023 Revenue: $3.2B",
      "source_action": "parse_table",
      "step_added": 2
    }
  ],
  "search_history": [
    {"query": "annual revenue", "results": [5, 12, 28]}
  ],
  "open_claims": ["revenue increased by 15%"],
  "remaining_budget": 7,
  "trajectory_so_far": ["search", "parse_table"]
}
```

### 1.5 动作空间（10-Action，修订版）

基于 [16 篇论文的 action 空间对比分析](./08_action_space_reference.md)，原 9-action 空间调整为 **10-action**（新增 `overview`），按使用频率分为核心层和扩展层。`parse_chart` 暂缓到 Phase 2。

#### 核心 Action（5 个）— 所有轨迹必须使用

| # | Action | 参数 | 返回 Observation | 副作用 | 共识度 |
|---|--------|------|-----------------|--------|:------:|
| 1 | `search(query, top_k)` | 文本查询 + 返回数 | 候选页面列表 + snippet | 更新 search_history | 9/16 |
| 2 | `read_page(page_ids)` | 页码列表（支持批量） | OCR 文本 + 页面图像描述 | 添加到 visited_pages | 11/16 |
| 3 | `crop(page_id, bbox)` | 页码 + 坐标 | 裁剪区域图像 + OCR | — | 5/16 |
| 8 | `answer(text, evidence_refs)` | 答案文本 + 证据引用 | 终止 (成功) | episode 结束 | 16/16 |
| 9 | `refuse(reason)` | 拒答理由 | 终止 (拒答) | episode 结束 | 2/16 (独特) |

#### 扩展 Action（5 个）— 按任务类型选择性使用

| # | Action | 参数 | 返回 Observation | 副作用 | 共识度 |
|---|--------|------|-----------------|--------|:------:|
| 10 | **`overview()`** | 无 | 文档缩略图网格 + 元信息 | — | **新增** |
| 4 | `ocr(page_id, bbox=None)` | 页码 + 可选区域 | 识别文本 + 字符 bbox | — | 2/16 (可选) |
| 5 | `parse_table(page_id, bbox)` | 页码 + 区域 | 结构化表格 (cells + bbox) | 添加到 evidence_memory | 3/16 |
| 6 | `compute(expr, vars)` | 表达式 + 变量 | 计算结果 | 添加到 evidence_memory | 3/16 (必要) |
| 7 | `verify(claim, evidence_refs)` | 待验证 claim + 证据引用 | support/sufficiency 判断 | 添加到 quality_signals | 4/16 (创新) |

#### DocEnv 辅助工具（非 Agent action）

| 工具 | 说明 | 使用场景 |
|------|------|---------|
| `detect_layout(page_id)` | 返回页面布局元素 bbox 列表 | crop 前辅助定位（参照 DocLens LayoutDetect） |

#### 粒度层级

```text
Level 0: overview()      → 文档级概览
Level 1: search(query)   → 页面级检索
Level 2: read_page(ids)  → 页面级内容获取
Level 3: crop(page,bbox) → 区域级裁剪
Level 4: ocr/parse_table → 元素级解析
Level 5: compute/verify  → 推理级操作
```

> 各 action 的设计依据、实现参考和与现有系统的兼容性分析详见 [08_action_space_reference.md](./08_action_space_reference.md)。

### 1.6 Observation 格式标准

每个 observation 必须包含结构化审计字段：

```json
{
  "action": "parse_table",
  "status": "success | partial | failure",
  "result": {
    "content": "...",
    "structured": { "..." }
  },
  "provenance": {
    "page": 5,
    "bbox": [90, 280, 520, 430],
    "element_type": "table"
  },
  "confidence": 0.86,
  "cache_hit": false
}
```

### 1.7 Observation 缓存机制

文档环境的最大优势是**工具输出完全可缓存**：

```text
cache_key = hash(action_name, doc_id, action_params)

缓存规则:
  overview:    ✓ 缓存 (文档元信息不变)
  search:      ✓ 缓存 (同一文档同一 query 结果不变)
  read_page:   ✓ 缓存
  crop:        ✓ 缓存
  ocr:         ✓ 缓存
  parse_table: ✓ 缓存
  verify:      ✓ 缓存 (需含 verifier 版本号)
  compute:     ✗ 不缓存 (表达式可变)
  answer/refuse: ✗ 不缓存 (终止动作)
```

**缓存对 MCTS 的影响**: 假设 10 步深度 × 5 步宽度 MCTS → 理论 50 次 action，文档缓存命中率约 60-80% → 实际只需 10-20 次 unique 工具执行。相比 GUI 环境（每次操作必须真实执行），成本大幅降低。

---

## 模块二: 多源轨迹采样

### 2.1 种子任务准备

三类任务来源：

**来源 A — 已有 QA 数据集种子**:

| 来源 | 特点 | 用途 |
|------|------|------|
| DocVQA (单页) | 简单文本/表格查找 | text lookup / table lookup |
| MP-DocVQA (多页) | 跨页检索 | cross-page reasoning |
| MMLongBench-Doc | 长文档、含 unanswerable | 复杂推理 + 拒答 |
| TATQA / FinQA | 数值计算 | numeric computation |

**来源 B — 文档结构自动派生** (参照 AgentTrek Tutorial Harvesting 思路):

```text
文档结构分析:
  表格 → "What is the value in row X column Y?" (table lookup)
  表格 + 多行 → "Compare X in year A vs year B" (numeric computation)
  跨页标题 → "What does section X on page P discuss?" (cross-page)
```

**来源 C — LLM 任务合成**: 给定文档 profile + 摘要，LLM 生成多类型问题，人工/自动筛选保留。

每个种子任务标注以下元数据：task_id、doc_id、question、reference_answer、task_type、difficulty、required_tools、source、answerable。

### 2.2 任务分布

| 任务类型 | 占比 | 最小工具步数 |
|---|:---:|:---:|
| Text lookup | 25% | 2-3 |
| Table lookup | 20% | 3-4 |
| Numeric computation | 20% | 4-5 |
| Cross-page reasoning | 15% | 4-6 |
| Evidence verification | 10% | 3-4 |
| Unanswerable / Refusal | 10% | 3-5 |

> Pilot 暂不纳入 chart reasoning。`parse_chart` 放入 Phase 2。

### 2.3 四种轨迹采样方法

执行顺序固定为 **Rule/template → Teacher rollout → Hard Negative → 小规模 MCTS 消融**：

#### 方法 A: Rule-based 模板轨迹

为简单任务提供确定性轨迹，建立低成本 baseline coverage：

```text
Text Lookup Template:
  Thought: I need to find information about {query_topic}
  Action: search(query="{query}", top_k=5)
  Observation: {docenv_result}
  Thought: Page {p} seems relevant. Let me read it.
  Action: read_page(page_id={p})
  Observation: {docenv_result}
  Thought: I found the answer: {answer_text}
  Action: answer(text="{answer}", evidence_refs=[...])
```

#### 方法 B: 强模型 Teacher Rollout

参照 AgentTrek Guided Replay，在 DocEnv 中逐步执行：

1. System Prompt 定义工具 API 和 ReAct 格式
2. Teacher 模型 (GPT-4o / Gemini-2.5) 输出 Thought + Action
3. **DocEnv 执行 Action 返回真实 Observation**（非 Teacher 自行生成）
4. Teacher 根据 Observation 决定下一步
5. 直到 answer/refuse 或超出 budget

**成本估算**: 平均 5 步 × 每步 ~2K token → GPT-4o ~$0.10-0.30/轨迹，Gemini-2.5-Flash ~$0.02-0.05/轨迹。1000 条轨迹约 $20-$300。

#### 方法 C: Hard Negative 轨迹扰动

从正确轨迹出发注入可控错误，用于 DPO/PRM 训练：

| 扰动类型 | 方法 | 训练目标 |
|---------|------|---------|
| 工具选择错误 | parse_table → read_page | DPO 工具选择 |
| 参数错误 | 修改 search query / bbox | 参数正确性 |
| 过早回答 | 证据不足时直接 answer | sufficiency |
| 过度搜索 | 插入冗余 search/crop | 效率 |
| 答案错误 | 扰动数值 / 实体 | 答案验证 |
| 证据遗漏 | 删除关键 evidence_ref | grounding |
| 虚假拒答 | 可回答问题标记 refuse | over-refusal |

#### 方法 D: 小规模 MCTS 消融

参照 WebSynthesis World-Model-Guided MCTS，**仅在 50-100 个样本上运行**：

```text
输入: DocEnv + 种子任务
参数: 搜索宽度 w=2-3, 深度 d=6-8, simulations=20-50

for each simulation:
  Selection → Expansion (VLM 生成候选 action) →
  Simulation (DocEnv 执行，缓存命中则免费) →
  Evaluation (evidence_gain 函数) →
  Backpropagation

Evidence Gain:
  α × coverage(evidence_memory, required_evidence)
+ β × answer_proximity(evidence_memory, reference)
+ γ × tool_efficiency(step / max_steps)
```

### 2.4 ReAct 轨迹格式示例

完整的 ReAct JSON 轨迹结构（以数值计算任务为例）：

```json
{
  "doc_id": "annual_report_2023.pdf",
  "task_id": "t_042",
  "question": "What is the year-over-year revenue growth rate?",
  "reference_answer": "14.3%",
  "task_type": "numeric_computation",
  "source_method": "teacher_rollout",
  "trajectory": [
    {
      "step": 1,
      "thought": "I need to find revenue data. Let me search.",
      "action": "search",
      "action_input": {"query": "annual revenue", "top_k": 5},
      "observation": {"status": "success", "result": {"pages": [5, 12, 28]}, "cache_hit": false},
      "evidence_update": null
    },
    {
      "step": 2,
      "thought": "Page 5 has the financial table. Let me parse it.",
      "action": "parse_table",
      "action_input": {"page_id": 5, "bbox": [90, 280, 520, 430]},
      "observation": {
        "status": "success",
        "result": {"markdown": "| Year | Revenue |\n|---|---|\n| 2022 | $2.8B |\n| 2023 | $3.2B |"},
        "provenance": {"page": 5, "bbox": [90, 280, 520, 430], "element_type": "table"}
      },
      "evidence_update": {"eid": "e_001", "content": "FY2022=$2.8B, FY2023=$3.2B", "type": "table"}
    },
    {
      "step": 3,
      "thought": "Calculate YoY growth: (3.2-2.8)/2.8*100",
      "action": "compute",
      "action_input": {"expr": "(3.2 - 2.8) / 2.8 * 100", "vars": {}},
      "observation": {"status": "success", "result": {"value": 14.29}},
      "evidence_update": {"eid": "e_002", "content": "YoY growth=14.29%", "type": "computation"}
    },
    {
      "step": 4,
      "thought": "Verify the claim before answering.",
      "action": "verify",
      "action_input": {"claim": "YoY revenue growth ≈ 14.3%", "evidence_refs": ["e_001", "e_002"]},
      "observation": {"status": "success", "result": {"support_label": "SUPPORTED", "sufficiency": "sufficient"}}
    },
    {
      "step": 5,
      "thought": "Evidence sufficient. Answer now.",
      "action": "answer",
      "action_input": {"text": "≈14.3%", "evidence_refs": ["e_001", "e_002"]},
      "observation": {"status": "terminal"}
    }
  ],
  "quality_signals": {
    "answer_correct": true,
    "evidence_supported": true,
    "grounding_valid": true,
    "sufficiency_verified": true,
    "efficiency_score": 0.9
  }
}
```

### 2.5 SFT Conversation 格式转换

轨迹 JSON 可直接转换为 SFT 对话格式：

```text
[System] You are a document reasoning agent. Use tools: search, read_page, crop, ...

[User] Question: What is the YoY revenue growth rate?
Document: annual_report_2023.pdf (42 pages, financial)

[Assistant] Thought: I need to find revenue data.
Action: search(query="annual revenue", top_k=5)

[System/Tool] Observation: Found pages [5, 12, 28]. Page 5: "financial summary..."

[Assistant] Thought: Page 5 has the table. Let me parse it.
Action: parse_table(page_id=5, bbox=[90,280,520,430])

...（后续步骤类似）
```

---

## 模块三: 质量控制与 Reward 设计

### 3.1 五层质量检查体系

```text
Layer 1: 格式检查 (Format Validation)
  ├── action ∈ 合法工具集合?
  ├── action_input 参数类型和范围正确?
  ├── ReAct 格式完整 (每步都有 Thought→Action→Observation)?
  └── 终止条件合法 (answer 或 refuse 或 budget 耗尽)?

Layer 2: 执行检查 (Execution Validation)
  ├── 所有 observation 来自 DocEnv 真实执行?
  ├── observation.status ≠ "error"?
  └── 缓存一致性

Layer 3: 答案检查 (Answer Validation)
  ├── final_answer 与 reference_answer 匹配? (EM/F1/ANLS)
  ├── unanswerable 问题是否正确 refuse?
  └── refuse 理由是否与 evidence_memory 一致?

Layer 4: 证据检查 (Evidence Validation)
  ├── evidence_refs 中引用的证据是否在 evidence_memory 中?
  ├── evidence bbox 是否在 page 范围内?
  ├── evidence 内容是否与 page OCR 一致?
  └── 数值 evidence 的 compute 结果是否可复算?

Layer 5: 过程检查 (Process Validation)
  ├── 推理步骤是否被证据支持? (DocVerify++-lite)
  ├── 是否有冗余步骤?
  ├── 工具选择是否合理?
  └── 是否在证据充分时及时回答、不足时继续搜索?
```

### 3.2 四级轨迹质量分级

| 等级 | 通过 Layer | 定义 | 用途 | 预计占比 |
|:---:|:---:|------|------|:---:|
| **Gold ★★★** | L1-L5 全通过 | 答案正确 + 全部证据支持 + 无冗余 | SFT 主训练集 | 20-30% |
| **Silver ★★** | L1-L3, L4 部分 | 答案正确, 部分 grounding 缺失 | SFT 补充 | 25-35% |
| **Bronze ★** | L1-L3 通过 | 答案正确但过程有瑕疵 | PRM 对比正例 | 15-25% |
| **Negative ✗** | L3 失败 | 答案错误或不当拒答 | DPO/PRM 负例 | 20-30% |

### 3.3 七维 Reward 信号

| 层级 | 信号 | 取值 | 来源 |
|------|------|------|------|
| Outcome | R_answer | 0/1 或 F1 | 答案 vs 参考答案 |
| Evidence | R_support | 0/0.5/1 | DocVerify++ 证据支持性 |
| Grounding | R_ground | IoU / bbox validity | bbox 验证 |
| Sufficiency | R_suff | 0/1 | 回答时证据是否充分 |
| Efficiency | R_eff | [0,1] | 有效步数 / 总步数 |
| Refusal | R_refuse | 0/1 | 不可回答时是否拒答 |
| Tool | R_tool | 0/1 | 工具选择和参数正确性 |

**综合质量评分**:

```text
Q = w₁ × R_answer + w₂ × R_support + w₃ × R_ground
  + w₄ × R_suff   + w₅ × R_eff     + w₆ × R_refuse

推荐权重 (Pilot):     w₁=0.30, w₂=0.25, w₃=0.15, w₄=0.15, w₅=0.10, w₆=0.05
推荐权重 (含 unanswerable): w₁=0.25, w₂=0.20, w₃=0.15, w₄=0.15, w₅=0.10, w₆=0.15
```

### 3.4 Per-Step Reward (PRM 训练信号)

```text
r_step(i) = evidence_gain(i) + tool_appropriateness(i) - redundancy_penalty(i)

evidence_gain(i):    1.0 有效新证据 / 0.5 部分有用 / 0.0 无增益 / -0.5 误导
tool_appropriateness(i):  1.0 合理 / 0.0 不最优 / -1.0 明显不当
redundancy_penalty(i):    0.0 非冗余 / -0.5 高度重复
```

### 3.5 DocVerify++-lite: 轻量过程验证器

DocVerify++ 的轻量化版本，专为轨迹 pipeline 内嵌质检设计：

| 对比 | DocVerify++ (完整版) | DocVerify++-lite |
|------|-----|--------|
| 用途 | 独立研究 | pipeline 内嵌质检 |
| Claim 分解 | 8 类细粒度 | 简化为 thought/answer 句级 |
| Evidence 检索 | 多策略 ranking | 直接使用 evidence_refs |
| Support 判断 | 多信号 verifier | 规则 + NLI 二分类 |
| 延迟 | 离线 | 在线 (<10s/轨迹) |

### 3.6 Failure Taxonomy

| 失败类型 | 定义 | 修复策略 |
|---------|------|---------|
| `format_error` | ReAct 格式不完整 | 强化 prompt + parser |
| `retrieval_miss` | search 没找到相关页面 | 改善检索 + 增加 top_k |
| `bbox_wrong` | crop/parse bbox 不对应目标 | 自动 bbox 候选 |
| `parse_error` | parse_table 结果不正确 | 限制到高质量表格 |
| `compute_error` | 表达式或变量错误 | 程序验证 + 溯源 |
| `early_answer` | 证据不足时过早回答 | sufficiency reward |
| `over_search` | 过多不必要搜索 | efficiency penalty |
| `unsupported_claim` | 声明无证据支持 | DocVerify++ 过滤 |
| `wrong_refuse` | 可回答被错误拒答 | refusal F1 评估 |
| `wrong_answer` | 答案与参考不匹配 | 核心答案验证 |

---

## 模块四: 统一 Schema 与数据打包

### 4.1 DocWorldTrace Schema

```json
{
  "doc_id": "...",
  "task_id": "...",
  "question": "...",
  "environment_state": {
    "visible_pages": [],
    "evidence_memory": [],
    "tool_budget": 10
  },
  "trajectory": [
    {
      "step": 1,
      "thought": "...",
      "action": "search|read_page|crop|ocr|parse_table|compute|verify|answer|refuse",
      "action_input": {},
      "observation": {},
      "evidence_refs": [],
      "reward_signals": {
        "answer_correct": null,
        "evidence_supported": null,
        "bbox_valid": null,
        "tool_efficiency": null
      }
    }
  ],
  "final_answer": "...",
  "docverify_label": {
    "support": "supported|partial|contradicted|not_supported",
    "sufficiency": "sufficient|insufficient|missing|conflicting"
  }
}
```

### 4.2 扩展字段

| 字段 | 用途 |
|---|---|
| `document_profile` | 页数、领域、OCR 质量、表格/图表数量 |
| `task_type` | text_lookup / table_lookup / numeric / cross_page / unanswerable / verification |
| `tool_trace_format` | react / alr / vsc / doc_adp |
| `negative_construction` | numeric_perturbation / entity_swap / evidence_mismatch / evidence_removal |
| `quality_flags` | retrieval_miss / bbox_wrong / numeric_mismatch / over_refusal |
| `conversion_targets` | SFT conversation / ADP / RL rollout |

### 4.3 格式转换

DocWorldTrace Schema 支持以下目标格式：

1. **SFT Conversation** — System/User/Assistant/Tool 多轮对话，直接用于指令微调
2. **ADP-compatible** — 对齐 Agent Data Protocol 的 action/observation/metadata 结构
3. **RL Rollout** — 包含 per-step reward 的序列，适配 GRPO/SPO/RLVR
4. **PRM Training** — 正/负步骤对比对，用于过程奖励模型训练
