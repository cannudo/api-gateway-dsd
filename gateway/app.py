from flask import Flask, request, jsonify, Response
import requests

API_ETIQUETAS = "http://localhost:8000/"
API_TAREFAS = "http://localhost:8085/"

app = Flask(__name__)

def api_online(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return False
    return True

@app.get("/")
def root():
    return jsonify({
        "_links": {
            "self": {"href": "http://localhost:5000/"},
            "etiquetas": {"href": "http://localhost:5000/etiquetas/"},
            "tarefas": {"href": "http://localhost:5000/tarefas/"}
        }
    }), 200

@app.route("/etiquetas/", methods = ["GET", "POST"])
def listar_etiquetas():
    if not api_online(API_ETIQUETAS):
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
    print(f"Detalhando etiqueta {id_da_etiqueta}")
    if not api_online(API_ETIQUETAS):
        return Response("API offline", status=502)
    
    if request.method == "GET":
        requisicao_para_api = requests.get(API_ETIQUETAS + f"etiquetas/{id_da_etiqueta}/")
        if requisicao_para_api.status_code != 200:
            return Response("Etiqueta não encontrada", status = 404)
        return Response(requisicao_para_api.text, status = 200, mimetype = "application/json")
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
    

@app.route("/tarefas/", methods = ["GET", "POST"])
def listar_tarefas():
    if not api_online(API_TAREFAS):
        return Response("API offline", status=502)
    if request.method == "GET":
        resposta = requests.get(API_TAREFAS + "tarefas/")
        return Response(resposta.text, status = 200, mimetype = "application/json")
    if request.method == "POST":
        nome = request.json.get("nome")
        descricao = request.json.get("descricao")
        etiqueta_id = request.json.get("etiqueta_id")
        if not nome or not descricao:
            resposta = jsonify(
                {"error": "Dados insuficientes"},
                ), 400
            return resposta
        resposta = requests.post(
            API_TAREFAS + "tarefas/",
            json={"nome": nome, "descricao": descricao, "etiqueta_id": etiqueta_id}
        )
        if resposta.status_code == 400:
            return Response("Tarefa não encontrada", status = 404)
        return Response(resposta.text, status = 201)
    
@app.route("/tarefas/<int:id_da_tarefa>/", methods = ["GET", "PUT", "DELETE"])
def detalhar_tarefa(id_da_tarefa):
    if not api_online(API_TAREFAS):
        return Response("API offline", status=502)
    if request.method == "GET":
        print(f"Detalhando tarefa {id_da_tarefa}")
        requisicao_para_api = requests.get(API_TAREFAS + f"tarefas/{id_da_tarefa}/")
        if requisicao_para_api.status_code != 200:
            return Response("Tarefa não encontrada", status = 404)
        return Response(requisicao_para_api.text, status = 200, mimetype = "application/json")
    if request.method == "PUT":
        nome = request.json.get("nome")
        descricao = request.json.get("descricao")
        etiqueta_id = request.json.get("etiqueta_id")
        if not nome or not descricao:
            resposta = jsonify(
                {"error": "Dados insuficientes"},
            ), 400
            return resposta
        requisicao_para_api = requests.put(
            API_TAREFAS + f"tarefas/{id_da_tarefa}/",
            json={"nome": nome, "descricao": descricao, "etiqueta_id": etiqueta_id}
        )
        if requisicao_para_api.status_code not in [200, 201]:
            return Response(requisicao_para_api.text, status = 502)
        return Response(requisicao_para_api.text, status = 201, mimetype="application/json")
    if request.method == "DELETE":
        requisicao_para_api = requests.delete(API_TAREFAS + f"tarefas/{id_da_tarefa}/")
        return Response(requisicao_para_api.text, status = requisicao_para_api.status_code)