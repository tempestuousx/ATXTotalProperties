"""Social media, business card and favicon files. Writes HTML pages that render.mjs-style screenshots turn into PNGs."""
import os, re

INK, EMBER, HONEY, CREAM, FLANNEL = "#161616", "#E2692B", "#F2B33D", "#F6EFE4", "#5E656C"
os.makedirs("kit/html", exist_ok=True)


def inline(name, w=None):
    s = open(f"logos/svg/{name}.svg").read()
    s = re.sub(r'<title>.*?</title>', '', s)
    if w:
        s = re.sub(r'width="[\d.]+" height="[\d.]+"', f'width="{w}" height="auto"', s, count=1)
        s = s.replace('height="auto"', 'style="height:auto;display:block"')
    return s


def icon(name, size, variant="color"):
    return open(f"icons/svg-{variant}/{name}.svg").read().replace('width="64" height="64"', f'width="{size}" height="{size}"')


FONTS = """
@font-face{font-family:Archivo;src:url(../../fonts/ArchivoBlack-Regular.ttf)}
@font-face{font-family:Oswald;font-weight:700;src:url(../../fonts/Oswald-Bold.ttf)}
@font-face{font-family:Oswald;font-weight:500;src:url(../../fonts/Oswald-Medium.ttf)}
@font-face{font-family:Inter;font-weight:400;src:url(../../fonts/Inter-Regular.ttf)}
@font-face{font-family:Inter;font-weight:600;src:url(../../fonts/Inter-SemiBold.ttf)}
@font-face{font-family:Inter;font-weight:800;src:url(../../fonts/Inter-ExtraBold.ttf)}
*{box-sizing:border-box;margin:0;padding:0}
body{width:%dpx;height:%dpx;overflow:hidden;font-family:Inter}
.h{font-family:Archivo;letter-spacing:.01em}
.o{font-family:Oswald;font-weight:700;letter-spacing:.12em;text-transform:uppercase}
"""

PAGES = {}

# Profile picture (Facebook, Instagram, Google Business): the badge on black
PAGES["profile-picture"] = (1080, 1080, f"""<body style="background:{INK};display:flex;align-items:center;justify-content:center">
{inline('atx-badge-primary', 1040)}</body>""")

# Facebook cover 1640x624 (safe area in the middle)
services = ["handyman-tools", "paint-roller", "plumbing", "electrical", "tv-mounting", "yard-work"]
PAGES["facebook-cover"] = (1640, 624, f"""<body style="background:{INK};color:{CREAM};display:flex;align-items:center;padding:0 140px 0 470px;position:relative">
<div style="position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent 0 60px,rgba(255,255,255,.03) 60px 64px),repeating-linear-gradient(0deg,transparent 0 60px,rgba(255,255,255,.03) 60px 64px)"></div>
<div style="position:relative">
<div class="o" style="color:{HONEY};font-size:30px">Austin's honey-do list specialists</div>
<div class="h" style="font-size:92px;line-height:1.02;margin:14px 0 22px">Your list.<br><span style="color:{EMBER}">Done right.</span></div>
<div style="display:flex;gap:22px">{''.join(f'<div style="background:{CREAM};border-radius:14px;padding:10px">{icon(s, 56)}</div>' for s in services)}</div>
</div></body>""")

# Instagram post template 1080x1350
PAGES["instagram-post-template"] = (1080, 1350, f"""<body style="background:{CREAM};padding:80px;display:flex;flex-direction:column">
<div style="display:flex;align-items:center;gap:20px">{inline('atx-icon-mark', 90)}<div class="o" style="font-size:28px;color:{FLANNEL}">ATX Total Properties</div></div>
<div class="o" style="margin-top:120px;font-size:34px;color:{EMBER}">Honey-do tip #01</div>
<div class="h" style="font-size:104px;line-height:1.02;color:{INK};margin-top:20px">Your headline goes right here.</div>
<div style="font-size:36px;line-height:1.4;color:{FLANNEL};margin-top:40px;max-width:820px">One or two short lines of helpful detail. Keep it simple and useful.</div>
<div style="margin-top:auto;display:flex;justify-content:space-between;align-items:center;border-top:6px solid {HONEY};padding-top:30px">
<div class="o" style="font-size:30px;color:{INK}">Book your list today</div><div style="font-weight:800;font-size:30px;color:{INK}">(512) 000-0000</div></div></body>""")

# Instagram / Facebook story 1080x1920
PAGES["story-template"] = (1080, 1920, f"""<body style="background:{INK};color:{CREAM};padding:120px 90px;display:flex;flex-direction:column;align-items:center;text-align:center">
{inline('atx-badge-primary', 560)}
<div class="o" style="margin-top:80px;font-size:36px;color:{HONEY}">This week's opening</div>
<div class="h" style="font-size:120px;line-height:1.02;margin-top:24px">Got a list?<br><span style="color:{EMBER}">We got you.</span></div>
<div style="margin-top:auto;background:{EMBER};color:{INK};border-radius:999px;padding:30px 70px" class="o"><span style="font-size:40px">Send us your list</span></div></body>""")

# Business card, 3.5x2in at 300dpi = 1050x600, front and back
PAGES["business-card-front"] = (1050, 600, f"""<body style="background:{INK};display:flex;align-items:center;justify-content:center;gap:40px;padding:50px">
{inline('atx-badge-primary', 380)}
<div style="color:{CREAM}"><div class="h" style="font-size:52px;line-height:1.02"><span style="color:{EMBER}">ATX</span> TOTAL<br>PROPERTIES</div>
<div style="height:5px;background:{HONEY};margin:22px 0 18px"></div>
<div class="o" style="font-size:24px">Your honey-do list, done.</div></div></body>""")
PAGES["business-card-back"] = (1050, 600, f"""<body style="background:{CREAM};color:{INK};padding:70px 80px;display:flex;flex-direction:column;justify-content:space-between">
<div><div class="h" style="font-size:58px">Brandon</div><div class="o" style="font-size:24px;color:{EMBER};margin-top:8px">Owner, Lead Handyman</div></div>
<div style="font-size:30px;line-height:1.6;font-weight:600">(512) 000-0000<br>hello@atxtotalproperties.com<br>atxtotalproperties.com</div>
<div style="display:flex;justify-content:space-between;align-items:end"><div class="o" style="font-size:20px;color:{FLANNEL}">Austin, TX and surrounding areas</div>{inline('atx-icon-mark-plain', 90)}</div></body>""")

# Yard sign / truck magnet 24x18 proportion
PAGES["yard-sign"] = (2400, 1800, f"""<body style="background:{INK};color:{CREAM};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:50px;text-align:center">
{inline('atx-badge-primary', 760)}
<div class="h" style="font-size:150px;line-height:1">Honey-do list? <span style="color:{EMBER}">Done.</span></div>
<div style="font-family:Inter;font-weight:800;font-size:140px;color:{HONEY}">(512) 000-0000</div></body>""")

for name, (w, h, body) in PAGES.items():
    with open(f"kit/html/{name}.html", "w") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS % (w, h)}</style></head>{body}</html>")
print("pages:", len(PAGES))
