# 预期实验数据集与预期结果

> **目标**: 定义 DocWorldTrace 的实验设计，包括数据集构建规模、评测基准、对比实验、评测指标、预期 claims 和风险降级。

---

## 1. 实验数据集

### 1.1 Pilot 数据规模

| 项目 | Pilot 规模 | 说明 |
|---|---:|---|
| PDF 文档 | 40-60 篇 | arXiv 科学论文 + SEC/EDGAR 金融年报，优先数字化 PDF |
| QA 种子 | 100-200 个 | 每篇 2-4 个问题，覆盖 6 类任务 |
| 轨迹候选 | 2K-5K 条 | 每题多策略 rollout |
| 过滤后轨迹 | 1K-3K 条 | 通过 DocVerify++ 与工具审计 |
| 人工审核 | 150-300 条 | 校准 reward/filter 精度 |

### 1.2 文档来源

| 来源 | 类型 | 选择理由 |
|------|------|---------|
| arXiv (cs.*) | 科学论文 | 高 OCR 质量、含丰富表格和图表、多页结构 |
| SEC/EDGAR 10-K | 金融年报 | 高数值密度、复杂表格、跨页引用、行业标准 |

### 1.3 工具集合

Pilot 固定 7+2 个工具（7 个核心 + answer/refuse 终止动作）：

| 工具 | 必选 | 说明 |
|---|:---:|---|
| `search` | ✓ | BM25/embedding/ColPali 任一实现 |
| `read_page` | ✓ | OCR 文本 + 页面图像摘要 |
| `crop` | ✓ | 根据 bbox 裁剪页面区域 |
| `ocr` | ✓ | 对 page/bbox/crop 做文本识别 |
| `parse_table` | ✓ | 表格结构提取 |
| `compute` | ✓ | Python/表达式计算，禁止外部 IO |
| `verify` | ✓ | DocVerify++ support/sufficiency 判断 |

`parse_chart` 放入 Phase 2，因为 chart-to-data 与 legend grounding 风险较高。

### 1.4 任务分布

| 任务类型 | 比例 | 目标验证 |
|---|---:|---|
| Text lookup | 25% | search/read/ocr 工具链 |
| Table lookup | 20% | parse_table + source cell |
| Numeric computation | 20% | parse_table + compute |
| Cross-page reasoning | 15% | evidence memory 积累 |
| Verification / claim support | 10% | DocVerify++ 动作 |
| Unanswerable / refusal | 10% | sufficiency / refusal 能力 |

### 1.5 外部评测基准

| 基准 | 特点 | 评估目的 |
|------|------|---------|
| DocVQA | 单页文档 QA | 基础 QA 能力 |
| MP-DocVQA | 多页文档 QA | 跨页检索能力 |
| MMLongBench-Doc | 长文档 + unanswerable | 复杂推理 + 拒答 |
| DUDE | 工业文档理解 | 领域泛化 |
| SlideVQA | 幻灯片理解 | 视觉理解 |

---

## 2. 实验设计

### 2.1 数据质量实验

验证 DocWorldTrace 数据本身的质量：

| 实验 | 指标 |
|---|---|
| Tool execution validity | valid action rate / parameter success rate |
| Evidence grounding quality | bbox validity / evidence support rate |
| DocVerify++ filter precision | 人工审核 precision / recall |
| Trajectory diversity | tool sequence diversity / task type coverage |
| Failure taxonomy | retrieval_miss / bbox_wrong / numeric_mismatch / over_refusal 分布 |

### 2.2 过滤有效性实验

| 对比设置 | 检验目标 |
|---------|---------|
| 未过滤 teacher 轨迹 vs DocVerify++-lite filtered 轨迹 | unsupported claim 下降幅度 |
| 未过滤 vs filtered | early answer / wrong refuse / over_search 下降幅度 |

### 2.3 下游训练实验

| 设置 | 训练数据 | 目标 |
|---|---|---|
| Answer-only SFT | question-answer | 检验普通 QA SFT 下限 |
| ReAct teacher SFT | 未过滤 teacher 轨迹 | 检验 teacher distillation |
| DocWorldTrace SFT | 合成工具轨迹 | 检验工具轨迹数据价值 |
| Filtered DocWorldTrace SFT | DocVerify++ 过滤轨迹 | 检验验证引导过滤价值 |
| Filtered + hard negatives | 加入错误轨迹/拒答样本 | 检验可靠性和拒答 |

### 2.4 成本实验

| 采样方法 | 关键指标 |
|---------|---------|
| Rule-based / Teacher / Hard Negative / MCTS | 每条轨迹 token/API 成本 |
| 各方法 | 平均工具调用数 |
| MCTS | 缓存命中率、unique action 数 |

---

## 3. 评测指标体系

| 指标 | 说明 | 评估维度 |
|---|---|---|
| Answer Accuracy / F1 / ANLS | 最终答案质量 | Outcome |
| Evidence Support Rate | 输出引用证据是否支持答案 | Faithfulness |
| Grounding Accuracy | page/bbox/cell 定位质量 | Evidence |
| Tool Success Rate | 工具调用格式和参数成功率 | Tool |
| Step Efficiency | 平均步数、无效工具调用比例 | Efficiency |
| Refusal F1 | 不可回答问题上的 answer/abstain 判断 | Safety |
| Faithfulness Gap | 答案正确但证据不支持的比例 | Reliability |

---

## 4. Baselines

| Baseline | 目的 | 类型 |
|---|---|---|
| Direct VLM | 无工具直接回答 | 下限 |
| Vanilla RAG | 单轮检索 + 回答 | 简单检索 |
| ReAct Search-only | 只允许 search/read_page | 工具受限 |
| ReAct Search+Crop | 加入视觉细读 | 扩展工具 |
| Teacher Trajectory SFT | 闭源 teacher 轨迹蒸馏 | Teacher 对照 |
| DocVerify++ Post-hoc | 只做事后验证，不参与训练 | 验证对照 |
| **DocWorldTrace SFT** | 完整合成轨迹训练 | **主方法** |
| **DocWorldTrace + Verification Filter** | 过滤后轨迹训练 | **主方法增强** |

---

## 5. 预期结果与论文 Claims

### 可验证 Claims

1. **轨迹数据优于 answer-only 数据** — DocWorldTrace SFT 在工具调用成功率、证据支持率和复杂文档 QA 上优于 answer-only SFT
2. **DocVerify++ 过滤提升忠实性** — Filtered DocWorldTrace 降低 unsupported answer / faithfulness gap
3. **文档工具环境可复现且成本可控** — DocEnv-lite 允许缓存工具输出，生成轨迹成本低于全闭源 teacher rollout
4. **拒答行为可通过 sufficiency reward 改善** — 加入 insufficiency/refusal 样本后，unanswerable/refusal F1 提升

### 预期性能趋势

```text
Answer F1:     Direct VLM < Vanilla RAG < ReAct Search < DocWorldTrace SFT ≤ Filtered
Tool Success:  Answer-only << ReAct teacher < DocWorldTrace < Filtered DocWorldTrace
Evidence Support: Answer-only << ReAct teacher < DocWorldTrace < Filtered DocWorldTrace
Refusal F1:    所有无拒答训练方法 << DocWorldTrace + hard negatives
```

**不应强调绝对 SOTA**，聚焦可复现性、忠实性和工具效率的相对提升。

---

## 6. 风险与降级方案

| 风险 | 预警信号 | 降级方案 |
|---|---|---|
| parse_table 质量不稳定 | table task support rate <60% | Phase 1 只保留 OCR text/table markdown |
| DocVerify++ filter 误判多 | 人工审核 precision <75% | 只用 filter 做分析，不作为训练筛选 |
| 轨迹 SFT 效果不显著 | 工具成功率提升 <5% | 转向 dataset/benchmark/resource 叙事 |
| 生成轨迹自然性不足 | 人工评分 <3/5 | 增加 teacher rewrite |
| RL 成本过高 | rollout 速度不可控 | 只做 SFT + offline reward analysis |

---

## 7. Pilot 验收门槛

| 门槛 | 目标值 | 含义 |
|------|:---:|------|
| Tool execution valid rate | ≥90% | 工具调用足够稳定 |
| 人工审核 evidence support precision | ≥80% | 过滤信号可作为质控依据 |
| Unsupported answer 下降 | ≥25% | 过滤确实改善忠实性 |
| SFT 后工具成功率或证据支持率提升 | ≥5% | 轨迹数据对训练有可观测收益 |

失败降级策略：
- SFT 收益不足 → 转向 Resource + Benchmark + Quality Analysis 叙事
- DocVerify++-lite precision 不足 → 仅作为离线分析工具
- parse_table 质量不足 → 限制为 OCR text/table markdown
