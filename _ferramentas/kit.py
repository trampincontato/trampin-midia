"""Design kit TRAMPIN: HTML building blocks + renderer."""
import base64, pathlib
ROOT = pathlib.Path(__file__).parent
F = ROOT / "fonts"

def _font(name, w):
    b = base64.b64encode((F / name).read_bytes()).decode()
    return f"@font-face{{font-family:'PJS';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"

FONTS = (_font("plus-jakarta-sans-latin-800-normal.woff2", 800)
         + _font("plus-jakarta-sans-latin-700-normal.woff2", 700))

OR, OR2, GR, CI, GE, BR = "#F47B20", "#D96113", "#252A31", "#737B86", "#F3F5F7", "#FFFFFF"

def symbol(size=64, color=OR):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
            f'<path d="M9 13H51" stroke="{color}" stroke-width="11" stroke-linecap="round"/>'
            f'<path d="M22 13V43L30 51L52 29" stroke="{color}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def logo(size=44, dark=False, mono=None):
    tc = BR if dark else GR
    ic = OR if mono is None else mono
    tc = tc if mono is None else mono
    return (f'<div class="logo" style="font-size:{size}px">{symbol(int(size*1.15), ic)}'
            f'<span><span style="color:{tc}">TRAMP</span><span style="color:{ic}">IN</span></span></div>')

# simple line icons (24x24 grid)
ICONS = {
 "drop": '<path d="M12 3C9 7.5 6 10.6 6 14a6 6 0 0 0 12 0c0-3.4-3-6.5-6-11z"/>',
 "crack": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3l-2 5 3 3-2 4 2 3-1 3"/>',
 "cloud": '<path d="M7 17a4 4 0 0 1-.5-8A5.5 5.5 0 0 1 17 8a4.5 4.5 0 0 1 0 9z"/><path d="M8 20l1-2M12 21l1-2M16 20l1-2"/>',
 "meter": '<circle cx="12" cy="12" r="8"/><path d="M12 12l4-3"/><path d="M12 5v1.5M5 12h1.5M17.5 12H19"/>',
 "plug": '<rect x="5" y="3" width="14" height="18" rx="3"/><circle cx="9.5" cy="11" r="1.2"/><circle cx="14.5" cy="11" r="1.2"/><path d="M12 15v2"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "doc": '<path d="M6 2h9l4 4v16H6z"/><path d="M15 2v4h4M9 11h7M9 15h7M9 19h4"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 "camera": '<path d="M4 7h4l2-2h4l2 2h4v12H4z"/><circle cx="12" cy="13" r="3.5"/>',
 "split": '<path d="M12 3v18"/><rect x="3" y="6" width="6" height="12" rx="1.5"/><rect x="15" y="6" width="6" height="12" rx="1.5"/>',
 "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "house": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
 "phone": '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10 18h4"/>',
 "fire": '<path d="M12 22c4 0 7-3 7-7 0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-2-2-4-2 2-5 5-5 8 0 4 3 7 7 7z"/>',
 "tool": '<path d="M14.5 5.5a4 4 0 0 0 5 5l-9 9a2.1 2.1 0 0 1-3-3l9-9a4 4 0 0 0-2-2z"/>',
 "warn": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.5"/>',
 "pin": '<path d="M12 22s7-7.5 7-13a7 7 0 0 0-14 0c0 5.5 7 13 7 13z"/><circle cx="12" cy="9" r="2.5"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.5a5 5 0 0 1 5.5 5"/>',
}

def icon(name, size=96, color=OR, sw=2):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')

BASE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:%(W)dpx;height:%(H)dpx;overflow:hidden}
body{font-family:'Inter',sans-serif;font-weight:500;-webkit-font-smoothing:antialiased;color:#252A31}
.c{position:relative;width:%(W)dpx;height:%(H)dpx;overflow:hidden;display:flex;flex-direction:column}
.h{font-family:'PJS',sans-serif;font-weight:800;letter-spacing:-0.035em;line-height:1.02}
.o{color:#F47B20}
.logo{display:flex;align-items:center;gap:.28em;font-family:'PJS';font-weight:800;letter-spacing:-0.03em;line-height:1}
.chip{display:inline-flex;align-items:center;font-family:'PJS';font-weight:700;border-radius:999px;padding:.45em 1em;font-size:30px}
.dark{background:#252A31;color:#fff}
.light{background:#F3F5F7}
.orange{background:#F47B20;color:#fff}
.grain:after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.06;
 background-image:radial-gradient(#000 1px,transparent 1px);background-size:6px 6px}
"""

def page(body, W, H, extra_css=""):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}{BASE_CSS % {'W': W, 'H': H}}{extra_css}</style></head>"
            f"<body>{body}</body></html>")

def render_pngs(items, outdir):
    """items: list of (filename, html, W, H)"""
    from playwright.sync_api import sync_playwright
    outdir = pathlib.Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for fn, html, W, H in items:
            pg = b.new_page(viewport={"width": W, "height": H})
            pg.set_content(html, wait_until="load")
            pg.wait_for_timeout(150)
            pg.screenshot(path=str(outdir / fn), type="png")
            pg.close()
        b.close()
