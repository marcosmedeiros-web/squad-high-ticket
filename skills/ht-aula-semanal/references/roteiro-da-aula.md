# Roteiro da aula semanal

Marcação: **[FHT]** = do material; **[proposta da skill]** = organização desta skill.
O roteiro é guia em tópicos para o expert conduzir; nunca texto para ler. Testar os dois modelos; se o estilo do expert já
funciona, não está errado. [FHT]

## 1. Modelo 1: jeito errado x jeito certo [FHT, estrutura do GPT de roteiro, trilha 14 Parte 1]

Minutagem para 1 h [proposta da skill; a fonte dá minutagem para 40 min no GPT e só a saudação com tempo fixo]

| Bloco | O que entra | Tempo |
|---|---|---|
| 1. Saudação e quem sou | Cumprimento, pedir no chat se ouvem bem, chamar pelo nome quem entra; credencial e quantas pessoas já ajudou (só número real) | 2 a 3 min |
| 2. Promessa das aulas | Frase fixa: "toda [dia] às [hora], para [avatar] que quer [promessa]" | 15 s |
| 3. Tema de hoje | "E hoje vamos falar sobre [tema]" | 15 s |
| 4. História / procedência | De onde vem o conteúdo e por que o expert pode ensiná-lo (caso, anos, resultado com print se houver). Caso de aluno: mais transformação que problema. Seeding aqui | 3 a 8 min |
| 5. Contexto | O que é o tema e o que não é; o que não será falado hoje | 3 min |
| 6. Benefício | Por que ficar até o fim; 1 a 3 casos de gente parecida com o avatar (contar, foto, vídeo); 1 a 3 objeções da live ("será que serve para mim?") quebradas na hora. Sem caso autorizado: só objeções | 5 a 8 min |
| 7. Como | Primeiro o jeito errado (o erro mais comum e por que falha), depois o jeito certo em 3 a 4 passos | 25 a 30 min |
| 8. Aprendizado | "Me conta no chat o que você mais aprendeu; não vale falar tudo" | 3 min |
| 9. CTA | Ver `cta-nps-e-pergunta-da-sessao.md` | 3 a 5 min |
| 10. Antecipação | Próxima aula: data, mesmo horário, mesmo canal, tema se já houver | 1 min |

Por que o jeito errado primeiro: o expert acha o básico óbvio, e o aluno muitas vezes só aprende pelo erro. [FHT]
O aprendizado no chat fixa o conteúdo, mostra o nível de consciência, gera tema e deixa chamar a pessoa pelo nome. [FHT]

## 2. Modelo 2: aulão [FHT, modelo do apresentador da Live FHT]
Saudação · promessa das aulas · tema de hoje · história/procedência (explicação racional de onde veio o conteúdo) · seeding em
qualquer ponto · conteúdo corrido do começo ao fim (pode mostrar planilha, mapa mental) · CTA · antecipação.
Rota 3 dá a mesma espinha: promessa, prova/história/procedência, conteúdo, CTA.

## 3. Seeding [FHT]
Mencionar com naturalidade os alunos do programa, um resultado, como o acompanhamento funciona, sem preço e sem pitch. Pode ser
em qualquer bloco e também nos stories. Prova só real e autorizada (`06-entrega/`, `ht-provas-e-cases`).

## 4. Interação [FHT]
Responder pontual e estrategicamente, às vezes para quebrar objeção. Pergunta fora do tema: "não é desta aula", ou vira tema.
Aula gravada (Estreia): dizer que é gravada e que a equipe responde depois. No YouTube há atraso de 30 a 40 s.
Opcional (rota 3): perguntas e respostas no fim, depois do CTA; as dúvidas viram temas das próximas aulas. [FHT]

## 5. Molde do arquivo `roteiro-aula-NNN.md` [proposta da skill]
```
Aula nº [NNN] · [data] · [dia] [hora] (Brasília) · Modelo [1/2]
Títulos de capa (3): 1) .. 2) .. 3) ..   (recomendado: ..)
Âncora trabalhada: [..]   Objetivo de consciência: [..]
1 Saudação e quem sou: [credencial real] · [FALTA se não houver número]
2 Promessa das aulas: "[frase fixa]"
3 Tema: "[..]"
4 Procedência: [..]  · SEEDING: [..]
5 Contexto: é [..] / não é [..]
6 Benefício: casos [ref. em 06-entrega] · objeções da live: 1) .. → quebra .. 2) ..
7 Como: jeito errado [..] · jeito certo: passo 1 .. passo 2 .. passo 3 .. (passo 4)
8 Aprendizado: pergunta ao chat
9 CTA: presente [..] · pergunta da sessão [nome da sessão 1a1] · destino alternativo [..]
10 Antecipação: [data e tema da próxima]
Revisão: [ ] sem preço  [ ] sem pitch do HT  [ ] provas autorizadas  [ ] 1 CTA principal
```

## 6. Prompt de rascunho [proposta da skill; o GPT "Roteiro de Aula Semanal" da FHT não está nos arquivos]
```
Você vai rascunhar o roteiro em tópicos de uma aula ao vivo de 1 hora.
Expert: [quem é, credencial real]. Avatar: [..]. Promessa das aulas: "[..]". Tema: "[..]".
Use o modelo: saudação, promessa das aulas, tema, procedência, contexto (o que é e o que não é),
benefício (casos: [lista real ou "nenhum"]; 3 objeções desta aula), como (jeito errado e jeito certo em 3 a 4 passos),
aprendizado no chat, CTA [descrição], antecipação. Marque onde cabe seeding. Não invente número, caso
nem depoimento; onde faltar, escreva [FALTA]. Nada de preço nem oferta do programa. Dê 3 títulos de capa.
```
Depois: ajustar à voz do expert e cortar o que ele não diria. A IA destrava; a curadoria é humana. [FHT]
