from kit import *
import subprocess, shutil, pathlib, sys

W, H, FPS = 1080, 1920, 30
PADT, PADR, PADB, PADL = 230, 150, 430, 90

CSS = """
.sc{position:absolute;inset:0;display:none;flex-direction:column;justify-content:center;padding:%dpx %dpx %dpx %dpx}
.el{will-change:transform,opacity}
.h{font-family:'PJS';font-weight:800;letter-spacing:-0.035em;line-height:1.02}
.phone{width:620px;height:1000px;border-radius:70px;background:#fff;border:16px solid #252A31;box-shadow:0 40px 80px rgba(0,0,0,.25);
 padding:40px 34px;display:flex;flex-direction:column;gap:22px;align-self:center;overflow:hidden}
.card{background:#F3F5F7;border-radius:24px;padding:24px 26px;font-size:30px;color:#252A31}
.lbl{font-size:22px;color:#737B86;font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.btn{background:#F47B20;color:#fff;border-radius:999px;padding:22px;text-align:center;font-family:PJS;font-weight:800;font-size:32px}
""" % (PADT, PADR, PADB, PADL)

JS = """
const ease=x=>1-Math.pow(1-x,3);
function setTime(t){
 document.querySelectorAll('.sc').forEach(s=>{const a=+s.dataset.in,b=+s.dataset.out;s.style.display=(t>=a&&t<b)?'flex':'none'});
 document.querySelectorAll('.el').forEach(e=>{
  const a=+e.dataset.in, an=e.dataset.anim||'up'; let p=Math.max(0,Math.min(1,(t-a)/0.38)); p=ease(p);
  let tr='',op=p;
  if(an=='up') tr=`translateY(${(1-p)*70}px)`;
  if(an=='pop') tr=`scale(${0.6+0.4*p+(p<1?Math.sin(p*Math.PI)*0.08:0)})`;
  if(an=='left') tr=`translateX(${(1-p)*-120}px)`;
  if(an=='fade') tr='';
  if(e.dataset.pulse){const k=Math.max(0,t-a); tr+=` scale(${1+0.06*Math.sin(k*7)})`;}
  e.style.opacity=op; e.style.transform=tr;
 });
 document.querySelectorAll('[data-fill]').forEach(e=>{const a=+e.dataset.fill; e.style.fill=t>=a?'#F47B20':'none'});
}
"""

def el(html, t, anim="up", extra="", pulse=False):
    pa = ' data-pulse="1"' if pulse else ""
    return f'<div class="el" data-in="{t}" data-anim="{anim}"{pa} style="opacity:0;{extra}">{html}</div>'

def sc(theme, a, b, *els, extra=""):
    bg = {"dark": "#252A31", "light": "#F3F5F7", "orange": "#F47B20"}[theme]
    col = "#fff" if theme != "light" else "#252A31"
    return f'<div class="sc grain" data-in="{a}" data-out="{b}" style="background:{bg};color:{col};{extra}">{"".join(els)}</div>'

def h(lines, size, color=None, mt=0):
    txt = "<br>".join(lines).replace(".", '<span style="margin-left:-.11em">.</span>')
    c = f";color:{color}" if color else ""
    return f'<div class="h" style="font-size:{size}px;margin-top:{mt}px{c}">{txt}</div>'

def endcard(a, b, lines):
    return sc("orange", a, b,
              el(logo(64, mono="#fff"), a + .05, "pop", "margin-bottom:60px"),
              *[el(h([ln], 112, "#fff"), a + .2 + i * .2, "up") for i, ln in enumerate(lines)],
              el(f'<div style="display:inline-block;margin-top:56px;background:#252A31;color:#fff;border-radius:26px;padding:28px 40px;font-family:PJS;font-weight:800;font-size:54px">Grátis · trampin.com.br</div>', a + .2 + len(lines) * .2 + .1, "up"))

def video_amigo():
    D = 10
    s = [
        sc("dark", 0, 3.4,
           el(f'<div style="display:flex;gap:26px;margin-bottom:56px">{icon("tool",110,OR,1.8)}{icon("bolt",110,OR,1.8)}{icon("house",110,OR,1.8)}</div>', 0, "pop"),
           el(h(["Manda esse vídeo"], 96, OR), .15),
           el(h(["pro amigo que", "só trabalha", "por indicação."], 124, "#fff", 10), .55)),
        sc("light", 3.4, 6.6,
           el(h(["Ele é bom."], 150), 3.45, "pop"),
           el(h(["Mas quem conhece", 'é só o <span class="o">vizinho.</span>'], 104, None, 50), 4.5),
           el(f'<div style="margin-top:70px;display:flex;gap:30px">{icon("house",120,CI,1.6)}{icon("house",120,OR,1.8)}{icon("house",120,CI,1.6)}</div>', 5.1, "up")),
        endcard(6.6, D + 1, ["No TRAMPIN,", "quem faz bem,", "aparece."]),
    ]
    return D, s

def numscene(a, b, n, lines, ic):
    return sc("light", a, b,
              el(f'<div style="display:flex;align-items:center;gap:40px"><div class="h" style="font-size:300px;color:{OR};line-height:.8">{n}</div>{icon(ic,190,OR,1.6)}</div>', a, "pop"),
              el(h(lines, 130, None, 60), a + .3))

def video_tomada():
    D = 15
    s = [
        sc("dark", 0, 2.8,
           el(icon("plug", 260, OR, 1.5), 0, "pop", "margin-bottom:60px", pulse=True),
           el(h(["Tomada", 'esquentando?'], 140, "#fff"), .2),
           el(h(['Não é hora de <span class="o">jeitinho.</span>'], 84, "#fff", 40), .9)),
        numscene(2.8, 5.2, "1", ["Espelho", "quente"], "fire"),
        numscene(5.2, 7.6, "2", ["Cheiro de", "queimado"], "warn"),
        numscene(7.6, 10.0, "3", ["Disjuntor", "caindo toda", "hora"], "bolt"),
        sc("dark", 10.0, 12.6,
           el(f'<div style="display:inline-flex;align-items:center;gap:16px;background:{OR};color:#fff;border-radius:999px;padding:18px 36px;font-family:PJS;font-weight:800;font-size:40px">{icon("warn",48,"#fff",2.4)} Não mexa sozinho</div>', 10.0, "pop", "margin-bottom:60px;align-self:flex-start"),
           el(h(["Desligue o", "disjuntor"], 140, "#fff"), 10.25),
           el(h(['e chame um <span class="o">eletricista.</span>'], 84, "#fff", 40), 10.9)),
        endcard(12.6, D + 1, ["Ache um", "eletricista", "no TRAMPIN."]),
    ]
    return D, s

def phone(inner):
    return f'<div class="phone"><div style="display:flex;justify-content:center;margin-bottom:6px">{logo(34)}</div>{inner}</div>'

def step_label(n, t):
    return (f'<div style="display:flex;align-items:center;gap:22px;margin-bottom:46px"><span class="h" style="width:96px;height:96px;border-radius:50%;background:{OR};color:#fff;display:flex;align-items:center;justify-content:center;font-size:58px">{n}</span>'
            f'<span class="h" style="font-size:76px">{t}</span></div>')

def video_15s():
    D = 15
    form = phone(
        el('<div class="card"><div class="lbl">Serviço</div><b>Pedreiro</b></div>', 3.0, "left")
        + el('<div class="card"><div class="lbl">Cidade · Bairro</div><b>Nova Mutum · Centro</b></div>', 3.4, "left")
        + el('<div class="card"><div class="lbl">O que precisa</div>Rebocar e pintar o muro da frente</div>', 3.8, "left")
        + el('<div class="btn">Publicar pedido</div>', 4.3, "pop"))
    prop = lambda ini, esp, t: el(
        f'<div class="card" style="display:flex;gap:20px;align-items:center"><span style="flex:none;width:76px;height:76px;border-radius:50%;background:{GR};color:#fff;font-family:PJS;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center">{ini}</span>'
        f'<div><b>{esp}</b><div style="font-size:24px;color:{CI};margin-top:6px">Mão de obra ✓ · Materiais ✓ · Prazo ✓</div></div></div>', t, "up")
    props = phone('<div class="lbl" style="text-align:center">Propostas recebidas</div>' + prop("JS", "Pedreiro", 5.9) + prop("RA", "Pedreiro", 6.3) + prop("MC", "Pedreiro", 6.7))
    bub = lambda txt, me, t: el(f'<div style="max-width:82%;align-self:{"flex-end" if me else "flex-start"};background:{OR if me else "#F3F5F7"};color:{"#fff" if me else GR};border-radius:26px;padding:20px 24px;font-size:28px">{txt}</div>', t, "up", f'display:flex;flex-direction:column')
    chat = phone('<div class="lbl" style="text-align:center">Chat do pedido</div>'
                 + bub("Consegue começar na segunda?", True, 8.9) + bub("Consigo sim. Levo o material.", False, 9.4)
                 + el('<div style="flex:1"></div>', 9.4, "fade") + el('<div class="btn">Aceitar proposta</div>', 10.0, "pop"))
    stars = "".join(f'<svg width="96" height="96" viewBox="0 0 24 24" stroke="{OR}" stroke-width="1.6" stroke-linejoin="round"><path data-fill="{11.6 + i*.18:.2f}" fill="none" d="{ICONS["star"].split(chr(34))[1]}"/></svg>' for i in range(5))
    rate = phone('<div style="flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:30px">'
                 f'<div class="h" style="font-size:44px;text-align:center">Serviço concluído</div><div style="display:flex;gap:6px">{stars}</div>'
                 f'<div style="font-size:28px;color:{CI};text-align:center">Só quem contratou avalia</div></div>')
    s = [
        sc("dark", 0, 2.6,
           el(h(["Precisa de", '<span class="o">pedreiro</span>'], 150, "#fff"), 0, "pop"),
           el(h(["e não sabe", "quem chamar?"], 110, "#fff", 30), .6)),
        sc("light", 2.6, 5.4, el(step_label(1, "Publique o pedido"), 2.6), el(form, 2.7, "up")),
        sc("light", 5.4, 8.4, el(step_label(2, "Receba propostas"), 5.4), el(props, 5.5, "up")),
        sc("light", 8.4, 11.2, el(step_label(3, "Converse e escolha"), 8.4), el(chat, 8.5, "up")),
        sc("light", 11.2, 12.8, el(step_label(4, "Avalie o serviço"), 11.2), el(rate, 11.3, "up")),
        endcard(12.8, D + 1, ["Grátis pra quem", "contrata e pra", "quem trabalha."]),
    ]
    return D, s

def render(name, builder, bpm=104):
    from playwright.sync_api import sync_playwright
    D, scenes = builder()
    html = page("".join(scenes), W, H, CSS) .replace("</body>", f"<script>{JS}setTime(0)</script></body>")
    fr = ROOT / "frames" / name
    shutil.rmtree(fr, ignore_errors=True); fr.mkdir(parents=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        pg.set_content(html, wait_until="load"); pg.wait_for_timeout(200)
        for i in range(int(D * FPS)):
            pg.evaluate(f"setTime({i / FPS})")
            pg.screenshot(path=str(fr / f"{i:04d}.jpg"), type="jpeg", quality=92)
        b.close()
    wav = ROOT / "out" / f"{name}.wav"
    subprocess.run([sys.executable, str(ROOT / "music.py"), str(D), str(wav), str(bpm)], check=True)
    mp4 = ROOT / "out" / f"{name}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", str(fr / "%04d.jpg"), "-i", str(wav),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-profile:v", "high",
                    "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-shortest", "-movflags", "+faststart", str(mp4)], check=True)
    # cover frame jpg
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(fr / f"{int(1.6*FPS):04d}.jpg"), str(ROOT / "out" / f"{name}_capa.jpg")], check=True)
    print(name, "ok", D)

if __name__ == "__main__":
    which = sys.argv[1:]
    B = {"amigo": (video_amigo, 104), "tomada": (video_tomada, 100), "15s": (video_15s, 108)}
    for k in which or B:
        render(k, *B[k])
