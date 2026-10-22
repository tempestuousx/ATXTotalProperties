"""Builds every logo SVG for ATX Total Properties. Run from the brand/ folder."""
import base64, io, os
from PIL import Image
import textpath as tp

# Brand colors
INK = "#161616"      # Shop Black
EMBER = "#E2692B"    # Austin Ember (orange)
HONEY = "#F2B33D"    # Honey (the "honey-do" accent)
CREAM = "#F6EFE4"    # Sawdust
FLANNEL = "#5E656C"  # Flannel Gray

OUT = "logos/svg"
os.makedirs(OUT, exist_ok=True)


def portrait_b64(size=720):
    im = Image.open("source/brandon-square.png").convert("RGB").resize((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    return base64.b64encode(buf.getvalue()).decode()


PORTRAIT = portrait_b64()


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {w} {h}" width="{w}" height="{h}"><title>{title}</title>{body}</svg>\n')


def star(cx, cy, r, fill):
    import math
    pts = []
    for i in range(10):
        rad = r if i % 2 == 0 else r * 0.42
        a = math.radians(-90 + i * 36)
        pts.append(f"{cx + rad * math.cos(a):.1f},{cy + rad * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


def house_check(x, y, s, house=EMBER, check=HONEY, stroke=None, sw=0):
    """House with a check mark. Box is 100x100 at (x, y), scaled by s/100."""
    k = s / 100
    st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke else ""
    return (f'<g transform="translate({x} {y}) scale({k})">'
            f'<path d="M50 6 L96 46 L84 46 L84 94 L16 94 L16 46 L4 46 Z" fill="{house}"{st}/>'
            f'<path d="M30 64 L45 78 L72 50" fill="none" stroke="{check}" stroke-width="11" '
            f'stroke-linecap="round" stroke-linejoin="round"/></g>')


def badge(cx=500, cy=500, ring=EMBER, bg=INK, text_top=CREAM, text_bot=HONEY):
    """Primary circular badge with Brandon's portrait. Drawn in a 1000x1000 box."""
    b = []
    b.append(f'<defs><clipPath id="pc"><circle cx="{cx}" cy="{cy}" r="300"/></clipPath></defs>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="492" fill="{bg}"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="470" fill="none" stroke="{ring}" stroke-width="14"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="326" fill="none" stroke="{ring}" stroke-width="10"/>')
    # Portrait (image already has a black background)
    b.append(f'<g clip-path="url(#pc)"><rect x="{cx-300}" y="{cy-300}" width="600" height="600" fill="#000"/>'
             f'<image x="{cx-310}" y="{cy-292}" width="620" height="620" '
             f'xlink:href="data:image/jpeg;base64,{PORTRAIT}" href="data:image/jpeg;base64,{PORTRAIT}"/></g>')
    # Brand mark on the cap (replaces the old team logo)
    b.append(house_check(cx - 26.5, cy - 264, 84, stroke=INK, sw=5))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="300" fill="none" stroke="{CREAM}" stroke-width="4"/>')
    # Arc text
    b.append(f'<path fill="{text_top}" d="{tp.arc_text("ATX TOTAL PROPERTIES", "ArchivoBlack-Regular.ttf", 74, cx, cy, 372, -90, tracking=0.04)}"/>')
    b.append(f'<path fill="{text_bot}" d="{tp.arc_text("HONEY-DO LIST SPECIALISTS", "Oswald-Bold.ttf", 62, cx, cy, 425, 90, bottom=True, tracking=0.12)}"/>')
    b.append(star(cx - 398, cy + 6, 26, ring))
    b.append(star(cx + 398, cy + 6, 26, ring))
    return "".join(b)


def wordmark(x, y, main=INK, accent=EMBER, tag=FLANNEL, tagline=True):
    """Two-line wordmark. (x, y) is the top-left. Returns (svg, width, height)."""
    f1, f2 = "ArchivoBlack-Regular.ttf", "Oswald-Bold.ttf"
    s1 = 120
    w_atx = tp.measure("ATX ", f1, s1)
    w_total = tp.measure("TOTAL", f1, s1)
    line1_w = w_atx + w_total
    # Size "PROPERTIES" so it matches the first line width
    s2 = s1 * line1_w / tp.measure("PROPERTIES", f1, s1, tracking=0.02)
    cap1 = tp.cap_height(f1, s1)
    cap2 = tp.cap_height(f1, s2)
    gap = 26
    b = [f'<path fill="{accent}" d="{tp.text("ATX", f1, s1, x, y + cap1)}"/>',
         f'<path fill="{main}" d="{tp.text("TOTAL", f1, s1, x + w_atx, y + cap1)}"/>',
         f'<path fill="{main}" d="{tp.text("PROPERTIES", f1, s2, x, y + cap1 + gap + cap2, tracking=0.02)}"/>']
    h = cap1 + gap + cap2
    if tagline:
        ts = 44
        tag_w = tp.measure("YOUR HONEY-DO LIST, DONE.", f2, ts, tracking=0.14)
        ts = ts * line1_w / tag_w
        th = tp.cap_height(f2, ts)
        ty = y + h + 34
        b.append(f'<rect x="{x}" y="{ty - 4}" width="{line1_w}" height="6" fill="{HONEY}"/>')
        b.append(f'<path fill="{tag}" d="{tp.text("YOUR HONEY-DO LIST, DONE.", f2, ts, x, ty + 28 + th, tracking=0.14)}"/>')
        h = ty + 28 + th - y
    return "".join(b), line1_w, h


def write(name, w, h, body, title):
    with open(f"{OUT}/{name}.svg", "w") as f:
        f.write(svg(w, h, body, title))


# 1. Primary badge (full color, plus a cream ring version for dark photos)
write("atx-badge-primary", 1000, 1000, badge(), "ATX Total Properties badge")
write("atx-badge-honey", 1000, 1000, badge(ring=HONEY, text_bot=EMBER), "ATX Total Properties badge, honey ring")

# 2. Horizontal lockup: badge + wordmark
wm, ww, wh = wordmark(0, 0)
scale = 0.52
bw = 1000 * scale
pad = 60
H = max(bw, wh) + pad * 2
W = pad + bw + 70 + ww + pad
body = (f'<g transform="translate({pad} {(H - bw) / 2}) scale({scale})">{badge()}</g>'
        f'<g transform="translate({pad + bw + 70} {(H - wh) / 2})">{wm}</g>')
write("atx-lockup-horizontal", round(W), round(H), body, "ATX Total Properties horizontal logo")
wm_d, _, _ = wordmark(0, 0, main=CREAM, tag=CREAM)
body_d = (f'<g transform="translate({pad} {(H - bw) / 2}) scale({scale})">{badge()}</g>'
          f'<g transform="translate({pad + bw + 70} {(H - wh) / 2})">{wm_d}</g>')
write("atx-lockup-horizontal-on-dark", round(W), round(H), body_d, "ATX Total Properties horizontal logo, for dark backgrounds")

# 3. Stacked lockup
SW = max(1000 * 0.62, ww) + pad * 2
bs = 0.62
SH = pad + 1000 * bs + 50 + wh + pad
body = (f'<g transform="translate({(SW - 1000 * bs) / 2} {pad}) scale({bs})">{badge()}</g>'
        f'<g transform="translate({(SW - ww) / 2} {pad + 1000 * bs + 50})">{wm}</g>')
write("atx-lockup-stacked", round(SW), round(SH), body, "ATX Total Properties stacked logo")

# 4. Wordmark only
for nm, m, t in (("atx-wordmark", INK, FLANNEL), ("atx-wordmark-on-dark", CREAM, CREAM)):
    wmx, ww2, wh2 = wordmark(40, 40, main=m, tag=t)
    write(nm, round(ww2 + 80), round(wh2 + 80), wmx, "ATX Total Properties wordmark")

# 5. Simple icon mark (no portrait) for tiny sizes: favicon, app icon
icon = (f'<rect width="512" height="512" rx="112" fill="{INK}"/>'
        f'{house_check(86, 70, 340)}'
        f'<path fill="{CREAM}" d="{tp.text("ATX", "ArchivoBlack-Regular.ttf", 92, 256, 470, "middle", tracking=0.06)}"/>')
write("atx-icon-mark", 512, 512, icon, "ATX Total Properties icon")
write("atx-icon-mark-plain", 512, 512, f'<rect width="512" height="512" rx="112" fill="{INK}"/>{house_check(76, 70, 360)}',
      "ATX Total Properties icon, no text")
write("atx-icon-mark-transparent", 512, 512, house_check(16, 16, 480), "ATX Total Properties house check mark")

# 6. One-color versions (for vinyl, embroidery, stamps)
def mono(color):
    b = [f'<circle cx="500" cy="500" r="470" fill="none" stroke="{color}" stroke-width="14"/>',
         f'<circle cx="500" cy="500" r="326" fill="none" stroke="{color}" stroke-width="10"/>',
         f'<mask id="hk"><rect width="1000" height="1000" fill="#fff"/>{house_check(330, 260, 340, house="#fff", check="#000")}</mask>',
         f'<g mask="url(#hk)">{house_check(330, 260, 340, house=color, check=color)}</g>',
         f'<path fill="{color}" d="{tp.arc_text("ATX TOTAL PROPERTIES", "ArchivoBlack-Regular.ttf", 74, 500, 500, 372, -90, tracking=0.04)}"/>',
         f'<path fill="{color}" d="{tp.arc_text("HONEY-DO LIST SPECIALISTS", "Oswald-Bold.ttf", 62, 500, 500, 425, 90, bottom=True, tracking=0.12)}"/>',
         star(102, 506, 26, color), star(898, 506, 26, color),
         f'<path fill="{color}" d="{tp.text("AUSTIN, TX", "Oswald-Bold.ttf", 54, 500, 690, "middle", tracking=0.2)}"/>']
    return "".join(b)

write("atx-badge-one-color-black", 1000, 1000, mono(INK), "ATX Total Properties one-color badge")
write("atx-badge-one-color-white", 1000, 1000, mono("#FFFFFF"), "ATX Total Properties one-color badge, white")
print("built", len(os.listdir(OUT)), "svgs")
