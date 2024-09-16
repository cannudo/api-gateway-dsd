### Rodar o servidor WS do jogo connectfour

> caminho: ./connectfourgame

python3 app.py

### Rodar o servidor HTTP do jogo connectfour

> caminho: ./connectfourgame

python3 -m http.server

#### Testar conexão com o servidor WS

> O servidor WS não pode ser testado com um navegador web. Mas há um cliente Websocket interativo em Python:

python3 -m websockets ws://localhost:8001/

### Abrir conexão com WS a partir do JavaScript

const websocket = new WebSocket("ws://localhost:8001/");

## 💡 Formato das mensagens

Antes de transmitir mensagens de um cliente para o servidor, precisamos definir um formato para a transmissão. Não há um padrão específico, então são os desenvolvedores que convencionam.

Para fins de exemplo, usaremos um JSON com uma chave `type` identificando o tipo do evento. As demais chaves conterão as propriedades do evento.

#### Exemplo

const event = {type: "play", column: 3};

### Serializar evento e enviá-lo ao servidor usando JavaScript

websocket.send(JSON.stringify(event));

### Deserializar mensagem do servidor para JSON

websocket.addEventListener("message", ({ data }) => {
  const event = JSON.parse(data);
  // do something with event
});

