#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Iterable, NamedTuple

from PIL import Image, ImageDraw, ImageFont


ROOT_DIR = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT_DIR / "data/reports/h1_manual_review/contact_sheet.png"

PAGE_WIDTH = 620
CROP_WIDTH = 760
ROW_IMAGE_HEIGHT = 720
MARGIN = 36
GAP = 32
TITLE_HEIGHT = 46
ROW_GAP = 34
BACKGROUND = "white"
TEXT_COLOR = (25, 25, 25)
BORDER_COLOR = (180, 180, 180)


class ReviewSample(NamedTuple):
    doc_id: str
    page: int
    page_image: Path
    crop_image: Path


SAMPLES = [
    ReviewSample(
        "2308.06595v4",
        4,
        ROOT_DIR / "artifacts/docenv/2308.06595v4/page_004.png",
        ROOT_DIR / "artifacts/docenv/2308.06595v4/crops/page_004_225_229_1044_701.png",
    ),
    ReviewSample(
        "2310.03302v2",
        7,
        ROOT_DIR / "artifacts/docenv/2310.03302v2/page_007.png",
        ROOT_DIR / "artifacts/docenv/2310.03302v2/crops/page_007_326_207_1093_531.png",
    ),
    ReviewSample(
        "2503.00808v4",
        21,
        ROOT_DIR / "artifacts/docenv/2503.00808v4/page_021.png",
        ROOT_DIR / "artifacts/docenv/2503.00808v4/crops/page_021_202_783_983_1329.png",
    ),
    ReviewSample(
        "ti2025ars",
        34,
        ROOT_DIR / "artifacts/docenv/ti2025ars/page_034.png",
        ROOT_DIR / "artifacts/docenv/ti2025ars/crops/page_034_102_131_1170_1370.png",
    ),
    ReviewSample(
        "tm2529296d2_ars",
        52,
        ROOT_DIR / "artifacts/docenv/tm2529296d2_ars/page_052.png",
        ROOT_DIR / "artifacts/docenv/tm2529296d2_ars/crops/page_052_71_206_1128_1350.png",
    ),
]


def load_font(size: int) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def check_inputs(samples: Iterable[ReviewSample]) -> None:
    missing = []
    for sample in samples:
        if not sample.page_image.exists():
            missing.append(sample.page_image)
        if not sample.crop_image.exists():
            missing.append(sample.crop_image)
    if missing:
        details = "\n".join(f"- {path}" for path in missing)
        raise SystemExit(f"Missing required review images:\n{details}")


def fit_image(path: Path, max_width: int, max_height: int) -> Image.Image:
    image = Image.open(path).convert("RGB")
    scale = min(max_width / image.width, max_height / image.height)
    new_size = (max(1, int(image.width * scale)), max(1, int(image.height * scale)))
    return image.resize(new_size, Image.Resampling.LANCZOS)


def paste_framed(canvas: Image.Image, image: Image.Image, x: int, y: int, width: int, height: int) -> None:
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([x, y, x + width, y + height], outline=BORDER_COLOR, width=2)
    paste_x = x + (width - image.width) // 2
    paste_y = y + (height - image.height) // 2
    canvas.paste(image, (paste_x, paste_y))


def build_contact_sheet() -> Image.Image:
    check_inputs(SAMPLES)
    title_font = load_font(24)
    label_font = load_font(18)

    row_height = TITLE_HEIGHT + ROW_IMAGE_HEIGHT
    canvas_width = MARGIN * 2 + PAGE_WIDTH + GAP + CROP_WIDTH
    canvas_height = MARGIN * 2 + len(SAMPLES) * row_height + (len(SAMPLES) - 1) * ROW_GAP
    canvas = Image.new("RGB", (canvas_width, canvas_height), BACKGROUND)
    draw = ImageDraw.Draw(canvas)

    y = MARGIN
    for sample in SAMPLES:
        title = f"{sample.doc_id} | page {sample.page} | crop / OCR / parse_table check"
        draw.text((MARGIN, y), title, fill=TEXT_COLOR, font=title_font)

        image_y = y + TITLE_HEIGHT
        page = fit_image(sample.page_image, PAGE_WIDTH, ROW_IMAGE_HEIGHT)
        crop = fit_image(sample.crop_image, CROP_WIDTH, ROW_IMAGE_HEIGHT)
        paste_framed(canvas, page, MARGIN, image_y, PAGE_WIDTH, ROW_IMAGE_HEIGHT)
        paste_framed(canvas, crop, MARGIN + PAGE_WIDTH + GAP, image_y, CROP_WIDTH, ROW_IMAGE_HEIGHT)

        label_y = image_y + 8
        draw.text((MARGIN + 12, label_y), "Full rendered page", fill=TEXT_COLOR, font=label_font)
        draw.text((MARGIN + PAGE_WIDTH + GAP + 12, label_y), "Cropped evidence region", fill=TEXT_COLOR, font=label_font)

        y += row_height + ROW_GAP

    return canvas


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    sheet = build_contact_sheet()
    sheet.save(OUT_PATH)
    print(OUT_PATH)


if __name__ == "__main__":
    main()
