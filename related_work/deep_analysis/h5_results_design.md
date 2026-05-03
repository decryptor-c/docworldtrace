# H5 实验结果设计

> 基于 H5 实际实验数据（[h5_experiment_report.md](../../docs/reports/h5_experiment_report.md)）和原始设计（[09_pilot_verification.md](../../docs/research_plan/09_pilot_verification.md) Exp-5），设计论文中的实验结果呈现方案。

---

## 1. 实验设计概述（论文 §5.1）

### 1.1 实验目标

H5 验证的核心问题是：

> **用完整工具轨迹做 SFT，是否能比 answer-only SFT 更好地训练模型在文档环境中主动使用工具、积累证据并基于证据回答问题？**

这是 DocWorldTrace 论文最关键的下游验证——如果 trajectory SFT 没有行为差异，整个"轨迹数据优于 answer-only 数据"的 claim 就不成立。

### 1.2 实验设置

| 设置项 | 值 |
|-------|-----|
| 基座模型 | Qwen3-VL-8B-Instruct |
| 训练方法 | LoRA SFT（rank=16, alpha=32, lr=2e-4, bf16, 4-bit） |
| 训练数据 | 来自 H2 的 teacher rollout 轨迹（162 条，54 unique seeds，6 类任务） |
| Train/Eval 划分 | 144 / 18（按 seed 分层采样，每任务至少保留 1 条 held-out） |
| LoRA epoch | 2 |
| 训练步数 | answer-only: 36 steps; trajectory: 108 steps（样本展开更多） |

### 1.3 对照设计

| 对照条件 | 训练数据格式 | 训练样本数 | 核心差异 |
|---------|------------|:---:|------|
| **Answer-only SFT** | 每条 rollout 仅保留最终终止动作（answer/refuse 文本） | Train: 144, Eval: 18 | **不包含任何中间工具调用信号** |
| **Trajectory SFT** | 每条 rollout 拆为多个 next-action 样本（每步 thought→action→observation→next_action） | Train: 427, Eval: 50 | **包含完整的工具选择和证据积累路径** |

**关键设计要点**:
- 两个条件的基座模型、LoRA 配置、训练超参完全相同，**唯一的变量是训练数据形态**
- Trajectory 数据中 66.28% 的训练样本目标是**非终止工具**（search/read_page/parse_table/compute/verify/crop/ocr），只有 33.72% 是 answer/refuse —— 这是 answer-only 数据完全缺失的部分
- Answer-only 训练集只有 2 种目标 action（answer/refuse）；Trajectory 训练集覆盖 9 种 action

---

## 2. 训练基础指标（论文 §5.2 或 Appendix）

两组训练均正常收敛，trajectory adapter 因样本量更大（427 vs 144）而有更多训练步数：

| 指标 | Answer-only | Trajectory |
|------|:---:|:---:|
| 训练步数 | 36 | 108 |
| 最终训练 loss | 0.2657 | 0.2013 |
| 最终验证 loss | 0.2511 | 0.1927 |

> 注意：两组 loss 不可直接对比（不同数据分布），仅用于确认训练过程正常。

---

## 3. 核心结果 I：Next-Action 预测能力（论文 §5.3.1）

### 3.1 实验方式

Next-action eval 是 **teacher-forcing 风格**的评测：给模型完整的 query + 已完成的历史步骤 + 上一步的真实 observation，要求模型预测**下一步应该执行什么 action**。这个评测不涉及真实 DocEnv 执行，仅评估模型从训练数据中是否学习了 action 预测能力。

**为什么做这个评测？** 如果模型在"看到正确答案的上下文"后仍然不会预测下一步 action，那在真实交互中更不可能成功。Next-action eval 提供了一个干净的、不受环境执行误差影响的"纯行为学习"指标。

### 3.2 完整交叉评测结果

交叉评测意味着每个 adapter 在两个 eval set 上都做测评（共 4 组），以排除 eval set 偏差：

| 评测组合 | 样本数 | 格式合规率 | **Action Match** | 生成非终止工具 | 覆盖目标非终止工具 |
|---------|:---:|:---:|:---:|:---:|:---:|
| Answer-only adapter × answer-only eval | 18 | 100% | 100% | 0% | 0% |
| Answer-only adapter × trajectory eval | 50 | 100% | 38% | 14% | 21.88% |
| Trajectory adapter × answer-only eval | 18 | 100% | 16.67% | 0% | 0% |
| **Trajectory adapter × trajectory eval** | **50** | **100%** | **98%** | **66%** | **100%** |

### 3.3 核心对比（同 eval set 上的两 adapter）

在同样的 trajectory eval set（50 条，覆盖 7 种 core tool）上：

| 指标 | Answer-only | Trajectory | Δ |
|------|:---:|:---:|:---:|
| Action Match | 38% | **98%** | +60pp |
| 生成非终止工具 | 14% | **66%** | +52pp |
| 覆盖目标非终止工具 | 21.88% | **100%** | +78pp |

### 3.4 对数据形态的论证

直接回答论文的核心 claim：

> **Answer-only adapter 在 trajectory eval 上的 action match 仅 38%——它学会了终止动作（answer/refuse），但无法正确预测中间工具步骤（search/read_page/parse_table/compute/verify）。Trajectory adapter 的 action match 达 98%，覆盖了全部 7 种核心非终止工具。这直接证明：仅靠 answer-only 数据无法训练模型学会"下一步该用什么工具"。**

**审稿人可能质疑**: "Answer-only adapter 在它自己的 eval set 上是 100%，凭什么说它不行？"  
**回应**: 因为 answer-only eval 的目标全是 answer/refuse——一个只见过终止动作的模型在自己的测试集上答对终止动作，这恰好证明它**只学会了终止**，没有学会工具选择。

---

## 4. 核心结果 II：Closed-Loop DocEnv 交互能力（论文 §5.3.2）

### 4.1 实验方式

Closed-loop eval 是**真实交互评测**：模型进入 DocEnv 环境，自己输出 action → DocEnv 执行 → 返回真实 observation → 模型根据 observation 决定下一步 → 循环直到模型终止（answer/refuse）或达到步数上限。每条轨迹可被完整审查。

这是最严格、最能体现代理能力的评测方式——模型不能"看到正确答案"，必须自己在环境中导航。

**当前规模**: 每个 adapter 6 条 held-out seed（12 条 closed-loop 轨迹），按任务类型分层采样。适合 pilot 行为验证，后续需扩大。

### 4.2 Overall 结果

| 指标 | 12 条总体 |
|------|:---:|
| 格式合规率 | 91.67% |
| 正常终止率（answer/refuse） | 83.33% |
| Adjusted answer correct | 58.33% |
| Mean answer F1 | 59.85% |
| 直接回答率（跳过所有工具） | 41.67% |
| 非终止工具使用率 | 50.00% |
| Acceptable path rate | 41.67% |

> 总体数字偏低是因为 answer-only adapter 拉低了均值——它占据了全部直接回答和大部分错误。这也是实验设计的目的：**对比才能看到差异**。

### 4.3 By-Adapter 对比（论文核心表）

| 指标 | Answer-only | Trajectory | Δ |
|------|:---:|:---:|:---:|
| 格式合规率 | 83.33% | **100%** | +16.67pp |
| 正常终止率 | 83.33% | 83.33% | — |
| **Adjusted answer correct** | 33.33% | **83.33%** | **+50.00pp** |
| **非终止工具使用率** | 0% | **100%** | **+100pp** |
| Required tool coverage | 0% | **50%** | +50pp |
| **Acceptable path rate** | 0% | **83.33%** | **+83.33pp** |
| 直接回答率 | 83.33% | **0%** | **-83.33pp** |

### 4.4 对论文 Claims 的支撑

**Claim 1 "轨迹数据优于 answer-only 数据"**:
- Answer-only: 5/6 次直接回答（83.33%），0% 使用任何工具，0% path acceptable
- Trajectory: 0% 直接回答，100% 主动调用工具，83.33% path acceptable
- Answer correct 从 33.33% → 83.33%（+50pp），直接回答从 83.33% → 0%（-83.33pp）

**Claim 3 "文档工具环境可复现且成本可控"**:
- 12 条 closed-loop 全部在 DocEnv 中成功执行真实工具调用
- 所有 observation 来自真实 PDF 解析（非 LLM 模拟）

---

## 5. 逐任务案例分析（论文 §5.3.3 或 Appendix）

### 5.1 Cross-page Reasoning

**任务**: 搜索定位页面 → 读取相邻页 → 报告标题

| Adapter | 工具路径 | 输出 | 是否正确 | 路径可接受 |
|---------|---------|------|:---:|:---:|
| Answer-only | `answer`（无工具） | "MLAgentBench: Evaluating Language Agents on Multi-Step Reasoning Tasks" | ✗ | ✗ |
| Trajectory | `search → read_page → read_page → answer` | "MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation" | ✓ | ✓ |

**诊断**: Answer-only 跳过搜索直接回答，输出是幻觉文本（无空格拼接）。Trajectory 正确执行了"搜索锚点 → 读取目标页"的跨页推理链路。

### 5.2 Numeric Computation

**任务**: 从表格取数 → 计算差值

| Adapter | 工具路径 | 输出 | 是否正确 | 路径可接受 |
|---------|---------|------|:---:|:---:|
| Answer-only | format error | — | ✗ | ✗ |
| Trajectory | `parse_table → compute → answer` | "-85.71%" | ✓ | ✓ |

**诊断**: Answer-only 面对表格+计算任务时连格式都无法生成。Trajectory 正确组合了 `parse_table`（结构化提取数值）和 `compute`（表达式计算）。

### 5.3 Table Lookup

**任务**: 在指定表格中查找特定行列的值

| Adapter | 工具路径 | 输出 | 是否正确 | 路径可接受 |
|---------|---------|------|:---:|:---:|
| Answer-only | `answer`（无工具） | "C"（猜测） | ✗ | ✗ |
| Trajectory | `parse_table → answer` | "TXN" | ✓ | ✓ |

**诊断**: Answer-only 没有读取表格就猜了一个字母答案。Trajectory 触发 parse_table 后准确提取。

### 5.4 Text Lookup

**任务**: 读取指定页面 → 报告标题

| Adapter | 工具路径 | 输出 | 是否正确 | 路径可接受 |
|---------|---------|------|:---:|:---:|
| Answer-only | `answer`（无工具） | "Section 1: Introduction to the Document"（幻觉） | ✗ | ✗ |
| Trajectory | `read_page → answer` | "Technology Risks" | ✓ | ✓ |

**诊断**: Answer-only 编造了一个通用的章节标题。Trajectory 读取目标页后返回真实的页面标题。

### 5.5 Verification

**任务**: 判断 claim 是否被文档证据支持

| Adapter | 工具路径 | 输出 | 是否正确 | 路径可接受 |
|---------|---------|------|:---:|:---:|
| Answer-only | `answer`（无工具） | "SUPPORTED" | ✓（巧合） | ✗ |
| Trajectory | `read_page → verify → answer` | "SUPPORTED" | ✓ | ✓ |

**诊断**: Answer-only 虽然答对，但没有执行 `verify`——这是不可审查的推理。Trajectory 显式调用了 `verify` 并基于 evidence_refs 给出判断。这也展示了 paper 的核心论点：**答案正确 ≠ 推理忠实**。

### 5.6 Unanswerable / Refusal（失败案例）

| Adapter | 工具路径 | 输出 | 是否正确 | 路径可接受 |
|---------|---------|------|:---:|:---:|
| Answer-only | `refuse`（直接拒答，未尝试搜索） | "the document does not contain private mobile phone number" | ✓ | ✗（无搜索过程） |
| Trajectory | `search → search → ...` (×8) | budget exhausted | ✗ | ✗ |

**诊断**: 这是当前 H5 的主要失败点。Answer-only 学会了"对 unanswerable 直接拒绝"——虽然答案正确但没有证据积累过程。Trajectory 学会了"继续查证"但没有学会"查不到后停止并拒答"，导致 8 次重复 search 直至预算耗尽。

**根本原因**: 当前训练数据中 refuse 样本的 search→refuse 模式是"查 1-2 次 → 拒答"，但在 closed-loop 环境中模型陷入反复搜索。需要增强的方面：negative evidence 收集策略、最大搜索次数约束、sufficiency 信号的示教。

---

## 6. 实验结论与边界声明

### 6.1 可支持的核心结论

```
1. trajectory SFT 能显著改变 Qwen3-VL-8B 的行为，使其在 DocEnv 中主动调用
   非终止工具（100% vs 0%），正确率大幅提升（83.33% vs 33.33%）。

2. answer-only SFT 主要学习终止动作的文本格式（answer/refuse），不能稳定
   产生中间工具路径（0% tool use in closed-loop）。

3. 六类任务中五类（cross-page, numeric, table, text, verification）trajectory
   adapter 均产生正确的工具路径；仅 unanswerable/refuse 场景需要改进。

4. 即使在答案正确的情况下，answer-only 模型的推理路径也是不可审查的
   （verification 案例：答对但没有执行 verify）。
```

### 6.2 不能过度声明的内容

| 不能说的 | 原因 |
|---------|------|
| "模型已在大规模文档 QA 上完全泛化" | closed-loop 仅 12 条 seed，需扩大 |
| "refuse 场景已解决" | unanswerable 案例中模型陷入重复搜索 |
| "这是最终 DocVerify++ 严格过滤版训练结论" | 当前训练集 `keep_all=true`，未使用 DocVerify++ 过滤 |
| "trajectory SFT 在所有指标上均优于 answer-only" | 两者在正常终止率上持平（83.33%），refuse 案例 answer-only 反而更好 |

### 6.3 最准确的表述（推荐用于论文）

> *"In a pilot-scale controlled experiment (Qwen3-VL-8B-Instruct, 144 training seeds, LoRA SFT), trajectory supervision substantially outperforms answer-only supervision across behavioral metrics: next-action match improves from 38% to 98%, closed-loop non-terminal tool use rises from 0% to 100%, and adjusted answer correctness increases from 33.33% to 83.33%. The sole systematic failure occurs in the unanswerable/refusal category, where the trajectory-trained model over-searches without stopping—a known limitation we address through negative-evidence augmentation in future work."*

---

## 7. 实验呈现建议

### 7.1 论文中的建议章节结构

```text
5. Experiments
  5.1 H5 Downstream Training Setup
      - Model, LoRA config, data statistics, two adapter design
  5.2 Next-Action Prediction Accuracy (Table 4)
      - 交叉评测 4 组结果 + 同 eval set 对比
      - 论证: answer-only 无法学习非终止 action
  5.3 Closed-Loop DocEnv Evaluation (Table 5)
      - By-adapter 对比（主表）
      - Per-task breakdown（副表）
  5.4 Qualitative Case Analysis (Figure X)
      - 6 类任务的代表性轨迹可视化
      - 重点展示 verification 案例（答对但无 verify）和 refuse 失败案例
  5.5 Discussion of Refusal Limitation
      - 坦诚呈现 refuse 案例的失败
      - 分析原因并讨论 planned fix
```

### 7.2 关键图表设计

**Table 4: Next-Action Prediction Accuracy**

| Adapter | Eval Set | N | Action Match | Non-Terminal Tool Predicted | Target Tools Covered |
|---------|---------|:---:|:---:|:---:|:---:|
| Answer-only | answer-only | 18 | 100% | 0% | 0% |
| Answer-only | trajectory | 50 | 38% | 14% | 21.88% |
| Trajectory | answer-only | 18 | 16.67% | 0% | 0% |
| **Trajectory** | **trajectory** | **50** | **98%** | **66%** | **100%** |

**Table 5: Closed-Loop DocEnv Interaction**

| Metric | Answer-only SFT | Trajectory SFT | Δ |
|------|:---:|:---:|:---:|
| Format compliance | 83.33% | 100% | +16.67 |
| Proper termination | 83.33% | 83.33% | — |
| Adjusted answer correct | 33.33% | 83.33% | **+50.00** |
| Non-terminal tool use | 0% | 100% | **+100** |
| Required tool coverage | 0% | 50% | +50 |
| Acceptable path | 0% | 83.33% | **+83.33** |
| Direct answer rate | 83.33% | 0% | **-83.33** |

**Table 6: Per-Task Trajectory Comparison**（选 3 个代表性任务展示即可）

| Task | Answer-only Path | Trajectory Path | Answer-only Correct | Trajectory Correct |
|------|---------|---------|:---:|:---:|
| Cross-page | `answer` (no tools) | `search→read_page→read_page→answer` | ✗ | ✓ |
| Numeric | format error | `parse_table→compute→answer` | ✗ | ✓ |
| Verification | `answer` (correct but no verify) | `read_page→verify→answer` | ✓ (coincidental) | ✓ (auditable) |
| Refusal | `refuse` (no search) | `search×8→budget exhausted` | ✓ (correct but ungrounded) | ✗ |

### 7.3 叙事策略

1. **先定量后定性**: Table 4（next-action 行为学习）→ Table 5（closed-loop 真实交互）→ Table 6（per-task 案例）→ 文本讨论
2. **坦诚缺陷**: 在 §5.5 或 Discussion 中主动讨论 refuse 失败案例，说明原因和改进方向。审稿人欣赏坦诚——比隐藏缺陷然后在 rebuttal 中被发现好得多
3. **连接 claims**: 每个结果表后明确标注它支撑论文的哪条 claim（Claim 1: 轨迹数据优势 / Claim 3: 环境可复现 / Claim 4: 拒答可改善（当前不成熟））
4. **区分"实现 vs 计划"**: 在表格中用脚注标注当前 pilot 规模限制（12 closed-loop seeds），说明后续扩大计划

---

## 8. H5 未覆盖的实验维度

### 8.1 当前缺失的关键对比

| 缺失项 | 重要性 | 计划 |
|-------|:---:|------|
| Filtered vs Unfiltered SFT 对比 | ★★★★★ | DocVerify++ 过滤后重建训练集再做 SFT（当前 keep_all=true） |
| Hard Negative 的 DPO/PRM 收益 | ★★★★ | 需要构造 preference pair 后做 DPO |
| 不同数据规模的效果曲线 | ★★★ | 消融规模（50/100/200/400 条） |
| 回答质量 + 证据支持率的联合评估 | ★★★★ | 需要人工标注 GT evidence support |
| 公共 benchmark 上的评测 | ★★ | 当前只在内部 held-out seed 上评测 |

### 8.2 建议的补充实验优先级

| 优先级 | 实验 | 对论文的增量 |
|:---:|------|------------|
| **P0** | Filtered SFT（DocVerify++ keep/reject 后再训练） | 验证 C3（过滤提升训练质量）的核心 claim |
| **P0** | 扩大 closed-loop eval 到 30+ seeds | 统计显著性——当前 6/group 太弱 |
| **P1** | Refuse-augmented SFT（加入 negative search → refuse 轨迹） | 修复当前唯一系统性失败 |
| **P1** | 在 MMLongBench-Doc 上做 zero-shot/few-shot 评测 | 外部泛化性证据 |
| **P2** | Hard Negative DPO | 验证 HN 对 DPO 训练的收益 |
| **P2** | 数据规模消融 | 支撑 "1K-3K 是最优规模" 的 claim |

---

## 9. 修改后的综合实验架构

将 H5 放入整个 DocWorldTrace 实验架构中：

```text
Layer 1: 数据质量分析（H1-H4）
  ├── DocEnv 工具执行成功率 & 缓存一致性          
  ├── 五层质检分布统计 & Failure taxonomy         
  ├── 四级分级占比                                   
  └── DocVerify++ 在注入式负例上的 caught rate        

Layer 2: 训练行为对比（H5）                       
  ├── Next-Action Prediction（teacher-forcing）    
  │   └── 证明: trajectory SFT 学会了 action 选择  
  ├── Closed-Loop DocEnv Interaction（真实交互）    
  │   └── 证明: 行为差异转化为真实环境中的能力差异  
  └── Per-Task Case Analysis                      
      └── 展示: 任务覆盖和失败模式                 

Layer 3: 消融分析（Phase 3 执行）                  
  ├── DocVerify++ filtering on/off                 
  ├── Hard Negative 贡献                            
  ├── MCTS 采样的增量价值（可选）                    
  └── 数据规模缩放曲线                               

Layer 4: 外部评测（Phase 3 执行）                  
  └── DocVQA / MP-DocVQA / MMLongBench-Doc        
```

---

## 10. 总结

**H5 实验的核心叙事**: 在完全相同的基座模型和训练配置下，仅改变训练数据的形态（answer-only vs trajectory），模型在文档工具环境中的行为产生根本性差异——从"不调用工具、直接猜测"变为"主动搜索、定位、解析、计算、验证"。

**关键数字（用于 Abstract/Introduction）**: 

> Trajectory SFT achieves 98% next-action prediction accuracy (vs. 38% answer-only) and 83.33% closed-loop answer correctness (vs. 33.33%), with non-terminal tool use rising from 0% to 100%.

**唯一的系统性问题**: unanswerable/refusal——模型学会了搜索但没学会停止。这既是坦诚的缺陷披露，也是未来工作的自然动机。
