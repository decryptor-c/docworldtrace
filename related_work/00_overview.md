# DocWorldTrace ICLR 防御性文献调研总览

> **调研目标**: 为 DocWorldTrace 论文 proposal 的 6 个 ICLR 审稿人可能攻击维度建立系统性文献支撑和差异化论证。
> **调研日期**: 2026-04-30
> **论文定位**: DocWorldTrace: Verification-Guided Tool-Use Trajectory Synthesis in Reproducible Document Environments

---

## 调研结构

```
iclr_defense_survey/
├── 00_overview.md            ← 本文件：索引与跨维度阅读指南
├── d1_process_reward.md      ← 维度 1: 过程级监督与 Process Reward Models
├── d2_quality_filtering.md   ← 维度 2: 数据合成中的质量控制与过滤
├── d3_faithfulness.md        ← 维度 3: 文档理解中的忠实性与幻觉控制
├── d4_tool_use.md            ← 维度 4: Tool-use / Function-calling 训练数据与方法
├── d5_env_design.md          ← 维度 5: 环境设计与交互式学习范式
└── d6_novelty_defense.md     ← 维度 6: ICLR 审稿人可能的 novelty 质疑防线
```

---

## 各维度核心发现摘要

### 维度 1: 过程级监督与 PRM (14 篇)

**核心发现**: PRM 研究正从数学推理向 Agent、代码、Web 导航、多模态等领域快速扩展。2025 年的关键趋势是：(1) 自动过程标注（无需人工）成为主流；(2) Agent PRM 重新定义"正确性"为"进度+承诺"；(3) 生成式 PRM（think-then-judge）超越判别式。DocWorldTrace 填补了文档 Agent 领域的 PRM 空白。

**关键差异化**: 利用文档环境的结构化验证信号（bbox/OCR/计算）替代 MC 采样估计，提供更低方差的 7 维过程监督。

→ [详细分析](d1_process_reward.md)

### 维度 2: 质量控制与过滤 (14 篇)

**核心发现**: "Less is More"从 LIMA 到 DEITA 到 DS² 已成为指令微调的共识性范式。但现有数据过滤方法几乎完全依赖**语义信号**（LLM 评分/梯度/embedding），无法利用领域结构信号做精确验证。DocWorldTrace 的独特性在于引入文档领域特有的结构化验证（bbox/OCR 交叉验证、compute 复算、evidence traceability）。

**关键差异化**: 五层质检从"语义猜测"升级为"证据驱动的结构化验证"；四级分级支持差异化训练策略（SFT/DPO/PRM 分集）。

→ [详细分析](d2_quality_filtering.md)

### 维度 3: 忠实性与幻觉控制 (13 篇)

**核心发现**: FActScore、FaithAct、Medical VLM Faithfulness 等工作反复验证了一个核心发现——**答案准确性和推理忠实性是解耦的**。但现有 faithfulness 工作几乎全部聚焦于**事后评估**。DocWorldTrace 将 faithfulness 验证从"评估工具"升级为"数据合成基础设施"（在生成阶段预防 unsupported reasoning）。

**关键差异化**: 从"检测幻觉"到"预防幻觉训练数据"的范式迁移；closed-domain 文档环境的 bbox/OCR 验证比开放域知识库验证更精确。

→ [详细分析](d3_faithfulness.md)

### 维度 4: Tool-use 方法 (12 篇)

**核心发现**: Tool-use 领域从 Toolformer 到 ToolLLM 到 APIGen，重心一直在"API 覆盖率"和"调用正确性"。DocWorldTrace 提出的是一个新问题——**在少量但语义丰富的专用工具空间中，通过搜索式合成找到最优工具组合路径**。这与 General API 工具工作的核心挑战不同。

**关键差异化**: 从"学会调用更多工具"到"学会在正确时机用正确工具组合积累证据"；evidence-grounded 工具策略 > API coverage。

→ [详细分析](d4_tool_use.md)

### 维度 5: 环境设计 (15 篇)

**核心发现**: 从 TextWorld 到 WebArena 到 SWE-bench，交互式 Agent 环境的设计原则已经成熟。DocEnv-lite 完整遵循了这些原则（可复现性、确定性、结构化状态、程序化评估），且利用 PDF 的环境特性（静态、可缓存、可并行）提供了无现有环境可类比的结构性优势。

**关键差异化**: 首个将 PDF 文档建模为可审计、可缓存、可并行的确定性交互环境的工作。环境的可审计性（bbox/OCR/计算验证）是文档独有的。

→ [详细分析](d5_env_design.md)

### 维度 6: Novelty 防线 (综合)

**核心发现**: 四个主要攻击方向的防御策略都已建立：

1. **"WebArena 换 domain"** → 动作空间语义层级提升（像素→语义）+ 评估维度扩展（1→7）
2. **"验证信号不新颖"** → 组合优势：多维交叉验证集成到合成 pipeline
3. **"MCTS 已被做过"** → 文档环境缓存/确定性优势使 MCTS 成本结构质变
4. **"规模太小"** → LIMA/DEITA/LESS/DS² 等 "Less is More" 共识

→ [详细分析](d6_novelty_defense.md)

---

## 跨维度交叉引用指南

### 审稿人可能的多维度组合质疑

| 组合攻击 | 涉及维度 | 防御策略 |
|---------|---------|---------|
| "PRM+过滤+环境都是已有方法，组合起来有何新意？" | D1+D2+D5 | 文档环境的结构化验证优势贯穿所有维度——它是 D1 的低方差过程信号来源、D2 的精确质控信号来源、D5 的确定性保证 |
| "为什么不直接在已有 WebArena 上加文档任务？" | D5+D6 | WebArena 的 click/type/scroll 动作空间无法表达 search→parse→compute→verify 的语义工具链 |
| "你的贡献到底是数据集还是方法？" | all | 三者统一：可复现环境 (C1) × 验证引导合成方法 (C3) × 公开轨迹数据集 (C4)。环境使方法可行，方法使数据高质量，数据使训练可复现 |
| "Generalizability 到其他文档类型如何保证？" | D4+D5 | 10 个标准化工具是文档独立的（不绑定特定 PDF）；pipeline 为 Phase 2 扩展到更多文档类型预留了接口 |

### 各维度的差异化论证共享核心逻辑

所有 6 个维度的差异化定位共享一个核心逻辑链：

```text
文档环境的静态性和结构化
  → 工具输出可缓存、可交叉验证
  → 过程信号更丰富、更精确（对比 MC 采样/LLM judge）
  → 数据质量控制从"语义猜测"升级为"证据驱动验证"
  → 小规模高质量轨迹足以产生训练增益
  → 相比 GUI/Web/通用 API 环境具有结构性优势
```

这一逻辑链是 DocWorldTrace 应对任何 novelty 质疑的核心防线。

---

## 论文统计

| 维度 | 论文数量 | 时间范围 | 核心会议覆盖 |
|:---:|:---:|------|------|
| D1: PRM | 14 | 2023-2025 | ACL, NAACL, NeurIPS, ICML, AAAI |
| D2: 质量过滤 | 14 | 2022-2025 | ICLR, ICML, COLM, NeurIPS |
| D3: 忠实性 | 13 | 2023-2025 | NeurIPS, EMNLP, ACL, IJCV |
| D4: Tool-use | 12 | 2023-2025 | ICLR, NeurIPS, ICML, ACL |
| D5: 环境设计 | 15 | 2018-2025 | ICLR, NeurIPS, CVPR, EMNLP |
| D6: Novelty | 综合 | — | 引用前 5 维度论文 |
| **总计（去重后约）** | **~70 篇** | **2022-2026** | **ICLR/NeurIPS/ICML/ACL/EMNLP/AAAI/CVPR** |

---

## 使用建议

1. **撰写 Related Work**: 从各维度选取 3-5 篇最相关的论文，按"现有方法 → 不足 → DocWorldTrace 差异化"三段式组织
2. **撰写 Introduction**: 使用 D3（faithfulness gap）、D5（环境不可复现）、D1（过程监督缺失）的文献建立 motivation
3. **撰写 Method**: 引用 D1（PRM 设计参考）、D2（质控体系参考）、D4（工具空间设计参考）的具体方法
4. **回应审稿人**: D6 提供每个 novelty 质疑的逐条防御策略 + 引用支撑
5. **投稿策略**: ICLR 审稿人特别关注 novelty 和 generalizability——D6 的四个防线是首要准备内容

---

## 与现有 Related Work 的关系

本调研定位为**补充性调研**，聚焦于现有 [02_related_work.md](./02_related_work.md) 尚未覆盖的 6 个审稿人攻击维度。已覆盖的三个方向（通用 Agentic Synthesis、GUI Agent 范式、文档 Agent 系统）不在本次调研范围内。

最终论文的 Related Work 应融合两者，形成"已有方向 + 防御维度"的完整文献矩阵。
