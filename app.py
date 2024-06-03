from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Replace this with your Replit app URL
REPLIT_APP_URL = "https://flaskapp.ahmedshawky12.repl.co"

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Log the incoming request
        logging.info(f"Incoming request: {request.json}")
        
        # Forward the request to the Replit app
        response = requests.post(f"{REPLIT_APP_URL}/analyze", json=request.json)
        
        # Log the response from the Replit app
        logging.info(f"Response from Replit: {response.json()}")
        
        response.raise_for_status()  # Check if the request was successful
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"RequestException: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
