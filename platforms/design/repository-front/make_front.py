"""Repository front page standard v1: the cover pictures of a repository's README.

    python make_front.py <repo>/docs/assets/front/front.json            write the covers next to it
    python make_front.py <repo>/docs/assets/front/front.json --check    exit 1 when they differ from the config

The same config also holds the README front block: "start" (the documents a reader opens first) and "facts"
(What it is / Who it serves / State / Built with, in English and Armenian). The block is written into README.md
between <!-- FRONT:START --> and <!-- FRONT:END --> (top of the file); everything after it stays as it was.
Every linked path must exist in the repository, or the script stops.

From one small config (name, family, one line in English and Armenian, brand) it writes four SVG files:
cover-light.svg, cover-dark.svg (960 x 320, wide screens) and cover-narrow-light.svg, cover-narrow-dark.svg
(480 x 340, phones). Rules the pictures follow:
  - the brand's own identity only. A MenQ Studio repository carries the official MenQ wordmark file, copied as it is
    (brand-expression/assets/Logos); a client repository (brand "client") carries its own palette and no MenQ mark;
  - every letter is an outline traced from the brand fonts (Inter, Noto Sans Armenian; SIL OFL), so the picture looks
    the same everywhere and loads no font; no script, no foreignObject, no external resource;
  - light and dark are equals; text contrast at least 4.5:1, checked here;
  - the picture holds no fact that goes stale (no dates, counts or states): those stay in the Markdown next to it.
Needs fontTools and brotli.
"""
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = Path(__file__).resolve().parent
BRAND = HERE.parent / "brand-expression"
FONTS = BRAND / "fonts"
LOGOS = BRAND / "assets" / "Logos"

BRANDS = {
    "menq": {
        "light": {"bg": "#f8fafc", "ink": "#0f172a", "muted": "#475569", "chip_bg": "#e0f2fe", "chip_ink": "#075985", "grid": "#0f172a", "grid_a": 0.05, "glow1": "#0ea5e9", "glow2": "#22d3ee", "glow_a": 0.16, "rule": "#0369a1"},
        "dark": {"bg": "#020617", "ink": "#f8fafc", "muted": "#94a3b8", "chip_bg": "#0c2a3d", "chip_ink": "#7dd3fc", "grid": "#ffffff", "grid_a": 0.05, "glow1": "#0ea5e9", "glow2": "#22d3ee", "glow_a": 0.26, "rule": "#22d3ee"},
        "logo": {"light": "menq-wordmark-light.svg", "dark": "menq-wordmark-dark.svg"},
    },
}


def client_brand(p):
    """A client's palette from its own config: {"light": {...}, "dark": {...}} with the same keys as BRANDS."""
    return {"light": p["light"], "dark": p["dark"], "logo": None}


# ---------------------------------------------------------------- text as outlines
FACES = {
    ("latin", 400): "Inter-Latin-Variable.woff2", ("latin", 700): "Inter-Latin-Variable.woff2",
    ("cyrillic", 400): "Inter-Cyrillic-Variable.woff2", ("cyrillic", 700): "Inter-Cyrillic-Variable.woff2",
    ("armenian", 400): "NotoSansArmenian-Variable.woff2", ("armenian", 700): "NotoSansArmenian-Variable.woff2",
}


@lru_cache(None)
def face(script, weight):
    f = TTFont(FONTS / FACES[(script, weight)])
    if "fvar" in f:
        f = instancer.instantiateVariableFont(f, {"wght": weight})
    return f


def script_of(ch):
    o = ord(ch)
    if 0x0530 <= o <= 0x058F or 0xFB13 <= o <= 0xFB17:
        return "armenian"
    if 0x0400 <= o <= 0x04FF:
        return "cyrillic"
    return "latin"


def glyph(ch, weight):
    for script in (script_of(ch), "latin", "armenian", "cyrillic"):
        f = face(script, weight)
        name = f.getBestCmap().get(ord(ch))
        if name:
            return f, name
    raise SystemExit("no glyph for %r" % ch)


def measure(text, size, weight, ls=0.0):
    w = 0.0
    for ch in text:
        f, name = glyph(ch, weight)
        w += f["hmtx"][name][0] * size / f["head"].unitsPerEm + ls
    return w - ls if text else 0.0


def outline(text, x, y, size, weight, fill, ls=0.0, cls=None):
    """Path of `text` with its baseline starting at (x, y)."""
    parts = []
    for ch in text:
        f, name = glyph(ch, weight)
        k = size / f["head"].unitsPerEm
        gs = f.getGlyphSet()
        pen = SVGPathPen(gs)
        gs[name].draw(TransformPen(pen, (k, 0, 0, -k, x, y)))
        d = pen.getCommands()
        if d:
            parts.append(d)
        x += f["hmtx"][name][0] * k + ls
    d = " ".join(parts)
    d = re.sub(r"(\d+\.\d{2})\d+", r"\1", d)
    attr = ' class="%s"' % cls if cls else ""
    return '<path%s fill="%s" d="%s"/>' % (attr, fill, d)


def wrap(text, size, weight, width):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        cand = (cur + " " + wd).strip()
        if measure(cand, size, weight) <= width or not cur:
            cur = cand
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- contrast
def lum(hexc):
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def check_palette(p, theme):
    for fg, bg in (("ink", "bg"), ("muted", "bg"), ("chip_ink", "chip_bg")):
        r = ratio(p[fg], p[bg])
        if r < 4.5:
            raise SystemExit("%s: %s on %s is %.2f:1, needs 4.5:1" % (theme, fg, bg, r))


# ---------------------------------------------------------------- the pictures
def logo_svg(brand, theme, x, y, h):
    if not brand["logo"]:
        return "", 0.0
    src = (LOGOS / brand["logo"][theme]).read_text(encoding="utf-8")
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', src).group(1).split()]
    w = h * vb[2] / vb[3]
    inner = src[src.index(">", src.index("<svg")) + 1:src.rindex("</svg>")]
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)
    return ('<svg x="%.1f" y="%.1f" width="%.1f" height="%.1f" viewBox="%s" role="img" aria-label="MenQ">%s</svg>'
            % (x, y, w, h, " ".join("%g" % v for v in vb), inner)), w


def chip(text, x, y, p):
    size, padx, h = 13, 12, 26
    w = measure(text, size, 700, 0.6) + 2 * padx
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="13" fill="%s"/>' % (x, y, w, h, p["chip_bg"])
            + outline(text, x + padx, y + 17.5, size, 700, p["chip_ink"], 0.6)), w


def ground(W, H, p, uid):
    grid = "".join('<path d="M%d 0V%d"/>' % (gx, H) for gx in range(48, W, 48)) + "".join('<path d="M0 %dH%d"/>' % (gy, W) for gy in range(48, H, 48))
    return ('<defs><radialGradient id="g1-%s" cx="%d" cy="0" r="%d" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s" stop-opacity="%.2f"/><stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient>'
            '<radialGradient id="g2-%s" cx="%d" cy="%d" r="%d" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="%s" stop-opacity="%.2f"/><stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient></defs>'
            % (uid, W, int(W * 0.55), p["glow1"], p["glow_a"], p["glow1"], uid, int(W * 0.7), H, int(W * 0.4), p["glow2"], p["glow_a"] * 0.7, p["glow2"])
            + '<rect width="%d" height="%d" fill="%s"/>' % (W, H, p["bg"])
            + '<g stroke="%s" stroke-opacity="%.2f" stroke-width="1">%s</g>' % (p["grid"], p["grid_a"], grid)
            + '<rect width="%d" height="%d" fill="url(#g1-%s)"/><rect width="%d" height="%d" fill="url(#g2-%s)"/>' % (W, H, uid, W, H, uid))


def cover(cfg, brand, theme, narrow):
    p = brand[theme]
    check_palette(p, theme)
    W, H = (480, 340) if narrow else (960, 320)
    m = 32 if narrow else 48
    out = [ground(W, H, p, theme + ("n" if narrow else "w"))]
    top = 36 if narrow else 40
    lg, lw = logo_svg(brand, theme, m, top, 34 if narrow else 40)
    out.append(lg)
    cx = m + lw + (14 if lw else 0)
    c, cw = chip(cfg["family"]["en"], cx, top + (4 if narrow else 7), p)
    out.append(c)
    name_size = 40 if narrow else 56
    name_lines = wrap(cfg["name"], name_size, 700, W - 2 * m) if narrow else [cfg["name"]]
    if not narrow and measure(cfg["name"], name_size, 700) > W - 2 * m:
        name_size = 44
    y = (top + 34 + 60) if narrow else 164
    for i, line in enumerate(name_lines):
        if i:
            y += name_size * 1.08
        out.append(outline(line, m, y, name_size, 700, p["ink"], -0.02 * name_size))
    y += 12
    width = W - 2 * m if narrow else 780
    for key, size in (("en", 18 if narrow else 20), ("hy", 16 if narrow else 18)):
        for line in wrap(cfg["tagline"][key], size, 400, width):
            y += size * 1.45
            out.append(outline(line, m, y, size, 400, p["muted"]))
        y += 4
    if y > H - 16:
        raise SystemExit("%s %s: text runs past the picture (%.0f > %d); shorten the tagline" % (cfg["name"], "narrow" if narrow else "wide", y, H - 16))
    if y + 22 <= H - 20:
        out.append('<rect x="%d" y="%d" width="64" height="3" rx="1.5" fill="%s"/>' % (m, max(y + 22, H - 40), p["rule"]))
    alt = "%s: %s" % (cfg["name"], cfg["tagline"]["en"])
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="%s">%s</svg>\n'
            % (W, H, W, H, alt.replace('"', "&quot;"), "".join(out)))


START, END = "<!-- FRONT:START -->", "<!-- FRONT:END -->"


def picture(base):
    a = "docs/assets/front/"
    return ('<picture><source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="%scover-narrow-dark.svg">'
            '<source media="(max-width: 600px)" srcset="%scover-narrow-light.svg">'
            '<source media="(prefers-color-scheme: dark)" srcset="%scover-dark.svg">'
            '<img src="%scover-light.svg" alt="%s" width="960"></picture>') % (a, a, a, a, base.replace('"', "&quot;"))


def front_block(cfg, repo):
    for _, path in cfg["start"]:
        if not (repo / path.split("#")[0]).exists():
            raise SystemExit("start link points to a missing path: " + path)
    links = " · ".join("[%s](%s)" % (label, path) for label, path in cfg["start"])
    def table(rows):
        return "| | |\n| :-- | :-- |\n" + "\n".join("| **%s** | %s |" % (k, v) for k, v in rows) + "\n"
    return "\n".join([
        START,
        '<p align="center">' + picture("%s: %s" % (cfg["name"], cfg["tagline"]["en"])) + "</p>",
        "",
        "<p align=\"center\"><b>Start here</b> · " + links + "</p>",
        "",
        table(cfg["facts"]["en"]),
        "<details><summary><b>Հայերեն</b></summary>",
        "",
        table(cfg["facts"]["hy"]),
        "</details>",
        "",
        "<sub>%s · repository front page standard v1</sub>" % cfg["family"]["en"],
        END,
        "",
    ])


def write_readme(cfg, readme, check=False):
    text = readme.read_text(encoding="utf-8")
    block = front_block(cfg, readme.parent)
    if START in text:
        head, rest = text.split(START, 1)
        rest = rest.split(END, 1)[1].lstrip("\n")
        new = head + block + "\n" + rest
    else:
        new = block + "\n" + text
    if check:
        return new == text
    readme.write_text(new, encoding="utf-8", newline="")
    return True


def build(cfg_path):
    cfg = json.loads(Path(cfg_path).read_text(encoding="utf-8"))
    brand = BRANDS[cfg["brand"]] if cfg["brand"] in BRANDS else client_brand(cfg["palette"])
    return {("cover-%s%s.svg" % ("narrow-" if narrow else "", theme)): cover(cfg, brand, theme, narrow)
            for narrow in (False, True) for theme in ("light", "dark")}


def main():
    cfg_path = Path(sys.argv[1]).resolve()
    files = build(cfg_path)
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    readme = cfg_path.parents[3] / "README.md"          # <repo>/docs/assets/front/front.json
    if "--check" in sys.argv[2:]:
        stale = [n for n, t in files.items() if not (cfg_path.parent / n).exists() or (cfg_path.parent / n).read_text(encoding="utf-8") != t]
        if "start" in cfg and not write_readme(cfg, readme, check=True):
            stale.append("README.md front block")
        print("FRONT PAGE: " + ("STALE " + ", ".join(stale) if stale else "up to date"))
        return 1 if stale else 0
    for n, t in files.items():
        (cfg_path.parent / n).write_text(t, encoding="utf-8", newline="\n")
    if "start" in cfg:
        write_readme(cfg, readme)
    print("FRONT PAGE: written %d covers%s" % (len(files), " and the README front block" if "start" in cfg else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
