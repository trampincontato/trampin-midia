# Ferramentas de produção de conteúdo do TRAMPIN

- `kit.py`: identidade visual (cores, fonte Plus Jakarta Sans, logo, ícones) e renderizador PNG via Playwright.
- `slides.py`: posts estáticos e carrosséis (1080x1350 para IG/FB e 1080x1920 para TikTok).
- `video.py`: vídeos animados 9:16 (30 fps) e capas.
- `music.py`: trilha original gerada por código (sem direitos de terceiros).
- `posts.json`: legendas e calendário do lote 1 (modelo para os próximos).

Fluxo: renderizar → copiar mídias para `AAAA-MM-loteN/` → commit/push → usar
`https://raw.githubusercontent.com/trampincontato/trampin-midia/<sha>/<pasta>/<arquivo>` como mídia no Metricool.
