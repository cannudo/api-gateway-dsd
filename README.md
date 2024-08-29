# api-gateway-dsd

### Criar ambiente virtual

python3 -m venv venv

### Ativar ambiente virtual

source venv/bin/activate

### Instalar dependências

pip install -r requirements.txt

### Rodar o exemplo do Kinsta

cd gateway/

flask --app produtos-exemplo run

### Testando serializers

> Caminho: /microsservicos/etiquetas

python manage.py shell

from etiqueta.models import Etiqueta

from etiqueta.serializers import EtiquetaSerializer

from etiqueta.serializers import EtiquetaSerializer

titulo = "Teste do serializer"

descricao = "Testando se o serializer vai funcionar"

instancia = Etiqueta(titulo = titulo, descricao = descricao)

instancia.save()

serializado = EtiquetaSerializer(instancia)

serializado.data

> {'id': 1, 'titulo': 'Teste do serializer', 'descricao': 'Testando se o serializer vai funcionar'}

### Requisição para etiquetas (logado)

python3

import requests

url = 'https://fantastic-yodel-4qwq6g56p9p3q567-8000.app.github.dev/'

resposta = requests.get(url + '/etiquetas/?format=json')

resposta.text

> '{"count":2,"next":null,"previous":null,"results":[{"id":1,"titulo":"Teste do serializer","descricao":"Testando se o serializer vai funcionar"},{"id":2,"titulo":"Teste do serializer","descricao":"Testando se o serializer vai funcionar"}]}'

### Rodar API de etiquetas

> Caminho: /microsservicos/etiquetas/

python3 manage.py migrate

python3 manage.py runserver 8000

### Rodar API de tarefas

> Caminho: /microsservicos/tarefas/

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver 8085