# https://kinsta.com/blog/python-microservices/

import requests
import os
from flask import Flask, jsonify
app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

@app.route("/")
def home():
    return "Olá, mundo!"

BASE_URL = "https://dummyjson.com"
@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code != 200:
        return jsonify({'error': response.json()['message']}), response.status_code
    products = []
    for product in response.json()['products']:
        product_data = {
            'id': product['id'],
            'title': product['title'],
            #'brand': product['brand'],
            'price': product['price'],
            'description': product['description']
        }
        products.append(product_data)
    return jsonify({'data': products}), 200 if products else 204

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)