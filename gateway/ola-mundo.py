from flask import Flask

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

