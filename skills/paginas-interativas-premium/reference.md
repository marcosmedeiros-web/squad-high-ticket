# Reference — Páginas Interativas Premium (linha escura cinética)

Passo a passo completo do método, com as constantes e os snippets prontos. Tarefa de código: quem executa é o Paulo; a Turbo confere e entrega.

---

## 0. Quando esta skill se aplica

Página-vitrine que precisa de movimento e impacto: hero com vídeo de fundo, animação ao rolar, rastro de mouse, "para o scroll e diz uau". É a versão React/cinética. Se o pedido é funil editorial (bege, serifa, jornal, HTML estático), é a outra skill (`landing-funil-editorial`).

---

## 1. STACK / COMBO (o papel de cada ferramenta)

### 21st.dev Magic (MCP `21st-magic`)
- Servidor MCP que dá acesso a componentes React prontos + inspiração de layout.
- **Usar SÓ a tool de INSPIRAÇÃO** (busca/ideação de componentes). Ela funciona **headless** no nosso ambiente (servidor sem browser interativo).
- **NÃO usar o `component_builder`** — ele **não roda headless** aqui. Em vez de chamar e travar, pegar a inspiração e **escrever o componente à mão** no nosso stack/paleta.
- Pra que serve na prática: mineração rápida de padrões de hero, navbar, card, footer animados — depois adaptamos pra paleta e pras primitives da casa.

### Framer Motion (`framer-motion@11.3.19`, pinado)
O motor de toda a cinética. Os recursos que esta linha usa:
- **Scroll-reveal** com fade + slide + **blur-in** (`whileInView`, `viewport: { once: true }`).
- **Parallax scroll-driven** com `useScroll({ target, offset })` + `useTransform` (a copy do hero sobe e some, o vídeo desce e escala — profundidade).
- **Barra de progresso de scroll** com `useScroll` + `useSpring` (`scaleX`).
- **Botão magnético** (puxa pro cursor com spring).
- **Tilt 3D** (card rotaciona pro cursor, perspectiva).
- **Count-up** (número anima de 0 ao alvo quando entra na tela).
- **Sticky storytelling** (seção fixa enquanto o conteúdo interno avança no scroll).

### UI/UX Pro Max
Biblioteca de estilos/paletas/pares de fonte pra o output parecer DESENHADO, não gerado. Aqui a identidade já está travada (preto + emerald + gold + Geist/Fira Code), então o uso é: confirmar densidade, hierarquia tipográfica e estados (hover/foco) coerentes, e evitar os anti-padrões de "AI slop" (gradiente arco-íris, card com borda-esquerda colorida genérica, fonte batida, emoji fora de marca).

### Hyperframes (vídeo de background)
- Gera o **loop 3D** do fundo (three.js/shaders) e **renderiza pra mp4 via CLI**.
- O de referência é uma **rede neural** (esfera de nós conectados girando) na paleta emerald/cyan com toques de gold sobre quase-preto.
- Depois do render, **SEMPRE** passar no ffmpeg pra (a) **desacelerar** o giro (`setpts`) e (b) **otimizar/comprimir** (720p, H.264 CRF alto, sem áudio, `+faststart`). Ver §5.

Base do projeto (`package.json`):
```json
{
  "dependencies": {
    "framer-motion": "11.3.19",
    "lucide-react": "0.383.0",
    "react": "18.3.1",
    "react-dom": "18.3.1"
  },
  "devDependencies": {
    "tailwindcss": "3.4.7",
    "vite": "5.4.0",
    "@vitejs/plugin-react": "4.3.1"
  },
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview --host 0.0.0.0 --port 4321"
  }
}
```

---

## 2. PADRÃO VISUAL — fundo preto + 3 camadas + conteúdo

### 2.1 Montagem e z-index (verbatim do `App.tsx`)
```tsx
<div className="relative min-h-screen bg-black">
  <VideoBackground src="/video/neural-bg.mp4" poster="/video/neural-poster.jpg" />
  <AuroraShader />
  <PixelSpotlight />

  {/* barra de progresso de scroll no topo */}
  <motion.div
    className="fixed left-0 right-0 top-0 z-50 h-[3px] origin-left bg-gradient-to-r from-emerald via-emerald-soft to-gold shadow-glow"
    style={{ scaleX: progress }}
  />

  <Navbar />
  <main className="relative z-10">{/* seções */}</main>
  <Footer />
</div>
```
Camadas de fundo a `z-0`; rastro a `z-2`; conteúdo a `z-10`; barra de progresso a `z-50`. O `progress` é `useSpring(useScroll().scrollYProgress, { stiffness: 120, damping: 30, restDelta: 0.001 })`.

> Uma versão chegou a ter um `MatrixRain`. Foi **REMOVIDO** porque poluía o fundo — o padrão final é só vídeo + aurora + rastro.

### 2.2 VideoBackground — o vídeo é DETALHE, não protagonista
Constantes que controlam a discrição (mudar só estes números pra recalibrar):
```ts
const VIDEO_OPACITY = 0.30;       // <video> sobre o preto: ~70% do preto aparece
const BLACK_SCRIM_OPACITY = 0.55; // scrim preto POR CIMA do vídeo, antes do conteúdo
// efetivo: 0.30 * (1 - 0.55) ≈ 0.135 → a rede neural lê BEM apagada, mas perceptível
```
Estrutura: `<div fixed inset-0 z-0 bg-black>` contém o `<video autoPlay muted loop playsInline preload="auto" object-cover>` a `opacity:VIDEO_OPACITY`, e por cima um `<div bg-black>` a `opacity:BLACK_SCRIM_OPACITY`. O scrim fica ATRÁS do conteúdo (z-0), então escurece o vídeo sem nunca tocar o texto.
- Abordagem LIMPA: a discrição vem do **opacity do próprio vídeo + scrim preto**, NÃO de scrims radiais empilhados. Dois scrims radiais antigos foram removidos por redundância.
- `prefers-reduced-motion` → mostra o `poster` estático (mesmo `VIDEO_OPACITY`), sem playback. Pausa o vídeo quando a aba fica oculta.

### 2.3 AuroraShader — vida residual em WebGL
```ts
const AURORA_OPACITY = 0.18; // screen blend → só um respiro de luz emerald/gold
```
- Full-screen triangle + 1 fragment shader FBM (domain-warped) → aurora lenta que reage ao cursor (`u_mouse` com easing 0.04). Paleta baked: bg `#050806`, emerald `#1fe07a`, gold `#e8c66b`. Grain animado anti-banding (dá o "feel de vídeo").
- `devicePixelRatio` capado em 1.5; pausa rAF com aba oculta; `prefers-reduced-motion` → 1 frame estático; se WebGL faltar, a `.bg-aurora` CSS por baixo aparece (fallback gracioso).
- Render a `style={{ opacity: AURORA_OPACITY, mixBlendMode: "screen" }}`.

### 2.4 PixelSpotlight — o rastro de mouse (todos os knobs)
Os valores APROVADOS (verbatim), com o porquê:
```ts
const LIFE = 1275;        // ms que cada amostra vive → fade-out total ~1.5s ao parar (refino "50% mais lento")
const STEP = 7;           // px do stamp ao longo da cauda (fino, textura de pixel)
const SPACING = 6;        // px entre stamps interpolados (densidade da linha)
const MAX_SAMPLES = 135;  // ring buffer (+50% de comprimento de cauda)
const PEAK_ALPHA = 0.18;  // brilho no HEAD — baixo → NUNCA lava o texto
const MIN_MOVE = 1.2;     // px; ignora micro-jitter pra cauda realmente sumir parada
// espalhamento (pluma, não fio reto):
const PARTICLES = 5;      // stamps por amostra do caminho
const SPREAD_HEAD = 6;    // px de espalhamento lateral perto do head (apertado)
const SPREAD_TAIL = 24;   // px no fim da cauda (volumétrico)
const EMERALD = [31,224,122];  // head
const GOLD = [232,198,107];    // cauda
```
Como funciona: mantém um histórico `{x,y,t}` das últimas posições; densifica interpolando stamps entre uma posição e a próxima (flick rápido ainda desenha linha contínua); cada amostra carrega uma "nuvem" de partículas pré-sorteada (estável entre frames, sem shimmer) espalhada perpendicular ao movimento — apertada no head, larga na cauda → **pluma volumétrica**, não fio. Alpha = peso ao longo da cauda × decay por idade; após `LIFE` ms a amostra some, então **mouse parado = cauda some 100% em ~1.5s**. Limpa o canvas todo frame e redesenha só a cauda curta (barato). Blend `lighter`/`screen` com alpha baixo = glow suave sobre o vídeo, nunca wash sobre o texto.

Disciplina de performance: 1 canvas 2D + rAF; `devicePixelRatio` capado em 1.5; PARA o loop quando a cauda esvazia + mouse ocioso, reinicia no próximo `pointermove`; pausa com aba oculta; `prefers-reduced-motion` → não desenha nada.

Render: `<canvas aria-hidden fixed inset-0 pointer-events-none>` a `style={{ zIndex: 2, mixBlendMode: "screen" }}`.

> História do rastro (pra não repetir o erro): a 1ª versão era uma **mancha verde forte e PARADA** que lavava o texto do hero → reprovada. O certo é cauda FINA que segue o caminho, sutil (`PEAK_ALPHA 0.18`), espalhada (pluma) e que SOME ao parar. Refinos do Chefe: (a) mais espalhado + mais transparente; (b) 50% mais lento + 50% mais comprido (`LIFE` e `MAX_SAMPLES`); (c) escurecer o overlay do vídeo mais +50%.

---

## 3. CINÉTICA DO CONTEÚDO — primitives Framer (snippets reais)

Arquivo `src/components/primitives.tsx` + hooks em `src/lib/interactions.ts`.

### 3.1 Reveal (fade + slide + blur-in)
```tsx
<MotionTag
  initial={{ opacity: 0, y, x, filter: "blur(8px)" }}
  whileInView={{ opacity: 1, y: 0, x: 0, filter: "blur(0px)" }}
  viewport={{ once: true, margin: "-60px" }}
  transition={{ duration: 0.75, ease: [0.22, 1, 0.36, 1], delay }}
/>
```
Easing da casa: `[0.22, 1, 0.36, 1]`. Stagger em listas via `containerVariants`/`itemVariants` (staggerChildren 0.1).

### 3.2 Parallax scroll-driven (hero) — verbatim do `Hero.tsx`
```tsx
const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end start"] });
const copyY       = useTransform(scrollYProgress, [0, 1],   [0, -120]); // copy sobe
const copyOpacity = useTransform(scrollYProgress, [0, 0.7], [1, 0]);    // e some
const videoY      = useTransform(scrollYProgress, [0, 1],   [0, 80]);   // vídeo desce
const videoScale  = useTransform(scrollYProgress, [0, 1],   [1, 1.06]); // e escala
const glowY       = useTransform(scrollYProgress, [0, 1],   [0, 160]);  // glow em outra velocidade
```

### 3.3 Botão magnético (`useMagnetic`)
Puxa o elemento pro cursor com spring (`stiffness 220, damping 18, mass 0.4`), volta ao centro no leave. No componente: `shimmer-btn` coral + `shadow-glow-coral`, `whileHover scale 1.04`, `whileTap 0.97`. O CTA aponta pro checkout REAL (na V2, Hubla).

### 3.4 Tilt 3D (`useTilt`)
Card rotaciona pro cursor (`rotateX/rotateY` com spring), `perspective: 900` no pai, `transformStyle: preserve-3d`. Usado no frame do VSL e em cards de destaque.

### 3.5 Count-up (`useCountUp`)
Anima 0 → alvo (`duration 1.6`, mesmo easing) quando entra na view (`useInView once`). Render com `toLocaleString("pt-BR")`. Usado nos números de prova social (stats).

---

## 4. CAPTURAR A OFERTA 1:1 (`data.ts`)

Centralizar TODO o conteúdo num `src/data.ts`, copiado **1:1 da produção** (a página que a V2 vai substituir). Cabeçalho do arquivo:
```ts
/* Real offer content captured 1:1 from <sua-pagina-de-producao> (production).
   Accentuation corrected to proper Brazilian Portuguese. */
```
Exporta arrays/objetos: agentes, problemas, semanas, entregáveis, pra-quem, stats (com value/prefix/suffix pro count-up), itens da oferta, FAQ, texto de bio, e o embed do VSL. **Regras:** não inventar nada (preço, bullets, garantia, FAQ idênticos à base); corrigir só a acentuação pra PT-BR correto; sem travessão em copy (regra da casa).

---

## 5. GERAR + OTIMIZAR O VÍDEO DE FUNDO (Hyperframes → ffmpeg)

1. **Hyperframes**: gerar o loop 3D na paleta (rede neural / partículas / shader lento) e renderizar pra mp4 via CLI.
2. **Desacelerar** o giro pra ficar BEM lento (reencodar pra ~30% da velocidade, alongando o loop — `playbackRate` fica 1.0 porque desaceleramos no arquivo, não via hack de runtime). Em ffmpeg, o filtro de vídeo é `setpts` (fator > 1 deixa mais lento; ex.: `setpts=3.33*PTS` ≈ 30% da velocidade). Sem áudio, então não há `atempo`.
3. **Comprimir/otimizar** pra web: escalar pra **1280×720**, **H.264 CRF alto** (CRF ~30 = leve e ainda bonito de fundo), **sem áudio** (`-an`), **`+faststart`** (streama sem travar a página). Alvo: poucos MB — a V2 saiu de ~15MB pra ~1.8MB master.
4. **Guardar um backup** do master original (ex.: `neural-bg.original.BACKUP.mp4`) e servir o otimizado em `public/video/neural-bg.mp4` + um `neural-poster.jpg` (frame estático leve pro `poster`/reduced-motion).

Forma geral do re-encode (slow + 720p + leve + faststart, sem áudio):
```
ffmpeg -i master.mp4 -vf "setpts=3.33*PTS,scale=1280:720" -an \
  -c:v libx264 -crf 30 -preset slow -movflags +faststart neural-bg.mp4
```
(Ajustar o fator do `setpts` e o CRF na calibragem; validar peso + duração depois.)

---

## 6. CALIBRAR

Mexer SÓ nas constantes (não reescrever os componentes):
- Vídeo discreto demais / de menos → `VIDEO_OPACITY` e `BLACK_SCRIM_OPACITY`.
- Aurora forte/fraca → `AURORA_OPACITY`.
- Rastro lavando o texto → baixar `PEAK_ALPHA`; muito reto → subir `SPREAD_TAIL`/`PARTICLES`; rápido/curto demais → subir `LIFE`/`MAX_SAMPLES`.
- Giro do vídeo rápido demais → aumentar o fator do `setpts` no re-encode.
Critério de aceite: o vídeo é detalhe, o rastro é sutil e some ao parar, e o **texto fica 100% legível em toda seção**.

---

## 7. PUBLICAR EM PRÉVIA (padrão: publicar-pagina-cloudflare --previa · alternativa: Vercel REST API, NUNCA o CLI)

> Padrão do kit: `vite build` → `dist/` → `bash ~/.claude/head-turbo/bin/com-cofre.sh bash ~/.claude/head-turbo/bin/publicar-pagina-cloudflare.sh dist <projeto> --previa` (prévia em `https://previa.<projeto>.pages.dev`, produção intocada, conferida de fora). O `deploy.mjs` abaixo é a alternativa Vercel.

Padrão do `deploy.mjs`. **NUNCA `vercel` CLI** (já invadiu outro projeto antes). Sempre REST API com project + team pinados:
```
TEAM = "<VERCEL_TEAM_ID>"
PROJECT_ID  = "prj_..."            // o id do projeto preview desta página
PROJECT_NAME = "<projeto>-v2"  // exemplo
```
Fluxo: `vite build` → `dist/` → para cada arquivo, `POST https://api.vercel.com/v2/files?teamId=...` com header `x-vercel-digest: <sha1>` (upload por sha) → `POST https://api.vercel.com/v13/deployments?teamId=...&forceNew=1` com `{ name, project, target:"production", files:[{file,sha,size}], projectSettings:{framework:null,...} }` (deployment **prebuilt** estático). Token via `VERCEL_TOKEN` (do cofre 1Password / .env). Imprime `DEPLOY_URL` + `READY_STATE`.

> É **sempre uma V2/preview pra aprovar**. NUNCA tocar produção. A promoção / apontamento de domínio é decisão do Chefe depois do OK.

---

## 8. VALIDAR COM VÍDEO (Playwright — print NÃO prova animação)

Gravar um screencast headless que prova as 3 coisas ao mesmo tempo: (1) o vídeo de fundo girando lento + discreto, (2) o rastro seguindo o mouse 1:1 e **sumindo ~1.5s ao parar**, (3) a copy legível por cima de tudo, em todas as seções.

Esqueleto (`screencast-*.py`):
```python
b = p.chromium.launch(headless=True, args=[
    "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader",  # WebGL headless (aurora)
    "--autoplay-policy=no-user-gesture-required",                                 # vídeo dá play sem gesto
    "--no-sandbox", "--disable-dev-shm-usage",
])
ctx = b.new_context(viewport={"width":1366,"height":820}, device_scale_factor=1,
                    record_video_dir=str(CAST), record_video_size={"width":1366,"height":820},
                    reduced_motion="no-preference")
```
Roteiro: varrer o mouse pelo hero (cauda óbvia) → **parar o mouse e esperar ~1.4s** (prova o fade-out) → segurar parado um beat (giro lento do vídeo sem mouse competindo) → scroll lento topo→fim mexendo o mouse (bg discreto + copy legível por seção) → stills de fidelidade (hero + uma seção interna). Asserts úteis no runtime: `document.querySelectorAll('canvas').length` (MatrixRain removido → contagem esperada), `video.duration`/`playbackRate`/`opacity`/`currentTime` (provar slow + tocando), e os `opacity`/`backgroundColor` das divs de scrim. O Playwright grava **webm**; converter pra **mp4** com ffmpeg pra entregar pro Chefe.

---

## 9. OTIMIZAR MOBILE (1ª dobra cheia)

Auditar em viewport REAL de celular (`is_mobile=True`, `has_touch=True`, dpr 3, UA de iPhone), nas larguras **390** (iPhone 12/13) e **360** (Android pequeno). Medir e corrigir:
- **Sem overflow horizontal** (`document.documentElement.scrollWidth - innerWidth == 0`).
- **CTA primário acima da dobra** (`getBoundingClientRect().bottom <= innerHeight`).
- 1ª dobra com hero completo (badge + h1 + subtítulo + CTA), tipografia em `clamp()` que cabe.
Capturar o fold com `clip={x:0,y:0,width:W,height:H}` (o que o usuário vê sem rolar) + 1 full-page + 1 scroll. Entregar prints mobile fold/scroll junto da prova desktop.

> Pegadinha de Playwright mobile: NÃO usar vídeo full_page (crash de FrameInfo); usar `page.screenshot` com `clip`/`full_page=True` em PNG.

---

## 10. CHECKLIST DE ENTREGA (Paulo → Turbo → Chefe)

- [ ] Conteúdo/oferta 1:1 da base, acentuação PT-BR correta, sem travessão.
- [ ] Fundo preto + vídeo Hyperframes discreto (opacity + scrim) + aurora 0.18 + rastro 0.18 que some ao parar.
- [ ] Vídeo otimizado (720p, CRF alto, sem áudio, faststart, poucos MB); backup do master guardado.
- [ ] Reveal/parallax/magnetic/tilt/count-up funcionando; `prefers-reduced-motion` respeitado.
- [ ] Prévia publicada (`publicar-pagina-cloudflare --previa`, linha CONFERIDO; na alternativa Vercel: REST API com teamId/project pinados, **sem CLI**), produção intocada.
- [ ] PROVA em VÍDEO do scroll + mouse (não só print) + prints mobile fold (390/360) sem overflow, CTA na dobra.
- [ ] Subagente devolve texto/links pra Turbo (NUNCA escreve no outbox/Telegram).

---

## Anti-padrões (não fazer)
- Vídeo de fundo protagonista / forte / sem otimizar (peso) → ele é DETALHE.
- Rastro de mouse forte ou parado que lava o texto.
- `component_builder` do 21st (não roda headless aqui).
- `vercel` CLI pra deploy.
- Mexer na produção, ou na pasta de um projeto enquanto outro agente está editando.
- Paleta editorial bege/coral (essa é a outra skill).
- Entregar só print como prova de animação.
- Arquivo > 1000 linhas; `const styles = {}` genérico (nomear único por componente); valor arbitrário de Tailwind tipo `h-[600px]` (preferir classe core).
