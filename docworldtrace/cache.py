from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Dict, Optional


class ObservationCache:
    def __init__(self) -> None:
        self._store: Dict[str, Dict[str, Any]] = {}

    def _make_key(self, action: str, payload: Dict[str, Any]) -> str:
        encoded = json.dumps({"action": action, "payload": payload}, sort_keys=True)
        return hashlib.sha256(encoded.encode("utf-8")).hexdigest()

    def get(self, action: str, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        key = self._make_key(action, payload)
        item = self._store.get(key)
        return copy.deepcopy(item) if item is not None else None

    def set(self, action: str, payload: Dict[str, Any], observation: Dict[str, Any]) -> None:
        key = self._make_key(action, payload)
        self._store[key] = copy.deepcopy(observation)

    def size(self) -> int:
        return len(self._store)
