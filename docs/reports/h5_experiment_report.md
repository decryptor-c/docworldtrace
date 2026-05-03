# H5 Experiment Report: Qwen3-VL Trajectory SFT

> 更新时间：2026-05-01  
> 目标：单独汇总 H5 阶段的实验设计、数据规模、训练结果、评测结果和典型样例。  
> 核心结论：在当前 pilot 规模下，trajectory SFT 明显优于 answer-only SFT。它不仅能生成合法 JSON，更重要的是能在真实 DocEnv closed-loop 中主动调用工具，而不是直接回答。

---

## 1. 实验问题

H5 验证的是：H2-H4 产生的多步工具轨迹，是否能作为 SFT 监督信号，让 student model 学会 DocEnv action。

实验问题：

```text
只训练最终答案，模型是否能学会工具调用？
训练完整 trajectory，是否能显著提升工具使用行为？
```

H5 不是比较不同 base model，而是同一个 base model 的两种监督方式对照。

| 对照组 | 训练目标 | 预期行为 |
|---|---|---|
| `answer_only_adapter` | 只监督最终 `answer/refuse` | 倾向直接回答或拒答 |
| `trajectory_adapter` | 监督下一步 DocEnv action | 学会 `search/read_page/parse_table/compute/verify/refuse/answer` |

Base model:

```text
Qwen3-VL-8B-Instruct
```

---

## 2. 数据构造

H5 数据来自 H2 diverse-PDF rollouts：

```text
data/h2/rollouts_diverse_v2
```

当前本地 H5 数据构建记录：

| Item | Value |
|---|---:|
| Rollout count | 162 |
| Unique seed count | 54 |
| Train / eval rollouts | 144 / 18 |
| Held-out per task | 1 |
| Output dir | `data/h5/sft_diverse_v2` |

当前本地 `summary.json` 记录为 `docverify=null, keep_all=true`。因此这版 H5 应定位为 **pilot 行为收益验证**，不是最终严格 DocVerify++ 过滤版训练集。

### 2.1 Answer-Only SFT 数据

answer-only 数据只保留每条 rollout 的最终终止动作。

| Split | Count | Terminal Rate | Actions |
|---|---:|---:|---|
| Train | 144 | 100% | `answer/refuse` |
| Eval | 18 | 100% | `answer/refuse` |

训练集目标 action 分布：

| Action | Count |
|---|---:|
| `answer` | 105 |
| `refuse` | 39 |

### 2.2 Trajectory SFT 数据

trajectory 数据把一条多步 rollout 拆成多个 next-action 样本。

| Split | Count | Non-Terminal Target Rate | Core Tool Coverage |
|---|---:|---:|---|
| Train | 427 | 66.28% | 7 / 7 |
| Eval | 50 | 64.00% | 7 / 7 |

训练集 action 分布：

| Action | Count |
|---|---:|
| `read_page` | 131 |
| `answer` | 105 |
| `search` | 76 |
| `refuse` | 39 |
| `parse_table` | 30 |
| `verify` | 27 |
| `compute` | 17 |
| `ocr` | 1 |
| `crop` | 1 |

这个分布说明 trajectory 数据不是单纯答案数据，而是包含大量非终止工具 action。

---

## 3. 训练设置

两个 adapter 使用相同 base model、相同 LoRA 设置和相同训练参数，只改变训练样本类型。

| Item | Value |
|---|---:|
| Base model | `Qwen3-VL-8B-Instruct` |
| Method | LoRA SFT |
| Epochs | 2 |
| Max length | 4096 |
| Per-device batch size | 1 |
| Gradient accumulation | 8 |
| Learning rate | 2e-4 |
| Precision | bf16 |
| 4-bit loading | true |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |

训练输出：

| Adapter | Output |
|---|---|
| `answer_only_adapter` | `runs/h5_qwen3_vl_diverse_v2/answer_only_adapter` |
| `trajectory_adapter` | `runs/h5_qwen3_vl_diverse_v2/trajectory_adapter` |

训练日志显示两组 adapter 都正常收敛。

| Adapter | Global Steps | Last Logged Train Loss | Final Eval Loss |
|---|---:|---:|---:|
| `answer_only_adapter` | 36 | 0.2657 | 0.2511 |
| `trajectory_adapter` | 108 | 0.2013 | 0.1927 |

---

## 4. Next-Action Eval

next-action eval 是 teacher-forcing 风格：给模型已有 query、history 和 observation，看模型能否预测下一步 action。

| Evaluation | Count | Format Valid | Action Match | Generated Non-Terminal | Target Non-Terminal Covered |
|---|---:|---:|---:|---:|---:|
| answer-only on answer-only eval | 18 | 100% | 100% | 0% | 0% |
| answer-only on trajectory eval | 50 | 100% | 38% | 14% | 21.88% |
| trajectory on answer-only eval | 18 | 100% | 16.67% | 0% | 0% |
| trajectory on trajectory eval | 50 | 100% | 98% | 66% | 100% |

关键对比是同一组 `trajectory_eval`：

| Adapter | Action Match | Generated Non-Terminal | Target Non-Terminal Covered |
|---|---:|---:|---:|
| `answer_only_adapter` | 38% | 14% | 21.88% |
| `trajectory_adapter` | 98% | 66% | 100% |

解释：

```text
answer-only adapter 学会了终止动作，但没有学会中间工具动作。
trajectory adapter 能正确预测 search/read_page/parse_table/compute/verify 等下一步 action。
```

---

## 5. Closed-Loop DocEnv Eval

closed-loop eval 更严格：模型必须自己输出 action，DocEnv 执行真实工具，然后把 observation 反馈给模型，直到模型终止或达到步数上限。

当前 closed-loop 使用 H5 held-out eval split，每个 adapter 6 条 seed，共 12 条交互轨迹。

### 5.1 Overall

| Metric | Value |
|---|---:|
| Count | 12 |
| Format compliance | 91.67% |
| Proper termination | 83.33% |
| Adjusted answer correct | 58.33% |
| Mean answer F1 | 59.85% |
| Direct answer rate | 41.67% |
| Non-terminal tool use rate | 50.00% |
| Acceptable path rate | 41.67% |

### 5.2 By Adapter

| Adapter | Count | Format Valid | Proper Termination | Adjusted Correct | Non-Terminal Tool Use | Required Tool Coverage | Acceptable Path | Direct Answer |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `answer_only_adapter` | 6 | 83.33% | 83.33% | 33.33% | 0% | 0% | 0% | 83.33% |
| `trajectory_adapter` | 6 | 100% | 83.33% | 83.33% | 100% | 50% | 83.33% | 0% |

trajectory 相对 answer-only 的提升：

| Metric | Delta |
|---|---:|
| Adjusted answer correct | +50.00 pp |
| Non-terminal tool use | +100.00 pp |
| Required tool coverage | +50.00 pp |
| Acceptable path | +83.33 pp |
| Direct answer | -83.33 pp |

结论：trajectory adapter 在真实 DocEnv 交互中显著减少直接回答，并且主动调用工具。

---

## 6. 验证样例

详细轨迹对比见：

```text
h5_closed_loop_trajectory_comparison.md
```

关键样例：

| Task | Answer-Only Path | Trajectory Path | Outcome |
|---|---|---|---|
| cross-page | `answer` | `search -> read_page -> read_page -> answer` | trajectory correct |
| verification | `answer` | `read_page -> verify -> answer` | trajectory path valid |
| table_lookup | `answer` | `parse_table -> answer` | trajectory correct |
| numeric_computation | format error | `parse_table -> compute -> answer` | trajectory correct |
| text_lookup | `answer` | `read_page -> answer` | trajectory correct |
| unanswerable | `refuse` | `search x8` | trajectory budget exhausted |

---

## 7. H5 结论

H5 通过 pilot 验收，但结论边界需要写清楚。

可以支持的结论：

```text
trajectory SFT 能显著改变 Qwen3-VL 的行为，使其在 DocEnv 中主动调用工具。
answer-only SFT 主要学习终止动作，不能稳定产生中间工具路径。
```

最准确的展示表述：

```text
H5 在 pilot 规模下验证了 trajectory supervision 的有效性：
next-action eval 中 action match 从 38% 提升到 98%；
closed-loop eval 中 adjusted correct 从 33.33% 提升到 83.33%，
non-terminal tool use 从 0% 提升到 100%。
```

---

## 8. 当前问题和下一步

| 问题 | 证据 | 影响 |
|---|---|---|
| closed-loop eval 样本量小 | 只有 6 条 held-out seed per adapter | 适合 pilot 结论，不适合大规模泛化声明 |
| refuse 停止策略弱 | unanswerable seed 重复 `search` 到 budget exhausted | 需要补强 negative evidence -> refuse 轨迹 |
| 当前训练集 `keep_all=true` | 本地 summary 中 `docverify=null` | 后续需要使用完整 DocVerify++ keep/reject 文件重建 SFT 数据 |

下一步：

```text
使用 V3 refuse-augmented seeds 扩大 held-out closed-loop eval，
并强化 negative evidence -> bounded search -> refuse 的训练路径。
```

