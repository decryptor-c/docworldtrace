# 背景与研究动机

> **研究方向**: DocWorldTrace — 面向多模态文档推理的可交互环境与验证引导工具轨迹合成  
> **核心定位**: 可复现文档工具环境 + 验证引导轨迹合成 + 过程级质量控制

---

## 1. 研究领域概述

多模态文档推理 (Multimodal Document Reasoning) 正经历从"直接回答"到"多步 Agent 交互"的范式转变。以 VISOR、MM-Doc-R1、DocSeeker、DocCogito、DocLens 等为代表的文档 Agent 系统，已将长文档理解任务重构为包含主动检索、视觉定位、证据积累、工具组合和拒答判断的多步交互过程。

这些系统的共同特征是引入了工具化动作空间（如 search、crop、parse_table、compute），使模型从"一次性读取全文并输出答案"转变为"在文档环境中逐步探索并基于多步证据做出判断"。这一趋势与 GUI Agent 领域（WebArena、OSWorld、AndroidWorld）的发展路径高度一致——两者都将任务建模为 Agent 与环境之间的多轮交互。

---

## 2. 核心问题：开源 RL 蒸馏悖论

当前多模态文档 Agent 面临一个根本性的**"开源 RL 蒸馏悖论"**：

- 新发表的系统声称通过 GRPO/SPO 等方法训练开放模型获得 agentic reasoning 能力；
- 但冷启动轨迹**普遍依赖 GPT-4o/Gemini 等闭源 teacher**，且轨迹数据**通常不公开**；
- 这导致后续研究者既无法复现训练过程，也无法在此基础上迭代改进。

| 系统 | 轨迹公开 | Teacher 依赖 | 环境可复现 |
|------|:---:|:---:|:---:|
| VISOR | ✗ | GPT-4o | ✗ |
| MM-Doc-R1 | ✗ | Gemini | ✗ |
| DocSeeker | ✗ | GPT-4o | ✗ |
| DocCogito | ✗ | 闭源 VLM | ✗ |
| DocLens | — (training-free) | — | — |
| MDocAgent | ✗ | GPT-4V | ✗ |

---

## 3. 数据层瓶颈：从 Answer-only 到 Process Data

更深层的问题在于**数据形态**。现有公开文档 QA 数据大多是 answer-only 格式（question → answer），无法训练模型以下关键能力：

1. **工具选择** — 何时 search、何时 read_page、何时 crop、何时 parse_table
2. **证据积累** — 如何在多页文档中逐步构建 evidence memory
3. **充分性判断** — 如何判断已收集的证据是否足够回答问题
4. **拒答能力** — 如何在证据不足或问题不可回答时正确拒答
5. **忠实性保证** — 如何避免答案正确但中间推理 unsupported 的"faithfulness gap"

这与通用 Agentic Data Synthesis 领域（RandomWorld、SynWorld、Simia、SynthTools、WebSynthesis）所解决的问题高度一致：当现有数据无法覆盖 Agent 的过程行为时，需要合成**完整的 Thought-Action-Observation-Evidence-Reward 轨迹**，而非仅记录最终答案。

---

## 4. 核心 Thesis：文档即环境

DocWorldTrace 的核心判断是：**多模态文档推理可以被建模为交互式环境**。

```text
通用 agentic synthesis:
  simulated environment + tool actions + observations + rewards

迁移到多模态文档推理:
  PDF/long document environment + document tools + evidence observations + DocVerify++ rewards
```

具体映射关系如下：

| RL/Agent 概念 | 文档任务映射 |
|---|---|
| Environment | PDF 页面、OCR 文本、layout 结构、表格、图表、图像区域 |
| State | 已读页面、检索历史、evidence memory、剩余工具预算 |
| Action | search / read_page / crop / OCR / parse_table / compute / verify / answer / refuse |
| Observation | 检索结果、页面截图、裁剪图、OCR 文本、表格结构、计算结果、验证结果 |
| Reward | 答案正确性、证据支持性、bbox 有效性、工具效率、拒答正确性 |

这使得 PDF 不再只是静态输入，而是可被 Agent 逐步探索的 **Document Environment**。

---

## 5. 迁移合理性：方法论迁移而非交互机制照搬

GUI Agent 领域已形成成熟的"环境构建 → 轨迹收集 → 质量过滤"范式。DocWorldTrace 迁移的是这一**方法论框架**，而非 GUI 的具体交互机制（click/scroll/type）。文档环境在以下维度具备结构性优势：

| 维度 | GUI 环境 | 文档环境 (DocEnv) |
|------|---------|------------------|
| 环境稳定性 | 低 (JS/动态内容) | **高 (PDF 静态)** |
| 工具输出缓存 | 多数不可缓存 | **search/read/crop/ocr/parse 全量可缓存** |
| 奖励信号丰富度 | 稀疏 (任务完成 0/1) | **答案 + 证据 + grounding + sufficiency + 效率** |
| 环境构建成本 | 高 (Docker/VM) | **中低 (PDF 解析 pipeline)** |
| 环境重置 | 需快照恢复 | **零成本 (PDF 不变)** |
| 并行化 | 中 (多 VM) | **高 (多 PDF 独立运行)** |

基于此，DocWorldTrace 的核心假设是：

> **如果把文档任务重构为可交互环境，并用 DocVerify++ 提供过程级验证信号，就可以合成比 answer-only QA 更适合训练文档 Agent 的工具轨迹数据。**

这一假设将在后续 [方法设计](./05_method.md) 和 [预期实验](./06_experiments.md) 中具体展开和验证。
