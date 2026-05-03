# 维度 3：文档理解中的忠实性与幻觉控制

> **审稿人可能攻击点**: DocWorldTrace 的 core claim "验证引导过滤可降低 unsupported reasoning" 是否有充分的 faithfulness/hallucination 文献支撑？Faithfulness 评估是否只是 factuality evaluation 的换皮？

---

## 1. 维度概述

DocWorldTrace 的核心叙事之一是：当前文档 Agent 存在"答案正确但推理无据"的 faithfulness gap，而 DocVerify++ 的过程验证可以降低此类 unsupported reasoning。这需要在以下方向找到文献支撑：

- Faithful generation 与 attribution 方法
- Hallucination detection（特别是长文档和多模态场景）
- Claim verification 和事实性评估
- Faithfulness vs Factuality 的概念区分

---

## 2. 代表性论文

### 2.1 忠实性评估与 Attribution

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 1 | **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (Min et al.) | NeurIPS 2023 | 将生成长文本分解为原子事实，逐条与知识库（Wikipedia）验证；ChatGPT 仅 58% factuality；自动版本误差 <2% vs 人工 | **原子分解范式**：DocVerify++ 的 claim decomposition → evidence retrieval → support judgment 直接继承此范式，但证据源从 Wikipedia 变为文档本身（closed-domain） |
| 2 | **Attribute or Abstain: Large Language Models as Long Document Assistants (LAB)** (Buchmann et al.) | EMNLP 2024 | 6 种长文档任务 + 引用归因 benchmark；发现 citation（回答+证据提取一步完成）最有效；证据质量预测回答质量仅对简单 claim 成立 | **长文档归因**：直接验证"长文档场景需要 attribution"的需求；DocWorldTrace 的 evidence_refs 字段可视为 LAB 的归因在工具轨迹中的扩展 |
| 3 | **D-FActScore: Merging Facts, Crafting Fallacies** (Chiang et al.) | ACL 2024 Findings | 发现模型生成的事实单独验证正确但组合后因实体歧义导致非事实；D-FActScore 比 FActScore 低 10%+ | **实体歧义**：文档场景中的 entity disambiguation 问题（同一文档中多处提到不同实体），DocWorldTrace 的 bbox grounding 可以部分缓解 |
| 4 | **VERISCORE: Evaluating the Factuality of Verifiable Claims in Long-Form Text Generation** (Song et al.) | 2024 | 区分 verifiable 和 unverifiable claims；在 8 个长文本任务上被人类标注者在 93% 情况下偏好 | **可验证性区分**：DocWorldTrace 的 unanswerable/refusal 训练与 VERISCORE 的 unverifiable 类别直接对应 |

### 2.2 多模态幻觉检测

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 5 | **FaithSCAN: Model-Driven Single-Pass Hallucination Detection for Faithful VQA** | arXiv 2026.01 | 利用 VLM 内部信号（token 级不确定性、跨模态对齐特征）做单 pass 幻觉检测；无需重复采样/外部验证器 | **内部信号利用**：DocWorldTrace 可以探索将 token 级不确定性作为 per-step 质量信号的补充 |
| 6 | **KIE-HVQA: Mitigating OCR Hallucinations in Multimodal LLMs** (He et al.) | NeurIPS 2025 | 首个退化文档 OCR 幻觉 benchmark；GRPO + uncertainty-aware reward；7B 模型幻觉减少 28% vs GPT-4o | **OCR 幻觉**：DocWorldTrace 的文档 OCR 是核心工具；KIE-HVQA 的 hallucination-free accuracy 直接支撑"过滤 unsupported reasoning"的 claim |
| 7 | **FaithAct: Faithfulness Planning and Acting in MLLMs** (Li et al.) | arXiv 2025.11 | 区分 behavioral faithfulness（推理→输出一致性）和 perceptual faithfulness（推理→输入一致性）；FaithEval benchmark | **双忠诚度**：DocWorldTrace 的 evidence support（行为忠诚）+ bbox grounding（感知忠诚）与 FaithAct 的框架一致 |
| 8 | **HalluMix: A Task-Agnostic, Multi-Domain Benchmark for Real-World Hallucination Detection** | arXiv 2025.05 | 6,500 样本跨 4 领域；短 vs 长上下文性能差异巨大；Patronus Lynx 8B 擅长长文本摘要但短 NLI/QA 弱 | **跨域评估**：提醒 DocWorldTrace 需要在不同文档类型和任务类型上验证 hallucination 控制效果 |
| 9 | **Evaluating Reasoning Faithfulness in Medical VLMs using Multimodal Perturbations** (Moll et al.) | ML4H 2025 (NeurIPS) | 通过文本和图像扰动探测 CoT faithfulness；发现答案准确性和解释质量**解耦** | **答案-推理解耦**：直接支持 DocWorldTrace 的核心 claim："答案正确 ≠ 推理忠实"需要过程验证 |

### 2.3 幻觉检测方法论

| # | 论文 | 会议/年份 | 核心贡献 | 与 DocWorldTrace 关联 |
|---|------|----------|---------|---------------------|
| 10 | **HEDGE: Hallucination Estimation via Dense Geometric Entropy for VQA** (Gautam et al.) | 2025 | 统一框架：视觉扰动 + 语义聚类 + 鲁棒不确定性度量 | **不确定性量化**：DocWorldTrace 的 confidence 字段可借鉴 HEDGE 的多信号融合方法 |
| 11 | **DAHL: Domain-specific Automated Hallucination Evaluation of Long-Form Text in Biomedicine** | EMNLP 2024 | 8,573 问题，29 个生物医学类别，原子化分解评分 | **原子分解**：与 DocVerify++ 的 claim decomposition 共享方法论 |
| 12 | **FaithEval: Contextual Faithfulness Benchmark for LLMs** (Salesforce) | 2024 | 4.9K 问题，覆盖 unanswerable/inconsistent/counterfactual 上下文；大模型 ≠ 更忠实 | **不可回答问题**：直接支撑 DocWorldTrace 的 unanswerable 训练需求 |
| 13 | **A Survey of Multimodal Hallucination Evaluation and Detection** (Chen et al.) | IJCV 2025 | 多模态幻觉综述，按 faithfulness 和 factuality 建立 taxonomy | **概念框架**：为 DocWorldTrace 区分"answer correctness"和"reasoning faithfulness"提供理论基础 |

---

## 3. 与 DocWorldTrace 的关联分析

### 3.1 Faithfulness gap 的理论基础

FActScore、FaithAct、Medical VLM Faithfulness 等工作共同确立了一个核心发现：**答案准确性和推理忠实性是解耦的**。这意味着仅评估 answer correctness（如当前大部分文档 QA benchmark 的做法）会系统性地遗漏 faithfulness gap。DocWorldTrace 的核心贡献之一就是通过过程级验证（DocVerify++-lite）填补这一缺失维度。

### 3.2 Closed-domain 文档情景的优势

现有 faithfulness 评估（FActScore、VERISCORE）主要依赖 Wikipedia 等开放知识库做验证，面临实体链接和知识覆盖的挑战。DocWorldTrace 的 closed-domain 文档情景有以下优势：

- 证据空间有限（限定在给定 PDF 内），不需要开放世界知识
- 证据可精确追溯（page/bbox 级别），消除"证据在哪儿"的模糊性
- 验证信号更可靠：OCR 文本匹配 + bbox 交叉验证 > 开放检索 + NLI

### 3.3 从 Detection 到 Prevention

现有 hallucination detection 方法（FaithSCAN、HEDGE、HalluMix）聚焦于**事后检测**（输出后判断是否幻觉）。DocWorldTrace 的创新在于将验证信号前移到**合成阶段**（在轨迹生成时就过滤 unsupported reasoning），实现从"检测幻觉"到"预防幻觉训练数据"的转变。

---

## 4. DocWorldTrace 的差异化定位

| 对比维度 | FActScore / VERISCORE | Multimodal Hallucination (FaithSCAN/KIE-HVQA) | **DocWorldTrace** |
|---------|----------------------|----------------------------------------------|-------------------|
| 验证场景 | 开放域长文生成 | 多模态 VQA | **封闭域文档 Agent 工具轨迹** |
| 验证粒度 | 原子事实级 | Token/图像区域级 | **Step 级 + 证据引用级** |
| 证据来源 | 外部知识库 (Wikipedia) | 图像 + 文本 | **文档内部 (闭合证据空间)** |
| 验证阶段 | 事后评估 | 事后检测 | **合成阶段内嵌过滤** |
| 信号类型 | Support 二元 | Hallucination 概率 | **7 维 reward + support/sufficiency/failure taxonomy** |
| 训练价值 | 仅评估 | 仅评估 | **直接生成训练/过滤信号** |

**核心差异化论点**: 现有 faithfulness 工作几乎全部聚焦于**评估**（evaluation），而非**训练数据合成**（synthesis）。DocWorldTrace 的创新在于将 faithfulness 评估信号（claim-evidence verification）从"事后评测工具"升级为"事中数据过滤基础设施"。这是评估方法论到数据工程方法的范式性迁移。

---

## 5. 审稿人防御话术

> **Q: "FActScore 和相关工作已经解决了 faithfulness 评估问题，为什么还需要 DocVerify++？"**

A: FActScore 解决的是"如何评估已生成文本的忠实性"，但不解决"如何生成更忠实的训练数据"。DocWorldTrace 的创新在于将 faithfulness 验证嵌入数据合成 pipeline——不是评估最终模型输出，而是在训练数据生成阶段就过滤 unsupported reasoning。这是从"评估"到"数据工程"的跃迁。

> **Q: "文档情景是 closed-domain，faithfulness 验证天然更简单。这是优势还是 trivial？"**

A: Closed-domain 确实使验证更可靠，但这正是 DocWorldTrace 的结构性优势。正因为文档环境提供了 bbox、OCR 交叉验证、compute 复算等结构化验证信号，我们才能构建比开放域更精确的过程监督。这类似于"代码执行可以验证推理"的优势——不是 trivial，而是选择了一个更可验证的领域，使 process supervision 的可靠性大幅提升。

---

## 6. 参考文献索引

- [FActScore (NeurIPS 2023)](https://neurips.cc/virtual/2023/79626)
- [LAB / Attribute or Abstain (EMNLP 2024)](https://arxiv.org/abs/2407.07799)
- [D-FActScore (ACL 2024)](https://arxiv.org/abs/2402.05629)
- [VERISCORE (2024)](https://arxiv.org/abs/2406.19276)
- [FaithSCAN (arXiv 2026)](https://arxiv.org/abs/2601.00269)
- [KIE-HVQA (NeurIPS 2025)](https://arxiv.org/abs/2506.20168)
- [FaithAct / FaithEval (arXiv 2025)](https://arxiv.org/abs/2511.08409)
- [HalluMix (arXiv 2025)](https://arxiv.org/abs/2505.00506)
- [Medical VLM Faithfulness (ML4H 2025)](https://arxiv.org/abs/2510.11196)
- [DAHL (EMNLP 2024)](https://arxiv.org/abs/2411.09255)
- [Multimodal Hallucination Survey (IJCV 2025)](https://www.semanticscholar.org/paper/A-Survey-of-Multimodal-Hallucination-Evaluation-and-Chen-Min/fdc092d0bddb1a99a80a37be878f183096ad236b)
- [HEDGE (2025)](https://arxiv.org/abs/2511.12693)
