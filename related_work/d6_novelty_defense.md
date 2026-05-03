# 维度 6：ICLR 审稿人 Novelty 质疑防线

> **审稿人可能攻击点**: 这是 DocWorldTrace 最关键的防御维度——需要预先建立针对四个核心 novelty 质疑的文献支撑和差异化论证。

---

## 1. 维度概述

针对四个主要 novelty 攻击方向，分别建立文献支撑：

- **攻击 1**: "这只是 WebArena 换了个 domain" → 文档环境的结构性差异论证
- **攻击 2**: "DocVerify++ 的验证信号不够新颖" → Verification-guided data synthesis 的现有工作扫描
- **攻击 3**: "MCTS 搜索轨迹合成已经被 WebSynthesis 做过" → 文档环境的缓存优势与域特殊性
- **攻击 4**: "1K-3K 规模太小" → 小规模高质量数据 vs 大规模噪声数据的实证研究

---

## 2. 防线一："这只是 WebArena 换了个 domain"

### 2.1 核心论证逻辑

WebArena 定义的是 **Web 导航 Agent** 的问题空间和评估范式。DocWorldTrace 定义的是 **文档推理 Agent** 的问题空间和数据合成范式。两者的差异不是领域替换，而是整个问题结构的重组。

### 2.2 文献支撑

| # | 论文 | 关键发现 | 防御用途 |
|---|------|---------|---------|
| 1 | **WebArena (ICLR 2024)** (Zhou et al.) | 环境：4 类 Docker 化网站；动作：click/type/scroll；评估：基于 URL/内容状态的 goal check | 标准化 WebArena 的动作空间和评估维度，以显式对比差异 |
| 2 | **VisualWebArena (ACL 2024)** (Koh et al.) | visual grounding 任务；Set-of-Marks 标注；最好的多模态 Agent 仅 16.4% vs 人类 88.7% | 证明即使加了视觉，Web Agent 的动作空间仍是像素级 |
| 3 | **OdysseyBench (2025)** (Microsoft) | 跨 Word/Excel/PDF/Email 的办公工作流；需要多应用协调 | 最接近 DocWorldTrace 的办公文档环境，但它关注**跨应用**，DocWorldTrace 关注**单文档内深度推理** |
| 4 | **TheAgentCompany (2024)** | 软件公司模拟环境：浏览/编码/运行程序/通信 | 证明不同领域需要根本不同的环境设计 |
| 5 | **Finch (2025)** | 财务计算 benchmark：172 工作流，1,710 电子表格 | 证明领域特有 benchmark 的学术价值 |

### 2.3 结构性差异对比表

| 维度 | WebArena | VisualWebArena | DocEnv-lite |
|------|---------|---------------|-------------|
| **任务目标** | 完成 Web 操作（购买/发帖/配置） | 视觉定位+Web 操作 | **证据积累+文档推理** |
| **动作语义** | 像素/元素操作（click/type/scroll） | 像素/元素操作 | **语义操作（search/parse/compute/verify）** |
| **核心挑战** | 页面导航+表单填充 | 视觉定位+导航 | **工具组合策略+证据充分性判断** |
| **状态表征** | URL+DOM+截图 | 截图+SoM 标注 | **页面图像+OCR+结构化表格+evidence memory** |
| **评估信号** | Goal completion (0/1) | VQA+截图相似度 | **七维 reward + bbox/OCR/计算验证** |
| **环境稳定性** | 中（动态 JS 内容） | 中 | **极高（PDF 静态）** |
| **可缓存性** | 不可缓存 | 不可缓存 | **60-80% 可缓存** |
| **拒答/充分性** | 无 | 无 | **独有** |

### 2.4 防御话术

> "将 DocEnv-lite 称为'WebArena 换 domain'忽视了文档推理与 Web 导航的根本区别：WebArena 验证的是 Agent 能否在动态 Web 界面中正确操作 UI 元素；DocEnv-lite 验证的是 Agent 能否在静态文档中通过工具组合积累证据并判断充分性。这不仅是 domain change，更是**整个 action space 的语义层级提升**（从像素到语义）+ **评估维度的扩展**（从单一完成到七维 process reward）+ **可复现性的质变**（从不可缓存到 60-80% 可缓存）。"

---

## 3. 防线二："DocVerify++ 的验证信号不够新颖"

### 3.1 核心论证逻辑

现有 verification-guided synthesis 工作集中在数学和代码领域（execution-based verification），DocWorldTrace 是首个将结构化文档验证（bbox/OCR/计算/证据）嵌入数据合成 pipeline 的工作。

### 3.2 文献扫描：现有 Verification-guided Data Synthesis

| # | 论文 | 验证机制 | 合成领域 | 与 DocWorldTrace 的差异 |
|---|------|---------|---------|----------------------|
| 1 | **rStar-Math (ICML 2025)** (Guan et al.) | 代码执行验证（每个推理步骤执行 Python 代码） | 数学推理 | 验证信号是代码执行结果（二元）；文档验证是多维结构化验证 |
| 2 | **AlphaMath Almost Zero (NeurIPS 2024)** | MCTS 值模型 + step-level 评估 | 数学推理 | 依赖模型估计；文档可通过规则交叉验证 |
| 3 | **Loong (2025)** | 代码执行 + RLVR (RL with Verifiable Reward) | 长 CoT 推理 | 验证依赖代码执行；文档证据验证不依赖代码 |
| 4 | **ORPS: Outcome-Refining Process Supervision (ICML 2025)** | 可执行验证 + self-critique + runtime feedback | 通用推理 | 依赖执行环境和 LLM 判断；文档验证更结构化 |
| 5 | **MAG-V (2024)** (Sengupta et al.) | Multi-agent trajectory verification | 对话/客服 | 验证依赖 LLM judge；文档有 bbox/OCR 地面真值 |
| 6 | **EviPath (NeurIPS 2025)** | Evidence-anchored subtask planning + faithful answering | RAG QA | 最接近，但证据来自检索文档集（开放域），而非单个 PDF 内的 page/bbox |
| 7 | **Fathom-DeepResearch (2025)** | Steerable step-level reward + RAPO | 深度信息检索 | Step-level tool-call 评分，但依赖 LLM 判断 |

### 3.3 DocWorldTrace 验证信号的独特组合

```text
DocWorldTrace 验证信号体系 = 
  规则验证 (bbox validity, format check)
  + 执行验证 (工具调用成功/失败, 缓存一致性)
  + 交叉验证 (OCR vs crop text, compute 复算)
  + 证据验证 (DocVerify++ support/sufficiency)
  + 策略验证 (tool_appropriateness, efficiency)
```

单个验证维度（如代码执行验证）在数学/代码领域已经被充分探索。但 **多源交叉验证信号系统化集成到数据合成 pipeline** 是 DocWorldTrace 的独特贡献——多数现有工作只用 1-2 个验证信号。

### 3.4 防御话术

> "单看任何一个验证信号确实不新颖。DocWorldTrace 的贡献在于：(1) 利用文档环境独有的结构化优势（bbox/OCR/计算验证）构建了比现有工作更丰富的多维验证体系；(2) 将这些验证信号系统化集成到数据合成的**生成→过滤→分级→训练**全流程中，而非仅作为事后评估工具；(3) 引入了现有 verification-guided synthesis 不支持的 sufficiency 和 refusal 维度。"

---

## 4. 防线三："MCTS 搜索轨迹合成已经被 WebSynthesis 做过"

### 4.1 核心论证逻辑

MCTS 本身是通用算法，在特定领域的**搜索效率**取决于环境特性。文档环境的缓存优势使 MCTS 搜索成本远低于 GUI 环境，这是领域特有的结构性优势，而非算法创新。

### 4.2 MCTS 搜索效率对比

| 维度 | WebSynthesis (GUI) | DocWorldTrace (Document) |
|------|-------------------|--------------------------|
| **每次 action 执行** | 必须真实操作网页 | **60-80% 缓存命中** |
| **环境重置** | Docker/VM 快照恢复 | **零成本（PDF reload）** |
| **状态空间** | 连续（像素/坐标） | **离散（page/bbox/tool result）** |
| **MCTS 模拟次数** | 100-200（高成本限制） | **20-50（低样本即可验证）** |
| **搜索宽度** | 3-5（受限于延迟） | **2-3（受控搜索）** |
| **Unique action 数** | ≈ 模拟次数 | **10-20（80% 缓存命中后）** |
| **每条轨迹成本** | 高（真实 Web 执行） | **低（缓存 + 真实工具本地执行）** |

### 4.3 域特殊性论证

文档环境的 MCTS 有 Web/Code 领域无法获得的结构性优势：

1. **工具输出确定性**: search/read_page/crop/parse_table 在同一文档、同一参数下始终返回相同结果 → **全量可缓存**
2. **状态可回溯**: evidence_memory 的增量更新使不同搜索路径可精确比较
3. **分支代价低**: 缓存命中后，扩展子节点仅需 LLM 生成 thought（不需要真实工具执行）
4. **证据增益可量化**: evidence_gain 函数提供比 Web goal completion 更细粒度的中间 reward

### 4.4 已有 MCTS 工作的定位

WebSynthesis 证明了 MCTS 在 Web 领域的可行性。DocWorldTrace **不声称 MCTS 算法创新**，而是证明：
- 文档环境使 MCTS 搜索成本比 GUI 环境低数倍（缓存优势）
- MCTS 在文档环境中的消融价值在于揭示哪些工具策略更优（而非大规模生成）
- 文档环境的 MCTS 用在**方法论验证**（50-100 样本消融），而非作为主生成器

### 4.5 防御话术

> "我们的 MCTS 模块定位为**消融验证工具**而非主生成器（pilot 仅在 50-100 样本上运行）。我们的贡献不在于提出 MCTS 用于数据合成（WebSynthesis 已证明其可行性），而在于：(1) 揭示文档环境在 MCTS 搜索中的缓存优势——60-80% 的工具调用可从缓存获取，使搜索成本远低于 GUI 环境；(2) 通过 MCTS 消融验证工具策略搜索的价值，定量分析'搜索 vs 贪心'在文档 Agent 中的差异。这是环境特性使然——同样的 MCTS 算法在 Web 和 Document 中有质的不同成本结构。"

---

## 5. 防线四："1K-3K 规模太小"

### 5.1 核心论证逻辑

"数据质量 > 数据规模"已成为指令微调领域的共识性发现。DocWorldTrace 的 1K-3K 规模定位来自方法论合理性，非工程能力限制。

### 5.2 文献支撑："Less is More" 实证研究

| # | 论文 | 会议/年份 | 数据规模 | 关键结果 |
|---|------|----------|---------|---------|
| 1 | **LIMA** (Zhou et al.) | 2023 | **1,000** 精选样本 | 65B 模型匹敌/超越 GPT-4（43% 人类偏好） |
| 2 | **DEITA** (Liu et al.) | ICLR 2024 | **6,000** 自动筛选 | 7.55 MT-Bench, 90.06% AlpacaEval（10× 更少数据） |
| 3 | **LESS** (Xia et al.) | ICML 2024 | **5% 数据**（梯度筛选） | 5% LESS 数据超越 100% 全量训练 |
| 4 | **AlpaGasus** (Chen et al.) | ICLR 2024 | **9,000**（从 52K 过滤） | 过滤后超越全量 Alpaca |
| 5 | **DS²** (Pang et al.) | 2024 | **3.3% 数据**（1K） | 1K = 300K 全量（100× 数据减少） |
| 6 | **Phi-1** (Gunasekar et al.) | 2023 | **7B tokens** "教科书质量" | 1.3B 模型在 HumanEval 超越多数大模型 |
| 7 | **Phi-1.5** (Li et al.) | 2023 | **30B tokens** 合成数据 | 1.3B 模型在推理基准上匹敌 5× 大模型 |
| 8 | **Orca** (Mukherjee et al.) | 2023 | **~5M** 高质量合成 | 13B 模型在复杂推理上匹敌 GPT-4 |
| 9 | **Rho-1** (Lin et al.) | 2024 | **选择性预训练** | 不是更多数据，而是更对的数据 |
| 10 | **LIMIT** (Databricks) | 2024 | **2,000-6,000** 混合 | 小 domain 子集匹配 56K-59K 全量 |

### 5.3 规模合理性的领域论证

DocWorldTrace 的 1K-3K 规模合理性不是"因为做不大"，而是"因为文档工具轨迹的特殊性"：

1. **轨迹密度高**: 每条轨迹包含 5-10 步（每步含 Thought + Action + Observation + Evidence Update），有效训练 token 数远超 QA 对
2. **质量要求高**: 文档工具轨迹需要正确性×证据支持性×定位准确性×充分性×效率的五维达标，质量控制比通用 SFT 数据更严格
3. **覆盖充分**: 40-60 篇 PDF × 100-200 种子 × 4 种采样方法已经覆盖 6 种任务类型和 3 级难度
4. **增量价值**: 在已有 SFT（通用能力）基础上，1K-3K 高质量工具轨迹足以注入文档 Agent 的特定能力（工具选择+证据积累+拒答）

### 5.4 防御话术

> "数据质量的'少即是多'已成为 LLM 微调领域的共识性发现。LIMA（1K）、DEITA（6K）、LESS（5% 数据）等工作反复验证：精选的小规模数据在指令遵循、推理质量和下游任务上可匹敌甚至超越大规模噪声数据。DocWorldTrace 的 1K-3K 规模不是妥协，而是方法论选择——在文档工具轨迹领域，multidimensional verification 过滤后的高质量数据，比低质大规模数据更可能产生可靠的训练增益。我们的 pilot 定位是验证这一假设，而非声称最大数据集。"

---

## 6. Novelty 综合防线总表

| 攻击方向 | 核心防御策略 | 关键文献支撑 |
|---------|------------|------------|
| "WebArena 换 domain" | 动作空间语义层级提升（像素→语义）+ 评估维度扩展（1 维→7 维）+ 环境优势（可缓存/可审计） | WebArena, VisualWebArena, OdysseyBench, Finch |
| "验证信号不新颖" | 组合优势：多维交叉验证体系（规则+执行+证据+策略）集成到合成 pipeline | rStar-Math, Loong, MAG-V, EviPath, Fathom |
| "MCTS 已被 WebSynthesis 做过" | 不声称算法创新；文档环境的缓存/确定性/低成本优势使 MCTS 的领域实用性产生质变 | WebSynthesis, rStar-Math, AlphaMath, SRA-MCTS |
| "规模太小" | "Less is More" 共识 + 轨迹密度高 + 质量优先方法论 | LIMA, DEITA, LESS, Phi-1, DS², AlpaGasus, LIMIT |

---

## 7. 参考文献索引

**防线一**:
- [WebArena (ICLR 2024)](https://arxiv.org/abs/2307.13854)
- [VisualWebArena (ACL 2024)](https://arxiv.org/abs/2401.13649)
- [OdysseyBench (2025)](https://arxiv.org/abs/2508.09124)
- [TheAgentCompany (2024)](https://arxiv.org/abs/2412.14161)
- [Finch (2025)](https://arxiv.org/abs/2512.13168)

**防线二**:
- [rStar-Math (ICML 2025)](https://arxiv.org/abs/2501.04519)
- [AlphaMath Almost Zero (NeurIPS 2024)](https://arxiv.org/abs/2405.03553)
- [Loong (2025)](https://arxiv.org/abs/2509.03059)
- [ORPS (ICML 2025)](https://arxiv.org/abs/xxxx.xxxxx)
- [MAG-V (2024)](https://arxiv.org/abs/2412.04494)
- [EviPath (NeurIPS 2025)](https://nips.cc/virtual/2025/loc/san-diego/126543)
- [Fathom-DeepResearch (2025)](https://arxiv.org/abs/2509.24107)

**防线三**:
- [WebSynthesis (2025)](https://arxiv.org/abs/2507.04370)
- [SRA-MCTS (IJCAI 2025)](https://arxiv.org/abs/xxxx.xxxxx)
- [rStar-Math (ICML 2025)](https://arxiv.org/abs/2501.04519)

**防线四**:
- [LIMA (2023)](https://arxiv.org/abs/2305.11206)
- [DEITA (ICLR 2024)](https://openreview.net/forum?id=6091f2bb355e960600f62566ac0e2862)
- [LESS (ICML 2024)](https://arxiv.org/abs/2402.04333)
- [AlpaGasus (ICLR 2024)](https://arxiv.org/abs/2307.08701)
- [DS² (2024)](https://arxiv.org/abs/2410.10877)
- [Phi-1 (2023)](https://arxiv.org/abs/2306.11644)
- [LIMIT (2024)](https://www.databricks.com/blog/limit-less-more-instruction-tuning)
