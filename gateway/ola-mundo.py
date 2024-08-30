from flask import Flask, request, jsonify, Response
import requests

API_ETIQUETAS = "https://friendly-spoon-6v4vwrqwp5g27j6-8000.app.github.dev/"

app = Flask(__name__)

def api_online():
    try:
        response = requests.get(API_ETIQUETAS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return False
    return True

@app.route("/etiquetas/", methods = ["GET", "POST"])
def listar_tarefas():
    if not api_online():
        return Response("API offline", status=502)
    if request.method == "GET":
        resposta = requests.get(API_ETIQUETAS + "etiquetas/")
        return Response(resposta.text, status = 200, mimetype = "application/json")
    if request.method == "POST":
        titulo = request.json.get("titulo")
        descricao = request.json.get("descricao")
        if not titulo or not descricao:
            resposta = jsonify(
                {"error": "Dados insuficientes"},
                ), 400
            return resposta # objeto do tipo Response
        resposta = requests.post(
            API_ETIQUETAS + "etiquetas/",
            json={"titulo": titulo, "descricao": descricao}
        )
        return Response(resposta.text, status = 201)
    
@app.route("/etiquetas/<int:id_da_etiqueta>/", methods = ["GET", "PUT", "DELETE"])
def detalhar_etiqueta(id_da_etiqueta):
    if not api_online():
        return Response("API offline", status=502)
    if request.method == "GET":
        print(f"Detalhando etiqueta {id_da_etiqueta}")
        requisicao_para_api = requests.get(API_ETIQUETAS + f"etiquetas/{id_da_etiqueta}/")
        if requisicao_para_api.status_code != 200:
            return Response("Etiqueta não encontrada", status = 404)
    if request.method == "PUT":
        titulo = request.json.get("titulo")
        descricao = request.json.get("descricao")
        if not titulo or not descricao:
            resposta = jsonify(
                {"error": "Dados insuficientes"},
            ), 400
            return resposta
        requisicao_para_api = requests.put(
            API_ETIQUETAS + f"etiquetas/{id_da_etiqueta}/",
            json={"titulo": titulo, "descricao": descricao}
        )
        if requisicao_para_api.status_code not in [200, 201]:
            return Response(requisicao_para_api.text, status = 502)
        return Response(requisicao_para_api.text, status = 201, mimetype="application/json")
    if request.method == "DELETE":
        requisicao_para_api = requests.delete(API_ETIQUETAS + f"etiquetas/{id_da_etiqueta}/")
        return Response(requisicao_para_api.text, status = requisicao_para_api.status_code)