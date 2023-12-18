from flask import Flask, Blueprint, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# URL of the page
url = "https://odai-509-devbot.hf.space/--replicas/3xiwz/"

@app.route('/')
def index():
    return 'Hello Odai, here you will be able to communicate with the API and the Flutter app'

@app.route('/code_gen', methods=['POST'])
def process_text():
    try:
        # Check if the request has JSON data
        if request.json:
            input_text = request.json.get('text')
        else:
            # Fallback to form data if no JSON data is found
            input_text = request.form.get('text')
            
        system_prompt = "You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer."

        # Make the API request to the new API using gradio_client
        client = Client(url)
        result = client.predict(
            system_prompt,     # str in 'System prompt' Textbox component
    		input_text,	# str  in 'User Prompt' Textbox component
    		0.6,	# float (numeric value between 0.0 and 1.0) in 'Temperature' Slider component
    		500,	# float (numeric value between 10 and 1548) in 'Maximum output lenght' Slider component
    		0.9,	# float (numeric value between 0.0 and 1.0) in 'Top_P' Slider component
    		1,	# float (numeric value between 0.0 and 4.0) in 'Repetition Penalty' Slider component
            api_name="/combine"
        )

        # Assuming the result is a string response
        return jsonify({'response': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
