# Q3: Baseline 选择

> **核心问题**: 为 DocWorldTrace 的四项 core claims 设计系统化、严谨、可防御的 baseline 实验。

---

## 1. 训练数据形态 Baseline（验证 Claim 1: 轨迹数据 vs 其他数据形态）

### 1.1 当前已规划的 Baseline

| Baseline | 数据来源 | 训练方式 | 验证目标 |
|---------|---------|---------|---------|
| B0: Base model (zero-shot) | 无 | 无 | 下界 |
| B1: Answer-only SFT | 种子 QA 的 (Q, A) 对 | SFT | Answer-only 数据能否训练文档 Agent？ |
| B2: ReAct Teacher SFT | Teacher 在 DocEnv 中生成的原始轨迹（无过滤） | SFT | 原始轨迹 vs 过滤后轨迹 |
| B3: DocWorldTrace SFT | 全量 DocWorldTrace（含 Silver/Bronze） | SFT | 全量轨迹数据效果 |
| B4: Filtered DocWorldTrace SFT | 仅 Gold + Silver | SFT | 过滤的增量价值 |

### 1.2 需要补充的 Baseline

#### B5: GRPO/SPO on Answer-only Data（"不做轨迹数据，直接 RL"路径）

**设计**:
- 在 B1 (Answer-only SFT) 的基座上做 GRPO/SPO
- Reward: 仅 outcome reward（答案正确性 + 格式）
- 目标: 验证"跳过轨迹数据，直接 RL"是否可行

**选择理由**:
- 这是当前主流的"agentic RL"路径（DeepSeek-R1 范式迁移）
- 如果 B5 的效果接近 B4，会削弱 DocWorldTrace 的必要性论证
- 预期结果：B5 在工具调用率和 evidence support 上显著弱于 B4（因为 answer-only 数据缺少工具使用策略的冷启动信号）

**公平对比条件**:
- 同基座模型
- 同数量级训练样本（保证"数据量"不是混淆变量）
- Reward 信号仅限 answer correctness（模拟真实 RL 场景）

**如果缺少此 baseline，审稿人可能质疑**: "你声称轨迹数据必要，但你没有证明 RL 路径不可行。为什么不直接用 GRPO 在 answer-only 数据上探索出工具使用策略？"

#### B6: LLM Self-Generated Trajectories（不经过 DocEnv 执行）

**设计**:
- 用同一个 Teacher 模型（GPT-4o/Gemini）生成 ReAct 轨迹，但 Tool Observation 由 Teacher 自己模拟（不经过 DocEnv 真实执行）
- 用这些"自由形式轨迹"做 SFT
- 与 B2（DocEnv 真实执行轨迹）对比

**选择理由**:
- 验证"环境约束下的轨迹合成"vs"自由形式轨迹合成"的质量差异
- 证明 DocEnv 真实执行是必需的（而非可选的优化）
- 预期结果：B6 的 Agent 在工具调用成功率、evidence support rate 上显著低于 B2（因为训练数据中的 observation 是 LLM 幻觉的）

**公平对比条件**:
- 同 Teacher 模型
- 同种子任务
- 同轨迹数量

**如果缺少此 baseline，审稿人可能质疑**: "你声称需要 DocEnv，但你有没有对比过直接用 LLM 生成轨迹的效果？也许 LLM 自生成的轨迹就够了。"

#### B7: Pure Rule-based Template Trajectories（无 Teacher 参与）

**设计**:
- 仅用 Rule-based 模板生成的确定性轨迹做 SFT（不使用 Teacher rollout）
- 验证"需要强模型 Teacher 吗？还是规则模板就够了？"

**选择理由**:
- 检验多源采样策略中 Rule-based 模板的独立价值
- 预期结果：B7 在简单任务（text lookup）上接近 B2，在复杂任务（cross-page, unanswerable）上明显弱于 B2

**如果缺少此 baseline，审稿人可能质疑**: "你声称需要 Teacher Rollout，但 Rule-based 模板也能生成轨迹。两者的差异在哪里？"

### 1.3 数据形态 Baseline 总结

| # | Baseline | 数据 | 执行环境 | 训练 | 预期效果排序 | 核心验证 |
|---|---------|------|---------|------|:---:|------|
| B0 | Base model | 无 | 无 | 无 | 最差 | 下界 |
| B1 | Answer-only SFT | (Q,A) | 无 | SFT | 差 | Answer-only 的局限 |
| B5 | Answer-only + GRPO | (Q,A) + RL reward | 无 | SFT→GRPO | 较差 | RL 能否自学工具？ |
| B7 | Rule Templates SFT | 模板轨迹 | DocEnv | SFT | 中 | Rule 的覆盖边界 |
| B6 | LLM Self-Gen SFT | Teacher 模拟轨迹 | LLM 模拟 | SFT | 中下 | 环境是否必需？ |
| B2 | Teacher ReAct SFT | Teacher 轨迹 | DocEnv | SFT | 中上 | 未过滤轨迹 baseline |
| B3 | DocWorldTrace SFT | 全量合成轨迹 | DocEnv | SFT | 好 | 全量数据 |
| B4 | Filtered DocWT SFT | Gold+Silver | DocEnv | SFT | 最好 | **过滤增量价值** |

**预期排序**: B4 > B3 > B2 > B7 ≈ B6 > B5 > B1 > B0

---

## 2. 方法对比 Baseline（与现有文档 Agent 系统的公平对比）

### 2.1 现有系统的自报 Baseline 和指标

| 系统 | 自报 Baseline | 自报评测指标 | 基座模型 |
|------|-------------|------------|---------|
| **VISOR** | RAG-based, End-to-End VLM, LlamaParse-based | Answer F1, Evidence Support Rate | Qwen2-VL-7B |
| **MM-Doc-R1** | RAG baselines, GRPO baseline | Accuracy, Tool Success Rate | Qwen3-8B/4B |
| **DocSeeker** | Vanilla GRPO, RAG+LLM | Answer EM, Evidence Precision | Qwen2-VL-7B |
| **DocCogito** | Single-pass VLM, RAG | Page-level Accuracy | 闭源 VLM |
| **MDocAgent** | Single-agent, Dual RAG | Answer F1, Retrieval Recall | GPT-4V (闭源) |

### 2.2 DocWorldTrace 的对比策略

**定位声明**: DocWorldTrace 不是"又一个文档 Agent 框架"，而是**数据与环境基础设施**。因此与现有系统的对比不是"谁的 Agent 更强"，而是：

| 对比维度 | 含义 | 对比方式 |
|---------|------|---------|
| **数据可复现性** | 我们的数据是否公开、可复现？ | 定性对比表 |
| **环境标准化** | 是否有标准化工具 API？ | 功能矩阵对比 |
| **训练后 Agent 能力** | 用同基座模型在同评测集上比较 | 实验对比（条件允许时） |
| **过程级评估** | 是否提供证据支持/充分性/效率等多维诊断？ | 定性对比 + 定量展示 |

### 2.3 公平对比条件

**可行对比方案**:

**方案 A: 同基座模型、同评测集、同训练数据量级**

```text
条件: Qwen2.5-VL-7B + MMLongBench-Doc/DocVQA + ~1K-3K 等效训练数据

可以对比:
  - DocWorldTrace SFT (Gold+Silver) vs 我们在 VISOR-style 设置下的复现
    （用 search/crop/answer 工具 + teacher 蒸馏轨迹 + SFT）
  - 这不是"与 VISOR 系统对比"而是"与 VISOR 的数据范式对比"

不能对比:
  - MM-Doc-R1 的 SPO 训练模型（轨迹不公开，无法复现训练）
  - DocCogito 的闭源 VLM（基座模型不同）
```

**方案 B: 环境功能矩阵对比（定性 + 定量）**

```text
维度: 环境标准化 | 工具数量 | 过程 reward | 轨迹公开 | provenance | 缓存 | 拒答支持

各系统矩阵:
  VISOR:       部分 | 3  | ✗ | ✗ | ✗ | ✗ | ✗
  DocSeeker:   部分 | 3  | ✗ | ✗ | ✗ | ✗ | ✗
  DocCogito:   无   | 5  | ✗ | ✗ | ✗ | ✗ | ✗
  DocLens:     部分 | 4  | ✗ | ✗ | ✓ | ✗ | ✗
  MDocAgent:   无   | N/A| ✗ | ✗ | ✗ | ✗ | ✗
  DocWorldTrace: ✓  | 10 | ✓ | ✓ | ✓ | ✓ | ✓
```

**推荐策略**: 方案 A + 方案 B 结合。用方案 A 在可复现条件下做定量对比，用方案 B 做全系统覆盖的定性定位。明确声明"我们无法与不公开轨迹的系统做公平 agent-level 对比——这正是 DocWorldTrace 存在的理由"。

### 2.4 关键对比指标

| 指标 | DocWorldTrace 独有? | 现有系统是否评测 |
|------|:---:|:---:|
| Answer Correctness (F1/EM) | ✗ | ✓ (所有系统) |
| Tool Success Rate | ✗ | ✓ (VISOR, MM-Doc-R1) |
| Evidence Support Rate | ✓ (DocVerify++ 提供) | 部分 (VISOR 隐式) |
| Bbox Grounding Accuracy | ✓ | ✗ |
| Refusal F1 | ✓ | ✗ |
| Sufficiency Accuracy | ✓ | ✗ |
| Efficiency Score | ✓ | ✗ |
| Trajectory Reproducibility | ✓ | ✗ (所有不公开) |

**策略**: 在通用指标上展示 competitive performance，在独有指标上展示不可替代的诊断价值。

---

## 3. 消融实验设计

### 3.1 ICLR 标准消融参考

#### AgentTrek (ICLR 2025) 的消融设计

| 消融项 | 消融方式 | 验证目标 |
|-------|---------|---------|
| Tutorial Harvesting | 移除 → 人工编写教程 | Harvesting 的自动化价值 |
| VLM Verification | 移除 → 全量轨迹 | Verification 过滤的价值 |
| CoT Enrichment | 移除 → 纯 ReAct | CoT 的增量 |
| Pipeline Stage 消融 | 逐步移除每个阶段 | 每阶段的独立贡献 |

#### DigiRL (NeurIPS 2024) 的消融设计

| 消融项 | 消融方式 | 验证目标 |
|-------|---------|---------|
| Online RL | Offline only → Offline+Online | Online RL 增量 |
| VLM Reward | Rule-only vs VLM reward | VLM 自动 reward 的价值 |
| Parallelization | 单环境 vs 多环境 | 并行化的加速比 |

#### WebArena (ICLR 2024) 的消融设计

| 消融项 | 消融方式 | 验证目标 |
|-------|---------|---------|
| DOM/A11y tree | 移除 → 仅截图 | 可访问性树的贡献 |
| Task 难度消融 | 按 task 难度分层 | 环境难度分级的合理性 |

### 3.2 DocWorldTrace 消融实验设计

#### 消融 A: DocVerify++ 过滤的增量价值

| 条件 | 训练数据 | 验证 |
|------|---------|------|
| A1: No Filter | 全量未过滤 Teacher 轨迹 | baseline |
| A2: Layer 1-3 Only | 仅格式+执行+答案检查 | 基础过滤够吗？ |
| A3: Layer 1-4 | L1-L4（含证据检查） | 证据检查的增量 |
| A4: Full (L1-L5) | 五层全量过滤 | **DocVerify++ 的完整价值** |

**预期**: A4 > A3 > A2 > A1。A3 vs A2 的差异量化证据检查（L4）的价值；A4 vs A3 的差异量化过程检查（L5）的价值。

**如果缺少此消融，审稿人可能质疑**: "你声称 DocVerify++ 过滤有价值，但你没有证明每一层过滤的独立贡献。"

#### 消融 B: Hard Negative 的贡献

| 条件 | 训练数据 | 训练方式 | 验证 |
|------|---------|---------|------|
| B1: Gold Only | 仅 Gold SFT | SFT | 仅最佳轨迹 |
| B2: Gold+Silver | 无 Hard Negative | SFT | 无 DPO/PRM 信号 |
| B3: Gold+Silver+HN (DPO) | 含 Negative 对 | SFT + DPO | Hard Negative 的 DPO 价值 |
| B4: Gold+Silver+HN (PRM) | 含 Bronze 对比 | SFT + PRM | Hard Negative 的 PRM 价值 |

**预期**: B3/B4 在工具选择错误率和拒答正确率上好于 B1/B2。DPO 通过工具选择对比对改善工具策略，PRM 通过 Bronze 过程信号改善证据积累。

#### 消融 C: MCTS 采样的贡献

| 条件 | 说明 | 验证 |
|------|------|------|
| C1: No MCTS | 仅 Rule+Teacher+HN | MCTS 消融为零 |
| C2: MCTS 50 samples | 50 样本 MCTS | 小规模 MCTS 的价值 |
| C3: MCTS 100 samples | 100 样本 MCTS | 规模的边际效益 |

**预期**: C2 vs C1 验证 MCTS 是否发现 Rule+Teacher 未覆盖的更优工具路径。C3 vs C2 验证 MCTS 规模是否饱和。

**关键叙事**: MCTS 在 DocWorldTrace 中定位为**消融验证模块**（非主生成器），目的是验证文档环境中的搜索式合成价值，而非声称 MCTS 创新。

#### 消融 D: Observation 缓存对成本的影响

| 条件 | 缓存策略 | 验证 |
|------|---------|------|
| D1: No Cache | 所有 action 真实执行 | MCTS/多策略 base 成本 |
| D2: Full Cache | 所有可缓存 action 缓存 | 缓存带来的成本降低 |
| D3: Partial Cache | step-based FIFO | 折中方案的效率 |

**关键指标**: 缓存命中率、每条轨迹 unique action 数、MCTS 边际成本。

**如果缺少此消融，审稿人可能质疑**: "你声称缓存是文档环境的优势，但没有量化这个优势。"

#### 消融 E: 不同 Reward 权重的影响

| 条件 | 权重配置 | 验证 |
|------|---------|------|
| E1: Outcome Only | w₁=1.0, others=0 | ORM 对比 |
| E2: Balanced | 推荐权重 | DocWorldTrace 默认 |
| E3: Process-heavy | w₂/w₃/w₅ 翻倍 | 过程信号是否过强？ |
| E4: Custom per Task | 按任务类型调整 | 自适应权重的价值 |

**预期**: E2 > E1（证明多维 reward > 纯 outcome）；E2 ≈ E4（证明默认权重足够鲁棒）。

#### 消融 F: 训练数据规模的 Scaling

| 条件 | 数据规模 | 验证 |
|------|:---:|------|
| F1 | 500 Gold | 小规模下限 |
| F2 | 1,000 Gold | 建议最低规模 |
| F3 | 3,000 Gold+Silver | DocWorldTrace 目标规模 |
| F4 | 5,000 All | 规模上限 |

**预期**: 从 F1→F2 增益最大，F3→F4 边际递减或无增益。验证 "Less is More" 假设在文档工具轨迹场景中的有效性。

### 3.3 消融实验矩阵总结

| # | 消融项 | 条件数 | 关键指标 | 审稿人质疑防线 |
|---|-------|:---:|------|------|
| A | DocVerify++ 过滤层级 | 4 | Evidence Support Rate, Unsupported Answer Rate | "每层过滤的独立贡献？" |
| B | Hard Negative 贡献 | 4 | Tool Error Rate, Refusal F1 | "HN 是必要的吗？" |
| C | MCTS 贡献 | 3 | Answer Accuracy, Tool Path Diversity | "MCTS 到底带来了什么？" |
| D | 缓存成本 | 3 | Cache Hit Rate, Cost/trajectory | "缓存优势有多大量化？" |
| E | Reward 权重 | 4 | 各维度 reward 相关性 | "多维 reward 中的维度是否冗余？" |
| F | 数据规模 | 4 | Accuracy vs Data Size | "1K-3K 真的是最优规模吗？" |

---

## 4. 综合实验计划

### 4.1 四层验证结构

```text
Layer 1: 数据质量验证（不涉及下游训练）
  ├── 五层质检分布统计
  ├── Failure taxonomy 分布
  ├── 四级分级占比
  ├── DocVerify++-lite precision/recall (人工审核 50-100 条)
  └── Observation 缓存命中率

Layer 2: 数据形态对比（SFT 实验）
  ├── B0-B7 全系列 baseline
  ├── 评测: DocVQA, MP-DocVQA, MMLongBench-Doc
  └── 关键指标: Answer F1, Evidence Support, Tool Success, Refusal F1

Layer 3: 消融实验
  ├── 消融 A-F
  └── 成本分析

Layer 4: 外部对比（定性为主 + 条件允许时定量）
  ├── 环境功能矩阵
  ├── 可复现性对比表
  └── 与 VISOR-style 数据范式复现的定量对比
```

### 4.2 关键风险与降级策略

| 风险 | 影响 | 降级策略 |
|------|------|---------|
| B4 未显著优于 B2（过滤无效） | Claim 1 削弱 | 降级：Verifier 仅做质量分析，不做强过滤 |
| B5 接近 B4（RL 足够） | Claim 1 致命 | 降级：强调轨迹数据的其他价值（可审计、公开、可复现） |
| DocVerify++-lite precision < 80% | Claim 2 致命 | 降级：人工审核扩充，仅用于质量报告 |
| 消融数量过多导致审稿人认为不聚焦 | 叙事分散 | 优先 A/B/D/F，C/E 可选放入 Appendix |

---

## 5. 参考文献索引

- [AgentTrek (ICLR 2025)](https://arxiv.org/abs/2412.09605) — 消融实验设计参考
- [DigiRL (NeurIPS 2024)](https://arxiv.org/abs/2406.18518) — RL 消融实验参考
- [WebArena (ICLR 2024)](https://arxiv.org/abs/2307.13854) — 环境评测消融参考
- [MM-Doc-R1 (2026)](https://arxiv.org/abs/2604.13579) — SPO vs GRPO baseline
- [VLAA-Thinking (TMLR 2025)](https://ucsc-vlaa.github.io/VLAA-Thinking/) — SFT vs RL baseline
- [R1-VL / StepGRPO (2025)](https://arxiv.org/abs/2503.12937) — Step-wise reward baseline
- [DocVQA](https://www.docvqa.org/) / [MP-DocVQA](https://mp-docvqa.github.io/) / [MMLongBench-Doc](https://arxiv.org/abs/2402.02888) — 评测基准
- [DEITA (ICLR 2024)](https://openreview.net/forum?id=6091f2bb355e960600f62566ac0e2862) — 数据选择 baseline
- [DeepSeek-R1 (2025)](https://arxiv.org/abs/2501.12948) — SFT cold start + GRPO 范式
