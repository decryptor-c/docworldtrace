# Q1: DocWorldTrace 数据集必要性论证

> **核心 Claim**: 相比于当前主流的 agentic RL 范式（在 answer-only 或简单 ReAct 数据上做 GRPO/SPO），高质量的结构化工具轨迹数据 + 验证引导过滤是必要且更优的训练数据形态。

---

## 1. Agentic RL 的数据依赖瓶颈

### 1.1 当前 agentic RL 的冷启动问题

DeepSeek-R1 (Guo et al., Jan 2025) 确立了两阶段训练范式：

```
Stage 1 (Cold Start SFT): 数千条高质量 long-CoT 样本
    → 强制可读格式，防止早期 RL 不稳定
Stage 2 (RL): GRPO + rule-based rewards (正确性 + 格式 + 语言一致性)
    → 在推理任务上训练至收敛
```

**关键发现**: R1-Zero（无冷启动 SFT）虽然展现了强推理能力，但存在**可读性差、语言混用、格式混乱**三个严重问题。这直接证明了：即使在数学推理领域（有 ground-truth reward），RL 仍然需要**结构化冷启动数据**。

将此结论迁移到文档推理场景：

| 维度 | 数学推理 | 文档推理 |
|------|---------|---------|
| Reward 信号 | 答案二元正确性 | 答案 + 证据支持 + grounding + 充分性 + 工具效率 |
| 冷启动需求 | CoT 格式模板 | **工具调用格式 + 证据积累路径 + 工具选择策略** |
| 无初始数据的 RL | R1-Zero 勉强可行 | **基本不可行**（动作空间对模型完全陌生） |
| reward sparsity | 部分样本有正 reward | **极稀疏**（需所有维度同时达标才得正 reward） |

**结论**: 文档推理的 RL 冷启动问题比数学推理严重得多——没有工具轨迹示范，模型甚至不知道如何调用 `search/parse_table/compute`。

### 1.2 现有文档 Agent 的数据依赖

调研现有文档 Agent 系统揭示了明确的隐式轨迹依赖：

| 系统 | RL 方法 | 冷启动数据 | 轨迹公开 | 数据形态 |
|------|--------|----------|:---:|------|
| **MM-Doc-R1** | SPO (Similarity-based Policy Optimization) | Teacher 生成的多步工具轨迹（Planner→Seeker→Answer） | ✗ | **隐式依赖完整工具轨迹** |
| **VISOR** | GRPO + visual action eval | 声称 RL，但工具空间（search/crop/answer）需要轨迹示范 | ✗ | **隐式依赖** |
| **DocSeeker** | evidence-aware GRPO | ALR (Analysis-Localization-Reasoning) 三阶段格式需要示范轨迹 | ✗ | **隐式依赖** |
| **DocCogito** | 闭源 VLM 蒸馏 | 蒸馏需要 teacher 的工具操作序列 | ✗ | **隐式依赖** |

**关键洞察**: 这些系统在论文中声称"用 RL 训练了开放模型"，但它们的 RL 训练都依赖闭源 teacher（GPT-4o/Gemini）生成的轨迹作为冷启动。这些轨迹**不公开**，导致：

1. 后续研究者无法复现训练过程
2. 每个新系统从零重新蒸馏 teacher 轨迹
3. 无法公平对比不同 RL 方法的收益（轨迹质量差异混淆了方法比较）

SPO (MM-Doc-R1) 对 GRPO 的改进（+5-6%）本质上是在**更好的轨迹相似度 baseline 估计**上做 RL——这进一步证明：轨迹数据的质量直接影响 RL 稳定性。

### 1.3 Answer-only 数据能否支撑 RL？

**理论分析**: RLVR (RL with Verifiable Rewards) 在数学推理中只需要 answer correctness 作为 reward，模型能在探索中自我发现推理策略。但这一机制成立的前提是：

1. **动作空间对模型已知**: 数学推理的动作是"思考下一个 token"——模型在预训练中已大量学习
2. **Reward 信号密度足够**: 至少部分样本能得到正 reward

文档推理不满足这两个前提：

| 前提条件 | 数学推理 | 文档推理 |
|---------|---------|---------|
| 动作空间是否已知 | ✓（语言 token 生成） | ✗（search/crop/parse_table/compute 是陌生的函数调用形式） |
| Reward 密度 | 中等（部分样本偶然做对） | 极低（随机工具调用极难碰巧正确） |
| 探索空间 | 连续语义空间 | 离散工具+参数的组合爆炸 |
| 中间步骤验证 | 不可验证（纯语言推理） | **可验证**（bbox/OCR/计算可交叉验证） |

**实证证据**: R1-VL (StepGRPO, Zhang et al., Mar 2025) 发现——当仅用 outcome-level reward 在 MLLM 上做 GRPO 时，大多数轨迹得到全零 reward，训练极度不稳定。这直接支持：**在弱模型+复杂动作空间的组合下，纯 outcome reward 无法支撑 RL**。R1-VL 通过 step-wise rule-based rewards（StepRAR + StepRVR）才稳定了训练——而这恰恰是 DocWorldTrace 七维 per-step reward 提供的价值。

**VLAA-Thinking (TMLR 2025)** 进一步发现：SFT 仅用 answer-only 数据训练的模型产生 **"pseudo reasoning paths"**——看起来像推理但包含错误步骤的模仿性思维链。这直接支撑 DocWorldTrace 的 claim：过程级验证信号是防止"伪推理"进入训练数据的必要条件。

---

## 2. 轨迹数据的不可替代性论证

### 2.1 轨迹数据 vs Answer-only 数据：能力维度对比

| 训练目标 | Answer-only 数据 | 完整工具轨迹 | 文献支撑 |
|---------|:---:|:---:|------|
| **答案正确性** | ✓（可训练） | ✓ | 无需轨迹 |
| **工具选择策略** | ✗（无工具信号） | ✓（每步 tool choice 可见） | ToolLLM, APIGen |
| **证据逐步积累** | ✗（无中间状态） | ✓（evidence_memory 增量更新） | EviPath (NeurIPS 2025) |
| **充分性判断** | ✗（不知何时该继续/停止） | ✓（sufficiency reward at answer step） | DocVerify++ 独有 |
| **拒答决策** | ✗（无 refusal 信号） | ✓（refusal F1 + sufficiency） | 无现有工作 |
| **过程忠实性** | ✗（不能验证推理来源） | ✓（evidence_refs + provenance） | FaithAct, KIE-HVQA |
| **工具参数正确性** | ✗（无参数信号） | ✓（bbox 验证 + compute 复算） | APIGen execution verification |
| **效率优化** | ✗（无步骤信号） | ✓（efficiency reward） | AgentPRM |

**核心论点**: Answer-only 数据至多能训练前 1 个能力（答案正确性）。其余 7 个能力——正是文档 Agent 区别于通用 QA 模型的**核心差异化能力**——必须依赖完整工具轨迹数据。

### 2.2 PRM vs ORM 的训练效果差异

最新 2024-2025 研究为过程监督 vs 结果监督提供了关键证据：

**正面证据（PRM > ORM）**:

| 论文 | 发现 | 与 DocWorldTrace 关联 |
|------|------|---------------------|
| Snell et al. (ICLR 2025) | PRM-guided search 4× 效率 > best-of-N；小模型 + PRM search 可超越 14× 大模型 | DocWorldTrace 的 7 维 per-step reward 可用于训练 PRM |
| Setlur et al. (ICLR 2025) | Process Advantage Verifiers (PAVs) 比 ORM 准确 8%+，**1.5-5× 计算效率** | 支持 DocWorldTrace 的 per-step evidence_gain 设计 |
| StepGRPO / R1-VL (2025) | Step-wise rewards 显著稳定 MLLM 的 GRPO 训练 | 直接支持七维 per-step reward 的必要性 |
| ProRAG (2025) | 过程监督 RL 在复杂长程 Agent RAG 任务上优于结果监督 | 文档推理正是长程 Agent RAG |

**负面/谨慎证据**:

| 论文 | 发现 | 对 DocWorldTrace 的警示 |
|------|------|----------------------|
| Gao et al. (2024) | 训练好的 PRM 可能通过 reward hacking **损害** RL 训练 | 需要 Clipping/Delta 机制；DocWorldTrace 的规则化验证（非模型判断）可能天然抗 hacking |
| Lee et al. (2025) | PRM 优势在多领域任务中**消失**甚至反转（gORM 最鲁棒） | 文档领域的封闭性（限定 PDF 内验证）可能使 PRM 更可靠 |
| Yuan et al. (2024) | Implicit PRM（从 outcome label 推导）匹敌显式 PRM，**38× 数据效率** | DocWorldTrace 需要证明显式多维 reward > implicit reward |

### 2.3 轨迹数据的实证优势

目前缺少文档领域的直接 SFT vs RL 对比，但从 VLAA-Thinking 和 RL-with-Cold-Start 的结果可推断：

- **SFT 学到的是"格式"** — 模型模仿 CoT 格式但不一定理解工具选择逻辑
- **RL 学到的是"策略"** — 模型在 reward 引导下探索更优的工具路径
- **SFT + RL 最优** — 冷启动 SFT 提供格式和基础策略，RL 在探索中优化

这暗示 DocWorldTrace 的最佳训练方案是：**DocWorldTrace Gold 轨迹做冷启动 SFT → 然后在 DocEnv 中做 RL（用七维 reward）**。这一路径的价值在于：冷启动数据的质量远高于单纯的 answer-only CoT。

---

## 3. "高质量"的增量价值

### 3.1 数据质量 vs 数据规模的文献共识

"Less is More" 已成为指令微调的共识性发现：

| 论文 | 数据规模 | 性能 | 关键发现 |
|------|:---:|------|---------|
| LIMA (2023) | **1,000** 精选 | 匹敌 GPT-4（43% 人类偏好） | 模型知识来自预训练，微调只需学习交互格式 |
| DEITA (ICLR 2024) | **6,000** 自动筛选 | 7.55 MT-Bench（10× 更少） | Complexity × Quality × Diversity 三维度 = 最优 |
| LESS (ICML 2024) | **5% 数据**（梯度筛选） | 超越全量 100% | 梯度相似度选择 > 语义选择 |
| DS² (2024) | **3.3% 数据**（1K） | 1K = 300K 全量 | Score transition matrix 校正是关键 |

这些工作的共同启示：**当质量信号足够精确时，1K-3K 的高质量数据可以匹敌甚至超越 100K+ 的噪声数据**。

### 3.2 Verification-guided Synthesis 在数学/代码领域的证据

| 论文 | 验证机制 | 合成效果 | 对文档领域的迁移 |
|------|---------|---------|---------------|
| rStar-Math (ICML 2025) | 代码执行验证 | Qwen-7B 从 58.8% → 90.0% MATH | 代码执行=文档工具执行的类比 |
| Loong (2025) | RLVR + code-executed verification | 8,729 样本跨 12 领域 | Verifier-guided CoT synthesis 的可行性 |
| ORPS (ICML 2025) | Execution + self-critique | +26.9% correctness, +42.2% efficiency | 执行反馈 + self-critique 的协同 |

**迁移逻辑**: 数学/代码领域通过"执行验证"实现了高质量合成数据的规模化。文档领域可以通过"文档工具执行 + bbox/OCR 交叉验证 + compute 复算"实现类似的高质量合成——且文档工具的验证信号比代码执行更丰富（不仅仅是 pass/fail）。

### 3.3 DocVerify++ 过滤的增量价值

现有 filtering 方法（DEITA/LESS）纯依赖语义信号（LLM 评分/梯度）。DocVerify++ 的过程级过滤提供了独特的增量：

1. **规则验证**不可作弊（bbox 是否在页面内、compute 结果是否可复算——这些是 zero-variance ground truth）
2. **交叉验证**对抗 hallucination（OCR 文本 vs crop 图像中的文本、parse_table 结果 vs 原始文档值）
3. **过程验证**预防"伪推理"（即使答案正确，中间推理无证据支撑也会被降级）

这些是纯语义过滤器（DEITA Quality Scorer / LLM-as-judge）无法提供的信号。文档领域的独特性在于：这些验证信号的 ground truth 就存在于 PDF 本身（OCR 文本、bbox 坐标、表格数值），不需要外部知识库。

---

## 4. 反事实分析：未做 DocWorldTrace 的困境

### 4.1 "开源 RL 蒸馏悖论"的严重程度

文献调查量化了当前文档 Agent 领域的不可复现程度：

| 系统 | 轨迹数据公开 | 环境代码公开 | Teacher 模型 | 可复现等级 |
|------|:---:|:---:|------|:---:|
| VISOR | ✗ | ✗ | GPT-4o | **完全不可复现** |
| MM-Doc-R1 | ✗ | ✗ | Gemini (推测) | **完全不可复现** |
| DocSeeker | ✗ | ✗ | GPT-4o | **完全不可复现** |
| DocCogito | ✗ | ✗ | 闭源 VLM | **完全不可复现** |
| MDocAgent | ✗ | ✗ | GPT-4V | **完全不可复现** |
| DocLens | — | ✓（部分） | — | Training-free（无训练数据需求） |

**严重程度**: 5/6 的主要文档 Agent 系统**完全不可复现**，唯一可复现的是 training-free 方法。对比 GUI Agent 领域（WebArena Docker 环境开放、AgentTrek 轨迹公开），文档 Agent 领域的开放性严重滞后。

### 4.2 当前研究者的事实困境

如果不做 DocWorldTrace，研究者面临的选择：

1. **从零蒸馏 Teacher 轨迹**: 用 GPT-4o/Gemini 生成工具轨迹 → 每条 $0.10-0.30 × 数万条 = **数千美元成本** + **不可复现的闭源依赖**
2. **在 answer-only 数据上直接做 RL**: 如前述分析，冷启动极度困难，reward sparsity 致命
3. **用 LLM 自生成轨迹**: 不经过 DocEnv 真实执行，工具输出是 LLM 幻觉的，训练出的 Agent 会学习错误的工具反馈
4. **放弃工具轨迹**: 退化为纯 RAG/CoT 方法，丧失文档 Agent 的工具选择+证据积累+拒答等核心能力

**DocWorldTrace 解决了什么？** 不是"创造了一个新任务"，而是**打破了一个结构性瓶颈**——使后续研究者可以在公开环境 + 公开轨迹的基础上进行可复现研究，而不必每人重新支付数千美元的闭源蒸馏成本。

### 4.3 反事实分析框架

```text
如果没有 DocWorldTrace:
  研究者 A → 自建环境 → 蒸馏 GPT-4o 轨迹 → 训练 → 不公开
  研究者 B → 自建环境 → 蒸馏 Gemini 轨迹 → 训练 → 不公开
  研究者 C → 自建环境 → 蒸馏 GPT-4o 轨迹 → 训练 → 不公开
  → 三个环境不可互操作、三组轨迹不可对比、三组结论不可复现
  → 领域整体进展速度被"重复造轮子"拖慢

有了 DocWorldTrace:
  研究者 A → DocEnv-lite → DocWorldTrace SFT → DocEnv RL → 公开结果
  研究者 B → DocEnv-lite → 自己的 Agent 策略 → 在同一环境评测
  研究者 C → 基于 DocWorldTrace 数据做 SFT → 在自己任务上做 domain adaptation
  → 环境互操作、数据可复用、结果可复现
  → 领域加速迭代
```

---

## 5. 综合论证框架

### 5.1 论证逻辑链

```text
1. Agentic RL 需要冷启动数据（DeepSeek-R1 范式）
   ↓
2. 文档推理的冷启动需求远大于数学推理（陌生动作空间 + 极稀疏 reward）
   ↓
3. Answer-only 数据无法满足冷启动需求（缺乏工具调用/证据积累/充分性信号）
   ↓
4. 完整工具轨迹数据是必要的数据形态（覆盖 7 维度能力）
   ↓
5. 但现有文档 Agent 系统均不公开轨迹数据（"开源 RL 蒸馏悖论"）
   ↓
6. 因此需要 DocWorldTrace — 公开的、验证引导合成的高质量工具轨迹数据集
   ↓
7. "高质量"通过 DocVerify++ 的结构化验证保证（比语义过滤更精确）
   ↓
8. 小规模（1K-3K）+ 高质量 > 大规模 + 噪声数据（LIMA/DEITA 共识）
```

### 5.2 薄弱环节与需要补强的实证

| 薄弱环节 | 风险 | 补强方向 |
|---------|------|---------|
| **轨迹 vs Answer-only 的因果证据** | 缺少文档领域的直接对照实验 | Pilot 实验必须包含：同一基座模型在 answer-only SFT vs DocWorldTrace SFT 上的完整对比 |
| **Implicit PRM 可能匹敌显式多维 reward** | Yuan et al. (2024) 发现 implicit PRM 38× 更高效 | 需要对比：DocWorldTrace 的七维 reward vs 简单的 answer correctness + 隐式 PRM |
| **高质量过滤的 precision 未经验证** | DocVerify++-lite 的 precision 可能 <80% | 必须用人工审核建立 ground-truth precision/recall |
| **1K-3K 是否真的足够** | LIMA/DEITA 的结论来自通用指令微调，非工具轨迹 | 需设计数据量消融实验（500 / 1K / 3K / 10K） |
| **文档类型的泛化性** | Pilot 仅 arXiv + SEC，其他文档类型未知 | 需在至少 3 种文档类型上验证 |

### 5.3 关键文献支撑索引

- [DeepSeek-R1 (2025)](https://arxiv.org/abs/2501.12948) — Cold start + multi-stage RL 范式
- [MM-Doc-R1 (2026)](https://arxiv.org/abs/2604.13579) — SPO 改进 GRPO；隐式轨迹依赖
- [R1-VL / StepGRPO (2025)](https://arxiv.org/abs/2503.12937) — Step-wise reward 稳定 MLLM RL
- [VLAA-Thinking (TMLR 2025)](https://ucsc-vlaa.github.io/VLAA-Thinking/) — SFT 产生 pseudo reasoning；RL 优于 SFT
- [SFT or RL for LVLMs (2025)](https://arxiv.org/abs/2505.22334) — SFT + GRPO > SFT-only/RL-only
- Snell et al. (ICLR 2025) — PRM search 4× 效率；小模型+验证超越大模型
- Setlur et al. (ICLR 2025) — PAVs 1.5-5× 计算效率优于 ORM
- LIMA (2023) / DEITA (ICLR 2024) / LESS (ICML 2024) / DS² (2024) — Less is More 共识
- rStar-Math (ICML 2025) / Loong (2025) / ORPS (ICML 2025) — Verification-guided synthesis
- ProRAG (2025) — 过程监督在 Agent RAG 中胜出
- Gao et al. (2024) — PRM reward hacking 风险
- Lee et al. (2025) — PRM 在多领域中的局限性
