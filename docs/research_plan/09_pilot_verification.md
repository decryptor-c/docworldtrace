# DocWorldTrace Pilot 验证设计报告

> **目标**: 在投入大规模开发前，用最小成本验证 DocWorldTrace 的核心假设，识别 deal-breaker 风险并决定是否/如何继续推进。  
> **原则**: 先验证假设，再扩展规模。每个实验都服务于一个最终决策。

---

## 核心假设拆解

DocWorldTrace 的整体 thesis 可拆解为 **5 个独立可验证的子假设**，按风险/依赖顺序排列如下（H1 最基础，失败则后续全部无意义）：

```text
H1: DocEnv 可行性
 └─ H2: 轨迹可生成性
     ├─ H3: 验证过滤有效性
     │   └─ H5: 训练收益
     └─ H4: 轨迹质量多样性
```

| ID | 假设 | 核心风险 | 若失败 |
|:--:|------|---------|--------|
| H1 | PDF 可被建模为稳定、可复现的工具交互环境 | OCR/表格解析/检索质量不够稳定 | 整个项目不可行，需重新评估 |
| H2 | 强模型 Teacher 可在 DocEnv 中生成合理的多步 ReAct 轨迹 | Teacher 不会用文档工具 / 生成轨迹格式混乱 | 轨迹合成路线不通，需改为人工标注 |
| H3 | DocVerify++-lite 可有效区分 supported vs unsupported 轨迹 | 过滤精度不足，好坏轨迹不可分 | 验证引导失效，降为 resource-only 叙事 |
| H4 | 合成轨迹在工具组合和推理路径上有足够多样性 | 所有轨迹高度同质（同样的工具顺序） | 数据对 SFT 无独特价值 |
| H5 | 轨迹 SFT 在工具调用/证据支持/拒答上优于 answer-only SFT | SFT 后无可观测提升 | 转向 benchmark/resource 叙事 |

---

## Pilot 实验设计

### Pilot Exp-1: DocEnv 环境可行性 → 验证 H1

> **核心问题**: 文档工具在真实 PDF 上的执行成功率是否足够高？

**规模**: 5 篇 PDF（3 arXiv + 2 SEC 10-K），涵盖简单/中等/复杂各级别

**实验方法**:
1. 对 5 篇 PDF 执行完整的环境初始化 pipeline（渲染 → OCR → Layout → 索引）
2. 人工设计 **30 个标准工具调用**（每个 action 类型 3-5 个），逐一执行并记录结果
3. 评估每次调用的执行状态和输出质量

**评估指标**:

| 指标 | 定义 | 通过门槛 |
|------|------|:--------:|
| 工具执行成功率 | status=success 的比例 | ≥90% |
| OCR 文本准确度 | 人工抽检 10 段 OCR 文本的 CER | ≤5% |
| BM25 检索相关性 | 10 个 query 的 top-3 页面包含正确页面的比例 | ≥80% |
| parse_table 结构正确率 | 表格行列结构与原 PDF 一致的比例 | ≥70% |
| crop bbox 有效性 | 裁剪结果包含目标视觉元素的比例 | ≥85% |
| compute 结果正确率 | 表达式计算结果与人工验算一致 | 100% |
| 缓存一致性 | 相同输入二次调用返回相同结果 | 100% |

**判定逻辑**:
- ✅ 全部达标 → H1 成立，进入 Exp-2
- ⚠️ parse_table <70% → 降级为 OCR text + markdown table，不使用独立结构化解析
- ⚠️ BM25 <80% → 评估补充 ColPali 的必要性
- ❌ 工具执行成功率 <80% → 停止，重新审视技术选型

**预计耗时**: 3-4 天（含环境搭建）

---

### Pilot Exp-2: Teacher 轨迹生成可行性 → 验证 H2

> **核心问题**: 强模型 Teacher 能否在 DocEnv 中生成格式正确、推理合理的多步 ReAct 轨迹？

**前提**: H1 通过

**规模**: 从 5 篇 PDF 中选 **20 个 QA 种子**（每类任务 3-4 个），对每个种子做 2 次 Teacher Rollout

**实验方法**:
1. 设计 system prompt（包含工具 API spec + ReAct 格式 + 2 个 few-shot 示例）
2. 使用 2 个 Teacher（GPT-4o + Gemini-2.5-Flash），各生成 20 条轨迹
3. DocEnv 执行每一步 action 并返回真实 observation（Teacher 不自行生成 observation）
4. 记录每条轨迹的步数、工具调用序列、最终答案

**评估指标**:

| 指标 | 定义 | 通过门槛 |
|------|------|:--------:|
| 格式合规率 | 轨迹完整遵守 ReAct 格式（Thought-Action-Obs 循环） | ≥85% |
| 正确终止率 | 以 answer/refuse 正常终止（非截断/循环/格式崩坏） | ≥80% |
| 答案正确率 | 最终答案与 reference 匹配（F1≥0.5） | ≥60% |
| 工具调用合理性 | 人工审核: 各步工具选择是否合理（1-5 分） | 平均 ≥3.5 |
| 平均步数 | 每条轨迹的平均 Thought-Action-Obs 轮数 | 3-8 步 |
| Teacher 比较 | GPT-4o vs Gemini-2.5 的质量/成本 trade-off | 记录即可 |

**关键观察点**:
- Teacher 是否倾向于跳过工具直接回答？（常见问题）
- Teacher 是否能正确使用 `verify` 和 `refuse`？（创新 action 的可用性）
- 不同任务类型的成功率差异？（识别哪些任务类型需要更多 prompt 工程）

**判定逻辑**:
- ✅ 格式合规 ≥85% + 答案正确 ≥60% → H2 成立
- ⚠️ verify/refuse 使用率极低 → 需加强 prompt 引导或增加 few-shot 示例
- ⚠️ Teacher 跳过工具直接回答 >30% → system prompt 需强制约束工具使用
- ❌ 格式合规 <70% 或答案正确 <40% → 评估 prompt 改进空间，若仍无法改善则停止

**预计耗时**: 2-3 天 | **预计成本**: $5-15（40 条轨迹 × $0.05-0.30/条）

---

### Pilot Exp-3: DocVerify++ 过滤有效性 → 验证 H3

> **核心问题**: DocVerify++-lite 能否有效区分"证据支持"和"证据不支持"的轨迹？

**前提**: H1 + H2 通过，已有 ~40 条 Teacher 轨迹

**规模**: 对 Exp-2 产出的 40 条轨迹全量运行 DocVerify++-lite

**实验方法**:
1. 对每条轨迹的 final answer 执行 claim decomposition（拆解为原子声明）
2. 用轨迹中的 evidence_refs 做 evidence retrieval（直接使用，不做额外检索）
3. 对每个 claim-evidence 对执行 support judgment（规则 + NLI）
4. 综合判断轨迹级 support label 和 sufficiency label
5. **人工标注 40 条轨迹的 ground truth support label** 作为对照

**评估指标**:

| 指标 | 定义 | 通过门槛 |
|------|------|:--------:|
| Support 判断 precision | 自动标注 "SUPPORTED" 中确实 supported 的比例 | ≥80% |
| Support 判断 recall | 人工标注 supported 中被自动识别的比例 | ≥70% |
| Unsupported 识别率 | 人工标注 unsupported 中被自动捕获的比例 | ≥60% |
| 过滤前/后 unsupported 率 | 过滤前 vs 过滤后 unsupported answer 比例变化 | 下降 ≥25% |
| Sufficiency 判断准确率 | 充分/不充分的判断与人工一致的比例 | ≥65% |

**关键观察点**:
- 主要的误判类型是什么？（false positive: 标为 supported 但实际不是 / false negative: 标为 unsupported 但实际是）
- 哪些 claim 类型最容易误判？（数值 / 比较 / 推理 / 定性描述）
- NLI 模型的瓶颈在哪里？

**判定逻辑**:
- ✅ Precision ≥80% + unsupported 下降 ≥25% → H3 成立
- ⚠️ Recall <70% 但 precision 高 → 保守过滤策略可行（只过滤高置信度 unsupported）
- ⚠️ Sufficiency <65% → sufficiency 判断降级为分析工具，不参与过滤
- ❌ Precision <70% → DocVerify++ 不可靠，降为分析/可视化工具

**预计耗时**: 3-4 天（含人工标注 40 条 ground truth）

---

### Pilot Exp-4: 轨迹多样性分析 → 验证 H4

> **核心问题**: 合成轨迹是否高度同质，还是有足够的工具组合和推理路径多样性？

**前提**: H2 通过，已有 ~40 条 Teacher 轨迹

**规模**: 对 Exp-2 产出的 40 条轨迹做统计分析（可与 Exp-3 并行）

**分析维度**:

| 分析 | 方法 | 关注指标 |
|------|------|---------|
| 工具序列多样性 | 提取所有轨迹的 action sequence，计算 unique 序列比例 | unique 序列 / 总轨迹 ≥50% |
| 工具覆盖度 | 统计 10 个 action 各自在轨迹中的出现频率分布 | ≥7/10 action 被使用 |
| 步数分布 | 轨迹长度分布的方差 | 不应过度集中（std ≥1.5） |
| 任务类型 × 工具路径交叉表 | 不同任务类型对应的典型工具组合 | 各任务类型应有区分度 |
| 搜索策略多样性 | 不同 search query 的语义重复率 | 语义重复率 <30% |
| 与 Rule-based 模板的偏离度 | 多少轨迹与预定义模板高度匹配 | 偏离率 ≥40% |

**判定逻辑**:
- ✅ Unique 序列 ≥50% + action 覆盖 ≥7/10 → H4 成立
- ⚠️ 轨迹高度同质 → 需增加采样温度 / 多 Teacher 混合 / 引入 MCTS
- ❌ 所有轨迹几乎相同（unique <20%）→ Teacher Rollout 策略失败，需根本性调整

**预计耗时**: 1 天（脚本分析为主）

---

### Pilot Exp-5: 迷你 SFT 收益验证 → 验证 H5

> **核心问题**: 用轨迹数据做 SFT 是否比 answer-only SFT 有可观测的工具使用/证据支持提升？

**前提**: H1-H4 通过。此实验规模较大，仅在前 4 个假设全通过后执行。

**规模**: 使用 ~40 条高质量轨迹 + ~40 条 answer-only 对照数据

**实验方法**:
1. 基座模型: Qwen2.5-VL-7B（或同级别开放 VLM）
2. 两组对比 SFT:
   - **Baseline**: 40 个 question-answer 对（answer-only SFT）
   - **Treatment**: 40 条 ReAct 轨迹（DocWorldTrace SFT）
3. 评估: 在 **10 个 held-out 文档问题** 上做 inference，给定 DocEnv 工具

**评估指标**:

| 指标 | 定义 | 预期方向 |
|------|------|:--------:|
| 工具调用率 | inference 时主动使用工具的比例 | Treatment >> Baseline |
| 工具格式正确率 | 工具调用参数格式正确的比例 | Treatment > Baseline |
| 答案 F1 | 最终答案质量 | Treatment ≥ Baseline |
| 证据引用率 | 回答时附带 evidence_refs 的比例 | Treatment >> Baseline |
| 拒答行为 | 对 unanswerable 问题的处理 | Treatment 应有 refuse |

> **注意**: 40 条数据的 SFT 不应期望大幅性能提升。关键是观察**行为差异信号**（是否使用工具、是否引用证据、是否尝试拒答），而非绝对性能。

**通过标准**:
- ✅ 观察到 Treatment 组明确使用工具、引用证据的行为，Baseline 组则不使用 → H5 初步成立
- ⚠️ 行为差异微弱 → 需扩大数据量到 200+ 条后再评估
- ❌ 完全无差异 → 轨迹数据对 SFT 无价值，转向 benchmark/resource 叙事

**预计耗时**: 3-4 天（SFT 训练 + 评估）

**当前 Pilot 实现状态（2026-04-27）**:

当前仓库已实现 H5 的数据准备与 proxy/readiness 评估层，真实 SFT 训练仍需在 GPU 服务器上接入具体开源基座模型后执行。

已生成的 H5 文件：

| 文件 | 含义 |
|---|---|
| `data/h5/sft_v4/answer_only_train.jsonl` | answer-only SFT 训练集，只监督 `answer/refuse` 终止动作 |
| `data/h5/sft_v4/trajectory_train.jsonl` | trajectory SFT 训练集，监督逐步 ReAct 工具 action |
| `data/h5/sft_v4/answer_only_eval.jsonl` | answer-only held-out 对照集 |
| `data/h5/sft_v4/trajectory_eval.jsonl` | trajectory held-out 对照集 |
| `data/h5/sft_v4/summary.json` | SFT 数据统计 |
| `data/h5/eval_v4/summary.json` | H5 proxy/readiness 评估 |

当前数据规模：

| 数据 | 数量 |
|---|---:|
| DocVerify++ keep rollout | 80 |
| unique seed | 20 |
| train rollout | 56 |
| eval rollout | 24 |
| answer-only train sample | 56 |
| trajectory train next-action sample | 162 |
| answer-only eval sample | 24 |
| trajectory eval next-action sample | 72 |

当前 H5 proxy/readiness 结果：

| 指标 | 结果 |
|---|---:|
| H5 proxy passed | `true` |
| answer-only terminal target rate | 100.00% |
| trajectory non-terminal target rate | 65.43% |
| trajectory core tool coverage | `answer, compute, parse_table, read_page, refuse, search, verify` |
| no-tool adjusted answer correct | 32.50% |
| DocEnv-agent adjusted answer correct | 100.00% |
| no-tool direct answer rate | 100.00% |
| DocEnv-agent direct answer rate | 0.00% |

解释：当前结果不能替代真实 SFT 训练结论，但说明 H5 的训练数据已经具备清晰的监督差异：answer-only 数据只教终止答案，trajectory 数据显式教非终止工具调用、证据读取、计算、验证和拒答。下一步真实 H5 需要固定同一个 base model，分别用 `answer_only_train.jsonl` 和 `trajectory_train.jsonl` 微调，并在 held-out split 上比较工具使用率、格式正确率、证据支持率与答案正确率。

---

## 执行计划

```text
             Week 1                    Week 2              Week 3
    ┌──────────────────┐     ┌───────────────────┐    ┌──────────┐
    │ Exp-1: DocEnv    │     │ Exp-3: DocVerify  │    │ Exp-5:   │
    │ 环境可行性 (H1) │────▶│ 过滤有效性 (H3)  │───▶│ SFT 收益 │
    │ 3-4d             │     │ 3-4d              │    │ (H5)     │
    └──────────────────┘     └───────────────────┘    │ 3-4d     │
            │                                          └──────────┘
            ▼                         ▲
    ┌──────────────────┐     ┌───────┘
    │ Exp-2: Teacher   │     │
    │ 轨迹生成 (H2)   │─────┤
    │ 2-3d             │     │
    └──────────────────┘     │
                             ▼
                     ┌───────────────────┐
                     │ Exp-4: 多样性分析  │
                     │ (H4) 1d (并行)     │
                     └───────────────────┘
```

**总计**: ~3 周 | **API 成本**: ~$15-30 | **人工标注**: ~2 人天（40 条轨迹质量标注）

---

## 决策树

```text
Exp-1 通过?
├─ ❌ → STOP. 重新评估技术选型或转向其他研究方向
└─ ✅ → Exp-2

Exp-2 通过?
├─ ❌ → STOP. 评估人工标注替代方案或降低自动化要求
└─ ✅ → Exp-3 (H3) + Exp-4 (H4) 并行

Exp-3 通过?
├─ ❌ → DocVerify++ 降为分析工具。论文转向 Resource-only (环境+轨迹)
└─ ✅ → 继续

Exp-4 通过?
├─ ❌ → 调整采样策略（增加温度/多 Teacher 混合），不阻塞 Exp-5
└─ ✅ → 继续

Exp-3 + Exp-4 至少一个通过?
├─ ❌ → MAJOR PIVOT. 重新审视 idea
└─ ✅ → Exp-5

Exp-5 通过?
├─ ❌ → 转向 Resource + Benchmark 叙事（数据集+环境），放弃训练 claim
└─ ✅ → 全面推进 DocWorldTrace（扩大数据规模，进入正式实验）
```

---

## Pilot 实验与论文 Claims 的映射

| Pilot Exp | 验证假设 | 论文核心 Claim | 失败后影响 |
|:---------:|:--------:|----------------|-----------|
| Exp-1 | H1 | **C3: DocEnv-lite 提供可复现环境** | 整个项目不可行 |
| Exp-2 | H2 | **C4: DocWorldTrace 数据集可被合成** | 大规模自动合成不可行 |
| Exp-3 | H3 | **C3: Verification-guided filtering 有效** | DocVerify++ 核心叙事失效 |
| Exp-4 | H4 | **C4: 数据集有多样性** | 数据质量叙事受损 |
| Exp-5 | H5 | **C5: 轨迹数据对训练有价值** | SFT 收益 claim 不成立 |

---

## 最小可行交付物 (Minimum Viable Deliverable)

即使 H5 失败，只要 H1-H3 通过，仍可产出有价值的贡献：

| 假设通过情况 | 可行叙事 | 投稿方向 |
|------------|---------|---------|
| H1-H5 全通过 | 完整 Resource + Method 论文 | ACL/EMNLP Resource / NeurIPS D&B |
| H1-H4 通过, H5 弱 | Resource + Benchmark + Quality Analysis | EMNLP Resource / Findings |
| H1-H3 通过, H4 弱 | Environment + Verification-guided Dataset | Workshop / Findings |
| H1-H2 通过, H3 失败 | DocEnv + Trajectory Dataset (无验证过滤) | Workshop |
| H1 失败 | 停止，转向其他方向 | — |
