# Domínio, itens técnicos e teste de fluxo

Referência da `ht-pagina-inscricao-sessao`.

## 1. Domínio e itens técnicos

- **Domínio próprio:** profissionalismo (endereço estranho parece golpe) e exigência do tráfego (configuração de anúncio e
  verificação no BM pedem domínio). Pode ser o nome do expert ou do produto. Subdomínio vale (ex.: `sessao.dominiodoexpert.com.br`).
  Subdomínio gratuito da ferramenta é pouco profissional.
- **Compra:** registro em provedor de domínio; compra e acesso são do expert (gasto: com OK do expert). O squad
  nunca cria conta nem digita senha do expert.
- **Propagação:** até 24 h (algumas ferramentas avisam até 72 h). Configurar com antecedência, nunca no dia de ligar o tráfego.
- **SSL (https):** obrigatório; conferir o cadeado. Se não emitir em 72 h, suporte da ferramenta.
- **Verificação do domínio no Business Manager** e pixel ("conjunto de dados") instalado: sem isso não há público de visitantes
  nem otimização por Lead (responsabilidade do `ht-gestor-trafego`; o bootcamp não tem aula própria disso).
- **URLs:** com hífen, nunca underline (algumas ferramentas removem o underline). Padrão sugerido: `/sessao-[nome]` e
  `/obrigado-sessao-[nome]`.
- **Título da aba e favicon** (32 x 32 px, quadrado, simples).
- **Selo da ferramenta:** remover quando o plano permitir.
- **Organização:** um documento do projeto com URLs, tag, nome do formulário, cores (hex) e acessos (sem senha).
- **Editor:** uma aba por página; salvar e publicar a cada alteração (alterou e não mudou = não publicou).

## 2. Teste de fluxo ponta a ponta (antes de qualquer tráfego)

Regra do protocolo: verificar é observar o resultado de fora; editar ou ler a configuração não é verificar.

**Checklist de 8 itens (reconstrução do squad a partir dos passos demonstrados; o material não traz
uma lista numerada), com a prova exigida no squad:**

| # | Item | Prova a registrar |
|---|---|---|
| 1 | Domínio apontado e com SSL ativo (https) | Print da página com o cadeado / saída de verificação |
| 2 | Tag criada | Print da tag na ferramenta |
| 3 | Formulário com e-mail e telefone, ligado à tag e ao obrigado | Print da configuração |
| 4 | Página de inscrição com todos os CTAs ancorados no formulário, URL no domínio, título e favicon | Teste de clique em cada botão |
| 5 | Selo da ferramenta removido (se o plano permite) | Print do rodapé |
| 6 | Obrigado publicado e escolhido no formulário | Print do destino no formulário |
| 7 | Inscrição de teste cai no obrigado e aparece nos contatos com a tag e o telefone | Print do contato |
| 8 | Tudo salvo E publicado | Abrir a URL em aba anônima |

**Testes adicionais do squad:**
- No celular (navegador do Instagram, que é onde o lead abre): página carrega, formulário funciona, botão visível.
- Com pixel: abrir a obrigado com o teste de eventos do gerenciador e ver o Lead disparar uma vez; conferir que não há dois
  pixels na mesma página/conta; Pixel Helper no Chrome (no Safari não aparece).
- Segmentação: um teste para cada faixa da pergunta de corte; cada um no destino e com a tag certos.
- Aviso interno: a pessoa que agenda recebeu o alerta da inscrição de teste.
- Depois do teste: marcar ou remover o contato de teste para não sujar a lista e os números.

**Relatório:** arquivo `11-automacoes/pagina-sessao/AAAA-MM-DD-teste-de-fluxo.md` com data, quem testou, cada item com
aprovado/reprovado e a prova, o que foi corrigido e o nível de evidência (verificado / feito sem teste / inferido). Reprovou um
item: o tráfego não liga.

## 3. Problemas comuns e causa

| Sintoma | Causa provável |
|---|---|
| Inscrição cai na página padrão da ferramenta | Confirmação do formulário não foi trocada pelo obrigado |
| Formulário sumiu da página | Duas abas do editor abertas na mesma página |
| Alteração não aparece | Salvou e não publicou |
| URL diferente da combinada | Underline removido pela ferramenta |
| Aviso "sem atividade de conversão" no gerenciador | Evento Lead não configurado ou não disparando na obrigado |
| Público de obrigado com gente de outra página | Padrão de URL genérico ("obrigado") |
| Página sem https | Propagação incompleta ou SSL pendente |
