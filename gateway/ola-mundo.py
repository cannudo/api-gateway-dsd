from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    '''
    Isto é: execute a função ola_mundo() quando o Flask detectar uma requisição para a rota /
    '''
    return "<h1>Olá, mundo!</h1>"

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
        retorno = "Veio um post"
    else: # a requisição nunca chega nesse else, porque outros métodos retornam 405 automaticamente
        retorno = "Veio outro método"
    return retorno