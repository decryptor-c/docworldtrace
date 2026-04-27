from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

from .types import DocumentRecord, PageRecord, TableRecord, WordRecord
from .utils import first_non_empty_line


def load_document_json(path: str) -> DocumentRecord:
    with open(path, "r", encoding="utf-8") as handle:
        return DocumentRecord.from_dict(json.load(handle))


def load_pdf_document(
    pdf_path: str,
    output_dir: Optional[str] = None,
    render_dpi: int = 150,
) -> DocumentRecord:
    try:
        import fitz  # type: ignore
        import pdfplumber  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "PDF loading requires PyMuPDF and pdfplumber. "
            "Run scripts/setup_python_env.sh on the server first."
        ) from exc

    pdf_path_obj = Path(pdf_path).expanduser().resolve()
    doc_id = pdf_path_obj.stem
    artifact_root = (
        Path(output_dir).expanduser().resolve()
        if output_dir
        else Path("artifacts/docenv") / doc_id
    )
    artifact_root.mkdir(parents=True, exist_ok=True)

    fitz_doc = fitz.open(str(pdf_path_obj))
    pages: List[PageRecord] = []

    with pdfplumber.open(str(pdf_path_obj)) as plumber_doc:
        for index, plumber_page in enumerate(plumber_doc.pages):
            fitz_page = fitz_doc.load_page(index)
            page_number = index + 1
            words = []
            for item in plumber_page.extract_words() or []:
                words.append(
                    WordRecord(
                        text=item.get("text", ""),
                        bbox=(
                            float(item["x0"]),
                            float(item["top"]),
                            float(item["x1"]),
                            float(item["bottom"]),
                        ),
                    )
                )

            tables = []
            if hasattr(plumber_page, "find_tables"):
                try:
                    found_tables = plumber_page.find_tables()
                except Exception:
                    found_tables = []
                for table in found_tables:
                    rows = table.extract() or []
                    tables.append(
                        TableRecord(
                            bbox=tuple(float(value) for value in table.bbox),
                            rows=[
                                ["" if cell is None else str(cell) for cell in row]
                                for row in rows
                            ],
                        )
                    )

            text = plumber_page.extract_text() or fitz_page.get_text("text") or ""
            summary = first_non_empty_line(text)[:160]

            zoom = render_dpi / 72.0
            pix = fitz_page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
            image_path = artifact_root / f"page_{page_number:03d}.png"
            pix.save(str(image_path))

            pages.append(
                PageRecord(
                    page_number=page_number,
                    text=text,
                    summary=summary,
                    words=words,
                    tables=tables,
                    width=float(fitz_page.rect.width),
                    height=float(fitz_page.rect.height),
                    image_path=str(image_path),
                    metadata={
                        "word_count": len(words),
                        "table_count": len(tables),
                    },
                )
            )

    fitz_doc.close()
    return DocumentRecord(
        doc_id=doc_id,
        title=doc_id,
        pages=pages,
        metadata={
            "source": str(pdf_path_obj),
            "render_dpi": render_dpi,
            "page_count": len(pages),
        },
    )
