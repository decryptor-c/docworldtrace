# DocWorldTrace: 验证引导的文档 Agent 工具轨迹合成

> **Executive Summary**: 当前多模态文档 Agent 系统（VISOR、MM-Doc-R1、DocSeeker 等）普遍面临"开源 RL 蒸馏悖论"——声称通过 GRPO/SPO 训练开放模型获得 agentic reasoning 能力，但冷启动轨迹均依赖 GPT-4o/Gemini 等闭源 teacher，且轨迹数据一律不公开。更深层的问题在于数据形态：现有公开的 DocVQA/MP-DocVQA/MMLongBench-Doc 等数据集仅提供 answer-only QA 对，无法训练模型的工具选择策略、证据积累路径、充分性判断和拒答能力。DocWorldTrace 提出将 PDF 文档建模为可交互环境（DocEnv-lite），通过 10 个标准化文档工具和多源轨迹采样，以 DocVerify++ 的 claim-evidence 验证信号引导合成与过滤，产出可复现、可审计、经验证的高质量文档 Agent 工具轨迹数据集。Pilot 实验（H1-H4）已在 5 篇 PDF、20 个种子、80 条轨迹上完成闭环验证：DocEnv 工具执行成功率 100%，Teacher 轨迹格式合规率 100%，DocVerify++ 在注入式负例上 caught rate 100%。

---

## 1. 背景与研究动机

### 1.1 范式转变：从"直接回答"到"多步 Agent 交互"

多模态文档推理正经历根本性的范式转变。以 VISOR、MM-Doc-R1、DocSeeker、DocCogito、DocLens、MDocAgent 为代表的文档 Agent 系统，已将长文档理解任务重构为包含主动检索、视觉定位、证据积累、工具组合和拒答判断的多步交互过程。

这些系统的共同特征是引入了工具化动作空间（search/crop/parse_table/compute 等），使模型从"一次性读取全文并输出答案"转变为"在文档环境中逐步探索并基于多步证据做出判断"。这一趋势与 GUI Agent 领域（WebArena, OSWorld, AndroidWorld）的发展路径高度一致——两者都将任务建模为 Agent 与环境之间的多轮交互。

### 1.2 "开源 RL 蒸馏悖论"

当前文档 Agent 领域面临一个根本性困境：

| 系统 | RL 方法 | 轨迹数据公开 | Teacher 依赖 | 环境可复现 |
|------|--------|:---:|:---:|:---:|
| VISOR | GRPO + visual action eval | ✗ | GPT-4o | ✗ |
| MM-Doc-R1 | SPO (Similarity-based Policy Optimization) | ✗ | Gemini (推测) | ✗ |
| DocSeeker | evidence-aware GRPO | ✗ | GPT-4o | ✗ |
| DocCogito | 闭源 VLM 蒸馏 | ✗ | 闭源 VLM | ✗ |
| MDocAgent | 多 Agent 框架 | ✗ | GPT-4V | ✗ |
| DocLens | Training-free | — | — | 部分 |

**5/6 的主要文档 Agent 系统完全不可复现**。每个新系统必须从零重新蒸馏闭源 teacher 轨迹（成本 $0.10-0.30/条 × 数千条 = 数百至数千美元），且轨迹不公开使后续研究者无法在同一数据上做公平对比。

### 1.3 数据形态瓶颈

更深层的问题在于**数据形态**。现有公开文档 QA 数据集（DocVQA, MP-DocVQA, MMLongBench-Doc, TATQA, FinQA）仅提供 question-answer 对。Answer-only 数据无法训练以下五项关键能力：

| 能力 | 训练需求 | Answer-only 能否满足？ |
|------|---------|:---:|
| **工具选择策略** | 每步的 tool choice + 参数示范 | ✗（无工具调用信号） |
| **证据逐步积累** | evidence_memory 的增量更新过程 | ✗（无中间状态） |
| **充分性判断** | 何时该停止搜索、何时该继续 | ✗（无 sufficiency 信号） |
| **拒答决策** | 不可回答问题的正确处理 | ✗（无 refusal 示范） |
| **过程忠实性** | 推理是否被文档证据支持 | ✗（无 provenance 可追溯） |

---

## 2. 现有研究的五个核心缺口

### Gap 1: 轨迹数据缺失

所有公开文档 QA 数据集（DocVQA/MP-DocVQA/MMLongBench-Doc）只提供 question-answer 对，不含中间推理步骤和工具调用序列。ADP (Agent Data Protocol) 虽提供了统一的 agent trajectory schema，但没有文档领域的数据实例。

### Gap 2: 环境不可复现

每个文档 Agent 系统自建交互环境（VISOR 的 search/crop/answer、DocSeeker 的 ALR 三阶段、DocCogito 的 VSC 原子操作），但这些环境**不标准化、不可互操作**，无法在同一环境中公平对比不同 Agent 策略。

### Gap 3: 过程级奖励缺失

现有文档 Agent 的训练和评估仅验证最终答案正确性（answer-level），不评估：(a) 每步 action 是否带来 evidence gain；(b) 推理步骤是否被文档证据支持（support）；(c) 定位是否精确（grounding）；(d) 工具选择是否合理。

### Gap 4: 忠实性控制缺口（Faithfulness Gap）

存在一种隐蔽的质量问题：**答案正确但中间推理未被文档证据支持**。例如模型凭记忆估算数值而非从文档表格中读取。现有 answer F1/ANLS 评估完全不检测这一 gap。VLAA-Thinking (TMLR 2025) 进一步发现，SFT 训练的模型会产生"pseudo reasoning paths"——看起来像推理但包含错误步骤的模仿性思维链。

### Gap 5: 拒答与充分性训练缺失

实际场景中用户问题经常**不可回答**（信息不在文档中）或**证据不足**，但现有训练数据几乎不包含这类场景。MMLongBench-Doc 有 unanswerable 标注但无工具调用轨迹。模型缺乏基于充分性的动态决策能力。

---

## 3. 核心解决思路：文档即环境 + 验证引导合成

### 3.1 核心 Thesis

> **如果把文档任务重构为可交互环境，并用 DocVerify++ 提供过程级验证信号，就可以合成比 answer-only QA 更适合训练文档 Agent 的工具轨迹数据。**

### 3.2 三条研究线索的统一

```text
线索 1: GUI Agent 的"环境→轨迹→质控"方法论
        (WebArena, AgentTrek, DigiRL)
线索 2: 多模态文档推理的工具化动作空间
        (VISOR, DocSeeker, DocCogito)
线索 3: DocVerify++ 的 claim-evidence 可验证信号
        (support/sufficiency/failure taxonomy)
              ↓
统一产出: DocWorldTrace — 可复现、可审计、经验证的文档 Agent 工具轨迹数据集
```

### 3.3 本质定位：不是"又一个文档 Agent 框架"

DocWorldTrace 是**数据与环境基础设施**，而非"又一个文档 QA Agent"。与现有工作的核心区别：

| 维度 | 现有文档 Agent 系统 | DocWorldTrace |
|------|-------------------|---------------|
| 定位 | Agent 框架/方法 | **数据与环境基础设施** |
| 轨迹公开 | ✗ | **✓（核心贡献）** |
| 环境标准化 | 各自实现 | **DocEnv-lite 统一接口** |
| 过程级 reward | 无/隐式 | **七维显式 reward + DocVerify++** |
| 拒答训练 | 无 | **sufficiency reward + unanswerable 样本** |
| Schema 兼容 | 绑定各自格式 | **ADP 兼容 + 多格式转换** |

### 3.4 文档环境 vs GUI 环境的结构性优势

| 维度 | GUI 环境（WebArena） | 文档环境（DocEnv-lite） |
|------|---------------------|----------------------|
| 环境稳定性 | 中（Docker 化但动态 Web 内容） | **极高（PDF 静态）** |
| 工具输出缓存 | 多数不可缓存 | **search/read/crop/ocr/parse 全量可缓存 (60-80%)** |
| 评估信号丰富度 | 1 维（goal completion 0/1） | **7 维（answer/support/ground/suff/eff/refuse/tool）** |
| 环境构建成本 | 高（Docker/VM） | **低（PDF 解析 pipeline）** |
| 环境重置 | 需快照恢复 | **零成本（PDF reload）** |
| 并行化 | 中（多 Docker 实例） | **高（多 PDF 独立运行）** |
| 过程可审计性 | 有限（VLM judge 不可靠） | **精确（bbox/OCR/compute 交叉验证）** |

---

## 4. 大致方案（四个核心模块）

### 模块一：DocEnv-lite — 面向 PDF 的轻量交互环境

将 PDF 解析为可交互环境，提供 **10 个标准化文档工具**，按使用频率分为核心层和扩展层：

**核心 Action（5 个）**:

| # | Action | 参数 | 返回 Observation | 共识度 |
|---|--------|------|-----------------|:---:|
| 1 | `search(query, top_k)` | 文本查询 + 返回数 | 候选页面列表 + snippet | 9/16 |
| 2 | `read_page(page_ids)` | 页码列表（支持批量） | OCR 文本 + 页面图像描述 | 11/16 |
| 3 | `crop(page_id, bbox)` | 页码 + 坐标 | 裁剪区域图像 + OCR | 5/16 |
| 8 | `answer(text, evidence_refs)` | 答案文本 + 证据引用 | 终止 (成功) | 16/16 |
| 9 | `refuse(reason)` | 拒答理由 | 终止 (拒答) | 2/16 (独特) |

**扩展 Action（5 个）**:

| # | Action | 参数 | 返回 Observation |
|---|--------|------|-----------------|
| 10 | `overview()` | 无 | 文档缩略图网格 + 元信息 |
| 4 | `ocr(page_id, bbox=None)` | 页码 + 可选区域 | 识别文本 + 字符 bbox |
| 5 | `parse_table(page_id, bbox)` | 页码 + 区域 | 结构化表格 (cells + bbox) |
| 6 | `compute(expr, vars)` | 表达式 + 变量 | 计算结果 |
| 7 | `verify(claim, evidence_refs)` | 待验证 claim + 证据引用 | support/sufficiency 判断 |

每个 observation 包含结构化 provenance 信息（page/bbox/element_type/confidence），确保证据可追溯。内置 observation 缓存机制使 MCTS 搜索中 60-80% 的工具调用可从缓存获取，边际成本趋近于零。

环境状态包含 `evidence_memory`——跨步骤积累的证据列表，每个证据记录其来源页码、bbox 坐标、内容、所属元素类型和产生该证据的 source_action。

### 模块二：多源轨迹采样

**种子任务准备**（三类来源）:
- **来源 A**: 已有 QA 数据集（DocVQA, MP-DocVQA, MMLongBench-Doc, TATQA/FinQA）
- **来源 B**: 文档结构自动派生（表格 → table lookup、跨页标题 → cross-page）
- **来源 C**: LLM 任务合成（给定文档 profile + 摘要生成多类型问题）

六类任务分布：Text lookup (25%) / Table lookup (20%) / Numeric computation (20%) / Cross-page reasoning (15%) / Verification (10%) / Unanswerable (10%)

**四种采样方法**（按执行的顺序）:

1. **Rule-based 模板轨迹**: 为简单任务提供确定性轨迹（例如 text_lookup: `search → read_page → answer`）
2. **Teacher Rollout**: 强模型（GPT-4o/Gemini）在 DocEnv 中按 ReAct 格式逐步执行，**Observation 100% 来自 DocEnv 真实执行**
3. **Hard Negative 扰动**: 从正确轨迹注入 7 类可控错误（工具选择错误/参数错误/过早回答/过度搜索/答案错误/证据遗漏/虚假拒答），用于 DPO/PRM 训练
4. **小规模 MCTS 消融**（仅 50-100 样本）: 验证文档环境中搜索式轨迹合成的价值

### 模块三：质量控制与 Reward 设计

**五层质量检查体系**:

```text
Layer 1: 格式检查 → action 合法性、ReAct 完整性
Layer 2: 执行检查 → observation 来自 DocEnv 真实执行
Layer 3: 答案检查 → EM/F1/ANLS vs reference
Layer 4: 证据检查 → bbox 有效性、OCR 交叉验证、compute 复算
Layer 5: 过程检查 → DocVerify++-lite 的 claim-evidence support/sufficiency
```

**四级轨迹质量分级**:

| 等级 | 通过 Layer | 定义 | 用途 | 预计占比 |
|:---:|:---:|------|------|:---:|
| Gold ★★★ | L1-L5 全通过 | 答案正确 + 全证据支持 + 无冗余 | SFT 主训练集 | 20-30% |
| Silver ★★ | L1-L3, L4 部分 | 答案正确, 部分 grounding 缺失 | SFT 补充 | 25-35% |
| Bronze ★ | L1-L3 通过 | 答案正确但过程有瑕疵 | PRM 对比正例 | 15-25% |
| Negative ✗ | L3 失败 | 答案错误或不当拒答 | DPO/PRM 负例 | 20-30% |

**七维 Reward 信号**:

| 层级 | 信号 | 取值 | 来源 |
|------|------|------|------|
| Outcome | R_answer | 0/1 或 F1 | 答案 vs 参考答案 |
| Evidence | R_support | 0/0.5/1 | DocVerify++ 证据支持性 |
| Grounding | R_ground | IoU / bbox validity | bbox 验证 |
| Sufficiency | R_suff | 0/1 | 回答时证据是否充分 |
| Efficiency | R_eff | [0,1] | 有效步数 / 总步数 |
| Refusal | R_refuse | 0/1 | 不可回答时是否拒答 |
| Tool | R_tool | 0/1 | 工具选择和参数正确性 |

**10 类 Failure Taxonomy**: format_error / retrieval_miss / bbox_wrong / parse_error / compute_error / early_answer / over_search / unsupported_claim / wrong_refuse / wrong_answer

### 模块四：统一 Schema 与数据打包

DocWorldTrace Schema 统一记录 Thought→Action→Observation→Evidence Update→Optional Verify→Answer，每条轨迹自带 evidence_refs 和 quality_signals。支持三种输出格式：
- **SFT Conversation**（System/User/Assistant/Tool 多轮对话）
- **ADP-compatible**（对接 Agent Data Protocol 标准）
- **RL Rollout**（含 per-step reward 的序列，适配 GRPO/SPO/RLVR）

---

## 5. 为什么能解决当前的研究问题

### 缺口-方案对应论证

| 缺口 | DocWorldTrace 方案 | 为什么现有工作无法解决 |
|------|-------------------|---------------------|
| **Gap 1: 轨迹缺失** | DocWorldTrace-1K/3K 公开数据集 | 现有系统轨迹不公开；公开数据仅有 answer-only |
| **Gap 2: 环境不可复现** | DocEnv-lite 标准化环境 | 各系统自建环境，不可互操作 |
| **Gap 3: 过程 reward 缺失** | 七维 reward + per-step PRM | 仅 answer-level 评估，无 step-level 信号 |
| **Gap 4: 忠实性缺口** | DocVerify++-lite 过程验证 + 过滤 | 无系统化的 claim-evidence support 检查 |
| **Gap 5: 拒答缺失** | Sufficiency reward + unanswerable 样本 | 无 sufficiency/refusal 训练数据 |

### 跨维度核心逻辑链

```
文档环境的静态性和结构化
  → 工具输出可缓存、可交叉验证
  → 过程信号更丰富、更精确（对比 MC 采样/LLM judge）
  → 数据质量控制从"语义猜测"升级为"证据驱动验证"
  → 小规模高质量轨迹足以产生训练增益
```

### Pilot 实验初步验证（H1-H4）

| 实验 | 假设 | 核心结果 | 状态 |
|:---:|------|---------|:---:|
| **H1** | DocEnv 工具环境可行性 | 50/50 工具调用成功（100%），缓存一致性 100%，5 篇 PDF per-document pass rate 100% | ✅ |
| **H2** | Teacher 可生成多步工具轨迹 | 80/80 格式合规（100%），adjusted 答案正确率 100%，direct answer 率 0%，覆盖 6 类任务 | ✅ |
| **H3** | DocVerify++ 可区分 supported/unsupported | 正例 80/80 supported/sufficient/keep；注入式负例 144/144 caught（128 reject + 16 review），missed-keep 0% | ✅ |
| **H4** | 轨迹具有任务与路径多样性 | 覆盖 6/6 任务类型、7/7 核心动作 + crop、10 类 unique 工具序列、search query unique 率 52.78% | ✅ |

**关键指标**: Tool execution valid rate 100%（门槛 ≥90%）；注入式负例 caught rate 100%（零 false-keep）；6 类 failure taxonomy（missing_evidence/answer_mismatch/numeric_mismatch/table_value_mismatch/verification_label_mismatch/insufficient_negative_evidence）

**残余风险**: (a) 文档池仅 5 篇且偏 arXiv+ARS，缺真 10-K/扫描件；(b) 自然分布上的人工 GT confusion matrix 仍未做（当前仅有注入式负例）；(c) 步数方差偏低（2.925 处于设计 3-8 下沿）；(d) verify 使用率仅 10%（主要在 verification 任务中）。这些将在 Phase 2 扩展中补齐。

---

## 6. 预期产出与贡献

### 五大贡献

**C1: DocEnv-lite** — 首个面向 PDF 的可交互、可审计、可缓存的文档工具环境。提供 10 个语义级文档工具、7 维过程 reward 信号体系、observation 缓存机制和完整 provenance 追溯。可独立于数据集被社区用作文档 Agent 的标准化评测环境。

**C2: DocWorldTrace Schema** — 统一轨迹格式，兼容 ReAct/ALR/VSC/ADP。每条轨迹自带 evidence_refs 和 quality_signals，支持 SFT/DPO/PRM/RL 多训练目标。

**C3: Verification-guided Synthesis** — 将 DocVerify++ 的 claim-evidence-support/sufficiency 验证信号系统化嵌入多源轨迹采样→过滤→分级的全流程，实现从"事后 faithfulness 评估"到"事中数据质量保证"的范式升级。

**C4: DocWorldTrace-1K/3K Dataset** — 公开的高质量文档 Agent 工具轨迹数据集。40-60 篇 PDF（arXiv + SEC/EDGAR）生成 100-200 个 QA 种子，多源采样产出 2K-5K 候选轨迹，DocVerify++ 过滤后保留 1K-3K 高质量轨迹，覆盖 6 类任务、Gold/Silver/Bronze/Negative 四级分级。

**C5: Training and Evaluation Study** — 系统化对比 answer-only SFT / teacher ReAct SFT / DocWorldTrace SFT / filtered DocWorldTrace SFT，7 维评测指标全覆盖。不强调绝对 SOTA，聚焦可复现性、忠实性、工具效率和拒答能力。

### 投稿定位与叙事策略

- **优先投稿方向**: ACL/EMNLP Resource Track（强调环境+数据集+公开轨迹的资源价值）；NeurIPS Datasets and Benchmarks（强调数据合成 pipeline + 质量分析的系统化贡献）
- **叙事聚焦**: 可复现性、忠实性和工具效率的相对提升，而非绝对 SOTA 性能
- **叙事结构**: "环境使方法可行，方法使数据高质量，数据使训练可复现"——三层因果链

### 与现有项目的协同

| 项目 | 协同方式 |
|------|---------|
| **DocVerify++** | 提供 support/sufficiency reward 与 failure taxonomy；DocWorldTrace 依赖其做质量过滤 |
| **DocGround** | 作为 training-free grounded output 的评测对象；DocWorldTrace 数据可评估其 grounding 质量 |
| **CodeAsReasoning** | 共享 compute 计算沙盒组件 |
| **FaithfulnessByDesign** | 可消费 DocWorldTrace 的 faithfulness gap 数据进行诊断分析 |

---

## 7. Related Work 定位与差异化总结

### 三个已有方向

1. **通用 Agentic Data Synthesis**（RandomWorld, SynWorld, Simia, SynthTools, WebSynthesis, ADP）— 将通用方法论迁移到文档领域，利用文档环境的静态可缓存优势
2. **GUI Agent 范式**（WebArena, AgentTrek, DigiRL, SPORT）— 迁移"环境化+轨迹化+质控化"方法论，但动作空间从像素级变为语义级
3. **多模态文档 Agent**（VISOR, MM-Doc-R1, DocSeeker, DocCogito）— 不做新 Agent 框架，提供可复现环境+公开轨迹+验证引导合成的基础设施

### 六个防御维度的核心差异化

| 维度 | 核心差异化 | 关键文献 |
|------|----------|---------|
| **D1: PRM** | 首个面向文档 Agent 的 7 维过程信号体系；利用 bbox/OCR/计算的结构化验证替代 MC 采样估计，提供更低方差的过程监督 | Math-Shepherd, Web-Shepherd, AgentPRM, PRInTS |
| **D2: 质控** | 从"语义猜测"（LLM 评分/梯度）升级为"证据驱动的结构化验证"（bbox validity/OCR consistency/compute reproducibility）；四级分级支持 SFT/DPO/PRM 分集训练 | DEITA, LESS, AlpaGasus, DS², LIMA |
| **D3: 忠实性** | 从"检测幻觉"到"预防幻觉训练数据"的范式迁移；closed-domain 文档的 bbox/OCR 验证比开放域 KB 验证更精确 | FActScore, FaithAct, KIE-HVQA, VERISCORE |
| **D4: Tool-use** | 从"API 覆盖率"（ToolLLM/APIGen）到"工具组合策略+证据积累路径"；10 个语义丰富工具覆盖完整文档推理谱系（工具组合 > 工具数量） | Toolformer, Gorilla, ToolLLM, APIGen, EviPath |
| **D5: 环境** | 首个将 PDF 文档建模为可审计、可缓存、可并行的确定性交互环境；环境的可审计性（bbox/OCR/计算验证）是文档领域独有的结构性优势 | TextWorld, WebArena, SWE-bench, AndroidWorld |
| **D6: Novelty** | 准备了对"WebArena 换 domain""验证信号不新颖""MCTS 已被做过""规模太小"四大攻击方向的完整文献支撑和差异化论证 | 详见 d6_novelty_defense.md |

所有差异化定位共享底层优势：**文档环境的静态性和结构化特性使 DocWorldTrace 在整个 pipeline 的每个环节都比通用领域工作拥有更精确、更可验证的信号**。

---

## 当前阶段与下一步计划

**当前阶段**: Pilot 验证完成（H1-H4 全部通过），进入 Phase 1 — DocEnv-lite 构建 + Phase 2 — 大规模轨迹采样准备

**时间线**（共 12 周）:
- Week 1-2: DocEnv-lite 构建（7 个 MVP 工具 API + observation 缓存）
- Week 3-4: Pilot 种子任务（40-60 篇 PDF、100-200 个 QA 种子）与多源轨迹采样（2K-5K 候选轨迹）
- Week 5-6: 质量控制与过滤集成（五层质检 + DocVerify++-lite + 人工审核 100-150 条）
- Week 7-8: Dataset v0.1 打包（三种格式 + 统计报告 + datacard）
- Week 9-10: Baselines 实验（4 组 SFT 对比 + 消融）
- Week 11-12: 论文撰写

**关键决策点**:
- Week 2 末: tool execution valid rate <85% → 停顿修复
- Week 4 末: MCTS 成本/质量可控 → 扩展；否则仅做消融
- Week 6 末: DocVerify++ precision <75% → 降为分析工具；SFT 效果不足 → 转向 Resource 叙事
- Week 8 末: SFT 显著提升 → 加入 GRPO 实验

**Pilot 优先补充实验**:
1. **P0-4 [最高优先级]**: 自然分布人工 GT 标注（60-100 条）— 计算 DocVerify++ 在 teacher 自然产出上的 precision/recall（当前仅有注入式负例证据）
2. **P0-5**: review vs reject 阈值校准（16 条拒答负例全部走 review）
3. **P1-1**: 扩文档池到真 SEC 10-K、扫描件、坏 PDF 探针
4. **P2-1/2**: 定义 rule-based baseline + 量化步数方差
5. **P3**: 启动 H5 迷你 SFT 收益验证

---

> **文档版本**: v1.0 | **日期**: 2026-04-30 | **目标读者**: 外部合作者 / 审稿人 / 导师 | **预计阅读时间**: 15 分钟
