# DocWorldTrace Proposal Briefing Deck Narrative Plan

## Audience and Goal

- Audience: 导师 / 外部合作者
- Goal: 用 13 页中文 briefing deck 讲清楚 DocWorldTrace 的研究动机、核心方案、数据样例、pilot 证据、预期贡献和下一步执行计划。
- Principle: 图片只作为无文字视觉板；所有事实、标题、数字、图表标签和流程节点都保留为可编辑 PPT 对象。

## Visual System

- Tone: 克制、学术、系统化；避免营销式 hero 和过度装饰。
- Layout: 每页一个主论点，图解占主导，文本压缩到可扫读范围。
- Colors: warm off-white background, charcoal text, teal primary accent, amber secondary accent, slate neutral.
- Typography: 中文优先使用 PingFang SC / Hiragino Sans GB / Microsoft YaHei fallback；英文和数字使用 Aptos / Arial fallback.

## Slide Plan

### 1. 标题页

- Title: DocWorldTrace
- Message: 验证引导的文档 Agent 工具轨迹合成。
- Visual: `assets/title_environment_trace.png` as full-slide text-free visual plate.
- Notes: 先把定位说清楚：这不是又一个文档 QA Agent，而是数据与环境基础设施。核心抓手是把 PDF 变成可交互环境，再用验证信号约束轨迹质量。

### 2. 研究动机

- Title: 文档推理正在从 answer-only 转向多步 Agent 交互
- Message: 新一代系统需要学习工具选择、证据积累、定位与拒答，而不仅是输出最终答案。
- Visual: Editable two-column transformation diagram.
- Notes: 先建立范式转变：传统 DocVQA 只问最终答案，而 VISOR、DocSeeker 等系统已经把任务变成 search/read/crop/compute 的交互过程。

### 3. 开源 RL 蒸馏悖论

- Title: 开源模型的 agentic 能力，冷启动仍依赖闭源 teacher
- Message: 主要系统不公开轨迹、依赖 GPT-4o/Gemini，导致复现与公平对比困难。
- Visual: Editable comparison matrix.
- Notes: 强调悖论不是“用了闭源 teacher”本身，而是轨迹不公开、环境不可复现，使每个后续系统都要重新付蒸馏成本。

### 4. 五个核心缺口

- Title: Answer-only 数据无法训练文档 Agent 的关键能力
- Message: 缺的是过程数据、标准环境、过程 reward、faithfulness 控制和拒答/充分性示范。
- Visual: Editable five-column gap map.
- Notes: 这页把问题拆成五个独立缺口，后面每个方案模块都要回扣这些缺口。

### 5. 核心 Thesis

- Title: 文档即环境 + 验证引导合成
- Message: 静态 PDF 环境让工具输出可缓存、证据可追溯、过程信号可验证。
- Visual: Three research threads converge to DocWorldTrace.
- Notes: 这里给出完整 thesis：环境化让轨迹真实可执行，DocVerify++ 让轨迹质量可审计，最终产出更适合训练文档 Agent 的数据。

### 6. DocEnv-lite

- Title: DocEnv-lite: 面向 PDF 的轻量交互环境
- Message: 10 个语义级工具覆盖 search/read/crop/ocr/table/compute/verify/answer/refuse/overview，并维护 evidence memory。
- Visual: `assets/docenv_workbench.png` as background plate plus editable tool layer.
- Notes: 强调工具输出来自环境真实执行，不让 teacher 自己编 observation；每条 evidence 都带 page/bbox/type/confidence。

### 7. 多源轨迹采样

- Title: 多源轨迹采样: 从种子任务到候选轨迹
- Message: Rule-based、Teacher rollout、Hard negative、MCTS 消融共同覆盖正例、负例和多样路径。
- Visual: `assets/trajectory_synthesis.png` plus editable pipeline.
- Notes: 这页重点是数据生成不只靠 teacher，一部分确定性模板提高稳定性，一部分负例为 DPO/PRM 提供训练信号。

### 8. 数据样例

- Title: 数据样例: question + documents + reasoning trajectory
- Message: 一条样例记录同时包含 question、document evidence、tool reasoning trajectory、answer 和 quality signals。
- Visual: `assets/dataset_example_visual.png` as text-free background plate plus editable question/evidence/trajectory cards.
- Notes: 用 pilot seed `ti2025ars__numeric_free_cash_flow_margin_change_p29` 展示数据长什么样。重点是 answer-only 只保留最后答案，而 DocWorldTrace 保留可执行工具过程、证据引用和验证信号。

### 9. 质量控制与 Reward

- Title: DocVerify++ 把质量控制前移到轨迹合成过程
- Message: 五层质检、四级分级、七维 reward 将 answer-level 评价升级为 evidence-driven process supervision。
- Visual: `assets/quality_control.png` plus editable funnel/reward matrix.
- Notes: 解释 reward 不只是最终答案，还包括 support、grounding、sufficiency、efficiency、refusal 和 tool correctness。

### 10. Gap-to-Solution

- Title: 为什么这套方案能正面解决五个缺口
- Message: 环境使方法可行，验证使数据高质量，数据使训练可复现。
- Visual: Editable gap-to-solution matrix and causal chain.
- Notes: 用一页完成回扣：每个 gap 都有一个明确机制，而不是泛泛说“数据更好”。

### 11. Pilot H1-H4 证据

- Title: Pilot 已完成 H1-H4 闭环验证
- Message: 5 篇 PDF、20 个 seed、80 条轨迹、144 条注入式负例上，关键可行性指标全部通过。
- Visual: Editable KPI cards and small bar summary.
- Notes: 数字必须准确：H1 50/50 tool calls；H2 80/80 format compliance；H3 144/144 caught；H4 6/6 task coverage, 8/10 action coverage, search query unique 52.78%。

### 12. 预期贡献与投稿定位

- Title: 五项贡献: 环境、Schema、合成方法、数据集、训练评测
- Message: 叙事重点是可复现性、忠实性和工具效率，不追求绝对 SOTA。
- Visual: Editable contribution stack.
- Notes: 投稿定位优先 ACL/EMNLP Resource Track 或 NeurIPS Datasets and Benchmarks。

### 13. 下一步计划与风险

- Title: 12 周推进计划: 从 DocEnv-lite 到 Dataset v0.1
- Message: 下一步的关键不是扩写 proposal，而是补齐自然分布 GT、文档池多样性和 H5 mini-SFT。
- Visual: Editable roadmap and risk panel.
- Notes: 明确三个 P0 风险：自然分布人工 GT confusion matrix、真 10-K/扫描件扩展、H5 行为收益验证。
