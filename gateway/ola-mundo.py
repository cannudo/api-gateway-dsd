from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    '''
    Isto é: execute a função ola_mundo() quando o Flask detectar uma requisição para a rota /
    '''
    #return "<h1>Olá, mundo!</h1>"
    return {"etiquetas": "http://localhost:5000/etiquetas/"} # Python converte isso para um JSON

@app.route("/etiquetas/")
def listar_etiquetas():
    return "OK"

@app.route("/etiquetas/<int:id_da_etiqueta>/")
def detalhar_etiqueta(id_da_etiqueta):
    return f"Etiqueta #{id_da_etiqueta}"

@app.route("/metodo/", methods = ["GET", "POST"])
def testar_metodo():
    if request.method == "GET":
        retorno = "Veio um GET"
    elif request.method == "POST":
        try:
            teste = request.form['atributo_da_requisicao'] # só vai ter alguma coisa se for passado como form-data (só consegui com postman)
        except KeyError:
            teste = None
        retorno = f"Veio um post ({teste})"
    else: # a requisição nunca chega nesse else, porque outros métodos retornam 405 automaticamente
        retorno = "Veio outro método"
    return retorno

@app.put("/metodos/")
def testar_put():
    retorno = "PUT funcionou"
    if request.method != "PUT":
        retorno = "Será que um GET cai aqui?" # Não. Retorna 405 automaticamente
    return retorno