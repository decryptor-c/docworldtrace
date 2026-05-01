from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Sequence

import torch

from docworldtrace.pilot.h5_qwen_sft import _messages_for_template, _resolve_template_style


TERMINAL_ACTIONS = {"answer", "refuse"}


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _load_model_class() -> Any:
    try:
        from transformers import Qwen3VLForConditionalGeneration

        return Qwen3VLForConditionalGeneration
    except ImportError as exc:
        raise ImportError(
            "Qwen3VLForConditionalGeneration is unavailable. Install a recent transformers build, "
            "for example with scripts/setup_h5_qwen_sft_env.sh."
        ) from exc


def _first_device(model: Any) -> torch.device:
    for param in model.parameters():
        return param.device
    return torch.device("cpu")


def _parse_action_json(text: str) -> Dict[str, Any]:
    stripped = text.strip()
    candidates = [stripped]
    if "{" in stripped and "}" in stripped:
        candidates.append(stripped[stripped.find("{") : stripped.rfind("}") + 1])
    for candidate in candidates:
        try:
            payload = json.loads(candidate)
            if isinstance(payload, dict):
                return payload
        except json.JSONDecodeError:
            continue
    return {}


def _render_prompt(processor: Any, messages: Sequence[Dict[str, Any]], style: str) -> str:
    renderer = processor if hasattr(processor, "apply_chat_template") else processor.tokenizer
    return renderer.apply_chat_template(
        _messages_for_template(messages, style),
        tokenize=False,
        add_generation_prompt=True,
    )


def _load_adapter_base(adapter_path: Path) -> str | None:
    config_path = adapter_path / "adapter_config.json"
    if not config_path.exists():
        return None
    config = json.loads(config_path.read_text(encoding="utf-8"))
    return config.get("base_model_name_or_path")


def load_model_and_processor(model_or_adapter: str, base_model: str | None, dtype: str, device_map: str) -> tuple[Any, Any]:
    from peft import PeftModel
    from transformers import AutoProcessor

    path = Path(model_or_adapter)
    adapter_base = _load_adapter_base(path)
    model_cls = _load_model_class()
    torch_dtype = {"auto": "auto", "bf16": torch.bfloat16, "fp16": torch.float16, "fp32": torch.float32}[dtype]
    resolved_device_map = None if device_map == "none" else device_map

    if adapter_base or base_model:
        base = base_model or adapter_base
        if not base:
            raise ValueError("Missing base model path for adapter evaluation.")
        processor_path = str(path) if (path / "preprocessor_config.json").exists() else base
        processor = AutoProcessor.from_pretrained(processor_path, trust_remote_code=True)
        model = model_cls.from_pretrained(
            base,
            torch_dtype=torch_dtype,
            device_map=resolved_device_map,
            trust_remote_code=True,
        )
        model = PeftModel.from_pretrained(model, str(path))
    else:
        processor = AutoProcessor.from_pretrained(str(path), trust_remote_code=True)
        model = model_cls.from_pretrained(
            str(path),
            torch_dtype=torch_dtype,
            device_map=resolved_device_map,
            trust_remote_code=True,
        )

    model.eval()
    return model, processor


def evaluate(args: argparse.Namespace) -> Dict[str, Any]:
    eval_path = Path(args.eval_file)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = _load_jsonl(eval_path)
    if not rows:
        raise ValueError(f"Empty eval file: {eval_path}")

    model, processor = load_model_and_processor(args.model_or_adapter, args.base_model, args.dtype, args.device_map)
    tokenizer = processor.tokenizer if hasattr(processor, "tokenizer") else processor
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    style = _resolve_template_style(processor, rows[0]["messages"][:-1])
    device = _first_device(model)

    records = []
    for index, row in enumerate(rows[: args.limit] if args.limit else rows, start=1):
        prompt_messages = row["messages"][:-1]
        prompt = _render_prompt(processor, prompt_messages, style)
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=args.max_length, add_special_tokens=False)
        inputs = {key: value.to(device) for key, value in inputs.items()}
        with torch.no_grad():
            output_ids = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
        generated_ids = output_ids[0, inputs["input_ids"].shape[1] :]
        generated_text = tokenizer.decode(generated_ids, skip_special_tokens=True)
        parsed = _parse_action_json(generated_text)
        generated_action = parsed.get("action")
        target_action = row.get("target_action")
        format_valid = bool(parsed and isinstance(generated_action, str))
        records.append(
            {
                "id": row.get("id"),
                "condition": row.get("condition"),
                "task_type": row.get("task_type"),
                "target_action": target_action,
                "target_is_terminal": target_action in TERMINAL_ACTIONS,
                "generated_action": generated_action,
                "generated_is_terminal": generated_action in TERMINAL_ACTIONS,
                "format_valid": format_valid,
                "action_match": generated_action == target_action,
                "generated_text": generated_text,
                "parsed": parsed,
                "index": index,
            }
        )

    total = len(records)
    target_nonterminal = [r for r in records if not r["target_is_terminal"]]
    summary = {
        "model_or_adapter": args.model_or_adapter,
        "base_model": args.base_model,
        "eval_file": str(eval_path),
        "count": total,
        "format_valid_rate": round(sum(r["format_valid"] for r in records) / total, 4) if total else 0.0,
        "action_match_rate": round(sum(r["action_match"] for r in records) / total, 4) if total else 0.0,
        "generated_nonterminal_rate": round(
            sum(not r["generated_is_terminal"] for r in records if r["generated_action"]) / total, 4
        )
        if total
        else 0.0,
        "target_nonterminal_generated_nonterminal_rate": round(
            sum((not r["generated_is_terminal"]) for r in target_nonterminal if r["generated_action"])
            / len(target_nonterminal),
            4,
        )
        if target_nonterminal
        else 0.0,
        "target_action_distribution": dict(Counter(r["target_action"] for r in records)),
        "generated_action_distribution": dict(Counter(r["generated_action"] for r in records)),
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "records.jsonl").write_text(
        "\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n",
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate Qwen3-VL H5 LoRA adapters on H5 next-action datasets.")
    parser.add_argument("--model-or-adapter", required=True)
    parser.add_argument("--base-model", default="")
    parser.add_argument("--eval-file", required=True)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-length", type=int, default=4096)
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--dtype", choices=["auto", "bf16", "fp16", "fp32"], default="bf16")
    parser.add_argument("--device-map", default="auto")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    summary = evaluate(args)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
