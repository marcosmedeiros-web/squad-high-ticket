# Erros comuns de campanha (sintoma → causa provável → conserto)

Fontes: laboratórios e plantões de tráfego das turmas (FEV26 §8, §9.1, §9.3, §9.4; OUT25 aulas 8, 9, 12, 15 e 20, via
`parte-G` `resolvedor-erros-campanha-meta-aluno`); trilha 13 `RESUMO-trafego.md` §8 e §10; trilha 14 `RESUMO-funil-de-reels-parte2.md` §8;
FEV26 aula 33 (transcrição nova).

| Sintoma | Causa provável | Conserto |
|---|---|---|
| Campanha não gasta | ficou em rascunho (barra verde), um nível desativado, pagamento pendente, conta nova com limite, público pequeno demais | publicar; ativar os 3 níveis; Cobrança > pagar agora e reativar os anúncios com erro em massa; aceitar o limite inicial; ampliar o público |
| Muitos cliques, zero cadastro (ex.: centenas de cliques) | objetivo errado (Tráfego/Engajamento), destino errado, página quebrada | objetivo não muda depois: duplicar e recriar em Leads/Site; conferir URL e testar o fluxo |
| Gerenciador conta mais lead que a base | evento Lead no clique do botão | mover o Lead para obrigado/redirecionamento; testar de novo |
| Aviso "nenhuma atividade de conversão" | evento não instalado ou não dispara; pixel diferente do conjunto | Testar eventos + Pixel Helper; conferir o ID do pixel no conjunto e na página |
| Evento caindo em outro pixel | dois pixels na mesma conta ou página | deixar um ID único; reconectar ativos |
| Página/IG não aparecem para criar o anúncio | ativos não atribuídos no BM, ou BM errado | refazer a atribuição no BM; conferir se a conta e o pixel são do mesmo BM |
| Campanha sumiu na gravação/subida | "Descartar rascunho" antes de confirmar a publicação | nunca descartar sem confirmar; a Meta não tem desfazer |
| Erro ao publicar | instabilidade | atualizar e publicar de novo |
| Anúncio reprovado ou vídeo bloqueado | vídeo regravado/baixado do Instagram com baixa qualidade; música com direito autoral; telefone no anúncio; promessa fora de política | subir o arquivo original; trocar o áudio por livre de direitos; tirar telefone; revisar o texto com o revisor (compliance Meta) |
| Botão Turbinar não aparece | Reels > 90 s, filtro do Instagram, música em alta com direito autoral, qualidade baixa | acelerar/cortar/regravar; subir sem filtro; música livre ou nenhuma |
| CPL subiu de repente | escala acima de 30%, público esgotado (frequência ~3,5), criativo fadigado (~45 dias), página ficou lenta | voltar a verba ou duplicar; abrir frio; criativo novo; medir a taxa de carregamento |
| CTR bom, CPL ruim | página converte pouco ou carrega mal | mexer na página antes do criativo (teste A/B de página) |
| CPL bom, ninguém agenda | criativo atrai quem não serve; formulário sem filtro | segmentar no criativo; pergunta de corte no formulário; olhar o perfil de quem chega |
| Público fechado alcança muito mais que o tamanho dele | expansão de público personalizado ligada | `targeting_relaxation_types` com `custom_audience: 0`; reler o alcance |
| Conta não aceita mudar moeda/fuso | criados errados | abrir nova conta de anúncios |
| Não consegue criar empresa/página | perfil novo em carência; muitas tentativas seguidas | esperar; outro e-mail ou navegador; verificação por código ou selfie é do expert |
| Hotmart e gerenciador não batem | delay, iOS, atribuição | usar a base/Hotmart como verdade para venda; gerenciador para tendência |
| Campanha parou "sem motivo" | instabilidade da Meta | duplicar e republicar (não apagar a original antes) |

Regras que evitam a maioria: trabalhar no Chrome; 2FA por aplicativo; BM próprio; duplicar antes de apagar; quando o CPL está
bom, não mexer.
