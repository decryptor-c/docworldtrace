# 维度 4：Tool-use / Function-calling 训练数据与方法

> **审稿人可能攻击点**: DocWorldTrace 的工具化动作空间和工具选择策略学习是否在 Toolformer/ToolLLM/APIGen 等工作后仍有新意？Document tools 和 General API tools 有本质区别吗？

---

## 1. 维度概述

DocWorldTrace 定义了 10 个文档专用工具（search / read_page / overview / crop / ocr / parse_table / compute / verify / answer / refuse），并将工具选择纳入七维 reward（R_tool）和 per-step PRM（tool_appropriateness）。这需要在以下方向找到文献支撑：

- Tool-use 训练数据合成方法
- Function-calling fine-tuning 和 benchmark
- 工具选择作为学习问题（不只是 API 调用）
- Multi-step tool use planning

---

## 2. 代表性论文

### 2.1 基础 Tool-use 工作

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 1 | **Toolformer: Language Models Can Teach Themselves to Use Tools** (Schick et al.) | NeurIPS 2023 | 首次系统证明 LLM 可自我学习何时调用外部工具（计算器/搜索/日历）；GPT-J 6.7B 超越 GPT-3 175B | **工具自学范式**：DocWorldTrace 的 teacher rollout 是这一范式的文档领域迁移 |
| 2 | **Gorilla: Large Language Model Connected with Massive APIs** (Patil et al.) | ICML 2024 | 微调 LLaMA-7B 连接 1,600+ API；Retriever-Aware Training (RAT) 使模型推理时可使用最新 API 文档；零样本 API 选择超越 GPT-4 | **API 选择**：DocWorldTrace 的 tool_appropriateness reward 与 Gorilla 的工具选择对齐 |
| 3 | **ToolLLM: Facilitating LLMs to Master 16000+ Real-world APIs** (Qin et al.) | ICLR 2024 | 16,464 API + DFSDT 搜索生成 200K 训练样本；ToolLLaMA-7B 匹敌 ChatGPT；多工具组合场景 (G1/G2/G3) | **多工具组合**：DocWorldTrace 的 10-action 工具空间需要类似的 multi-tool composition 数据 |

### 2.2 工具数据合成与验证

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 4 | **APIGen: Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets** (Liu et al., Salesforce) | arXiv 2024.06 | 三阶段验证（格式→执行→语义）；60K 高质量数据；xLAM-1B 超越 GPT-3.5-Turbo（仅 1B 模型） | **验证驱动合成**：APIGen 的 verification pipeline 是 DocWorldTrace 的"合成→验证→过滤"最接近的对照工作 |
| 5 | **BFCL: The Berkeley Function Calling Leaderboard** (Patil et al.) | ICML 2025 | V4 版本：单轮/并行/多轮/多步/Agentic web search+memory；AST 子树匹配评估；揭示多轮性能仅 ~50-55% | **评估标准**：DocWorldTrace 的多步工具轨迹评估可对照 BFCL 的 multi-turn 指标 |
| 6 | **ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases** | 2023 | 小规模模拟工具场景训练，让小模型泛化到未见工具 | **规模 vs 质量**：与 DocWorldTrace 的"1K-3K 小规模高质量"理念一致 |

### 2.3 Multi-step Tool Planning

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 7 | **EviPath: Evidence-Anchored Reasoning Path Synthesis for RAG Agents** | NeurIPS 2025 | 用 abductive subtask planning + faithful sub-question answering 合成完整的 agent-environment 交互轨迹；8B 模型 +14.7% EM | **证据锚定规划**：EviPath 的 evidence-anchored synthesis 与 DocWorldTrace 的 evidence-grounded trajectory 直接对应 |
| 8 | **MALT: Improving Reasoning with Multi-Agent LLM Training** (Motwani et al.) | 2024 | 多 Agent 角色协同（generator/verifier/refiner）；trajectory-expansion + joint outcome-based credit assignment | **Credit Assignment**：DocWorldTrace 的 per-step reward 本质上是在解决多步工具组合的 credit assignment |
| 9 | **MSearcher: Self-Reflective Search Agent Empowered by MCTS** | Under Review | MCTS 驱动的自我反思搜索 Agent；两阶段：SFT cold start + RL | **搜索 Agent**：文档 Agent 本质上是"文档中的搜索 Agent"，MSearcher 的方法论可迁移 |
| 10 | **Loong: Synthesize Long Chain-of-Thoughts at Scale through Verifiers** | arXiv 2025.09 | LoongBench (8,729 样本, 12 领域) + LoongEnv (代码执行验证 + RLVR) | **Verifier-guided CoT**：Loong 的"verifier 引导合成"与 DocWorldTrace 的 DocVerify++ 引导合成方法一致 |

### 2.4 工具选择作为学习问题

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 11 | **SynWorld: Virtual Scenario Synthesis for Agentic Action Knowledge Refinement** | ACL 2025 | 从 action space 出发合成多步场景，MCTS 探索优化 action knowledge；关注"工具组合工作流"而非单工具调用 | **工具工作流**：SynWorld 的"工具组合 workflow"与 DocWorldTrace 的核心问题（何时 search→crop→parse）完全一致 |
| 12 | **Fathom-DeepResearch: RAPO & Steerable Step-Level Rewards** | arXiv 2025.09 | 可操控的 step-level reward：按认知行为和边际效度对每次 tool call 分类评分；4B 模型做多步信息检索 | **Step-level Tool Reward**：Fathom 的"按工具行为类型评分"与 DocWorldTrace 的 tool_appropriateness 高度一致 |

---

## 3. 与 DocWorldTrace 的关联分析

### 3.1 General API tools vs Document tools

现有 tool-use 工作（Toolformer、ToolLLM、APIGen、Gorilla）聚焦于**通用 API**（搜索、计算器、翻译、日历等），核心挑战是"从成千上万个 API 中选择正确的"。DocWorldTrace 聚焦于**领域专用工具**，核心挑战不同：

| 对比维度 | General API Tools | DocWorldTrace Document Tools |
|---------|------------------|------------------------------|
| 工具数量 | 数百-数万 | **10 个标准化工具** |
| 核心挑战 | API 选择和参数填充 | **工具组合策略 + 证据积累路径** |
| Observation 可靠性 | API 返回结构化结果（可靠） | **工具输出可缓存 + bbox/OCR 可交叉验证（更可靠）** |
| 训练需求 | 大规模 API 覆盖 | **高质量工具路径示范** |

这意味着文档领域的核心不是"学会调用更多工具"，而是**学会在正确时机用正确工具组合来积累证据**——这是一个 planning/strategy 问题，而非 API coverage 问题。

### 3.2 Tool verification 的领域优势

APIGen 的三阶段验证（format → execution → semantic）需要依赖实际 API 调用。DocWorldTrace 的工具验证有其特有优势：

- **Search/read_page/crop/ocr/parse_table 的输出可缓存**：验证成本低
- **Bbox/page 交叉验证**：文档特有的定位验证
- **Compute 复算**：表达式确定性验证
- **Verify action**：内建元工具，自我审计

### 3.3 EviPath 与证据锚定

EviPath（NeurIPS 2025）是最接近 DocWorldTrace 的工作——它同样强调 evidence-anchored 推理路径合成。关键区别：

- EviPath 面向 RAG 开放域 QA，证据来自检索文档集
- DocWorldTrace 面向 closed-domain PDF，证据来自单个文档内的 page/bbox 定位

DocWorldTrace 的 closed-domain 特性使得证据锚定更精确（page/bbox 级 vs passage 级）。

---

## 4. DocWorldTrace 的差异化定位

| 对比维度 | ToolLLM / APIGen | EviPath | **DocWorldTrace** |
|---------|-----------------|---------|-------------------|
| 工具类型 | 通用 API (REST/Python) | RAG 检索+阅读 | **文档专用工具 (10-action)** |
| 训练目标 | API 调用正确性 | 证据锚定 QA | **工具组合策略 + 证据积累 + 拒答** |
| 验证信号 | API 执行结果 | 答案正确性 | **7 维 reward + bbox/OCR/compute 交叉验证** |
| 环境 | 无环境（API sandbox） | 开放域检索 | **封闭域 DocEnv-lite** |
| 复现性 | API 可能变更 | 检索结果不可复现 | **PDF 静态 + 工具输出可缓存** |

**核心差异化论点**: DocWorldTrace 不是在已有 tool-use 工作上做"又一个工具调用数据集"。它解决的是工具领域（tool-use field）的一个新问题——**在数量少但语义丰富的专用工具空间中，如何通过搜索式合成找到最优工具组合路径，并用领域结构化验证信号保证路径质量**。这个问题的挑战性在于工具选择策略（何时 search vs crop vs parse）而非工具覆盖率。

---

## 5. 审稿人防御话术

> **Q: "APIGen 已经解决了 function-calling 数据合成的验证问题，你们在文档领域的方式有何不同？"**

A: APIGen 的验证依赖"API 是否执行成功"，这只能验证工具调用的**格式正确性**，无法验证工具选择的**策略合理性**（即"在这个状态下该不该调用这个工具"）。DocWorldTrace 的 tool_appropriateness reward 和 per-step evidence_gain 信号补充了策略层面的验证。此外，文档工具的输出可通过 bbox/OCR/compute 交叉验证，比 API 返回值的单点验证更丰富。

> **Q: "10 个工具规模太小，如何处理现实中的数百种文档类型？"**

A: 文档工具的语义丰富性而非数量决定了其价值。search 的语义因文档而异，parse_table 的结构因表格而异——10 个标准化工具已经可以覆盖从文本查找到跨页推理到数值计算的完整文档推理谱系。这与 GUI Agent 只有 click/type/scroll 几个底层动作但能完成数百种任务的逻辑一致：少即是多，工具组合产生复杂度。

---

## 6. 参考文献索引

- [Toolformer (NeurIPS 2023)](https://arxiv.org/abs/2302.04761)
- [Gorilla (ICML 2024)](https://arxiv.org/abs/2305.15334)
- [ToolLLM (ICLR 2024)](https://arxiv.org/abs/2307.16789)
- [APIGen (arXiv 2024)](https://arxiv.org/abs/2406.18518)
- [BFCL V4 (ICML 2025)](https://icml.cc/virtual/2025/poster/46593)
- [EviPath (NeurIPS 2025)](https://nips.cc/virtual/2025/loc/san-diego/126543)
- [SynWorld (ACL 2025)](https://arxiv.org/abs/2504.03561)
- [Loong (arXiv 2025)](https://arxiv.org/abs/2509.03059)
- [Fathom-DeepResearch (arXiv 2025)](https://arxiv.org/abs/2509.24107)
- [MALT (2024)](https://www.semanticscholar.org/paper/MALT%3A-Improving-Reasoning-with-Multi-Agent-LLM-Motwani-Smith/c6c570296a491267697ed30ef37e5865c4a19109)
- [MSearcher (Under Review)](https://openreview.net/forum?id=vJBMYahZY5)
- [ToolAlpaca (2023)](https://arxiv.org/abs/2306.05301)
