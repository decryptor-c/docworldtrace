from __future__ import annotations

import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Sequence

from .utils import tokenize


NUMBER_RE = re.compile(r"[-+]?\d+(?:\.\d+)?")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "under",
    "with",
}


@dataclass
class AtomicClaim:
    claim_id: str
    text: str
    claim_type: str
    expected_answer: str = ""
    expected_action: str = ""
    numbers: List[float] = field(default_factory=list)
    unit: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class EvidenceItem:
    evidence_id: str
    source_action: str
    text: str
    page: Optional[int] = None
    bbox: Optional[List[float]] = None
    element_type: Optional[str] = None
    confidence: float = 1.0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ClaimJudgment:
    claim_id: str
    label: str
    sufficiency: str
    confidence: float
    evidence_ids: List[str]
    rationale: str
    failure_taxonomy: Optional[str] = None
    signals: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def compact_text(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def numbers(value: str) -> List[float]:
    return [float(item) for item in NUMBER_RE.findall(value or "")]


def meaningful_tokens(value: str) -> List[str]:
    return [token for token in tokenize(value) if token not in STOPWORDS and len(token) > 1]


def token_f1(reference: str, prediction: str) -> float:
    ref_tokens = meaningful_tokens(reference)
    pred_tokens = meaningful_tokens(prediction)
    if not ref_tokens and not pred_tokens:
        return 1.0
    if not ref_tokens or not pred_tokens:
        return 0.0
    ref_counts = Counter(ref_tokens)
    pred_counts = Counter(pred_tokens)
    overlap = sum(min(count, pred_counts.get(token, 0)) for token, count in ref_counts.items())
    if overlap == 0:
        return 0.0
    precision = overlap / len(pred_tokens)
    recall = overlap / len(ref_tokens)
    return 2 * precision * recall / (precision + recall)


def numeric_match(expected: Sequence[float], text: str, tolerance: float = 1e-6) -> bool:
    observed = numbers(text)
    if not expected:
        return True
    return all(any(abs(item - candidate) <= tolerance for candidate in observed) for item in expected[:1])


def has_percentage_point_unit(value: str) -> bool:
    normalized = (value or "").lower()
    compact = compact_text(value)
    return (
        "percentage point" in normalized
        or "percentage points" in normalized
        or "percentagepoint" in compact
        or "percentagepoints" in compact
    )


def _string_contains(reference: str, prediction: str) -> bool:
    ref = compact_text(reference)
    pred = compact_text(prediction)
    return bool(ref and pred and (ref in pred or pred in ref and len(pred) >= 8))


def _extract_sentences(text: str) -> List[str]:
    clean = " ".join((text or "").split())
    if not clean:
        return []
    parts = [part.strip() for part in SENTENCE_SPLIT_RE.split(clean) if part.strip()]
    return parts or [clean]


class ClaimDecomposer:
    def decompose(self, seed: Dict[str, Any], final_action: Optional[str], final_answer: str) -> List[AtomicClaim]:
        task_type = seed.get("task_type", "")
        reference = seed.get("reference_answer", "")
        answerable = bool(seed.get("answerable", True))
        final_answer = final_answer or ""
        if not answerable:
            return [
                AtomicClaim(
                    claim_id="c1",
                    text="The requested information is not provided by the document.",
                    claim_type="refusal_absence",
                    expected_answer="REFUSE",
                    expected_action="refuse",
                    metadata={"question": seed.get("question", "")},
                )
            ]
        if task_type == "verification":
            claim = seed.get("metadata", {}).get("claim") or _extract_claim_from_question(seed.get("question", ""))
            return [
                AtomicClaim(
                    claim_id="c1",
                    text=claim or final_answer,
                    claim_type="verification",
                    expected_answer=reference,
                    expected_action="answer",
                    metadata={"final_answer": final_answer},
                )
            ]
        if task_type == "numeric_computation":
            return [
                AtomicClaim(
                    claim_id="c1",
                    text=f"The computed answer is {final_answer}.",
                    claim_type="numeric",
                    expected_answer=reference,
                    expected_action="answer",
                    numbers=numbers(reference),
                    unit="percentage_points" if has_percentage_point_unit(reference) else None,
                    metadata={"question": seed.get("question", "")},
                )
            ]
        if task_type == "table_lookup":
            return [
                AtomicClaim(
                    claim_id="c1",
                    text=f"The table answer is {final_answer}.",
                    claim_type="table_cell",
                    expected_answer=reference,
                    expected_action="answer",
                    numbers=numbers(reference),
                    metadata={"question": seed.get("question", "")},
                )
            ]
        claims = []
        for index, sentence in enumerate(_extract_sentences(final_answer), start=1):
            claims.append(
                AtomicClaim(
                    claim_id=f"c{index}",
                    text=sentence,
                    claim_type="text_answer",
                    expected_answer=reference,
                    expected_action="answer",
                    numbers=numbers(reference),
                    metadata={"question": seed.get("question", "")},
                )
            )
        return claims or [
            AtomicClaim(
                claim_id="c1",
                text=final_answer,
                claim_type="text_answer",
                expected_answer=reference,
                expected_action="answer",
            )
        ]


def _extract_claim_from_question(question: str) -> str:
    match = re.search(r'"([^"]+)"', question or "")
    if match:
        return match.group(1)
    return question


def _verification_label(value: str) -> Optional[str]:
    tokens = re.findall(r"[A-Z_]+", (value or "").upper())
    if "UNSUPPORTED" in tokens:
        return "UNSUPPORTED"
    if "SUPPORTED" in tokens:
        return "SUPPORTED"
    return None


class EvidenceCollector:
    def collect(self, payload: Dict[str, Any]) -> List[EvidenceItem]:
        items: List[EvidenceItem] = []
        for step in payload.get("trajectory", []):
            action = step.get("action")
            observation = step.get("observation") or {}
            if not action or observation.get("status") not in {"success", "partial"}:
                continue
            result = observation.get("result") or {}
            provenance = observation.get("provenance") or {}
            before = len(items)
            if action == "search":
                for result_index, item in enumerate(result.get("results", [])[:5], start=1):
                    items.append(
                        EvidenceItem(
                            evidence_id=f"e{len(items)+1}",
                            source_action="search",
                            text=str(item.get("snippet", "")),
                            page=_safe_int(item.get("page")),
                            element_type="search_snippet",
                            confidence=float(observation.get("confidence", 0.6)),
                            metadata={"step": step.get("step"), "rank": result_index, "score": item.get("score")},
                        )
                    )
            elif action == "read_page":
                for page in result.get("pages", []):
                    text = str(page.get("text") or page.get("summary") or "")
                    items.append(
                        EvidenceItem(
                            evidence_id=f"e{len(items)+1}",
                            source_action="read_page",
                            text=text,
                            page=_safe_int(page.get("page")),
                            element_type="page",
                            confidence=float(observation.get("confidence", 0.9)),
                            metadata={"step": step.get("step"), "summary": page.get("summary")},
                        )
                    )
            elif action in {"crop", "ocr"}:
                items.append(
                    EvidenceItem(
                        evidence_id=f"e{len(items)+1}",
                        source_action=action,
                        text=str(result.get("text", "")),
                        page=_safe_int(result.get("page") or provenance.get("page")),
                        bbox=_safe_bbox(result.get("bbox") or provenance.get("bbox")),
                        element_type=provenance.get("element_type") or action,
                        confidence=float(observation.get("confidence", 0.7)),
                        metadata={"step": step.get("step")},
                    )
                )
            elif action == "parse_table":
                table_text = str(result.get("markdown") or _rows_to_text(result.get("rows", [])))
                items.append(
                    EvidenceItem(
                        evidence_id=f"e{len(items)+1}",
                        source_action="parse_table",
                        text=table_text,
                        page=_safe_int(result.get("page") or provenance.get("page")),
                        bbox=_safe_bbox(result.get("bbox") or provenance.get("bbox")),
                        element_type="table",
                        confidence=float(observation.get("confidence", 0.8)),
                        metadata={"step": step.get("step"), "rows": result.get("rows", [])[:8]},
                    )
                )
            elif action == "compute":
                items.append(
                    EvidenceItem(
                        evidence_id=f"e{len(items)+1}",
                        source_action="compute",
                        text=jsonish({"expr": result.get("expr"), "value": result.get("value"), "error": result.get("error")}),
                        element_type="computed_value",
                        confidence=float(observation.get("confidence", 1.0)),
                        metadata={"step": step.get("step"), "value": result.get("value")},
                    )
                )
            elif action == "verify":
                items.append(
                    EvidenceItem(
                        evidence_id=f"e{len(items)+1}",
                        source_action="verify",
                        text=jsonish(result),
                        element_type="verification",
                        confidence=float(observation.get("confidence", 0.7)),
                        metadata={"step": step.get("step"), **result},
                    )
                )
            if len(items) == before and action not in {"answer", "refuse"}:
                text = _fallback_observation_text(result)
                if text:
                    items.append(
                        EvidenceItem(
                            evidence_id=f"e{len(items)+1}",
                            source_action=str(action),
                            text=text,
                            page=_safe_int(provenance.get("page")),
                            bbox=_safe_bbox(provenance.get("bbox")),
                            element_type=provenance.get("element_type"),
                            confidence=float(observation.get("confidence", 0.5)),
                            metadata={"step": step.get("step")},
                        )
                    )
        return [item for item in items if item.text.strip()]


def _rows_to_text(rows: Any) -> str:
    if not isinstance(rows, list):
        return ""
    return "\n".join(" | ".join(str(cell) for cell in row) for row in rows if isinstance(row, list))


def _fallback_observation_text(result: Dict[str, Any]) -> str:
    parts = []
    for key in ["text", "summary", "markdown", "content", "reason"]:
        if result.get(key):
            parts.append(str(result[key]))
    return "\n".join(parts)


def _safe_int(value: Any) -> Optional[int]:
    try:
        if value is None:
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def _safe_bbox(value: Any) -> Optional[List[float]]:
    if not isinstance(value, list) or len(value) != 4:
        return None
    try:
        return [float(item) for item in value]
    except (TypeError, ValueError):
        return None


def jsonish(value: Dict[str, Any]) -> str:
    return " ".join(f"{key}: {item}" for key, item in value.items() if item is not None)


class EvidenceRanker:
    def rank(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], top_k: int = 5) -> List[EvidenceItem]:
        scored = []
        for item in evidence_items:
            score = self._score(claim, item)
            scored.append((score, item))
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [item for score, item in scored[:top_k] if score > 0]

    def _score(self, claim: AtomicClaim, evidence: EvidenceItem) -> float:
        text = evidence.text
        f1 = token_f1(claim.text + " " + claim.expected_answer, text)
        number_bonus = 0.25 if numeric_match(claim.numbers, text) and claim.numbers else 0.0
        action_bonus = {
            "parse_table": 0.2 if claim.claim_type in {"table_cell", "numeric"} else 0.0,
            "compute": 0.15 if claim.claim_type == "numeric" else 0.0,
            "verify": 0.2 if claim.claim_type == "verification" else 0.0,
            "read_page": 0.08,
            "crop": 0.08,
            "ocr": 0.08,
            "search": 0.02,
        }.get(evidence.source_action, 0.0)
        answer_bonus = 0.35 if _string_contains(claim.expected_answer, text) else 0.0
        return f1 + number_bonus + action_bonus + answer_bonus


class SupportJudge:
    def judge(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], payload: Dict[str, Any]) -> ClaimJudgment:
        if not evidence_items:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="NOT_SUPPORTED",
                sufficiency="MISSING",
                confidence=0.2,
                evidence_ids=[],
                rationale="No evidence was available for the claim.",
                failure_taxonomy="missing_evidence",
            )
        if claim.claim_type == "refusal_absence":
            return self._judge_refusal(claim, evidence_items, payload)
        if claim.claim_type == "verification":
            return self._judge_verification(claim, evidence_items, payload)
        if claim.claim_type == "numeric":
            return self._judge_numeric(claim, evidence_items, payload)
        if claim.claim_type == "table_cell":
            return self._judge_table(claim, evidence_items, payload)
        return self._judge_text(claim, evidence_items, payload)

    def _judge_refusal(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], payload: Dict[str, Any]) -> ClaimJudgment:
        sequence = payload.get("tool_sequence", [])
        final_action = payload.get("final_action")
        has_negative_search = "search" in sequence and "read_page" in sequence
        if final_action == "refuse" and has_negative_search:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="SUPPORTED",
                sufficiency="SUFFICIENT",
                confidence=0.85,
                evidence_ids=[item.evidence_id for item in evidence_items[:3]],
                rationale="The trajectory searched and inspected document pages before refusing.",
                failure_taxonomy=None,
                signals={"negative_search": True},
            )
        return ClaimJudgment(
            claim_id=claim.claim_id,
            label="PARTIAL",
            sufficiency="INSUFFICIENT",
            confidence=0.45,
            evidence_ids=[item.evidence_id for item in evidence_items[:3]],
            rationale="The refusal lacks the expected search/read_page negative-evidence path.",
            failure_taxonomy="insufficient_negative_evidence",
            signals={"negative_search": has_negative_search},
        )

    def _judge_verification(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], payload: Dict[str, Any]) -> ClaimJudgment:
        verify_items = [item for item in evidence_items if item.source_action == "verify"]
        final_label = _verification_label(payload.get("final_answer") or "")
        expected_label = _verification_label(claim.expected_answer)
        final_ok = bool(expected_label and final_label == expected_label)
        if verify_items and final_ok:
            labels = " ".join(str(item.metadata.get("label", "")) for item in verify_items)
            evidence_label = _verification_label(labels)
            if evidence_label == expected_label:
                return ClaimJudgment(
                    claim_id=claim.claim_id,
                    label="SUPPORTED",
                    sufficiency="SUFFICIENT",
                    confidence=0.9,
                    evidence_ids=[item.evidence_id for item in verify_items[:2]],
                    rationale="The verify tool was used and the final answer matches the expected verification label.",
                    failure_taxonomy=None,
                    signals={"verify_used": True},
                )
        if verify_items and not final_ok:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="NOT_SUPPORTED",
                sufficiency="INSUFFICIENT",
                confidence=0.35,
                evidence_ids=[item.evidence_id for item in verify_items[:2]],
                rationale="The verify tool was used, but the final verification answer does not match the expected label.",
                failure_taxonomy="verification_label_mismatch",
                signals={"verify_used": True, "final_ok": final_ok},
            )
        return self._judge_text(claim, evidence_items, payload)

    def _judge_numeric(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], payload: Dict[str, Any]) -> ClaimJudgment:
        final = payload.get("final_answer") or ""
        number_ok = numeric_match(claim.numbers, final)
        unit_ok = not claim.unit or has_percentage_point_unit(final)
        has_document_evidence = any(item.source_action in {"read_page", "crop", "ocr", "parse_table", "search"} for item in evidence_items)
        has_compute = any(item.source_action == "compute" for item in evidence_items)
        evidence_ids = [item.evidence_id for item in evidence_items[:5]]
        if number_ok and unit_ok and has_document_evidence and has_compute:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="SUPPORTED",
                sufficiency="SUFFICIENT",
                confidence=0.92,
                evidence_ids=evidence_ids,
                rationale="The answer has the expected number/unit and the trajectory includes document evidence plus compute.",
                failure_taxonomy=None,
                signals={"number_ok": number_ok, "unit_ok": unit_ok, "has_compute": has_compute},
            )
        if number_ok and unit_ok:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="PARTIAL",
                sufficiency="INSUFFICIENT",
                confidence=0.62,
                evidence_ids=evidence_ids,
                rationale="The numeric answer is correct, but the trajectory lacks document evidence or compute provenance.",
                failure_taxonomy="answer_without_document_evidence" if not has_document_evidence else "missing_compute",
                signals={"number_ok": number_ok, "unit_ok": unit_ok, "has_compute": has_compute},
            )
        return ClaimJudgment(
            claim_id=claim.claim_id,
            label="NOT_SUPPORTED",
            sufficiency="INSUFFICIENT",
            confidence=0.3,
            evidence_ids=evidence_ids,
            rationale="The numeric answer does not match the expected value or unit.",
            failure_taxonomy="numeric_mismatch" if not number_ok else "unit_error",
            signals={"number_ok": number_ok, "unit_ok": unit_ok},
        )

    def _judge_table(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], payload: Dict[str, Any]) -> ClaimJudgment:
        final = payload.get("final_answer") or ""
        final_ok = _string_contains(claim.expected_answer, final)
        evidence_ok = _string_contains(claim.expected_answer, " ".join(item.text for item in evidence_items))
        has_table = any(item.source_action == "parse_table" for item in evidence_items)
        evidence_ids = [item.evidence_id for item in evidence_items[:5]]
        if final_ok and evidence_ok and has_table:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="SUPPORTED",
                sufficiency="SUFFICIENT",
                confidence=0.9,
                evidence_ids=evidence_ids,
                rationale="The expected table value appears in the final answer/table evidence and parse_table was used.",
                failure_taxonomy=None,
                signals={"has_table": True},
            )
        if final_ok:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="PARTIAL",
                sufficiency="INSUFFICIENT",
                confidence=0.6,
                evidence_ids=evidence_ids,
                rationale="The answer matches, but table-structured evidence is missing.",
                failure_taxonomy="missing_table_evidence",
                signals={"has_table": has_table, "evidence_ok": evidence_ok},
            )
        if evidence_ok and has_table:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="NOT_SUPPORTED",
                sufficiency="INSUFFICIENT",
                confidence=0.35,
                evidence_ids=evidence_ids,
                rationale="The table evidence contains the expected value, but the final answer does not match it.",
                failure_taxonomy="table_value_mismatch",
                signals={"has_table": has_table, "evidence_ok": evidence_ok, "final_ok": final_ok},
            )
        return self._not_supported_text(claim, evidence_items, "table_value_mismatch")

    def _judge_text(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], payload: Dict[str, Any]) -> ClaimJudgment:
        final = payload.get("final_answer") or ""
        evidence_text = " ".join(item.text for item in evidence_items[:5])
        answer_ok = _string_contains(claim.expected_answer, final)
        evidence_ok = _string_contains(claim.expected_answer, evidence_text) or token_f1(claim.expected_answer, evidence_text) >= 0.45
        evidence_ids = [item.evidence_id for item in evidence_items[:5]]
        if answer_ok and evidence_ok:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="SUPPORTED",
                sufficiency="SUFFICIENT",
                confidence=0.88,
                evidence_ids=evidence_ids,
                rationale="The final answer matches the reference and evidence contains matching content.",
                failure_taxonomy=None,
                signals={"answer_ok": answer_ok, "evidence_ok": evidence_ok},
            )
        if answer_ok:
            return ClaimJudgment(
                claim_id=claim.claim_id,
                label="PARTIAL",
                sufficiency="INSUFFICIENT",
                confidence=0.58,
                evidence_ids=evidence_ids,
                rationale="The final answer matches the reference, but evidence match is weak.",
                failure_taxonomy="weak_evidence_support",
                signals={"answer_ok": answer_ok, "evidence_ok": evidence_ok},
            )
        return self._not_supported_text(claim, evidence_items, "answer_mismatch")

    def _not_supported_text(self, claim: AtomicClaim, evidence_items: List[EvidenceItem], failure: str) -> ClaimJudgment:
        return ClaimJudgment(
            claim_id=claim.claim_id,
            label="NOT_SUPPORTED",
            sufficiency="INSUFFICIENT",
            confidence=0.35,
            evidence_ids=[item.evidence_id for item in evidence_items[:5]],
            rationale="The final answer does not match the expected answer or evidence.",
            failure_taxonomy=failure,
        )


class RewardScorer:
    def score(self, payload: Dict[str, Any], judgments: List[ClaimJudgment], evidence_items: List[EvidenceItem]) -> Dict[str, float]:
        seed = payload["seed"]
        final_action = payload.get("final_action")
        sequence = payload.get("tool_sequence", [])
        answerable = bool(seed.get("answerable", True))
        expected_terminal = "answer" if answerable else "refuse"
        supported = [judgment for judgment in judgments if judgment.label == "SUPPORTED"]
        sufficient = [judgment for judgment in judgments if judgment.sufficiency == "SUFFICIENT"]
        support_score = len(supported) / len(judgments) if judgments else 0.0
        sufficiency_score = len(sufficient) / len(judgments) if judgments else 0.0
        terminal_score = 1.0 if final_action == expected_terminal else 0.0
        evidence_score = 1.0 if any(item.source_action not in {"compute"} for item in evidence_items) else 0.0
        required = [tool for tool in seed.get("required_tools", []) if tool not in {"answer", "refuse"}]
        tool_score = sum(1 for tool in required if tool in sequence) / len(required) if required else 1.0
        efficiency_score = max(0.0, 1.0 - max(0, len(sequence) - 4) * 0.08)
        refusal_score = 1.0 if (answerable or final_action == "refuse") else 0.0
        quality = (
            0.25 * terminal_score
            + 0.25 * support_score
            + 0.2 * sufficiency_score
            + 0.1 * evidence_score
            + 0.1 * tool_score
            + 0.05 * efficiency_score
            + 0.05 * refusal_score
        )
        return {
            "R_answer": round(terminal_score, 4),
            "R_support": round(support_score, 4),
            "R_sufficiency": round(sufficiency_score, 4),
            "R_ground": round(evidence_score, 4),
            "R_tool": round(tool_score, 4),
            "R_efficiency": round(efficiency_score, 4),
            "R_refusal": round(refusal_score, 4),
            "quality_score": round(quality, 4),
        }


class DocVerifyPlus:
    def __init__(self, top_k: int = 5) -> None:
        self.decomposer = ClaimDecomposer()
        self.collector = EvidenceCollector()
        self.ranker = EvidenceRanker()
        self.judge = SupportJudge()
        self.reward = RewardScorer()
        self.top_k = top_k

    def verify_rollout(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        seed = payload["seed"]
        final_action = payload.get("final_action")
        final_answer = payload.get("final_answer") or ""
        claims = self.decomposer.decompose(seed, final_action, final_answer)
        evidence_items = self.collector.collect(payload)
        if payload.get("status") != "completed" or final_action not in {"answer", "refuse"}:
            judgments = [
                ClaimJudgment(
                    claim_id=claim.claim_id,
                    label="INVALID",
                    sufficiency="INVALID",
                    confidence=0.1,
                    evidence_ids=[],
                    rationale="The rollout did not terminate with a valid answer/refuse action.",
                    failure_taxonomy=payload.get("status") or "invalid_terminal",
                )
                for claim in claims
            ]
            rewards = self.reward.score(payload, judgments, evidence_items)
            return {
                "support_label": "INVALID",
                "sufficiency": "INVALID",
                "filter_decision": "reject",
                "failure_taxonomy": payload.get("status") or "invalid_terminal",
                "claims": [claim.to_dict() for claim in claims],
                "evidence": [item.to_dict() for item in evidence_items],
                "claim_judgments": [judgment.to_dict() for judgment in judgments],
                "reward_signals": rewards,
            }
        judgments = []
        for claim in claims:
            ranked = self.ranker.rank(claim, evidence_items, top_k=self.top_k)
            judgments.append(self.judge.judge(claim, ranked, payload))
        rewards = self.reward.score(payload, judgments, evidence_items)
        support_label = _aggregate_support(judgments)
        sufficiency = _aggregate_sufficiency(judgments)
        failure_types = [judgment.failure_taxonomy for judgment in judgments if judgment.failure_taxonomy]
        filter_decision = _filter_decision(payload, support_label, sufficiency, rewards)
        return {
            "support_label": support_label,
            "sufficiency": sufficiency,
            "filter_decision": filter_decision,
            "failure_taxonomy": failure_types[0] if failure_types else None,
            "claims": [claim.to_dict() for claim in claims],
            "evidence": [item.to_dict() for item in evidence_items],
            "claim_judgments": [judgment.to_dict() for judgment in judgments],
            "reward_signals": rewards,
        }


def _aggregate_support(judgments: List[ClaimJudgment]) -> str:
    if not judgments:
        return "NOT_SUPPORTED"
    labels = {judgment.label for judgment in judgments}
    if labels == {"SUPPORTED"}:
        return "SUPPORTED"
    if "NOT_SUPPORTED" in labels:
        return "NOT_SUPPORTED"
    if "PARTIAL" in labels:
        return "PARTIAL"
    return "NOT_SUPPORTED"


def _aggregate_sufficiency(judgments: List[ClaimJudgment]) -> str:
    if judgments and all(judgment.sufficiency == "SUFFICIENT" for judgment in judgments):
        return "SUFFICIENT"
    if any(judgment.sufficiency == "MISSING" for judgment in judgments):
        return "MISSING"
    return "INSUFFICIENT"


def _filter_decision(payload: Dict[str, Any], support_label: str, sufficiency: str, rewards: Dict[str, float]) -> str:
    if payload.get("status") != "completed" or payload.get("final_action") not in {"answer", "refuse"}:
        return "reject"
    if support_label == "SUPPORTED" and sufficiency == "SUFFICIENT" and rewards["quality_score"] >= 0.75:
        return "keep"
    if support_label == "NOT_SUPPORTED":
        return "reject"
    return "review"
