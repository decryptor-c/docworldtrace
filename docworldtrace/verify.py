from __future__ import annotations

import re
from typing import Dict, Iterable, List

from .utils import tokenize

NUMBER_RE = re.compile(r"\d+(?:\.\d+)?")


class SimpleVerifier:
    def judge(self, claim: str, evidence_texts: Iterable[str]) -> Dict[str, object]:
        joined = " ".join(text for text in evidence_texts if text).strip()
        if not joined:
            return {
                "label": "UNSUPPORTED",
                "sufficiency": "INSUFFICIENT",
                "confidence": 0.2,
                "failure_taxonomy": "missing_evidence",
            }

        claim_tokens = set(tokenize(claim))
        evidence_tokens = set(tokenize(joined))
        overlap = len(claim_tokens & evidence_tokens)
        number_hits = all(number in joined for number in NUMBER_RE.findall(claim))
        support = overlap >= max(2, len(claim_tokens) // 3) and number_hits

        if support:
            return {
                "label": "SUPPORTED",
                "sufficiency": "SUFFICIENT",
                "confidence": min(0.99, 0.55 + overlap * 0.06),
                "failure_taxonomy": None,
            }

        return {
            "label": "UNSUPPORTED",
            "sufficiency": "INSUFFICIENT",
            "confidence": 0.35,
            "failure_taxonomy": "claim_not_grounded",
        }
