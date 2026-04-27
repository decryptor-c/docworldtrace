# Action Space 设计参考：16 篇论文映射与工具定义指南

> **目标**: 基于 16 篇核心论文的 action/tool 空间对比分析，为 DocWorldTrace 工具开发提供设计依据和实现参考。  
> **用途**: 开发 DocEnv 工具集时的查阅文档，而非 proposal 正文。

---

## 1. DocWorldTrace 10-Action 空间定义（修订版）

基于 16 篇论文的 action 共识度分析，原 9-action 空间调整为 **10-action**（新增 `overview`），并按使用频率分为三层：

### 核心 Action（5 个）— 所有轨迹必须使用

| # | Action | 参数 | 返回 | 共识度 |
|---|--------|------|------|:------:|
| 1 | `search(query, top_k)` | 文本查询 + 返回数 | 候选页面+snippet | 9/16 ★★★★ |
| 2 | `read_page(page_ids)` | 页码列表（支持批量） | OCR 文本+页面描述 | 11/16 ★★★★★ |
| 3 | `crop(page_id, bbox)` | 页码+坐标 | 裁剪区域图像+OCR | 5/16 ★★★ |
| 8 | `answer(text, evidence_refs)` | 答案+证据引用 | 终止(成功) | 16/16 ★★★★★ |
| 9 | `refuse(reason)` | 拒答理由 | 终止(拒答) | 2/16 ★★ (独特) |

### 扩展 Action（5 个）— 按任务类型选择性使用

| # | Action | 参数 | 返回 | 共识度 |
|---|--------|------|------|:------:|
| 10 | **`overview()`** | 无 | 文档缩略图网格+元信息 | **新增** |
| 4 | `ocr(page_id, bbox=None)` | 页码+可选区域 | 识别文本+bbox | 2/16 ★★ (可选) |
| 5 | `parse_table(page_id, bbox)` | 页码+区域 | 结构化表格 | 3/16 ★★ |
| 6 | `compute(expr, vars)` | 表达式+变量 | 计算结果 | 3/16 ★★★ (必要) |
| 7 | `verify(claim, evidence_refs)` | 断言+证据引用 | support/sufficiency | 4/16 ★★★ (创新) |

### 辅助工具（DocEnv 内部，非 Agent action）

| 工具 | 说明 | 使用场景 |
|------|------|---------|
| `detect_layout(page_id)` | 返回页面布局元素 bbox 列表 | crop 前辅助定位 |
| BM25 索引 | `search` 的后端 | 环境初始化构建 |
| ColPali/ColQwen 索引 | `search` 的视觉检索后端 | Phase 2 扩展 |

### Action 粒度层级

```text
Level 0: overview()      → 文档级概览（缩略图+统计）
Level 1: search(query)   → 页面级检索
Level 2: read_page(ids)  → 页面级内容获取
Level 3: crop(page,bbox) → 区域级裁剪
Level 4: ocr/parse_table → 元素级结构化解析
Level 5: compute/verify  → 推理级操作
```

---

## 2. 16 篇论文 Action 映射矩阵

> 符号: ● 直接对应 / ◐ 部分对应 / ○ 间接实现 / — 不支持

| DocWorldTrace Action | ARIAL | CoE | MDoc | DocLens | VISOR | SiSaSo | JBD | Cogi | MMDR | DocV* | Seek | FGRPO | EGG | SLEUTH | Clue | SPARC |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `search` | ● | ◐ | ● | ● | ● | ◐ | — | ◐ | ● | ● | ◐ | — | — | ● | — | — |
| `read_page` | ◐ | ● | ◐ | ● | ◐ | ◐ | — | ● | ● | ● | ◐ | ◐ | ◐ | ● | ◐ | — |
| `crop` | — | ◐ | — | ● | ● | — | — | ◐ | — | — | — | — | ● | ◐ | ● | ● |
| `ocr` | ● | — | — | ● | — | — | — | — | — | — | — | — | — | — | — | — |
| `parse_table` | — | — | — | ◐ | — | — | — | ◐ | — | — | — | — | — | — | — | — |
| `compute` | ● | ◐ | — | — | — | — | — | ◐ | — | — | — | — | — | — | — | — |
| `verify` | — | ◐ | ◐ | ◐ | — | — | ● | — | — | — | — | ● | — | — | — | — |
| `answer` | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| `refuse` | ◐ | — | — | ◐ | — | — | — | — | — | — | — | — | — | — | — | — |

---

## 3. 各 Action 的实现参考

### 3.1 search — 检索实现方案

16 篇论文中存在 4 种检索方式，开发时需考虑支持多后端：

| 类型 | 代表系统 | 实现方式 | 适用场景 |
|------|---------|---------|---------|
| 文本检索 (BM25) | MM-Doc-R1 | `rank_bm25` | OCR 质量高的数字化 PDF |
| 语义检索 (embedding) | ARIAL (MiniLM-v6) | sentence-transformers | 语义相似但关键词不同 |
| 视觉检索 (ColPali/ColQwen) | VISOR, Doc-V\*, SLEUTH | ColPali/ColQwen2 | 视觉丰富的文档 |
| VLM 导航 (无检索器) | DocLens | VLM 看缩略图选页 | 结构简单的短文档 |

**Pilot 建议**: 默认 BM25，可选 ColPali。Phase 2 统一为多后端。

### 3.2 read_page — 页面读取

Doc-V\* 是唯一显式区分"搜索"和"导航"的系统：
- `retrieval_page(q_t)` — 语义搜索页面（对应 `search`）
- `fetch_page([i_1,...,i_m])` — 按页码索引获取（对应 `read_page`）

**开发建议**: `read_page` 支持批量页码输入 `read_page(page_ids=[3, 7, 12])`，返回多页信息。

### 3.3 crop — 区域裁剪

两种裁剪范式：

| 范式 | 代表 | 方式 | DocWorldTrace 选择 |
|------|------|------|-------------------|
| Agent 主动裁剪 | VISOR | Agent 输出 bbox 坐标 | **✓ 采用** |
| 自动检测+裁剪 | DocLens, SPARC, ClueTracer | 模型自动定位区域 | 辅助工具 `detect_layout` |

**开发建议**: `crop(page_id, bbox)` 要求 Agent 提供坐标，但 DocEnv 可通过 `detect_layout(page_id)` 辅助返回候选 bbox 列表。

### 3.4 ocr — 文本识别

**OCR-free 趋势**: 16 篇中仅 ARIAL 和 DocLens 有显式 OCR tool，其余系统：
- OCR-free 端到端 VLM（CoE, VISOR, DocCogito 等）
- OCR 预处理（MM-Doc-R1 用 Doc2X 预处理，不作为 Agent tool）

**开发建议**: `ocr` 降级为可选工具。对高质量数字化 PDF，OCR 在环境初始化时预执行；对低质量扫描件，保留为 Agent 可调用 action。

### 3.5 parse_table — 表格解析

现有系统表格处理方式：
- DocLens: `LayoutDetect` 自动检测 → 裁剪表格区域
- DocCogito: `Select(table)` → `Read` → 内部推理
- ARIAL: OCR 提取后由 QA 模块处理

**开发建议**: 保留为独立 tool，但认识到 VLM 端到端表格理解能力在快速提升。Phase 2 可评估 `crop + VLM read` 是否能替代独立 `parse_table`。

### 3.6 compute — 数值计算

仅 ARIAL 有显式 `Compute(sum, values)` 工具。但数值计算是文档高频需求（财报、科学论文），且 VLM 计算可靠性不足。

**开发建议**: 必须保留。使用 `RestrictedPython` 或 `ast.literal_eval` 实现安全计算沙盒。

### 3.7 verify — 验证

**DocWorldTrace 最独特的设计**。16 篇论文中无任何系统将验证作为 Agent 显式可调用 tool。现有验证机制：
- RL reward 信号: CoE (R_step), Faithful GRPO (Lagrangian 约束)
- 多 Agent 质控: MDocAgent (Critical Agent), DocLens (Adjudicator)
- 事后评估: Journey Before Destination (VLM Judge)

**开发建议**: 作为 DocVerify++-lite 的接口，Agent 主动调用以验证当前 claim 是否被证据支持。这是核心差异化，需优先实现。

### 3.8 overview — 全局概览（新增）

Doc-V\* 的 Thumbnail Overview 实验证明缩略图对长文档导航有显著价值。

**开发建议**: 返回文档元信息（页数/领域/表格数/图表数）+ 全页缩略图网格。在轨迹起始时可选调用。

### 3.9 refuse — 拒答

几乎无现有系统有显式 refuse 机制。DocWorldTrace 独特设计，与 sufficiency reward 直接相关。

**开发建议**: 与 `verify` 配合——Agent 调用 verify 判断证据是否充分，不充分时可选择 refuse。

---

## 4. 与现有系统 Schema 的兼容性

开发 Schema 转换器时的参考：

| 目标系统 | 转换策略 | 难度 |
|---------|---------|:----:|
| VISOR (search/crop/answer) | search→search, crop→crop, answer→answer；verify/compute 嵌入 thought | 低 |
| MM-Doc-R1 (search/read) | search→search, read_page→read, crop/ocr→内部步骤 | 低 |
| Doc-V\* (retrieval/fetch/answer) | search→retrieval_page, read_page→fetch_page | 低 |
| DocCogito VSC | crop→Select, ocr→Read, compute→Aggregate/Compare | 中 |
| DocSeeker ALR | action 映射到 search+read_page, ALR 阶段映射到 thought | 中 |
| ARIAL | ocr→RunOCR, search→FindText, answer→AskQA+GroundAnswer | 低 |

---

## 5. Phase 2 扩展路线

| 扩展 | 来源系统 | 说明 | 优先级 |
|------|---------|------|:------:|
| `parse_chart(page_id, bbox)` | — (已规划) | 图表解析 | 高 |
| `compare(values, metric)` | DocCogito Compare | 显式比较操作 | 中 |
| `filter(candidates, predicate)` | DocCogito Filter | 条件筛选（May keep in thought） | 低 |
| Evidence Space 管理 | VISOR | Sliding Window + 持久化证据空间 | 高 |
| Intent Injection | VISOR | 每步重注入 query 防止搜索漂移 | 中 |
| Visual Action Evaluation | VISOR | 评估 crop action 效用 | 低 |
| 多检索后端统一 | MM-Doc-R1/VISOR/Doc-V\* | BM25 + ColPali + ColQwen | 高 |

---

## 6. 核心设计发现（开发时牢记）

1. **`verify` + `refuse` 是 DocWorldTrace 的独特组合** — 无现有系统同时具备，是核心差异化
2. **`search` 实现差异最大** — 开发时需支持可插拔的检索后端
3. **`crop` 是文档 Agent 的独特操作** — GUI 的 click 在文档域自然映射为 crop
4. **`compute` 使用率低但不可删** — VLM 数值计算不可靠是已知问题
5. **`ocr` 可降级但不可删** — OCR-free 趋势明显，但低质量文档仍需要
6. **`overview` 是重要补充** — Doc-V\* 实验证明 thumbnail 对长文档有显著价值
