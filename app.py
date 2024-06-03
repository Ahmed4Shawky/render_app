from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# URL of your Hugging Face model endpoint
HUGGING_FACE_URL = "https://huggingface.co/spaces/A7med4/flask_app2"

@app.route('/')
def home():
    return 'Welcome to the Flask App!'

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Log the incoming request data
        logging.info(f"Incoming request: {request.json}")
        
        # Extract text from the request JSON payload
        text = request.json.get('text')  # Using .get() to avoid KeyError
        
        if not text:
            raise ValueError("Text field is missing or empty")
        
        # Send the text to the Hugging Face model for analysis
        response = requests.post(f"{HUGGING_FACE_URL}/analyze", json={"text": text})
        
        # Log the response from the Hugging Face model
        logging.info(f"Response from Hugging Face: {response.text}")
        
        # Check if the request to Hugging Face was successful
        response.raise_for_status()
        
        # Parse the JSON response
        response_data = response.json()
        
        return jsonify(response_data), response.status_code
    except requests.exceptions.RequestException as e:
        # Log any request exceptions
        logging.error(f"RequestException: {e}")
        return jsonify({'error': 'Error making request to Hugging Face model'}), 500
    except (KeyError, ValueError) as e:
        # Log and handle KeyError or ValueError
        logging.error(f"Error processing response: {e}")
        return jsonify({'error': f"Error processing response: {e}"}), 400


@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
