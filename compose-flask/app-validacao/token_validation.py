from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemplo simples de validação de token
@app.route('/validate', methods=['GET'])
def validate_token():
    token = request.headers.get('Authorization')

    # Exemplo básico de validação de token
    if token == "valid-token":
        return jsonify({"message": "Token is valid"}), 200
    else:
        return jsonify({"message": "Token is invalid"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
