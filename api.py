from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_url')
def get_url():
    # URL del archivo raw en GitHub
    github_url_file = "https://raw.githubusercontent.com/palmace/github.io/main/url.txt"
    
    try:
        # Realiza la petición GET para obtener el contenido del archivo
        response = requests.get(github_url_file)
        
        # Verifica que la petición fue exitosa
        if response.status_code == 200:
            # Obtiene el contenido del archivo y lo limpia de espacios en blanco
            url_content = response.text.strip()
            
            # Devuelve la URL como una respuesta JSON
            return jsonify({"url": url_content})
        else:
            return jsonify({"error": "No se pudo acceder al archivo."}, 404)
            
    except requests.exceptions.RequestException as e:
        # Manejo de errores de conexión
        return jsonify({"error": str(e)}, 500)

if __name__ == '__main__':
    # Ejecuta el servidor de la API
    app.run(debug=True)
