from __future__ import annotations

import math
import re
from typing import Iterable, List, Sequence, Tuple

from .types import BBox

TOKEN_RE = re.compile(r"[a-zA-Z0-9]+")


def tokenize(text: str) -> List[str]:
    return TOKEN_RE.findall(text.lower())


def bbox_intersection(a: BBox, b: BBox) -> float:
    left = max(a[0], b[0])
    top = max(a[1], b[1])
    right = min(a[2], b[2])
    bottom = min(a[3], b[3])
    width = max(0.0, right - left)
    height = max(0.0, bottom - top)
    return width * height


def bbox_area(box: BBox) -> float:
    return max(0.0, box[2] - box[0]) * max(0.0, box[3] - box[1])


def bbox_overlap_ratio(a: BBox, b: BBox) -> float:
    base = max(bbox_area(a), bbox_area(b), 1e-9)
    return bbox_intersection(a, b) / base


def bbox_contains(outer: BBox, inner: BBox, threshold: float = 0.6) -> bool:
    return bbox_overlap_ratio(outer, inner) >= threshold


def choose_best_bbox(target: BBox, candidates: Iterable[BBox]) -> Tuple[int, float]:
    best_index = -1
    best_score = 0.0
    for index, bbox in enumerate(candidates):
        score = bbox_overlap_ratio(target, bbox)
        if score > best_score:
            best_index = index
            best_score = score
    return best_index, best_score


def first_non_empty_line(text: str) -> str:
    for line in text.splitlines():
        clean = line.strip()
        if clean:
            return clean
    return ""


def is_close(a: float, b: float, tolerance: float = 1e-6) -> bool:
    return math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance)
