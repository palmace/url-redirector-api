from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Headers anti-cache GLOBALES
@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['X-Accel-Expires'] = '0'
    return response

# ✅ CAMBIO IMPORTANTE: Nueva ruta /get_url_v2
@app.route('/get_url_v2')
def get_url():
    github_url_file = "https://raw.githubusercontent.com/palmace/palmace.github.io/main/url.txt"
    
    try:
        # Headers anti-cache para la petición a GitHub también
        headers = {
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache'
        }
        
        response = requests.get(github_url_file, headers=headers)
        
        if response.status_code == 200:
            url_content = response.text.strip()
            return jsonify({"url": url_content})
        else:
            return jsonify({"error": "No se pudo acceder al archivo en GitHub"}), 404
            
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
