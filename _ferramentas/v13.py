"""22/11/2026 TikTok: 13º salário — a ordem certa pra gastar na casa."""
from video import *

def chip(txt, bg=OR, col="#fff", ic=None):
    i = icon(ic, 44, col, 2.4) if ic else ""
    return (f'<div style="display:inline-flex;align-items:center;gap:14px;background:{bg};color:{col};border-radius:999px;'
            f'padding:16px 32px;font-family:PJS;font-weight:800;font-size:38px">{i}{txt}</div>')

def tag(txt):
    return (f'<span style="display:inline-block;background:#fff;border:3px solid {GR};color:{GR};border-radius:16px;'
            f'padding:10px 22px;font-family:PJS;font-weight:700;font-size:34px;margin:0 14px 14px 0">{txt}</span>')

def bar(k):
    segs = "".join(f'<div style="flex:1;height:14px;border-radius:7px;background:{OR if i < k else "#D5DAE0"}"></div>' for i in range(4))
    return f'<div style="display:flex;gap:12px;width:100%;margin-bottom:70px">{segs}</div>'

def step(a, b, n, lines, sub, ic, tags):
    return sc("light", a, b,
              el(bar(n), a, "fade"),
              el(f'<div style="display:flex;align-items:center;gap:34px"><div class="h" style="font-size:230px;color:{OR};line-height:.8">{n}º</div>{icon(ic,170,OR,1.6)}</div>', a, "pop"),
              el(h(lines, 116, None, 50), a + .25),
              el(f'<div style="font-size:42px;color:{CI};margin-top:26px;font-weight:600">{sub}</div>', a + .55),
              el(f'<div style="margin-top:44px">{"".join(tag(t) for t in tags)}</div>', a + .8))

def build():
    D = 18
    s = [
        sc("dark", 0, 2.8,
           el(chip("1ª parcela do 13º: até 30/11", ic="clock"), 0, "pop", "align-self:flex-start;margin-bottom:64px"),
           el(h(["Caiu o 13º", "e vai usar", '<span class="o">na casa?</span>'], 124, "#fff"), .2),
           el(h(["Não começa", "pela pintura."], 96, "#fff", 46), 1.0)),
        step(2.8, 5.2, 1, ["O que piora", "com a chuva"], "Goteira, vazamento, infiltração", "drop", ["Encanador", "Pedreiro"]),
        step(5.2, 7.6, 2, ["O que é", "segurança"], "Tomada esquentando, fiação velha", "bolt", ["Eletricista"]),
        step(7.6, 10.0, 3, ["O que é", "estrutura"], "Rachadura, telhado, madeiramento", "crack", ["Pedreiro", "Carpinteiro"]),
        step(10.0, 12.4, 4, ["Só depois:", 'o <span class="o">bonito</span>'], "Pintura, forro, acabamento", "house", ["Pintor", "Gesseiro"]),
        sc("dark", 12.4, 14.8,
           el(h(["E antes de", 'gastar, pede', '<span class="o">proposta.</span>'], 120, "#fff"), 12.4, "up"),
           el(f'<div style="margin-top:60px;background:#fff;color:{GR};border-radius:30px;padding:34px 38px;font-size:40px;font-weight:600;display:flex;flex-direction:column;gap:20px">'
              f'<div style="display:flex;align-items:center;gap:18px">{icon("check",48,OR,2.6)}Mão de obra</div>'
              f'<div style="display:flex;align-items:center;gap:18px">{icon("check",48,OR,2.6)}Materiais</div>'
              f'<div style="display:flex;align-items:center;gap:18px">{icon("check",48,OR,2.6)}Prazo</div></div>', 13.0, "up")),
        sc("orange", 14.8, D + 1,
           el(logo(64, mono="#fff"), 14.85, "pop", "margin-bottom:56px"),
           el(h(["Publique seu", "pedido e receba", "propostas."], 104, "#fff"), 15.0),
           el(f'<div style="font-size:40px;color:#fff;margin-top:34px;font-weight:600">{icon("pin",40,"#fff",2.4)} 11 cidades de Mato Grosso</div>', 15.5),
           el(f'<div style="display:inline-block;margin-top:44px;background:#252A31;color:#fff;border-radius:26px;padding:26px 38px;font-family:PJS;font-weight:800;font-size:52px">Grátis · link na bio</div>', 15.8, "up")),
    ]
    return D, s

if __name__ == "__main__":
    (ROOT / "out").mkdir(exist_ok=True)
    render("decimo13", build, 102)
