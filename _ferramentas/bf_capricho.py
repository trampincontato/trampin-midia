"""Carrossel IG 26/11/2026 — véspera da Black Friday: opinião "tudo com desconto, menos o capricho"."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kit import page, render_pngs, logo, icon, OR, OR2, GR, CI, GE, BR

W, H = 1080, 1350
OUT = sys.argv[1] if len(sys.argv) > 1 else "out_bfcap"
TOT = 7

CSS = """
.blk{background:#121418;color:#fff}
.foot{position:absolute;left:80px;right:80px;bottom:64px;display:flex;justify-content:space-between;align-items:center}
.pg{font-family:'PJS';font-weight:700;font-size:28px}
.body{font-size:46px;line-height:1.36;font-weight:500}
.label{font-family:'PJS';font-weight:800;font-size:30px;letter-spacing:.08em;text-transform:uppercase;color:#F47B20}
.tag{position:relative;display:inline-flex;align-items:center;font-family:'PJS';font-weight:800;color:#fff;background:#F47B20;
 clip-path:polygon(14% 0,100% 0,100% 100%,14% 100%,0 50%);padding:.32em .8em .32em 1.25em;letter-spacing:-.02em}
.tag:before{content:"";position:absolute;left:.48em;top:50%;width:.26em;height:.26em;margin-top:-.13em;border-radius:50%;background:#121418}
.tag.w{background:#fff;color:#252A31}
.tag.g{background:#252A31;color:#fff}
.tag.g:before,.tag.w:before{background:#F3F5F7}
.strike{position:relative;display:inline-block;color:rgba(255,255,255,.45)}
.strike:after{content:"";position:absolute;left:-4%;right:-4%;top:52%;height:.09em;background:#F47B20;transform:rotate(-6deg)}
.item{display:flex;align-items:center;gap:26px;font-size:42px;font-weight:600;line-height:1.25}
.dot{flex:none;width:58px;height:58px;border-radius:50%;background:#F47B20;display:flex;align-items:center;justify-content:center}
"""

def foot(n, dark=False, mono=None):
    c = "rgba(255,255,255,.55)" if dark else CI
    if mono: c = "rgba(255,255,255,.85)"
    arrow = " →" if n < TOT else ""
    return f'<div class="foot">{logo(34, dark=dark, mono=mono)}<span class="pg" style="color:{c}">{n}/{TOT}{arrow}</span></div>'

def chk(c=BR):
    return f'<span class="dot">{icon("check", 34, c, 3)}</span>'

def s1():
    return f"""<div class="c blk" style="padding:96px 80px 170px">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <span class="tag" style="font-size:34px">Black Friday é amanhã</span>
    <span class="label" style="color:rgba(255,255,255,.55)">Opinião</span>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center">
    <div class="h" style="font-size:128px">Tudo com<br><span class="strike">desconto.</span></div>
    <div class="h" style="font-size:128px;margin-top:40px">Menos o<br><span class="o">capricho.</span></div>
    <div style="margin-top:60px;font-size:42px;line-height:1.38;color:rgba(255,255,255,.78);font-weight:600;max-width:860px">O preço de um bom profissional tem coisa que você não vê. Arrasta pro lado <span class="o">→</span></div>
  </div>
  {foot(1, True)}
</div>"""

def s2():
    return f"""<div class="c" style="background:#fff;padding:80px 80px 170px;justify-content:center">
  <div class="label">Quando chega a proposta</div>
  <div class="h" style="font-size:96px;margin-top:30px">Você vê<br>um <span class="o">número.</span></div>
  <div style="margin:80px 0 80px -10px"><span class="tag g" style="font-size:150px;transform:rotate(-5deg)">R$ ???</span></div>
  <div class="body" style="color:#3a414b">Mas dentro dele vem muita coisa que não aparece na conta. E é isso que separa o serviço que dura do serviço que tem que ser <b>refeito.</b></div>
  {foot(2)}
</div>"""

def s3():
    its = ["Os anos aprendendo o ofício", "Ferramenta própria (e da boa)", "A ida até a sua casa, no calorão de MT",
           "EPI e cuidado com a segurança", "Saber o que <b>não</b> fazer", "Deixar tudo em ordem no final"]
    rows = "".join(f'<div class="item">{chk()}<div>{t}</div></div>' for t in its)
    return f"""<div class="c light" style="padding:80px 80px 170px;justify-content:center">
  <div class="label">O que vem junto no preço</div>
  <div class="h" style="font-size:88px;margin-top:26px">O que você<br>não <span class="o">vê.</span></div>
  <div style="display:flex;flex-direction:column;gap:34px;margin-top:62px">{rows}</div>
  {foot(3)}
</div>"""

def s4():
    cmp = ["Mão de obra", "Materiais", "Prazo", "Fotos de trabalhos", "Avaliações"]
    chips = "".join(f'<span class="tag w" style="font-size:36px">{c}</span>' for c in cmp)
    return f"""<div class="c blk" style="padding:80px 80px 170px;justify-content:center">
  <div class="label">Pra quem contrata</div>
  <div class="h" style="font-size:92px;margin-top:30px">Pechinchar<br>faz parte.</div>
  <div class="h" style="font-size:92px;margin-top:22px;color:rgba(255,255,255,.55)">Escolher só pelo<br>menor número, <span class="o">não.</span></div>
  <div class="body" style="margin-top:60px;color:rgba(255,255,255,.85)">Antes de decidir, compare a proposta inteira:</div>
  <div style="display:flex;flex-wrap:wrap;gap:22px 18px;margin-top:34px">{chips}</div>
  {foot(4, True)}
</div>"""

def s5():
    its = ["Fotos do que você já fez no perfil", "Proposta com mão de obra, materiais e prazo",
           "Cumpriu o combinado? Pede pro cliente avaliar"]
    rows = "".join(f'<div class="item" style="color:{GR}">{chk()}<div>{t}</div></div>' for t in its)
    return f"""<div class="c" style="background:#fff;padding:80px 80px 170px;justify-content:center">
  <div class="label">Pra quem faz o trampo</div>
  <div class="h" style="font-size:92px;margin-top:30px">Não entra na<br>guerra do preço.</div>
  <div class="h" style="font-size:92px;margin-top:22px">Mostra o <span class="o">porquê</span><br>dele.</div>
  <div style="display:flex;flex-direction:column;gap:34px;margin-top:66px">{rows}</div>
  {foot(5)}
</div>"""

def s6():
    return f"""<div class="c orange" style="padding:96px 80px 170px;justify-content:center">
  <div class="h" style="font-size:136px;color:#fff">Promoção<br>acaba.</div>
  <div class="h" style="font-size:136px;margin-top:40px;color:{GR}">Serviço bem<br>feito fica.</div>
  <div style="margin-top:70px;font-size:44px;line-height:1.38;color:#fff;font-weight:600;max-width:880px">Na sexta, aproveita o desconto. Na obra, escolhe quem faz bem.</div>
  {foot(6, mono=BR)}
</div>"""

def s7():
    its = ["Quem contrata publica o pedido e compara propostas completas",
           "Quem faz mostra fotos dos serviços e a nota dos clientes",
           "Grátis pros dois lados"]
    rows = "".join(f'<div class="item" style="font-size:38px">{chk()}<div>{t}</div></div>' for t in its)
    cities = ("Cuiabá · Várzea Grande · Rondonópolis · Sinop · Tangará da Serra · Sorriso · Nova Mutum · "
              "Lucas do Rio Verde · Primavera do Leste · Barra do Garças · Cáceres")
    return f"""<div class="c blk" style="padding:80px 80px 170px;justify-content:center">
  <div class="h" style="font-size:90px">No TRAMPIN,<br>quem faz bem,<br><span class="o">aparece.</span></div>
  <div style="display:flex;flex-direction:column;gap:30px;margin-top:56px">{rows}</div>
  <div style="margin-top:56px"><span class="tag" style="font-size:54px">trampin.com.br</span></div>
  <div style="margin-top:44px;font-size:28px;line-height:1.45;color:rgba(255,255,255,.6);font-weight:600">{cities}</div>
  {foot(7, True)}
</div>"""

if __name__ == "__main__":
    slides = [s1, s2, s3, s4, s5, s6, s7]
    import re
    def fixdots(html):
        def rep(m):
            return re.sub(r'\.(?=<|$)', '<span style="margin-left:-.11em">.</span>', m.group(0))
        return re.sub(r'<div class="h"[^>]*>.*?</div>', rep, html, flags=re.S)
    items = [(f"bfcap_ig_{i}.png", page(fixdots(f()), W, H, CSS), W, H) for i, f in enumerate(slides, 1)]
    render_pngs(items, OUT)
    print(len(items), "ok")
