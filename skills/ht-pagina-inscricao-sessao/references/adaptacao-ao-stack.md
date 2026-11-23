# Como a ferramenta de referência se traduz no stack do projeto

Referência da `ht-pagina-inscricao-sessao`. A referência demonstra em Hotmart Pages (páginas) e Hotmart Send (e-mail marketing), e
avisa que o fundamento é o mesmo em qualquer ferramenta. A escolha da ferramenta do projeto segue o padrão assumido (SKILL, seção 5).

| Peça do método | Na Hotmart | Em página estática própria | O que não muda |
|---|---|---|---|
| Domínio e SSL | Criador de páginas → Domínio → configurar com o provedor | Domínio do expert apontado para a hospedagem da página; publicação por `publicar-pagina-cloudflare` | Domínio próprio, https, antecedência |
| Página de inscrição | Página em branco + seções de modelo, botões com ação "ancorar seção" | Página estática feita pelo `ht-web-designer` (ex.: `frontend-design:frontend-design`, `pagina-design-premium`), âncora `#formulario` em todos os botões | Estrutura de seções, CTAs ancorados |
| Formulário | Formulário do Send importado na página | Formulário ligado ao e-mail marketing/CRM do projeto (ex.: Mautic via `email-marketing-mautic`) por formulário nativo ou código incorporado | E-mail + telefone, curto, sem dupla confirmação |
| Tag | Tag "solicitou diagnóstico" no Send | Tag/segmento equivalente no e-mail/CRM | Toda inscrição marcada |
| Obrigado | Modelo simples, escolhido como "página personalizada" no formulário | Página estática própria, definida como redirecionamento após envio | Sem CTA, URL específica |
| Lista de leads | Contatos → filtro "inscritos por formulário" → exportar | Segmento por tag no e-mail/CRM; exportação para a Central 1x1 | Lead identificado e exportável |
| Pixel e evento Lead | Ensinado no bootcamp de tráfego | Pixel no `<head>` das duas páginas; Lead só na obrigado; conferência com `meta-ads-cli` / `hotmart-meta-conversao` | Evento só na obrigado |
| Remetente de e-mail | Configuração de remetente com registros no domínio  | SPF/DKIM/DMARC pelo gestor de e-mail do projeto | Só se houver e-mail automático, com OK do estrategista |

Regras para qualquer ferramenta:
- O squad não cria conta em nome do expert nem digita senha; acesso concedido pelo expert/estrategista.
- Página publicada só depois do teste de fluxo com prova e do OK do estrategista.
- Mensagem automática ao lead (e-mail ou WhatsApp de confirmação) é automação de envio: só liga com OK do estrategista.
- Hotmart Pages: plano gratuito pode não permitir remover o selo; limites de páginas e domínios por plano mudam com o tempo
  (conferir com o suporte da Hotmart antes de contratar).
