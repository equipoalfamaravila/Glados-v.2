from flask import Flask, request, jsonify, render_template
import requests

# Inicializa la aplicación Flask
app = Flask(__name__)

# URL de la API para realizar consultas
API_URL = "https://api.stack-ai.com/inference/v0/run/4e53f387-b479-4eb5-afb6-cec2fb93772a/666b66e83007b181c335ac9c"

# Encabezados para la solicitud HTTP, incluyendo la autorización
headers = {
    'Authorization': 'Bearer 117f8069-4144-4822-8f89-4f07f007d1a4',
    'Content-Type': 'application/json'
}

# Función para realizar consultas a la API
def query(payload):
    # Realiza una solicitud POST a la API con el payload y los encabezados
    response = requests.post(API_URL, headers=headers, json=payload)
    # Devuelve la respuesta en formato JSON
    return response.json()

# Ruta para la página principal
@app.route('/')
def index():
    # Renderiza la plantilla HTML llamada 'index.html'
    return render_template('index.html')

# Ruta para manejar las preguntas del usuario
@app.route('/ask', methods=['POST'])
def ask():
    # Obtiene la pregunta del usuario del cuerpo de la solicitud JSON
    question = request.json.get('question')
    # Crea el payload con la pregunta
    payload = {"in-0": question}
    # Realiza la consulta a la API
    output = query(payload)
    # Devuelve la respuesta en formato JSON
    return jsonify({"answer": output['outputs']['out-0']})

# Inicia la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)
