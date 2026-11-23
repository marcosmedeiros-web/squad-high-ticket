# Roteiro de montagem (configurações ditas nas aulas 3 a 6)

Quem monta: executor de automação, com o dono logado nas contas. Chaves digitadas pelo dono no gerenciador de credenciais do n8n;
nunca em chat, prompt ou print.

## A. Fireflies (aula 3)
1. Criar conta; liberar acesso à agenda; habilitar transcrições ilimitadas (plano gratuito).
2. Escolher "todas as reuniões" ou "only meetings that I own".
3. "Send a meeting recap to": only me.
4. Idioma: português. Usando Zoom: conectar a conta Zoom.
5. Formas de pôr o robô na reunião: automático pela agenda; convidar o e-mail do assistente do Fireflies; menu Capture (colar o link
   da reunião e aprovar a entrada); upload de áudio/vídeo.

## B. n8n: gatilho (aula 4)
1. Novo fluxo do zero, nome no padrão "[Expert] - Análise de reuniões ([tipo])".
2. Primeiro nó: **Webhook**. Method: POST. Aba URL: **Production URL**. Copiar.
3. Fireflies → Settings → Developer Settings → campo Webhook: colar a URL de produção e marcar **Transcription complete**. Salvar.
4. **Publish** no n8n (sem publicar, nada chega).
5. Reunião de teste ≥ 5 min; esperar 1-2 min após encerrar; Executions deve mostrar execução verde com `meetingId`.
6. Abrir a execução verde → **Copy to editor** (traz os dados reais para montar o resto).

## C. n8n: transcrição e limpeza
7. Nó **Fireflies → Get a transcript**. Credencial: API key do Fireflies (Developer Settings), cadastrada pelo dono no n8n. Transcription ID: arrastar
   `meetingId` do esquema do webhook (modo Expression). Execute step.
8. Nó **Code (JavaScript)**: juntar as falas em um texto com timestamps e trazer o título. O código da aula não está nos arquivos:
   gerar com uma IA a partir do JSON de saída do passo 7 (dica do professor: copiar o JSON e perguntar "o que faço agora?").

## D. IA 1
9. Nó **AI Agent**: Source for Prompt = **Define below**, com a transcrição do Code (mensagem do usuário). Options → **System
   Message** = prompt de avaliação (Markdown).
10. Plugar **Chat Model → OpenRouter**; credencial com a API key (cadastrada pelo dono no n8n); modelo escolhido (arquitetura-e-custos.md). Executar:
    resposta em JSON por etapa.
11. **Code 2**: quebrar o JSON em campos (status e observação por etapa).

## E. Planilha e IA 2 (aula 5)
12. **Google Sheets → Append Row in Sheet**; credencial OAuth2 da conta Google; documento e aba (a planilha tem de estar no Drive
    dessa conta). Mapear: nome (title), data (Code para formatar), duração (Code para formatar), participantes, link (transcript URL),
    status e observação de cada etapa; nota e resumo em branco.
13. Duplicar o AI Agent com OpenRouter; System Message = prompt de nota e resumo; mensagem do usuário = transcrição completa + JSON
    da IA 1.
14. **Code 3** simples; **Google Sheets → Append or Update Row**, coluna de casamento = nome da reunião; atualizar nota geral e resumo.
15. Publish de novo a cada mudança.

## F. Erros e alertas (aula 6), com envio DESLIGADO até o OK do estrategista
16. Novo fluxo: nó **Error Trigger** → nó de envio (HTTP Request para o canal escolhido). Mensagem: aviso de erro + mensagem do erro +
    nome do workflow (campos arrastados do Error Trigger).
17. No fluxo principal: Settings → **Error Workflow** = fluxo de erro. Salvar.
18. Depois do Sheets final: nó **If**, nota geral (Number) **less than 70** → nó de envio com: aviso de nota baixa, nota, reunião,
    link, participantes. Falso: fim.
19. Exemplo de aula para o envio por Z-API (só referência): HTTP Request POST na URL "enviar texto" da documentação com instância e
    token; header `client-token`; body com `phone` (55 + DDD + número) e `message` (Expression). Tokens cadastrados pelo dono no n8n.
20. Deixar os nós de envio **desativados** e anotar em `arquitetura.md` o que falta para ligar.

## G. Rotina
Conferir Executions (verdes e vermelhas) toda semana; revisar 1 reunião aleatória por mentor/closer por mês contra a nota da IA
(amostragem contínua, trilha 19).
