from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TeacherConfig:
    name: str
    api_base: str
    model: str
    api_key_env: str
    temperature: float = 0.2
    max_tokens: int = 400
    timeout_sec: int = 120
    max_retries: int = 3
    retry_delay_sec: float = 2.0
    extra_headers: Optional[Dict[str, str]] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TeacherConfig":
        return cls(
            name=data["name"],
            api_base=data["api_base"],
            model=data["model"],
            api_key_env=data["api_key_env"],
            temperature=float(data.get("temperature", 0.2)),
            max_tokens=int(data.get("max_tokens", 400)),
            timeout_sec=int(data.get("timeout_sec", 120)),
            max_retries=int(data.get("max_retries", 3)),
            retry_delay_sec=float(data.get("retry_delay_sec", 2.0)),
            extra_headers=dict(data.get("extra_headers", {})),
        )


class OpenAICompatibleClient:
    def __init__(self, config: TeacherConfig) -> None:
        self.config = config

    def chat(self, messages: List[Dict[str, str]]) -> Dict[str, Any]:
        api_key = os.environ.get(self.config.api_key_env)
        if not api_key:
            raise RuntimeError(f"Missing API key env var: {self.config.api_key_env}")

        url = self.config.api_base.rstrip("/") + "/chat/completions"
        payload = {
            "model": self.config.model,
            "messages": messages,
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }
        body = json.dumps(payload).encode("utf-8")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        }
        headers.update(self.config.extra_headers or {})

        raw = self._post_with_retries(url, body, headers)

        payload = json.loads(raw)
        try:
            message = payload["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"Unexpected teacher response shape: {payload}") from exc
        return {
            "content": message,
            "usage": payload.get("usage", {}),
            "raw_response": payload,
        }

    def _post_with_retries(self, url: str, body: bytes, headers: Dict[str, str]) -> str:
        attempts = max(1, self.config.max_retries + 1)
        last_error: Optional[BaseException] = None
        for attempt in range(1, attempts + 1):
            request = urllib.request.Request(url, data=body, headers=headers, method="POST")
            try:
                with urllib.request.urlopen(request, timeout=self.config.timeout_sec) as response:
                    return response.read().decode("utf-8")
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="ignore")
                if exc.code not in {429, 500, 502, 503, 504} or attempt == attempts:
                    raise RuntimeError(f"Teacher API HTTP {exc.code}: {detail}") from exc
                last_error = RuntimeError(f"Teacher API HTTP {exc.code}: {detail}")
            except urllib.error.URLError as exc:
                if attempt == attempts:
                    raise RuntimeError(f"Teacher API request failed: {exc}") from exc
                last_error = exc

            delay = self.config.retry_delay_sec * (2 ** (attempt - 1))
            time.sleep(delay)

        raise RuntimeError(f"Teacher API request failed after retries: {last_error}")


def load_teacher_configs(path: str) -> List[TeacherConfig]:
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    items = payload["teachers"] if isinstance(payload, dict) else payload
    return [TeacherConfig.from_dict(item) for item in items]
