"""Service and brand icon set. 64x64 grid, rounded line style, one orange accent."""
import os

INK, EMBER, CREAM = "#161616", "#E2692B", "#F6EFE4"

# Each icon: list of (kind, svg_fragment). "L" = line in main color, "A" = accent fill/stroke.
ICONS = {
    "honey-do-list": [
        ("L", '<rect x="14" y="10" width="36" height="46" rx="4"/>'),
        ("L", '<path d="M24 10v-2h16v2"/>'),
        ("A", '<path d="M20 24l3 3 6-6M20 37l3 3 6-6"/>'),
        ("L", '<path d="M34 25h10M34 38h10M20 49h24"/>')],
    "house-check": [
        ("L", '<path d="M8 30L32 9l24 21M14 25v29h36V25"/>'),
        ("A", '<path d="M23 38l6 6 12-12"/>')],
    "handyman-tools": [
        ("L", '<path d="M40 10a10 10 0 0 0-9 14L11 44a4 4 0 0 0 6 6l20-20a10 10 0 0 0 14-9l-6 6-6-2-2-6z"/>'),
        ("A", '<path d="M12 12l6-2 14 14-4 4-14-14zM36 36l14 14"/>')],
    "drill": [
        ("L", '<path d="M10 16h30v14H10zM40 20h8M48 23h8M22 30l-4 22h12l2-22"/>'),
        ("A", '<path d="M18 52h12"/>')],
    "hammer": [
        ("L", '<path d="M30 26L12 50a4 4 0 0 0 6 4l18-22"/>'),
        ("A", '<path d="M24 18l10-8 14 4 6 8-10 2-6 8-8-6z"/>')],
    "paint-roller": [
        ("A", '<rect x="10" y="10" width="38" height="14" rx="3"/>'),
        ("L", '<path d="M48 17h6v14H32v8M28 39h8v16h-8z"/>')],
    "plumbing": [
        ("L", '<path d="M10 22h18v-6h12v6h4a8 8 0 0 1 8 8v4h-8v-4H40v6H28v-6H10z"/>'),
        ("A", '<path d="M48 44c0 0-5 6-5 9a5 5 0 0 0 10 0c0-3-5-9-5-9z"/>')],
    "electrical": [
        ("L", '<path d="M22 40a14 14 0 1 1 20 0c-2 2-3 4-3 8H25c0-4-1-6-3-8zM25 53h14M28 58h8"/>'),
        ("A", '<path d="M33 24l-5 9h8l-5 9"/>')],
    "ceiling-fan": [
        ("L", '<path d="M32 6v16M8 30c6-6 16-6 18 0M56 30c-6-6-16-6-18 0M32 40c4 8 2 14-2 16"/>'),
        ("A", '<circle cx="32" cy="30" r="6"/>')],
    "tv-mounting": [
        ("L", '<rect x="8" y="12" width="48" height="30" rx="3"/>'),
        ("L", '<path d="M24 52h16M32 42v10"/>'),
        ("A", '<path d="M16 20h10M16 26h6"/>')],
    "furniture-assembly": [
        ("L", '<path d="M10 22l22-10 22 10v22L32 54 10 44zM10 22l22 10 22-10M32 32v22"/>'),
        ("A", '<path d="M40 8l10 4"/>')],
    "door-lock": [
        ("L", '<path d="M16 56V10h32v46M10 56h44"/>'),
        ("A", '<circle cx="40" cy="34" r="3"/>')],
    "drywall-repair": [
        ("L", '<rect x="8" y="10" width="48" height="44" rx="2"/>'),
        ("A", '<rect x="22" y="24" width="20" height="16" rx="1"/>'),
        ("L", '<path d="M44 46l10 6"/>')],
    "yard-work": [
        ("L", '<path d="M32 58V30M32 36c-10 0-16-8-16-18 10 0 16 8 16 18zM32 42c8 0 14-6 14-14-8 0-14 6-14 14z"/>'),
        ("A", '<path d="M10 58h44"/>')],
    "pressure-washing": [
        ("L", '<path d="M8 40h18l6-6h8v12h-8l-6-6M18 40v12h10"/>'),
        ("A", '<path d="M44 34l12-8M44 40h14M44 46l12 8"/>')],
    "fence-deck": [
        ("L", '<path d="M12 56V18l5-6 5 6v38M29 56V18l5-6 5 6v38M46 56V18l5-6 5 6v38"/>'),
        ("A", '<path d="M8 28h52M8 44h52"/>')],
    "gutter-cleaning": [
        ("L", '<path d="M6 18h52v8a4 4 0 0 1-4 4H10a4 4 0 0 1-4-4zM46 30v20a4 4 0 0 0 4 4h6"/>'),
        ("A", '<path d="M20 40c0 0-4 5-4 7a4 4 0 0 0 8 0c0-2-4-7-4-7z"/>')],
    "caulk-seal": [
        ("L", '<path d="M10 24h30v16H10zM40 28h8l10 4-10 4h-8"/>'),
        ("A", '<path d="M14 50c6-4 12 4 18 0s12 4 18 0"/>')],
    "smoke-detector": [
        ("L", '<path d="M10 14h44M14 14v6a18 6 0 0 0 36 0v-6"/>'),
        ("A", '<path d="M24 34c0 6 4 6 4 12M32 34c0 6 4 6 4 12M40 34c0 6 4 6 4 12"/>')],
    "move-in-out": [
        ("L", '<path d="M6 20h30v26H6zM36 28h12l10 10v8H36"/>'),
        ("A", '<circle cx="16" cy="48" r="5"/><circle cx="46" cy="48" r="5"/>')],
    "rental-turnover": [
        ("L", '<path d="M8 30L32 10l24 20M14 26v28h36V26"/>'),
        ("A", '<path d="M38 36a8 8 0 1 1-2-6M38 28v6h-6"/>')],
    "calendar": [
        ("L", '<rect x="8" y="12" width="48" height="44" rx="4"/>'),
        ("L", '<path d="M8 24h48M20 6v10M44 6v10"/>'),
        ("A", '<path d="M22 40l6 6 14-14"/>')],
    "phone": [
        ("L", '<path d="M18 8l10 2 4 12-6 4c3 7 8 12 14 14l4-6 12 4 2 10c-2 4-6 6-10 6C26 54 10 38 10 16c0-4 4-8 8-8z"/>'),
        ("A", '<path d="M38 10a16 16 0 0 1 16 16M38 18a8 8 0 0 1 8 8"/>')],
    "free-quote": [
        ("L", '<path d="M10 34V10h24l22 22-24 24z"/>'),
        ("A", '<circle cx="21" cy="21" r="4"/>')],
    "five-star-review": [
        ("A", '<path d="M32 8l7 15 16 2-12 11 3 16-14-8-14 8 3-16L9 25l16-2z"/>')],
    "licensed-insured": [
        ("L", '<path d="M32 6l22 8v16c0 14-10 24-22 28C20 54 10 44 10 30V14z"/>'),
        ("A", '<path d="M22 32l7 7 14-14"/>')],
    "on-time": [
        ("L", '<circle cx="32" cy="34" r="22"/>'),
        ("A", '<path d="M32 22v12l8 6"/>'),
        ("L", '<path d="M26 6h12"/>')],
    "local-service": [
        ("L", '<path d="M32 58S14 38 14 24a18 18 0 0 1 36 0c0 14-18 34-18 34z"/>'),
        ("A", '<circle cx="32" cy="24" r="6"/>')],
    "tile": [
        ("L", '<rect x="10" y="10" width="44" height="44" rx="3"/><path d="M32 10v44M10 32h44"/>'),
        ("A", '<rect x="35" y="13" width="16" height="16" rx="1"/>')],
    "toilet": [
        ("L", '<path d="M16 8h18v18H16zM12 30h40c0 10-8 16-16 16h-8v10H18V44c-4-3-6-8-6-14z"/>'),
        ("A", '<path d="M22 14h6"/>')],
    "shower": [
        ("L", '<path d="M14 58V16a8 8 0 0 1 16 0v2M24 18h14l-2 8H26z"/>'),
        ("A", '<path d="M28 34v4M34 34v4M40 34v4M30 44v4M38 44v4"/>')],
    "garage-door": [
        ("L", '<path d="M6 26L32 8l26 18M12 22v34h40V22"/>'),
        ("A", '<path d="M18 32h28M18 40h28M18 48h28"/>')],
    "picture-hanging": [
        ("L", '<rect x="12" y="22" width="40" height="32" rx="2"/><path d="M20 22l12-12 12 12"/>'),
        ("A", '<path d="M18 48l10-12 8 8 6-6 6 10z"/><circle cx="32" cy="10" r="3"/>')],
    "shelving": [
        ("L", '<path d="M10 22h44M10 42h44M14 22v6M50 22v6M14 42v6M50 42v6"/>'),
        ("A", '<rect x="16" y="10" width="6" height="12"/><rect x="24" y="12" width="6" height="10"/><rect x="38" y="32" width="12" height="10"/>')],
    "cabinet": [
        ("L", '<rect x="10" y="12" width="44" height="42" rx="2"/><path d="M32 12v42"/>'),
        ("A", '<path d="M27 30v6M37 30v6"/>')],
    "vent-cleaning": [
        ("L", '<rect x="10" y="12" width="44" height="40" rx="3"/>'),
        ("A", '<path d="M18 22h28M18 30h28M18 38h28M18 46h28"/>')],
    "bed-assembly": [
        ("L", '<path d="M8 50V16M8 36h48v14M56 36v-8a6 6 0 0 0-6-6H26v14"/>'),
        ("A", '<rect x="12" y="26" width="10" height="8" rx="3"/>')],
}


def icon_svg(parts, line, accent, size=64):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="{size}" height="{size}" '
           'fill="none" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">']
    for kind, frag in parts:
        c = line if kind == "L" else accent
        filled = kind == "A" and any(t in frag for t in ("<rect", "<circle", "z\"/>"))
        if filled and "five-star" not in frag:
            out.append(f'<g stroke="{c}" fill="{c}" fill-opacity="0.9">{frag}</g>')
        else:
            out.append(f'<g stroke="{c}">{frag}</g>')
    out.append("</svg>\n")
    return "".join(out)


VARIANTS = {"color": (INK, EMBER), "white": (CREAM, EMBER), "black": (INK, INK)}

if __name__ == "__main__":
    for v, (line, accent) in VARIANTS.items():
        d = f"icons/svg-{v}"
        os.makedirs(d, exist_ok=True)
        for name, parts in ICONS.items():
            with open(f"{d}/{name}.svg", "w") as f:
                f.write(icon_svg(parts, line, accent))
    print(len(ICONS), "icons x", len(VARIANTS), "variants")
