from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulação de um "banco de dados" em memória (para testes)
sensor_data = []

# Endpoint para receber dados dos sensores
@app.route('/sensor-data', methods=['POST'])
def post_sensor_data():
    data = request.get_json()

    # Validação básica
    if not data or 'temperatura' not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    # Adiciona timestamp e salva
    data_with_timestamp = {
        **data,
        "timestamp": datetime.now().isoformat()
    }
    sensor_data.append(data_with_timestamp)

    return jsonify({"status": "Dados recebidos!"}), 201

# Endpoint para recuperar dados históricos
@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)