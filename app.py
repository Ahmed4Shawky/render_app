from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your Replit app URL (without /analyze at the end)
REPLIT_APP_URL = "https://flaskapp.ahmedshawky12.repl.co"

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Forward the request to the Replit app
        response = requests.post(f"{REPLIT_APP_URL}/analyze", json=request.json)
        response.raise_for_status()  # Check if the request was successful
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
