# Setup de ativos Meta, pixel, evento Lead e públicos



Se o expert já tem BM e conta, conferir primeiro o acesso pela ferramenta de tráfego do perfil (token, escopos, conta, IG; ver `execucao-ferramenta-trafego.md`). O checklist abaixo é para expert novo
ou para auditar o que existe. Login, senha, 2FA, cartão e aceite de termos são **sempre do expert ou do estrategista**, nunca do agente.

## 1. Ativos (ordem)

1. Perfil pessoal no Facebook (obrigatório; conta nova tem carência e pede verificação, planejar com antecedência).
2. Página pública do Facebook (perfil pessoal não serve como página de anúncio).
3. Instagram profissional (criador de conteúdo), vinculado à Página em Contas vinculadas.
4. Gerenciador de Negócios (BM) do expert. Usar o que já existe; **nunca BM de terceiro**. Ter BM de backup.
5. Conta de anúncios: **moeda BRL e fuso São Paulo não mudam depois** (errou, cria outra conta).
6. Pagamento: cartão de crédito recomendado. Uma orientação diz que, cadastrado Pix ou boleto, a conta fica presa a esse meio, e
   com cartão dá para trocar depois; outra diz que boleto e cartão podem ser trocados. **Conferir na conta** antes de
   escolher. Dados fiscais: CNPJ ou CPF (a Meta emite nota mensal).
7. Conferir no BM: Página, Instagram e conta atribuídos; pessoas com acesso. Dar **acesso total** a quem vai resolver bloqueio
   e pagamento (só quem tem acesso total fala com o suporte e recebe aviso de problema). Convidado no BM também precisa ser
   incluído na conta de anúncios.
8. 2FA por aplicativo autenticador, **não por WhatsApp** (casos de clonagem de número), e guardar os códigos de reserva.
9. Trabalhar no Chrome (Safari falhou em vários passos e o Pixel Helper não roda nele).
10. Conta nova libera gasto devagar (sequência citada ~R$ 30/40/60/90 por dia; ~R$ 50/dia nos primeiros dias). Aviso de
    "atualização recomendada" é normal.

## 2. Pixel (conjunto de dados)

- Um pixel por negócio/avatar. Projetos diferentes do mesmo expert com públicos diferentes: pixels separados.
- Conectar o pixel à conta de anúncios (Ativos conectados).
- Instalar em **todas** as páginas do funil (captura, obrigado, grupo, vendas). Hotmart Pages: ID do pixel + token da API de
  conversões (Gerenciador de Eventos > Conjunto de dados > Configurações > Gerar token) em Integração Facebook, com o
  nome de evento PageView em todas as páginas; o Lead sai de uma conversão personalizada por URL do obrigado.
  O mesmo ID e token valem para todas as páginas do mesmo pixel. WordPress: script no head. Green: duplicar a linha de PageView para Lead (L maiúsculo) no
  JavaScript customizado, sem tags script.
- Verificar o domínio no BM.
- Testar com **Testar eventos** (Gerenciador de Eventos) e com a extensão **Meta Pixel Helper** no Chrome (verde = ok,
  amarelo/vermelho = erro de instalação).
- Atenção a **dois pixels** na mesma conta ou página: o evento pode estar caindo no outro.

## 3. Evento Lead (o ponto que mais quebra)

- Disparar Lead **só com cadastro real**: na página de obrigado, ou numa página de redirecionamento de ~5 s antes do grupo.
- Evento no clique do botão conta lead falso. Caso de referência: 38 leads no gerenciador para 8 na base.
- Sem página de obrigado: evento personalizado no gerenciador de eventos (não é retroativo) ou conversão personalizada pela
  URL (slug) do obrigado.
- Aviso "não recebemos nenhuma atividade de conversão" = evento não configurado ou não disparando.
- Funil com redirecionamento direto ao formulário de confirmação: pedir o e-mail de novo no fim ou usar campos ocultos/UTM.
- Minicurso e ingresso: Purchase do checkout (Hotmart) via integração; ver skill `hotmart-meta-conversao`.

## 4. Públicos (criar antes da campanha)

Todos atualizam sozinhos; público pequeno vale criar já.

| Público | Fonte e janela | Uso |
|---|---|---|
| Visitantes do site | pixel, todos os visitantes; criar várias janelas (7, 14, 21, 30, 60, 90 e 180 dias; 180 é o máximo para site) | 00 (180d) e remarketing curto (7 a 30d) |
| Visitantes da inscrição | URL contém `<slug-da-inscricao>`, 180 dias | 00 ou remarketing |
| Leads (obrigado) | URL contém `obrigado-<canal>` (padrão **específico**, senão mistura páginas), 180 dias | exclusão e remarketing |
| Engajamento Instagram | 365 dias (também 180, 90, 30) | conjunto 01 |
| Seguidores / envolvimento | perfil e página | internos |
| Vídeo 75% | Públicos > personalizado > vídeo > 75% > vídeos escolhidos | internos e semelhante |
| Lista de clientes/leads | upload (Meta aceita de 100; entrega melhor acima de ~1.000) | internos, semelhante, exclusão de alunos |
| Semelhante | 1% Brasil a partir de qualquer interno; criar faixas 1 a 10% para testar (já houve 4% melhor que 1%) | conjunto 02 |
| Interesses | 3 a 5 do nicho juntos; depois isolados | conjunto 02 |

Regras de público:
- Nome do público = fonte + recorte + janela: `Site geral 30d`, `Seguidores - @perfil`, `Envolvimento IG - 365d`,
  `Envolvimento FB - 365d`. Com mais de um perfil conectado, o `@` evita usar o público da conta errada.
- Público de envolvimento do Facebook aceita até 730 dias; janela maior contém a menor, então não somar as duas no mesmo
  conjunto.
- Semelhante pede base de ~1.000 (seguidores, leads ou visitas).
- Frequência ~3,5 no quente = público esgotado: abrir para frio.
- Público pequeno encarece o CPM; seguidores de perfil recém-profissionalizado (ex.: ~1.900) não sustentam campanha.
- Não usar pixel ou público de concorrente; salvar público novo em vez de editar um compartilhado.
- Público PJ: evitar interesse que atrai curioso (ex.: interesse em marca cara); falar com o público no criativo e na página.

## 5. Teste do fluxo (prova antes de subir)

Checklist de 8 itens: domínio com SSL · tag · formulário ·
página publicada · etiqueta · obrigado · teste feito · publicado. Preencher como lead, cair no obrigado, ver o Lead no Testar
eventos e o contato com a tag na ferramenta. Nunca editar a página em duas abas ao mesmo tempo. Registrar data e resultado.
