"""Carrossel IG 24/11/2026 — newsjacking: recorde de raios em MT -> proteção elétrica da casa."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import page, render_pngs, logo, symbol, icon, OR, OR2, GR, CI, GE, BR

W, H = 1080, 1350
OUT = sys.argv[1] if len(sys.argv) > 1 else "out_raios"
TOT = 7

BOLT = ('<svg viewBox="0 0 100 160" xmlns="http://www.w3.org/2000/svg" style="{st}">'
        '<path d="M58 0 L14 92 H46 L32 160 L88 58 H56 L74 0 Z" fill="{c}"/></svg>')

CSS = """
.night{background:radial-gradient(120% 80% at 80% 0%,#3a3f47 0%,#252A31 45%,#171a1f 100%);color:#fff}
.foot{position:absolute;left:80px;right:80px;bottom:64px;display:flex;justify-content:space-between;align-items:center}
.pg{font-family:'PJS';font-weight:700;font-size:28px}
.body{font-size:46px;line-height:1.36;font-weight:500}
.big{font-family:'PJS';font-weight:800;letter-spacing:-.05em;line-height:.86}
.row{display:flex;gap:30px;align-items:flex-start}
.row svg{flex-shrink:0;margin-top:2px}
.row b{font-weight:700}
.card{background:#fff;border-radius:36px;padding:56px 56px;box-shadow:0 30px 70px rgba(0,0,0,.12)}
.box{width:62px;height:62px;border:5px solid #252A31;border-radius:14px;flex-shrink:0}
.src{font-size:26px;font-weight:600}
.pn{margin-left:-.06em}
.label{font-family:'PJS';font-weight:800;font-size:30px;letter-spacing:.08em;text-transform:uppercase;color:#F47B20}
"""

def foot(n, dark=False, mono=None):
    c = "rgba(255,255,255,.55)" if dark else CI
    if mono: c = "rgba(255,255,255,.8)"
    arrow = " →" if n < TOT else ""
    return f'<div class="foot">{logo(34, dark=dark, mono=mono)}<span class="pg" style="color:{c}">{n}/{TOT}{arrow}</span></div>'

def bolt(w, c=OR, extra=""):
    return BOLT.format(c=c, st=f"width:{w}px;{extra}")

def s1():
    return f"""<div class="c night" style="padding:96px 80px">
  {bolt(220, OR, "position:absolute;right:70px;top:110px;opacity:.95;filter:drop-shadow(0 0 60px rgba(244,123,32,.55))")}
  <div class="chip" style="background:rgba(255,255,255,.1);color:#fff;align-self:flex-start">Temporada de temporal no MT</div>
  <div style="margin-top:120px">
    <div class="big" style="font-size:250px">+3 mi</div>
    <div class="h" style="font-size:74px;margin-top:26px">de raios em Mato Grosso<br>só em <span class="o">outubro.</span></div>
  </div>
  <div class="h" style="font-size:66px;margin-top:110px;color:rgba(255,255,255,.92)">Sua casa tá pronta<br>pro próximo <span class="o">temporal?</span></div>
  <div class="src" style="margin-top:36px;color:rgba(255,255,255,.5)">Fonte: Gazeta Digital, 17/11/2026</div>
  {foot(1, True)}
</div>"""

def s2():
    items = ["Geladeira", "TV", "Roteador", "Computador", "Carregador"]
    chips = "".join(f'<span class="chip" style="background:{GR};color:#fff;font-size:34px">{i}</span>' for i in items)
    return f"""<div class="c light" style="padding:80px 80px 170px;justify-content:center">
  <div class="label">O que pouca gente sabe</div>
  <div class="h" style="font-size:96px;margin-top:30px">O raio não precisa<br>cair na sua casa<br>pra dar <span class="o">prejuízo.</span></div>
  <div class="body" style="margin-top:56px;color:#3a414b">Uma descarga perto da rede pode gerar um <b>surto elétrico</b> que chega pela fiação e queima o que estiver ligado na tomada.</div>
  <div style="display:flex;flex-wrap:wrap;gap:16px;margin-top:56px">{chips}</div>
  {foot(2)}
</div>"""

def s3():
    rows = [("plug", "<b>Tire da tomada</b> os aparelhos eletrônicos enquanto houver raios."),
            ("warn", "<b>Fique longe</b> de postes, cercas e estruturas metálicas."),
            ("bolt", "<b>Fio caído no chão:</b> não toque. Chame a distribuidora de energia.")]
    r = "".join(f'<div class="row body" style="color:#fff">{icon(i, 76, OR, 2)}<div>{t}</div></div>' for i, t in rows)
    return f"""<div class="c night" style="padding:80px 80px 170px;justify-content:center">
  <div class="label">Durante o temporal</div>
  <div class="h" style="font-size:96px;margin-top:30px">3 cuidados<br>na <span class="o">hora H.</span></div>
  <div style="display:flex;flex-direction:column;gap:54px;margin-top:80px">{r}</div>
  <div class="src" style="margin-top:70px;color:rgba(255,255,255,.5)">Recomendações da Defesa Civil de MT</div>
  {foot(3, True)}
</div>"""

def s4():
    return f"""<div class="c" style="background:#fff;padding:80px 80px 170px;justify-content:center">
  <div class="label">Antes do próximo · 1</div>
  <div class="h" style="font-size:100px;margin-top:30px">Pergunte ao<br>eletricista sobre<br>o <span class="o">DPS.</span></div>
  <div style="display:flex;gap:40px;align-items:center;margin-top:70px">
    <div style="background:{OR};color:#fff;border-radius:28px;padding:34px 40px;transform:rotate(-4deg)" class="h"><span style="font-size:86px">DPS</span></div>
    <div class="body" style="font-size:40px;color:{CI}">Dispositivo de<br>Proteção contra Surtos</div>
  </div>
  <div class="body" style="margin-top:64px;color:#3a414b">Fica no quadro de energia e ajuda a proteger a instalação e os aparelhos contra surtos. Se a sua casa precisa e qual modelo usar, <b>quem avalia é o eletricista.</b></div>
  {foot(4)}
</div>"""

def s5():
    return f"""<div class="c light" style="padding:80px 80px 170px;justify-content:center">
  <div class="label">Antes do próximo · 2</div>
  <div class="h" style="font-size:94px;margin-top:30px">Tomada de 3 furos<br>não é sinônimo de<br><span class="o">aterramento.</span></div>
  <div style="display:flex;justify-content:center;margin-top:70px">
    <div style="width:300px;height:300px;border-radius:60px;background:#fff;box-shadow:0 24px 60px rgba(0,0,0,.1);position:relative">
      <div style="position:absolute;left:78px;top:150px;width:40px;height:40px;border-radius:50%;background:{GR}"></div>
      <div style="position:absolute;right:78px;top:150px;width:40px;height:40px;border-radius:50%;background:{GR}"></div>
      <div style="position:absolute;left:130px;top:70px;width:40px;height:40px;border-radius:50%;background:{OR};box-shadow:0 0 0 12px rgba(244,123,32,.2)"></div>
    </div>
  </div>
  <div class="body" style="margin-top:70px;color:#3a414b">O furo do meio só protege se tiver <b>fio terra ligado de verdade</b>. E o DPS também depende de um bom aterramento. Peça pro eletricista conferir.</div>
  {foot(5)}
</div>"""

def s6():
    items = ["Revisar o quadro e os disjuntores", "Avaliar a instalação de DPS", "Conferir o aterramento",
             "Ver tomadas e fios com desgaste"]
    rows = "".join(f'<div class="row" style="align-items:center;gap:34px"><div class="box"></div>'
                   f'<div class="h" style="font-size:50px;letter-spacing:-.02em;line-height:1.12">{t}</div></div>' for t in items)
    return f"""<div class="c orange" style="padding:80px 80px 170px;justify-content:center">
  <div class="h" style="font-size:92px">Tira print<br>e manda pro<br><span style="color:{GR}">eletricista.</span></div>
  <div class="card" style="margin-top:70px;color:{GR}">
    <div class="label" style="margin-bottom:40px">Revisão pós-temporal</div>
    <div style="display:flex;flex-direction:column;gap:42px">{rows}</div>
  </div>
  {foot(6, True, "#fff")}
</div>"""

def s7():
    cities = ("Cuiabá · Várzea Grande · Rondonópolis · Sinop · Tangará da Serra · Sorriso · Nova Mutum · "
              "Lucas do Rio Verde · Primavera do Leste · Barra do Garças · Cáceres")
    return f"""<div class="c night" style="padding:110px 80px">
  <div>{symbol(110)}</div>
  <div class="h" style="font-size:80px;margin-top:46px">Publique <span class="o">“revisão elétrica”</span> no TRAMPIN e receba propostas de eletricistas da sua cidade.</div>
  <div class="body" style="margin-top:40px;color:rgba(255,255,255,.82);font-size:42px">Eletricista: tem cliente procurando você. Cadastro <b style="color:#fff">grátis</b> pra quem contrata e pra quem trabalha.</div>
  <div style="margin-top:40px;font-size:27px;line-height:1.5;color:rgba(255,255,255,.6);font-weight:600">{cities}</div>
  <div style="position:absolute;left:80px;right:80px;bottom:70px;display:flex;justify-content:space-between;align-items:center">
    <div style="background:{OR};color:#fff;border-radius:999px;padding:24px 44px;font-family:'PJS';font-weight:800;font-size:44px">trampin.com.br</div>
    <div class="h" style="font-size:34px;text-align:right;line-height:1.2;letter-spacing:-.02em">Quem faz bem,<br><span class="o">aparece.</span></div>
  </div>
</div>"""

def fixp(h):
    return re.sub(r"(?<=[A-Za-zÀ-ú>])([.?!,])(?=\s|<|$)", r'<span class="pn">\1</span>', h)

slides = [s1(), s2(), s3(), s4(), s5(), s6(), s7()]
render_pngs([(f"raios_ig_{i+1}.png", page(fixp(s), W, H, CSS), W, H) for i, s in enumerate(slides)], OUT)
print("ok", OUT)
