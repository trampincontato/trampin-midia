"""Lote 2 (benchmark Alfredo Soares / Tallis Gomes / G4) — 3 Reels + 1 carrossel."""
from video import *
from video import render as _render
import slides

# ---------- componentes ----------
def bubble(who, hora, txt, side="left", dark_bg=True):
    bg = "#fff" if side == "left" else OR
    fg = GR if side == "left" else "#fff"
    lbl = "rgba(255,255,255,.75)" if dark_bg else CI
    al = "flex-start" if side == "left" else "flex-end"
    rad = "40px 40px 40px 10px" if side == "left" else "40px 40px 10px 40px"
    return (f'<div style="display:flex;flex-direction:column;align-items:{al}">'
            f'<div style="font-family:PJS;font-weight:700;font-size:32px;color:{lbl};margin:0 14px 14px">{who} · {hora}</div>'
            f'<div style="max-width:780px;background:{bg};color:{fg};border-radius:{rad};padding:34px 40px;font-size:50px;line-height:1.28;font-weight:600;box-shadow:0 20px 50px rgba(0,0,0,.25)">{txt}</div></div>')

def tag(txt, bg=OR, fg="#fff", size=38):
    return (f'<div style="display:inline-block;background:{bg};color:{fg};border-radius:999px;padding:16px 34px;'
            f'font-family:PJS;font-weight:800;font-size:{size}px">{txt}</div>')

# ---------- Reel A: contraste (ref. G4 legenda de contraste + print de WhatsApp do Alfredo) ----------
def reel_contraste():
    D = 12.5
    s = [
        sc("dark", 0, 3.4,
           el(tag("Mesma cidade. Mesmo dia."), -1, "fade", "margin-bottom:70px;align-self:flex-start"),
           el(bubble("Cliente", "9:12", "Alguém conhece um encanador bom? Tá vazando aqui em casa 😩"), -1, "fade"),
           el(bubble("Encanador", "9:14", "Semana fraca. Se alguém precisar, tô disponível 🙏", "right"), 1.3, "up", "margin-top:70px")),
        sc("light", 3.4, 6.4,
           el(h(["Os dois moravam", "a poucas ruas", 'um do <span class="o">outro.</span>'], 112), 3.4, "pop"),
           el(h(["Nenhum achou", "o outro."], 112, CI, 60), 4.6)),
        sc("dark", 6.4, 9.4,
           el(h(["Não falta", "profissional."], 128, "#fff"), 6.4, "up"),
           el(h(['Falta <span class="o">encontrar.</span>'], 128, "#fff", 40), 7.4, "up")),
        endcard(9.4, D + 1, ["Um pedido.", "Os dois", "resolvidos."]),
    ]
    return D, s

# ---------- Reel B: opinião forte (ref. capas de opinião do Tallis Gomes) ----------
def reel_opiniao():
    D = 12
    big = lambda lines, c="#fff", mt=0: h(lines, 136, c, mt)
    s = [
        sc("dark", 0, 4.2,
           el(tag("Opinião", "#fff", GR, 34), -1, "fade", "margin-bottom:60px;align-self:flex-start"),
           el(big(["Profissional bom"]), -1, "fade"),
           el(big(["não é o que"], "#fff", 10), .9),
           el(big(['nunca <span class="o">erra.</span>'], "#fff", 10), 1.8)),
        sc("orange", 4.2, 7.6,
           el(big(["É o que"]), 4.2, "up"),
           el(big(["volta pra"], "#fff", 10), 5.0, "up"),
           el(big(["arrumar."], GR, 10), 5.8, "pop")),
        sc("light", 7.6, 9.6,
           el(h(["Palavra cumprida", 'vira <span class="o">avaliação.</span>'], 112), 7.6, "up"),
           el(f'<div style="margin-top:60px;display:flex;gap:18px">' + "".join(icon("star", 110, OR, 1.8).replace('fill="none"', 'fill="#F47B20"') for _ in range(5)) + '</div>', 8.3, "up")),
        endcard(9.6, D + 1, ["E no TRAMPIN,", "quem faz bem,", "aparece."]),
    ]
    return D, s

# ---------- Reel C: caixinha de pergunta (ref. "pergunta da caixinha" do Alfredo) ----------
def pergunta_card():
    return (f'<div style="background:#fff;border-radius:44px;overflow:hidden;box-shadow:0 30px 70px rgba(0,0,0,.35)">'
            f'<div style="background:{OR};color:#fff;padding:30px 44px;font-family:PJS;font-weight:800;font-size:40px;display:flex;align-items:center;gap:18px">'
            f'{symbol(52, "#fff")} Pergunta pro TRAMPIN</div>'
            f'<div style="padding:44px;color:{GR};font-family:PJS;font-weight:800;font-size:72px;line-height:1.1;letter-spacing:-.03em">'
            f'Como eu sei se o pedreiro é bom <span class="o">antes</span> de contratar?</div></div>')

def passo(a, b, n, lines, ic):
    return sc("light", a, b,
              el(f'<div style="display:flex;align-items:center;gap:40px"><div class="h" style="font-size:260px;color:{OR};line-height:.8">{n}</div>{icon(ic,170,OR,1.6)}</div>', a, "pop"),
              el(h(lines, 104, None, 60), a + .3))

def reel_caixinha():
    D = 16
    s = [
        sc("dark", 0, 3.2,
           el(pergunta_card(), -1, "fade"),
           el(h(['4 coisas pra olhar 👇'], 80, "#fff", 70), 1.2, "up")),
        passo(3.2, 5.6, "1", ["Fotos de", "serviços que", "ele já fez"], "camera"),
        passo(5.6, 8.0, "2", ["Avaliação de", "quem já", "contratou"], "star"),
        passo(8.0, 10.6, "3", ["Proposta com", "mão de obra,", "materiais e prazo"], "doc"),
        passo(10.6, 13.0, "4", ["Conversa antes.", "Se der, uma", "visita."], "chat"),
        endcard(13.0, D + 1, ["No TRAMPIN", "você vê tudo", "antes de fechar."]),
    ]
    return D, s

# ---------- Carrossel D: print de post + análise (ref. "print de post" do Alfredo) ----------
W4, H4 = 1080, 1350
TOT = 6

def printpost():
    return (f'<div style="background:#fff;border-radius:40px;padding:52px 54px;box-shadow:0 30px 70px rgba(0,0,0,.35);color:{GR}">'
            f'<div style="display:flex;align-items:center;gap:22px;margin-bottom:34px">'
            f'<div style="width:96px;height:96px;border-radius:50%;background:{GR};display:flex;align-items:center;justify-content:center">{symbol(60)}</div>'
            f'<div><div style="font-family:PJS;font-weight:800;font-size:38px">TRAMPIN</div><div style="font-size:30px;color:{CI}">@trampin.app</div></div></div>'
            f'<div style="font-size:50px;line-height:1.32;font-weight:600">Muitas vezes, o profissional que some no meio da obra não é desonesto.<br><br>'
            f'<b style="font-family:PJS;font-weight:800">Ele pegou serviço demais com medo de ficar sem nenhum no mês seguinte.</b></div></div>')

def lista(items, dark=False):
    col = "#fff" if dark else GR
    return "".join(
        f'<div style="display:flex;gap:26px;align-items:flex-start;font-size:44px;line-height:1.3;font-weight:600;color:{col};margin:22px 0">'
        f'<span style="flex:none;width:64px;height:64px;border-radius:50%;background:{OR};display:flex;align-items:center;justify-content:center;margin-top:-2px">{icon("check", 38, BR, 3)}</span>{t}</div>'
        for t in items)

def carrossel():
    hl = slides.hl
    f = lambda inner, theme, n: slides.frame(inner, W4, H4, theme, page_no=n, total=TOT)
    ciclo = ["Mês cheio", "Aceita tudo", "Atrasa", "Cliente reclama", "Indicação some", "Mês vazio"]
    ciclo_html = '<div style="display:flex;flex-direction:column;gap:14px;margin-top:50px">' + "".join(
        f'<div style="display:flex;align-items:center;gap:24px"><span class="chip" style="background:{OR if i in (0,5) else "#fff"};color:{"#fff" if i in (0,5) else GR};font-size:42px;padding:18px 34px">{t}</span>'
        f'{"<span style=\"font-size:40px;color:" + CI + "\">↓</span>" if i < 5 else ""}</div>' for i, t in enumerate(ciclo)) + "</div>"
    pages = [
        f(printpost() + f'<div style="margin-top:56px;font-family:PJS;font-weight:800;font-size:46px;color:#fff">Concorda? Arrasta pro lado <span class="o">→</span></div>', "dark", 1),
        f(hl(['O ciclo que', 'ninguém <span class="o">vê:</span>'], 104) + ciclo_html, "light", 2),
        f(hl(['Pra quem', '<span class="o">contrata:</span>'], 110) + '<div style="margin-top:40px">' + lista([
            "Combine o prazo por escrito, não de boca",
            "Pergunte quantos serviços ele tem em andamento",
            "Desconfie de quem promete tudo pra amanhã",
        ]) + "</div>", "light", 3),
        f(hl(['Pra quem', '<span class="o">trabalha:</span>'], 110, "#fff") + '<div style="margin-top:40px">' + lista([
            "“Consigo começar em 15 dias” passa mais confiança que “amanhã”",
            "Dizer não hoje protege sua avaliação amanhã",
            "Cliente satisfeito é o que traz o próximo",
        ], dark=True) + "</div>", "dark", 4),
        f(hl(['Onde o', 'TRAMPIN <span class="o">entra:</span>'], 110) + '<div style="margin-top:40px">' + lista([
            "Pedidos da sua especialidade, na sua cidade",
            "Botão disponível / indisponível: você mostra quando tem agenda",
            "Prazo já vai escrito na proposta",
        ]) + "</div>", "light", 5),
        f(hl(["Combinou,", "tá combinado."], 130, "#fff") + f'<div style="margin-top:50px;font-size:48px;line-height:1.35;color:#fff;font-weight:600">'
          f'Grátis pra quem contrata e pra quem trabalha.<br><b style="font-family:PJS;font-weight:800">trampin.com.br</b></div>', "orange", 6),
    ]
    return [(f"servico_demais_ig_{i+1}.png", p, W4, H4) for i, p in enumerate(pages)]

REELS = {"contraste": (reel_contraste, 100), "opiniao": (reel_opiniao, 92), "caixinha": (reel_caixinha, 104)}

def preview(name, times):
    """Renderiza só alguns frames em PNG para conferir antes do vídeo."""
    from playwright.sync_api import sync_playwright
    D, scenes = REELS[name][0]()
    html = page("".join(scenes), W, H, CSS).replace("</body>", f"<script>{JS}setTime(0)</script></body>")
    out = ROOT / "preview"; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        pg.set_content(html, wait_until="load"); pg.wait_for_timeout(200)
        for t in times:
            pg.evaluate(f"setTime({t})"); pg.screenshot(path=str(out / f"{name}_{t}.jpg"), type="jpeg", quality=80)
        b.close()

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "preview":
        for n, ts in {"contraste": [0, 2.5, 5.5, 8.5, 11], "opiniao": [0, 3.5, 7, 9, 11], "caixinha": [0, 2.5, 9.5, 14.5]}.items():
            preview(n, ts)
    elif cmd == "carrossel":
        render_pngs(carrossel(), ROOT / "out")
    else:
        (ROOT / "out").mkdir(exist_ok=True)
        _render(cmd, *REELS[cmd])
