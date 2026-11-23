export const meta = {
  name: 'vsl-bar-ilustrado',
  description: 'Cria 130 b-rolls Hyperframe de barra (1080x844) que ILUSTRAM a fala de cada take (kicker+headline+elementos), nao legenda',
  phases: [{ title: 'Desenhar+Render', detail: 'lotes de takes por subagente' }],
}
const SCHEMA = { type:'object', additionalProperties:false, properties:{
  rendered:{type:'array',items:{type:'number'}}, failed:{type:'array',items:{type:'number'}}, notes:{type:'string'} },
  required:['rendered','failed','notes'] }

const NPX='npx'  // ou o caminho absoluto do npx (hook que reescreve npx: ver GOTCHAS da SKILL)
const ROOT='$HOME/videos-broll'
const N=130, BATCH=4, batches=[]
for(let i=0;i<N;i+=BATCH){const g=[];for(let j=i;j<Math.min(i+BATCH,N);j++)g.push(j);batches.push(g)}
log(`desenhando ${N} barras em ${batches.length} lotes`)

const BRIEF=`Você é motion designer. Vai criar b-rolls Hyperframe de BARRA HORIZONTAL (1080x844) que vão preencher a faixa preta de baixo de uma VSL. Cada barra ILUSTRA o que o apresentador fala naquele trecho.

## O MAIS IMPORTANTE (versao que so queima a frase e reprovada)
- NUNCA escreva a frase falada inteira como legenda. PROIBIDO.
- Em vez disso: ENTENDA a ideia da fala e crie um b-roll com KICKER curto (label de acento) + HEADLINE PUNCHY (resuma a ideia em 3-7 palavras, CAIXA ALTA) + ELEMENTOS VISUAIS que ILUSTRAM: numero contando, barra crescendo/encolhendo, icones, comparacao lado a lado, carimbo (back.out), seta, checklist, gauge. Igual aos b-rolls de um VSL profissional.
- Ex: fala "demitiu 4 mil pessoas" -> headline "−4.000 POSTOS" + numero gigante contando + barra de equipe encolhendo. Fala "agente atende 24h" -> headline "ATENDE 24H SEM PARAR" + icones de canais + relogio. Use a fala SO como inspiracao do conceito.

## ESTILO (leia o arquivo de referencia)
LEIA ~/.claude/skills/broll-faixa-hyperframe/assets/template-bar-1080x844.html pra absorver o estilo. Fundo #07090d com radial sutil; texto #f4f7fb; acento verde #19e08a (positivo/marca) e vermelho #ff4747 (dor/custo); apoio #8a93a3. Helvetica Neue 800 caixa alta, letter-spacing apertado. Guias verticais sutis. Movimento suave (power3.out/back.out/expo). Sem gradiente berrante, sem emoji, sem webfont (system font), sem audio.

## FORMATO BARRA (1080x844 — landscape, NAO portrait)
Composicao standalone 1080x844. Aproveite o espaco horizontal: kicker em cima/esquerda, headline grande (~80-104px, pode 2 linhas, max-width ~940), elementos (numeros/barras/icones) ao lado ou abaixo. Padding >=64px. O texto e os elementos tem que CABER em 1080x844 (rode inspect).

## CONTRATO HYPERFRAMES (quebrar = falha)
- index.html standalone: <div id="root" data-composition-id="barNNN" data-width="1080" data-height="844" data-start="0" data-duration="DUR"> direto no body, sem <template>. Root com width:1080px;height:844px;position:relative;overflow:hidden.
- Tudo numa <section class="scene clip" data-start="0" data-duration="DUR" data-track-index="1" style="position:absolute;inset:0">.
- GSAP via cdn.jsdelivr no head. UMA timeline paused, window.__timelines["barNNN"]=tl, construida sincrona. Estados iniciais via opacity:0 + fromTo. Sem Date.now/Math.random/repeat:-1. Numero contando = objeto proxy {v} com onUpdate. data-duration manda na duracao.

## FLUXO (por take)
1. cd ${ROOT}/barproj && cp -r ../broll11-hf bN (onde N=id) ... na verdade: mkdir -p ${ROOT}/barproj/d{id} && cp ${ROOT}/barproj/hyperframes.json ${ROOT}/barproj/d{id}/hyperframes.json
2. Escreva ${ROOT}/barproj/d{id}/index.html (1080x844, ilustrando a fala). data-composition-id="bar{id3}" (id com 3 digitos, ex bar007).
3. Valide e renderize (o hook quebra 'npx' — use o caminho absoluto e dangerouslyDisableSandbox=true):
   cd ${ROOT}/barproj/d{id} && ${NPX} --yes hyperframes@0.6.110 lint ; ... validate ; ... inspect ; ... render --quality high --output ${ROOT}/brolls/bar/bar-{id3}.mp4
   (corrija ate lint=0 e inspect=0; marque overlap intencional com data-layout-allow-overlap)
4. ffprobe confirma 1080x844 e a duracao. 
Retorne rendered (ids ok) e failed.`

const results=await parallel(batches.map((b)=>()=>{
  const id3=b.map(i=>String(i).padStart(3,'0')).join(', ')
  return agent(`${BRIEF}\n\n## SEUS TAKES: ids ${b.join(', ')} (id3 = ${id3}).\nLeia o arquivo ${ROOT}/barproj/specs130.json (array de {id,dur,fala}) e pegue a fala e a dur de CADA um dos SEUS ids. Para cada take, ILUSTRE a ideia da fala (NAO copie a frase). Saida: ${ROOT}/brolls/bar/bar-<id3>.mp4 pra cada um.`,
    { label:`barras ${b[0]}-${b[b.length-1]}`, phase:'Desenhar+Render', schema:SCHEMA, effort:'medium' })
}))
const rendered=results.filter(Boolean).flatMap(r=>r.rendered||[])
const failed=results.filter(Boolean).flatMap(r=>r.failed||[])
log(`render: ${rendered.length} ok, ${failed.length} falhas`)
return { rendered:rendered.length, failed }
