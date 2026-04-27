# References

> 本文件集中记录 DocWorldTrace 研究 proposal 所涉及的本地材料与外部论文引用。

---

## 1. 原始调研材料

### 来源调研目录

- [`agentic_doc_synthesis_survey/`](../agentic_doc_synthesis_survey/) — DocWorldTrace 原始调研与 proposal 的基础材料
  - `00_overview.md` — 调研总览与核心 thesis
  - `01_general_agentic_synthesis.md` — 通用 agentic 合成方法
  - `02_document_task_mapping.md` — 文档任务映射与 schema
  - `03_research_directions.md` — 四个研究方向
  - `04_recommended_proposal.md` — DocWorldTrace 核心 proposal
  - `05_gui_agent_paradigm.md` — GUI Agent 范式调研
  - `06_docenv_design.md` — DocEnv 环境设计
  - `07_trajectory_pipeline.md` — 轨迹收集 pipeline
  - `08_quality_reward.md` — 质量控制与 reward 设计
  - `09_overview_env_sim.md` — 环境模拟方法论总览

### 关联项目

- [`DocVerify++/`](../DocVerify++/) — Claim-evidence verification 数据合成
- [`DocGround/`](../DocGround/) — Training-free grounded CoT 方法
- [`FaithfulnessByDesign/`](../FaithfulnessByDesign/) — 忠实推理诊断与修正
- [`CodeAsReasoning/`](../CodeAsReasoning/) — 代码执行推理方法

---

## 2. 外部论文

### 通用 Agentic Synthetic Data / Simulated Environment

| 论文 | 链接 | 核心贡献 |
|------|------|---------|
| RandomWorld | [arXiv:2506.11045](https://arxiv.org/abs/2506.11045) | 程序化工具环境生成 |
| SynWorld | [arXiv:2504.03561](https://arxiv.org/abs/2504.03561) | 场景合成 + MCTS action knowledge |
| Simia-SFT / Simia-RL | [arXiv:2511.01824](https://arxiv.org/abs/2511.01824) | LLM 模拟环境反馈 |
| SynthTools | [arXiv:2511.09572](https://arxiv.org/abs/2511.09572) | Tool Generation/Simulation/Audit |
| WebSynthesis | [arXiv:2507.04370](https://arxiv.org/abs/2507.04370) | World-Model MCTS 轨迹合成 |
| Agent Data Protocol | [arXiv:2510.24702](https://arxiv.org/abs/2510.24702) | 统一 agent trajectory schema |

### GUI Agent 环境与轨迹

| 论文 | 会议 | 核心贡献 |
|------|------|---------|
| WebArena | 2024 | 可复现 Web 环境基准 |
| OSWorld | 2024 | 跨应用桌面环境 |
| AndroidWorld | 2024 | Android 模拟器环境 |
| AgentTrek | ICLR 2025 | 自动化轨迹合成 pipeline |
| GUI-Net-1M / TongUI | AAAI 2026 | 百万级轨迹数据集 |
| SPORT | 2025 | 自探索 step-level preference |
| DigiRL | NeurIPS 2024 | Offline-to-online RL |
| DART | 2025 | 异步 RL 训练框架 |

### 多模态文档 Agent

| 论文 | 核心贡献 |
|------|---------|
| VISOR | Structured evidence space + GRPO |
| Doc-V* | Coarse-to-fine navigation + working memory |
| MM-Doc-R1 | Planner/seeker/answer + SPO |
| DocSeeker | ALR 轨迹 + evidence-aware GRPO |
| DocCogito | VSC 原子操作链 |
| DocLens | Training-free 工具链 |
| MDocAgent | 多 Agent + Dual RAG |

---

## 3. 评测基准

| 基准 | 用途 |
|------|------|
| DocVQA | 单页文档 QA |
| MP-DocVQA | 多页文档 QA |
| MMLongBench-Doc | 长文档 QA + unanswerable |
| DUDE | 工业文档理解 |
| SlideVQA | 幻灯片理解 |
| ChartQA | 图表理解 (Phase 2) |
| TATQA / FinQA | 数值推理 |
