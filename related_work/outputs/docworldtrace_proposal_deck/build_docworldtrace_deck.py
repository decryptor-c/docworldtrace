#!/usr/bin/env python3
"""
Builds the DocWorldTrace proposal deck as editable PPTX OOXML.

The local PowerPoint artifact runtime is unavailable in this environment, so this
builder writes the PPTX package directly with editable text, shapes, and images.
It also renders PNG previews from the same layout data for visual checks.
"""

from __future__ import annotations

import html
import os
import posixpath
import shutil
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
PREVIEWS = ROOT / "tmp" / "slides" / "previews"
OUT = ROOT / "DocWorldTrace_Proposal_Briefing.pptx"
VERIFY = ROOT / "verification_report.md"

W, H = 1280, 720
EMU = 9525
SLIDE_CX, SLIDE_CY = W * EMU, H * EMU

P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
PKG_REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CP_NS = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DC_NS = "http://purl.org/dc/elements/1.1/"
DCTERMS_NS = "http://purl.org/dc/terms/"
DCTYPE_NS = "http://purl.org/dc/dcmitype/"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"

FONT_CN = "PingFang SC"
FONT_BODY = "PingFang SC"
FONT_LATIN = "Aptos"

COLORS = {
    "paper": "F7F5EF",
    "paper2": "FFFDF8",
    "ink": "1D252C",
    "muted": "5F6B74",
    "line": "C9D1D6",
    "teal": "0E8F84",
    "teal_dark": "096B63",
    "teal_light": "DCEFEB",
    "amber": "D98D2B",
    "amber_light": "F6E5CB",
    "slate": "304252",
    "slate_light": "E7ECEF",
    "rose": "B85450",
    "green": "4C9A64",
    "white": "FFFFFF",
}


@dataclass
class Element:
    kind: str
    x: float
    y: float
    w: float
    h: float
    text: str = ""
    fill: Optional[str] = None
    line: Optional[str] = None
    color: str = COLORS["ink"]
    size: int = 24
    bold: bool = False
    align: str = "left"
    valign: str = "top"
    radius: int = 0
    alpha: int = 100000
    image: Optional[str] = None
    name: str = ""
    arrow: bool = False
    line_width: float = 1.5


@dataclass
class Slide:
    title: str
    message: str
    notes: str
    elements: List[Element] = field(default_factory=list)


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def emu(value: float) -> int:
    return int(round(value * EMU))


def rgb(value: str) -> str:
    return value.replace("#", "").upper()


def alpha_xml(alpha: int) -> str:
    if alpha >= 100000:
        return ""
    return f'<a:alpha val="{alpha}"/>'


def solid_fill(color: Optional[str], alpha: int = 100000) -> str:
    if not color:
        return "<a:noFill/>"
    return f'<a:solidFill><a:srgbClr val="{rgb(color)}">{alpha_xml(alpha)}</a:srgbClr></a:solidFill>'


def line_xml(color: Optional[str], width: float = 1.2, arrow: bool = False) -> str:
    if not color:
        return "<a:ln><a:noFill/></a:ln>"
    head = '<a:headEnd type="triangle"/>' if arrow else ""
    return (
        f'<a:ln w="{int(width * 12700)}">'
        f'<a:solidFill><a:srgbClr val="{rgb(color)}"/></a:solidFill>{head}</a:ln>'
    )


def xfrm_xml(x: float, y: float, w: float, h: float) -> str:
    return (
        f"<a:xfrm><a:off x=\"{emu(x)}\" y=\"{emu(y)}\"/>"
        f"<a:ext cx=\"{emu(w)}\" cy=\"{emu(h)}\"/></a:xfrm>"
    )


def body_pr(valign: str = "top") -> str:
    anchor = {"top": "t", "middle": "ctr", "bottom": "b"}.get(valign, "t")
    return f'<a:bodyPr wrap="square" rtlCol="0" anchor="{anchor}"><a:spAutoFit/></a:bodyPr><a:lstStyle/>'


def paragraphs_xml(text: str, size: int, color: str, bold: bool, align: str) -> str:
    lines = text.split("\n") if text else [""]
    out = []
    for line in lines:
        ppr = f'<a:pPr algn="{align}"/>'
        bold_attr = 'b="1"' if bold else ""
        rpr = (
            f'<a:rPr lang="zh-CN" sz="{max(800, int(size * 75))}" '
            f'{bold_attr}>'
            f'<a:solidFill><a:srgbClr val="{rgb(color)}"/></a:solidFill>'
            f'<a:latin typeface="{FONT_LATIN}"/><a:ea typeface="{FONT_CN}"/><a:cs typeface="{FONT_CN}"/>'
            f"</a:rPr>"
        )
        out.append(f"<a:p>{ppr}<a:r>{rpr}<a:t>{esc(line)}</a:t></a:r><a:endParaRPr/></a:p>")
    return "".join(out)


def shape_xml(el: Element, shape_id: int) -> str:
    geom = "roundRect" if el.radius else "rect"
    text_body = ""
    if el.text:
        text_body = (
            f"<p:txBody>{body_pr(el.valign)}"
            f"{paragraphs_xml(el.text, el.size, el.color, el.bold, el.align)}</p:txBody>"
        )
    return (
        f"<p:sp><p:nvSpPr><p:cNvPr id=\"{shape_id}\" name=\"{esc(el.name or 'Shape')}\"/>"
        f"<p:cNvSpPr txBox=\"1\"/><p:nvPr/></p:nvSpPr>"
        f"<p:spPr>{xfrm_xml(el.x, el.y, el.w, el.h)}"
        f"<a:prstGeom prst=\"{geom}\"><a:avLst/></a:prstGeom>"
        f"{solid_fill(el.fill, el.alpha)}{line_xml(el.line, el.line_width)}</p:spPr>{text_body}</p:sp>"
    )


def connector_xml(el: Element, shape_id: int) -> str:
    return (
        f"<p:cxnSp><p:nvCxnSpPr><p:cNvPr id=\"{shape_id}\" name=\"{esc(el.name or 'Connector')}\"/>"
        f"<p:cNvCxnSpPr/><p:nvPr/></p:nvCxnSpPr>"
        f"<p:spPr>{xfrm_xml(el.x, el.y, el.w, el.h)}"
        f'<a:prstGeom prst="straightConnector1"><a:avLst/></a:prstGeom>'
        f"{line_xml(el.line or COLORS['line'], el.line_width, el.arrow)}</p:spPr></p:cxnSp>"
    )


def picture_xml(el: Element, shape_id: int, rid: str) -> str:
    return (
        f"<p:pic><p:nvPicPr><p:cNvPr id=\"{shape_id}\" name=\"{esc(el.name or 'Image')}\"/>"
        f"<p:cNvPicPr><a:picLocks noChangeAspect=\"1\"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>"
        f"<p:blipFill><a:blip r:embed=\"{rid}\"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>"
        f"<p:spPr>{xfrm_xml(el.x, el.y, el.w, el.h)}"
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'
    )


def add_title(slide: Slide, title: str, kicker: str = "") -> None:
    if kicker:
        slide.elements.append(Element("text", 58, 38, 800, 30, kicker, color=COLORS["teal_dark"], size=18, bold=True))
    slide.elements.append(Element("text", 58, 66, 1000, 56, title, color=COLORS["ink"], size=32, bold=True))
    slide.elements.append(Element("rect", 58, 126, 96, 4, fill=COLORS["teal"], line=None, radius=0))


def add_footer(slide: Slide, n: int) -> None:
    slide.elements.append(Element("text", 1098, 676, 130, 22, f"DocWorldTrace · {n:02d}", color=COLORS["muted"], size=12, align="right"))


def card(slide: Slide, x: float, y: float, w: float, h: float, title: str, body: str, fill: str = "white", accent: str = "teal") -> None:
    slide.elements.append(Element("rect", x, y, w, h, fill=COLORS[fill], line=COLORS["line"], radius=10, alpha=96500))
    slide.elements.append(Element("rect", x, y, 6, h, fill=COLORS[accent], line=None, radius=0))
    slide.elements.append(Element("text", x + 18, y + 16, w - 32, 26, title, color=COLORS["ink"], size=18, bold=True))
    slide.elements.append(Element("text", x + 18, y + 48, w - 34, h - 58, body, color=COLORS["muted"], size=14))


def pill(slide: Slide, x: float, y: float, w: float, h: float, text: str, fill: str, color: str = "ink", size: int = 14) -> None:
    slide.elements.append(Element("rect", x, y, w, h, fill=COLORS[fill], line=COLORS["line"], radius=14))
    slide.elements.append(Element("text", x + 8, y + 6, w - 16, h - 10, text, color=COLORS[color], size=size, align="center", valign="middle", bold=True))


def background(slide: Slide, color: str = "paper") -> None:
    slide.elements.insert(0, Element("rect", 0, 0, W, H, fill=COLORS[color], line=None, name="Background"))


def make_slides() -> List[Slide]:
    slides: List[Slide] = []

    s = Slide(
        "DocWorldTrace",
        "验证引导的文档 Agent 工具轨迹合成",
        "定位不是另一个文档 QA Agent，而是数据与环境基础设施。抓手是把 PDF 变成交互环境，再用验证信号约束轨迹质量。",
    )
    s.elements.append(Element("image", 0, 0, W, H, image="title_environment_trace.png", name="Text-free title visual"))
    s.elements.append(Element("rect", 40, 58, 565, 512, fill=COLORS["white"], line=None, radius=18, alpha=90000))
    s.elements.append(Element("text", 72, 92, 480, 70, "DocWorldTrace", color=COLORS["ink"], size=46, bold=True))
    s.elements.append(Element("rect", 74, 170, 128, 6, fill=COLORS["teal"], line=None))
    s.elements.append(Element("text", 74, 202, 455, 96, "验证引导的文档 Agent\n工具轨迹合成", color=COLORS["slate"], size=30, bold=True))
    s.elements.append(Element("text", 76, 328, 470, 82, "将 PDF 文档建模为可交互环境，通过标准化工具轨迹与 DocVerify++ 过程验证，合成可复现、可审计的高质量训练数据。", color=COLORS["muted"], size=18))
    pill(s, 74, 444, 118, 34, "DocEnv-lite", "teal_light", "teal_dark", 13)
    pill(s, 204, 444, 126, 34, "DocVerify++", "amber_light", "amber", 13)
    pill(s, 342, 444, 152, 34, "Trajectory Data", "slate_light", "slate", 13)
    s.elements.append(Element("text", 74, 628, 450, 24, "Proposal briefing · 中文 12 页", color=COLORS["muted"], size=13))
    add_footer(s, 1)
    slides.append(s)

    s = Slide(
        "研究动机",
        "文档推理正在从 answer-only 转向多步 Agent 交互",
        "传统数据只给问题和答案；新系统已经需要主动检索、视觉定位、证据积累、工具组合和拒答判断。",
    )
    background(s)
    add_title(s, "文档推理正在从 answer-only 转向多步 Agent 交互", "1 · 背景与动机")
    s.elements.append(Element("rect", 80, 190, 440, 360, fill=COLORS["white"], line=COLORS["line"], radius=12))
    s.elements.append(Element("text", 112, 220, 370, 38, "Answer-only QA", color=COLORS["ink"], size=24, bold=True, align="center"))
    pill(s, 150, 298, 300, 46, "Question", "slate_light", "slate", 18)
    s.elements.append(Element("line", 298, 354, 2, 58, line=COLORS["line"], line_width=2.2, arrow=True))
    pill(s, 150, 430, 300, 46, "Final Answer", "amber_light", "amber", 18)
    s.elements.append(Element("text", 114, 506, 365, 36, "缺少工具调用、证据路径、充分性与拒答示范", color=COLORS["rose"], size=16, align="center", bold=True))
    s.elements.append(Element("rect", 610, 190, 585, 360, fill=COLORS["white"], line=COLORS["line"], radius=12))
    s.elements.append(Element("text", 640, 220, 525, 38, "Document Agent Interaction", color=COLORS["ink"], size=24, bold=True, align="center"))
    for i, label in enumerate(["search", "read_page", "crop", "compute"]):
        pill(s, 652 + i * 123, 296, 108, 44, label, "teal_light", "teal_dark", 13)
        if i < 3:
            s.elements.append(Element("line", 762 + i * 123, 318, 28, 1, line=COLORS["teal"], line_width=2, arrow=True))
    pill(s, 720, 398, 250, 46, "evidence_memory", "slate_light", "slate", 16)
    s.elements.append(Element("line", 842, 352, 1, 38, line=COLORS["line"], line_width=2, arrow=True))
    pill(s, 700, 485, 135, 44, "answer", "amber_light", "amber", 15)
    pill(s, 858, 485, 135, 44, "refuse", "amber_light", "amber", 15)
    s.elements.append(Element("line", 842, 450, -76, 28, line=COLORS["line"], line_width=2, arrow=True))
    s.elements.append(Element("line", 865, 450, 78, 28, line=COLORS["line"], line_width=2, arrow=True))
    s.elements.append(Element("text", 720, 580, 390, 40, "训练对象从“最终答案”升级为“可执行过程”", color=COLORS["teal_dark"], size=20, bold=True, align="center"))
    add_footer(s, 2)
    slides.append(s)

    s = Slide(
        "开源 RL 蒸馏悖论",
        "主要文档 Agent 系统不公开轨迹、依赖闭源 teacher，复现成本和公平对比都受限。",
        "重点不是闭源 teacher 本身，而是轨迹不公开和环境不可复现。",
    )
    background(s)
    add_title(s, "开源模型的 agentic 能力，冷启动仍依赖闭源 teacher", "2 · 问题定位")
    s.elements.append(Element("text", 72, 150, 640, 36, "5/6 主要文档 Agent 系统完全不可复现", color=COLORS["rose"], size=24, bold=True))
    x0, y0 = 74, 205
    cols = [190, 265, 150, 160, 150]
    headers = ["系统", "RL / 方法", "轨迹公开", "Teacher", "环境复现"]
    rows = [
        ["VISOR", "GRPO + visual action eval", "No", "GPT-4o", "No"],
        ["MM-Doc-R1", "SPO", "No", "Gemini", "No"],
        ["DocSeeker", "evidence-aware GRPO", "No", "GPT-4o", "No"],
        ["DocCogito", "闭源 VLM 蒸馏", "No", "闭源 VLM", "No"],
        ["MDocAgent", "多 Agent 框架", "No", "GPT-4V", "No"],
        ["DocLens", "Training-free", "-", "-", "Partial"],
    ]
    hrow = 48
    x = x0
    for w, head in zip(cols, headers):
        s.elements.append(Element("rect", x, y0, w, hrow, fill=COLORS["slate"], line=COLORS["white"]))
        s.elements.append(Element("text", x + 8, y0 + 13, w - 16, 22, head, color=COLORS["white"], size=13, bold=True, align="center"))
        x += w
    for r, row in enumerate(rows):
        y = y0 + hrow + r * 46
        x = x0
        for c, (w, val) in enumerate(zip(cols, row)):
            fill = COLORS["white"] if r % 2 == 0 else COLORS["slate_light"]
            s.elements.append(Element("rect", x, y, w, 46, fill=fill, line=COLORS["white"]))
            color = COLORS["rose"] if val == "No" else COLORS["ink"]
            s.elements.append(Element("text", x + 8, y + 13, w - 16, 20, val, color=color, size=12, bold=(c == 0 or val == "No"), align="center", valign="middle"))
            x += w
    card(s, 900, 218, 260, 232, "核心代价", "每个新系统需要重新蒸馏闭源 teacher 轨迹。\n\n估计 $0.10-0.30 / 条 × 数千条，且无法在同一轨迹集上公平对比。", "white", "rose")
    card(s, 900, 476, 260, 110, "DocWorldTrace 切入点", "公开轨迹 + 标准环境 + 过程验证", "teal_light", "teal")
    add_footer(s, 3)
    slides.append(s)

    s = Slide(
        "五个核心缺口",
        "Answer-only 数据无法训练文档 Agent 的关键能力。",
        "五个缺口分别对应轨迹数据、可复现环境、过程奖励、忠实性控制和拒答充分性。",
    )
    background(s)
    add_title(s, "Answer-only 数据无法训练文档 Agent 的关键能力", "3 · 五个缺口")
    gaps = [
        ("Gap 1", "轨迹数据缺失", "无中间推理步骤和工具调用序列"),
        ("Gap 2", "环境不可复现", "各系统自建环境，接口不互操作"),
        ("Gap 3", "过程级 reward 缺失", "只评最终答案，不评每步证据收益"),
        ("Gap 4", "Faithfulness Gap", "答案正确但推理未被文档证据支持"),
        ("Gap 5", "拒答与充分性缺失", "不可回答 / 证据不足场景缺少示范"),
    ]
    for i, (g, title, body) in enumerate(gaps):
        x = 58 + i * 240
        s.elements.append(Element("rect", x, 186, 208, 330, fill=COLORS["white"], line=COLORS["line"], radius=12))
        s.elements.append(Element("rect", x, 186, 208, 10, fill=COLORS["teal" if i < 3 else "amber"], line=None))
        s.elements.append(Element("text", x + 18, 220, 172, 24, g, color=COLORS["teal_dark"], size=15, bold=True, align="center"))
        s.elements.append(Element("text", x + 18, 262, 172, 58, title, color=COLORS["ink"], size=20, bold=True, align="center"))
        s.elements.append(Element("text", x + 20, 350, 168, 96, body, color=COLORS["muted"], size=15, align="center"))
    s.elements.append(Element("text", 178, 578, 925, 42, "结论：需要训练的不是“答案字符串”，而是可执行、可验证、可追溯的工具轨迹。", color=COLORS["slate"], size=24, bold=True, align="center"))
    add_footer(s, 4)
    slides.append(s)

    s = Slide(
        "核心 Thesis",
        "文档即环境 + 验证引导合成。",
        "环境化让轨迹真实可执行，DocVerify++ 让轨迹质量可审计，最终产出更适合训练文档 Agent 的数据。",
    )
    background(s)
    add_title(s, "文档即环境 + 验证引导合成", "4 · 核心思路")
    s.elements.append(Element("rect", 394, 218, 492, 164, fill=COLORS["white"], line=COLORS["teal"], radius=16))
    s.elements.append(Element("text", 428, 250, 425, 82, "把文档任务重构为\n可交互环境", color=COLORS["ink"], size=28, bold=True, align="center", valign="middle"))
    s.elements.append(Element("text", 430, 338, 420, 26, "+ DocVerify++ 过程级验证信号", color=COLORS["teal_dark"], size=18, bold=True, align="center"))
    threads = [
        ("GUI Agent 方法论", "环境 → 轨迹 → 质控\nWebArena / AgentTrek"),
        ("文档工具动作空间", "search / crop / parse / compute\nVISOR / DocSeeker"),
        ("claim-evidence 验证", "support / sufficiency\nfailure taxonomy"),
    ]
    for i, (t, b) in enumerate(threads):
        y = 180 + i * 122
        card(s, 76, y, 260, 88, t, b, "white", "teal" if i != 2 else "amber")
        s.elements.append(Element("line", 338, y + 44, 54, 70 - i * 10, line=COLORS["line"], line_width=2, arrow=True))
    card(s, 944, 228, 250, 146, "统一产出", "DocWorldTrace\n可复现、可审计、经验证的文档 Agent 工具轨迹数据集", "teal_light", "teal")
    s.elements.append(Element("line", 888, 300, 52, 0, line=COLORS["teal"], line_width=2.2, arrow=True))
    s.elements.append(Element("text", 224, 555, 832, 56, "静态 PDF 的结构化特性，使工具输出可缓存、证据可追溯、质量可交叉验证。", color=COLORS["slate"], size=24, bold=True, align="center"))
    add_footer(s, 5)
    slides.append(s)

    s = Slide(
        "DocEnv-lite",
        "10 个标准化工具 + evidence memory 构成可审计的 PDF 交互环境。",
        "工具 observation 来自环境真实执行，每条 evidence 记录 page、bbox、element_type 和 source_action。",
    )
    s.elements.append(Element("image", 0, 0, W, H, image="docenv_workbench.png", name="DocEnv visual"))
    s.elements.append(Element("rect", 0, 0, W, H, fill=COLORS["paper2"], line=None, alpha=72000))
    add_title(s, "DocEnv-lite: 面向 PDF 的轻量交互环境", "5 · 模块一")
    s.elements.append(Element("rect", 65, 170, 520, 368, fill=COLORS["white"], line=COLORS["line"], radius=14, alpha=95500))
    s.elements.append(Element("text", 92, 198, 210, 30, "核心 Action", color=COLORS["teal_dark"], size=22, bold=True))
    for i, label in enumerate(["search(query)", "read_page(page_ids)", "crop(page_id, bbox)", "answer(text, refs)", "refuse(reason)"]):
        pill(s, 94, 248 + i * 52, 430, 36, label, "teal_light", "teal_dark", 14)
    s.elements.append(Element("rect", 650, 170, 510, 368, fill=COLORS["white"], line=COLORS["line"], radius=14, alpha=95500))
    s.elements.append(Element("text", 678, 198, 210, 30, "扩展 Action", color=COLORS["amber"], size=22, bold=True))
    for i, label in enumerate(["overview()", "ocr(page_id, bbox)", "parse_table(page_id, bbox)", "compute(expr, vars)", "verify(claim, refs)"]):
        pill(s, 680, 248 + i * 52, 410, 36, label, "amber_light", "amber", 14)
    s.elements.append(Element("rect", 162, 574, 956, 62, fill=COLORS["slate"], line=None, radius=14, alpha=94000))
    s.elements.append(Element("text", 190, 590, 900, 30, "evidence_memory: page + bbox + content + element_type + source_action + confidence", color=COLORS["white"], size=18, bold=True, align="center"))
    add_footer(s, 6)
    slides.append(s)

    s = Slide(
        "多源轨迹采样",
        "从种子任务到候选轨迹，多源采样同时提供正例、多样路径和可控负例。",
        "数据生成不只靠 teacher；模板提供稳定性，负例为 DPO/PRM 提供训练信号，MCTS 做小规模消融。",
    )
    s.elements.append(Element("image", 0, 0, W, H, image="trajectory_synthesis.png", name="Trajectory synthesis visual"))
    s.elements.append(Element("rect", 0, 0, W, H, fill=COLORS["paper2"], line=None, alpha=76000))
    add_title(s, "多源轨迹采样: 从种子任务到候选轨迹", "6 · 模块二")
    pill(s, 72, 214, 180, 48, "Seed Tasks", "slate_light", "slate", 17)
    lanes = [
        ("Rule-based 模板", "search → read → answer", "teal_light", "teal_dark"),
        ("Teacher Rollout", "ReAct +真实 Observation", "amber_light", "amber"),
        ("Hard Negative", "7 类可控扰动", "slate_light", "slate"),
        ("MCTS 消融", "50-100 样本验证", "teal_light", "teal_dark"),
    ]
    for i, (t, b, fill, col) in enumerate(lanes):
        y = 170 + i * 92
        card(s, 330, y, 250, 70, t, b, fill, "teal" if i in (0, 3) else "amber")
        s.elements.append(Element("line", 254, 237, 72, y - 206, line=COLORS["line"], line_width=1.8, arrow=True))
        s.elements.append(Element("line", 582, y + 35, 80, 0, line=COLORS["line"], line_width=1.8, arrow=True))
    pill(s, 684, 305, 185, 54, "2K-5K\n候选轨迹", "white", "ink", 16)
    s.elements.append(Element("line", 870, 332, 90, 0, line=COLORS["teal"], line_width=2.5, arrow=True))
    pill(s, 982, 305, 170, 54, "DocVerify++\n过滤分级", "teal_light", "teal_dark", 16)
    s.elements.append(Element("line", 1068, 364, 0, 70, line=COLORS["teal"], line_width=2.5, arrow=True))
    pill(s, 930, 450, 275, 62, "DocWorldTrace-1K/3K\nGold / Silver / Bronze / Negative", "amber_light", "amber", 15)
    s.elements.append(Element("text", 78, 560, 760, 42, "任务分布: Text 25% · Table 20% · Numeric 20% · Cross-page 15% · Verification 10% · Unanswerable 10%", color=COLORS["slate"], size=18, bold=True))
    add_footer(s, 7)
    slides.append(s)

    s = Slide(
        "数据样例",
        "一条样例记录同时包含 question、document evidence、tool reasoning trajectory、answer 和 quality signals。",
        "这页用 pilot seed ti2025ars__numeric_free_cash_flow_margin_change_p29 展示数据长什么样。重点是 answer-only 只保留最后答案，而 DocWorldTrace 保留可执行工具过程、证据引用和验证信号。",
    )
    s.elements.append(Element("image", 0, 0, W, H, image="dataset_example_visual.png", name="Dataset example visual"))
    s.elements.append(Element("rect", 0, 0, W, H, fill=COLORS["paper2"], line=None, alpha=81000))
    add_title(s, "数据样例: 从问题到可验证工具轨迹", "7 · Dataset record")
    card(s, 62, 154, 468, 108, "Question", "基于 page 29 表格，计算 2024→2025 的 non-GAAP FCF margin 增加量；只输出 percentage points。", "white", "teal")
    card(s, 62, 284, 468, 188, "Documents / Evidence", "doc_id: ti2025ars\npage: 29\nbbox: [48.96, 365.70, 561.96, 493.95]\nevidence_refs: table/crop region", "white", "amber")
    s.elements.append(Element("rect", 106, 416, 380, 44, fill=COLORS["amber_light"], line=COLORS["amber"], radius=8))
    s.elements.append(Element("text", 124, 429, 344, 18, "compute: value_2025 − value_2024", color=COLORS["amber"], size=14, bold=True, align="center"))
    s.elements.append(Element("rect", 62, 520, 468, 62, fill=COLORS["teal_light"], line=COLORS["teal"], radius=12))
    s.elements.append(Element("text", 86, 537, 420, 25, "Answer: 7.0 percentage points", color=COLORS["teal_dark"], size=21, bold=True, align="center"))

    traj = [
        ("1", "read_page", "载入 page 29，获得 OCR + 页面布局"),
        ("2", "parse_table", "抽取目标表格单元格与 bbox provenance"),
        ("3", "compute", "value_2025 − value_2024"),
        ("4", "answer", "7.0 percentage points + evidence_refs"),
    ]
    for i, (num, action, obs) in enumerate(traj):
        y = 166 + i * 98
        s.elements.append(Element("rect", 650, y, 462, 70, fill=COLORS["white"], line=COLORS["line"], radius=12, alpha=97000))
        s.elements.append(Element("rect", 668, y + 17, 36, 36, fill=COLORS["teal"], line=None, radius=18))
        s.elements.append(Element("text", 668, y + 25, 36, 18, num, color=COLORS["white"], size=14, bold=True, align="center", valign="middle"))
        s.elements.append(Element("text", 724, y + 13, 130, 22, action, color=COLORS["ink"], size=18, bold=True))
        s.elements.append(Element("text", 724, y + 40, 360, 20, obs, color=COLORS["muted"], size=13))
        if i < len(traj) - 1:
            s.elements.append(Element("line", 686, y + 72, 0, 24, line=COLORS["teal"], line_width=2, arrow=True))
    s.elements.append(Element("rect", 650, 574, 462, 58, fill=COLORS["slate"], line=None, radius=12, alpha=94000))
    s.elements.append(Element("text", 676, 588, 410, 24, "quality_signals: SUPPORTED · SUFFICIENT · keep", color=COLORS["white"], size=17, bold=True, align="center"))
    s.elements.append(Element("text", 64, 636, 1040, 24, "记录粒度: question + doc_id + actions + observations + evidence_update + answer + reward/quality signals", color=COLORS["slate"], size=15, bold=True))
    add_footer(s, 8)
    slides.append(s)

    s = Slide(
        "质量控制与 Reward",
        "DocVerify++ 把质量控制前移到轨迹合成过程。",
        "从 answer-level 评价升级为 evidence-driven process supervision。",
    )
    s.elements.append(Element("image", 0, 0, W, H, image="quality_control.png", name="Quality control visual"))
    s.elements.append(Element("rect", 0, 0, W, H, fill=COLORS["paper2"], line=None, alpha=79000))
    add_title(s, "DocVerify++ 把质量控制前移到轨迹合成过程", "8 · 模块三")
    layers = ["L1 格式检查", "L2 执行检查", "L3 答案检查", "L4 证据检查", "L5 过程检查"]
    for i, layer in enumerate(layers):
        w = 420 - i * 42
        x = 98 + i * 21
        y = 184 + i * 64
        s.elements.append(Element("rect", x, y, w, 46, fill=COLORS["white"], line=COLORS["line"], radius=8, alpha=96000))
        s.elements.append(Element("text", x + 16, y + 13, w - 32, 20, layer, color=COLORS["ink"], size=16, bold=True, align="center"))
    quals = [("Gold", "L1-L5 全通过\nSFT 主训练集"), ("Silver", "答案正确\n部分 grounding 缺失"), ("Bronze", "答案正确\n过程有瑕疵"), ("Negative", "答案错误或不当拒答\nDPO/PRM 负例")]
    for i, (t, b) in enumerate(quals):
        card(s, 600 + (i % 2) * 280, 188 + (i // 2) * 132, 240, 96, t, b, "white", "amber" if i < 2 else "teal")
    rewards = ["R_answer", "R_support", "R_ground", "R_suff", "R_eff", "R_refuse", "R_tool"]
    for i, rwd in enumerate(rewards):
        pill(s, 96 + i * 158, 572, 132, 34, rwd, "slate_light", "slate", 13)
    s.elements.append(Element("text", 614, 466, 446, 52, "质量从“语义猜测”升级为\nbbox / OCR / compute / claim-evidence 交叉验证", color=COLORS["teal_dark"], size=21, bold=True, align="center"))
    add_footer(s, 9)
    slides.append(s)

    s = Slide(
        "Gap-to-Solution",
        "环境使方法可行，验证使数据高质量，数据使训练可复现。",
        "每个 gap 都有明确机制对应，而不是泛泛说数据更好。",
    )
    background(s)
    add_title(s, "为什么这套方案能正面解决五个缺口", "9 · 机制回扣")
    matrix = [
        ("轨迹缺失", "DocWorldTrace-1K/3K 公开工具轨迹"),
        ("环境不可复现", "DocEnv-lite 标准化 PDF 工具接口"),
        ("过程 reward 缺失", "七维 reward + per-step quality signals"),
        ("Faithfulness Gap", "DocVerify++ support / sufficiency 过滤"),
        ("拒答缺失", "unanswerable 样本 + sufficiency reward"),
    ]
    x0, y0 = 84, 178
    s.elements.append(Element("rect", x0, y0, 420, 46, fill=COLORS["slate"], line=COLORS["white"]))
    s.elements.append(Element("rect", x0 + 420, y0, 660, 46, fill=COLORS["slate"], line=COLORS["white"]))
    s.elements.append(Element("text", x0 + 12, y0 + 13, 390, 20, "核心缺口", color=COLORS["white"], size=15, bold=True, align="center"))
    s.elements.append(Element("text", x0 + 432, y0 + 13, 630, 20, "DocWorldTrace 机制", color=COLORS["white"], size=15, bold=True, align="center"))
    for i, (gap, sol) in enumerate(matrix):
        y = y0 + 46 + i * 50
        fill = COLORS["white"] if i % 2 == 0 else COLORS["slate_light"]
        s.elements.append(Element("rect", x0, y, 420, 50, fill=fill, line=COLORS["white"]))
        s.elements.append(Element("rect", x0 + 420, y, 660, 50, fill=fill, line=COLORS["white"]))
        s.elements.append(Element("text", x0 + 20, y + 15, 380, 20, gap, color=COLORS["ink"], size=15, bold=True, align="center"))
        s.elements.append(Element("text", x0 + 440, y + 15, 620, 20, sol, color=COLORS["teal_dark"], size=15, bold=True, align="center"))
    chain_y = 540
    for i, txt in enumerate(["PDF 静态结构化", "工具输出可验证", "轨迹质量可过滤", "训练数据可复现"]):
        pill(s, 92 + i * 286, chain_y, 220, 50, txt, "teal_light" if i < 3 else "amber_light", "teal_dark" if i < 3 else "amber", 15)
        if i < 3:
            s.elements.append(Element("line", 314 + i * 286, chain_y + 25, 54, 0, line=COLORS["line"], line_width=2, arrow=True))
    add_footer(s, 10)
    slides.append(s)

    s = Slide(
        "Pilot H1-H4 证据",
        "5 篇 PDF、20 个 seed、80 条轨迹、144 条注入式负例上完成闭环验证。",
        "H1-H4 可以作为 proposal 可行性证据，但自然分布人工 GT 仍是 P0 补充实验。",
    )
    background(s)
    add_title(s, "Pilot 已完成 H1-H4 闭环验证", "10 · 初步证据")
    kpis = [
        ("H1", "DocEnv 可行性", "50/50", "工具调用成功\ncache 一致性 100%"),
        ("H2", "Teacher 轨迹", "80/80", "格式合规\nDirect answer 率 0%"),
        ("H3", "验证过滤", "144/144", "注入式负例 caught\nmissed-keep 0%"),
        ("H4", "多样性", "6/6", "任务覆盖\n8/10 action 覆盖"),
    ]
    for i, (h, t, num, body) in enumerate(kpis):
        x = 64 + i * 292
        s.elements.append(Element("rect", x, 182, 248, 176, fill=COLORS["white"], line=COLORS["line"], radius=12))
        s.elements.append(Element("text", x + 18, 204, 58, 28, h, color=COLORS["teal_dark"], size=22, bold=True))
        s.elements.append(Element("text", x + 82, 207, 140, 24, t, color=COLORS["muted"], size=14, bold=True))
        s.elements.append(Element("text", x + 18, 248, 210, 42, num, color=COLORS["ink"], size=36, bold=True, align="center"))
        s.elements.append(Element("text", x + 28, 306, 190, 34, body, color=COLORS["muted"], size=14, align="center"))
    s.elements.append(Element("rect", 76, 418, 544, 112, fill=COLORS["teal_light"], line=COLORS["teal"], radius=12))
    s.elements.append(Element("text", 104, 444, 500, 30, "Search query unique rate: 52.78%", color=COLORS["teal_dark"], size=24, bold=True, align="center"))
    s.elements.append(Element("text", 106, 486, 500, 24, "轨迹覆盖 10 类 unique 工具序列，核心动作 7/7", color=COLORS["slate"], size=16, align="center"))
    card(s, 690, 408, 430, 136, "残余风险", "文档池仍小；自然分布人工 GT confusion matrix 未做；平均步数处于设计下沿；verify 主要用于 verification 任务。", "white", "amber")
    s.elements.append(Element("text", 146, 594, 974, 38, "结论：H1-H4 可宣布通过；H5 mini-SFT 与自然分布验证是下一步关键。", color=COLORS["ink"], size=22, bold=True, align="center"))
    add_footer(s, 11)
    slides.append(s)

    s = Slide(
        "预期贡献与投稿定位",
        "五项贡献围绕环境、Schema、验证引导合成、公开数据集和训练评测展开。",
        "叙事重点是可复现性、忠实性和工具效率，而不是绝对 SOTA。",
    )
    background(s)
    add_title(s, "五项贡献: 环境、Schema、合成方法、数据集、训练评测", "11 · 产出与贡献")
    contribs = [
        ("C1 DocEnv-lite", "面向 PDF 的可交互、可审计、可缓存文档工具环境"),
        ("C2 Schema", "兼容 ReAct / ALR / VSC / ADP 的统一轨迹格式"),
        ("C3 Verification-guided Synthesis", "把 DocVerify++ 嵌入采样、过滤、分级全过程"),
        ("C4 DocWorldTrace-1K/3K", "40-60 篇 PDF、1K-3K 高质量轨迹、四级分级"),
        ("C5 Training & Evaluation", "answer-only / teacher ReAct / filtered traces 系统对比"),
    ]
    for i, (t, b) in enumerate(contribs):
        y = 164 + i * 76
        card(s, 84, y, 704, 58, t, b, "white", "teal" if i != 3 else "amber")
    card(s, 852, 188, 300, 118, "优先投稿方向", "ACL / EMNLP Resource Track\nNeurIPS Datasets and Benchmarks", "teal_light", "teal")
    card(s, 852, 348, 300, 142, "叙事策略", "环境使方法可行\n方法使数据高质量\n数据使训练可复现", "amber_light", "amber")
    s.elements.append(Element("text", 838, 560, 330, 42, "不强调绝对 SOTA；强调基础设施价值、可复现性和忠实性。", color=COLORS["slate"], size=18, bold=True, align="center"))
    add_footer(s, 12)
    slides.append(s)

    s = Slide(
        "下一步计划与风险",
        "12 周推进重点是补齐自然分布 GT、文档池多样性和 H5 mini-SFT。",
        "关键决策点要前置：工具执行率、MCTS 成本质量、DocVerify++ precision、SFT 行为收益。",
    )
    background(s)
    add_title(s, "12 周推进计划: 从 DocEnv-lite 到 Dataset v0.1", "12 · 下一步")
    timeline = [
        (1, 2, "DocEnv-lite\n7 个 MVP 工具"),
        (3, 4, "种子任务 +\n2K-5K 候选轨迹"),
        (5, 6, "五层质检 +\n人工审核"),
        (7, 8, "Dataset v0.1\n三种格式"),
        (9, 10, "Baselines\n4 组 SFT"),
        (11, 12, "论文撰写"),
    ]
    x_start, x_end = 88, 1110
    y = 220
    s.elements.append(Element("line", x_start, y, x_end - x_start, 0, line=COLORS["line"], line_width=3))
    for wk in range(1, 13):
        x = x_start + (wk - 1) * ((x_end - x_start) / 11)
        s.elements.append(Element("line", x, y - 8, 0, 16, line=COLORS["line"], line_width=1.2))
        s.elements.append(Element("text", x - 16, y + 18, 32, 18, str(wk), color=COLORS["muted"], size=11, align="center"))
    for i, (a, b, label) in enumerate(timeline):
        x = x_start + (a - 1) * ((x_end - x_start) / 11)
        w = (b - a + 1) * ((x_end - x_start) / 11) - 6
        yy = 270 + (i % 2) * 82
        s.elements.append(Element("rect", x, yy, w, 58, fill=COLORS["teal_light"] if i < 4 else COLORS["amber_light"], line=COLORS["line"], radius=10))
        s.elements.append(Element("text", x + 6, yy + 12, w - 12, 32, label, color=COLORS["teal_dark"] if i < 4 else COLORS["amber"], size=12, bold=True, align="center"))
        s.elements.append(Element("line", x + w / 2, yy, 0, y - yy, line=COLORS["line"], line_width=1.1))
    card(s, 90, 500, 330, 116, "P0 补充实验", "自然分布人工 GT 60-100 条\nreview vs reject 阈值校准\n真 SEC 10-K / 扫描件扩展", "white", "rose")
    card(s, 480, 500, 330, 116, "关键决策点", "Week 2: 工具执行率\nWeek 6: DocVerify++ precision\nWeek 8: SFT 是否显著提升", "white", "amber")
    card(s, 870, 500, 310, 116, "下一步判断", "若 H5 行为收益成立，加入 GRPO 实验；否则转向 Resource / Benchmark 叙事。", "teal_light", "teal")
    add_footer(s, 13)
    slides.append(s)

    return slides


def slide_xml(slide: Slide, idx: int) -> Tuple[str, Dict[str, str], List[str]]:
    rid_counter = 2
    image_rels: Dict[str, str] = {}
    image_files: List[str] = []
    shape_id = 2
    body = [
        '<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>',
        '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>',
    ]
    for el in slide.elements:
        if el.kind == "image":
            assert el.image
            media_name = f"slide{idx}_{Path(el.image).name}"
            rid = f"rId{rid_counter}"
            rid_counter += 1
            image_rels[rid] = f"../media/{media_name}"
            image_files.append(el.image)
            body.append(picture_xml(el, shape_id, rid))
        elif el.kind == "line":
            body.append(connector_xml(el, shape_id))
        else:
            body.append(shape_xml(el, shape_id))
        shape_id += 1
    xml = (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<p:sld xmlns:a="{A_NS}" xmlns:r="{R_NS}" xmlns:p="{P_NS}">'
        f"<p:cSld><p:spTree>{''.join(body)}</p:spTree></p:cSld>"
        f"<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>"
    )
    return xml, image_rels, image_files


def rels_xml(rels: Iterable[Tuple[str, str, str]]) -> str:
    parts = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="{PKG_REL_NS}">']
    for rid, typ, target in rels:
        parts.append(f'<Relationship Id="{rid}" Type="{typ}" Target="{target}"/>')
    parts.append("</Relationships>")
    return "".join(parts)


def content_types_xml(slide_count: int) -> str:
    overrides = [
        ('/ppt/presentation.xml', 'application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml'),
        ('/ppt/slideMasters/slideMaster1.xml', 'application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml'),
        ('/ppt/notesMasters/notesMaster1.xml', 'application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml'),
        ('/ppt/slideLayouts/slideLayout1.xml', 'application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml'),
        ('/ppt/theme/theme1.xml', 'application/vnd.openxmlformats-officedocument.theme+xml'),
        ('/ppt/presProps.xml', 'application/vnd.openxmlformats-officedocument.presentationml.presProps+xml'),
        ('/ppt/viewProps.xml', 'application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml'),
        ('/ppt/tableStyles.xml', 'application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml'),
        ('/docProps/core.xml', 'application/vnd.openxmlformats-package.core-properties+xml'),
        ('/docProps/app.xml', 'application/vnd.openxmlformats-officedocument.extended-properties+xml'),
    ]
    for i in range(1, slide_count + 1):
        overrides.append((f'/ppt/slides/slide{i}.xml', 'application/vnd.openxmlformats-officedocument.presentationml.slide+xml'))
        overrides.append((f'/ppt/notesSlides/notesSlide{i}.xml', 'application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml'))
    body = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">',
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>',
        '<Default Extension="xml" ContentType="application/xml"/>',
        '<Default Extension="png" ContentType="image/png"/>',
    ]
    body.extend([f'<Override PartName="{part}" ContentType="{ctype}"/>' for part, ctype in overrides])
    body.append("</Types>")
    return "".join(body)


def presentation_xml(slide_count: int) -> str:
    ids = "".join([f'<p:sldId id="{255 + i}" r:id="rId{i}"/>' for i in range(1, slide_count + 1)])
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<p:presentation xmlns:a="{A_NS}" xmlns:r="{R_NS}" xmlns:p="{P_NS}" saveSubsetFonts="1">'
        f'<p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rIdMaster"/></p:sldMasterIdLst>'
        f'<p:notesMasterIdLst><p:notesMasterId r:id="rIdNotesMaster"/></p:notesMasterIdLst>'
        f"<p:sldIdLst>{ids}</p:sldIdLst>"
        f'<p:sldSz cx="{SLIDE_CX}" cy="{SLIDE_CY}" type="wide"/>'
        f'<p:notesSz cx="6858000" cy="9144000"/>'
        f"</p:presentation>"
    )


def master_xml() -> str:
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<p:sldMaster xmlns:a="{A_NS}" xmlns:r="{R_NS}" xmlns:p="{P_NS}">'
        f'<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
        f'<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
        f"</p:spTree></p:cSld>"
        f'<p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>'
        f'<p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst>'
        f"</p:sldMaster>"
    )


def notes_master_xml() -> str:
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<p:notesMaster xmlns:a="{A_NS}" xmlns:r="{R_NS}" xmlns:p="{P_NS}">'
        f'<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
        f'<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
        f"</p:spTree></p:cSld>"
        f'<p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>'
        f"</p:notesMaster>"
    )


def layout_xml() -> str:
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<p:sldLayout xmlns:a="{A_NS}" xmlns:r="{R_NS}" xmlns:p="{P_NS}" type="blank" preserve="1">'
        f'<p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
        f'<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
        f"</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>"
    )


def notes_slide_xml(slide: Slide, idx: int) -> str:
    note_text = slide.notes
    body = [
        '<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>',
        '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>',
        f'<p:sp><p:nvSpPr><p:cNvPr id="2" name="Speaker Notes {idx}"/><p:cNvSpPr txBox="1"/><p:nvPr><p:ph type="body" idx="1"/></p:nvPr></p:nvSpPr>'
        f'<p:spPr>{xfrm_xml(70, 430, 580, 250)}<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>{solid_fill(None)}{line_xml(None)}</p:spPr>'
        f'<p:txBody>{body_pr("top")}{paragraphs_xml(note_text, 16, COLORS["ink"], False, "left")}</p:txBody></p:sp>',
    ]
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<p:notes xmlns:a="{A_NS}" xmlns:r="{R_NS}" xmlns:p="{P_NS}">'
        f"<p:cSld><p:spTree>{''.join(body)}</p:spTree></p:cSld>"
        f"<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:notes>"
    )


def theme_xml() -> str:
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<a:theme xmlns:a="{A_NS}" name="DocWorldTrace Theme"><a:themeElements>'
        f'<a:clrScheme name="DocWorldTrace"><a:dk1><a:srgbClr val="{COLORS["ink"]}"/></a:dk1><a:lt1><a:srgbClr val="{COLORS["paper"]}"/></a:lt1>'
        f'<a:dk2><a:srgbClr val="{COLORS["slate"]}"/></a:dk2><a:lt2><a:srgbClr val="{COLORS["paper2"]}"/></a:lt2>'
        f'<a:accent1><a:srgbClr val="{COLORS["teal"]}"/></a:accent1><a:accent2><a:srgbClr val="{COLORS["amber"]}"/></a:accent2>'
        f'<a:accent3><a:srgbClr val="{COLORS["rose"]}"/></a:accent3><a:accent4><a:srgbClr val="{COLORS["green"]}"/></a:accent4>'
        f'<a:accent5><a:srgbClr val="{COLORS["slate"]}"/></a:accent5><a:accent6><a:srgbClr val="{COLORS["muted"]}"/></a:accent6>'
        f'<a:hlink><a:srgbClr val="{COLORS["teal_dark"]}"/></a:hlink><a:folHlink><a:srgbClr val="{COLORS["amber"]}"/></a:folHlink></a:clrScheme>'
        f'<a:fontScheme name="DocWorldTrace"><a:majorFont><a:latin typeface="{FONT_LATIN}"/><a:ea typeface="{FONT_CN}"/><a:cs typeface="{FONT_CN}"/></a:majorFont>'
        f'<a:minorFont><a:latin typeface="{FONT_LATIN}"/><a:ea typeface="{FONT_CN}"/><a:cs typeface="{FONT_CN}"/></a:minorFont></a:fontScheme>'
        f'<a:fmtScheme name="DocWorldTrace"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>'
        f'<a:lnStyleLst><a:ln w="9525"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst>'
        f'<a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst><a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst></a:fmtScheme>'
        f"</a:themeElements><a:objectDefaults/><a:extraClrSchemeLst/></a:theme>"
    )


def write_pptx(slides: List[Slide]) -> None:
    media_map: Dict[str, str] = {}
    slide_xmls = []
    slide_rels = []
    for i, slide in enumerate(slides, 1):
        xml, imgs, image_files = slide_xml(slide, i)
        slide_xmls.append(xml)
        rels = [("rId1", f"{R_NS}/slideLayout", "../slideLayouts/slideLayout1.xml")]
        for rid, target in imgs.items():
            rels.append((rid, f"{R_NS}/image", target))
        slide_rels.append(rels_xml(rels))
        for image_file in image_files:
            media_map[f"slide{i}_{Path(image_file).name}"] = image_file

    pres_rels = [(f"rId{i}", f"{R_NS}/slide", f"slides/slide{i}.xml") for i in range(1, len(slides) + 1)]
    pres_rels.extend([
        ("rIdMaster", f"{R_NS}/slideMaster", "slideMasters/slideMaster1.xml"),
        ("rIdNotesMaster", f"{R_NS}/notesMaster", "notesMasters/notesMaster1.xml"),
        ("rIdTheme", f"{R_NS}/theme", "theme/theme1.xml"),
        ("rIdPresProps", f"{R_NS}/presProps", "presProps.xml"),
        ("rIdViewProps", f"{R_NS}/viewProps", "viewProps.xml"),
        ("rIdTableStyles", f"{R_NS}/tableStyles", "tableStyles.xml"),
    ])

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types_xml(len(slides)))
        z.writestr("_rels/.rels", rels_xml([
            ("rId1", f"{R_NS}/officeDocument", "ppt/presentation.xml"),
            ("rId2", "http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties", "docProps/core.xml"),
            ("rId3", f"{R_NS}/extended-properties", "docProps/app.xml"),
        ]))
        z.writestr("docProps/core.xml", core_xml())
        z.writestr("docProps/app.xml", app_xml(len(slides)))
        z.writestr("ppt/presentation.xml", presentation_xml(len(slides)))
        z.writestr("ppt/_rels/presentation.xml.rels", rels_xml(pres_rels))
        z.writestr("ppt/slideMasters/slideMaster1.xml", master_xml())
        z.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", rels_xml([
            ("rId1", f"{R_NS}/slideLayout", "../slideLayouts/slideLayout1.xml"),
            ("rId2", f"{R_NS}/theme", "../theme/theme1.xml"),
        ]))
        z.writestr("ppt/notesMasters/notesMaster1.xml", notes_master_xml())
        z.writestr("ppt/notesMasters/_rels/notesMaster1.xml.rels", rels_xml([
            ("rId1", f"{R_NS}/theme", "../theme/theme1.xml"),
        ]))
        z.writestr("ppt/slideLayouts/slideLayout1.xml", layout_xml())
        z.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", rels_xml([
            ("rId1", f"{R_NS}/slideMaster", "../slideMasters/slideMaster1.xml"),
        ]))
        z.writestr("ppt/theme/theme1.xml", theme_xml())
        z.writestr("ppt/presProps.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:presentationPr xmlns:p="%s"/>' % P_NS)
        z.writestr("ppt/viewProps.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><p:viewPr xmlns:p="%s"/>' % P_NS)
        z.writestr("ppt/tableStyles.xml", '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><a:tblStyleLst xmlns:a="%s" def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"/>' % A_NS)
        for i, xml in enumerate(slide_xmls, 1):
            z.writestr(f"ppt/slides/slide{i}.xml", xml)
            rel_xml = slide_rels[i - 1].replace(
                "</Relationships>",
                f'<Relationship Id="rIdNotes" Type="{R_NS}/notesSlide" Target="../notesSlides/notesSlide{i}.xml"/></Relationships>',
            )
            z.writestr(f"ppt/slides/_rels/slide{i}.xml.rels", rel_xml)
            z.writestr(f"ppt/notesSlides/notesSlide{i}.xml", notes_slide_xml(slides[i - 1], i))
            z.writestr(f"ppt/notesSlides/_rels/notesSlide{i}.xml.rels", rels_xml([
                ("rId1", f"{R_NS}/slide", f"../slides/slide{i}.xml"),
                ("rId2", f"{R_NS}/notesMaster", "../notesMasters/notesMaster1.xml"),
            ]))
        for media_name, image_file in media_map.items():
            z.write(ASSETS / image_file, f"ppt/media/{media_name}")


def core_xml() -> str:
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<cp:coreProperties xmlns:cp="{CP_NS}" xmlns:dc="{DC_NS}" xmlns:dcterms="{DCTERMS_NS}" xmlns:dcmitype="{DCTYPE_NS}" xmlns:xsi="{XSI_NS}">'
        f"<dc:title>DocWorldTrace Proposal Briefing</dc:title><dc:creator>Codex</dc:creator>"
        f"<cp:lastModifiedBy>Codex</cp:lastModifiedBy><dcterms:created xsi:type=\"dcterms:W3CDTF\">2026-04-30T00:00:00Z</dcterms:created>"
        f"<dcterms:modified xsi:type=\"dcterms:W3CDTF\">2026-04-30T00:00:00Z</dcterms:modified></cp:coreProperties>"
    )


def app_xml(slide_count: int) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
        'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
        f"<Application>Codex</Application><PresentationFormat>16:9</PresentationFormat><Slides>{slide_count}</Slides>"
        "</Properties>"
    )


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size=size, index=0)
    return ImageFont.load_default()


def wrap_text(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, width: int) -> List[str]:
    lines: List[str] = []
    for raw in text.split("\n"):
        current = ""
        for ch in raw:
            trial = current + ch
            box = draw.textbbox((0, 0), trial, font=fnt)
            if box[2] - box[0] <= width or not current:
                current = trial
            else:
                lines.append(current)
                current = ch
        lines.append(current)
    return lines


def draw_text(draw: ImageDraw.ImageDraw, el: Element) -> None:
    fnt = font(el.size, el.bold)
    lines = wrap_text(draw, el.text, fnt, int(el.w))
    line_h = int(el.size * 1.22)
    total_h = line_h * len(lines)
    y = el.y
    if el.valign == "middle":
        y = el.y + (el.h - total_h) / 2
    elif el.valign == "bottom":
        y = el.y + el.h - total_h
    for line in lines:
        box = draw.textbbox((0, 0), line, font=fnt)
        tw = box[2] - box[0]
        x = el.x
        if el.align == "center":
            x = el.x + (el.w - tw) / 2
        elif el.align == "right":
            x = el.x + el.w - tw
        draw.text((x, y), line, font=fnt, fill="#" + rgb(el.color))
        y += line_h


def render_previews(slides: List[Slide]) -> None:
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    for i, slide in enumerate(slides, 1):
        img = Image.new("RGB", (W, H), "#" + COLORS["paper"])
        draw = ImageDraw.Draw(img, "RGBA")
        for el in slide.elements:
            if el.kind == "image" and el.image:
                bg = Image.open(ASSETS / el.image).convert("RGB").resize((int(el.w), int(el.h)))
                img.paste(bg, (int(el.x), int(el.y)))
                draw = ImageDraw.Draw(img, "RGBA")
            elif el.kind == "rect":
                fill = None if not el.fill else tuple(int(rgb(el.fill)[j:j+2], 16) for j in (0, 2, 4)) + (int(el.alpha * 255 / 100000),)
                outline = None if not el.line else "#" + rgb(el.line)
                xy = [int(el.x), int(el.y), int(el.x + el.w), int(el.y + el.h)]
                if el.radius:
                    draw.rounded_rectangle(xy, radius=el.radius, fill=fill, outline=outline, width=max(1, int(el.line_width)))
                else:
                    draw.rectangle(xy, fill=fill, outline=outline, width=max(1, int(el.line_width)) if outline else 1)
            elif el.kind == "line":
                x1, y1 = el.x, el.y
                x2, y2 = el.x + el.w, el.y + el.h
                draw.line([x1, y1, x2, y2], fill="#" + rgb(el.line or COLORS["line"]), width=max(1, int(el.line_width)))
                if el.arrow:
                    draw.polygon([(x2, y2), (x2 - 8, y2 - 5), (x2 - 8, y2 + 5)], fill="#" + rgb(el.line or COLORS["line"]))
            elif el.kind == "text" and el.text:
                draw_text(draw, el)
            elif el.text:
                draw_text(draw, el)
        img.save(PREVIEWS / f"slide_{i:02d}.png")


def validate_pptx(slides: List[Slide]) -> None:
    findings: List[str] = []
    with zipfile.ZipFile(OUT, "r") as z:
        names = set(z.namelist())
        expected = {f"ppt/slides/slide{i}.xml" for i in range(1, len(slides) + 1)}
        missing = sorted(expected - names)
        findings.append(f"- Slides present: {len(expected) - len(missing)}/{len(expected)}")
        if missing:
            findings.append(f"- Missing slide XML: {missing}")
        for name in expected:
            ET.fromstring(z.read(name))
        text_count = 0
        key_terms = ["DocWorldTrace", "50/50", "80/80", "144/144", "52.78%", "12 周", "ti2025ars", "7.0 percentage points"]
        all_xml = "\n".join(z.read(name).decode("utf-8") for name in expected)
        for name in expected:
            text_count += z.read(name).decode("utf-8").count("<a:t>")
        findings.append(f"- Editable text runs: {text_count}")
        for term in key_terms:
            findings.append(f"- Key term `{term}` present: {'yes' if esc(term) in all_xml or term in all_xml else 'no'}")
    findings.append(f"- Preview PNGs: {len(list(PREVIEWS.glob('slide_*.png')))}/{len(slides)}")
    VERIFY.write_text("# Verification Report\n\n" + "\n".join(findings) + "\n", encoding="utf-8")


def main() -> None:
    required = [
        ASSETS / "title_environment_trace.png",
        ASSETS / "docenv_workbench.png",
        ASSETS / "trajectory_synthesis.png",
        ASSETS / "dataset_example_visual.png",
        ASSETS / "quality_control.png",
    ]
    for path in required:
        if not path.exists():
            raise FileNotFoundError(path)
    slides = make_slides()
    write_pptx(slides)
    render_previews(slides)
    validate_pptx(slides)
    print(f"Wrote {OUT}")
    print(f"Wrote {PREVIEWS}")
    print(f"Wrote {VERIFY}")


if __name__ == "__main__":
    main()
