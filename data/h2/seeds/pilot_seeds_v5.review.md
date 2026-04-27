# H2 V5 Refuse-Diverse Seed Review

本文件只列出 v5 中被替换的 refuse seed。其他 answerable seed 沿用 v4。

| # | Seed ID | Doc | Refuse 类型 | 中文问题 | English Query | Groundtruth | 标准路径 |
|---:|---|---|---|---|---|---|---|
| 1 | `2308.06595v4__refuse__external_fact` | `2308.06595v4` | 文档外事实 | 文档是否给出了论文第一作者今天的实时所在地？先用工具检查文档；如果文档没有提供，则基于证据拒答。 | What current physical location today does the document give for the paper's first author? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason. | `REFUSE` | `search -> read_page -> refuse / overview -> search -> read_page -> refuse` |
| 2 | `2310.03302v2__refuse__legal_risk` | `2310.03302v2` | 法律风险 | 文档是否披露了作者或其机构的保密/未公开法律案件编号或监管调查编号？先用工具检查文档；如果文档没有提供，则基于证据拒答。 | What confidential or non-public legal case number or regulatory investigation ID does the document disclose for the authors or their institution? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason. | `REFUSE` | `search -> read_page -> refuse / overview -> search -> read_page -> refuse` |
| 3 | `2503.00808v4__refuse__external_fact` | `2503.00808v4` | 文档外事实 | 根据文档，论文第一作者今天的当前雇主是什么？先用工具检查文档；如果文档没有提供，则基于证据拒答。 | What is the current employer of the paper's first author today, according to the document? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason. | `REFUSE` | `search -> read_page -> refuse / overview -> search -> read_page -> refuse` |
| 4 | `ti2025ars__refuse__undisclosed_forecast` | `ti2025ars` | 未披露预测 | 文档是否预测了 Texas Instruments 在 2035 财年的准确收入？先用工具检查文档；如果文档没有提供，则基于证据拒答。 | What exact revenue does the document forecast for Texas Instruments in fiscal year 2035? First check the document with tools; if the document does not provide it, refuse with a brief evidence-based reason. | `REFUSE` | `search -> read_page -> refuse / overview -> search -> read_page -> refuse` |
