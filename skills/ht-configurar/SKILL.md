---
name: ht-configurar
description: 'Personalização opcional do Squad HT: muda só o que a pessoa pedir (pasta dos experts, ferramenta e prefixo de campanha, padrões do método) e grava em ~/.config/squad-ht/perfil.md. Use em "personaliza o squad", "muda o prefixo de campanha", "minha pasta de experts é outra", "mostra meu perfil". NÃO usar para montar o HT de um expert (ht-diretor).'
---

# Personalizar o Squad High Ticket (opcional)

## 1. Para que serve

O squad funciona sem configurar nada: sem perfil, todo agente usa os padrões recomendados do `ht-protocolo` (seção 5), chama a
pessoa de "você", guarda cada expert em `~/squad-ht/<expert>/ht/` e, no tráfego, entrega a campanha campo a campo para subir à
mão no Gerenciador de Anúncios. Esta skill existe só para quem **quer** mudar algum desses pontos. Ela roda quando a pessoa
pede; nenhum agente a oferece nem a sugere.

Modelo com todos os campos e os valores padrão: `references/perfil-modelo.md`.

## 2. Como funciona (curto, sem questionário)

1. Ver se `~/.config/squad-ht/perfil.md` existe e, se existir, ler.
2. **O pedido já diz o que mudar** ("uso a Meta Ads CLI", "prefixo [SQUAD HT]", "minha pasta é ~/clientes", "sinal de R$ 300"):
   mudar só isso. Não perguntar mais nada.
3. **O pedido é genérico** ("personaliza o squad"): mostrar em 5 linhas simples o que dá para mudar e perguntar uma única vez
   "O que você quer mudar?". As opções:
   - como você quer ser chamado (`estrategista`) e o nome da sua empresa (`agencia`);
   - a pasta onde ficam os experts (`raiz_projetos`; padrão `~/squad-ht`);
   - como você sobe campanha (`trafego.ferramenta`; padrão: o gestor entrega tudo campo a campo e você sobe no Gerenciador) e
     um prefixo no nome das campanhas (`trafego.prefixo_campanha`; padrão: sem prefixo);
   - algum padrão do método (ex.: valor do sinal, duração da sessão), pela chave da seção 5 do `ht-protocolo`.
   Se a resposta for "nada" ou "tá bom assim", não grava nada e encerra.
4. Mostrar antes e depois de cada campo, numa linha ("prefixo de campanha: vazio → [SQUAD HT]"), e gravar com o OK da pessoa.
   "Pode", "ok" e "sim" valem como OK.
5. Gravar: criar `~/.config/squad-ht/` se não existir; se já houver perfil, copiar o atual para
   `~/.config/squad-ht/historico/perfil-AAAA-MM-DD-HHMM.md` antes; gravar só os campos mudados (o resto fica como estava ou no
   padrão do modelo), com permissão 600 (`chmod 600`).
6. Conferir que o bloco YAML carrega (ex.: `python3 -c "import yaml,re,sys; t=open(sys.argv[1]).read();
   yaml.safe_load(re.search(r'```yaml\n(.*?)```', t, re.S).group(1))" ~/.config/squad-ht/perfil.md`). Falhou: voltar a cópia do
   histórico e avisar.
7. "Mostra meu perfil": exibir o resumo, sem editar. Sem perfil: dizer que está tudo no padrão.

Mudança de padrão vale para os projetos a partir de agora. Para mudar só num projeto, a mudança vai em `00-plano/decisoes.md`
daquele projeto (pelo ht-diretor), que vence o perfil ali.

## 3. Regras

- Uma pergunta só, e só quando o pedido for genérico. Nada de passar campo por campo.
- Nunca gravar senha, token, chave de API ou dado de cliente no perfil. Se a pessoa colar um token, não gravar e avisar que ele
  deve ser trocado.
- A skill não muda nada sem o OK e não inventa valor.
- Os nomes dos agentes são fixos (tabela da seção 2.1 do `ht-protocolo`) e o `name` técnico (`ht-closer` etc.) também: não se
  trocam aqui nem em lugar nenhum.
- Se a mudança de padrão contraria o método, gravar como a pessoa pediu e acrescentar na linha o comentário
  `# diverge do padrão recomendado: <valor recomendado>`.

## 4. Critério de pronto

- [ ] Mudou só o que a pessoa pediu; nenhuma pergunta além da única do passo 3.
- [ ] A pessoa viu o antes e depois e deu o OK.
- [ ] `~/.config/squad-ht/perfil.md` com permissão 600 e YAML carregando; cópia anterior em `~/.config/squad-ht/historico/`.

## 5. Saída

Uma ou duas linhas: o que mudou e onde foi gravado.
