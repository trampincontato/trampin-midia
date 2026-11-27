"""Reel IG 28/11/2026 — contagem regressiva: contando hoje, restam 4 sábados até o Natal."""
from video import *

def chip(txt, bg=OR, col="#fff", ic=None, fs=38):
    i = icon(ic, fs + 6, col, 2.4) if ic else ""
    return (f'<div style="display:inline-flex;align-items:center;gap:14px;background:{bg};color:{col};border-radius:999px;'
            f'padding:16px 32px;font-family:PJS;font-weight:800;font-size:{fs}px">{i}{txt}</div>')

SAB = [("28", "nov"), ("05", "dez"), ("12", "dez"), ("19", "dez")]

def cal(a, hi=0):
    cards = ""
    for i, (d, m) in enumerate(SAB):
        on = i == hi
        bg = OR if on else "rgba(255,255,255,.08)"
        bd = OR if on else "rgba(255,255,255,.25)"
        cards += el(f'<div style="width:190px;border-radius:28px;border:4px solid {bd};background:{bg};padding:22px 0 26px;text-align:center">'
                    f'<div style="font-family:PJS;font-weight:700;font-size:26px;letter-spacing:.08em;color:{"#fff" if on else "rgba(255,255,255,.6)"}">SÁB</div>'
                    f'<div class="h" style="font-size:96px;color:#fff;margin-top:6px">{d}</div>'
                    f'<div style="font-family:PJS;font-weight:700;font-size:30px;color:{"#fff" if on else "rgba(255,255,255,.6)"}">{m}</div></div>',
                    a + i * .12, "pop")
    return f'<div style="display:flex;gap:22px;margin-bottom:70px">{cards}</div>'

def row(txt, tagtxt, ic, t, dark=False):
    col = "#fff" if dark else GR
    bg = "rgba(255,255,255,.08)" if dark else "#fff"
    return el(f'<div style="display:flex;align-items:center;gap:28px;background:{bg};border-radius:28px;padding:26px 30px">'
              f'<span style="flex:none;width:92px;height:92px;border-radius:24px;background:{OR};display:flex;align-items:center;justify-content:center">{icon(ic,56,"#fff",2.2)}</span>'
              f'<div><div class="h" style="font-size:50px;color:{col}">{txt}</div>'
              f'<div style="font-size:30px;font-weight:600;color:{OR};margin-top:6px">{tagtxt}</div></div></div>', t, "left")

def build():
    D = 18
    s = [
        sc("dark", 0, 3.4,
           el(chip("Contando hoje", ic="clock", fs=36), 0, "pop", "align-self:flex-start;margin-bottom:54px"),
           el(cal(0.1), 0, "fade"),
           el(h(["Restam", '<span class="o">4 sábados</span>', "até o Natal."], 128, "#fff"), .5),
           el(h(["E a casa?"], 84, "rgba(255,255,255,.7)", 40), 1.5)),
        sc("light", 3.4, 7.0,
           el(chip("Dá tempo", ic="check", fs=40), 3.4, "pop", "align-self:flex-start;margin-bottom:40px"),
           el(h(["Serviço mais", '<span class="o">rápido:</span>'], 104), 3.55),
           el('<div style="height:46px"></div>', 3.5, "fade"),
           row("Pintar um cômodo", "Pintor", "house", 4.0),
           el('<div style="height:22px"></div>', 3.5, "fade"),
           row("Trocar chuveiro e tomadas", "Eletricista", "bolt", 4.4),
           el('<div style="height:22px"></div>', 3.5, "fade"),
           row("Consertar vazamento", "Encanador", "drop", 4.8),
           el('<div style="height:22px"></div>', 3.5, "fade"),
           row("Reparo no forro de gesso", "Gesseiro", "tool", 5.2)),
        sc("dark", 7.0, 10.4,
           el(chip("Pede proposta já", ic="warn", fs=40), 7.0, "pop", "align-self:flex-start;margin-bottom:40px"),
           el(h(["Tem mais", '<span class="o">etapas?</span>'], 116, "#fff"), 7.15),
           el('<div style="height:46px"></div>', 7.0, "fade"),
           row("Troca de piso", "Pedreiro · Servente", "split", 7.6, True),
           el('<div style="height:22px"></div>', 7.0, "fade"),
           row("Reforma do banheiro", "Pedreiro · Encanador", "drop", 8.0, True),
           el('<div style="height:22px"></div>', 7.0, "fade"),
           row("Muro, reboco, telhado", "Pedreiro · Carpinteiro", "crack", 8.4, True)),
        sc("light", 10.4, 13.4,
           el(icon("users", 170, OR, 1.6), 10.4, "pop", "margin-bottom:50px"),
           el(h(["Em dezembro,", "todo mundo", 'lembra da casa', '<span class="o">ao mesmo tempo.</span>'], 104), 10.55),
           el(f'<div style="font-size:44px;color:{CI};margin-top:44px;font-weight:600;line-height:1.35">Quem pede antes escolhe com calma.</div>', 11.6)),
        sc("dark", 13.4, 15.6,
           el(chip("É profissional?", ic="tool", fs=40), 13.4, "pop", "align-self:flex-start;margin-bottom:50px"),
           el(h(["Deixa o perfil", 'como <span class="o">disponível</span>', "e mostra suas", "fotos."], 112, "#fff"), 13.55),
           el(f'<div style="font-size:42px;color:rgba(255,255,255,.75);margin-top:40px;font-weight:600">Fim de ano é época de pedido.</div>', 14.4)),
        sc("orange", 15.6, D + 1,
           el(logo(64, mono="#fff"), 15.65, "pop", "margin-bottom:56px"),
           el(h(["Publique seu", "pedido hoje e", "receba propostas."], 100, "#fff"), 15.8),
           el(f'<div style="font-size:40px;color:#fff;margin-top:34px;font-weight:600;display:flex;align-items:center;gap:12px">{icon("pin",44,"#fff",2.4)} 11 cidades de Mato Grosso</div>', 16.2),
           el(f'<div style="display:inline-block;margin-top:44px;background:#252A31;color:#fff;border-radius:26px;padding:26px 38px;font-family:PJS;font-weight:800;font-size:52px">Grátis · trampin.com.br</div>', 16.5, "up")),
    ]
    return D, s

if __name__ == "__main__":
    (ROOT / "out").mkdir(exist_ok=True)
    render("natal4", build, 106)
