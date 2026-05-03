# 维度 2：数据合成中的质量控制与过滤

> **审稿人可能攻击点**: DocWorldTrace 的"五层质检 + 四级分级"是否足够新颖？现有的 RLHF/DPO 数据质量、SFT 数据过滤和合成数据质控方法已经非常成熟，你们的 filtering 有何增量贡献？

---

## 1. 维度概述

DocWorldTrace 的 Verification-guided filtering 包含五层质量检查（格式→执行→答案→证据→过程）和四级轨迹分级（Gold/Silver/Bronze/Negative）。这需要在以下方向找到文献对标：

- RLHF/DPO 偏好数据质量控制
- SFT 数据去噪与过滤方法
- 合成数据的 self-consistency / reject sampling / quality scoring
- "少即是多"数据效率研究

---

## 2. 代表性论文

### 2.1 指令微调数据选择方法

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 1 | **DEITA: What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning** (Liu et al.) | ICLR 2024 | 三维度自动数据选择：Complexity (Evol Complexity)、Quality (Evol Quality)、Diversity (Repr Filter)；6K SFT 样本即达 SOTA（10× 数据减少） | **质量度量框架**：DEITA 的 Complexity-Quality-Diversity 三维度与 DocWorldTrace 的质量分级思想一致，但我们增加了 evidence support 和 process validity 两个文档特有维度 |
| 2 | **LESS: Selecting Influential Data for Targeted Instruction Tuning** (Xia et al.) | ICML 2024 | 基于梯度相似度的优化器感知数据选择；用 5% 数据超越全量训练；可跨模型迁移 | **影响力选择**：DocWorldTrace 的四级分级（Gold→Silver→Bronze→Negative）也是一种影响力排序，但依据是文档证据支撑而非梯度 |
| 3 | **AlpaGasus: Training a Better Alpaca with Fewer Data** (Chen et al.) | ICLR 2024 | 基于质量评分的过滤 + 更少数据训练更强模型 | **质量过滤训练**：为 DocWorldTrace 的"过滤后轨迹优于全量轨迹"假设提供直接证据 |
| 4 | **Self-Guided Data Selection for Instruction Tuning** (Li et al.) | NAACL 2024 | 用模型自身评分选择和过滤高质量指令微调样本 | **自引导过滤**：DocVerify++-lite 的在线质检可类比为"verifier-guided data selection" |

### 2.2 RLHF/DPO 偏好数据质量

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 5 | **R.I.P.: Better Models by Survival of the Fittest Prompts** (Meta/FAIR) | ICML 2025 | 从 prompt 层面过滤：低质量 prompt 产生高方差低质量响应；基于 rejected response quality 和 reward gap 过滤；Llama 3.1-8B 上 +9.4% AlpacaEval2 | **Prompt 质量视角**：DocWorldTrace 的种子任务质量直接影响轨迹质量，R.I.P. 的过滤逻辑可迁移到种子任务筛选 |
| 6 | **Constitutional AI: Harmlessness from AI Feedback** (Bai et al.) | 2023 | 用 AI 反馈替代人类反馈做 RLHF；监督信号通过修订（revision）而非二元偏好获得 | **反馈范式**：DocVerify++ 的 support/sufficiency 反馈与 Constitutional AI 的"修订式反馈"思路一致——指出具体问题而非仅给出分数 |
| 7 | **Direct Preference Optimization** (Rafailov et al.) | NeurIPS 2024 | 跳过显式 reward model，直接从偏好数据优化策略 | **DPO 连接**：DocWorldTrace 的 Gold vs Negative 轨迹对天然适合 DPO 训练 |

### 2.3 合成数据质量控制

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 8 | **GDR: Generative Data Refinement — Just Ask for Better Data** (Google DeepMind) | arXiv 2025.09 | 不丢弃脏数据，而是用 LLM 重写净化（保留有用知识）；在代码匿名化和对话脱毒上超越传统丢弃方法 | **精炼 vs 丢弃**：DocWorldTrace 的部分 Bronze 轨迹可通过 Hard Negative 修正升级为 Silver，而非简单丢弃 |
| 9 | **BARE: Base-Refine** (UC Berkeley) | 2025 | 两阶段 pipeline：Base 模型生成多样性输出 → Instruct 模型精炼质量；解决合成数据的 diversity collapse | **多样性保证**：DocWorldTrace 的多源采样（Rule + Teacher + MCTS）与 BARE 的 Base+Instruct 共享"多源→精炼"逻辑 |
| 10 | **MAG-V: Multi-Agent Framework for Synthetic Data Generation and Verification** (Sengupta et al.) | arXiv 2024.11 | 多 Agent 生成+验证框架；trajectory verification 准确率超越 GPT-4o judge 11% | **验证框架**：DocWorldTrace 的 verify action 和 DocVerify++ 可类比 MAG-V 的 verification agent |
| 11 | **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (Wang et al.) | ICLR 2023 | 采样多条推理路径取多数投票；首次系统证明 self-consistency 的价值 | **一致性信号**：DocWorldTrace 的多源采样（同一问题出多条轨迹）可以实现 cross-trajectory consistency check |

### 2.4 质量评分与数据效率

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 12 | **DS²: Diversity-aware Score Curation** | 2024 | 用 score transition matrix 校正 LLM 质量评分 + diversity promotion；3.3% 数据匹配 100% 性能 | **评分校准**：DocWorldTrace 的 Q = ΣwᵢRᵢ 综合评分需要考虑维度间校准（类似 transition matrix） |
| 13 | **Surveying the Effects of Quality, Diversity, and Complexity in Synthetic Data from LLMs** (Havrilla et al.) | arXiv 2024.12 | 系统化调查合成数据中 Quality/Diversity/Complexity 三个维度对下游性能的独立影响 | **维度解耦**：为 DocWorldTrace 的七维解耦 reward 提供方法论支撑 |
| 14 | **Best Practices and Lessons Learned on Synthetic Data** (Liu, Wei, Zhou et al.) | COLM 2024 | 来自实践者的合成数据质量指南；强调数据验证和迭代精炼的重要性 | **实践验证**：支持 DocWorldTrace 的多轮过滤 + 人工抽检策略 |

---

## 3. 与 DocWorldTrace 的关联分析

### 3.1 "五层质检"的理论定位

现有数据过滤方法主要在**语义层**操作（DEITA 的 Quality/Complexity/Diversity，LESS 的梯度相似度）。DocWorldTrace 的五层质检扩展了过滤维度：

| 层级 | DocWorldTrace | 对标方法 | DocWorldTrace 的增量 |
|------|--------------|---------|---------------------|
| L1 格式 | action 合法性、ReAct 完整性 | 基础格式校验 | 标准化工具 schema 验证 |
| L2 执行 | observation 来源真实性、缓存一致性 | — | **独有**：确保执行 trace 可审计 |
| L3 答案 | EM/F1/ANLS vs reference | DEITA Quality | 标准方法 |
| L4 证据 | bbox validity、OCR 交叉验证、compute 复算 | — | **独有**：文档特有的结构化验证 |
| L5 过程 | DocVerify++-lite 的 evidence support + sufficiency | — | **独有**：过程级证据支撑判断 |

**关键增量**: L2/L4/L5 是文档领域的独特优势——GUI 和通用文本无法做 bbox 验证和 OCR 交叉验证。

### 3.2 "四级分级" vs 传统二元过滤

传统方法（DEITA、LESS、AlpaGasus）通常做二元过滤（保留/丢弃）。DocWorldTrace 的四级分级（Gold/Silver/Bronze/Negative）支持更细粒度的训练策略：

- Gold → SFT 主训练集
- Silver → SFT 补充集
- Bronze → PRM 对比正例
- Negative → DPO/PRM 负例

这种分级设计使得**不同错误类型的轨迹可以有针对性地用于不同训练目标**，而不是简单丢弃。

### 3.3 合成数据质控的领域特化

MAG-V、GDR、BARE 等通用合成数据质控方法没有考虑文档的特有信号（bbox 定位准确性、表格解析正确性、证据链完整性）。DocWorldTrace 的质控 system 可以看作**文档领域的特化合成数据质控**，其核心理念是：利用领域结构信号做自动质控，比纯 LLM-as-judge 更可靠。

---

## 4. DocWorldTrace 的差异化定位

| 对比维度 | DEITA/LESS/AlpaGasus | GDR/MAG-V | **DocWorldTrace** |
|---------|---------------------|-----------|-------------------|
| 过滤维度 | Complexity/Quality/Diversity (语义) | LLM 重写/多 Agent 验证 (语义) | **语义 + 执行 + 证据 + 过程 (多维)** |
| 过滤粒度 | 二元 (保留/丢弃) | 二元 | **四级 (Gold/Silver/Bronze/Negative)** |
| 信号来源 | LLM 评分 / 梯度 | LLM judge | **规则 + 执行 + bbox/OCR 交叉验证 + DocVerify++** |
| 训练策略 | 全量 SFT | 全量 SFT | **分级训练 (SFT/DPO/PRM 分集)** |
| 领域信号 | 无 | 无 | **bbox validity、OCR consistency、compute reproducibility** |

**核心差异化论点**: DocWorldTrace 不是在通用数据过滤方法上简单叠加更多维度，而是**利用文档环境的结构化优势**（bbox 可验证、OCR 可交叉检查、compute 可复算、evidence 可追溯），将合成数据质控从"语义猜测"升级为"证据驱动的结构化验证"。这是文档领域数据合成的独有结构性优势。

---

## 5. 审稿人防御话术

> **Q: "DEITA 等已经充分探索了数据过滤，你们的五层质检不过是多加了几层规则检查。"**

A: DEITA 等方法的过滤完全依赖语言信号（quality score、embedding diversity），无法验证"模型是否真的读了文档相关部分"和"推理是否被文档证据支持"。DocWorldTrace 的 L4（证据检查）和 L5（过程检查）利用了文档环境独有的结构化验证能力——bbox 在页面范围内、OCR 文本与裁剪区一致、compute 结果可复算。这些不是"多加的规则"，而是文档领域特有的、比语义评分更可靠的质量信号。

> **Q: "四级分级是否过度工程化？简单的好/坏二分不够吗？"**

A: 四级分级的必要性来自训练需求：Gold 轨迹确保核心能力的学习不受噪声干扰；Silver 轨迹增加数据多样性；Bronze 轨迹为 PRM 提供"部分正确"的对比信号（比纯负例更有信息量）；Negative 轨迹为 DPO 提供偏好对。二元过滤会丢失 Bronze 类轨迹的过程级训练价值。

---

## 6. 参考文献索引

- [DEITA (ICLR 2024)](https://openreview.net/forum?id=6091f2bb355e960600f62566ac0e2862)
- [LESS (ICML 2024)](https://arxiv.org/abs/2402.04333)
- [AlpaGasus (ICLR 2024)](https://arxiv.org/abs/2307.08701)
- [R.I.P. (ICML 2025)](https://icml.cc/virtual/2025/poster/44431)
- [GDR (arXiv 2025)](https://arxiv.org/abs/2509.08653)
- [BARE (2025)](https://sky.cs.berkeley.edu/project/bare/)
- [MAG-V (arXiv 2024)](https://arxiv.org/abs/2412.04494)
- [DS² (2024)](https://arxiv.org/abs/2410.10877)
- [Synthetic Data Survey (arXiv 2024)](https://arxiv.org/abs/2412.xxxxx)
- [Best Practices Synthetic Data (COLM 2024)](https://arxiv.org/abs/2406.06592)
- [Self-Consistency (ICLR 2023)](https://arxiv.org/abs/2203.11171)
- [DPO (NeurIPS 2024)](https://arxiv.org/abs/2305.18290)
