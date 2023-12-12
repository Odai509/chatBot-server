from flask import Flask, Blueprint, request, jsonify
from gradio_client import Client
from parse_url import get_api_url

app = Flask(__name__)

# URL of the page to scrape
url = "https://deepseek-ai-deepseek-coder-7b-instruct.hf.space/?view=api"

@app.route('/')
def index():
    return 'Hello Odai, here you will be able to communicate with the API and the Flutter app'

@app.route('/code_gen', methods=['POST'])
def process_text():
    try:
        # Check if the request has JSON data
        if request.json:
            input_text = request.json.get('text')
            system_prompt = request.json.get('system')
        else:
            # Fallback to form data if no JSON data is found
            input_text = request.form.get('text')
            system_prompt = request.form.get('system')

        # Make the API request to the new API using gradio_client
        api = get_api_url(url)
        client = Client(api)
        result = client.predict(
            input_text,     # str in 'Message' Textbox component
            system_prompt,     # str in 'System prompt' Textbox component
            300,              # int | float in 'Max new tokens' Slider component
            0.9,           # int | float in 'Top-p (nucleus sampling)' Slider component
            50,              # int | float in 'Top-k' Slider component
            1,              # int | float in 'Repetition penalty' Slider component
            api_name="/chat"
        )

        # Assuming the result is a string response
        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
