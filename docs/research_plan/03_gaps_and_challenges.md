# 现有研究的缺陷与问题

> **目标**: 系统归纳当前多模态文档 Agent 研究在数据、环境、奖励、忠实性和拒答五个维度上的核心缺口，为 DocWorldTrace 的研究动机提供支撑。

---

## Gap 1: 轨迹数据缺失

### 问题描述

当前文档 Agent 系统（VISOR、MM-Doc-R1、DocSeeker、DocCogito、MDocAgent）均在训练阶段使用多步工具轨迹，但这些轨迹数据**一律不公开**。这意味着：

- 后续研究者无法在同一数据上复现训练过程或做公平对比
- 每个新系统都必须从零重新蒸馏 teacher 轨迹，重复大量工程投入
- 不同系统声称的 RL 训练收益无法从数据侧验证

更关键的是，现有公开文档 QA 数据集（DocVQA、MP-DocVQA、MMLongBench-Doc、ChartQA、TATQA）**只提供 question-answer 对**，不包含中间推理步骤和工具调用序列。这类 answer-only 数据无法训练模型学习工具选择策略、证据积累路径和多步推理流程。

### 现有尝试的不足

| 数据资源 | 覆盖范围 | 缺失 |
|---------|---------|------|
| DocVQA / MP-DocVQA | 单页/多页 QA | 无中间步骤、无工具调用 |
| MMLongBench-Doc | 长文档 QA + unanswerable | 无轨迹、无证据引用 |
| TATQA / FinQA | 数值推理 | 无文档环境交互 |
| ADP (Agent Data Protocol) | 统一 schema | 无文档领域数据 |

---

## Gap 2: 环境不可复现

### 问题描述

每个文档 Agent 系统自建交互环境，但这些环境**不标准化、不可复现**：

- VISOR 定义了 search/crop/answer 但未公开环境实现
- DocSeeker 用 ALR 三阶段格式但绑定特定方法
- DocCogito 定义了 VSC 原子操作但需要映射到底层工具
- DocLens 工具链完整但不产生 SFT/RL 训练数据

结果是：**无法在同一文档环境中对比不同 Agent 策略**，每篇论文的"超越 baseline"结论都可能受到各自环境实现差异的影响。

对比 GUI Agent 领域，WebArena/OSWorld 已经建立了标准化可复现的交互环境，使不同 Agent 策略可在同一环境中公平竞争。文档推理领域缺少类似的公共基础设施。

---

## Gap 3: 过程级奖励缺失

### 问题描述

GUI Agent 领域的奖励信号通常只有**最终任务是否完成**（goal completion 0/1），属于稀疏 reward。虽然 SPORT 等工作开始探索 step-level preference，但信号仍来自 VLM 判官，可靠性有限。

文档推理领域虽然理论上可以提供更丰富的过程级信号，但现有系统尚未系统化建立：

| 潜在过程信号 | 理论价值 | 现有实现 |
|------------|---------|---------|
| 每步 evidence gain | 判断 action 是否带来有效证据 | 无系统化实现 |
| 证据支持性 (support) | 判断推理是否被文档证据支持 | 仅 VISOR 隐式使用 |
| 定位准确性 (grounding) | bbox/page 是否定位正确 | DocLens 有工具但无 reward |
| 工具选择合理性 | 当前状态下工具选择是否最优 | 无 |
| 充分性判断 | 证据是否足够回答 | 无 |

DocVerify++ 的 claim-evidence-support/sufficiency 标注提供了解决这一缺口的直接工具，但尚未被系统化集成到轨迹合成 pipeline 中。

---

## Gap 4: 忠实性控制缺口 (Faithfulness Gap)

### 问题描述

文档推理中存在一种隐蔽的质量问题：**答案正确但中间推理未被文档证据支持** (faithfulness gap)。例如：

```text
问题: FY2023 的收入增长率是多少？
答案: 14.3% ← 正确
推理: 模型记忆中"通常科技公司增长约 15%"→ 估算 14.3% ← 未被文档支持
```

这种"正确但不忠实"的答案在 answer-only 评估中会被判为正确，但在部署场景中可能导致用户基于错误的推理依据做出决策。

现有文档 Agent 的训练和评估**均不检测 faithfulness gap**：

- Answer F1/ANLS 只评估最终答案
- 没有系统化的 claim decomposition → evidence retrieval → support judgment 流程
- 训练数据中的 unsupported reasoning 会被当作正例学习

---

## Gap 5: 拒答与充分性训练缺失

### 问题描述

实际文档推理场景中，用户问题经常**不可回答**（信息不在文档中）或**证据不足**（需要更多搜索），但现有训练数据几乎不包含这类场景：

| 能力 | 训练需求 | 现有数据支持 |
|------|---------|------------|
| 不可回答问题的正确拒答 | 含 unanswerable 标注的轨迹 | MMLongBench-Doc 有标注但无轨迹 |
| 证据不足时继续搜索 | 含 sufficiency 判断的多步轨迹 | 无 |
| 避免 over-refusal | 含可回答但看似困难的对比样本 | 无 |
| 证据充分时及时回答 | 含 "stop searching" 信号的轨迹 | 无 |

结果是模型要么总是尝试回答（即使证据不足），要么过于保守地拒答（over-refusal），缺乏基于证据充分性做动态判断的能力。

---

## 缺口总结与 DocWorldTrace 的对应

| 缺口 | 核心问题 | DocWorldTrace 的对应方案 |
|------|---------|----------------------|
| Gap 1 轨迹缺失 | 无公开文档工具轨迹 | DocWorldTrace-1K/3K 公开数据集 |
| Gap 2 环境不可复现 | 各系统自建环境 | DocEnv-lite 标准化环境 |
| Gap 3 过程 reward 缺失 | 只有 answer-level 评估 | 七维 reward + DocVerify++-lite |
| Gap 4 忠实性缺口 | 答案正确但推理无据 | Verification-guided 过滤 |
| Gap 5 拒答缺失 | 无 sufficiency/refusal 训练数据 | Sufficiency reward + unanswerable 样本 |

详细方案见 [我们的 Idea 与创新点](./04_idea_and_contributions.md) 和 [方法具体内容](./05_method.md)。
