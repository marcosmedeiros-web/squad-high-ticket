# WhatsApp: o que a política exige e como o pacote cumpre

Resumo com palavras próprias da Política de Mensagens do WhatsApp Business. Leia o original antes de ligar.

| Exigência | No pacote |
|---|---|
| Permissão antes de escrever | o desenho declara `consentimento_base`; no formulário, só recebe quem marcou a caixa de aceite (valor inteiro: "não aceito" não passa) |
| Respeitar pedido de parar | antes de cada envio individual a conversa é lida; quem pediu para parar não recebe. Todo texto modelo diz como parar |
| Não surpreender, sem spam | uma mensagem por evento, no máximo uma por pessoa a cada 24 h somando todos os fluxos, teto diário (`AF_TETO_WHATSAPP_DIA`), janela de horário (`AF_JANELA_*`), só conversa individual ou grupo da lista do desenho |
| Caminho para um humano | o texto modelo convida a responder; a resposta cai na conversa do número do dono |

## Fica com o dono
- O gateway (OpenWA) usa o WhatsApp Web, não a API oficial. O número pode ser restringido pelo WhatsApp. Para volume
  alto, o caminho é a API oficial com modelos aprovados (fluxo sob medida).
- A base legal (consentimento ou legítimo interesse) é decisão dele.
- Grupo: só os ids que ele listou no desenho; o pacote confere que o grupo é da sessão antes de mandar.
