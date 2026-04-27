from __future__ import annotations

from collections import Counter
from typing import Dict, Iterable, List

from .utils import tokenize


class SimpleSearchIndex:
    def __init__(self, documents: Dict[int, str]) -> None:
        self._documents = documents
        self._doc_tokens = {page: tokenize(text) for page, text in documents.items()}

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, object]]:
        query_tokens = tokenize(query)
        if not query_tokens:
            return []
        scored = []
        query_counts = Counter(query_tokens)
        for page, tokens in self._doc_tokens.items():
            counts = Counter(tokens)
            overlap = sum(min(counts[token], query_counts[token]) for token in query_counts)
            phrase_bonus = 3 if query.lower() in self._documents[page].lower() else 0
            score = overlap + phrase_bonus
            if score > 0:
                scored.append(
                    {
                        "page": page,
                        "score": float(score),
                        "snippet": self._documents[page][:240],
                    }
                )
        scored.sort(key=lambda item: item["score"], reverse=True)
        return scored[:top_k]
