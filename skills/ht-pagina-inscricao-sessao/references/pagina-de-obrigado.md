# Página de obrigado da sessão 1a1

Referência da `ht-pagina-inscricao-sessao`. Aula 06 da trilha 12 e RESUMO-trafego da trilha 13.

## 1. Para que serve

1. Marcar a conversão do tráfego: o pixel registra como inscrito quem chega nesta página (evento Lead), e ela vira público
   personalizado por URL.
2. Avisar o lead de que a equipe vai entrar em contato. O lead não precisa fazer mais nada.

## 2. Conteúdo

Modelo da aula (texto curto, sem botão e sem cronômetro):
```
Pronto!
Em breve nossa equipe vai entrar em contato com você para [agendar seu nome da sessão].
```
Acréscimo opcional do squad (não está na aula; usar só se for verdade e com OK do estrategista): uma linha sobre **como** o contato
vem, para o lead reconhecer a mensagem, por exemplo "Vamos te chamar pelo WhatsApp [no número informado / pelo número com a
foto de (nome)]". Motivo: notificação de número desconhecido e sem foto reduz resposta (lição citada em live sobre funil
comercial).

Manter: logo, rodapé com CNPJ. Retirar: botão, cronômetro, oferta, novos passos para o lead.

## 3. Técnica

- URL própria e específica: `/obrigado-sessao-1a1` ou `/obrigado-[nome-da-sessao]`. Nunca só `/obrigado` se o domínio tiver
  outras páginas de obrigado (aula ao vivo, evento): o público por URL e a conversão se misturam.
- Título da aba ("Obrigado"), favicon, selo da ferramenta removido quando o plano permitir.
- O formulário aponta para esta página como confirmação (trocar a confirmação padrão da ferramenta depois que esta existir).
- Pixel instalado na página e **evento Lead disparando só aqui**.
- Público para o tráfego: visitantes desta URL, 180 dias (nome sugerido em aula: "Leads | Sessão 1a1 | Conversão | Página de
  obrigado | 180 dias"); usado como exclusão nas campanhas de captação de sessão (padrão do squad: exclusões em cascata; o
  bootcamp criou o público mas não mostrou a exclusão, ponto de atenção registrado na fonte).
