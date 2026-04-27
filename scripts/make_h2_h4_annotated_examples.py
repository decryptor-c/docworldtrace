#!/usr/bin/env python3
from __future__ import annotations

import textwrap
from pathlib import Path
from typing import Iterable, Sequence

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data/reports/h2_h4_annotated_examples"
OUT_FILE = OUT_DIR / "h2_h4_annotated_examples.png"
SINGLE_EXAMPLES = [
    {
        "filename": "example_01_h2_cross_page.png",
        "title": "H2 Cross-page",
        "page_path": ROOT / "artifacts/docenv/2308.06595v4/page_002.png",
        "rects": [((110, 128, 1120, 265), "#2563eb", "Groundtruth: 1 Introduction")],
        "notes": [
            "问题：先 search 定位包含 “visit bench a benchmark for vision” 的页面，再阅读下一页。",
            "标准路径：search -> read_page -> answer。H2 重点验证 teacher 不是直接回答，而是先定位页面再读取证据。",
            "H3 正例结论：SUPPORTED / SUFFICIENT / keep，因为 read_page observation 可支撑最终答案。",
        ],
    },
    {
        "filename": "example_02_h2_numeric.png",
        "title": "H2 Numeric",
        "page_path": ROOT / "artifacts/docenv/ti2025ars/page_029.png",
        "rects": [((102, 760, 1172, 1030), "#d97706", "Table evidence + compute")],
        "notes": [
            "问题：根据第 29 页表格，计算 2024 到 2025 的 free cash flow margin 增加量。",
            "标准路径：parse_table -> compute -> answer；可接受路径也包括 read_page/crop 后再 compute。",
            "Groundtruth：7.0 percentage points。H3 检查最终数值和 compute/evidence 是否同时成立。",
        ],
    },
    {
        "filename": "example_03_h3_verification.png",
        "title": "H3 Verification",
        "page_path": ROOT / "artifacts/docenv/tm2529296d2_ars/page_081.png",
        "rects": [((90, 180, 1145, 660), "#16a34a", "Evidence for SUPPORTED")],
        "notes": [
            "问题：判断声明 “frozen executive death benefit plan ...” 是否被文档支持。",
            "标准路径：read_page/search -> verify -> answer。H3 不重新解题，而是检查 verify observation 与最终 SUPPORTED 是否一致。",
            "坏路径测试：如果把最终答案改成 UNSUPPORTED，DocVerify++ 应判 verification_label_mismatch / reject。",
        ],
    },
    {
        "filename": "example_04_h4_table_path.png",
        "title": "H4 Table Path",
        "page_path": ROOT / "artifacts/docenv/tm2529296d2_ars/page_002.png",
        "rects": [((72, 640, 1160, 1035), "#7c3aed", "Table lookup: Revenue / High-Touch Solutions N.A.")],
        "notes": [
            "问题：第 2 页表格中 Revenue 在 High-Touch Solutions N.A. 列下的值是什么？",
            "标准路径：read_page -> parse_table -> answer；Groundtruth：$14.0B。",
            "H4 作用：证明保留下来的轨迹覆盖 table_lookup、numeric_computation、verification、refuse、cross_page 等不同路径，而不是单一模板。",
        ],
    },
]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if path and Path(path).exists():
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


FONT_TITLE = load_font(44, bold=True)
FONT_SECTION = load_font(30, bold=True)
FONT_BODY = load_font(23)
FONT_SMALL = load_font(20)
FONT_MONO = load_font(21)


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.ImageFont,
    fill: str,
    width: int,
    line_gap: int = 7,
) -> int:
    x, y = xy
    avg_char = max(1, text_size(draw, "中", font)[0])
    max_chars = max(8, width // avg_char)
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        lines.extend(textwrap.wrap(paragraph, width=max_chars, break_long_words=False, replace_whitespace=False))
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += text_size(draw, line or " ", font)[1] + line_gap
    return y


def rounded_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str,
    outline: str = "#d8dee8",
    width: int = 2,
    radius: int = 18,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def resize_page(path: Path, width: int) -> Image.Image:
    image = Image.open(path).convert("RGB")
    height = int(image.height * width / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def draw_scaled_rect(
    draw: ImageDraw.ImageDraw,
    origin: tuple[int, int],
    original_size: tuple[int, int],
    scaled_size: tuple[int, int],
    rect: tuple[int, int, int, int],
    color: str,
    label: str,
) -> None:
    ox, oy = origin
    sx = scaled_size[0] / original_size[0]
    sy = scaled_size[1] / original_size[1]
    x1, y1, x2, y2 = rect
    scaled = (
        int(ox + x1 * sx),
        int(oy + y1 * sy),
        int(ox + x2 * sx),
        int(oy + y2 * sy),
    )
    draw.rectangle(scaled, outline=color, width=6)
    label_w, label_h = text_size(draw, label, FONT_SMALL)
    label_box = (scaled[0], max(oy, scaled[1] - label_h - 16), scaled[0] + label_w + 18, max(oy + label_h + 10, scaled[1] - 2))
    draw.rounded_rectangle(label_box, radius=8, fill=color)
    draw.text((label_box[0] + 9, label_box[1] + 5), label, font=FONT_SMALL, fill="white")


def draw_pipeline(draw: ImageDraw.ImageDraw, x: int, y: int, steps: Sequence[str], color: str) -> int:
    current_x = x
    for idx, step in enumerate(steps):
        w = max(120, text_size(draw, step, FONT_MONO)[0] + 34)
        h = 44
        draw.rounded_rectangle((current_x, y, current_x + w, y + h), radius=14, fill="#ffffff", outline=color, width=3)
        draw.text((current_x + 17, y + 10), step, font=FONT_MONO, fill="#1f2937")
        current_x += w
        if idx != len(steps) - 1:
            draw.line((current_x + 10, y + h // 2, current_x + 50, y + h // 2), fill=color, width=4)
            draw.polygon(
                [(current_x + 50, y + h // 2), (current_x + 39, y + h // 2 - 7), (current_x + 39, y + h // 2 + 7)],
                fill=color,
            )
            current_x += 62
    return y + 60


def paste_page_card(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    title: str,
    page_path: Path,
    rects: Iterable[tuple[tuple[int, int, int, int], str, str]],
    notes: Sequence[str],
    width: int = 450,
) -> int:
    original = Image.open(page_path).convert("RGB")
    page = resize_page(page_path, width)
    card_h = page.height + 104
    rounded_box(draw, (x, y, x + width + 28, y + card_h), fill="#f8fafc")
    draw.text((x + 18, y + 16), title, font=FONT_SECTION, fill="#0f172a")
    page_x, page_y = x + 14, y + 74
    canvas.paste(page, (page_x, page_y))
    draw.rectangle((page_x, page_y, page_x + page.width, page_y + page.height), outline="#cbd5e1", width=2)
    for rect, color, label in rects:
        draw_scaled_rect(draw, (page_x, page_y), original.size, page.size, rect, color, label)
    note_y = y + 74
    note_x = x + width + 60
    for note in notes:
        rounded_box(draw, (note_x, note_y, note_x + 1110, note_y + 126), fill="#ffffff")
        note_y = draw_wrapped(draw, (note_x + 22, note_y + 18), note, FONT_BODY, "#111827", 1060) + 18
    return max(y + card_h, note_y)


def make_image() -> None:
    required = [item["page_path"] for item in SINGLE_EXAMPLES]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing required images:\n" + "\n".join(missing))

    canvas = Image.new("RGB", (1700, 3050), "#eef2f7")
    draw = ImageDraw.Draw(canvas)

    draw.text((56, 42), "H2-H4 示例路径可视化标注", font=FONT_TITLE, fill="#0f172a")
    draw_wrapped(
        draw,
        (58, 104),
        "左侧为文档页面证据，彩色框标出答案或证据区域；右侧标出 H2 生成路径、H3 验证结论、H4 覆盖的能力类型。",
        FONT_BODY,
        "#334155",
        1550,
    )

    y = 172
    for example in SINGLE_EXAMPLES:
        y = paste_page_card(
            canvas,
            draw,
            56,
            y,
            example["title"],
            example["page_path"],
            example["rects"],
            example["notes"],
        ) + 34

    rounded_box(draw, (56, y, 1644, y + 322), fill="#0f172a", outline="#0f172a")
    draw.text((88, y + 30), "H4 多样性覆盖摘要", font=FONT_SECTION, fill="white")
    pipeline_y = y + 94
    pipeline_y = draw_pipeline(draw, 92, pipeline_y, ["search", "read_page", "answer"], "#60a5fa")
    pipeline_y = draw_pipeline(draw, 92, pipeline_y, ["parse_table", "compute", "answer"], "#fbbf24")
    pipeline_y = draw_pipeline(draw, 92, pipeline_y, ["read_page", "verify", "answer"], "#4ade80")
    draw_wrapped(
        draw,
        (920, y + 92),
        "H4 不评判单条答案，而是统计所有 keep 轨迹是否覆盖多种任务和工具路径：6 类任务、7 个核心动作、10 类工具序列。",
        FONT_BODY,
        "#e2e8f0",
        660,
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    canvas.crop((0, 0, 1700, y + 372)).save(OUT_FILE)
    print(f"Wrote {OUT_FILE}")


def make_single_images() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for example in SINGLE_EXAMPLES:
        canvas = Image.new("RGB", (1700, 820), "#eef2f7")
        draw = ImageDraw.Draw(canvas)
        draw.text((56, 42), example["title"], font=FONT_TITLE, fill="#0f172a")
        draw_wrapped(
            draw,
            (58, 104),
            "文档页面证据 + 工具路径标注。可单独插入报告或 PPT。",
            FONT_BODY,
            "#334155",
            1550,
        )
        bottom = paste_page_card(
            canvas,
            draw,
            56,
            172,
            example["title"],
            example["page_path"],
            example["rects"],
            example["notes"],
        )
        out_path = OUT_DIR / example["filename"]
        canvas.crop((0, 0, 1700, bottom + 46)).save(out_path)
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    make_image()
    make_single_images()
