# 研究现状与 Related Work

> **目标**: 系统梳理 DocWorldTrace 所涉及的三大研究领域的代表性工作，明确定位差距。

---

## 1. 通用 Agentic Data Synthesis

当前 Agentic Reasoning 数据合成工作按环境来源和技术路径可分为以下四类：

### 1.1 程序化环境生成

**RandomWorld** 和 **SynthTools** 提出了自动化生成交互式工具环境的范式。RandomWorld 通过程序化生成可调用工具、工具状态和组合任务，使模型在合成环境中学习多步 tool use，验证了合成工具环境在 SFT/RL 训练中的可扩展性。SynthTools 进一步强调 Tool Generation、Tool Simulation 和 Tool Audit 三组件，特别是审计工具模拟输出一致性的能力。

**与 DocWorldTrace 的关系**: 文档工具（search/read_page/crop/parse_table/compute）可以类比程序化定义的工具生态；文档任务可从 PDF 结构自动派生。DocWorldTrace 的 DocEnv-lite 本质上是面向文档领域的程序化交互环境。

### 1.2 场景/轨迹搜索合成

**SynWorld** 从给定 action space 出发，合成多步 action invocation 场景，并通过 MCTS 探索来优化 action knowledge。它关注的核心问题是 Agent 是否理解工具组合的工作流（workflow），而非单一工具能否被调用。

**WebSynthesis** 针对 WebUI 轨迹成本高、真实环境不可控的问题，用 World Model 模拟虚拟 Web 环境，通过 MCTS 做可逆树搜索，证明了搜索式合成在轨迹质量上优于贪心 rollout。

**与 DocWorldTrace 的关系**: 文档 Agent 的核心难点正是工具组合策略（何时 search、何时 crop、何时 parse_table），MCTS 搜索适合比较不同工具路径。且文档环境比 WebUI 更适合 MCTS：PDF 是静态的，工具输出可全量缓存，使搜索成本远低于 GUI 环境。

### 1.3 LLM 模拟环境反馈

**Simia-SFT / Simia-RL** 的核心主张是：不必为每个 agent benchmark 手写真实环境，reasoning model 可以根据环境描述模拟 observation/reward，从而低成本合成 SFT 或 RL 训练数据。

**与 DocWorldTrace 的关系**: 文档任务中大部分工具反馈可真实执行（BM25 检索、OCR、表格解析、代码计算），仅少数复杂语义判断（图表解释、证据充分性）适合 LLM 模拟。DocWorldTrace 采用"真实工具优先 + LLM 模拟补全 + DocVerify++ 过滤"的混合策略。

### 1.4 轨迹标准化协议

**Agent Data Protocol (ADP)** 将异构 agent 数据集转换为统一的 action / observation / metadata schema，降低 agent SFT 数据工程成本。

**与 DocWorldTrace 的关系**: DocWorldTrace Schema 需要 ADP 兼容性，同时增加文档特有字段（page_id、bbox、element_type、evidence_ref、support_label、sufficiency）。

---

## 2. GUI Agent 环境模拟与轨迹收集

GUI Agent 领域在 2024-2026 年间形成了从环境构建到在线 RL 的完整范式，按技术路径可分为四大类：

### 2.1 交互环境基准

**WebArena** 构建了包含电商、社交媒体、代码管理、CMS 的 Docker 化 Web 环境，提供 812 个人工设计的 long-horizon 任务和基于 URL/内容/功能状态的自动化 goal check。**OSWorld** 将环境扩展到完整操作系统桌面，支持跨应用任务。**AndroidWorld** 使用 Android 模拟器，任务参数动态随机化支持百万级变体，并通过 ADB/SQLite 非侵入式状态检查做验证。

这些工作的核心贡献是确立了**"可复现环境 + 标准化评测"**的范式。DocWorldTrace 沿用这一理念，但将环境从 Web/OS/App 替换为 PDF 文档。

### 2.2 大规模轨迹合成

**AgentTrek** (ICLR 2025) 提出完全自动化的轨迹合成 pipeline（Tutorial Harvesting → Guided Replay → VLM Verification），成本仅 $0.55/轨迹。**GUI-Net-1M / TongUI** (AAAI 2026) 将规模扩展到 1M 条轨迹，覆盖 5 个操作系统和 280+ 应用。

这两项工作验证了"从结构化资源中提取并在真实环境中重放"的大规模轨迹合成可行性。DocWorldTrace 迁移这一结构：文档的目录/标题/表格对应 tutorial 的 step-by-step 结构，Teacher Rollout 对应 Guided Replay。

### 2.3 搜索式轨迹优化

**WebSynthesis** 用 World Model 指导 MCTS，在虚拟 WebUI 中做可逆树搜索生成高质量轨迹。**SPORT** 提出无需人工标注的自探索策略优化，通过 step-level VLM preference 信号做 DPO 迭代。

这些方法为 DocWorldTrace 的 MCTS 消融和 step-level reward 设计提供了直接参考。

### 2.4 在线 RL 训练

**DigiRL** (NeurIPS 2024) 在 Android 模拟器中做 offline-to-online RL，VLM 评估器自动生成 reward。**DART** 提出异步四模块框架优化 RL 训练的 GPU 利用率。

DocWorldTrace 短期聚焦 SFT，但预留 RL 接口：DocEnv 可并行化、DocVerify++ 可替代 VLM 评估器、Offline-to-online 路线（先 SFT 再 RL）与 DocWorldTrace pipeline 天然兼容。

### 2.5 GUI → Document 迁移映射

| GUI Agent 组件 | GUI 实现 | 文档 Agent 对应 | 关键差异/优势 |
|---|---|---|---|
| 环境 | Docker Web / Android VM | PDF 解析 + 工具 API | 文档静态，无部署成本 |
| 状态表征 | 截图 + DOM/A11y tree | 页面图像 + OCR/Layout | 无 DOM，需 OCR 替代 |
| 动作空间 | click / type / scroll | search / read / crop / parse / compute | 文档动作更语义化 |
| Observation | 页面截图 + 文本 | 工具结果 + provenance (page/bbox) | 文档 observation 更结构化 |
| 轨迹格式 | ReAct (T→A→O) | ReAct (T→A→O→Evidence Update) | 文档增加证据积累维度 |
| 奖励信号 | 任务完成 (0/1) | 答案 + 证据 + grounding + 效率 | 文档 reward 更丰富 |
| 环境重置 | Docker/VM 快照恢复 | PDF reload (零成本) | 文档重置最快 |
| 规模化 | 多模拟器并行 | 多 PDF + observation 缓存 | 文档并行化更容易 |

---

## 3. 多模态文档 Agent

### 3.1 代表系统

近期文档 Agent 工作形成了丰富的技术生态，但均存在"轨迹不公开、环境不可复现"的共同缺陷：

| 系统 | 工具/轨迹设计 | 训练方式 | 关键缺口 |
|------|-------------|---------|---------|
| **VISOR** | search / crop / answer + structured evidence space | GRPO + visual action eval | 无公开轨迹；reward 主要服务 RL |
| **Doc-V*** | retrieval / fetch / answer + working memory | 蒸馏 + SFT | evidence support 监督不足 |
| **MM-Doc-R1** | planner / seeker / answer + search/read | SPO + 轨迹相似性 | 无 bbox/cell 细粒度 grounding |
| **DocSeeker** | Analysis-Localization-Reasoning | evidence-aware GRPO | 轨迹格式绑定方法 |
| **DocCogito** | Select/Read/Filter/Compare/Aggregate (VSC) | 闭源 VLM 蒸馏 | 需要映射到底层工具 observation |
| **DocLens** | OCR / Element Localizer / Crop / VLM Reader | Training-free | 无 SFT/RL 轨迹数据 |
| **MDocAgent** | Text Agent / Image Agent / Critical Agent | 多 Agent 框架 | 无显式 bbox / grounded CoT |

### 3.2 共同局限性

这些系统共同说明文档推理的关键能力已经变成"如何选择工具并积累证据"，但存在以下系统性不足：

1. **数据封闭**: 工具轨迹数据通常不公开，无法被后续研究复用
2. **环境绑定**: 每个系统自建环境，难以在同一环境中对比不同策略
3. **格式碎片化**: VISOR 用 search/crop/answer，DocSeeker 用 ALR，DocCogito 用 VSC，无跨系统数据协议
4. **过程验证缺失**: 多数只验证最终答案正确性，不验证中间推理是否被证据支持
5. **拒答训练缺失**: 几乎无系统化的 unanswerable / refusal 训练数据

DocWorldTrace 旨在通过**标准化文档环境 + 统一轨迹 schema + 验证引导合成**填补上述缺口，而非提出"又一个文档 QA Agent"。

---

## 4. Related Work 定位总结

```text
DocWorldTrace 在三个维度上区别于现有工作:

1. vs 通用 Agentic Synthesis (RandomWorld, SynWorld, Simia):
   → 将通用方法论迁移到文档领域，利用文档环境的静态可缓存优势

2. vs GUI Agent 范式 (WebArena, AgentTrek, DigiRL):
   → 迁移"环境化+轨迹化+质控化"方法论，但动作空间从像素级变为语义级

3. vs 文档 Agent (VISOR, MM-Doc-R1, DocCogito):
   → 不做新 Agent 框架，而是提供可复现环境+公开轨迹+验证引导合成的基础设施
```
