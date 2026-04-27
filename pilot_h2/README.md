# Pilot Exp-2 / H2

本目录对应 `09_pilot_verification.md` 中的 `Pilot Exp-2: Teacher 轨迹生成可行性`。

## 目标

在 `DocEnv-lite` 上用强模型 teacher 跑真实工具回环，产出多步 `Thought -> Action -> Observation` 轨迹，并统计：

- 格式合规率
- 正常终止率
- 答案正确率
- 平均步数
- `verify` / `refuse` 使用率

## 最短流程

1. 生成 QA seeds
2. 准备 teacher 配置和 API key
3. 跑 rollout
4. 跑自动评测

## Teacher 配置

如果使用 DMXAPI，直接生成运行配置：

```bash
bash scripts/setup_h2_dmxapi_teachers.sh
export DMXAPI_API_KEY=你的_dmxapi_key
```

也可以使用一键脚本。它会优先读取仓库根目录的 `.env.dmxapi`：

```bash
cp .env.dmxapi.example .env.dmxapi
# 编辑 .env.dmxapi，填入 DMXAPI_API_KEY
bash scripts/run_h2_dmxapi.sh
```

`.env.dmxapi` 已在 `.gitignore` 中忽略，不应提交或同步公开。

该配置使用 OpenAI-compatible endpoint：

```text
https://www.dmxapi.cn/v1/chat/completions
```

并启用两个 teacher：

```text
gpt-4o-2024-11-20
gemini-2.5-flash
```

如果使用官方 OpenAI / Gemini API，可以把通用模板复制到运行目录：

```bash
mkdir -p data/h2
cp pilot_h2/teachers.example.json data/h2/teachers.json
```

然后设置环境变量：

```bash
export OPENAI_API_KEY=...
export GEMINI_API_KEY=...
```

## 运行

```bash
bash scripts/generate_h2_seeds.sh
bash scripts/run_h2_rollouts.sh
bash scripts/eval_h2_rollouts.sh
```

输出目录：

- seeds: `data/h2/seeds/`
- rollout logs: `data/h2/rollouts/`
- evaluation: `data/h2/eval/`

## 说明

- H2 runner 使用 OpenAI-compatible `chat/completions` HTTP 接口，不依赖供应商 SDK。
- assistant 每一步必须输出一个 JSON object：`thought`, `action`, `action_input`。
- observation 始终来自 `DocEnv` 真实执行，不允许 teacher 自造。
- `verify` 和 `answer` 的 `evidence_refs` 允许只给 page-level ref，例如 `[{"page": 5}]`。
