"""Carrossel IG 21/11/2026 — Black Friday de material de obra (estilo etiqueta de preço)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import page, render_pngs, logo, symbol, icon, OR, OR2, GR, CI, GE, BR

W, H = 1080, 1350
OUT = sys.argv[1] if len(sys.argv) > 1 else "out_bf"

CSS = """
.tag{position:relative;background:#F47B20;color:#fff;border-radius:28px 28px 28px 28px;
 padding:56px 64px 56px 120px;box-shadow:0 24px 60px rgba(0,0,0,.18)}
.tag:before{content:"";position:absolute;left:44px;top:50%;width:34px;height:34px;margin-top:-17px;
 border-radius:50%;background:var(--bg)}
.tag .cord{position:absolute;left:61px;top:50%;width:200px;height:4px;background:var(--cord);
 transform-origin:0 0;transform:rotate(-140deg)}
.num{font-family:'PJS';font-weight:800;font-size:150px;line-height:.9;letter-spacing:-.05em}
.foot{position:absolute;left:80px;right:80px;bottom:64px;display:flex;justify-content:space-between;align-items:center}
.pg{font-family:'PJS';font-weight:700;font-size:28px;color:#737B86}
.strike{text-decoration:line-through;text-decoration-thickness:8px;text-decoration-color:#F47B20}
.body{font-size:44px;line-height:1.35;font-weight:500}
.h .pn,.tag .pn{margin-left:-.06em}
.tag.nohole:before{display:none}
.tag.nohole{padding:30px 54px!important}
.x{display:flex;gap:28px;align-items:flex-start}
.x svg{flex-shrink:0;margin-top:4px}
.x b{font-weight:700}
.dash{border-top:4px dashed rgba(37,42,49,.18);margin:44px 0}
"""

def foot(n, dark=False):
    c = "rgba(255,255,255,.55)" if dark else CI
    return (f'<div class="foot">{logo(34, dark=dark)}'
            f'<span class="pg" style="color:{c}">{n}/7 →</span></div>')

def slide_cover():
    b = f"""<div class="c dark grain" style="--bg:{GR};--cord:rgba(255,255,255,.35);padding:96px 80px">
  <div class="chip" style="background:rgba(255,255,255,.1);color:#fff;align-self:flex-start">Black Friday · 27 de novembro</div>
  <div class="h" style="font-size:112px;margin-top:70px">Vai comprar<br>material de obra<br>na <span class="o">promoção?</span></div>
  <div style="margin-top:150px;transform:rotate(-4deg);align-self:flex-start">
    <div class="tag">
      <div class="h" style="font-size:70px">Lê isso antes<br>de passar no caixa.</div>
    </div>
  </div>
  {foot(1, dark=True)}
</div>"""
    return b

def slide_problem():
    b = f"""<div class="c light" style="padding:110px 80px">
  <div class="h" style="font-size:104px">Promoção boa<br>é a que você <span class="o">usa.</span></div>
  <div class="dash"></div>
  <div style="display:flex;flex-direction:column;gap:46px;margin-top:10px">
    <div class="x body">{icon("warn",64,OR,2.2)}<div><b>Piso que sobrou</b>, encostado na garagem</div></div>
    <div class="x body">{icon("warn",64,OR,2.2)}<div><b>Tinta da cor errada</b>, porque ninguém testou antes</div></div>
    <div class="x body">{icon("warn",64,OR,2.2)}<div><b>Cimento empedrado</b>, esperando a obra começar</div></div>
  </div>
  <div class="h" style="font-size:58px;margin-top:110px;color:{CI}">Aí o desconto<br>vira <span style="color:{GR}">prejuízo.</span></div>
  {foot(2)}
</div>"""
    return b

def slide_tip(n, k, title, text, ic, bg="light"):
    dark = bg == "dark"
    bgc = GR if dark else (BR if bg == "white" else GE)
    tc = "#fff" if dark else GR
    sub = "rgba(255,255,255,.78)" if dark else "#3a414b"
    return f"""<div class="c" style="background:{bgc};color:{tc};--bg:{bgc};--cord:rgba(0,0,0,0);padding:80px 80px 180px;justify-content:center">
  <div style="display:flex;align-items:center;gap:40px">
    <div class="tag nohole" style="transform:rotate(-6deg)">
      <div class="num">{k}</div></div>
    <div>{icon(ic, 120, OR, 1.8)}</div>
  </div>
  <div class="h" style="font-size:100px;margin-top:90px">{title}</div>
  <div class="body" style="margin-top:50px;color:{sub};font-size:50px">{text}</div>
  {foot(n, dark=dark)}
</div>"""

def slide_cta():
    cities = "Cuiabá · Várzea Grande · Rondonópolis · Sinop · Tangará da Serra · Sorriso · Nova Mutum · Lucas do Rio Verde · Primavera do Leste · Barra do Garças · Cáceres"
    return f"""<div class="c orange" style="padding:110px 80px;--bg:{OR}">
  <div>{symbol(120, "#fff")}</div>
  <div class="h" style="font-size:86px;margin-top:50px">No TRAMPIN, a proposta já chega com <span style="color:{GR}">mão de obra, materiais e prazo.</span></div>
  <div class="body" style="margin-top:44px;color:#fff">Publique seu pedido e receba propostas de profissionais da sua cidade. Grátis pra quem contrata e pra quem trabalha.</div>
  <div style="margin-top:44px;font-size:27px;line-height:1.5;color:rgba(255,255,255,.85);font-weight:600">{cities}</div>
  <div style="position:absolute;left:80px;right:80px;bottom:70px;display:flex;justify-content:space-between;align-items:center">
    <div style="background:#fff;color:{GR};border-radius:999px;padding:24px 44px;font-family:'PJS';font-weight:800;font-size:44px">trampin.com.br</div>
    <div class="h" style="font-size:34px;text-align:right;line-height:1.2;letter-spacing:-.02em">Quem faz bem,<br>aparece.</div>
  </div>
</div>"""

slides = [
    slide_cover(),
    slide_problem(),
    slide_tip(3, "1", 'Peça a lista<br>ao <span class="o">profissional.</span>',
              "Quem vai executar sabe o tipo certo de material e a quantidade. Feche a lista com ele antes de olhar preço.", "doc", "white"),
    slide_tip(4, "2", 'Confira medida<br>e <span class="o">quantidade.</span>',
              "Metragem da parede, do piso, do telhado. Pergunte ao profissional quanto de sobra ele recomenda para perda e recorte.", "meter", "light"),
    slide_tip(5, "3", 'Olhe validade e<br>onde vai <span class="o">guardar.</span>',
              "Cimento, argamassa e tinta têm prazo de validade. E com a chuva no MT, saco de cimento fica no seco, longe do chão.", "cloud", "dark"),
    slide_tip(6, "4", 'Feche o profissional.<br>Depois <span class="o">compre.</span>',
              "Material parado esperando a obra ocupa espaço e pode estragar. Com data do serviço combinada, a compra fica no ponto.", "clock", "white"),
    slide_cta(),
]

import re as _re
def fixp(h):
    return _re.sub(r"(?<=[A-Za-zÀ-ú>])([.?!,])(?=\s|<|$)", r'<span class="pn">\1</span>', h)
render_pngs([(f"bf_material_ig_{i+1}.png", page(fixp(s), W, H, CSS), W, H) for i, s in enumerate(slides)], OUT)
print("ok", OUT)
