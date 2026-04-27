# DocWorldTrace H2 Seeds

- Source file: `data/h2/seeds/pilot_seeds_v5.jsonl`
- Version: `v5`
- Record count: `20`
- Format: JSONL, compatible with `datasets.load_dataset("json", data_files=...)`.

## Fields

| Field | Meaning |
|---|---|
| `id` | Stable seed id |
| `doc_id` | Document id |
| `pdf_path` | Relative PDF path |
| `task_type` | Task category |
| `question` / `instruction` | User-facing query |
| `output` / `reference_answer` / `ground_truth` | Standard answer |
| `required_tools` | Expected core tools |
| `acceptable_paths` | Acceptable tool-action sequences |
| `supporting_refs` | Page/bbox evidence references |
| `messages` | Chat-style system/user/assistant example |

## Task Distribution

| Task type | Count |
|---|---:|
| `cross_page` | 4 |
| `numeric_computation` | 3 |
| `table_lookup` | 2 |
| `text_lookup` | 5 |
| `unanswerable` | 4 |
| `verification` | 2 |

## Load Example

```python
from datasets import load_dataset

ds = load_dataset('json', data_files='pilot_seeds_v5_hf.jsonl', split='train')
print(ds[0]['question'])
print(ds[0]['ground_truth'])
```
