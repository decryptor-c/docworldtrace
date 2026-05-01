# DocWorldTrace SFT 数据集推荐清单

> 目标：把当前 162 条 trajectory（54 seed × 3 teacher）扩到 **5K-50K trajectory**，足以做严肃的 Qwen2.5-VL-7B / InternVL2-8B SFT。
> 思路：找 **(question, reference_answer, supporting_pages)** 三元组现成的数据集 → 作为 H2 seed 喂 teacher rollout → 用 DocVerify++ 过滤 → 进 SFT。

---

## Tier 1 — 可以直接接 pipeline 的 QA 数据集（schema 几乎完美匹配）

| 数据集 | 规模 | 任务对应 | 文档类型 | 许可 | HF 链接 |
|---|---:|---|---|---|---|
| **MP-DocVQA** | 46K Q / 6K docs | text_lookup, table_lookup, **cross_page** | 工业文档 (含多页) | research-only | [`rubentito/mp-docvqa`](https://huggingface.co/datasets/rubentito/mp-docvqa) |
| **MMLongBench-Doc** | 13K Q / 1.4K long docs | 全部 6 类 + **unanswerable 显式标注** | 学术 / 技术 / 财报 / 政策 / 教程 | research | [`yinanhe/MMLongBench-Doc`](https://huggingface.co/datasets/yinanhe/MMLongBench-Doc) |
| **DocVQA** | 50K Q / 12K pages | text_lookup, table_lookup | 工业 / 行政文档 | CDLA-Permissive | [`lmms-lab/DocVQA`](https://huggingface.co/datasets/lmms-lab/DocVQA) |
| **DUDE** | 41K Q / 5K docs | 全部 6 类 (含 list/yes-no/abstain) | 多领域企业文档 | research | [`jordyvl/DUDE_loader`](https://huggingface.co/datasets/jordyvl/DUDE_loader) |
| **TAT-QA** | 16K Q / 2.7K passages | **numeric_computation**, table_lookup | 金融年报 (table + text 混合) | MIT | [`next-tat/tat-qa`](https://huggingface.co/datasets/next-tat/tat-qa) |
| **FinQA** | 8K Q / 2.8K reports | **numeric_computation** (含 step-by-step 算式) | 上市公司财报 | MIT | [`czyssrs/finqa`](https://huggingface.co/datasets/dreamerdeo/finqa) |

**Tier 1 合计 ≈ 174K 候选 seed**，按 5-10% 通过率（pdf 可获得 + 答案稳定）保守估计能产出 **8K-17K trajectory**。

### MMLongBench-Doc 是最高优先级

- 唯一一个**显式标注 unanswerable** 的长文档 QA（你的 refuse 任务最缺这个）
- 文档长度 30-200 页，天然支持 cross-page reasoning
- 6 类问题类型与你的 6 类任务几乎 1:1
- 论文里 SOTA 模型 accuracy ~30%，证明任务难度合适
- **建议先 100% 跑通这个**，光这一份就能产出 ~8K trajectory

---

## Tier 2 — 需要少量改造（增加任务模板或引入新工具）

| 数据集 | 规模 | 改造点 | 用途 |
|---|---:|---|---|
| **Qasper** | 5K Q / 1.6K NLP papers | 已有 evidence span，需要映射 page | cross_page，长文档推理 |
| **ChartQA** | 9.6K Q / 4.8K charts | 等 `parse_chart` 上线（Phase 2） | 图表数值推理 |
| **SlideVQA** | 52K Q / 2.6K decks | PPT 转 PDF | 多页幻灯片 |
| **ConvFinQA** | 3.9K dialogues | 拆成单轮 numeric | 财务多轮 |
| **HybridQA** | 70K Q / Wikipedia | wiki 表+文混合，转 PDF | 长尾 table+text |
| **InfographicVQA** | 30K Q / 5K infographics | 视觉推理 | 视觉密集型文档 |
| **VisualMRC** | 30K Q / 10K web pages | 视觉阅读理解 | 网页样式文档 |
| **WTQ (WikiTableQuestions)** | 22K Q / 2.1K tables | wiki table → PDF | 纯 table_lookup |
| **TabFact** | 117K claims / 16K tables | claim verification | **verification** |
| **DocBench (2024)** | 1K docs / 9.5K Q | 较新长文档 bench | 多任务覆盖 |

---

## Tier 3 — PDF 原料库（适合"无监督"自动派生 seed）

不带标注，但你已经有 `structure_heuristic_v2_review` 可以从结构里自动派生题目。这些是源源不断的 PDF 来源：

| 来源 | 规模 | 类型 | 抓取 |
|---|---:|---|---|
| **arXiv** | 2.5M+ papers | 科学论文（你已用过）| `arxiv.org/list/cs.CL/2024` 月度 dump |
| **SEC EDGAR** | 数百万 filings | 10-K / 10-Q / 8-K / S-1 | `https://www.sec.gov/cgi-bin/browse-edgar` |
| **PubMed Central OAI** | 4M+ papers | 医学论文 (open access) | `oai.eprints.org` |
| **Federal Register** | 周更 | 美国政府规章 | `federalregister.gov/api` |
| **EUR-Lex** | 数十万 | 欧盟法律 / 指令 | `eur-lex.europa.eu/eli` |
| **WHO Publications** | 1万+ | 全球公共卫生 | `who.int/publications` |
| **IPCC reports** | 数十份 long docs | 气候科学 | `ipcc.ch/reports` |
| **NASA Tech Reports** | 50万+ | 航空航天 | `ntrs.nasa.gov` |
| **GAO Reports** | 数千份 | 美国政府审计 | `gao.gov/products` |
| **WB Open Knowledge** | 4万+ | 世界银行报告 | `openknowledge.worldbank.org` |
| **CommonCrawl PDFs** | TB 级 | 任意主题（需过滤）| `commoncrawl.org` |
| **Project Gutenberg** | 7万+ books | 经典书籍（噪声大）| `gutenberg.org` |

---

## Tier 4 — 用作对照 / 借鉴的 agent trajectory 数据

你不一定直接用，但论文里可以引用并比较：

| 数据集 | 规模 | 类型 | 价值 |
|---|---:|---|---|
| **AgentTrek** (ICLR 2025) | 10K+ web trajectories | GUI agent | 你 related work 已引用，可作 cross-domain 比较 |
| **GUI-Net-1M / TongUI** (AAAI 2026) | 1M GUI trajectories | GUI agent | 大规模对照 |
| **ToolBench** (Qin et al.) | 16K tool-use | API 工具 | 通用 tool-use baseline |
| **APIBench / Gorilla** | 16K | API 调用 | 同上 |
| **Mind2Web** | 2K real web tasks | Web agent | 真实分布 |
| **AgentInstruct** | 1.8K | Agent SFT 指令 | 通用 |

---

## 推荐分阶段执行路线

### Phase A — 1 周内可启动（最低风险）

只跑 **MMLongBench-Doc**：
- 13K Q × 1 teacher (Gemini-Flash 最便宜) × 1 run = 13K rollouts
- 估计成本：13K × $0.02 = **$260**
- DocVerify++ 过滤后保守预期 8K-10K keep
- 交付：DocWorldTrace-10K v1

### Phase B — 2-3 周内（确立资源贡献）

加入 **MP-DocVQA + DUDE + TAT-QA + FinQA**：
- 增量 ~110K Q
- 用 3 个 teacher × 1 run（保留 teacher 异质性）
- 成本：110K × 3 × $0.05 平均 ≈ **$16K**（如果用 Gemini Flash 主力 + GPT-4o 抽样可降到 ~$5K）
- 过滤后预期 50K-80K keep
- 交付：DocWorldTrace-50K + 多 teacher 对比

### Phase C — Resource paper 投稿规模（5-8 周）

加入 Tier 2 + 自动派生（用 arXiv / SEC 1万篇 PDF 跑 structure_heuristic）：
- 增量 ~30K-100K seed
- 总目标：100K-200K trajectory（含原始 162 条 pilot 作为 gold-standard 子集）
- 成本：~$10-30K
- 交付：**DocWorldTrace-100K**，分 train/dev/test，可直接对标 ACL Resource Track / NeurIPS D&B

---

## 数据集映射到你的 6 类任务（覆盖核查）

| 任务 | Tier 1 主力 | 缺口 |
|---|---|---|
| text_lookup | DocVQA / MP-DocVQA / DUDE | 已饱和 |
| table_lookup | DocVQA / MP-DocVQA / TAT-QA / DUDE | 已饱和 |
| numeric_computation | TAT-QA / FinQA / MMLongBench | **强（FinQA 含 step-by-step 算式可直接喂 compute 工具）** |
| cross_page | MP-DocVQA / MMLongBench / Qasper | 已饱和 |
| verification | TabFact / 自构造（claim ↔ evidence） | 中等 |
| unanswerable | **MMLongBench-Doc 唯一显式标注** | 仅靠它 |

---

## 实施建议

1. **优先级**：MMLongBench-Doc（一份覆盖全部 6 类 + 唯一 unanswerable）→ MP-DocVQA → TAT-QA → FinQA → DUDE → DocVQA。
2. **PDF 获取**：MMLongBench / MP-DocVQA / DUDE 都附带 PDF；TAT-QA / FinQA 有 HTML 表 + 文字段，需要按 SEC 原文回填 PDF（脚本可写）。
3. **Teacher 配比**：90% Gemini-2.5-Flash（成本低）+ 10% GPT-4o（质量基线）+ 抽 5% 用 Claude（异质 teacher，回应 H4 多样性 reviewer 必问）。
4. **DocVerify++ 过滤**：保持当前宽松版（v2），预期 keep_rate 80-95%。
5. **质量分级**：用 quality_score 把 keep 集合分为 Gold/Silver/Bronze，Gold 做 SFT 主集，Silver+Bronze 做 PRM/DPO 负例。
6. **Splits**：按 doc_id 而非 seed_id split（避免数据泄漏）；推荐 80/10/10。

---

## 与现有 pilot 的衔接

当前你已有：
- 14 篇 PDF + 54 seed = 162 trajectory（gold-standard pilot subset）
- 验证过的 H2 pipeline + DocVerify++ 宽松版 + H5 closed-loop

新数据集进来不需要改任何代码，只需要：
1. 写一个 `tools/import_<dataset>.py`，把数据集里的 (Q, A, doc, page) 转成 `data/h2/seeds/<dataset>_v1.jsonl` 格式
2. 把 PDF 拷贝到 `data/raw_pdfs/<dataset>/`
3. 跑 `scripts/run_h1_calls_batch.sh`（H1 stress test）→ 通过的进 H2
4. 跑 `scripts/run_h2_rollouts.sh` → `run_h3_docverify_plus.sh` → `run_h4_diversity.sh` → `run_h5_pilot.sh`

预期你的现有 pipeline 能直接吃下 1-2 个数量级的扩张，瓶颈只在 API 成本与 GPU SFT 资源。

---

## 一句话推荐

> **先把 MMLongBench-Doc 端到端跑完**——它一份就解决你 unanswerable 训练数据缺失的问题，13K Q 跑一遍只需 $260，能在 1 周内把 162 trajectory 扩到 8K-10K，对标真实 SFT 训练已经够用。其他数据集可以按照 Phase B/C 节奏加。
