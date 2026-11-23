# Checklist de revisão de entregável de projeto (pt-BR)

Base do `ht-revisor-metodo-copy` para revisar **entregável de um projeto de expert** (oferta, roteiro, página, anúncio, plano,
cronograma, mensagem). Não serve para revisar as **skills** do plugin
(estrutura de SKILL.md, fontes das aulas, gatilhos). Cada item que falha é um achado numerado
no parecer, com arquivo, trecho, fonte e correção.

## 1. Entrada da revisão (antes de ler a peça)

- [ ] Li o pedido do Diretor (`00-plano/pedidos/`), a entrega do agente e **todos** os artefatos citados (não amostra).
- [ ] Sei qual oferta vale: vigente, ou proposta vN antes da Aprovação 1 (`ht-protocolo` §4 regra 4). Sem Aprovação 1, a peça
      precisa dizer "rascunho, oferta proposta vN"; **não reprovo por falta da vigente** nessa fase.
- [ ] Li `00-plano/decisoes.md` e `00-plano/variaveis.md` (versão citada no pedido).
- [ ] Abri o SKILL.md da skill que gerou a peça (critério de pronto e auditoria final).

## 2. Método e fidelidade

1. Toda regra, passo e número de método tem fonte (skill ou transcrição aberta). Reconstrução do squad está marcada como tal.
2. Número de aula aparece como "referência, conferir"; número do expert tem fonte (planilha, Hotmart, conta de anúncio).
3. **Número marcado como verificado é recalculado por mim**: refaço soma, média, porcentagem e faixa a partir do dado bruto
   (amostra de pelo menos 5 números ou todos, se forem menos). Faixa etária não vira idade exata; soma errada é achado grave.
4. Oferta idêntica ao arquivo de `02-oferta/` citado (preço, entrada, parcelas, dupla, bônus, garantia, duração, número de
   revisões ou sessões, quem entrega cada item). Ordem do preço entrada, parcelado, à vista (padrão `ordem_preco_sessao`);
   sinal de R$ 500 a R$ 1.000, até 10% do valor, pago com a call aberta (padrão `sinal_sessao`), salvo o que o perfil mudou.
5. O que a peça assumiu pelo padrão está listado em "Assumi" com código `PREFIXO-n` (`ht-protocolo` §6), em linguagem simples;
   preço e garantia aparecem como proposta até a Aprovação 1; data pública e verba nunca valem sem o OK da pessoa. Lote de
   perguntas ou opções a/b/c para a pessoa é achado (regra 16 do protocolo).
6. Nada de lançamento pago de evento como método, nem como benchmark de método.

## 3. Coerência entre peças irmãs

7. Nome do programa, promessa, Big Idea, nome da sessão (`03-sessao/nome-da-sessao.md`), dia e horário, destino do CTA e datas
   iguais aos de `00-plano/variaveis.md` e aos das peças irmãs do mesmo lote. Divergência entre duas peças é achado nas duas.
8. O que a peça promete existe na oferta: seeding, convite e anúncio só citam entregáveis que estão na oferta, com as mesmas
   quantidades e o mesmo responsável ("até 8 revisões pela consultora" não vira "revisão ilimitada com a expert").
9. Calendário: datas conferidas contra feriado e recesso; portão do um-para-muitos em D-15 do evento (`ht-protocolo` §3.6).
10. Conta de verba ou de meta fecha: a escada de verba somada dia a dia bate com o total; metas batem com o funil reverso do
    `ht-controller` (ou estão `[A CONFIRMAR COM ht-controller]`).

## 4. Copy e anti-IA em português

A skill `avoid-ai-writing` é escrita em inglês e as listas de palavras dela são do inglês. **Aplicar os critérios dela (estrutura,
ritmo, inflação, fecho genérico) ao texto em português**, sem procurar as palavras inglesas, e usar esta lista pt-BR:

11. **Muletas banidas**: "genuinamente", "honestamente", "sinceramente", "simples assim", "na real", "vale ressaltar", "é importante
    notar", "em suma", "basicamente", "de forma geral", "no fim do dia", "é sobre isso", "não é sobre X, é sobre Y", "jornada"
    (fora do sentido do método), "potencializar", "alavancar" (fora do sentido das 4 alavancas), "transformador", "virada de chave".
12. **Estrutura de IA**: tricolon genérico (três adjetivos ou três frases paralelas sem conteúdo); travessão como vírgula; série de
    perguntas retóricas; abertura que repete a pergunta; fechamento que resume o que acabou de dizer; frase-slogan solta no fim
    do parágrafo; negrito espalhado; lista de substantivos soltos.
13. **Inflação**: "incrível", "poderoso", "único", "revolucionário", "definitivo" sem prova; promessa sem número, prazo ou
    mecanismo.
14. **Voz**: o texto soa como o expert (`08-copy/big-idea-e-voz/voz-<slug>.md` ou a transcrição dele), não como modelo genérico.
    pt-BR com acentuação; sem anglicismo desnecessário.
15. **Bajulação** no texto ao estrategista ("ótima ideia", "excelente pergunta") é achado.
16. **Absolutos sem lastro**: "sempre", "nunca", "garantido", "100%", "todo mundo" em fala de venda.

## 5. Compliance Meta e conselho profissional (todo anúncio, Reels impulsionado e página de destino de anúncio)

17. **Atributo pessoal**: o texto não afirma nem insinua atributo do leitor (idade, condição de saúde, peso, situação financeira,
    desemprego, religião, etnia, orientação sexual, deficiência, situação jurídica). Idade pode ser **segmentação**, nunca frase
    ("você que tem mais de 40", "você que está desempregada"). Reescrever na terceira pessoa ou pelo problema ("profissionais que
    querem entrar na indústria depois de anos em outra área").
18. Sem promessa de renda, emprego, contratação, cura ou resultado garantido; escassez e prazo reais; antes e depois sob risco.
19. Profissão regulada (saúde, odontologia, psicologia, direito) respeita o conselho; resultado de paciente só com OK do estrategista.
20. Campanha descrita como PAUSADA, com o prefixo de campanha do perfil (`trafego.prefixo_campanha`) se houver; nada diz que foi publicado, enviado ou ligado.

## 6. Operacional

21. Quem vai usar a peça executa do começo ao fim: falas, tempos (dentro do teto da skill: sessão 1h30; objeções 5 a 10 min no
    fechamento), CTA, destino do link, dono de cada passo, horário de atendimento (SLA fora do horário tem dono ou regra).
22. Lacunas marcadas `[FALTA: …]` ou `[A CONFIRMAR COM <dono>]`, nunca preenchidas por suposição.
23. Dado de lead e aluno fora do material público; prova só com `06-entrega/provas/autorizacoes.md` (ausente = nenhuma).

## 7. Veredito

- **Reprovado**: preço ou oferta divergente, número inventado ou conta errada marcada como verificada, compliance grave
  (atributo pessoal, promessa de resultado), decisão do estrategista tomada pela peça.
- **Aprovado com ajustes**: achados que o agente corrige sem nova decisão.
- **Aprovado**: os itens aplicáveis conferidos e marcados; o que não deu para conferir está listado com o motivo.
