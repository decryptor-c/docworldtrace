# Pilot Exp-1 Server Setup

本目录对应 [docs/research_plan/09_pilot_verification.md](../docs/research_plan/09_pilot_verification.md) 里的第一部分：`Pilot Exp-1 / H1: DocEnv 环境可行性`。

## 目标

- 在服务器上安装 PDF/OCR 依赖
- 用 `DocEnv-lite` 跑通 `overview/search/read_page/crop/ocr/parse_table/compute/verify`
- 记录工具成功率、检索命中和缓存一致性

## 一次性安装

```bash
bash scripts/bootstrap_server_env.sh
```

或分步执行：

```bash
bash scripts/install_system_deps.sh
bash scripts/setup_python_env.sh
bash scripts/check_server_env.sh
```

## 先跑样例

```bash
bash scripts/run_pilot_exp1_sample.sh
```

输出会写到：

- `artifacts/pilot_exp1/sample_report.json`
- `artifacts/pilot_exp1/sample_report.md`

## 跑真实 PDF

先准备一个调用规格文件，参考 `sample_calls.json`。

```bash
bash scripts/run_pilot_exp1_pdf.sh /path/to/file.pdf /path/to/calls.json
```

## 当前实现边界

- PDF 渲染：`PyMuPDF`
- 文本/单词 bbox：`pdfplumber`
- OCR：当前优先用 PDF 文本层和 bbox 聚合；必要时可在后续补 `pytesseract` 真 OCR fallback
- 表格解析：当前使用 `pdfplumber.find_tables()` 的结果
- 检索：当前是轻量词项重叠检索，够做 H1 feasibility；后续可替换 `rank_bm25` 或向量检索

## 建议的 H1 执行方式

1. 先用 5 篇 PDF 各跑一遍 `overview/read/search`
2. 再人工设计 30 个标准调用，放进 JSON
3. 跑完后看：
   - tool success rate
   - retrieval checks
   - cache checks
4. 对 OCR CER、表格结构正确率、crop 有效性补人工抽检
