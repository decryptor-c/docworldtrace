# Preliminary Research 大纲 — Co-worker 工作指导

> **目标**: 为 co-worker 提供 DocWorldTrace 项目的分阶段工作计划，包含每阶段的目标、子任务分解、交付物、技术选型和验收标准。

> ⚠️ **前置文档**: 在开始本大纲中的工作前，请先完成 [Pilot 验证设计报告](./09_pilot_verification.md) 中的 5 个假设验证实验。本大纲假设 H1-H4 已通过。

---

## 总体时间线

```text
Week 1-2:   Phase 1 — DocEnv-lite 构建
Week 3-4:   Phase 2 — Pilot 种子任务与轨迹采样
Week 5-6:   Phase 3 — 质量控制与过滤
Week 7-8:   Phase 4 — Dataset v0.1 打包
Week 9-10:  Phase 5 — Baselines 实验
Week 11-12: Phase 6 — 论文撰写
```

---

## Phase 1: DocEnv-lite 构建 (Week 1-2)

### 目标
完成面向 PDF 的轻量交互环境，对 5-10 篇 PDF 通过功能验证。

### 子任务分解

| # | 子任务 | 预计工期 | 交付物 |
|---|--------|---------|--------|
| 1.1 | PDF 页面渲染 pipeline | 1d | `render_pages(pdf) → page_images[]` |
| 1.2 | OCR + Layout 解析集成 | 2d | `ocr_parse(page) → text + bbox + blocks` |
| 1.3 | 表格候选区域检测 | 1d | `detect_tables(page) → table_candidates[]` |
| 1.4 | BM25 检索索引构建 | 1d | `build_index(ocr_texts) → retrieval_index` |
| 1.5 | 7 个 MVP 工具 API 封装 | 3d | `DocEnv.search/read_page/crop/ocr/parse_table/compute/verify` |
| 1.6 | Observation 缓存机制 | 1d | `ObsCache(action_hash → result)` |
| 1.7 | 功能验证 (5 篇 PDF) | 1d | 验证报告：每个工具的执行成功率 |

### 技术选型建议

| 组件 | 推荐方案 | 备选 | 选择理由 |
|------|---------|------|---------|
| PDF 渲染 | `pdf2image` / `pymupdf` | `pdfplumber` | 支持高 DPI 渲染 |
| OCR | `surya` | `paddleocr`, `tesseract` | 多语言、高精度、含 layout |
| Layout 解析 | `surya` layout 模块 | `layoutparser` | 一体化方案 |
| 表格检测 | `TableTransformer` | `surya` table 模块 | 结构化输出 |
| 检索引擎 | `rank_bm25` | `ColPali` (Phase 2) | 简单可靠 |
| 计算沙盒 | `RestrictedPython` / `ast.literal_eval` | 自定义解析 | 安全执行 |

### 验收标准
- [ ] 5 篇 PDF 的页面渲染和 OCR 成功率 ≥95%
- [ ] 7 个工具的 tool execution valid rate ≥90%
- [ ] 缓存命中返回结果与非缓存一致
- [ ] 完整文档：环境配置说明 + API 文档

---

## Phase 2: Pilot 种子任务与轨迹采样 (Week 3-4)

### 目标
准备 100-200 个 QA 种子，生成 2K-5K 条候选轨迹。

### 子任务分解

| # | 子任务 | 预计工期 | 交付物 |
|---|--------|---------|--------|
| 2.1 | PDF 文档收集 (40-60 篇) | 1d | 文档集 + document profile |
| 2.2 | 种子 QA 采集 (来源 A: 已有 QA) | 1d | 从 DocVQA/MP-DocVQA/MMLongBench 映射种子 |
| 2.3 | 种子 QA 派生 (来源 B: 结构派生) | 2d | 表格/跨页自动生成问题 |
| 2.4 | 种子 QA 合成 (来源 C: LLM 合成) | 1d | LLM 生成 + 筛选 |
| 2.5 | Rule-based 模板轨迹生成 | 2d | 模板覆盖 text/table/numeric 任务 |
| 2.6 | Teacher Rollout 执行 | 3d | GPT-4o/Gemini 在 DocEnv 中生成轨迹 |
| 2.7 | Hard Negative 扰动生成 | 1d | 7 类扰动负例 |
| 2.8 | (可选) MCTS 消融 (50-100 样本) | 2d | MCTS 可行性报告 |

### 关键注意事项
1. Teacher Rollout 中 **Observation 必须来自 DocEnv 真实执行**，不允许 Teacher 自行编造
2. 每个种子任务需标注 task_type / difficulty / required_tools / answerable
3. 任务分布需满足目标比例 (text 25% / table 20% / numeric 20% / cross-page 15% / verification 10% / unanswerable 10%)
4. 预算控制: Teacher Rollout 目标 1000 条 → $20-$300 (Gemini-Flash) 或 $100-$300 (GPT-4o)

### 验收标准
- [ ] ≥100 个种子 QA，覆盖 6 类任务
- [ ] ≥2000 条候选轨迹 (含 Rule/Teacher/Hard Negative)
- [ ] 轨迹格式符合 DocWorldTrace Schema
- [ ] 任务分布偏差 <10%

---

## Phase 3: 质量控制与过滤 (Week 5-6)

### 目标
集成 DocVerify++-lite，过滤产出 1K-3K 高质量轨迹，完成人工审核校准。

### 子任务分解

| # | 子任务 | 预计工期 | 交付物 |
|---|--------|---------|--------|
| 3.1 | L1 格式检查脚本 | 1d | 自动化格式验证 |
| 3.2 | L2 执行检查脚本 | 1d | observation 来源与一致性验证 |
| 3.3 | L3 答案检查 (EM/F1/ANLS) | 1d | 答案匹配评分 |
| 3.4 | L4 证据检查 (bbox + OCR 交叉) | 2d | grounding 验证 |
| 3.5 | L5 DocVerify++-lite 集成 | 3d | claim → evidence → support 判断 |
| 3.6 | 质量分级 (Gold/Silver/Bronze/Negative) | 1d | 分层标注 |
| 3.7 | 人工审核 100-150 条 | 2d | 校准报告：各 precision/recall |
| 3.8 | Failure taxonomy 统计 | 1d | 10 类失败分布报告 |

### 验收标准
- [ ] 自动化质检覆盖 L1-L5 全部层级
- [ ] 过滤后轨迹 ≥1000 条
- [ ] 人工审核 evidence support precision ≥80%
- [ ] Unsupported answer 比例较过滤前下降 ≥25%
- [ ] Failure taxonomy 分布报告

---

## Phase 4: Dataset v0.1 打包 (Week 7-8)

### 目标
发布 DocWorldTrace-1K 数据集的三种格式版本。

### 子任务分解

| # | 子任务 | 预计工期 | 交付物 |
|---|--------|---------|--------|
| 4.1 | 数据清洗与最终审核 | 2d | 清洗后数据 |
| 4.2 | ReAct JSON 格式打包 | 1d | `docworldtrace_v01_react.jsonl` |
| 4.3 | SFT Conversation 格式转换 | 1d | `docworldtrace_v01_sft.jsonl` |
| 4.4 | ADP-compatible 格式转换 | 1d | `docworldtrace_v01_adp.jsonl` |
| 4.5 | 数据集统计报告 | 2d | 任务分布/工具使用分布/质量分层/成本报告 |
| 4.6 | 数据集文档 (README + datacard) | 1d | 数据集描述文档 |

### 验收标准
- [ ] 三种格式数据完整且可加载
- [ ] 统计报告覆盖任务/工具/质量/成本维度
- [ ] README 包含使用说明和许可

---

## Phase 5: Baselines 实验 (Week 9-10)

### 目标
完成 answer-only / ReAct teacher / DocWorldTrace SFT 的下游训练对比。

### 子任务分解

| # | 子任务 | 预计工期 | 交付物 |
|---|--------|---------|--------|
| 5.1 | 实验环境搭建 | 1d | 训练/评估脚本 |
| 5.2 | Answer-only SFT baseline | 2d | 训练 + 评测结果 |
| 5.3 | ReAct teacher SFT baseline | 2d | 训练 + 评测结果 |
| 5.4 | DocWorldTrace SFT | 2d | 训练 + 评测结果 |
| 5.5 | Filtered DocWorldTrace SFT | 2d | 训练 + 评测结果 |
| 5.6 | 结果对比分析 | 1d | 实验结果表格 + 分析报告 |

### 推荐基础模型
- **7B 级**: Qwen2.5-VL-7B / InternVL2-8B
- **关键评测集**: DocVQA, MP-DocVQA, MMLongBench-Doc

### 验收标准
- [ ] 至少 4 组对比实验完成
- [ ] 7 维评测指标全覆盖
- [ ] SFT 后工具成功率或证据支持率提升 ≥5%

---

## Phase 6: 论文撰写 (Week 11-12)

### 目标
完成 DocWorldTrace 论文初稿。

### 建议章节结构

```text
1. Introduction
2. Related Work
   2.1 Agentic Data Synthesis
   2.2 GUI Agent Environments
   2.3 Multimodal Document Agents
3. DocWorldTrace Framework
   3.1 DocEnv-lite
   3.2 Multi-source Trajectory Sampling
   3.3 Verification-guided Quality Control
   3.4 DocWorldTrace Schema
4. DocWorldTrace-1K Dataset
   4.1 Construction Statistics
   4.2 Quality Analysis
   4.3 Failure Taxonomy
5. Experiments
   5.1 Data Quality Evaluation
   5.2 Downstream Training Evaluation
   5.3 Ablation Studies
6. Discussion
7. Conclusion
```

---

## 阅读清单

### 必读 (Phase 1 前完成)

| 论文 | 核心价值 |
|------|---------|
| WebArena (Zhou et al., 2024) | 环境设计范式 |
| AgentTrek (Xu et al., 2025) | 轨迹合成 pipeline |
| VISOR (2024) | 文档 Agent 动作空间与 evidence space |
| Agent Data Protocol (Awasthi et al., 2025) | 统一轨迹 schema |

### 建议精读 (Phase 2 前补充)

| 论文 | 核心价值 |
|------|---------|
| WebSynthesis (2025) | World-Model MCTS |
| SPORT (2025) | Step-level preference |
| RandomWorld (2025) | 程序化环境生成 |
| MM-Doc-R1 (2024) | search/read 工具 + SPO |
| DocCogito (2024) | VSC 原子操作 |

### 视需要阅读

| 论文 | 相关场景 |
|------|---------|
| DigiRL / DART | 如需扩展到在线 RL |
| SynWorld / SynthTools | 深入工具环境合成 |
| Simia | LLM 模拟反馈策略 |
| ToolBench / StableToolBench | 通用 tool-use 数据质控 |

---

## 与现有项目协同

| 项目 | 协同方式 | 依赖关系 |
|------|---------|---------|
| **DocVerify++** | 提供 support/sufficiency reward 与 failure taxonomy | DocWorldTrace 的 verify 工具和质量过滤依赖 DocVerify++ |
| **DocGround** | 作为 training-free grounded output 生成器和评测对象 | DocWorldTrace 数据可评估 DocGround 的 grounding 质量 |
| **CodeAsReasoning** | compute 工具与数值 claim 验证 | 共享计算沙盒组件 |
| **FaithfulnessByDesign** | 使用 DocWorldTrace 分析 unsupported reasoning | FBD 可消费 DocWorldTrace 的 faithfulness gap 数据 |

---

## 风险预警与决策点

| 时间节点 | 决策 | 触发条件 |
|---------|------|---------|
| Week 2 末 | 是否继续推进 | tool execution valid rate <85% → 停顿修复 |
| Week 4 末 | MCTS 是否扩大规模 | 50 样本消融显示成本/质量可控 → 扩展 |
| Week 6 末 | 论文叙事方向 | SFT 效果不足 → 转向 Resource 叙事 |
| Week 6 末 | DocVerify++ 角色 | precision <75% → 降为分析工具 |
| Week 8 末 | 是否进入 RL 阶段 | SFT 显著提升 → 加入 GRPO 实验 |
