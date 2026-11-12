from kit import *

def pad(W, H):
    # top, right, bottom, left
    if H > 1500:  # 9:16 (TikTok / Reels safe zones)
        return (190, 150, 360, 90)
    return (88, 88, 88, 88)

def frame(inner, W, H, theme="light", footer=True, page_no=None, total=None, logo_top=True):
    t, r, b, l = pad(W, H)
    dark = theme in ("dark", "orange")
    foot = ""
    if footer:
        col = "rgba(255,255,255,.85)" if dark else CI
        foot = (f'<div style="display:flex;justify-content:space-between;align-items:center;font-size:30px;color:{col};font-weight:600">'
                f'<span>Quem faz bem, aparece.</span><span>trampin.com.br</span></div>')
    top = ""
    if logo_top:
        mono = BR if theme == "orange" else None
        pn = ""
        if page_no:
            pc = "rgba(255,255,255,.7)" if dark else CI
            pn = f'<span style="font-family:PJS;font-weight:700;font-size:28px;color:{pc}">{page_no}/{total}</span>'
        top = f'<div style="display:flex;justify-content:space-between;align-items:center">{logo(40, dark, mono)}{pn}</div>'
    body = (f'<div class="c {theme} grain" style="padding:{t}px {r}px {b}px {l}px">{top}'
            f'<div style="flex:1;display:flex;flex-direction:column;justify-content:center">{inner}</div>{foot}</div>')
    return page(body, W, H)

def hl(lines, size, color=None):
    style = f"font-size:{size}px" + (f";color:{color}" if color else "")
    txt = "<br>".join(lines).replace(".", '<span style="margin-left:-.11em">.</span>')
    return f'<div class="h" style="{style}">' + txt + "</div>"

CATS = ["Pedreiro", "Servente", "Eletricista", "Encanador", "Pintor", "Gesseiro", "Carpinteiro"]

def chips(items, bg=GR, fg=BR, size=30):
    return ('<div style="display:flex;flex-wrap:wrap;gap:14px">' +
            "".join(f'<span class="chip" style="background:{bg};color:{fg};font-size:{size}px">{i}</span>' for i in items) + "</div>")

# ---------------- statics ----------------
def post1(W, H):
    tall = H > 1500
    inner = (f'<div style="margin-bottom:46px">{icon("eye", 120, OR, 1.8)}</div>'
             + hl(["Todo trabalho", "bem feito", 'merece ser <span class="o">visto.</span>'], 128 if not tall else 132, BR)
             + f'<div style="margin-top:54px;font-size:40px;line-height:1.4;color:rgba(255,255,255,.82);max-width:860px">'
               'O pedreiro caprichoso. O encanador de confiança. O eletricista que resolve de primeira.'
               '<br><b style="color:#fff">Toda cidade tem. Quase sempre só o vizinho conhece.</b></div>')
    return frame(inner, W, H, "dark")

def post2(W, H):
    item = lambda t: (f'<div style="display:flex;gap:22px;align-items:center;font-size:40px;font-weight:600;margin:18px 0">'
                      f'<span style="flex:none;width:62px;height:62px;border-radius:50%;background:{OR};display:flex;align-items:center;justify-content:center">{icon("check", 38, BR, 3)}</span>{t}</div>')
    inner = (hl(["Seu capricho", "merece mais que", 'o <span class="o">boca a boca.</span>'], 112)
             + '<div style="margin-top:50px">' + item("Perfil com fotos dos seus trabalhos") + item("Pedidos da sua especialidade")
             + item("Você manda a proposta e combina direto") + "</div>"
             + f'<div style="margin-top:44px;display:inline-block;align-self:flex-start;background:{GR};color:#fff;border-radius:22px;padding:26px 34px;font-family:PJS;font-weight:800;font-size:44px">'
               f'Grátis. <span class="o">Sem taxa, sem mensalidade.</span></div>'
             + f'<div style="margin-top:40px">{chips(CATS, "#fff", GR, 28)}</div>')
    return frame(inner, W, H, "light")

def post3(W, H):
    step = lambda n, t: (f'<div style="display:flex;gap:28px;align-items:center;background:#fff;border-radius:28px;padding:24px 34px;margin:12px 0;color:{GR}">'
                         f'<span class="h" style="font-size:76px;color:{OR};width:60px">{n}</span>'
                         f'<span style="font-size:38px;font-weight:600;line-height:1.3">{t}</span></div>')
    inner = (hl(["Cansou de procurar?", "A gente acha", f'quem <span style="color:{GR}">resolve.</span>'], 96, BR)
             + '<div style="margin-top:40px">' + step(1, "Você publica o que precisa")
             + step(2, "Profissionais da sua cidade mandam propostas com mão de obra, materiais e prazo")
             + step(3, "Você conversa pelo chat, escolhe e combina direto") + "</div>"
             + '<div class="h" style="margin-top:36px;font-size:46px;color:#fff">Grátis pra usar.</div>')
    return frame(inner, W, H, "orange")

# ---------------- carousels ----------------
def cover(lines, sub, ic, W, H, theme="dark", n=None, tot=None):
    subc = "rgba(255,255,255,.85)" if theme != "light" else CI
    swipe = (f'<div style="margin-top:56px;display:flex;align-items:center;gap:18px;font-family:PJS;font-weight:800;font-size:36px;color:{OR}">'
             f'Arrasta pro lado <span style="font-size:52px">→</span></div>')
    inner = (f'<div style="margin-bottom:44px">{icon(ic, 130, OR, 1.8)}</div>' + hl(lines, 132, BR if theme != "light" else None)
             + f'<div style="margin-top:44px;font-size:44px;line-height:1.35;color:{subc};max-width:880px;font-weight:600">{sub}</div>' + swipe)
    return frame(inner, W, H, theme, page_no=n, total=tot)

def tip(num, title, body, who, ic, W, H, n, tot, warn=False):
    theme = "dark" if warn else "light"
    bc = "rgba(255,255,255,.85)" if warn else "#4A515B"
    tc = BR if warn else GR
    who_html = ""
    if who:
        who_html = (f'<div style="margin-top:54px"><div style="font-family:PJS;font-weight:700;font-size:30px;letter-spacing:.06em;text-transform:uppercase;color:{OR};margin-bottom:18px">Quem resolve</div>'
                    + chips(who, OR, BR, 32) + "</div>")
    badge = ""
    if warn:
        badge = (f'<div style="display:inline-flex;align-self:flex-start;align-items:center;gap:14px;background:{OR};color:#fff;border-radius:999px;padding:14px 30px;font-family:PJS;font-weight:800;font-size:32px;margin-bottom:36px">'
                 f'{icon("warn", 40, BR, 2.4)} O mais sério</div>')
    inner = (badge + f'<div style="display:flex;align-items:center;gap:34px;margin-bottom:40px">'
             f'<div class="h" style="font-size:210px;color:{OR};line-height:.8">{num}</div>{icon(ic, 150, OR if not warn else BR, 1.6)}</div>'
             + hl(title, 92, tc)
             + f'<div style="margin-top:38px;font-size:44px;line-height:1.4;color:{bc};font-weight:500;max-width:900px">{body}</div>' + who_html)
    return frame(inner, W, H, theme, page_no=n, total=tot)

def cta(lines, bullets, W, H, n, tot):
    bl = "".join(f'<div style="display:flex;gap:22px;align-items:flex-start;font-size:38px;font-weight:600;margin:14px 0;line-height:1.3">'
                 f'<span style="flex:none;width:58px;height:58px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center">{icon("check", 36, OR, 3)}</span>{b}</div>' for b in bullets)
    inner = (hl(lines, 92, BR) + f'<div style="margin-top:36px">{bl}</div>'
             + f'<div style="margin-top:46px;align-self:flex-start;background:{GR};color:#fff;border-radius:24px;padding:28px 38px;font-family:PJS;font-weight:800;font-size:50px">trampin.com.br</div>'
             + '<div class="h" style="margin-top:34px;font-size:44px;color:#fff">Quem faz bem, aparece.</div>')
    return frame(inner, W, H, "orange", footer=False, page_no=n, total=tot)

def chuva(W, H):
    T = 7
    return [
        cover(["Chuva chegou.", "Sua casa", 'tá <span class="o">pronta?</span>'], "5 sinais pra ficar de olho. O último é o mais sério. Salva esse post.", "cloud", W, H, "dark", 1, T),
        tip("1", ["Mancha ou bolha", "na pintura"], "Pode ser umidade entrando pela parede ou pelo telhado. Quanto antes resolver, menor o estrago.", ["Pedreiro", "Pintor"], "drop", W, H, 2, T),
        tip("2", ["Mofo no teto", "ou no forro"], "Sinal de goteira ou infiltração vindo de cima. Só pintar por cima não resolve.", ["Gesseiro", "Pedreiro", "Carpinteiro"], "cloud", W, H, 3, T),
        tip("3", ["Rachadura", "que aumenta"], "Fissura que cresce depois da chuva pede avaliação. Tire uma foto hoje e compare daqui a uma semana.", ["Pedreiro"], "crack", W, H, 4, T),
        tip("4", ["Conta de água", "subindo"], "Sem mudar o consumo? Pode ser vazamento escondido. Feche as torneiras e veja se o relógio continua girando.", ["Encanador"], "meter", W, H, 5, T),
        tip("5", ["Umidade perto", "de tomada"], "Não mexa. Desligue o disjuntor daquele circuito e chame um eletricista.", ["Eletricista"], "plug", W, H, 6, T, warn=True),
        cta(["Achou algum sinal?", "Publique seu pedido", "no TRAMPIN."], ["Profissionais da sua cidade mandam propostas", "Mão de obra, materiais e prazo na proposta", "Grátis pra usar"], W, H, 7, T),
    ]

def orcamento(W, H):
    T = 7
    return [
        cover(["Orçamento", "sem dor de", '<span class="o">cabeça.</span>'], "5 combinados simples que evitam briga no meio da obra.", "doc", W, H, "dark", 1, T),
        tip("1", ["Explique com", "detalhe e foto"], "Medidas, o que você quer e o que já tem em casa. Quanto mais claro o pedido, mais justo o preço.", None, "camera", W, H, 2, T),
        tip("2", ["Mão de obra e", "material separados"], "Assim você compara propostas de verdade e sabe exatamente o que está pagando.", None, "split", W, H, 3, T),
        tip("3", ["Prazo combinado", "antes"], "Data de início e de entrega definidas antes de começar. Combinou, tá combinado.", None, "clock", W, H, 4, T),
        tip("4", ["Veja trabalhos", "anteriores"], "Fotos de serviços já feitos e avaliações de quem já contratou dizem muito.", None, "star", W, H, 5, T),
        tip("5", ["Tudo por", "escrito"], "Escopo, valores, prazo e forma de pagamento. Evita o famoso “não foi isso que eu falei”.", None, "doc", W, H, 6, T),
        cta(["No TRAMPIN", "isso já vem", "pronto."], ["Cada proposta chega com mão de obra, materiais e prazo", "Perfil com fotos e avaliações de clientes", "Contrato digital aceito pelos dois lados no app"], W, H, 7, T),
    ]

if __name__ == "__main__":
    import sys
    items = []
    for (W, H, tag) in [(1080, 1350, "ig"), (1080, 1920, "tt")]:
        if tag == "ig":
            items += [("post1_ig.png", post1(W, H), W, H), ("post2_ig.png", post2(W, H), W, H), ("post3_ig.png", post3(W, H), W, H)]
        for i, h in enumerate(chuva(W, H), 1):
            items.append((f"chuva_{tag}_{i}.png", h, W, H))
        for i, h in enumerate(orcamento(W, H), 1):
            items.append((f"orc_{tag}_{i}.png", h, W, H))
    render_pngs(items, ROOT / "out")
    print(len(items), "rendered")
