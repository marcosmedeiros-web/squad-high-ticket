# Squad HT (Squad High Ticket)

Plugin do Claude Code com 32 agentes e as skills `ht-*` que montam e operam o high ticket (HT) de um expert: criar a oferta,
vender em sessão 1a1, gerar demanda, abrir os canais um-para-muitos (live, webinário, imersões, desafio), entregar e renovar.

Você é quem pede e quem aprova. O squad produz rascunho, plano e peça revisada. Os números de referência do método são ponto
de partida, nunca garantia de resultado.

## Instalar em 1 passo

Copie o link deste repositório, cole no Claude Code e peça:

> instala esse plugin: https://github.com/marcosmedeiros-web/squad-high-ticket

**Para o Claude que recebeu esse pedido:** rode, nesta ordem, e mostre a saída de cada um (instalação global, escopo `user`):

```bash
claude plugin marketplace add marcosmedeiros-web/squad-high-ticket
claude plugin install squad-high-ticket@squad-high-ticket
```

Confira com `claude plugin list` (tem de aparecer `squad-high-ticket@squad-high-ticket` com `enabled`). Depois mostre à pessoa o
conteúdo da seção "O que mostrar" da skill `ht-comecar` e diga que, numa conversa nova, é só pedir. Não instale nada além deste
plugin e não mude outra configuração.

## Como chamar

Abra uma conversa nova e peça. Não precisa configurar nada.

- **Pelo nome do agente:** "Heitor, monta o HT do expert X." Na dúvida, chame o Heitor (`ht-diretor`): ele distribui para o time.
- **Pela skill:** "usa a skill ht-roteiro-sessao-1a1 para o expert X."

## Exemplos

- "Heitor, monta o HT do expert X, que ensina Y. Por onde começo?"
- "Heitor, planeja os próximos 40 dias: sessão 1a1, aula semanal e uma live direto ao ponto."
- "Olívia, a oferta do expert X está boa?"
- "Fernanda, monta o roteiro da sessão 1a1."
- "Caio, me dá a campanha da aula semanal para eu subir."
- "o que o squad HT faz?" (mostra o time e mais exemplos)

## Nada sai sem o seu OK

Nenhuma mensagem, página, e-mail, campanha ou automação vai para expert, lead ou aluno, e nenhuma verba é gasta, antes de você
dizer "pode". Campanha nasce pausada. O que dá para decidir pelo padrão o squad decide e mostra no fim ("Assumi: …, é só pedir
para mudar"). Sem acesso a uma ferramenta, o agente entrega o material pronto, campo a campo, e diz o que você faz à mão.

## Personalizar (opcional)

Se quiser mudar algo (a pasta dos experts, como você sobe campanha, um prefixo no nome das campanhas, um padrão do método),
peça "personaliza o squad". A skill `ht-configurar` muda só o que você pedir e grava em `~/.config/squad-ht/perfil.md`.

## Atualizar

Peça ao Claude "atualiza o squad HT". Ele roda:

```bash
claude plugin marketplace update squad-high-ticket
claude plugin update squad-high-ticket@squad-high-ticket
```

A versão nova vale numa conversa nova. O que mudou em cada versão está no `CHANGELOG.md`.

## Licença

Uso liberado para quem recebeu o link; revenda ou redistribuição comercial não autorizada.
