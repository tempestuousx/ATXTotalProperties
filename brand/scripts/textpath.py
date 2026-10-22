"""Turn text into SVG path data so logos look the same everywhere (no font needed)."""
import math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT_DIR = "fonts/"
_cache = {}


def font(name):
    if name not in _cache:
        f = TTFont(FONT_DIR + name)
        _cache[name] = (f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm)
    return _cache[name]


def _glyph(fname, ch):
    f, gs, cmap, upm = font(fname)
    gname = cmap.get(ord(ch), ".notdef")
    return gs[gname], gname, upm


def measure(text, fname, size, tracking=0):
    """Width in px. tracking is extra space per letter, in em."""
    w = 0
    for ch in text:
        g, _, upm = _glyph(fname, ch)
        w += g.width * size / upm + tracking * size
    return w - tracking * size if text else 0


def cap_height(fname, size):
    f, _, _, upm = font(fname)
    os2 = f["OS/2"]
    return getattr(os2, "sCapHeight", 0.7 * upm) * size / upm


def _glyph_path(g, gs, s, matrix):
    pen = SVGPathPen(gs)
    g.draw(TransformPen(pen, matrix))
    return pen.getCommands()


def text(text, fname, size, x, y, anchor="start", tracking=0):
    """Straight text. (x, y) is the baseline point."""
    f, gs, cmap, upm = font(fname)
    s = size / upm
    w = measure(text, fname, size, tracking)
    cx = x - {"start": 0, "middle": w / 2, "end": w}[anchor]
    out = []
    for ch in text:
        g, _, _ = _glyph(fname, ch)
        out.append(_glyph_path(g, gs, s, (s, 0, 0, -s, cx, y)))
        cx += g.width * s + tracking * size
    return " ".join(out)


def arc_text(text, fname, size, cx, cy, r, center_deg, bottom=False, tracking=0):
    """Text on a circle. Top text: baseline on r, reads clockwise.
    Bottom text: baseline on r, letters point to center, reads left to right."""
    f, gs, cmap, upm = font(fname)
    s = size / upm
    ch_h = cap_height(fname, size)
    rr = r - ch_h / 2 if bottom else r + ch_h / 2  # spacing radius at letter middle
    total = measure(text, fname, size, tracking)
    span = total / rr  # radians
    direction = -1 if bottom else 1
    start = math.radians(center_deg) - direction * span / 2
    pos = 0
    out = []
    for ch in text:
        g, _, _ = _glyph(fname, ch)
        adv = g.width * s
        a = start + direction * (pos + adv / 2) / rr
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        rot = a + (-math.pi / 2 if bottom else math.pi / 2)
        c, sn = math.cos(rot), math.sin(rot)
        # local: x' = (gx*s - adv/2), y' = -gy*s, then rotate and move
        a11, a12 = c * s, -sn * -s
        a21, a22 = sn * s, c * -s
        tx = px + c * (-adv / 2)
        ty = py + sn * (-adv / 2)
        out.append(_glyph_path(g, gs, s, (a11, a21, a12, a22, tx, ty)))
        pos += adv + tracking * size
    return " ".join(out)
