"""TikTok 29/11/2026 — Retrospectiva 2026 da sua casa (estrutura de 'retrospectiva do ano', sem marca de terceiros)."""
from video import *

def chip(txt, bg=OR, col="#fff", ic=None, fs=38):
    i = icon(ic, fs + 6, col, 2.4) if ic else ""
    return (f'<div style="display:inline-flex;align-items:center;gap:14px;background:{bg};color:{col};border-radius:999px;'
            f'padding:16px 32px;font-family:PJS;font-weight:800;font-size:{fs}px">{i}{txt}</div>')

def tag(txt):
    return (f'<span style="display:inline-block;background:rgba(255,255,255,.14);color:#fff;border-radius:16px;'
            f'padding:10px 22px;font-family:PJS;font-weight:700;font-size:32px;margin:0 14px 14px 0">{txt}</span>')

def prog(k, n=4):
    segs = "".join(f'<div style="flex:1;height:10px;border-radius:5px;background:{"#fff" if i <= k else "rgba(255,255,255,.3)"}"></div>' for i in range(n))
    return f'<div style="display:flex;gap:10px;width:100%;margin-bottom:60px">{segs}</div>'

def card(a, b, k, label, big, sub, ic, tags, bg):
    return sc("orange", a, b,
              el(prog(k), a, "fade"),
              el(f'<div style="font-family:PJS;font-weight:700;font-size:38px;letter-spacing:.06em;text-transform:uppercase;color:rgba(255,255,255,.85)">{label}</div>', a, "left"),
              el(f'<div style="margin-top:40px;width:220px;height:220px;border-radius:56px;background:{GR};display:flex;align-items:center;justify-content:center">{icon(ic,140,OR,1.8)}</div>', a + .2, "pop"),
              el(h(big, 116, "#fff", 46), a + .45),
              el(f'<div style="font-size:42px;color:{GR};margin-top:26px;font-weight:600">{sub}</div>', a + .8),
              el(f'<div style="margin-top:40px">{"".join(tag(t) for t in tags)}</div>', a + 1.05),
              extra=f"background:{bg}")

def build():
    D = 18
    g1 = "linear-gradient(160deg,#F47B20,#D96113)"
    s = [
        sc("dark", 0, 2.8,
           el(chip("RETROSPECTIVA 2026", ic="star"), 0, "pop", "align-self:flex-start;margin-bottom:64px"),
           el(h(["A retrospectiva", 'da sua <span class="o">casa</span>', "chegou."], 124, "#fff"), .2),
           el(f'<div style="font-size:46px;color:#C9CED6;margin-top:44px;font-weight:600">Spoiler: ela lembra de tudo.</div>', 1.1)),
        card(2.8, 5.0, 0, "Som mais tocado do ano", ["A goteira"], "Tocou sem parar desde que a chuva voltou em MT", "drop", ["Encanador", "Pedreiro"], g1),
        card(5.0, 7.2, 1, "Artista que você mais evitou", ["O disjuntor", "que cai"], "Toda vez que liga chuveiro e forno juntos", "bolt", ["Eletricista"], g1),
        card(7.2, 9.4, 2, "Lugar mais visitado", ["Aquela", "rachadura"], "Você olha pra ela todo dia", "crack", ["Pedreiro", "Pintor"], g1),
        card(9.4, 11.6, 3, "Frase do ano", ["“Semana que", "vem eu chamo", "alguém.”"], "Repetida o ano inteiro", "chat", ["Todo mundo"], g1),
        sc("dark", 11.6, 14.2,
           el(h(["Que 2027", "não tenha a", 'mesma <span class="o">playlist.</span>'], 128, "#fff"), 11.65, "up"),
           el(f'<div style="font-size:46px;color:#C9CED6;margin-top:50px;font-weight:600;line-height:1.35">Chama quem resolve<br>antes do ano virar.</div>', 12.4, "up")),
        sc("orange", 14.2, D + 1,
           el(logo(64, mono="#fff"), 14.25, "pop", "margin-bottom:56px"),
           el(h(["Publique o", "pedido e receba", "propostas."], 104, "#fff"), 14.4),
           el(f'<div style="font-size:40px;color:#fff;margin-top:34px;font-weight:600">{icon("pin",40,"#fff",2.4)} Profissionais de 11 cidades de Mato Grosso</div>', 14.9),
           el(f'<div style="display:inline-block;margin-top:44px;background:#252A31;color:#fff;border-radius:26px;padding:26px 38px;font-family:PJS;font-weight:800;font-size:52px">Grátis · link na bio</div>', 15.3, "up")),
    ]
    return D, s

if __name__ == "__main__":
    (ROOT / "out").mkdir(exist_ok=True)
    render("retro2026", build, 106)
