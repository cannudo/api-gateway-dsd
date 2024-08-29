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
        return Response(resposta.json(), status = 200)
    if request.method == "POST":
        titulo = request.json.get("titulo")
        descricao = request.json.get("descricao")
        if not titulo or not descricao: # TESTAR PQ QUE DÁ 400 E N RETORNA ESSE JSONIFY
            resposta = jsonify(
                {"error": "Dados insuficientes"}
            )
            return Response(resposta, status = 400)
        resposta = requests.post(
            API_ETIQUETAS + "etiquetas/",
            json={"titulo": titulo, "descricao": descricao}
        )
        return Response(resposta.text, status = 201)
