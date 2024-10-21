from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask app on port 5100!"

# Exemplo de um endpoint que faz requisição ao microserviço de validação de token
@app.route('/data', methods=['GET'])
def get_data():
    token = request.headers.get('Authorization')

    # Fazendo uma requisição ao microserviço de validação de tokens
    response = requests.get('http://token-validation:5001/validate', headers={'Authorization': token})

    if response.status_code == 200:
        return jsonify({"data": "Here is your secure data!"})
    else:
        return jsonify({"error": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
