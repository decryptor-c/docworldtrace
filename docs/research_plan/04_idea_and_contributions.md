# 我们的 Idea 与创新点

> **标题方向**: DocWorldTrace: Verification-Guided Tool-Use Trajectory Synthesis in Reproducible Document Environments  
> **投稿定位**: ACL/EMNLP Resource + Method 或 NeurIPS Datasets and Benchmarks  
> **核心贡献**: 可交互文档环境 + DocVerify++ 质检 + 自动合成文档 Agent 工具轨迹数据

---

## 1. 核心 Idea

DocWorldTrace 将长 PDF 建模为可交互环境 (DocEnv-lite)，通过 search/read_page/crop/ocr/parse_table/compute/verify 等标准化工具合成文档 Agent 多步推理轨迹，并用 DocVerify++ 的 claim-evidence-support/sufficiency 标注对轨迹进行奖励、过滤和质量分析。

其核心假设是：

> **如果把文档任务重构为可交互环境，并用 DocVerify++ 提供过程级验证信号，就可以合成比 answer-only QA 更适合训练文档 Agent 的工具轨迹数据。**

这一 idea 的价值在于将三条独立的研究线索统一起来：

```text
线索 1: GUI Agent 的"环境→轨迹→质控"方法论
线索 2: 多模态文档推理的工具化动作空间
线索 3: DocVerify++ 的 claim-evidence 可验证信号
          ↓
统一产出: DocWorldTrace — 可复现、可审计、经验证的文档 Agent 工具轨迹数据集
```

---

## 2. 五大贡献

### C1: DocEnv-lite — 面向 PDF 的轻量交互环境

- 将 PDF 解析为可交互环境，支持 page rendering、OCR/layout、retrieval、crop、table parsing、compute、verify 等工具
- 所有工具输出包含可审计的 provenance 信息（page/bbox/element_type/confidence）
- 内置 observation 缓存机制，使 MCTS/多策略 rollout 零边际成本
- 不绑定任何特定 Agent 框架，作为通用基础设施

### C2: DocWorldTrace Schema — 统一轨迹格式

- 统一记录 Thought → Action → Observation → Evidence Update → Optional Verify → Answer
- 兼容 ReAct / ALR (DocSeeker) / VSC (DocCogito) 等现有格式
- 支持 ADP-compatible 转换，可直接用于 SFT conversation / RL rollout
- 每条轨迹自带 evidence_refs 和 quality_signals，而非纯文本 ReAct 日志

### C3: Verification-guided Synthesis — 验证引导合成

- 将 DocVerify++ 的 support/sufficiency/failure taxonomy 用作轨迹 reward 和过滤器
- 在合成阶段过滤 unsupported reasoning，而非事后评估
- 支持 per-step PRM 训练信号：每个 thought/action 是否带来有效 evidence
- 将拒答/证据不足纳入工具策略学习

### C4: DocWorldTrace-1K/3K Pilot Dataset

- 40-60 篇 PDF（arXiv + SEC/EDGAR）生成 100-200 个 QA 种子
- 多源采样（Rule-based + Teacher Rollout + Hard Negative + 小规模 MCTS）产出 2K-5K 候选轨迹
- DocVerify++ 过滤后保留 1K-3K 高质量轨迹
- 覆盖 text/table/numeric/cross-page/verification/unanswerable 六类任务

### C5: Training and Evaluation Study

- 系统化对比 answer-only SFT / teacher ReAct / DocWorldTrace SFT / filtered DocWorldTrace SFT
- 评估维度覆盖答案质量、证据支持、定位准确、工具效率和拒答能力
- 提供 failure taxonomy 和质量分析报告

---

## 3. 创新点论证：与现有工作的差异化

### 3.1 vs 通用 Agentic Data Synthesis

| 对比维度 | RandomWorld / SynthTools | DocWorldTrace |
|---------|------------------------|---------------|
| 环境类型 | 程序化生成的通用工具 | 真实 PDF 文档 + 文档专用工具 |
| Observation 可信度 | 工具模拟，可能不真实 | 大部分来自真实解析 (OCR/检索/计算) |
| Reward 信号 | 任务完成 0/1 | 七维 reward (answer/support/ground/suff/eff/refuse/tool) |
| 领域专业性 | 通用 | 文档特有的 evidence memory / bbox grounding / sufficiency |

### 3.2 vs GUI Agent 轨迹合成

| 对比维度 | AgentTrek / WebSynthesis | DocWorldTrace |
|---------|------------------------|---------------|
| 环境部署成本 | Docker/VM (高) | PDF 解析 pipeline (低) |
| 环境重置成本 | 快照恢复 | 零成本 (PDF 静态) |
| MCTS 搜索成本 | 每步真实执行 | 工具输出可缓存，60-80% 命中率 |
| 过程验证信号 | VLM 判官 (不可靠) | DocVerify++ 结构化验证 |
| 动作语义 | 像素级 (click/scroll) | 语义级 (search/parse/compute) |

### 3.3 vs 现有文档 Agent 系统

| 对比维度 | VISOR / MM-Doc-R1 / DocCogito | DocWorldTrace |
|---------|------------------------------|---------------|
| 定位 | Agent 框架/方法 | **数据与环境基础设施** |
| 轨迹公开 | ✗ | **✓ (核心贡献)** |
| 环境标准化 | 各自实现 | **DocEnv-lite 统一接口** |
| 过程级 reward | 无/隐式 | **七维显式 reward + DocVerify++** |
| 拒答训练 | 无 | **sufficiency reward + unanswerable 样本** |
| Schema 兼容性 | 绑定各自格式 | **ADP 兼容 + 多格式转换** |

---

## 4. 投稿定位

### 优先投稿方向

1. **ACL/EMNLP Resource Track** — 强调 DocEnv-lite 环境 + DocWorldTrace 数据集 + 公开轨迹的资源价值
2. **NeurIPS Datasets and Benchmarks** — 强调数据合成 pipeline + 质量分析 + failure taxonomy 的系统化贡献

### 论文叙事聚焦

论文 claim 应聚焦以下可验证命题：

1. 轨迹数据优于 answer-only 数据（尤其在工具调用、证据支持和拒答行为上）
2. DocVerify++-lite 过滤可以降低 unsupported answer / faithfulness gap
3. DocEnv-lite 提供可复现、可缓存、可审计的文档工具环境
4. Hard negatives 和 sufficiency reward 可以改善不当拒答与过早回答

**不应强调绝对 SOTA 性能**，而应聚焦可复现性和忠实性。
