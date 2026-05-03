# H5 Closed-Loop Trajectory Comparison

> 对比对象：`answer_only_adapter` vs `trajectory_adapter`  
> 数据来源：`data/h5/closed_loop_diverse_v2`  
> 样例范围：6 个 held-out closed-loop 验证 seed  
> 结论：answer-only adapter 主要直接进入终止动作；trajectory adapter 能根据任务调用工具，但在 unanswerable/refuse 场景中仍存在停止策略失败。

---

## 1. Cross-page

Seed: `2310.03302v2__cross__p1_p2`  
任务目标：先搜索 anchor phrase，再读取下一页顶部 running title。

Answer-only 轨迹：

```text
1. answer("MLAgentBench: Evaluating Language Agents on Multi-Step Reasoning Tasks")
```

结果：错误。它没有执行 `search/read_page`，直接回答，且标题不符合 reference。

Trajectory 轨迹：

```text
1. search("mlagentbench evaluating language agents on")
2. read_page([1])
3. read_page([2])
4. answer("MLAgentBench:EvaluatingLanguageAgentsonMachineLearningExperimentation")
```

结果：正确。路径符合 cross-page 要求。

---

## 2. Verification

Seed: `irs_2025_form_1040__verify__p2`  
任务目标：判断文档中的 claim 是否被支持。

Answer-only 轨迹：

```text
1. answer("SUPPORTED")
```

结果：答案正确，但路径不合规。它没有调用 `verify`，不可作为可审查工具轨迹。

Trajectory 轨迹：

```text
1. read_page([2])
2. verify("subtract line 14 from line 11b if zero or less enter 0 this is your taxable income")
3. answer("SUPPORTED")
```

结果：正确。路径包含 `verify`，符合验证任务目标。

---

## 3. Unanswerable / Refuse

Seed: `nasa_fy2025_budget_summary__refuse__generic`  
任务目标：文档不包含目标信息时应拒答。

Answer-only 轨迹：

```text
1. refuse("The document does not contain any information about the private mobile phone number...")
```

结果：最终拒答正确，但没有查证路径。

Trajectory 轨迹：

```text
1. search("author OR CEO")
2. search("contact information")
3. search("phone number")
4. search("email address")
5. search("NASA leadership")
6. search("NASA Administrator")
7. search("NASA Director")
8. search("NASA Chief")
```

结果：失败，`budget_exhausted`。说明 trajectory adapter 学会了搜索，但没有学会“搜索不到后停止并拒答”。

---

## 4. Table Lookup

Seed: `ti2025ars__table__p7`  
任务目标：从表格中找 trading symbol。

Answer-only 轨迹：

```text
1. answer("The value for the row 'Common Stock, par value $1.00' under the column 'Trading Symbol(s)' is 'C'.")
```

结果：错误，答案为 `C`，reference 是 `TXN`。

Trajectory 轨迹：

```text
1. parse_table(page=7, bbox=[49.5, 335.89999, 562.5, 364.39999])
2. answer("TXN")
```

结果：正确。它调用了 `parse_table`，符合表格任务路径。

---

## 5. Numeric Computation

Seed: `tm2529296d2_ars__numeric__p2`  
任务目标：从表格取数并计算百分比变化。

Answer-only 轨迹：

```text
1. format error / no valid action
```

结果：失败，没有有效 JSON action。

Trajectory 轨迹：

```text
1. parse_table(page=2, bbox=[35.94, 333.96, 535.455, 458.28005])
2. compute("((new_value - old_value) / old_value) * 100", old_value=14.0, new_value=2.0)
3. answer("-85.71%")
```

结果：正确。它完成了表格解析和计算。

---

## 6. Text Lookup

Seed: `tm2529296d2_ars__text__p27`  
任务目标：读取指定页并回答标题/文本。

Answer-only 轨迹：

```text
1. answer("The heading on page 27 is 'Section 1: Introduction to the Document'.")
```

结果：错误，属于未读文档直接生成的幻觉式答案。

Trajectory 轨迹：

```text
1. read_page([27])
2. answer("Technology Risks")
```

结果：正确。它先读页再回答。

---

## 7. 总结

| 类型 | Answer-only 行为 | Trajectory 行为 |
|---|---|---|
| cross-page | 直接答，答错 | `search + read_page`，答对 |
| verification | 直接答，缺 `verify` | `read_page + verify`，答对 |
| table_lookup | 直接答，答错 | `parse_table`，答对 |
| numeric | 格式失败 | `parse_table + compute`，答对 |
| text_lookup | 直接答，幻觉 | `read_page`，答对 |
| unanswerable | 直接 `refuse`，答案对但无证据路径 | 反复 `search`，未能 stop/refuse |

总体结论：

```text
answer-only adapter 学到的是终止动作倾向；
trajectory adapter 学到的是工具路径，但 refuse 停止策略还需要补强。
```

