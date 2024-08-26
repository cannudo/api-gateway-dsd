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