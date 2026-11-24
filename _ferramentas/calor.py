"""Carrossel de fotos TikTok 25/11/2026 — newsjacking: semana de até 38°C em MT -> obra em casa no calorão (respeito cliente x profissional)."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import page, render_pngs, logo, symbol, icon, OR, OR2, GR, CI, GE, BR

W, H = 1080, 1920
OUT = sys.argv[1] if len(sys.argv) > 1 else "out_calor"
TOT = 7
# TikTok safe zone: top 190, right 150, bottom ~400 (legenda + botões)
PAD = "padding:200px 160px 420px 90px"

CSS = """
.heat{background:radial-gradient(110% 70% at 85% 8%,#FFB347 0%,#F47B20 38%,#D96113 75%,#B84E0C 100%);color:#fff}
.night{background:radial-gradient(120% 80% at 80% 0%,#3a3f47 0%,#252A31 45%,#171a1f 100%);color:#fff}
.foot{position:absolute;left:90px;right:160px;bottom:400px;display:flex;justify-content:space-between;align-items:center}
.pg{font-family:'PJS';font-weight:700;font-size:30px}
.body{font-size:48px;line-height:1.36;font-weight:500}
.big{font-family:'PJS';font-weight:800;letter-spacing:-.05em;line-height:.86}
.label{font-family:'PJS';font-weight:800;font-size:32px;letter-spacing:.08em;text-transform:uppercase;color:#F47B20}
.num{font-family:'PJS';font-weight:800;font-size:230px;line-height:.8;color:#F47B20;letter-spacing:-.06em}
.pn{margin-left:-.06em}
.row{display:flex;gap:28px;align-items:flex-start}
.row svg{flex-shrink:0;margin-top:4px}
.src{font-size:28px;font-weight:600}
"""

SUN = ('<svg width="{s}" height="{s}" viewBox="0 0 100 100" style="{st}"><circle cx="50" cy="50" r="22" fill="#FFF3E0"/>'
       + "".join(f'<rect x="47" y="4" width="6" height="16" rx="3" fill="#FFF3E0" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45))
       + "</svg>")

ICX = {
 "bottle": '<path d="M10 2h4v3l1.5 2v13a2 2 0 0 1-2 2h-3a2 2 0 0 1-2-2V7L10 5z"/><path d="M8.5 11h7M8.5 16h7"/>',
 "shade": '<path d="M3 11a9 9 0 0 1 18 0z"/><path d="M12 11v10M9 21h6"/>',
 "sunr": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "door": '<rect x="5" y="2" width="14" height="20" rx="1.5"/><circle cx="15" cy="12" r="1"/>',
 "hat": '<path d="M2 17c3 1.5 17 1.5 20 0"/><path d="M5 16.5V12a7 7 0 0 1 14 0v4.5"/>',
}

def ic(name, size=120, color=OR, sw=1.8):
    p = ICX.get(name)
    if p is None:
        return icon(name, size, color, sw)
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{p}</svg>')

def foot(n, dark=False, mono=None):
    c = "rgba(255,255,255,.6)" if dark else CI
    if mono: c = "rgba(255,255,255,.85)"
    arrow = " →" if n < TOT else ""
    return f'<div class="foot">{logo(36, dark=dark, mono=mono)}<span class="pg" style="color:{c}">{n}/{TOT}{arrow}</span></div>'

def s1():
    sun = SUN.format(s=330, st="position:absolute;right:-60px;top:120px;opacity:.9")
    return f"""<div class="c heat" style="{PAD}">
  {sun}
  <div class="chip" style="background:rgba(37,42,49,.85);color:#fff;align-self:flex-start;font-size:32px">Previsão pra MT essa semana</div>
  <div style="margin-top:110px">
    <div class="big" style="font-size:300px">38°C</div>
    <div class="h" style="font-size:80px;margin-top:40px">e tem obra<br>na sua casa?</div>
  </div>
  <div class="h" style="font-size:66px;margin-top:80px;color:{GR}">4 gestos que o<br>profissional não pede,<br>mas nunca esquece.</div>
  {foot(1, True, "#fff")}
</div>"""

def tip(n, title, body, name, theme="light"):
    dark = theme == "night"
    bc = "rgba(255,255,255,.85)" if dark else "#3a414b"
    tc = "#fff" if dark else GR
    cls = "night" if dark else ("light" if theme == "light" else "")
    bg = "" if theme in ("light", "night") else "background:#fff;"
    return f"""<div class="c {cls}" style="{bg}{PAD};justify-content:center">
  <div style="display:flex;align-items:center;gap:40px;margin-bottom:56px">
    <div class="num">{n}</div>{ic(name, 150)}
  </div>
  <div style="position:absolute;right:120px;bottom:470px;opacity:.09">{ic(name, 520, OR, 1.4)}</div>
  <div class="h" style="font-size:116px;color:{tc};position:relative">{title}</div>
  <div class="body" style="margin-top:56px;color:{bc};font-size:54px;position:relative">{body}</div>
  {foot(int(n)+1, dark)}
</div>"""

def s6():
    rows = [("hat", "<b>Boné ou chapéu</b> com aba e roupa leve de manga longa"),
            ("bottle", "<b>Água sempre por perto</b>, sem esperar a sede"),
            ("sunr", "<b>Protetor solar</b> e pausa na sombra nos horários mais quentes"),
            ("warn", "<b>EPI não sai do corpo</b> por causa do calor")]
    r = "".join(f'<div class="row body" style="color:#fff;font-size:46px">{ic(i, 80, OR, 2)}<div>{t}</div></div>' for i, t in rows)
    return f"""<div class="c night" style="{PAD};justify-content:center">
  <div class="label">E se você é o profissional</div>
  <div class="h" style="font-size:96px;margin-top:30px">Capricho também<br>é chegar <span class="o">inteiro</span><br>em casa.</div>
  <div style="display:flex;flex-direction:column;gap:46px;margin-top:70px">{r}</div>
  {foot(6, True)}
</div>"""

def s7():
    cities = ("Cuiabá · Várzea Grande · Rondonópolis · Sinop · Tangará da Serra · Sorriso · Nova Mutum · "
              "Lucas do Rio Verde · Primavera do Leste · Barra do Garças · Cáceres")
    return f"""<div class="c night" style="{PAD}">
  <div style="margin-top:40px">{symbol(120)}</div>
  <div class="h" style="font-size:86px;margin-top:50px">Respeito de quem<br>contrata por<br><span class="o">quem faz.</span></div>
  <div class="body" style="margin-top:50px;color:rgba(255,255,255,.85);font-size:44px">Precisa de pedreiro, pintor, eletricista ou encanador? Publique seu pedido no TRAMPIN e receba propostas de profissionais da sua cidade.</div>
  <div class="h" style="margin-top:40px;font-size:56px;color:#fff">Grátis pros dois lados.</div>
  <div style="margin-top:36px;font-size:29px;line-height:1.5;color:rgba(255,255,255,.6);font-weight:600">{cities}</div>
  <div style="position:absolute;left:90px;right:160px;bottom:400px;display:flex;justify-content:space-between;align-items:center">
    <div style="background:{OR};color:#fff;border-radius:999px;padding:24px 40px;font-family:'PJS';font-weight:800;font-size:42px">trampin.com.br</div>
    <div class="h" style="font-size:34px;text-align:right;line-height:1.2;letter-spacing:-.02em">Quem faz bem,<br><span class="o">aparece.</span></div>
  </div>
</div>"""

def fixp(h):
    return re.sub(r"(?<=[A-Za-zÀ-ú>])([.?!,])(?=\s|<|$)", r'<span class="pn">\1</span>', h)

slides = [
    s1(),
    tip("1", "Água gelada<br>à vista.", "Uma garrafa gelada e um copo no canto da obra. Ninguém pede. Todo mundo lembra.", "bottle"),
    tip("2", "Um canto<br>na <span class=\"o\">sombra.</span>", "Garagem, varanda ou debaixo da árvore: um lugar pra pausa e pro almoço longe do sol.", "shade", "white"),
    tip("3", "Horário<br>combinado<br>com o sol.", "Telhado, laje e parte externa rendem mais cedinho e no fim da tarde. Combine isso antes de começar.", "sunr"),
    tip("4", "Banheiro<br><span class=\"o\">liberado.</span>", "Parece óbvio, mas muita gente esquece de combinar. É o básico do respeito.", "door", "white"),
    s6(),
    s7(),
]

if __name__ == "__main__":
    render_pngs([(f"calor_tt_{i+1}.png", page(fixp(s), W, H, CSS), W, H) for i, s in enumerate(slides)], OUT)
    from PIL import Image
    for i in range(len(slides)):
        p = pathlib.Path(OUT) / f"calor_tt_{i+1}.png"
        Image.open(p).convert("RGB").save(p.with_suffix(".jpg"), "JPEG", quality=92)
    print("ok", OUT)
