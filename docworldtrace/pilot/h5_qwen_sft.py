from __future__ import annotations

import argparse
import inspect
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence

import torch
from torch.utils.data import Dataset


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _content_as_vl_text(content: Any) -> List[Dict[str, str]]:
    return [{"type": "text", "text": str(content)}]


def _messages_for_template(messages: Sequence[Dict[str, Any]], style: str) -> List[Dict[str, Any]]:
    if style == "vl":
        return [{"role": item["role"], "content": _content_as_vl_text(item.get("content", ""))} for item in messages]
    return [{"role": item["role"], "content": str(item.get("content", ""))} for item in messages]


def _resolve_template_style(processor: Any, sample_messages: Sequence[Dict[str, Any]]) -> str:
    renderer = processor if hasattr(processor, "apply_chat_template") else processor.tokenizer
    for style in ("vl", "text"):
        try:
            renderer.apply_chat_template(
                _messages_for_template(sample_messages, style),
                tokenize=False,
                add_generation_prompt=False,
            )
            return style
        except Exception:
            continue
    raise RuntimeError("The loaded tokenizer/processor cannot render the H5 chat messages.")


def _render_chat(processor: Any, messages: Sequence[Dict[str, Any]], style: str, add_generation_prompt: bool) -> str:
    renderer = processor if hasattr(processor, "apply_chat_template") else processor.tokenizer
    return renderer.apply_chat_template(
        _messages_for_template(messages, style),
        tokenize=False,
        add_generation_prompt=add_generation_prompt,
    )


class H5ChatDataset(Dataset):
    def __init__(self, path: Path, processor: Any, max_length: int) -> None:
        rows = _load_jsonl(path)
        if not rows:
            raise ValueError(f"Empty dataset: {path}")
        self.path = path
        self.processor = processor
        self.tokenizer = processor.tokenizer if hasattr(processor, "tokenizer") else processor
        self.max_length = max_length
        self.template_style = _resolve_template_style(processor, rows[0]["messages"])
        self.items = [item for item in (self._encode_row(row) for row in rows) if item is not None]
        if not self.items:
            raise ValueError(f"No trainable examples remain after tokenization: {path}")

    def _encode_row(self, row: Dict[str, Any]) -> Dict[str, Any] | None:
        messages = row["messages"]
        if len(messages) < 2 or messages[-1].get("role") != "assistant":
            raise ValueError(f"Expected final assistant target in row: {row.get('id')}")

        prompt_messages = messages[:-1]
        full_text = _render_chat(self.processor, messages, self.template_style, add_generation_prompt=False)
        prompt_text = _render_chat(self.processor, prompt_messages, self.template_style, add_generation_prompt=True)

        full = self.tokenizer(
            full_text,
            truncation=True,
            max_length=self.max_length,
            add_special_tokens=False,
        )
        prompt = self.tokenizer(
            prompt_text,
            truncation=True,
            max_length=self.max_length,
            add_special_tokens=False,
        )
        input_ids = full["input_ids"]
        if not input_ids:
            return None
        prompt_len = min(len(prompt["input_ids"]), len(input_ids))
        labels = list(input_ids)
        labels[:prompt_len] = [-100] * prompt_len
        if all(label == -100 for label in labels):
            return None
        return {
            "id": row.get("id"),
            "input_ids": input_ids,
            "attention_mask": full.get("attention_mask", [1] * len(input_ids)),
            "labels": labels,
        }

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> Dict[str, Any]:
        return self.items[index]


@dataclass
class CausalLMDataCollator:
    tokenizer: Any

    def __call__(self, features: Sequence[Dict[str, Any]]) -> Dict[str, torch.Tensor]:
        model_inputs = self.tokenizer.pad(
            [
                {
                    "input_ids": feature["input_ids"],
                    "attention_mask": feature["attention_mask"],
                }
                for feature in features
            ],
            padding=True,
            return_tensors="pt",
        )
        labels = [feature["labels"] for feature in features]
        max_len = model_inputs["input_ids"].shape[1]
        padded_labels = []
        for label in labels:
            pad_len = max_len - len(label)
            if self.tokenizer.padding_side == "left":
                padded_labels.append([-100] * pad_len + label)
            else:
                padded_labels.append(label + [-100] * pad_len)
        model_inputs["labels"] = torch.tensor(padded_labels, dtype=torch.long)
        return model_inputs


def _torch_dtype(name: str) -> torch.dtype | str:
    if name == "auto":
        return "auto"
    if name == "bf16":
        return torch.bfloat16
    if name == "fp16":
        return torch.float16
    if name == "fp32":
        return torch.float32
    raise ValueError(f"Unsupported dtype: {name}")


def _load_model_class() -> Any:
    try:
        from transformers import Qwen3VLForConditionalGeneration

        return Qwen3VLForConditionalGeneration
    except ImportError as exc:
        raise ImportError(
            "Qwen3VLForConditionalGeneration is unavailable. Install a recent transformers build, "
            "for example with scripts/setup_h5_qwen_sft_env.sh."
        ) from exc


def _training_args(**kwargs: Any) -> Any:
    from transformers import TrainingArguments

    params = inspect.signature(TrainingArguments.__init__).parameters
    if "eval_strategy" in params:
        kwargs["eval_strategy"] = kwargs.pop("evaluation_strategy")
    return TrainingArguments(**kwargs)


def _trainer(**kwargs: Any) -> Any:
    from transformers import Trainer

    params = inspect.signature(Trainer.__init__).parameters
    processing_class = kwargs.pop("processing_class")
    if "processing_class" in params:
        kwargs["processing_class"] = processing_class
    else:
        kwargs["tokenizer"] = processing_class
    return Trainer(**kwargs)


def train(args: argparse.Namespace) -> None:
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from transformers import AutoProcessor

    model_path = Path(args.model_name_or_path)
    train_path = Path(args.train_file)
    eval_path = Path(args.eval_file) if args.eval_file else None
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    processor = AutoProcessor.from_pretrained(str(model_path), trust_remote_code=True)
    tokenizer = processor.tokenizer if hasattr(processor, "tokenizer") else processor
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    quantization_config = None
    if args.load_in_4bit:
        from transformers import BitsAndBytesConfig

        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16 if args.dtype == "bf16" else torch.float16,
            bnb_4bit_use_double_quant=True,
        )

    model_cls = _load_model_class()
    model_kwargs = {
        "torch_dtype": _torch_dtype(args.dtype),
        "device_map": None if args.device_map == "none" else args.device_map,
        "trust_remote_code": True,
        "quantization_config": quantization_config,
    }
    if args.attn_implementation:
        model_kwargs["attn_implementation"] = args.attn_implementation
    model = model_cls.from_pretrained(str(model_path), **model_kwargs)
    if hasattr(model.config, "use_cache"):
        model.config.use_cache = False
    if args.gradient_checkpointing:
        model.gradient_checkpointing_enable()
        if hasattr(model, "enable_input_require_grads"):
            model.enable_input_require_grads()
    if args.load_in_4bit:
        model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=args.gradient_checkpointing)

    target_modules = [item.strip() for item in args.target_modules.split(",") if item.strip()]
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=target_modules,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    train_dataset = H5ChatDataset(train_path, processor, max_length=args.max_length)
    eval_dataset = H5ChatDataset(eval_path, processor, max_length=args.max_length) if eval_path else None

    training_args = _training_args(
        output_dir=str(out_dir),
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.per_device_train_batch_size,
        per_device_eval_batch_size=args.per_device_eval_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        eval_steps=args.eval_steps,
        save_total_limit=args.save_total_limit,
        evaluation_strategy="steps" if eval_dataset is not None else "no",
        bf16=args.dtype == "bf16",
        fp16=args.dtype == "fp16",
        gradient_checkpointing=args.gradient_checkpointing,
        remove_unused_columns=False,
        dataloader_pin_memory=False,
        report_to=[] if args.report_to == "none" else [args.report_to],
    )
    trainer = _trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        data_collator=CausalLMDataCollator(tokenizer),
        processing_class=processor,
    )
    trainer.train(resume_from_checkpoint=args.resume_from_checkpoint or None)
    trainer.save_model(str(out_dir))
    processor.save_pretrained(str(out_dir))
    (out_dir / "h5_qwen_sft_config.json").write_text(json.dumps(vars(args), indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="LoRA SFT for H5 answer-only / trajectory datasets with Qwen3-VL.")
    parser.add_argument("--model-name-or-path", default="models/Qwen3-VL-8B-Instruct")
    parser.add_argument("--train-file", required=True)
    parser.add_argument("--eval-file")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-length", type=int, default=4096)
    parser.add_argument("--num-train-epochs", type=float, default=2.0)
    parser.add_argument("--per-device-train-batch-size", type=int, default=1)
    parser.add_argument("--per-device-eval-batch-size", type=int, default=1)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--warmup-ratio", type=float, default=0.03)
    parser.add_argument("--weight-decay", type=float, default=0.0)
    parser.add_argument("--logging-steps", type=int, default=5)
    parser.add_argument("--save-steps", type=int, default=50)
    parser.add_argument("--eval-steps", type=int, default=50)
    parser.add_argument("--save-total-limit", type=int, default=2)
    parser.add_argument("--dtype", choices=["auto", "bf16", "fp16", "fp32"], default="bf16")
    parser.add_argument("--device-map", default="auto")
    parser.add_argument("--attn-implementation", default="")
    parser.add_argument("--gradient-checkpointing", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--load-in-4bit", action="store_true")
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument(
        "--target-modules",
        default="q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj",
    )
    parser.add_argument("--report-to", default="none")
    parser.add_argument("--resume-from-checkpoint", default="")
    args = parser.parse_args()
    train(args)


if __name__ == "__main__":
    main()
