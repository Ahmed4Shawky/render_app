from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# URL of your Hugging Face space
HUGGING_FACE_URL = "https://huggingface.co/spaces/A7med4/flask_app2"

@app.route('/')
def home():
    return 'Welcome to the Flask App!'

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Log the incoming request
        logging.info(f"Incoming request: {request.json}")
        
        # Extract text from the request
        text = request.json['text']
        
        # Send the text to the Hugging Face model for analysis
        response = requests.post(f"{HUGGING_FACE_URL}/analyze", json={"text": text})
        
        # Log the response from the Hugging Face model
        logging.info(f"Response from Hugging Face: {response.text}")
        
        response.raise_for_status()  # Check if the request was successful
        
        # Check if the response content is empty
        if not response.text:
            raise ValueError("Empty response from Hugging Face model")
        
        # Parse the JSON response
        response_data = response.json()
        
        return jsonify(response_data), response.status_code
    except requests.exceptions.RequestException as e:
        # Log any request exceptions
        logging.error(f"RequestException: {e}")
        return jsonify({'error': str(e)}), 500
    except (KeyError, ValueError) as e:
        # Handle KeyError or ValueError
        logging.error(f"Error processing response: {e}")
        return jsonify({'error': f"Error processing response: {e}"}), 500


@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
