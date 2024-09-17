# api-gateway-dsd

Projeto de arquitetura de microsserviços utilizando gateway para interligar API e cliente, com implementação adicional de websockets.

Abaixo, você encontra instruções de como rodar o projeto localmente.

### Contribuidores

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/cannudo>
            <img src=https://avatars.githubusercontent.com/u/24627793?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Luan da Costa Redmann/>
            <br />
            <sub style="font-size:14px"><b>Luan da Costa Redmann</b></sub>
        </a>
    </td>
        <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/leomttx>
            <img src=https://avatars.githubusercontent.com/u/115085347?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Leonardo/>
            <br />
            <sub style="font-size:14px"><b>Leonardo</b></sub>
        </a>
    </td>
</tr>
</table>

## Ambiente de testes

As instruções a seguir foram implementadas usando um ambiente Debian GNU/Linux, que usa o shell `bash` como terminal.

Sinta-se livre para propor mudanças neste documento e adicionar instruções específicas ao seu sistema operacional.

### Criar ambiente virtual

Para rodar o projeto, há a necessidade de fazer o download de vários pacotes adicionais para o Python usando o gerenciador de pacotes `pip`. Para que seu sistema operacional permaneça sem conflitos, é recomendável criar um ambiente virtual.

Dessa forma, obtém-se uma instalação limpa do Python e os downloads serão feitos exclusivamente para ela.

```bash
python3 -m venv venv
```

### Ativar ambiente virtual

Após criar o ambiente virtual, é preciso ativá-lo. Após o comando a seguir, o caminho dos downloads feitos usando o gerenciador de pacotes `pip` deverá mudar e você já será capaz de utilizar a inbstalação limpa do Python.

```bash
source venv/bin/activate
```

### Instalar dependências

Dentre as principais dependências do projeto, algumas se destacam:

- Django: usado para a construção das APIs de `tarefas` e `etiquetas`;
- Flask: usado para a construção do gateway;
- Websockets: usado para a construção do websocket.

```bash
pip install -r requirements.txt
```

💡 **Aviso:** as instruções que seguem devem ser executadas em instâncias próprias dos terminais, pois serão cinco processos diferentes:

1. API de etiquetas;
1. API de tarefas;
1. Gateway;
1. Websocket;
1. Frontend.

Para cada instrução que segue (isto é, para cada processo que será aberto daqui em diante), considera-se que você ativou o ambiente virtual.

### Rodar API de etiquetas


```bash
# com o ambiente virtual ativado
cd microsservicos/etiquetas/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 8000
```

💡 *O processo deverá rodar em http://localhost:8000/*

### Rodar API de tarefas


```bash
# com o ambiente virtual ativado
cd microsservicos/tarefas/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 8085
```

💡 *O processo deverá rodar em http://localhost:8085/*

### Rodar gateway


```bash
# com o ambiente virtual ativado
cd gateway/
flask run
```

💡 *O processo deverá rodar em http://localhost:5000/*


### Rodar websocket


```bash
# com o ambiente virtual ativado
cd websocket/
python3 ws-server.py
```

💡 *O processo deverá rodar em [wss://localhost:8765/](wss://localhost:8765/), **porém** não é acessível com navegador.* 
**Opcionalmente**, apenas a título de testes, você pode abrir mais uma instância do terminal, ativar o ambiente virtual, se conectar ao websocket através de um cliente Python e mandar uma mensagem de testes:

```bash
# com o ambiente virtual ativado
python3 -m websockets ws://localhost:8765/
> Olá, mundo!
< Nova notificação recebida!
```

### Para o frontend

Há um projeto que usa esta arquitetura.

Faça o clone dxo repositório localizado em [@leomttx/Cursos-react/](https://github.com/leomttx/Cursos-react) e rode o seguinte comando para dar início ao último processo:

```bash
cd Lista-de-tarefas/lista-de-tarefas/
npm i
npm run dev
```

### Desenho arquitetural

<!-- imagem -->