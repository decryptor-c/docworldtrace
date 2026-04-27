from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

BBox = Tuple[float, float, float, float]


@dataclass
class Provenance:
    page: Optional[int] = None
    bbox: Optional[List[float]] = None
    element_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Observation:
    action: str
    status: str
    result: Dict[str, Any]
    provenance: Provenance = field(default_factory=Provenance)
    confidence: float = 1.0
    cache_hit: bool = False

    def to_dict(self) -> Dict[str, Any]:
        payload = asdict(self)
        payload["provenance"] = self.provenance.to_dict()
        return payload


@dataclass
class WordRecord:
    text: str
    bbox: BBox

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WordRecord":
        return cls(text=data["text"], bbox=tuple(data["bbox"]))


@dataclass
class TableRecord:
    bbox: BBox
    rows: List[List[str]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TableRecord":
        return cls(
            bbox=tuple(data["bbox"]),
            rows=[list(row) for row in data.get("rows", [])],
            metadata=dict(data.get("metadata", {})),
        )

    def to_markdown(self) -> str:
        if not self.rows:
            return ""
        header = self.rows[0]
        body = self.rows[1:] or [[]]
        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(["---"] * len(header)) + " |",
        ]
        for row in body:
            padded = row + [""] * max(0, len(header) - len(row))
            lines.append("| " + " | ".join(padded[: len(header)]) + " |")
        return "\n".join(lines)


@dataclass
class PageRecord:
    page_number: int
    text: str = ""
    summary: str = ""
    words: List[WordRecord] = field(default_factory=list)
    tables: List[TableRecord] = field(default_factory=list)
    width: float = 0.0
    height: float = 0.0
    image_path: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PageRecord":
        return cls(
            page_number=int(data["page_number"]),
            text=data.get("text", ""),
            summary=data.get("summary", ""),
            words=[WordRecord.from_dict(item) for item in data.get("words", [])],
            tables=[TableRecord.from_dict(item) for item in data.get("tables", [])],
            width=float(data.get("width", 0.0)),
            height=float(data.get("height", 0.0)),
            image_path=data.get("image_path"),
            metadata=dict(data.get("metadata", {})),
        )


@dataclass
class DocumentRecord:
    doc_id: str
    title: str
    pages: List[PageRecord]
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DocumentRecord":
        return cls(
            doc_id=data["doc_id"],
            title=data.get("title", data["doc_id"]),
            pages=[PageRecord.from_dict(item) for item in data["pages"]],
            metadata=dict(data.get("metadata", {})),
        )


def bbox_to_list(bbox: Optional[Sequence[float]]) -> Optional[List[float]]:
    if bbox is None:
        return None
    return [float(value) for value in bbox]
