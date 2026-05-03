# 维度 1：过程级监督与 Process Reward Models

> **审稿人可能攻击点**: DocWorldTrace 的七维 reward 和 per-step PRM 信号是否有理论和方法的扎实支撑？PRM 是否仅在数学推理有效，迁移到文档 Agent 领域是否成立？

---

## 1. 维度概述

DocWorldTrace 使用七维 reward 信号（R_answer / R_support / R_ground / R_suff / R_eff / R_refuse / R_tool）和 per-step PRM 信号（evidence_gain + tool_appropriateness - redundancy_penalty）进行过程级监督。这需要在以下方向找到文献支撑：

- PRM vs Outcome RM (ORM) 的理论对比
- 自动化过程标注方法（无人工标注）
- PRM 从数学推理向非数学领域（Agent、代码、Web 导航）的扩展
- Step-level supervision 的最新 benchmarks 和评估体系

---

## 2. 代表性论文

### 2.1 PRM 奠基与自动化标注

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 1 | **Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations** (Wang et al.) | ACL 2024 | 提出自动过程标注方法：通过 continuation sampling（Hard Estimation / Soft Estimation）对中间步骤打分，无需人工标注；在 DeepSeek-67B 上 MATH 达 48.1% | **自动化标注范式**：DocWorldTrace 的 per-step evidence_gain 评分可类比 Math-Shepherd 的 MC 估计，但我们用 DocVerify++ 的结构化验证替代 MC 采样 |
| 2 | **AutoPRM: Automating Procedural Supervision for Multi-Step Reasoning via Controllable Question Decomposition** (Chen et al.) | NAACL 2024 | 将复杂问题分解为子问题，用 RL 迭代改进子问题求解器；强调分解粒度可控 | **分解思路**：DocWorldTrace 的 claim decomposition → evidence retrieval → support judgment 与 AutoPRM 的问题分解共享"层次化监督"思想 |
| 3 | **OmegaPRM: Improve Mathematical Reasoning by Automated Process Supervision** (Luo et al., Google DeepMind) | arXiv 2024.06 | 使用 MCTS + Binary Search 自动定位推理链中的首个错误步骤，收集 1.5M+ 过程监督标注；Gemini Pro MATH 从 51% → 69.4% | **错误定位**：DocWorldTrace 的 failure taxonomy（retrieval_miss, bbox_wrong, unsupported_claim）本质上是文档领域的"first error localization" |

### 2.2 PRM 基准与评估

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 4 | **PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models** (Song et al.) | ACL 2025 | 6,216 问题，83,456 step-level 标注，评估 simplicity / soundness / sensitivity 三维度；揭示现有 PRM 在细粒度错误检测上的系统性问题 | **评估体系参考**：DocWorldTrace 的 5 层质量检查体系需要类似 PRMBench 的系统性验证框架 |
| 5 | **ProcessBench** (Zheng et al.) | 2024 | 评估 PRM 识别数学推理中错误步骤的能力；发现 PRM 难以泛化到 GSM8K/MATH 之外的更难数学题 | **泛化警示**：DocWorldTrace 需要验证 PRM 信号在文档领域（非数学）的有效性 |
| 6 | **Socratic-PRMBench** (Li et al.) | arXiv 2025.05 | 2,995 条推理路径，覆盖 6 种推理模式（Transformation, Decomposition, Regather, Deduction, Verification, Integration）；Qwen2.5-Math-PRM 仅 68.0 | **多模式覆盖**：文档推理涉及 search → read → crop → parse → compute → verify 多工具模式，需考虑不平衡性 |
| 7 | **PRM-BiasBench** (Bamba et al.) | ICML 2025 | 增强 ProcessBench，加入 8 种扰动类型测试 PRM 鲁棒性；发现 PRM 在流畅但逻辑错误的轨迹上失效 | **鲁棒性**：DocWorldTrace 的 DocVerify++-lite 需要抵抗"格式正确但证据不匹配"的假阳性 |

### 2.3 PRM 向非数学领域的扩展（核心论证支撑）

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 8 | **Web-Shepherd: Advancing PRMs for Reinforcing Web Agents** (Chae et al.) | NeurIPS 2025 | **首个 Web Agent PRM**：构建 WebPRM Collection (40K step-level preference pairs)；在 WebArena-lite 上 +10.9 点，10× 更低成本 | **最直接的相关工作**：证明了 PRM 从数学扩展到 Agent 领域的可行性；DocWorldTrace 将其扩展到文档 Agent |
| 9 | **AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress** (Xi et al.) | arXiv 2025.11 | 重新定义 Agent PRM：不按二元正确性打分，而按"目标接近度 + 进展"评分；使用 TD + GAE 做样本高效标注；8× 计算效率提升 | **打分哲学**：DocWorldTrace 的 evidence_gain + tool_appropriateness 与 AgentPRM 的"promise + progress"高度一致 |
| 10 | **PRInTS: Reward Modeling for Long-Horizon Information Seeking** (Lee, Prasad et al.) | arXiv 2025.11 | 生成式 PRM，双能力：密集多维评分 + 轨迹摘要；在 FRAMES/GAIA 上 +9.3%；仅需 1-2K 训练样本 | **信息寻求场景**：文档 Agent 本质是信息寻求，PRInTS 的 multi-dimensional scoring（information gain, tool output interpretation）与 DocWorldTrace 重叠度高 |
| 11 | **Process Supervision-Guided Policy Optimization for Code Generation** (Dai et al.) | arXiv 2024.10 | PRM 提供代码的**行级反馈**；使用 binary search 定位首错行；长时序代码任务上 +1.6-4.0% | **代码→文档**：将代码的行级监督迁移为文档的 step 级监督 |
| 12 | **Process Reward Models for LLM Agents: Practical Framework and Directions** (Choudhury) | arXiv 2025.02 | 系统化 Agent PRM 框架：AgentPRM（actor-critic + MC rollouts）+ InversePRM（无需 outcome label）；3B PRM 超越 GPT-4o | **框架参考**：为 DocWorldTrace 的 PRM 设计提供工程蓝图 |

### 2.4 PRM 综述与趋势

| # | 论文 | 会议/年份 | 核心贡献 |
|---|------|----------|---------|
| 13 | **A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for LLMs** (Zheng et al.) | arXiv 2025.10 | 全面综述 PRM pipeline：数据生成 → 模型架构 → 使用方法 → 跨域应用（数学/代码/多模态/机器人/Agent） |
| 14 | **Enhancing LLM Reasoning with Reward Models: An Analytical Survey** (Liu et al.) | 2025 | ORM 与 PRM 对比分析，覆盖 RL 训练阶段使用 |

---

## 3. 与 DocWorldTrace 的关联分析

### 3.1 自动化标注的继承与创新

Math-Shepherd/OmegaPRM 的核心贡献是**无需人工标注的过程监督**。DocWorldTrace 继承这一范式，但有以下关键差异：

- **标注源不同**: Math-Shepherd 用 MC 采样、OmegaPRM 用 MCTS+Binary Search；DocWorldTrace 用 **DocVerify++ 结构化验证**（claim-evidence-support/sufficiency），信号来源更丰富
- **标注粒度不同**: 数学 PRM 给"推理正确性"打分；DocWorldTrace 给 7 个正交维度打分，解耦了答案正确性、证据支持性和工具效率
- **标注可信度不同**: 数学 PRM 依赖 MC 估计（有方差）；DocWorldTrace 的证据支撑性来自文档 OCR 交叉验证和 bbox 验证，更接近 ground truth

### 3.2 Agent PRM 的定位

Web-Shepherd、AgentPRM、PRInTS 是 2025 年最相关的工作，它们共同确立了 **PRM 可以用于非数学的 Agent 场景**。DocWorldTrace 的定位是：**首个面向文档 Agent 的 PRM 信号体系**，补充了 Web Agent PRM（Web-Shepherd）和通用 Agent PRM（AgentPRM）之间的空白。

### 3.3 PRM 鲁棒性挑战

PRMBench 和 PRM-BiasBench 揭示了 PRM 的系统性弱点（对流畅但错误的轨迹误判）。这恰恰强化了 DocWorldTrace 使用 **结构化验证**（而非纯模型判断）的动机：DocVerify++ 的 bbox 验证、OCR 交叉验证、compute 复算等规则化检查，可以弥补纯模型 PRM 的鲁棒性缺陷。

---

## 4. DocWorldTrace 的差异化定位

| 对比维度 | 数学 PRM (Math-Shepherd/OmegaPRM) | Agent PRM (Web-Shepherd/AgentPRM) | **DocWorldTrace PRM** |
|---------|----------------------------------|-----------------------------------|----------------------|
| 领域 | 数学推理 | Web/GUI Agent | **文档 Agent** |
| 过程信号来源 | MC 采样 / Binary Search | Promise + Progress / TD | **DocVerify++ 结构化验证 (claim-evidence)** |
| 信号维度 | 1 维（步骤正确性） | 1-2 维（进度+效率） | **7 维（answer/support/ground/suff/eff/refuse/tool）** |
| 标注自动化 | MC 估计（有方差） | TD+GAE (样本高效) | **规则+执行+证据交叉验证（低方差）** |
| 可审计性 | 低（模型判断） | 低（模型判断） | **高（provenance bbox/OCR/计算机可复算）** |
| 拒答/充分性 | 无 | 无 | **独有（sufficiency reward + unanswerable）** |

**核心差异化论点**: DocWorldTrace 的 PRM 不是在数学 PRM 上做"又一个 Agent 扩展"，而是利用文档环境的结构化优势（静态 PDF、可缓存工具输出、bbox/OCR 可审计），构建了**比通用 Agent PRM 更丰富、更可验证的多维过程信号体系**。这是文档领域独有的结构性优势。

---

## 5. 审稿人防御话术

> **Q: "PRM 已经在 Math-Shepherd/OmegaPRM 中被充分探索，你们的 per-step reward 有何新意？"**

A: 我们的贡献不在提出 PRM 的概念，而在 (1) 将 PRM 从数学扩展到文档 Agent 这一未覆盖领域；(2) 用 DocVerify++ 的结构化验证信号（bbox/OCR/计算验证）替代 MC 估计，提供更低方差的过程监督；(3) 提出 7 维解耦 reward 体系，包含现有 PRM 不支持的 sufficiency 和 refusal 维度，这对安全部署至关重要。

> **Q: "为什么不在数学领域验证你的 PRM，而要做一个新领域？"**

A: 文档 Agent 的场景特性——静态环境、可缓存工具输出、多证据源交叉验证——使得过程信号天然比数学推理更丰富、更可靠。数学推理的正确性只有最终答案一个 ground truth；文档推理的过程正确性（证据是否被检索到、bbox 是否正确、计算是否可复算）每一步都有可验证信号。这种结构性优势使得文档 Agent 是验证 PRM 价值的理想试验场。

---

## 6. 参考文献索引

- [Math-Shepherd (ACL 2024)](https://aclanthology.org/2024.acl-long.510/)
- [AutoPRM (NAACL 2024)](https://aclanthology.org/2024.naacl-long.73/)
- [OmegaPRM (arXiv 2024)](https://arxiv.org/abs/2406.06592)
- [PRMBench (ACL 2025)](https://aclanthology.org/2025.acl-long.1230/)
- [GroundedPRM (NeurIPS 2025)](https://neurips.cc/virtual/2025/loc/san-diego/124511)
- [Web-Shepherd (NeurIPS 2025)](https://neurips.cc/virtual/2025/loc/san-diego/118996)
- [AgentPRM (arXiv 2025)](https://arxiv.org/abs/2511.08325)
- [PRInTS (arXiv 2025)](https://arxiv.org/abs/2511.19314)
- [PRM for LLM Agents Framework (arXiv 2025)](https://arxiv.org/abs/2502.10325)
- [PRM Survey (arXiv 2025)](https://arxiv.org/abs/2510.08049)
- [Process Supervision for Code Generation (arXiv 2024)](https://arxiv.org/abs/2410.17621)
- [SPARE (2025)](https://api.scienceopen.com/document?vid=6d18f4bc-ff3d-44ab-8667-2854fd14e01d)
