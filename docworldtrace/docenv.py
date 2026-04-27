from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple

from PIL import Image

from .cache import ObservationCache
from .loaders import load_document_json, load_pdf_document
from .safe_eval import safe_eval
from .search import SimpleSearchIndex
from .types import BBox, DocumentRecord, Observation, PageRecord, Provenance, bbox_to_list
from .utils import bbox_contains, bbox_overlap_ratio, choose_best_bbox, first_non_empty_line
from .verify import SimpleVerifier


class DocEnv:
    CACHED_ACTIONS = {
        "overview",
        "search",
        "read_page",
        "crop",
        "ocr",
        "parse_table",
        "verify",
        "detect_layout",
    }

    def __init__(self, document: DocumentRecord) -> None:
        self.document = document
        self.cache = ObservationCache()
        self.verifier = SimpleVerifier()
        self.search_index = SimpleSearchIndex(
            {page.page_number: page.text for page in self.document.pages}
        )

    @classmethod
    def from_json(cls, path: str) -> "DocEnv":
        return cls(load_document_json(path))

    @classmethod
    def from_pdf(
        cls,
        path: str,
        output_dir: Optional[str] = None,
        render_dpi: int = 150,
    ) -> "DocEnv":
        return cls(load_pdf_document(path, output_dir=output_dir, render_dpi=render_dpi))

    def execute(self, action: str, **params: Any) -> Dict[str, Any]:
        dispatch = {
            "overview": self.overview,
            "search": self.search,
            "read_page": self.read_page,
            "crop": self.crop,
            "ocr": self.ocr,
            "parse_table": self.parse_table,
            "compute": self.compute,
            "verify": self.verify,
            "answer": self.answer,
            "refuse": self.refuse,
            "detect_layout": self.detect_layout,
        }
        if action not in dispatch:
            raise ValueError(f"Unsupported action: {action}")
        return dispatch[action](**params)

    def overview(self) -> Dict[str, Any]:
        return self._cached("overview", {}, self._build_overview)

    def search(self, query: str, top_k: int = 3) -> Dict[str, Any]:
        payload = {"query": query, "top_k": top_k}

        def builder() -> Observation:
            results = self.search_index.search(query, top_k=top_k)
            return Observation(
                action="search",
                status="success" if results else "partial",
                result={
                    "query": query,
                    "results": results,
                },
                provenance=Provenance(element_type="page_list"),
                confidence=0.85 if results else 0.4,
            )

        return self._cached("search", payload, builder)

    def read_page(self, page_ids: Sequence[int]) -> Dict[str, Any]:
        payload = {"page_ids": list(page_ids)}

        def builder() -> Observation:
            pages = []
            missing = []
            for page_id in page_ids:
                page = self._get_page(page_id)
                if page is None:
                    missing.append(page_id)
                    continue
                pages.append(
                    {
                        "page": page.page_number,
                        "text": page.text,
                        "summary": page.summary,
                        "image_path": page.image_path,
                    }
                )
            status = "success" if pages and not missing else "partial" if pages else "failure"
            return Observation(
                action="read_page",
                status=status,
                result={"pages": pages, "missing": missing},
                provenance=Provenance(
                    page=pages[0]["page"] if len(pages) == 1 else None,
                    element_type="page",
                ),
                confidence=0.95 if status == "success" else 0.5,
            )

        return self._cached("read_page", payload, builder)

    def crop(self, page_id: int, bbox: Sequence[float]) -> Dict[str, Any]:
        bbox_tuple = tuple(float(value) for value in bbox)
        payload = {"page_id": page_id, "bbox": list(bbox_tuple)}

        def builder() -> Observation:
            page = self._require_page(page_id)
            crop_text = self._extract_text_in_bbox(page, bbox_tuple)
            crop_path = self._render_crop(page, bbox_tuple)
            status = "success" if crop_text or crop_path else "partial"
            return Observation(
                action="crop",
                status=status,
                result={
                    "page": page_id,
                    "bbox": list(bbox_tuple),
                    "text": crop_text,
                    "image_path": crop_path,
                },
                provenance=Provenance(
                    page=page_id,
                    bbox=bbox_to_list(bbox_tuple),
                    element_type="region",
                ),
                confidence=0.9 if crop_text else 0.55,
            )

        return self._cached("crop", payload, builder)

    def ocr(self, page_id: int, bbox: Optional[Sequence[float]] = None) -> Dict[str, Any]:
        bbox_tuple = None if bbox is None else tuple(float(value) for value in bbox)
        payload = {"page_id": page_id, "bbox": bbox_to_list(bbox_tuple)}

        def builder() -> Observation:
            page = self._require_page(page_id)
            if bbox_tuple is None:
                text = page.text
                image_path = page.image_path
            else:
                text = self._extract_text_in_bbox(page, bbox_tuple)
                image_path = self._render_crop(page, bbox_tuple)
            if not text.strip() and image_path:
                text = self._tesseract_ocr(image_path)
            status = "success" if text.strip() else "failure"
            return Observation(
                action="ocr",
                status=status,
                result={
                    "page": page_id,
                    "bbox": bbox_to_list(bbox_tuple),
                    "text": text,
                },
                provenance=Provenance(
                    page=page_id,
                    bbox=bbox_to_list(bbox_tuple),
                    element_type="ocr_text",
                ),
                confidence=0.88 if status == "success" else 0.3,
            )

        return self._cached("ocr", payload, builder)

    def parse_table(self, page_id: int, bbox: Sequence[float]) -> Dict[str, Any]:
        bbox_tuple = tuple(float(value) for value in bbox)
        payload = {"page_id": page_id, "bbox": list(bbox_tuple)}

        def builder() -> Observation:
            page = self._require_page(page_id)
            if not page.tables:
                return Observation(
                    action="parse_table",
                    status="failure",
                    result={"reason": "no_tables_detected"},
                    provenance=Provenance(page=page_id, bbox=bbox_to_list(bbox_tuple)),
                    confidence=0.2,
                )
            index, score = choose_best_bbox(
                bbox_tuple,
                [table.bbox for table in page.tables],
            )
            if index < 0 or score < 0.2:
                return Observation(
                    action="parse_table",
                    status="failure",
                    result={"reason": "no_table_match"},
                    provenance=Provenance(page=page_id, bbox=bbox_to_list(bbox_tuple)),
                    confidence=0.2,
                )
            table = page.tables[index]
            return Observation(
                action="parse_table",
                status="success",
                result={
                    "page": page_id,
                    "bbox": list(table.bbox),
                    "rows": table.rows,
                    "markdown": table.to_markdown(),
                },
                provenance=Provenance(
                    page=page_id,
                    bbox=bbox_to_list(table.bbox),
                    element_type="table",
                ),
                confidence=min(0.95, 0.55 + score),
            )

        return self._cached("parse_table", payload, builder)

    def compute(self, expr: str, vars: Dict[str, Any]) -> Dict[str, Any]:
        try:
            value = safe_eval(expr, vars)
            return Observation(
                action="compute",
                status="success",
                result={"expr": expr, "vars": vars, "value": value},
                provenance=Provenance(element_type="computed_value"),
                confidence=1.0,
            ).to_dict()
        except Exception as exc:
            return Observation(
                action="compute",
                status="failure",
                result={"expr": expr, "vars": vars, "error": str(exc)},
                provenance=Provenance(element_type="computed_value"),
                confidence=0.0,
            ).to_dict()

    def verify(
        self,
        claim: str,
        evidence_refs: Sequence[Dict[str, Any]],
    ) -> Dict[str, Any]:
        payload = {"claim": claim, "evidence_refs": list(evidence_refs)}

        def builder() -> Observation:
            texts = []
            for ref in evidence_refs:
                text = self._resolve_evidence_ref(ref)
                if text:
                    texts.append(text)
            verdict = self.verifier.judge(claim, texts)
            return Observation(
                action="verify",
                status="success",
                result={
                    "claim": claim,
                    "evidence_count": len(texts),
                    **verdict,
                },
                provenance=Provenance(element_type="verification"),
                confidence=float(verdict["confidence"]),
            )

        return self._cached("verify", payload, builder)

    def answer(self, text: str, evidence_refs: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
        return Observation(
            action="answer",
            status="success",
            result={"text": text, "evidence_refs": list(evidence_refs), "terminated": True},
            provenance=Provenance(element_type="final_answer"),
            confidence=1.0,
        ).to_dict()

    def refuse(self, reason: str) -> Dict[str, Any]:
        return Observation(
            action="refuse",
            status="success",
            result={"reason": reason, "terminated": True},
            provenance=Provenance(element_type="refusal"),
            confidence=1.0,
        ).to_dict()

    def detect_layout(self, page_id: int) -> Dict[str, Any]:
        payload = {"page_id": page_id}

        def builder() -> Observation:
            page = self._require_page(page_id)
            elements = []
            for word in page.words:
                elements.append(
                    {
                        "element_type": "word",
                        "bbox": list(word.bbox),
                        "text": word.text,
                    }
                )
            for table in page.tables:
                elements.append(
                    {
                        "element_type": "table",
                        "bbox": list(table.bbox),
                        "text": first_non_empty_line(table.to_markdown()),
                    }
                )
            return Observation(
                action="detect_layout",
                status="success",
                result={"page": page_id, "elements": elements},
                provenance=Provenance(page=page_id, element_type="layout"),
                confidence=0.8,
            )

        return self._cached("detect_layout", payload, builder)

    def _build_overview(self) -> Observation:
        return Observation(
            action="overview",
            status="success",
            result={
                "doc_id": self.document.doc_id,
                "title": self.document.title,
                "page_count": len(self.document.pages),
                "pages": [
                    {
                        "page": page.page_number,
                        "summary": page.summary,
                        "image_path": page.image_path,
                    }
                    for page in self.document.pages
                ],
            },
            provenance=Provenance(element_type="document"),
            confidence=1.0,
        )

    def _cached(
        self,
        action: str,
        payload: Dict[str, Any],
        builder: Callable[[], Observation],
    ) -> Dict[str, Any]:
        if action in self.CACHED_ACTIONS:
            cached = self.cache.get(action, payload)
            if cached is not None:
                cached["cache_hit"] = True
                return cached

        observation = builder().to_dict()
        observation["cache_hit"] = False

        if action in self.CACHED_ACTIONS and observation["status"] != "failure":
            self.cache.set(action, payload, observation)
        return observation

    def _get_page(self, page_id: int) -> Optional[PageRecord]:
        for page in self.document.pages:
            if page.page_number == page_id:
                return page
        return None

    def _require_page(self, page_id: int) -> PageRecord:
        page = self._get_page(page_id)
        if page is None:
            raise ValueError(f"Unknown page: {page_id}")
        return page

    def _extract_text_in_bbox(self, page: PageRecord, bbox: BBox) -> str:
        words = []
        for word in page.words:
            if bbox_contains(bbox, word.bbox, threshold=0.3):
                words.append(word)
        if words:
            words.sort(key=lambda item: (item.bbox[1], item.bbox[0]))
            return " ".join(item.text for item in words)
        for table in page.tables:
            if bbox_overlap_ratio(bbox, table.bbox) >= 0.2:
                return table.to_markdown()
        return ""

    def _render_crop(self, page: PageRecord, bbox: BBox) -> Optional[str]:
        if not page.image_path:
            return None
        image_path = Path(page.image_path)
        if not image_path.exists() or page.width <= 0 or page.height <= 0:
            return None
        crop_dir = image_path.parent / "crops"
        crop_dir.mkdir(parents=True, exist_ok=True)
        with Image.open(image_path) as image:
            scale_x = image.width / page.width
            scale_y = image.height / page.height
            crop_box = (
                max(0, int(bbox[0] * scale_x)),
                max(0, int(bbox[1] * scale_y)),
                min(image.width, int(bbox[2] * scale_x)),
                min(image.height, int(bbox[3] * scale_y)),
            )
            if crop_box[0] >= crop_box[2] or crop_box[1] >= crop_box[3]:
                return None
            crop = image.crop(crop_box)
            crop_name = (
                f"page_{page.page_number:03d}_"
                f"{crop_box[0]}_{crop_box[1]}_{crop_box[2]}_{crop_box[3]}.png"
            )
            crop_path = crop_dir / crop_name
            crop.save(crop_path)
            return str(crop_path)

    def _resolve_evidence_ref(self, ref: Dict[str, Any]) -> str:
        page_id = ref.get("page")
        if page_id is None:
            return ""
        page = self._get_page(int(page_id))
        if page is None:
            return ""
        bbox = ref.get("bbox")
        if bbox is not None:
            return self._extract_text_in_bbox(page, tuple(float(value) for value in bbox))
        return page.text

    def _tesseract_ocr(self, image_path: str) -> str:
        try:
            import pytesseract  # type: ignore
        except ImportError:
            return ""
        try:
            return pytesseract.image_to_string(Image.open(image_path)).strip()
        except Exception:
            return ""
